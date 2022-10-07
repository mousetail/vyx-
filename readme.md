# What is this?

This is a attempt to compress vyxal code. It's a huffman tree compressor trained on 1500 Vyxal programs from [CSGE](https://codegolf.stackexchange.com).

# How good is it?

Medium

```
overall
      1693      Orig       Comp       Diff       Ratio
mean            32.36      27.71      -4.66    0.9722
stdev          198.46     134.57      97.14    0.0759
min              0.00       0.00   -3680.00    0.1304
10% med          4.00       4.00      -3.00    0.8750
25% med          6.00       6.00      -1.00    0.9286
median          10.00      10.00       0.00    1.0000
75% med         20.00      19.00       0.00    1.0000
90% med         50.00      48.00       0.00    1.0000
max           6553.00    5055.00      39.00    1.3333
min mode         6.00       6.00       0.00    1.0000
max mode         6.00       6.00       0.00    1.0000
None

Short Programs (length < 10)
       811      Orig       Comp       Diff       Ratio
mean             5.63       5.59      -0.05    0.9951
stdev            2.22       2.20       0.46    0.0710
min              0.00       0.00      -2.00    0.6667
10% med          3.00       3.00      -1.00    0.8889
25% med          4.00       4.00       0.00    1.0000
median           6.00       6.00       0.00    1.0000
75% med          8.00       7.00       0.00    1.0000
90% med          9.00       8.80       0.00    1.0000
max              9.00      10.00       1.00    1.3333
min mode         6.00       6.00       0.00    1.0000
max mode         6.00       6.00       0.00    1.0000
None

Medium programs (10 <= length < 100)
       803      Orig       Comp       Diff       Ratio
mean            25.20      23.85      -1.36    0.9540
stdev           18.66      17.45       2.74    0.0621
min             10.00       9.00     -24.00    0.7000
10% med         10.00      10.00      -4.00    0.8750
25% med         13.00      12.00      -2.00    0.9091
median          18.00      17.00      -1.00    0.9545
75% med         30.00      29.00       0.00    1.0000
90% med         52.60      50.00       0.00    1.0000
max             99.00      98.00       8.00    1.1818
min mode        10.00      10.00       0.00    1.0000
max mode        10.00      10.00       0.00    1.0000
None

Long programs (100 <= length)
        79      Orig       Comp       Diff       Ratio
mean           379.57     294.00     -85.57    0.9216
stdev          848.95     559.08     444.56    0.1473
min            102.00      78.00   -3680.00    0.1304
10% med        120.00     108.00     -85.00    0.7680
25% med        145.00     130.00     -33.00    0.8443
median         221.00     206.00     -14.00    0.8947
75% med        267.00     270.00      12.00    1.0642
90% med        551.00     482.00      21.00    1.0857
max           6553.00    5055.00      39.00    1.0917
min mode       250.00     108.00      21.00    0.7600
max mode       250.00     270.00      21.00    0.7600
```
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