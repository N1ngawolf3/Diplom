import CoolProp.CoolProp as CP
from config import *


def to_kvalues(value):
    return round(value, 3)


s_0 = CP.PropsSI("S", "P", p_0 * 10 ** 6, "T", t_0, fluid)

h_0 = CP.PropsSI("H", "P", p_0 * 10 ** 6, "T", t_0, fluid) #
h_ks = CP.PropsSI("H", "P", p_k * 10 ** 6, "S", s_0, fluid)

