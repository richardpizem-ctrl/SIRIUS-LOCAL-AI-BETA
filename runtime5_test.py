# runtime5_test.py

from runtime5 import Runtime5, KnowledgeGraph

# Create empty KG for test
kg = KnowledgeGraph()

# Create runtime
rt = Runtime5(kg)

# Test input
text = "what is test"

output = rt.process(text)

print("=== REASONING OUTPUT ===")
print(output["reasoning"])

print("\n=== WORKFLOW OUTPUT ===")
print(output["workflow"])
