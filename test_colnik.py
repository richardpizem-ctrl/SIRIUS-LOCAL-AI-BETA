# integration_test.py

import autonomy
import colnik_manager

def run_integration_test():
    print("=== INTEGRATION TEST: EXECUTE ===")

    req = autonomy.create_request(
        action="EXECUTE",
        target="C:/Windows/System32/cmd.exe",
        execute_type="SYSTEM_APP",
        priority="NORMAL",
        requires_confirmation=True
    )

    print("Request created by AUTONOMY:")
    print(req)
    print()

    response = colnik_manager.process_request(req)

    print("COLNIK response:")
    print(response)
    print()

    print("=== END OF TEST ===")
    return response


if __name__ == "__main__":
    run_integration_test()
