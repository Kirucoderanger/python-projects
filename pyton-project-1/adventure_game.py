# Text-based Adventure game
"""
Developer: King Emmanuel Aguomba

Purpose: To keep the user in Engaged.
"""

# dictionary to store the list of choices
lvl_1 = {
    "choices":["EXPLORE","WAIT","CALL FOR HELP"]
}
lvl_2 = {
   "explore":["SWIM", "BUILD A RAFT", "TURN BACK"],
   "wait":["HIDE", "CALL FOR HELP", "RUN"],
   "call" :["YES", "NO", "ASK WHO THEY ARE"]
}

lvl_3 = {
   "swim": ["FIGHT", "LET GO"],
   "hide" :["STAY", "RUN"],
   "yes":["EAT", "DECLINE"],
   "ask":["TRUST", "DON'T TRUST"]
}

# Empty scenario variable
scenario =""

# Starting Game
print("\n_____---Welcome to the Adventure---_____")

# function to how response and perform task
def ask_who():
    print("\n<--- Level 3: Ask Who They Are --->")
    scenario = input(f'You decide to question the voice. "Who are you?" you shout.\nThe voice responds, "A traveler, lost just like you."\nThey emerge from the trees cautiously. Do you TRUST them or DON\'T TRUST them?\n-- Choices: {lvl_3["ask"]} --> ').lower()

    if scenario == lvl_3["ask"][0].lower():  # TRUST
        outcome = """
        You decide to trust the traveler. They lead you to a small hidden
        clearing where you can rest. The traveler seems helpful, and for now,
        you feel safe, though you know you must remain cautious.
        """
        print(f"{outcome}\n<---------- The End! ---------->")
    elif scenario == lvl_3["ask"][1].lower():  # DON'T TRUST
        outcome = """
        You remain wary of the traveler and decide to part ways.
        The traveler seems indifferent, disappearing back into the trees.
        You’re left to continue your journey alone, unsure if you missed
        an opportunity or avoided a trap.
        """
        print(f"{outcome}\n<---------- The End! ---------->")
    else:
        print("Invalid choice! Please try again.")
        ask_who()

    pass
def trust():
    scenario = input(f"The voice belongs to a traveler offering food. Do you ACCEPT or DECLINE it?\n-- Choices: {lvl_3['yes']} --> ").lower()
    
    print("\n<--- Level 3: Trust --->")
    
    if scenario == lvl_3["yes"][0].lower():  # EAT
        outcome = """
        You accept the food and eat it. The traveler smiles, but soon you start feeling dizzy.
        The food was poisoned! As your vision blurs, the traveler reveals their true intentions.
        You have a few moments to act before everything goes black...
        """
        print(f"{outcome}\n<---------- Game Over! ---------->")
    elif scenario == lvl_3["yes"][1].lower():  # DECLINE
        outcome = """
        You politely decline the offer.
        The traveler looks disappointed but respects your decision.
        They give you directions to the nearest village, and you part ways.
        You move forward cautiously, relieved but still on high alert.
        """
        print(f"{outcome}\n<---------- The End! ---------->")
    else:
        print("Invalid choice! Please try again.")
        trust()
    pass
def dont_trust():
    print("\n<--- Level 3: Don't Trust --->")
    scenario = input(f"You don’t trust the voice and remain where you are, hiding behind a large rock. The voice calls out again, but you stay silent.\nMoments later, a group of figures appears, searching for you. What do you do?\n-- Choices: {lvl_3['hide']} --> ").lower()
    
    if scenario == lvl_3["hide"][0].lower():  # STAY
        outcome = """
        You remain hidden as the figures pass by, unaware of your presence.
        It was a close call, but you’ve avoided danger for now.
        As the group disappears into the trees, you wonder if they’ll come back.
        """
        print(f"{outcome}\n<---------- The End! ---------->")
    elif scenario == lvl_3["hide"][1].lower():  # RUN
        outcome = """
        You sprint away, the sound of footsteps behind you.
        The figures give chase, and after a tense pursuit,
        you barely manage to lose them by diving into a dense thicket.
        You're exhausted but alive, unsure if they’ll find you again.
        """
        print(f"{outcome}\n<---------- The End! ---------->")
    else:
        print("Invalid choice! Please try again.")
        dont_trust()
    pass
