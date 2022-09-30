import json
import collections
import math
import unicodedata

# vyxal_characters = 'Jk\xaf\u01d4\u1e03\u0226"2=%/\u1e44\u2026\xa3D\u1e8bY.\u207dqG\u207c\u1e0a\u1e61\u27c7^\xa8o\u221e\u2080Ty\u1e8a\xdfP\u03c4\u022fFM\xbe\u1e0b\u0192\u20813U\xb99\u2085#\u010a\u0281N\u21b3)Ez\u017b\u2264\xa5\u2105i]\U0001f36a\u27e8\xa6\u230a\u2229\u01cd5\u25a1\ua60d\u2248\xf0\u027d\u1e87W\u1e8f\u01d38\u2087X!\u1e58\u019b\u03b5\u0256\u1e22\u0d9ee\u2021\u2206\u01ce|js\xbc?\u2227\u1e45\xa1<[w:\u1e6a{t`n;\xb6\u2193\u1e6b\u226cu\u01d0&\u20ac\xa4\xbd\u2237\u2088\xac\u01d2\u0140\u03bb\u2022\xa2av\xa74\u2083\u1e86\u2191l$>g\u2082\u2234\u01211\u1e60\u21e9\xb1\xb0C\xde\u0280\u1e1f\u0117\u017c\u022e\xb2\u27e9\u1e02S\u22cf\u03a0}\u208c\\\u21e7\u201f\u0227Q\u2228Z@\xb5\u22600\u2310B\u204b\u1e1e\u2070~7\u2308\u010b\u2086\u0116\u208d\ua71db\u215b\u203aOr\u2194f\u1e57h\u2211\u22ced\u1e41\u027e\u22656\u20b4\u222a\u21b2I\xbbK,\u1e2d\xe6\u201b\xd7\u221a\u2084\xabp\u0130c\u01d1\u2235\'\xf8m\u1e23*\u2020R\u21b5V(L\u013f\u2192\xf7_\u201e\u1e56\u2039+x\u1e59\u1e40\u228d\u27d1\u2190H\u0120\u207aA\u03b2\u0188\u01cf-\u2424\u1e8e\u2207'

vyxal_characters = '''λƛ¬∧⟑∨⟇÷×«
»°•ß†€½∆ø↔¢⌐æʀʁɾɽÞƈ∞¨ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]`^_abcdefghijklmnopqrstuvwxyz{|}~↑↓∴∵›‹∷¤ð→←βτȧḃċḋėḟġḣḭŀṁṅȯṗṙṡṫẇẋẏż√⟨⟩‛₀₁₂₃₄₅₆₇₈¶⁋§ε¡∑¦≈µȦḂĊḊĖḞĠḢİĿṀṄȮṖṘṠṪẆẊẎŻ₌₍⁰¹²∇⌈⌊¯±₴…□↳↲⋏⋎꘍ꜝ℅≤≥≠⁼ƒɖ∪∩⊍£¥⇧⇩ǍǎǏǐǑǒǓǔ⁽‡≬⁺↵⅛¼¾Π„‟'''

special_chars = 'ø∆Þk¨⇧'

with open('code_json.json') as f:
    data = json.load(f)
print(len(data))


def get_sort_order(element, frequencies):
    if element == "END":
        return 0
    elif isinstance(element, tuple):
        return get_sort_order(element[0], frequencies)
    else:
        return sum(frequencies.values())-frequencies[element] + 1


def build_tree(frequencies):
    while len(frequencies) > 1:
        new_frequencies = frequencies.copy()
        least_two = sorted(frequencies, key=lambda i: frequencies[i])[:2]
        least_two.sort(key=lambda i: get_sort_order(i, frequencies))
        del new_frequencies[least_two[0]]
        del new_frequencies[least_two[1]]
        new_frequencies[tuple(
            least_two)] = frequencies[least_two[0]]+frequencies[least_two[1]]

        frequencies = new_frequencies
        # print(frequencies.keys())
    return next(iter(frequencies.keys()))


def escape_node(node):
    node_escaped = node
    if node == '"':
        node_escaped = '\\"'
    if node == '\\':
        node_escaped = '\\\\'
    return node_escaped


def print_tree_node(node, file, node_name, frequencies, key):
    if not isinstance(node, str):
        for index, i in enumerate(node):
            sub_node_name = print_tree_node(
                i, file, node_name+str(index), frequencies, key)
            file.write(f"    {node_name} -> {sub_node_name};\n")
        file.write(
            f"    {node_name} [label=\"{escape_node(key)+node_name[key and len(unicodedata.name(key)) or 1:]}\"]\n")

    else:
        node_escaped = escape_node(
            node) + f' ({math.log2(sum(frequencies.values())/frequencies[node]):.1f})'
        # node_escaped = node.replace("\"","\\\"")
        file.write(
            f"    {node_name} [label=\"{node_escaped}\" shape=\"box\"]\n")

        if node and node in special_chars:
            file.write(
                f"{node_name} -> {unicodedata.name(node).replace(' ', '_')} [weight=0 style=dashed]\n"
            )

    return node_name


def print_tree(tree, frequencies):
    with open('graph.dot', 'w') as f:
        f.write('digraph G {\n')
        # f.write('size="50,50"\n')
        f.write("pack=true\n")
        f.write('packMode="array1"\n')
        f.write('lwidth=2\n')

        last_graph_name = ''
        for key in tree:

            graph_name = f'luster{(key and unicodedata.name(key).replace(" ","_")) or "N"}'

            f.write(
                f'subgraph {graph_name} {{\n')
            print_tree_node(
                tree[key], f, (key and unicodedata.name(key).replace(" ", "_")) or "N", frequencies[key], key)
            f.write('}\n')

            # if last_graph_name:
            #     f.write(f'{last_graph_name} -> {graph_name};\n')
            # last_graph_name = graph_name
        f.write('}')


frequencies = {i: collections.Counter() for i in ['']+list(special_chars)}
for special_char in ['']+list(special_chars):
    for char in vyxal_characters:
        frequencies[special_char][char] += 1
        last_char = char
    frequencies[special_char]["END"] += 1


for program in data:
    last_char = ''
    for char in program or '':
        # if char == '\n':
        #    char = ' '
        if char in vyxal_characters:
            if last_char in special_chars:
                frequencies[last_char][char] += 1
            else:
                frequencies[''][char] += 1
            last_char = char
    # if last_char in special_chars:
    #     frequencies[last_char]["END"] += 1
    # else:
    #     frequencies['']['END'] += 1

# rint(frequencies)
# print(len(frequencies))


print(frequencies)
tree = {i: build_tree(frequencies[i]) for i in frequencies.keys()}
# print("tree", tree)
print_tree(tree, frequencies)

with open("tree.json", 'w', encoding='utf-8') as f:
    json.dump(tree, f)
