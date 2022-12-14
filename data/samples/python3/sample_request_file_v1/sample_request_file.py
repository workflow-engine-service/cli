
from . import setup
from fields import Fields
from lib.workflow import workflow
from states import States

from .. import settings


class sample_request_file_workFlow(workflow.Workflow):
    NAME = 'sample_request_file'
    VERSION = 1
    START_STATE = 'enter_info'
    END_STATE = 'finish'
    FIELDS = Fields()
    STATES = States

    def __init__(self) -> None:
        super().__init__(settings)
