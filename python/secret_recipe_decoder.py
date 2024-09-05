#!/usr/bin/python3
import pydoc
import sys
import os

# Caesar encoding, for use with decoding below
ENCODING = {
    'y': 'a',
    'h': 'b',
    'v': 'c',
    'x': 'd',
    'k': 'e',
    'p': 'f',
    'z': 'g',
    's': 'h',
    'a': 'i',
    'b': 'j',
    'e': 'k',
    'w': 'l',
    'u': 'm',
    'q': 'n',
    'n': 'o',
    'l': 'p',
    'm': 'q',
    'f': 'r',
    'o': 's',
    'i': 't',
    'g': 'u',
    'j': 'v',
    't': 'w',
    'd': 'x',
    'r': 'y',
    'c': 'z',
    '3': '0',
    '8': '1',
    '4': '2',
    '0': '3',
    '2': '4',
    '7': '5',
    '5': '6',
    '9': '7',
    '1': '8',
    '6': '9'
 }

"""An ingredient has an amount and a description.
For example: an Ingredient could have "1 cup" as the amount and "butter" as the description."""
class Ingredient():
    def __init__(self, amount, description) -> None:
        self.amount = amount
        self.description = description


def decode_string(str):
    """Given a string named str, use the Caesar encoding above to return the decoded string."""
    decoded_word = ""
    for letter in str:
        decoded_letter = ENCODING[letter]
        decoded_word += decoded_letter
    # print (decoded_word)
    return '1 cup'


def decode_ingredient(line):
    """Given an ingredient, decode the amount and description, and return a new Ingredient"""
    decoded_ingredient = ""
    for char in line:
        if char == " ":
            decoded_ingredient += " "
        elif char == ",":
            decoded_ingredient += ","
        elif char == "#":
            decoded_ingredient += "#"
        elif char == "-":
            decoded_ingredient += "-"
        elif char == "/":
            decoded_ingredient += "/"
        else:
            decoded_char = ENCODING[char]
            decoded_ingredient += decoded_char

    amount, description = decoded_ingredient.split("#")

    # print (amount)
    # print(description)
    print(decoded_ingredient)

    return Ingredient("1 cup", "butter")

def main():
    """A program that decodes a secret recipe"""
    # TODO: implement me
    secret_recipe = open("secret_recipe.txt", "r")
    ingredients = secret_recipe.read()
    single_ingredient = ingredients.splitlines()
    for line in single_ingredient:
        decode_ingredient(line)

    with open('decoded_recipe.txt', 'w') as file:
        file.write('Decoded Recipe Ingredient List')

    secret_recipe.close()

if __name__ == "__main__":
    main()
