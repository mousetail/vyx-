import json
import statistics
import typing

vyxal_characters = """λƛ¬∧⟑∨⟇÷×«
»°•ß†€½∆ø↔¢⌐æʀʁɾɽÞƈ∞¨ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]`^_abcdefghijklmnopqrstuvwxyz{|}~↑↓∴∵›‹∷¤ð→←βτȧḃċḋėḟġḣḭŀṁṅȯṗṙṡṫẇẋẏż√⟨⟩‛₀₁₂₃₄₅₆₇₈¶⁋§ε¡∑¦≈µȦḂĊḊĖḞĠḢİĿṀṄȮṖṘṠṪẆẊẎŻ₌₍⁰¹²∇⌈⌊¯±₴…□↳↲⋏⋎꘍ꜝ℅≤≥≠⁼ƒɖ∪∩⊍£¥⇧⇩ǍǎǏǐǑǒǓǔ⁽‡≬⁺↵⅛¼¾Π„‟"""  # noqa: E501


def analyze_corpus(lenghts: list[float]) -> dict[str, float]:
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


def get_original_data() -> list[str]:
    with open("code_json.json") as f:
        orignal_data = json.load(f)
    return ["".join(i for i in j[1] if i in vyxal_characters) for j in orignal_data]


def get_original_ids() -> list[int]:
    with open("code_json.json") as f:
        orignal_data = json.load(f)
    return [j[0] for j in orignal_data]


def get_forest():
    with open("tree.json") as f:
        tree = json.load(f)
    return tree


def find_in_tree(tree, char: str) -> typing.Optional[list[int]]:
    if tree == char:
        return []
    if isinstance(tree, str):
        return None

    if (a := find_in_tree(tree[0], char)) is not None:
        return [0] + a
    if (a := find_in_tree(tree[1], char)) is not None:
        return [1] + a

    return None


def find_in_forest(
    forest, char: str, last_char: str = ""
) -> typing.Optional[list[int]]:
    return find_in_tree(forest[last_char], char)


def encode(text: str, forest) -> typing.Optional[list[int]]:
    bits: list[int] = []
    last_char = ""
    for char in text:
        bits += find_in_forest(forest, char, last_char if last_char in forest else "") or []
        last_char = char
    bits += find_in_forest(forest, "END", last_char if last_char in forest else "") or []
    return bits


def decode(bits: list[int], forest) -> str:
    d = forest[""]
    out = ""
    for bit in bits:
        d = d[bit]
        if d == "END":
            return out
        elif isinstance(d, str):
            out += d
            d = forest[d if d in forest else ""]

    return out


def bits_to_bytes(bits: list[int]) -> bytes:
    out = bytearray()
    for i in range((len(bits) + 7) // 8):
        o = sum(bits[i * 8 + j] << (7 - j) for j in range(min(8, len(bits) - i * 8)))
        out.append(o)

    while len(out) > 0 and out[-1] == 0:
        del out[-1]
    return bytes(out)


def bytes_to_bits(bytes: bytes) -> list[int]:
    return [int(i) for b in bytes for i in f"{b:08b}"] + [0] * 8


def get_link(index):
    data = get_original_ids()[index]
    code = get_original_data()[index]
    return f"https: // codegolf.stackexchange.com/questions/{data}"


def gen_html_from_data(data, length, original_lengths):
    o = (
        f"| N={length} | Original |  Compressed | Difference | Ratio |\n"
        "| -- | -- | -- | -- | -- |\n"
    )

    def closest_index(i, orig):
        return min(range(len(orig)), key=lambda x: abs(orig[x]-i))

    for key in data[0].keys():
        o += f"| {key} |" + "".join(f" [{d[key]:.2f}]({get_link(closest_index(d[key], d2))}) |" for d,
                                    d2 in zip(data, original_lengths)) + "\n"

    return o


def graph_data(corpus: list[str], tree):
    corpus_coded = [bits_to_bytes(encode(i, tree) or []) for i in corpus]

    for program, coded_program in zip(corpus, corpus_coded):
        try:
            assert decode(bytes_to_bits(coded_program), tree) == program
        except ValueError as ex:
            raise ValueError(*ex.args, program, coded_program)

    original_lengths = [len(i) for i in corpus]
    compressed_lenghts = [len(i) for i in corpus_coded]
    difference_lengths = [(j - i) for i, j in zip(original_lengths, compressed_lenghts)]
    ratio_lenghts = [j/max(1, i) for i, j in zip(original_lengths, compressed_lenghts)]

    orignal_stats = analyze_corpus(original_lengths)
    compressed_stats = analyze_corpus(compressed_lenghts)
    difference_stats = analyze_corpus(difference_lengths)
    ratio_stats = analyze_corpus(ratio_lenghts)

    print(f"{len(corpus):>10}      Orig       Comp       Diff       Ratio")
    for key in orignal_stats.keys():
        print(
            f"{key:<10} {orignal_stats[key]:>10.2f} "
            f"{compressed_stats[key]:>10.2f} {difference_stats[key]:>10.2f}"
            f"{ratio_stats[key]:>10.4f}"
        )

    return gen_html_from_data(
        [orignal_stats, compressed_stats, difference_stats, ratio_stats],
        len(corpus),
        [original_lengths, compressed_lenghts, difference_lengths, ratio_lenghts]
    )


if __name__ == "__main__":
    corpus = get_original_data()
    tree = get_forest()

    o = "\n"
    o += "\n## Overall\n\n"
    print("overall")
    o += graph_data(corpus, tree)
    print()

    o += "\n## Short programs (length < 10)\n\n"
    print("Short Programs (length < 10)")
    o += graph_data([i for i in corpus if len(i) < 10], tree)
    print()
    o += "\n## Medium programs (10 <= length < 100)\n\n"
    print("Medium programs (10 <= length < 100)")
    o += graph_data([i for i in corpus if 10 <= len(i) <= 100], tree)
    print()
    o += "\n## Long programs (100 <= length)\n\n"
    print("Long programs (100 <= length)")
    o += graph_data([i for i in corpus if len(i) >= 100], tree)

    with open("readme.md", encoding="utf-8") as f:
        readme = f.read()

    start_marker = "<!-- INSERT AUTO GENERATED TABLE HERE -->"
    end_marker = "<!-- END AUTOGENERATED TABLE -->"
    start_pos = readme.index(start_marker) + len(start_marker)
    end_pos = readme.index(end_marker)

    with open("readme.md", "w", encoding="utf-8") as f:
        f.write(readme[:start_pos] + o + readme[end_pos:])
