from .base import ScalarFunction
from ..registry import (
        register_function_call,
        FieldType,
        FuncType,
        SqlFunc
    ) 

@register_function_call(
        name="IS_NUMERIC",
        printable=SqlFunc(
            description="Checks text contains whole, subscript, superscript numbers or fractions.",
            template=[
                "SELECT IS_NUMERIC(<field:str>)",
                "SELECT IS_NUMERIC(<field:str>) AS generic_alias",
                "SELECT IS_NUMERIC(<field:int>)",
                "SELECT IS_NUMERIC(<field:int>) AS generic_alias",
            ],
            extra_info="Does not support decimals, negatives, nor scietific notations",
            func_type=FuncType.SCALAR,
            input_type=[FieldType.TEXT,FieldType.INT],
            return_type=FieldType.BOOL,
            needs_groupby=False
        )
    )
class IsNumericFunction(ScalarFunction):

    def __init__(self):
        self.kind = "scalar"

    def evaluate(self, value):
        return value.isnumeric()