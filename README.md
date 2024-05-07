# eq_apo_squish

A simple Python script to help adjust gains on Equalizer APO-style parametric EQ configuration text files (commonly seen with AutoEQ presets, etc.). Compress them gains and tailor your correction EQ effect amount to your heart's content!

It's also my first Python script, so please don't expect too much. :)

## Usage
Tested on Python 3.11, but should work on Python 3.4+ as it includes `pathlib`.

```bash
$ python eq_apo_squish.py [path_to_txt_file] [squish_amount_pct]
```

For example:
```bash
$ python eq_apo_squish.py ./mh755_to_harman.txt 50
```
Will output `./mh755_to_harman_squished_50.0_pct.txt` to the current directory with all the decibel gains in the parametric EQ filters scaled by 50%.

Note that if `input_file_name_squished_50.0_pct.txt` already exists, it will be overwritten.

## Notes
- **Preamp value calculation**: The script takes the biggest positive gain from the set of (scaled) filters and sets an opposite negative value in decibels to compensate. This could either result in excessive or insufficient attenuation in the case of overlapping PEQ bands. Please double-check and adjust the preamp value to taste.

## Changelog

### 0.0.1
First version.

## License
MIT