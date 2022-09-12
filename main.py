#!/usr/bin/python3

import json

class Madlibs:
    def __init__(self, template, word_type):
        self.template = template
        self.word_type = word_type

    @staticmethod
    def get_template(name, path="./templates/"):
        with open(path + name + ".json") as f:
            data = json.load(f)
        return data

    def user_words(self):
        words = []
        print("Enter the words for the following types:")
        for description in self.word_type:
            user_input = input(description + ": ")
            words.append(user_input)
        return words

    def story(self, words):
        story = self.template.format(*words)
        return story

def main():
    template = Madlibs.get_template("day_at_zoo")
    word_type = template["word_type"]
    template = template["template"]
    words = Madlibs(template, word_type).user_words()
    print(Madlibs(template, word_type).story(words))

if __name__ == "__main__":
    main()
