from pythx import Client


c = Client(api_key='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI3NzIyMTEzMi0xODE1LTQxM2EtYjg0Ni02YzY2Mjk2ZmFmZmUiLCJpYXQiOjE2MzkxMTUxNDUuNTI2LCJpc3MiOiJNeXRoWCBBdXRoIFNlcnZpY2UiLCJleHAiOjE5NTQ2OTExNDUuNTA2LCJ1c2VySWQiOiI2MWIyZThiNzFmZDM5MzMxYTIxYTJlNWIifQ.oRXW6L2PIty52JMbRBji-UjrXTzCEEjJ_vOWmYRIXWw')

# submit bytecode, source files, their AST and more!
resp = c.analyze(bytecode="0xfe")

# wait for the analysis to finish
while not c.analysis_ready(resp.uuid):
    time.sleep(1)

# have all your security report data at your fingertips
for issue in c.report(resp.uuid):
    print(issue.swc_title or "Undefined", "-", issue.description_short)