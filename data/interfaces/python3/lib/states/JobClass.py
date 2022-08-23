
import json
from typing import Dict, Literal, Optional


class WorkflowStateJob():
    __id: str
    __repeat: int
    __time: Dict
    __set_fields: Dict
    __action_name: str
    __state_name: str

    def __init__(self, id: Optional[str], repeat: Optional[int], action_name: Optional[str], state_name: Optional[str]):
        self.__id = id
        self.__repeat = repeat
        self.__action_name = action_name
        self.__state_name = state_name

        return None

    def time(self, timestamp: Optional[int], timestamp_field: Optional[str], hour: Optional[int], minute: Optional[int], second: Optional[int], day: Optional[int]):
        self.__time = {}
        if timestamp is not None:
            self.__time['timestamp'] = timestamp
        if timestamp_field is not None:
            self.__time['timestamp_field'] = timestamp_field
        if day is not None:
            self.__time['day'] = day
        if hour is not None:
            self.__time['hour'] = hour
        if minute is not None:
            self.__time['minute'] = minute
        if second is not None:
            self.__time['second'] = second

        return self

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
