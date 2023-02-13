import random
import colorama
import textwrap
from colorama import Fore

colorama.init(autoreset=True)

print("Hello,this is your first random sentence: ")
print(Fore.CYAN + "For 'Exit' press 1 ")

names = ["Ivan", "Petko", "Ivailo", "Stoqn", "Dragan", "Petkan", "Georgi", "Todor", "Ruslan", "Teodora", "Petq",
         "Ivanka", ]
places = ["Dobrich", "Varna", "Sofia", "Plovdiv", "Shumen", "Razgrad", "Burgas", "Ivailovgrad", "Vidin", "Vraca",
          "Montana"]
verbs = ["eats", "brings", "holds", "plays with", "fights", "talks to", "runs at", "shouts at", "bakes", "jumps over",
         "breaks", "makes", "screams at"]
nouns = ["stones", "cake", "apple", "laptop", "bikes", "air", "food", "a friend", "a judge", "dirt", "a student",
         "an animal", "a chair", "a cup", "a computer"]
adverbs = ["slowly", "seriously", "warmly", "sadly", "rapidly", "impatiently", "loudly", "oddly", "loosley", "safely",
           "nicely", "colorfully", "diligently"]
details = ["near the river", "at home", "in the park", "at the cafeteria", "at work", "on the toilet", "in bed",
           "on the floor", "on the ceilling", "in the basement", "in the kitchen",
           "on the computer"]


def randomize_words(word):
    randomized = random.choice(word)
    return randomized


while True:
    random_names = randomize_words(names)
    random_places = randomize_words(places)
    random_verbs = randomize_words(verbs)
    random_nouns = randomize_words(nouns)
    random_adverbs = randomize_words(adverbs)
    random_details = randomize_words(details)

    print()
    print(
        Fore.LIGHTGREEN_EX + f"{random_names} from {random_places} {random_adverbs} {random_verbs} {random_nouns} {random_details}")

    print()
    read = input(Fore.LIGHTYELLOW_EX + "Click [Enter] to generate new sentence :)")

    if read == "1":
        print("Thanks ,you had played my sentence generator :) Bye !!")
        break
