

from enum import Enum
import json
from typing import Dict, List, Literal


class FieldItemValidationBuiltInCheckType(Enum):
    # FILE_TYPE = 'file_type'
    # FILE_SIZE = 'file_size'
    EMAIL = 'email'

    def __str__(self) -> str:
        return ''


class FieldItemValidation():
    __type: str
    __value: Dict
    __error: str = None
    # builtInType = FieldItemValidationBuiltInCheckType
    __regexValue: str = None
    __apiValue: str = None

    def __init__(self, type: Literal['max_length', 'min_length', 'accept_pattern', 'reject_pattern', 'email', 'min', 'max', 'api', 'file_type', 'file_size']):
        self.__type = type

    def value(self, value):
        self.__value = value
        return self

    def error(self, error):
        self.__error = error
        return self

    def apiValue(self, value):
        self.__apiValue = value
        return self

    def regexValue(self, regex: str, flags):
        self.__regexValue = {
            regex,
            flags,
        }
        return self

    def __str__(self) -> str:
        schema = {
            'type': self.__type,
        }
        if self.__apiValue is not None:
            schema['api_value'] = self.__apiValue
        if self.__regexValue is not None:
            schema['regex_value'] = self.__regexValue
        if self.__value is not None:
            schema['value'] = self.__value
        if self.__error is not None:
            schema['error'] = self.__error

        return json.dumps(schema)


class FieldItem():
    _description = 'A Short Description about field type'
    _type: Literal['file', 'string', 'number', 'datetime', 'boolean']
    __meta: Dict = {}
    __name: str = None
    __validations: List[FieldItemValidation] = []
    __default: any

    def __init__(self, name=None, meta: Dict = {}, default=None) -> None:
        self.__meta = meta
        self.__name = name
        self.__default = default
        if self.__default is None:
            self.autoDefaultValue()
        self.__validations = []
        return None

    def autoDefaultValue(self):
        self.__default = None

    def meta(self, key: str, default):
        return self.__meta.get(key, default)

    def validation(self, _validation: FieldItemValidation):
        self.__validations.append(_validation)
        return self

    def description(self):
        return self._description

    def setName(self, name: str):
        self.__name = name

    def hasName(self):
        return self.__name is not None

    def __str__(self) -> str:
        schema = {
            'name': self.__name,
            'meta': self.__meta,
            'type': self._type,
            'validation': []
        }
        if self.__validations:
            for val in self.__validations:
                schema['validation'].append(json.loads(str(val)))

        return json.dumps(schema)


class StringField(FieldItem):
    _description = 'String field contains chars, numbers and any other chars'
    _type = 'string'

    def autoDefaultValue(self):
        return ''


class NumberField(FieldItem):
    _description = 'Number field contains just numbers'
    _type = 'number'

    def autoDefaultValue(self):
        return 0


class FileField(FieldItem):
    _description = 'File Field contains a file object'
    _type = 'file'
    # __max_file_size: int
    # __allowed_mime_types: List[str]

    def __init__(self, *args):
        super().__init__(*args)


class BooleanField(FieldItem):
    _description = 'Boolean Field contains just true or false'
    _type = 'boolean'

    def autoDefaultValue(self):
        return False


class DateTimeField(FieldItem):
    _description = 'Date Time Field get date and time'
    _type = 'datetime'
