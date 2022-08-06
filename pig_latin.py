word = input("Enter your word ")

if word[0] in ["a", "e", "i", "o", "u"]:
    print("{}{}".format(word, "way"))
else:
    print("{}{}{}".format(word[1::], word[0], "ay"))