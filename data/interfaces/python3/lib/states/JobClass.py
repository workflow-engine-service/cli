
import json
from typing import Dict, Literal


class WorkflowStateJob():
    __id: str
    __repeat: int
    __time: Dict
    __set_fields: Dict
    __action_name: str
    __state_name: str

    def __init__(self, id: str, repeat: int, time: Dict, action_name: str, state_name: str):
        self.__id = id
        self.__repeat = repeat
        self.__time = time
        self.__action_name = action_name
        self.__state_name = state_name

        return None

    def set_fields(self, fields: Dict):
        self.__set_fields = fields
        return self

    def __str__(self) -> str:
        schema = {
            'time': self.__time,
        }
        if self.__repeat is not None:
            schema['repeat'] = self.__repeat
        if self.__id is not None:
            schema['_id'] = self.__id
        if self.__set_fields is not None:
            schema['set_fields'] = self.__set_fields
        if self.__action_name is not None:
            schema['action_name'] = self.__action_name
        if self.__state_name is not None:
            schema['state_name'] = self.__state_name

        return json.dumps(schema)
