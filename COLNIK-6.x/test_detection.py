from detection.detection import Detection

det = Detection()

print("Test 1 — anomaly check:")
print(det.check_anomaly({"action": "DELETE", "priority": "CRITICAL"}))

print("\nTest 2 — violation check:")
print(det.check_violation({"action": "EXECUTE", "execute_type": "SYSTEM"}))
