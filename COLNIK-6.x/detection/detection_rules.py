# Detection Rules (PRE-FINAL)
# Defines what constitutes an anomaly or rule violation inside COLNIK.

DETECTION_RULES = {
    "anomalies": [
        "missing_required_folder",
        "invalid_workflow_step",
        "duplicate_entity",
        "forbidden_operation"
    ],
    "violations": {
        "KG_WRITE": ["requires_permission", "requires_validation"],
        "WORKFLOW_EXEC": ["requires_navigation", "requires_authorization"]
    }
}

