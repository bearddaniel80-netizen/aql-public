from .base import ScalarFunction
from ..registry import (
        register_function_call,
        FieldType,
        FuncType,
        SqlFunc
    ) 

@register_function_call(
        name="IS_ALPHA",
        printable=SqlFunc(
            description="Checks if field DOES NOT contain numbers, puncation, nor spaces.",
            template=[
                "SELECT IS_ALPHA(<field:str>)",
                "SELECT IS_ALPHA(<field:str>) AS generic_alias",
                "SELECT IS_ALPHA(<field:int>)",
                "SELECT IS_ALPHA(<field:int>) AS generic_alias",
            ],
            func_type=FuncType.SCALAR,
            input_type=[FieldType.TEXT,FieldType.INT],
            return_type=FieldType.BOOL,
            needs_groupby=False
        )
    )
class IsAlphaFunction(ScalarFunction):

    def __init__(self):
        self.kind = "scalar"

    def evaluate(self, value):
        return value.isalpha()