from workflow_engine_core import WorkflowEngine

wf = WorkflowEngine()

print("Test 1 — READ:")
print(wf.run({"request_id": "W1", "action": "READ"}))

print("\nTest 2 — DELETE:")
print(wf.run({"request_id": "W2", "action": "DELETE"}))

print("\nTest 3 — EXECUTE USER_APP:")
print(wf.run({"request_id": "W3", "action": "EXECUTE", "execute_type": "USER_APP"}))

print("\nTest 4 — EXECUTE SYSTEM:")
print(wf.run({"request_id": "W4", "action": "EXECUTE", "execute_type": "SYSTEM"}))
