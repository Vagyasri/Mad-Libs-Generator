#!/usr/bin/python3

import json

class Madlibs:
    def __init__(self, template, word_type):
        self.template = template
        self.word_type = word_type
        self.user_words = []

    @staticmethod
    def get_template(name, path="./templates/"):
        with open(path + name + ".json") as f:
            data = json.load(f)
        return data

    def get_user_words(self):
        print("Enter the words for the following types:")
        for description in self.word_type:
            user_input = input(description + ": ")
            self.user_words.append(user_input)
        return self.user_words

    def story(self):
        story = self.template.format(*self.user_words)
        return story

    def select_template():
        template = input("Enter the name of the template: ")
        return template

def main():
    template_name = Madlibs.select_template()
    mad_lib = Madlibs.get_template(template_name)
    full_madlib = Madlibs(mad_lib["template"], mad_lib["word_type"])
    full_madlib.get_user_words()
    print(full_madlib.story())

if __name__ == "__main__":
    main()
