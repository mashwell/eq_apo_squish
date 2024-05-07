# eq_apo_squish

A simple Python script to help adjust parametric EQ gains on Equalizer APO-style configuration text files (commonly seen with AutoEQ presets, etc.)

Compress them gains and tailor your correction EQ effect amount to your heart's content!

It's also my first Python script, so please set your expectations accordingly. :)

## Usage
Should work on Python 3.6+ as it requires `pathlib`. Tested on Python 3.11.

```bash
python eq_apo_squish.py [path_to_txt_file] [squish_amount_pct]
```

For example:
```bash
python eq_apo_squish.py ./mh755_to_harman.txt 50
```
Will output `./mh755_to_harman_squished_50.0_pct.txt` to the current directory with all the decibel gains in the parametric EQ filters scaled by 50%.

Note that if `input_file_name_squished_50.0_pct.txt` already exists, it will be overwritten.

## Notes
- **Preamp value calculation**: The script only adjusts the preamp value if it already exists in the original filters file, and naively scales it by the squish value. This could either result in excessive or insufficient attenuation. Please double-check and adjust the preamp value to taste.

## Changelog

### 0.0.1
First version.

### 0.0.2
Made filter input handling more tolerant of multiple spaces inside a line. (Added a second test file that showcases this format.)
Simplified preamp line matching logic.

## License
MIT