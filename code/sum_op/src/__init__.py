from typing import NamedTuple


def sum_op(num1: float, num2: float) -> NamedTuple("Outputs", [("output", float)]):
    from src.core import Adder
    
    obj = Adder()
    out = obj(num1, num2)
    
    return (out, )