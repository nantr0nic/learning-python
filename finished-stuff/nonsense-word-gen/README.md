# Readme
## Non-Sense Word Generator </h>
#### A non-sense word generator for decoding practice.

Generates non-sense words based on consonant and vowel sounds for flashcards.
Ex: CV, VC, CCV, VCC, CVC, CCVC, CVCC, CCVCC.

The purpose of this generator is to easily create nonsense words to help students practice decoding phonemes. These words can be copies to flashcards and used as an aid in addition to "air writing" practice.

C denotes a consonant sound, V denotes a vowel sound.

For double consonant sounds (e.g. CCV, CVCC, etc.), a list of the most common combinations is used for generation. This avoids the generator producing consonant combinations like "kx", "zq", "tx" and so on. There are 3 exceptions for beginning CC words; included in the most common sounds are "scr", "spr", and "str" which are *technically* three consonant sounds but are simple and common enough to be practiced along with the other common sounds. 

There are several options that can be enabled for generation. Here is their explanation:

> Including dipthongs (for vowel sounds) such as "oi", "ow", "aw", and so on.
 -- These are dipthong sounds that can or should be introduced individually before being practiced.

> Including vowel teams (for vowel sounds) such as "ai", "ea", and "ui".
 -- These are special vowel combinations where (usually) the first vowel says its name instead of its sound. "ai" says A as in "fail", "ea" says E as in "speak".

> Include digraphs "th", "ch", and "sh" (for consonant sounds).
 -- These may be generated as a consonant sound at the beginning or end of a word. When enabled with "CC" at the beginning of a word the digraphs count as a single consonant sound. So, "throg" is a CCVC word where the digraph "th" is the first C, "r" is the second C, and so on. 
 -- These digraphs can also be generated at the end of a word, but only when there is one consonant sound at the end. Meaning VC, CVC, and CCVC can produce digraphs at the end of the words.
 -- When enabled for CCVCC words, a special list of digraphs is added to the possible CC combinations for the beginning of the word. (The lists are printed below.)

> Include "qu", "ph", and "kn".
 -- These may be generated at the beginning of a word, but only for CV, CVC, and CVCC.
 These are rare and should probably be consciously made and used by the educator. 

Below are the lists that are used for generation.

For words beginning or ending with "CC" sounds, I used a comprehensive list of the most common combinations. These lists are probably the best to practice decoding. Consonant combinations besides the ones used in this list are probably too difficult or impractical to practice (e.g. "xk", "zt", "qd", etc.)

> Beginning CC List
"bl", "cl", "fl", "gl", "pl", "sl", "sc", "sk", "sm", "sn", "sp", "st", "br", "cr", "dr", "fr", "gr", "pr", "tr", "scr", "spr", "str", "wh", "wr", "sw".

> Ending CC List
"nd", "nk", "nt", "ng", "mp", "st", "sk", "ft", "ct", "pt", "lt", "lk", "ld", "lf", "lp", "lm", "rm", "rn", "rp", "rt", "rd", "rf", "rk", "rl", "mb"

> Vowel dipthongs
"oo", "oi", "oy", "au", "augh", "aw", "oo", "ui", "ue", "ew", "ou", "ow"

> Vowel teams
"ai", "ea", "ea", "ey", "ay", "oe", "ue", "ie", "ow", "oa", "ui"

> Digraphs
"th", "ch", "sh"

> Digraphs for CCVCC words
"thr", "thw", "chr", "chl", "chw", "shd", "shg", "shk", "shr", "shl", "shv", "shw"



This is the first educational tool I've made and my first python program with a GUI! Please feel free to let me know if you have any questions, comments, suggestions, or if you find any problems -- I'd be happy to hear from you!

andy15givingup@gmail.com

----

<h>TO RUN</h>

If you're on Windows, there's an .exe file in /dist/. Or you can run the python files with the instructions below.

----------
(1) pip install -r requirements.txt

(2) GUI: python main.py
 -- or --
(2) CLI: python ns-w-gen.py
 
