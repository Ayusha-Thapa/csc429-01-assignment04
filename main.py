from kb_loader import load_rules
from engine import ForwardChainingEngine

KB_PATH = "kb/laptop_rules.json"

def ask(question):
    answer = input(question + " (y/n/u): ").lower()
    return answer == "y"

def collect_initial_facts():
    facts = []
    # TODO: Ask more questions to collect facts for reasoning
    if ask("Is portability important?"):
        facts.append("portable")

    if ask("Do you need long battery life?"):
        facts.append("long_battery")

    budget = input("Budget (low/medium/high): ").lower()
    facts.append("budget_" + budget)

    if ask("Do you play games?"):
        facts.append("gaming")

    if ask("Do you do creative work?"):
        facts.append("creative_work")

    if ask("Only for office work?"):
        facts.append("office_only")

    os = input("Preferred OS (windows/macos/linux): ").lower()
    facts.append("pref_os_" + os)

    if ask("Need AI acceleration?"):
        facts.append("needs_ai_accel")

    if ask("Want a large screen?"):
        facts.append("large_screen")

    if ask("Travel often?"):
        facts.append("travel_often")

    return facts

def main():
    # TODO: Load rules, create engine, assert facts, and run inference
    rules = load_rules(KB_PATH)
    engine = ForwardChainingEngine(rules)

    facts = collect_initial_facts()
    engine.assert_facts(facts)
    engine.run()

    results = engine.conclusions()

    print("\nRecommended Laptop:")
    if results["recommendations"]:
        for result in results["recommendations"]:
            print("-", result.split(":")[1].replace("_", " ").title())
    else:
        print("- No matching laptop found.")

    print("\nSuggested Specifications:")
    for result in results["specs"]:
        print("-", result.split(":")[1].replace("_", " ").title())

    print("\nRules Fired:")
    for i, step in enumerate(engine.trace, 1):
        print(f"{i}. {step['rule']}")
        print("   Because:", ", ".join(step["because"]))


if __name__ == "__main__":
    main()