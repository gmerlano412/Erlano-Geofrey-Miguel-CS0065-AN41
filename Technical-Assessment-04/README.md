## What is this?
This repository contains a Python-based **Advanced Technical Assessment** demonstrating foundational Artificial Intelligence reasoning techniques. It implements a simulated **IT Helpdesk / AI Diagnostics System** designed to diagnose hardware issues (like laptop failures) using three distinct AI methodologies:

1. **Knowledge Representation (KR):** Structuring system telemetry using Object-Oriented Design (OOP), Python `dataclasses`, and strict type hinting.
2. **Rule-Based Reasoning (RBR):** A deterministic inference engine that evaluates a list of dynamic rules (using lambda functions) against real-time system facts to trigger specific diagnostic actions.
3. **Case-Based Reasoning (CBR):** A machine learning approach that solves new problems based on the solutions of similar past problems, fully implementing the **4R Cycle** (Retrieve, Reuse, Revise, Retain) with normalized similarity scoring.

This project is built using pure standard Python—no external machine learning libraries are required. It serves as an educational framework for understanding how expert systems process information and learn over time.

---

## How it works

### Prerequisites
* **Python 3.7+** (Required for `@dataclass` and `typing` module support).
* No external dependencies (`pip install` is not needed).

### Running the Code
Save the script as `diagnostics.py` and run it via your terminal:
```bash
python diagnostics.py
```

### System Architecture Workflow
When you execute the script, it runs through two main diagnostic phases:

#### 1. The RBR Phase (Real-Time Telemetry)
* **Ingestion:** The system loads a `LaptopState` dataclass containing current telemetry (e.g., 92°C CPU, 5% battery, black screen).
* **Evaluation:** The `RuleBasedEngine` evaluates these facts against predefined conditions.
* **Output:** It dynamically triggers alerts, such as warning the user to plug in the charger and critically shutting down due to thermal throttling.

#### 2. The CBR Phase (Historical Helpdesk Tickets)
* **Initialize Base:** The `CaseBasedEngine` loads a historical database of previous IT tickets.
* **Retrieve & Reuse:** A new, unstructured ticket arrives (`power: False, noise: True`). The engine calculates a similarity score against past cases and suggests a fix (e.g., "Replace PSU").
* **Revise & Retain:** A human technician overrides the AI's suggestion with a specific fix ("PSU fan was jammed..."). The system learns from this by appending the new problem-solution pair back into its knowledge base.
