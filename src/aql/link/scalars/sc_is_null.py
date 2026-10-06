from .base import ScalarFunction
from ..registry import (
        register_function_call,
        FieldType,
        FuncType,
        SqlFunc
    ) 

@register_function_call(
        name="IS_NULL",
        printable=SqlFunc(
            description="Checks is null.",
            template=[
                "SELECT IS_NULL(<field:int>)",
                "SELECT IS_NULL(<field:str>)",
                "SELECT IS_NULL(<field:int>) AS generic_alias",
                "SELECT IS_NULL(<field:str>) AS generic_alias",
            ],
            func_type=FuncType.SCALAR,
            input_type=[FieldType.STR,FieldType.INT],
            return_type=FieldType.BOOL,
            needs_groupby=False
        )
    )
class IsNullFunction(ScalarFunction):

    def __init__(self):
        self.kind = "scalar"

    def evaluate(self, value):
        if value:
            return True
        return False