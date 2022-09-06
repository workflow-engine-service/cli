
import json
from typing import Dict


class WorkflowCalculator():
    __calc: Dict

    def __init__(self, calc: Dict = None) -> None:
        self.__calc = calc

    def field(self, name: str):
        self.__calc['$field'] = name
        return self

    def const(self, const):
        self.__calc['$const'] = const
        return self

    # def ifCondition(self, logic: WorkflowCalculator, then: WorkflowCalculator, elseIf: WorkflowCalculator = None):
    #     # TODO:
    #     return self

    def __str__(self) -> str:
        return json.dumps(self.__calc)
