from dataclasses import dataclass
from typing import List, Set, Dict, Any

@dataclass
class Rule:
    antecedents: List[str]
    consequent: str
    priority: int = 0
    name: str = ""

class ForwardChainingEngine:
    def __init__(self, rules: List[Rule]):
        self.rules = rules
        self.facts: Set[str] = set()
        self.trace: List[Dict[str, Any]] = []

    def assert_facts(self, initial: List[str]) -> None:
        """Store initial facts into the working memory."""
        self.facts.update(initial)

    def can_fire(self, rule: Rule) -> bool:
        """TODO: Return True if all antecedents are true and consequent not yet known."""
        return (all(fact in self.facts for fact in rule.antecedents)
                and rule.consequent not in self.facts)


    def run(self) -> None:
        """TODO: Implement the forward chaining loop."""
        # while there are rules that can fire:
        #     select one rule (students decide tie-breaking)
        #     add its consequent to facts
        #     record in trace
        while True:
            possible = [rule for rule in self.rules
                        if self.can_fire(rule)]

            if not possible:
                break

            rule = possible[0]  # Simple tie-breaking: select the first available rule
            self.facts.add(rule.consequent)

            self.trace.append({
                "rule": rule.name,
                "conclusion": rule.consequent,
                "because": rule.antecedents
            })
      
    def conclusions(self) -> Dict[str, List[str]]:
        return {
            "recommendations": sorted(f for f in self.facts
                                    if f.startswith("recommend:")),
            "specs": sorted(f for f in self.facts
                            if f.startswith("spec:")),
            "other": sorted(f for f in self.facts
                            if not f.startswith(("recommend:", "spec:")))
        }