word_definitions = dict()

word_definitions["Awesome"] = "The feeling of students when they are learning Python"

word_definitions["zeugma"] = "use of a word to modify two or more words in different ways"


word_definitions["virason"] = "sea breeze"

word_definitions["deric"] = "of, like or pertaining to the sking"

print(word_definitions["Awesome"])
print(word_definitions["virason"])


for (key, value) in word_definitions.items():
    print(f"The definition of {key} is a {value}")
