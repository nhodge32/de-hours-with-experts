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
    '6': '9',
    ',': ',',
    '/': '/',
    '-': '-',
    ' ': ' '
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
    return decoded_word


def decode_ingredient(line):
    """Given an ingredient, decode the amount and description, and return a new Ingredient"""
    amount, description = line.split("#")
    # Not sure if this would be the better way or defining a variable for each, decode, and then return with those new variables
    return Ingredient(decode_string(amount), decode_string(description))


def main():
    """A program that decodes a secret recipe"""
    decoded_recipe_file = open('decoded_recipe.txt', 'w')
    secret_recipe = open("secret_recipe.txt", "r")
    ingredients = secret_recipe.read()
    single_ingredient = ingredients.splitlines()
    for line in single_ingredient:
        decoded_ingredient = decode_ingredient(line)
        decoded_recipe_file.write(decoded_ingredient.amount + " " + decoded_ingredient.description + "\n")

    secret_recipe.close()
    decoded_recipe_file.close()

if __name__ == "__main__":
    main()
