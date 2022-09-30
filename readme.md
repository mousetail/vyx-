# What is this?

This is a attempt to compress vyxal code. It's a huffman tree compressor trained on 1500 Vyxal programs from [CSGE](https://codegolf.stackexchange.com).

# How good is it?

```
                 Orig       Comp       Diff       Ratio
mean            32.69      27.97      -4.72     0.9717
stdev          199.68     135.39      97.74     0.0762
min              0.00       0.00   -3680.00     0.1304
10% med          4.00       4.00      -3.00     0.8750
25% med          6.00       6.00      -1.00     0.9286
median          10.00      10.00       0.00     1.0000
75% med         20.00      19.00       0.00     1.0000
90% med         50.00      48.00       0.00     1.0000
max           6553.00    5055.00      39.00     1.3333
min mode         6.00       6.00       0.00     1.0000
max mode         6.00       6.00       0.00     1.0000
```
Saves around 4-5 bytes on average (but with huge variability), does nothing most of the time. Occasionally make the program slightly longer.

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