from terminal_assistant.terminal_assistant import TerminalAssistant

ta = TerminalAssistant()

print("Test 1 — allowed command:")
print(ta.check_command("dir"))

print("\nTest 2 — forbidden command:")
print(ta.check_command("format C:"))
