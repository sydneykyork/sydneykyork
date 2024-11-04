import random

# Lists of possible story elements
characters = ["Alice", "Bob", "Charlie", "David", "Eve"]
locations = ["a mysterious forest", "an ancient castle", "a distant planet", "a bustling city", "a quiet village"]
actions = ["discovered a hidden treasure", "embarked on an epic journey", "encountered a friendly alien", "solved a challenging mystery", "helped a stranger in need"]

# Generate a random story
character = random.choice(characters)
location = random.choice(locations)
action = random.choice(actions)

story = f"{character} found themselves in {location}. They {action}. It was a day to remember."

# Print the random story
print(story)
