# runtime5_cli.py

from runtime5 import SystemAgent5

def main():
    agent = SystemAgent5()

    print("SystemAgent5 CLI — type 'exit' to quit.")
    while True:
        text = input("\n> ")
        if text.strip().lower() in ("exit", "quit"):
            break

        response = agent.handle_request(text)

        print("\n=== INPUT ===")
        print(response["input"])

        print("\n=== REASONING ===")
        print(response["reasoning"])

        print("\n=== WORKFLOW ===")
        print(response["workflow"])

if __name__ == "__main__":
    main()
