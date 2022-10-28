# What is this?

This is a attempt to compress vyxal code. It's a huffman tree compressor trained on 1500 Vyxal programs from [CSGE](https://codegolf.stackexchange.com).

# How good is it?

Medium

<!-- INSERT AUTO GENERATED TABLE HERE -->

## Overall

| N=1831 | Original |  Compressed | Difference | Ratio |
| -- | -- | -- | -- | -- || mean | 30.97 | 26.12 | -4.84 | 0.92 |
| stdev | 191.10 | 131.25 | 92.76 | 0.09 |
| min | 0.00 | 0.00 | -3680.00 | 0.13 |
| 10% med | 4.00 | 3.00 | -3.00 | 0.80 |
| 25% med | 6.00 | 5.00 | -1.00 | 0.87 |
| median | 10.00 | 9.00 | -1.00 | 0.92 |
| 75% med | 19.00 | 18.00 | 0.00 | 1.00 |
| 90% med | 47.80 | 44.00 | 0.00 | 1.00 |
| max | 6553.00 | 5131.00 | 37.00 | 1.18 |
| min mode | 6.00 | 5.00 | -1.00 | 1.00 |
| max mode | 6.00 | 5.00 | -1.00 | 1.00 |

## Short programs (length < 10)

| N=908 | Original |  Compressed | Difference | Ratio |
| -- | -- | -- | -- | -- || mean | 5.66 | 5.16 | -0.50 | 0.91 |
| stdev | 2.22 | 2.15 | 0.54 | 0.11 |
| min | 0.00 | 0.00 | -2.00 | 0.50 |
| 10% med | 3.00 | 2.00 | -1.00 | 0.75 |
| 25% med | 4.00 | 3.00 | -1.00 | 0.83 |
| median | 6.00 | 5.00 | 0.00 | 1.00 |
| 75% med | 8.00 | 7.00 | 0.00 | 1.00 |
| 90% med | 9.00 | 8.00 | 0.00 | 1.00 |
| max | 9.00 | 9.00 | 1.00 | 1.12 |
| min mode | 6.00 | 5.00 | 0.00 | 1.00 |
| max mode | 6.00 | 5.00 | 0.00 | 1.00 |

## Medium programs (10 <= length < 100)

| N=843 | Original |  Compressed | Difference | Ratio |
| -- | -- | -- | -- | -- || mean | 25.17 | 23.29 | -1.88 | 0.92 |
| stdev | 18.77 | 17.59 | 2.65 | 0.06 |
| min | 10.00 | 8.00 | -25.00 | 0.69 |
| 10% med | 10.00 | 10.00 | -4.00 | 0.85 |
| 25% med | 13.00 | 12.00 | -2.00 | 0.89 |
| median | 18.00 | 16.00 | -1.00 | 0.92 |
| 75% med | 30.00 | 28.00 | -1.00 | 0.96 |
| 90% med | 52.60 | 49.00 | 0.00 | 1.00 |
| max | 99.00 | 97.00 | 7.00 | 1.18 |
| min mode | 10.00 | 10.00 | -1.00 | 1.00 |
| max mode | 10.00 | 10.00 | -1.00 | 1.00 |

## Long programs (100 <= length)

| N=80 | Original |  Compressed | Difference | Ratio |
| -- | -- | -- | -- | -- || mean | 379.29 | 293.89 | -85.40 | 0.92 |
| stdev | 843.56 | 563.87 | 438.58 | 0.15 |
| min | 102.00 | 77.00 | -3680.00 | 0.13 |
| 10% med | 120.00 | 108.00 | -85.60 | 0.77 |
| 25% med | 145.25 | 129.75 | -35.50 | 0.83 |
| median | 222.00 | 207.50 | -15.00 | 0.89 |
| 75% med | 270.75 | 268.75 | 10.50 | 1.06 |
| 90% med | 545.10 | 476.80 | 19.00 | 1.08 |
| max | 6553.00 | 5131.00 | 37.00 | 1.09 |
| min mode | 250.00 | 108.00 | 18.00 | 1.07 |
| max mode | 250.00 | 108.00 | 18.00 | 1.07 |
<!-- END AUTOGENERATED TABLE -->

Saves around 4-5 bytes on average (but with huge variability), does nothing most of the time. Occasionally make the program slightly longer. More savings for long programs but still a small average reduction even for very short programs.

# How do I run it?

## Collect your own data

If you want to collect your own data, you will need to set the `STACK_API_KEY` environment variable to your stack apps API key then remove the `if False` from `collect_data.py` and run it.

## Building a tree from the data

This depends on the `code_json.json` file created in the previous step. You could also chose to replace this with your own corpus.

You can then run `analize_data.py` to build a tree.

To visualize the tree you can use the command `dot -Tsvg graph.dot -o out.svg`. It's debatable whether this visualization is helpful.

## Use the data

The `encode_decode.py` will benchmark the encoding and produce the table like seen above. It will also make sure the enccoding is sane.

To use in your own script, use like this:

```py
from vyxμ import encode_decode

forest = encode_decode.load_forest()
encoded_string = encode_decode.bits_to_bytes(encode_decode.encode(string, forest))
```

For decoding use the same except inverse.