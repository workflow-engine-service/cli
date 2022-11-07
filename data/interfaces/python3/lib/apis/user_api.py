from typing import Dict, Tuple

from .base_api import BaseApi


class WorkflowUserApi(BaseApi):
    def stateInfo(self, processId: str) -> Dict:
        response = self._callGETApi(
            '/workflow/state-info', {'process_id': processId})
        if response.code == 200:
            return response.body['data']
        return None

    def deleteProcess(self, id: str) -> Dict:
        response = self._callDELETEApi(
            '/workflow/delete', {'id': id})
        if response.code == 200:
            return True
        return False

    def processInfo(self, processId: str) -> Dict:
        response = self._callGETApi(
            '/workflow/process-info', {'process_id': processId})
        if response.code == 200:
            return response.body['data']
        return None

    def workerInfo(self, workerId: str) -> Dict:
        response = self._callGETApi(
            '/worker/info', {'id': workerId})
        if response.code == 200:
            return response.body['data']
        return None

    def filter(self, workflows_name: list[str] = [], processes_id: list[str] = [],
               filter_finished_processes: str = "false", state: str = None, with_fields: str = "false",
               owner_id: int = 0, page_size: int = 500, page: int = 1) -> [Dict, Dict]:
        response = self._callPOSTApi('/workflow/filter', {'workflows': workflows_name,
                                                          'processes': processes_id,
                                                          'filter_finished_processes': filter_finished_processes,
                                                          'state': state,
                                                          'with_fields': with_fields,
                                                          'owner_id': owner_id,
                                                          "page_size": page_size,
                                                          "page": page})
        if response.code == 200:
            return response.body['data'], response.body['pagination']
        return None

    def processAction(self, processId: str, state_action: str, message: str = None, fields: Dict = {}) -> Tuple[
            Dict, str]:
        """call short action with no send files

        Args:
            processId (str): _description_
            state_action (str): _description_
            message (str, optional): _description_. Defaults to None.
            fields (Dict, optional): _description_. Defaults to {}.

        Returns:
            Dict: _description_
        """
        data = {
            'process_id': processId,
            'state_action': state_action,
        }
        if message is not None:
            data['message'] = message
        # =>add fields
        req_fields = {}
        for key, value in fields.items():
            req_fields['field.' + key] = value
        data['fields'] = req_fields
        response = self._callPOSTApi(
            '/workflow/short-action', data)
        if response.code == 200:
            return (response.body['data'], None)
        return (None, response.body)
