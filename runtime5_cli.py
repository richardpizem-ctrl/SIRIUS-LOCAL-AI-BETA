# runtime5_cli.py

from runtime5 import Runtime5, KnowledgeGraph
from runtime5.kg_loader import KnowledgeGraphLoader

def main():
    kg = KnowledgeGraph()
    loader = KnowledgeGraphLoader(kg)
    loader.load_minimal_test_data()

    rt = Runtime5(kg)

    print("Runtime 5.x CLI — type 'exit' to quit.")
    while True:
        text = input("\n> ")
        if text.strip().lower() in ("exit", "quit"):
            break

        output = rt.process(text)
        print("\n[REASONING]:", output["reasoning"])
        print("[WORKFLOW ]:", output["workflow"])

if __name__ == "__main__":
    main()
