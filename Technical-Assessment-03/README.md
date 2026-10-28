# Disaster Response Community Guide

This is a lightweight, interactive Python tool designed to help communities prepare for natural disasters like typhoons, earthquakes, and floods. 

It uses Case-Based Reasoning (CBR), meaning it looks at a database of historical disasters and uses those past experiences to recommend evacuation strategies, shelter capacities, and emergency resources for new situations. 

## How it works

1. **Describe the situation:** You input the type of disaster, location, intensity, and nearby hazards (like a river or mountain).
2. **Find a match:** The system searches its local memory for the most similar past event.
3. **Adapt and recommend:** It tweaks the past solution to fit your current emergency. For example, it might suggest increasing shelter capacity if the new disaster is stronger, or add specific protocols based on your local terrain.
4. **Learn:** You can review the suggested plan and save it back to the database, making the system smarter for the next time.

| Disaster Type | Intensity Level | Description |
|---|---|---|
| Flood | 1.0 - 2.0 | Minor to Moderate (Knee-deep) |
| Flood | 3.0 | High Danger (Waist-deep) |
| Flood | 4.0 | Severe (Roof-level) |
