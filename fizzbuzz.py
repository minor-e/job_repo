#!/usr/bin/env python3.6
"""
The script runs a simple algorithm based on the word game 'fizz buzz'.

The rules are:
For numbers that are a multiple of 3 e.g. 3, 6, 9 ... etc are substituted
by the word 'fizz'

For numbers that are a multiple of 5 e.g. 5, 10 ,15 ...etc  are substituted
by the word 'buzz'


For number that are  a mutltiple of both 3 and 5 e.g. 15, 30, 45 ... etc are
substituted by the word 'fizzbuzz'

"""
import sys

class FizzBuzz:

    # Class Attribute
    START = 1

    @staticmethod
    def _game_logic(endpoint):

        # Logic for game
        c1 = endpoint % 3 is 0
        c2 = endpoint % 5 is 0
        c3 = c1 and c2

        if c3:
            return "FizzBuzz"
        elif c1:
            return "Fizz"
        elif c2:
            return "Buzz"
        else:
            return endpoint

    def __init__(self, endpoint):
        self.endpoint = endpoint

    def play_game(self):
        sequence_of_digits = range(FizzBuzz.START, self.endpoint)
        return map(FizzBuzz._game_logic, sequence_of_digits)


if __name__ == "__main__":
    try:
        int(sys.argv[1])
    except (ValueError, TypeError) as nan:
        print("The value entered failed integer conversion{}".format(nan, file=sys.stderr))
    fizzbuzz_game = FizzBuzz(int(sys.argv[1]))
    print(list(fizzbuzz_game.play_game()))

