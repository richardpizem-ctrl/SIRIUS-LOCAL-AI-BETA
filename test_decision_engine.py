from decision_engine import decide

# Test 1 — jednoduchý READ (mal by byť ALLOW)
req1 = {
    "request_id": "T2",
    "origin": "USER",
    "action": "READ",
    "target": "C:/test.txt",
    "priority": "NORMAL",
    "requires_confirmation": False,
    "timestamp": "2026-08-11T08:45:00Z",
    "payload": {}
}

print("Test 1 — READ:")
print(decide(req1))
print()

# Test 2 — DELETE bez hash (mal by byť DENY)
req2 = {
    "request_id": "T3",
    "origin": "USER",
    "action": "DELETE",
    "target": "C:/test.txt",
    "priority": "HIGH",
    "requires_confirmation": False,
    "timestamp": "2026-08-11T08:45:00Z",
    "payload": {}
}

print("Test 2 — DELETE bez hash:")
print(decide(req2))
print()

# Test 3 — EXECUTE (mal by byť REQUIRE_CONFIRMATION)
req3 = {
    "request_id": "T4",
    "origin": "USER",
    "action": "EXECUTE",
    "execute_type": "USER_APP",
    "target": "C:/app.exe",
    "priority": "CRITICAL",
    "requires_confirmation": False,
    "timestamp": "2026-08-11T08:45:00Z",
    "payload": {}
}

print("Test 3 — EXECUTE:")
print(decide(req3))
print()
