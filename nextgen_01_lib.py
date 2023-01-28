from manim import *
from nextgen_01_defs import *
from manim_fonts import *


def patient_state_icon(symb, color=BLACK):
    # with RegisterFont("Open Sans") as fonts:
    #     return Text(symb, font=fonts[0], weight=BOLD, color=color)
    return Text(symb, font="sans-serif", weight=BOLD, color=color)
