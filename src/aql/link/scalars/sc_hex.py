from .base import ScalarFunction
from ..registry import (
        register_function_call,
        FieldType,
        FuncType,
        SqlFunc
    ) 

@register_function_call(
        name="HEX",
        printable=SqlFunc(
            description="Returns hexadecimal value.",
            template=[
                "SELECT HEX(<field:int>)",
                "SELECT HEX(<field:int>) AS generic_alias",
            ],
            func_type=FuncType.SCALAR,
            input_type=[FieldType.INT, FieldType.FLOAT, FieldType.COMPLEX],
            return_type=FieldType.TEXT,
            needs_groupby=False
        )
    )
class HexFunction(ScalarFunction):

    def __init__(self):
        self.kind = "scalar"

    def evaluate(self, value):
        return hex(value)