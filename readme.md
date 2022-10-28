# What is this?

This is a attempt to compress vyxal code. It's a huffman tree compressor trained on 1500 Vyxal programs from [CSGE](https://codegolf.stackexchange.com).

# How good is it?

Medium

<!-- INSERT AUTO GENERATED TABLE HERE -->

## Overall

| N=1831 | Original |  Compressed | Difference | Ratio |
| -- | -- | -- | -- | -- |
| mean | [31.12](https://codegolf.stackexchange.com/questions/253125) | [26.24](https://codegolf.stackexchange.com/questions/252105) | [-4.87](https://codegolf.stackexchange.com/questions/250567) | [0.92](https://codegolf.stackexchange.com/questions/229258) |
| stdev | [191.14](https://codegolf.stackexchange.com/questions/235708) | [131.28](https://codegolf.stackexchange.com/questions/235748) | [92.76](https://codegolf.stackexchange.com/questions/226832) | [0.10](https://codegolf.stackexchange.com/questions/235671) |
| min | [0.00](https://codegolf.stackexchange.com/questions/231333) | [0.00](https://codegolf.stackexchange.com/questions/231333) | [-3680.00](https://codegolf.stackexchange.com/questions/235671) | [0.00](https://codegolf.stackexchange.com/questions/231333) |
| 10% med | [4.00](https://codegolf.stackexchange.com/questions/253500) | [3.00](https://codegolf.stackexchange.com/questions/253389) | [-3.00](https://codegolf.stackexchange.com/questions/253239) | [0.80](https://codegolf.stackexchange.com/questions/253476) |
| 25% med | [6.00](https://codegolf.stackexchange.com/questions/253739) | [5.00](https://codegolf.stackexchange.com/questions/253720) | [-1.00](https://codegolf.stackexchange.com/questions/253794) | [0.87](https://codegolf.stackexchange.com/questions/251182) |
| median | [10.00](https://codegolf.stackexchange.com/questions/251056) | [9.00](https://codegolf.stackexchange.com/questions/253810) | [-1.00](https://codegolf.stackexchange.com/questions/253794) | [0.92](https://codegolf.stackexchange.com/questions/253719) |
| 75% med | [19.00](https://codegolf.stackexchange.com/questions/253068) | [18.00](https://codegolf.stackexchange.com/questions/253068) | [0.00](https://codegolf.stackexchange.com/questions/251056) | [1.00](https://codegolf.stackexchange.com/questions/251056) |
| 90% med | [48.00](https://codegolf.stackexchange.com/questions/248228) | [44.80](https://codegolf.stackexchange.com/questions/246489) | [0.00](https://codegolf.stackexchange.com/questions/251056) | [1.00](https://codegolf.stackexchange.com/questions/251056) |
| max | [6553.00](https://codegolf.stackexchange.com/questions/233768) | [5131.00](https://codegolf.stackexchange.com/questions/233768) | [37.00](https://codegolf.stackexchange.com/questions/226832) | [2.00](https://codegolf.stackexchange.com/questions/231288) |
| min mode | [6.00](https://codegolf.stackexchange.com/questions/253739) | [5.00](https://codegolf.stackexchange.com/questions/253720) | [-1.00](https://codegolf.stackexchange.com/questions/253794) | [1.00](https://codegolf.stackexchange.com/questions/251056) |
| max mode | [6.00](https://codegolf.stackexchange.com/questions/253739) | [5.00](https://codegolf.stackexchange.com/questions/253720) | [-1.00](https://codegolf.stackexchange.com/questions/253794) | [1.00](https://codegolf.stackexchange.com/questions/251056) |

## Short programs (length < 10)

| N=906 | Original |  Compressed | Difference | Ratio |
| -- | -- | -- | -- | -- |
| mean | [5.67](https://codegolf.stackexchange.com/questions/253830) | [5.17](https://codegolf.stackexchange.com/questions/253771) | [-0.49](https://codegolf.stackexchange.com/questions/251056) | [0.91](https://codegolf.stackexchange.com/questions/253739) |
| stdev | [2.20](https://codegolf.stackexchange.com/questions/253375) | [2.13](https://codegolf.stackexchange.com/questions/253395) | [0.54](https://codegolf.stackexchange.com/questions/250144) | [0.13](https://codegolf.stackexchange.com/questions/246504) |
| min | [0.00](https://codegolf.stackexchange.com/questions/246504) | [0.00](https://codegolf.stackexchange.com/questions/246504) | [-2.00](https://codegolf.stackexchange.com/questions/253490) | [0.00](https://codegolf.stackexchange.com/questions/246504) |
| 10% med | [3.00](https://codegolf.stackexchange.com/questions/253476) | [2.00](https://codegolf.stackexchange.com/questions/253395) | [-1.00](https://codegolf.stackexchange.com/questions/248543) | [0.75](https://codegolf.stackexchange.com/questions/253516) |
| 25% med | [4.00](https://codegolf.stackexchange.com/questions/253730) | [3.00](https://codegolf.stackexchange.com/questions/253516) | [-1.00](https://codegolf.stackexchange.com/questions/248543) | [0.83](https://codegolf.stackexchange.com/questions/253771) |
| median | [6.00](https://codegolf.stackexchange.com/questions/253830) | [5.00](https://codegolf.stackexchange.com/questions/253771) | [0.00](https://codegolf.stackexchange.com/questions/251056) | [1.00](https://codegolf.stackexchange.com/questions/251056) |
| 75% med | [8.00](https://codegolf.stackexchange.com/questions/248543) | [7.00](https://codegolf.stackexchange.com/questions/248543) | [0.00](https://codegolf.stackexchange.com/questions/251056) | [1.00](https://codegolf.stackexchange.com/questions/251056) |
| 90% med | [9.00](https://codegolf.stackexchange.com/questions/251056) | [8.00](https://codegolf.stackexchange.com/questions/253739) | [0.00](https://codegolf.stackexchange.com/questions/251056) | [1.00](https://codegolf.stackexchange.com/questions/251056) |
| max | [9.00](https://codegolf.stackexchange.com/questions/251056) | [9.00](https://codegolf.stackexchange.com/questions/251056) | [1.00](https://codegolf.stackexchange.com/questions/250144) | [2.00](https://codegolf.stackexchange.com/questions/246188) |
| min mode | [6.00](https://codegolf.stackexchange.com/questions/253830) | [5.00](https://codegolf.stackexchange.com/questions/253771) | [0.00](https://codegolf.stackexchange.com/questions/251056) | [1.00](https://codegolf.stackexchange.com/questions/251056) |
| max mode | [6.00](https://codegolf.stackexchange.com/questions/253830) | [5.00](https://codegolf.stackexchange.com/questions/253771) | [0.00](https://codegolf.stackexchange.com/questions/251056) | [1.00](https://codegolf.stackexchange.com/questions/251056) |

## Medium programs (10 <= length < 100)

| N=843 | Original |  Compressed | Difference | Ratio |
| -- | -- | -- | -- | -- |
| mean | [25.17](https://codegolf.stackexchange.com/questions/253131) | [23.29](https://codegolf.stackexchange.com/questions/253316) | [-1.88](https://codegolf.stackexchange.com/questions/253810) | [0.92](https://codegolf.stackexchange.com/questions/243926) |
| stdev | [18.78](https://codegolf.stackexchange.com/questions/253395) | [17.58](https://codegolf.stackexchange.com/questions/253395) | [2.65](https://codegolf.stackexchange.com/questions/251234) | [0.06](https://codegolf.stackexchange.com/questions/248682) |
| min | [10.00](https://codegolf.stackexchange.com/questions/251056) | [8.00](https://codegolf.stackexchange.com/questions/253313) | [-25.00](https://codegolf.stackexchange.com/questions/248682) | [0.69](https://codegolf.stackexchange.com/questions/248682) |
| 10% med | [10.00](https://codegolf.stackexchange.com/questions/251056) | [10.00](https://codegolf.stackexchange.com/questions/251056) | [-4.00](https://codegolf.stackexchange.com/questions/248543) | [0.85](https://codegolf.stackexchange.com/questions/253496) |
| 25% med | [13.00](https://codegolf.stackexchange.com/questions/253771) | [12.00](https://codegolf.stackexchange.com/questions/253830) | [-2.00](https://codegolf.stackexchange.com/questions/253810) | [0.89](https://codegolf.stackexchange.com/questions/253325) |
| median | [18.00](https://codegolf.stackexchange.com/questions/253158) | [16.00](https://codegolf.stackexchange.com/questions/253432) | [-1.00](https://codegolf.stackexchange.com/questions/253771) | [0.92](https://codegolf.stackexchange.com/questions/252050) |
| 75% med | [30.00](https://codegolf.stackexchange.com/questions/248435) | [28.00](https://codegolf.stackexchange.com/questions/253426) | [-1.00](https://codegolf.stackexchange.com/questions/253771) | [0.96](https://codegolf.stackexchange.com/questions/253316) |
| 90% med | [52.60](https://codegolf.stackexchange.com/questions/246510) | [49.00](https://codegolf.stackexchange.com/questions/252010) | [0.00](https://codegolf.stackexchange.com/questions/251056) | [1.00](https://codegolf.stackexchange.com/questions/251056) |
| max | [99.00](https://codegolf.stackexchange.com/questions/248999) | [97.00](https://codegolf.stackexchange.com/questions/248867) | [7.00](https://codegolf.stackexchange.com/questions/241593) | [1.18](https://codegolf.stackexchange.com/questions/247353) |
| min mode | [10.00](https://codegolf.stackexchange.com/questions/251056) | [10.00](https://codegolf.stackexchange.com/questions/251056) | [-1.00](https://codegolf.stackexchange.com/questions/253771) | [1.00](https://codegolf.stackexchange.com/questions/251056) |
| max mode | [10.00](https://codegolf.stackexchange.com/questions/251056) | [10.00](https://codegolf.stackexchange.com/questions/251056) | [-1.00](https://codegolf.stackexchange.com/questions/253771) | [1.00](https://codegolf.stackexchange.com/questions/251056) |

## Long programs (100 <= length)

| N=82 | Original |  Compressed | Difference | Ratio |
| -- | -- | -- | -- | -- |
| mean | [373.39](https://codegolf.stackexchange.com/questions/253198) | [289.45](https://codegolf.stackexchange.com/questions/253180) | [-83.94](https://codegolf.stackexchange.com/questions/248543) | [0.91](https://codegolf.stackexchange.com/questions/253738) |
| stdev | [833.94](https://codegolf.stackexchange.com/questions/253531) | [557.59](https://codegolf.stackexchange.com/questions/253338) | [433.24](https://codegolf.stackexchange.com/questions/253240) | [0.15](https://codegolf.stackexchange.com/questions/253338) |
| min | [102.00](https://codegolf.stackexchange.com/questions/253268) | [77.00](https://codegolf.stackexchange.com/questions/253537) | [-3680.00](https://codegolf.stackexchange.com/questions/253338) | [0.13](https://codegolf.stackexchange.com/questions/253338) |
| 10% med | [117.90](https://codegolf.stackexchange.com/questions/253738) | [108.00](https://codegolf.stackexchange.com/questions/253738) | [-84.80](https://codegolf.stackexchange.com/questions/253179) | [0.76](https://codegolf.stackexchange.com/questions/253420) |
| 25% med | [144.00](https://codegolf.stackexchange.com/questions/220138) | [128.00](https://codegolf.stackexchange.com/questions/253730) | [-36.25](https://codegolf.stackexchange.com/questions/253717) | [0.82](https://codegolf.stackexchange.com/questions/253191) |
| median | [220.00](https://codegolf.stackexchange.com/questions/253395) | [201.00](https://codegolf.stackexchange.com/questions/253517) | [-15.00](https://codegolf.stackexchange.com/questions/253154) | [0.89](https://codegolf.stackexchange.com/questions/253503) |
| 75% med | [268.25](https://codegolf.stackexchange.com/questions/253194) | [268.25](https://codegolf.stackexchange.com/questions/253496) | [9.50](https://codegolf.stackexchange.com/questions/253810) | [1.05](https://codegolf.stackexchange.com/questions/253720) |
| 90% med | [533.30](https://codegolf.stackexchange.com/questions/253133) | [470.40](https://codegolf.stackexchange.com/questions/253240) | [19.00](https://codegolf.stackexchange.com/questions/253432) | [1.08](https://codegolf.stackexchange.com/questions/253395) |
| max | [6553.00](https://codegolf.stackexchange.com/questions/253333) | [5131.00](https://codegolf.stackexchange.com/questions/253333) | [37.00](https://codegolf.stackexchange.com/questions/253240) | [1.09](https://codegolf.stackexchange.com/questions/253313) |
| min mode | [250.00](https://codegolf.stackexchange.com/questions/253496) | [108.00](https://codegolf.stackexchange.com/questions/253738) | [18.00](https://codegolf.stackexchange.com/questions/253720) | [0.92](https://codegolf.stackexchange.com/questions/253738) |
| max mode | [250.00](https://codegolf.stackexchange.com/questions/253496) | [108.00](https://codegolf.stackexchange.com/questions/253738) | [18.00](https://codegolf.stackexchange.com/questions/253720) | [1.07](https://codegolf.stackexchange.com/questions/253496) |
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