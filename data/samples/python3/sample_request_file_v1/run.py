import time

from .sample_request_file import sample_request_file_workFlow

print('[+] init workflow class')
sample_workFlow = sample_request_file_workFlow()
print(sample_workFlow)
# deploy workflow
print('[+] deploy workflow schema')
print(sample_workFlow.deploy())
# create new process
print('[+] create workflow process')
newProcess, message = sample_workFlow.create()
# print(newProcess)
print('[+] get current state of process')
# get current state info
state = newProcess.currentState()
print(state)
