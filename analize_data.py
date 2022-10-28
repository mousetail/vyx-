import collections
import json
import math
import typing
import unicodedata

vyxal_characters = """λƛ¬∧⟑∨⟇÷×«
»°•ß†€½∆ø↔¢⌐æʀʁɾɽÞƈ∞¨ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]`^_abcdefghijklmnopqrstuvwxyz{|}~↑↓∴∵›‹∷¤ð→←βτȧḃċḋėḟġḣḭŀṁṅȯṗṙṡṫẇẋẏż√⟨⟩‛₀₁₂₃₄₅₆₇₈¶⁋§ε¡∑¦≈µȦḂĊḊĖḞĠḢİĿṀṄȮṖṘṠṪẆẊẎŻ₌₍⁰¹²∇⌈⌊¯±₴…□↳↲⋏⋎꘍ꜝ℅≤≥≠⁼ƒɖ∪∩⊍£¥⇧⇩ǍǎǏǐǑǒǓǔ⁽‡≬⁺↵⅛¼¾Π„‟"""  # noqa: E501

special_chars = "ø∆Þk¨⇧"

with open("code_json.json") as f:
    data = json.load(f)
print(len(data))

Tree = typing.Union[str, tuple["Tree", "Tree"]]


def get_sort_order(element: Tree, last_letter_frequencies: dict[str, int]) -> int:
    if element == "END":
        return 0
    elif isinstance(element, tuple):
        return get_sort_order(element[0], last_letter_frequencies)
    else:
        return sum(last_letter_frequencies.values()) - last_letter_frequencies[element] + 1


def build_tree(frequencies: dict[str, int], last_letter_frequencies: dict[str, int]) -> Tree:
    while len(frequencies) > 1:
        new_frequencies = frequencies.copy()
        least_two = sorted(frequencies, key=lambda i: frequencies[i])[:2]
        least_two.sort(key=lambda i: get_sort_order(i, last_letter_frequencies))
        del new_frequencies[least_two[0]]
        del new_frequencies[least_two[1]]
        new_frequencies[tuple(least_two)] = (
            frequencies[least_two[0]] + frequencies[least_two[1]]
        )

        frequencies = new_frequencies
        # print(frequencies.keys())
    return typing.cast(Tree, next(iter(frequencies.keys())))


def escape_node(node: str) -> str:
    node_escaped = node
    if node == '"':
        node_escaped = '\\"'
    if node == "\\":
        node_escaped = "\\\\"
    return node_escaped


def print_tree_node(
    node: Tree, file: typing.IO, node_name: str, frequencies: dict[str, int], key: str
):
    if not isinstance(node, str):
        for index, i in enumerate(node):
            sub_node_name = print_tree_node(
                i, file, node_name + str(index), frequencies, key
            )
            file.write(f"    {node_name} -> {sub_node_name};\n")
        file.write(
            f'    {node_name} [label="{escape_node(key)+node_name[key and len(unicodedata.name(key)) or 1:]}"]\n'
        )

    else:
        node_escaped = (
            escape_node(node)
            + f" ({math.log2(sum(frequencies.values())/frequencies[node]):.1f})"
        )
        # node_escaped = node.replace("\"","\\\"")
        file.write(f'    {node_name} [label="{node_escaped}" shape="box"]\n')

        if node and node in special_chars:
            file.write(
                f"{node_name} -> {unicodedata.name(node).replace(' ', '_')} [weight=0 style=dashed]\n"
            )

    return node_name


def print_tree(tree: dict[str, Tree], frequencies: dict[str, dict[str, int]]):
    with open("graph.dot", "w") as f:
        f.write("digraph G {\n")
        # f.write('size="50,50"\n')
        f.write("pack=true\n")
        f.write('packMode="array1"\n')
        f.write("lwidth=2\n")

        for key in tree:

            graph_name = (
                f'luster{(key and unicodedata.name(key).replace(" ","_")) or "N"}'
            )

            f.write(f"subgraph {graph_name} {{\n")
            print_tree_node(
                tree[key],
                f,
                (key and unicodedata.name(key).replace(" ", "_")) or "N",
                frequencies[key],
                key,
            )
            f.write("}\n")
        f.write("}")


frequencies = {i: collections.Counter() for i in [""] + list(special_chars)}
last_letter_frequencies = collections.Counter()
for special_char in [""] + list(special_chars):
    for char in vyxal_characters:
        frequencies[special_char][char] += 1
        last_char = char
    frequencies[special_char]["END"] += 1


for program in data:
    last_char = ""
    for char in program or "":
        # if char == '\n':
        #    char = ' '
        if char in vyxal_characters:
            if last_char in special_chars:
                frequencies[last_char][char] += 1
            else:
                frequencies[""][char] += 1
            last_char = char
    if last_char:
        last_letter_frequencies[last_char] += 1
    # if last_char in special_chars:
    #     frequencies[last_char]["END"] += 1
    # else:
    #     frequencies['']['END'] += 1

# rint(frequencies)
# print(len(frequencies))


print(frequencies)
tree = {i: build_tree(frequencies[i], last_letter_frequencies) for i in frequencies.keys()}
# print("tree", tree)
print_tree(tree, frequencies)

with open("tree.json", "w", encoding="utf-8") as f:
    json.dump(tree, f)
