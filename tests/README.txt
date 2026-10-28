Testing

Test 1: Premium Ultrabook

- Input: budget_high, portable, long_battery
- Expected: Premium Ultrabook

Test 2: Budget Ultrabook

- Input: budget_low, office_only, portable
- Expected: Budget Ultrabook

Test 3: Gaming Laptop

- Input: gaming, budget_medium
- Expected: Midrange Gaming Laptop

Test 4: No Matching Laptop

- Input: budget_high, long_battery, creative_work, pref_os_macos, needs_ai_accel, travel_often
- Expected: No matching laptop recommendation, but specifications are suggested.

Limitations

The system can only make recommendations based on the existing rules. If the user's answers do not match any laptop recommendation rules, the system may only suggest specifications instead of a laptop.

Bonus Features

The system displays which rules fired and the conditions that caused them to fire. Users can answer "u" if they are unsure. These answers are not added as facts, so the system only makes recommendations based on known information.
