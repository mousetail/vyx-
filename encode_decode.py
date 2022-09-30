import statistics
import json

vyxal_characters = '''λƛ¬∧⟑∨⟇÷×«
»°•ß†€½∆ø↔¢⌐æʀʁɾɽÞƈ∞¨ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]`^_abcdefghijklmnopqrstuvwxyz{|}~↑↓∴∵›‹∷¤ð→←βτȧḃċḋėḟġḣḭŀṁṅȯṗṙṡṫẇẋẏż√⟨⟩‛₀₁₂₃₄₅₆₇₈¶⁋§ε¡∑¦≈µȦḂĊḊĖḞĠḢİĿṀṄȮṖṘṠṪẆẊẎŻ₌₍⁰¹²∇⌈⌊¯±₴…□↳↲⋏⋎꘍ꜝ℅≤≥≠⁼ƒɖ∪∩⊍£¥⇧⇩ǍǎǏǐǑǒǓǔ⁽‡≬⁺↵⅛¼¾Π„‟'''


def analyze_corpus(lenghts):
    return {
        "mean": statistics.mean(lenghts),
        "stdev": statistics.stdev(lenghts),
        "min": min(lenghts),
        "10% med": statistics.quantiles(lenghts, n=10)[0],
        "25% med": statistics.quantiles(lenghts)[0],
        "median": statistics.median(lenghts),
        "75% med": statistics.quantiles(lenghts)[2],
        "90% med": statistics.quantiles(lenghts, n=10)[8],
        "max": max(lenghts),
        "min mode": min(statistics.multimode(lenghts)),
        "max mode": max(statistics.multimode(lenghts)),
    }


def get_original_data():
    with open("code_json.json") as f:
        orignal_data = json.load(f)
    return [''.join(i for i in j if i in vyxal_characters) for j in orignal_data]


def get_forest():
    with open("tree.json") as f:
        tree = json.load(f)
    return tree


def find_in_tree(tree, char):
    if tree == char:
        return []
    if isinstance(tree, str):
        return None

    if (a := find_in_tree(tree[0], char)) is not None:
        return [0] + a
    if (a := find_in_tree(tree[1], char)) is not None:
        return [1] + a

    return None


def find_in_forest(forest, char, last_char=''):
    return find_in_tree(forest[last_char], char)


def encode(text, forest):
    bits = []
    last_char = ''
    for char in text:
        bits += find_in_forest(forest, char,
                               last_char if last_char in forest else '')
        last_char = char
    bits += find_in_forest(forest, "END",
                           last_char if last_char in forest else '')
    return bits


def decode(bits, forest):
    d = forest['']
    out = ""
    for bit in bits:
        d = d[bit]
        if d == "END":
            return out
        elif isinstance(d, str):
            out += d
            d = forest[d if d in forest else '']
    # if d not in forest.values():
    #    raise ValueError(f"half character left over: {bits=} {out=} {d=}")
    return out


def bits_to_bytes(bits):
    out = bytearray()
    for i in range((len(bits)+7)//8):
        o = sum(bits[i*8+j] << (7-j) for j in range(min(8, len(bits)-i*8)))
        out.append(o)

    while len(out) > 0 and out[-1] == 0:
        del out[-1]
    return bytes(out)


def bytes_to_bits(bytes):
    return [int(i) for b in bytes for i in f'{b:08b}'] + [0]*8


if __name__ == "__main__":
    corpus = get_original_data()
    tree = get_forest()
    corpus_coded = [bits_to_bytes(encode(i, tree)) for i in corpus]

    print(bits_to_bytes(encode("₁ƛ₍₃₅kF½*∑∴", tree)))
    exit()

    for program, coded_program in zip(corpus, corpus_coded):
        try:
            assert decode(bytes_to_bits(coded_program), tree) == program
        except ValueError as ex:
            raise ValueError(*ex.args, program, coded_program)

    orignal_stats = analyze_corpus([len(i) for i in corpus])
    compressed_stats = analyze_corpus([len(i) for i in corpus_coded])
    difference = analyze_corpus(
        [len(j)-len(i) for i, j in zip(corpus, corpus_coded)])
    ratio = analyze_corpus(
        [len(j)/max(1, len(i)) for i, j in zip(corpus, corpus_coded) if len(j) > 0])

    print("                 Orig       Comp       Diff       Ratio")
    for key in orignal_stats.keys():
        print(
            f"{key:<10} {orignal_stats[key]:>10.2f} {compressed_stats[key]:>10.2f} {difference[key]:>10.2f} {ratio[key]:>10.4f}")
