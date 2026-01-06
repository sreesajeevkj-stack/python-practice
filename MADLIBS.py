print("🎉 Welcome to the Mad Libs Game 🎉")
print("Fill in the blanks to create a funny story!\n")

name = input("Enter a name: ")
adjective = input("Enter an adjective: ")
place = input("Enter a place: ")
food = input("Enter a food: ")
verb_ing = input("Enter a verb ending with -ing: ")
plural_noun = input("Enter a plural noun: ")
emotion = input("Enter an emotion: ")
number = input("Enter a number: ")

print("\n📖 Your Mad Libs Story:\n")

story = f"""
One day, {name} went to {place} feeling very {adjective}.
Suddenly, the smell of {food} filled the air while {name} was {verb_ing}
near a group of {plural_noun}.

Everyone felt {emotion}, especially when {name} shouted,
"I can’t believe this happened {number} times today!"
"""

print(story)
