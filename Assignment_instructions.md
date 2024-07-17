# Lesson 2: Assignments: Nested If

Remember to take your time and work through each question diligently! Test your code, make sure it works, and try to find ways to improve. Once you are happy and satisfied with your code, upload it to Github, then turn in your Github link at the bottom of the page!

Don't forget. Make sure this assignment is in it's own repository. Not mixed in with others!

1. Nested Decisions: The Adventure Game 🏰
Objective:

To practice the use of nested if statements in creating a simple text-based adventure game.

Task 1: Code Correction

You are provided with a Python script that is supposed to guide a user through an adventure game, but it has some errors. Identify and fix them.

Buggy Code:

place = input("Choose a place: forest or cave? ")

if place = "forest":
    action = input("climb a tree or cross a river?")
    if action = "climb a tree":
        print("You found a bird's nest!")
    else action = "cross a river":
        print("You found a boat!")
elif place = "cave":
    print("You find a hidden treasure!")
Task 2: Setting the Scene

Based on the corrected code from Task 1, expand the game. If the user chooses "cave", instead of printing "You find a hidden treasure!" ask them if they want to "light a torch" or "proceed in the dark", and provide outcomes for each decision.

Task 3: Default Path

If the user makes an invalid choice at any point, use the pass statement for now. Later, you can enhance this to provide feedback or a different branch of the story.

2. Quick Decisions: The Event Planner 🎉
Objective:

To practice the use of shorthand if statements in determining event-related decisions.

Task 1: Code Correction

You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.

Buggy Code:

attendees = input("Enter number of attendees: ")
venue = "large hall" if attendees > 100 elif "conference room"
print(venue)



Task 2: Catering Choices

Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".

