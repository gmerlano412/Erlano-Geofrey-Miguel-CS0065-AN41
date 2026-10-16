"""
Advanced Technical Assessment: KR, RBR, and CBR
Use Case: IT Helpdesk / AI Diagnostics System
Upgrades: Object-Oriented Design, Type Hinting, Dataclasses, and Normalized Similarity Scoring.
"""

from typing import List, Dict, Any, Callable
from dataclasses import dataclass

# ==========================================
# PART 1 — Knowledge Representation (KR)
# ==========================================

@dataclass
class LaptopState:
    """Task 1A: Knowledge Base represented as a strictly typed Data Class."""
    battery_level: int       # Category: Status
    cpu_temperature: int     # Category: Temperature
    screen_is_black: bool    # Category: Status
    power_on: bool           # Category: Presence
    strange_noises: bool     # Category: Presence

    def to_dict(self) -> Dict[str, Any]:
        """Converts the object to a dictionary for engine processing."""
        return self.__dict__

# Initialize our facts
current_laptop_state = LaptopState(
    battery_level=5,
    cpu_temperature=92,
    screen_is_black=True,
    power_on=False,
    strange_noises=False
)

# ==========================================
# PART 2 — Rule-Based Reasoning (RBR)
# ==========================================

class Rule:
    """Encapsulates a single rule with a lambda/function condition and an action."""
    def __init__(self, name: str, condition: Callable[[Dict], bool], action: str):
        self.name = name
        self.condition = condition
        self.action = action

class RuleBasedEngine:
    """Task 2B: An OOP Inference Engine."""
    def __init__(self):
        self.rules: List[Rule] = []

    def add_rule(self, rule: Rule):
        self.rules.append(rule)

    def evaluate(self, facts: Dict[str, Any]) -> List[str]:
        """Task 2C: Checks each rule and returns all inferred actions."""
        triggered_actions = []
        for rule in self.rules:
            if rule.condition(facts):
                triggered_actions.append(f"[{rule.name}] {rule.action}")
        return triggered_actions

# Task 2A: Create Rules dynamically
rbr_engine = RuleBasedEngine()
rbr_engine.add_rule(Rule(
    name="DeadBatteryRule",
    condition=lambda f: not f["power_on"] and f["battery_level"] < 10,
    action="Plug in the laptop charger immediately."
))
rbr_engine.add_rule(Rule(
    name="ThermalThrottlingRule",
    condition=lambda f: f["cpu_temperature"] > 85,
    action="Critical Temp: Shut down and clean cooling fans."
))
rbr_engine.add_rule(Rule(
    name="DisplayFailureRule",
    condition=lambda f: f["power_on"] and f["screen_is_black"],
    action="Connect to an external monitor to isolate GPU/Screen failure."
))

# ==========================================
# PART 3 — Case-Based Reasoning (CBR)
# ==========================================

@dataclass
class Case:
    features: Dict[str, Any]
    solution: str

class CaseBasedEngine:
    """A modular CBR system encapsulating the 4R Cycle."""
    def __init__(self):
        self.case_base: List[Case] = []

    def load_initial_cases(self, cases: List[Dict]):
        """Task 3A: Build a Case Base."""
        for c in cases:
            self.case_base.append(Case(features=c["problem"], solution=c["solution"]))

    def retrieve_and_reuse(self, new_problem: Dict[str, Any]) -> str:
        """Task 3C: Advanced Similarity Matching (Normalized Jaccard-style Scoring)."""
        best_match = None
        highest_score = -1.0

        for case in self.case_base:
            # Calculate how many features match exactly
            matches = sum(1 for key, val in new_problem.items() 
                          if key in case.features and case.features[key] == val)
            
            # Normalize score between 0.0 and 1.0 (Percentage match)
            score = matches / len(new_problem) if len(new_problem) > 0 else 0
            
            if score > highest_score:
                highest_score = score
                best_match = case

        confidence = round(highest_score * 100, 2)
        return f"{best_match.solution} (Confidence: {confidence}%)" if best_match else "No match."

    def revise(self, suggested: str, actual_fix: str = "") -> str:
        """Task 3D: Revise Step."""
        return actual_fix if actual_fix.strip() else suggested

    def retain(self, new_problem: Dict[str, Any], final_solution: str):
        """Task 3E: Retain Step."""
        self.case_base.append(Case(features=new_problem, solution=final_solution))

# ==========================================
# MAIN EXECUTION
# ==========================================
if __name__ == "__main__":
    print("="*60)
    print(" 🛠️  PART 2: RULE-BASED REASONING (RBR) DIAGNOSTICS")
    print("="*60)
    
    facts_dict = current_laptop_state.to_dict()
    print(f"SYSTEM TELEMETRY: {facts_dict}\n")
    
    actions = rbr_engine.evaluate(facts_dict)
    print("RBR INFERRED ACTIONS:")
    if actions:
        for action in actions:
            print(f" ➔ {action}")
    else:
        print(" ➔ System Normal. No actions required.")

    print("\n" + "="*60)
    print(" 🧠 PART 3: CASE-BASED REASONING (CBR) ENGINE")
    print("="*60)
    
    # Initialize CBR Engine
    cbr_engine = CaseBasedEngine()
    initial_cases = [
        {"problem": {"power": False, "noise": False, "spill": False}, "solution": "Check wall outlet."},
        {"problem": {"power": False, "noise": True, "spill": False}, "solution": "Replace Power Supply Unit (PSU)."},
        {"problem": {"power": False, "noise": False, "spill": True}, "solution": "Liquid damage: Do not turn on. Disconnect battery."}
    ]
    cbr_engine.load_initial_cases(initial_cases)
    
    # Unstructured New Problem
    new_ticket = {"power": False, "noise": True, "spill": False}
    print(f"NEW TICKET OPENED: {new_ticket}\n")
    
    # 4R Cycle Execution
    suggestion = cbr_engine.retrieve_and_reuse(new_ticket)
    print(f"[1 & 2. RETRIEVE & REUSE] AI Suggestion: \n   ↳ {suggestion}\n")
    
    # Simulating technician finding a different root cause
    tech_notes = "PSU fan was jammed by a wire. Cleared obstruction. PSU functional."
    final_fix = cbr_engine.revise(suggestion, actual_fix=tech_notes)
    print(f"[3. REVISE] Technician Override Applied: \n   ↳ {final_fix}\n")
    
    cbr_engine.retain(new_ticket, final_fix)
    print(f"[4. RETAIN] Knowledge base updated. Total Cases: {len(cbr_engine.case_base)}")
    print("="*60)