import random
names = input("Enter a list of names seperated by commas:").split(",")
# lucky = random.choice(names)
# NUM_of_names = len(names)
# random_name = random.randint(0, NUM_of_names-1)
# print(f"{names[random_name]} is the lucky person!Congratulations!")
print(f"lucky guy {random.choice(names)}")
