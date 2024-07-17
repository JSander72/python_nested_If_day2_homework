
# Task 1: Code Correction & Task 2: Setting the Scene & Task 3: default Path


place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    print("light a torch or proceed in the dark?")
    action = input("light a torch or proceed in the dark?")
    if action == "light a torch":
        print("Wow, this cave is bigger then I thought!")
    elif action == "proceed in the dark":
        print("I hope there is nothing in this cave")
    else:
        pass
else:
    pass

#---------------#

#task 1: corrected code & Task 2: Catering Choices 

# print(user_input + 25) this will throw an error because we can't concatenate an integer and a string
# convert the string input to an integer 

attendees = input("Enter number of attendees: ")
user_input = int(attendees)
venue = "large hall or conferance room"
venue = "large hall" if int(input("enter number of attendees: "> 100)) else "conference room"
print(venue)


# Task 2: Catering Choices

customer = input("Choose a food type: vegetarian, non-vegetarian? ")

if customer == "vegetarian":
    recommendation = "Veggie Delight Caterers"
elif customer == "non-vegetarian":
    recommendation = "Gourmet Meals Caterers"
else:
    pass

print("I recommend:", recommendation) 






            

    

    



