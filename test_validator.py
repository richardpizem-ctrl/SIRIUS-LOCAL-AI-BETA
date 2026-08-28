import validator

req = {
    "request_id": "T1",
    "origin": "USER",
    "action": "READ",
    "target": "C:/test.txt",
    "priority": "NORMAL",
    "requires_confirmation": False,
    "timestamp": "2026-08-11T08:45:00Z",
    "payload": {}
}

print("Validator result:")
print(validator.validate_request(req))
