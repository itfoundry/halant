# Halant

Halant is an open source family of fonts supporting both Devanagari and Latin. This typeface design is well-suited for setting long continuous texts. The Halant family includes five weights, from Light through Bold. Each font has 928 glyphs, including all of the unique conjunct forms necessary for Indian languages like Hindi, Marathi, Nepali, etc.

The shape of the Devanagari characters in the Halant fonts are traditional in appearance — they are based on writing and calligraphic principles – which significantly aids their readability. Most of the counters are open (e.g., Ka, Tha, Ba, Va and Sha), while the knots are closed (e.g., Ga, Jha, Da and Na). The height of Halant’s matras is modest; they do not take up too much vertical space.

Halant’s Latin characters are drawn with a low stroke contrast. This part of the typeface is a traditional European serif in style, with diagonal stress and general Renaissance proportions. The lowercase letters have a tall x-height. The Devanagari base glyph height straddles the Latin cap-height, and the Latin ascenders reach slightly above the Devanagari headline. Halant’s Latin ascender serifs are visibly higher than this.

The Devanagari glyphs in the Halant project were designed by Vivek Sadamate and Ninad Kale. The Latin is by Jonny Pinhorn. The Indian Type Foundry first published Halant in 2014.

## Code base

This working directory is forked from the common code base, [ITF Base Devanagari (for Google Fonts)](https://github.com/itfoundry/base-devanagari-gf).

## Dependencies

- [Adobe Font Development Kit for OpenType](http://www.adobe.com/devnet/opentype/afdko.html) (AFDKO), version 2.5 build 63209 (Sep 18 2014) or newer.
- A script [`UFOInstanceGenerator.py`](https://github.com/adobe-type-tools/python-scripts/blob/master/FDK%20Extras/UFOInstanceGenerator.py) (to be placed in AFDKO’s directory `FDK/Tools/osx`) and two [modules](https://github.com/adobe-type-tools/python-modules) (to be placed in Python’s `site-packages` directory) from Adobe.