def call_help():
    print("\n<--- Level 2: Call for Help --->")
    scenario = input(f"You call out, and a voice responds from the trees. Do you TRUST them, NOT TRUST them, or ASK WHO THEY ARE?\n-- Choices: {', '.join(lvl_2['call'])} --> ").strip().lower()
    
    if scenario == lvl_2["call"][0].lower():  # YES / TRUST
        trust()
    elif scenario == lvl_2["call"][1].lower():  # NO / DON'T TRUST
        dont_trust()
    elif scenario == lvl_2["call"][2].lower():  # ASK WHO THEY ARE
        ask_who()
    else:
        print("Invalid choice! Please try again.")
        call_help()
    pass
def explore():
    print("\n<--- Level 2: Explore --->")
    scenario = input(f"As you walk down the path, you encounter a river. How do you cross it?\n<-- Choices: {', '.join(lvl_2['explore'])} --> ").strip().lower()
    if scenario == lvl_2["explore"][0].lower():  # SWIM
        swim()
    elif scenario == lvl_2["explore"][1].lower():  # BUILD A RAFT
        print("\n<--- Level 3 --->")
        outcome = "You gather materials and successfully build a raft. You cross the river safely and continue your journey."
        print(f"{outcome}\n<---------- The End! ---------->")
    elif scenario == lvl_2["explore"][2].lower():  # TURN BACK
        print("\n<--- Level 3 --->")
        outcome = "When you turned back, there was no way out... so you were trapped in the forest forever."
        print(f"{outcome}\n<---------- Game Over! ---------->")
    else:
        print("Invalid choice! Please try again.")
        explore()
    pass
def hide():
    print("\n<--- Level 3: Hide --->")
    scenario = input(f"You hide behind a tree, but the footsteps get closer. Do you STAY or RUN?\n-- Choices: {', '.join(lvl_3['hide'])} --> ").lower()
    if scenario == lvl_3["hide"][0].lower():  # STAY
        outcome = """
        You stay hidden as the footsteps stop near you. After a long, tense moment,
        the figure walks away, leaving you safe but alone in the forest.
        You continue your journey cautiously, never knowing who or what was behind the footsteps.
        """
        print(f"{outcome}\n<---------- The End! ---------->")
    elif scenario == lvl_3["hide"][1].lower():  # RUN
        outcome = """
        You dash out from behind the tree, running as fast as you can.
        The footsteps behind you quicken, and you barely manage to escape by diving into a thick bush.
        Panting, you realize you’ve lost them, but you're completely disoriented in the forest.
        """
        print(f"{outcome}\n<---------- The End! ---------->")
    else:
        print("Invalid choice! Please try again.")
        hide()
    pass
def wait():
    print("\n<--- Level 2: Wait --->")
    scenario = input(f"After waiting, you hear footsteps approaching. What do you do?\n<-- Choices: {', '.join(lvl_2['wait'])} --> ").lower()
    if scenario == "hide":
        hide()
    elif scenario == "call for help":
        call_help()
    elif scenario == "run":
        print("\n<--- Level 3 --->")
        outcome = """
        You run as fast as you can. The footsteps behind you quicken,
        and you barely manage to escape by diving into a thick bush.
        Panting, you realize you’ve lost them, but you're completely disoriented in the forest.
        """
        print(f"{outcome}\n<---------- The End! ---------->")
    else:
        print("Invalid choice! Please try again.")
        wait()

    pass
def swim():
    print("\n<--- Level 3: Swim --->")
    scenario = input(f"You swim across the river, but something pulls you under. Do you FIGHT or LET GO?\n-- Choices: {', '.join(lvl_3['swim'])} --> ").strip().lower()
    if scenario == lvl_3["swim"][0].lower():  # FIGHT
        outcome = "You fought valiantly against the unknown force and managed to escape the river's grasp. Congratulations!"
        print(f"\n<--- Level 3 Completed! --->\n{outcome}\n<---------- The End! ---------->")
    elif scenario == lvl_3["swim"][1].lower():  # LET GO
        outcome = "A crocodile was pulling you under, and you ended up being eaten. You were killed!\n<---------- Game Over! ---------->"
        print(outcome)
    else:
        print("Invalid choice! Please try again.")
        swim()
    pass

# Start game function
def start_game():
    prompt = input("Enter 'start' to begin your adventure: ").lower()
    if prompt == "start":
        print("\n<--- Level 1 --->")
        scenario = input(f"You wake up in a mysterious forest. There's a path ahead. What do you do?\n<-- Choices: {lvl_1['choices']} --> ").lower()
        if scenario == lvl_1["choices"][0].lower():
            explore()
        elif scenario == lvl_1["choices"][1].lower():
            wait()
        elif scenario == lvl_1["choices"][2].lower():
            call_help()
        else:
            print("Invalid choice! Please try again.")
            start_game()
    else:
        print("Invalid command! Please type 'start' to begin.")
        start_game()

start_game()