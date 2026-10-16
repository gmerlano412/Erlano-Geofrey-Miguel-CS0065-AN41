import random

class Environment:
    def __init__(self, state_a, state_b, state_c):
        # Task 1 & Bonus: Initialize rooms using a dictionary, now including Room C
        self.rooms = {'A': state_a, 'B': state_b, 'C': state_c}
        
    def is_dirty(self, room):
        # Task 1: Check if a room is dirty
        return self.rooms[room].lower() == 'dirty'
        
    def clean_room(self, room):
        # Task 1: Clean a room
        self.rooms[room] = 'Clean'
        
    def get_dirty_rooms(self):
        # Helper for Bonus Task to find all currently dirty rooms
        return [room for room, state in self.rooms.items() if state.lower() == 'dirty']

class RuleBasedAgent:
    def __init__(self, starting_location='A'):
        # Task 2: Create a class for the agent
        self.location = starting_location
        
    def perceive_and_act(self, env):
        # Task 2: Implement the perceive-and-act method
        if env.is_dirty(self.location):
            # Rule 1: If current room is dirty, clean it
            env.clean_room(self.location)
            return "Cleaned"
        else:
            # Rule 2 / Bonus: If clean, move to another room (random dirty room if available)
            return self.move(env)
            
    def move(self, env):
        # Task 2 & Bonus: Implement a move method to switch rooms randomly
        dirty_rooms = env.get_dirty_rooms()
        
        if dirty_rooms:
            # Bonus: Randomly choose which dirty room to clean next
            self.location = random.choice(dirty_rooms)
            return "Moved (targeting a dirty room)"
        else:
            # If all rooms are clean, just randomly move to any other room
            available_rooms = [r for r in env.rooms.keys() if r != self.location]
            self.location = random.choice(available_rooms)
            return "Moved (all rooms are clean)"

def visualize_grid(env, agent):
    # Bonus: Visualize the agent moving between rooms using a text-based grid
    grid_display = ""
    agent_pointer = ""
    
    for room in ['A', 'B', 'C']:
        # Format the room block, e.g., [ A: Dirty ]
        state = env.rooms[room]
        box = f"[ {room}: {state:<5} ]  "
        grid_display += box
        
        # Align an arrow (^) exactly under the agent's current location
        if agent.location == room:
            padding = len(box) // 2
            agent_pointer += (" " * padding) + "^ Agent" + (" " * (padding - 7)) + "  "
        else:
            agent_pointer += " " * len(box)
            
    print("\n" + grid_display)
    print(agent_pointer)

def main():
    # Task 1: Allow user to set initial states
    print("Set the initial state of the rooms (enter 'Dirty' or 'Clean')")
    state_a = input("Room A: ").strip().capitalize()
    state_b = input("Room B: ").strip().capitalize()
    state_c = input("Room C: ").strip().capitalize() # Bonus room
    
    env = Environment(state_a, state_b, state_c)
    agent = RuleBasedAgent(starting_location='A')
    
    # Task 3: Ask user how many steps to run
    try:
        steps = int(input("\nHow many steps should the simulation run? "))
    except ValueError:
        print("Please enter a valid number.")
        return

    # Task 3: Run the simulation in a loop
    for step in range(1, steps + 1):
        print(f"\n--- Step {step} ---")
        
        # Display the visual text grid before the action
        visualize_grid(env, agent)
        
        print(f"Agent's current location: Room {agent.location}")
        
        # Agent perceives and takes action
        action = agent.perceive_and_act(env)
        
        print(f"Action taken: {action}")
        print(f"Current state of the environment: {env.rooms}")
        
    # Final state visualization
    print("\n--- Final Environment State ---")
    visualize_grid(env, agent)

if __name__ == "__main__":
    main()