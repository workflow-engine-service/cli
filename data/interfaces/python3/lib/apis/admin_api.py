
from typing import Dict, List, Tuple
from .base_api import BaseApi


class WorkflowAdminApi(BaseApi):

    def workflows(self):
        # TODO:
        pass

    def deployWorkflow(self, code: Dict) -> Tuple[bool, str]:
        response = self._callPOSTApi('/admin/workflow/deploy', {'code': code})
        # print('response deploy:', response, code)
        if response.code == 200:
            return True, 'success'
        return False, response.body['data']

    def createWorkflowProcess(self, name: str, version: int = None, owner_id: int = None) -> Tuple[bool, str]:
        data = {'name': name}
        if version is not None:
            data['version'] = version
        if owner_id is not None:
            data['owner_id'] = owner_id

        response = self._callPOSTApi(
            '/workflow/create', data)
        # print('response deploy:', response)
        if response.code == 200:
            return True, response.body['data']
        return False, response.body['data']

    def setFields(self, process_id: str, fields: Dict) -> Tuple[bool, str]:
        response = self._callPOSTApi('/admin/workflow/set-fields', {
            'process_id': process_id,
            'fields': fields
        })
        print(response.body)
        if response.code == 200:
            return True, 'success'
        return False, response.body['data']