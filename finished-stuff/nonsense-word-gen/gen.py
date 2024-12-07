import random

c_list = "bcdfghjklmnpqrstvwxyz"
v_list = "aeiou"
front_cc_list = [
    "bl",
    "cl",
    "fl",
    "gl",
    "pl",
    "sl",
    "sc",
    "sk",
    "sm",
    "sn",
    "sp",
    "st",
    "br",
    "cr",
    "dr",
    "fr",
    "gr",
    "pr",
    "tr",
    "scr",
    "spr",
    "str",
    "wh",
    "wr",
    "sw",
]
end_cc_list = [
    "nd",
    "nk",
    "nt",
    "ng",
    "mp",
    "st",
    "sk",
    "ft",
    "ct",
    "pt",
    "lt",
    "lk",
    "ld",
    "lf",
    "lp",
    "lm",
    "rm",
    "rn",
    "rp",
    "rt",
    "rd",
    "rf",
    "rk",
    "rl",
    "mb",
]
v_dips = ["oo", "oi", "oy", "au", "augh", "aw", "oo", "ui", "ue", "ew", "ou", "ow"]
v_teams = ["ai", "ea", "ea", "ey", "ay", "oe", "ue", "ie", "ow", "oa", "ui"]
c_digraphs = ["th", "sh", "ch"]
c_digraphs_special = [
    "thr", "thw", 
    "chr", "chl", "chw", 
    "shd", "shg", "shk", "shr", "shl", "shv", "shw", 
]
c_digraphs_2 = ["qu", "ph", "kn"]


class Sounds:
    """Class for generating sounds in non-sense words."""

    def __init__(self):
        pass

    def get_c(self, c=0, c_2=0):
        """Picks a random consonant, with the option of "th, sh, ch"."""
        c_options = [c_list]
        if c == 1:
            c_options.append(c_digraphs)
        if c_2 == 1:
            c_options.append(c_digraphs_2)
        consonant = random.choice(c_options)
        return random.choice(consonant)

    def get_v(self, d=0, t=0):
        """Picks a random vowel, with the option of vowel teams and/or dipthongs."""
        v_options = [v_list]
        if d == 1:
            v_options.append(v_dips)
        if t == 1:
            v_options.append(v_teams)
        vowel = random.choice(v_options)
        return random.choice(vowel)

    def get_front_cc(self):
        """Picks a random combination of two beginning consonant sounds from a list of common occurences."""
        return random.choice(front_cc_list)

    def get_end_cc(self):
        """Picks a random combination of two ending consonant sounds from a list of common occurences."""
        return random.choice(end_cc_list)

    def cv(self, d=0, t=0, c=0, c_2=0):
        """Generates a consonant + a vowel."""
        return f"{self.get_c(c, c_2)}{self.get_v(d, t)}"

    def vc(self, d=0, t=0, c=0, c_2=0):
        """Generates a vowel + a consonant."""
        return f"{self.get_v(d, t)}{self.get_c(c, c_2=0)}"

    def ccv(self, d=0, t=0, c=0, c_2=0):
        """Generates a combination of two consonants and a vowel."""
        return f"{self.get_front_cc()}{self.get_v(d, t)}"

    def vcc(self, d=0, t=0, c=0, c_2=0):
        """Generates a combination of a vowel and a common consonant combination."""
        return f"{self.get_v(d, t)}{self.get_end_cc()}"

    def cvc(self, d=0, t=0, c=0, c_2=0):
        """Generates a combination of a consonant, a vowel, and a consonant."""
        return f"{self.get_c(c, c_2)}{self.get_v(d, t)}{self.get_c(c, c_2=0)}"

    def ccvc(self, d=0, t=0, c=0, c_2=0):
        """Generates a combination of a common double consonant sound, a vowel, and an ending consonant."""
        return f"{self.get_front_cc()}{self.get_v(d, t)}{self.get_c(c, c_2=0)}"

    def cvcc(self, d=0, t=0, c=0, c_2=0):
        """Generates a consonant, a vowel, and a common double consonant ending sound."""
        return f"{self.get_c(c, c_2)}{self.get_v(d, t)}{self.get_end_cc()}"

    def ccvcc(self, d=0, t=0, c=0, c_2=0):
        """Generates a common double consonant sound, a vowel, and a common double consonant ending sound."""
        if c == 1:
            # Special case. Includes common CC's and first list of digraphs.
            cc_digs = front_cc_list + c_digraphs_special
            cc = random.choice(cc_digs)
            return f"{cc}{self.get_v(d, t)}{self.get_end_cc()}"
        else:
            return f"{self.get_front_cc()}{self.get_v(d, t)}{self.get_end_cc()}"
