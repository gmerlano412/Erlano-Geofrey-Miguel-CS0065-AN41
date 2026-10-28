# AI Diagnostics System: KR, RBR, and CBR

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

---

## Questions about this code

**Q: How does the similarity scoring work in the CBR module?**
The engine uses a Normalized Similarity Score (a simplified Jaccard-style index). It iterates through the historical `case_base`, counts how many key-value pairs in the new problem perfectly match the historical case, and divides that by the total number of features in the new problem. This produces a confidence percentage from 0% to 100%.

**Q: Why use `@dataclass` for Knowledge Representation?**
Using `@dataclass` automatically generates boilerplate code like `__init__` and `__repr__`, making the code cleaner. Combined with type hints (`int`, `bool`), it strictly enforces the schema of our knowledge base, ensuring the RBR engine doesn't crash from unexpected data types. The `.to_dict()` method acts as a bridge, cleanly formatting the object for the lambda-based rule engine.

**Q: What is the "4R Cycle" in the CBR engine?**
The 4R cycle is the standard operational loop of Case-Based Reasoning:
1. **Retrieve:** Find the most similar past case (`retrieve_and_reuse`).
2. **Reuse:** Suggest the historical solution for the new problem (`retrieve_and_reuse`).
3. **Revise:** Adapt or correct the suggested solution based on human input or real-world execution (`revise`).
4. **Retain:** Save the newly solved problem back into the database to improve future accuracy (`retain`).

**Q: Why combine both Rule-Based and Case-Based reasoning in one system?**
They solve different types of problems. RBR is perfect for **deterministic, well-defined telemetry** (e.g., if CPU > 85°C, then trigger a thermal shutdown). It is fast and absolute. CBR is ideal for **fuzzy, unstructured human input** (e.g., a ticket saying "laptop makes a weird noise and won't turn on"). If the system hasn't seen the exact issue before, CBR can guess based on past similarities, whereas RBR would simply fail if a rigid rule wasn't explicitly programmed.

**Q: How are rules created dynamically in the RBR module?**
Rules are instantiated as objects containing a `name`, a `condition`, and an `action`. The `condition` utilizes Python `lambda` functions (anonymous functions). This allows the system to pass the dictionary of current facts (`f`) directly into a one-line logical check (e.g., `lambda f: f["cpu_temperature"] > 85`) without needing to hardcode complex `if/else` blocks inside the engine itself.