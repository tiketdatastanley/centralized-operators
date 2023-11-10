from typing import NamedTuple


def multiply_op(num1: float, num2: float) -> NamedTuple("Outputs", [("output", float)]):
    from src.core import Multiplier
    
    obj = Multipler()
    out = obj(num1, num2)
    
    return (out, )