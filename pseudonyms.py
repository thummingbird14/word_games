import random

print("Welcome to the 'Sidekick Name Picker'.\n\n")

first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'", "Bob 'Stinkbug'", 'Boxelder', "Bud 'Lite'", 'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield', 'Chewy', 'Chigger', 'Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat', 'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Diceman', 'Elphonso', 'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry', 'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny', 'Lemongrass', 'Lil Debil', 'Longbranch', 'Lunch Money', 'Mergatroid', 'Mr Peabody', 'Oil-Can', 'Oinks', 'Old Scratch', 'Ovaltine', 'Pennywhistle', 'Pitchfork Ben', 'Potato Bug', 'Pushmeet', 'Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut', "Sid 'The Squirts'", 'Slaps', 'Snakes', 'Snoobs', 'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky', 'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe', "Winston 'Jazz Hands'", 'Worms')

last = ('Appleyard', 'Bigmeat', 'Bloominshine')

while True:
    first_name = random.choice(first)
    last_name = random.choice(last)

    print("\n\n")
    print("{} {}".format(first_name, last_name))
    print("\n\n")

    try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")
    if try_again.lower() == "n":
        break

input("\nPress Enter to exit.")