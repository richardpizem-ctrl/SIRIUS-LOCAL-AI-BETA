from navigation.navigation import Navigation
from navigation.navigation_rules import NAVIGATION_RULES

nav = Navigation()

print("Allowed next steps from INIT:")
print(nav.get_allowed_next_steps("INIT"))

print("\nAllowed next steps from SCAN:")
print(nav.get_allowed_next_steps("SCAN"))

print("\nAllowed next steps from ANALYZE:")
print(nav.get_allowed_next_steps("ANALYZE"))
