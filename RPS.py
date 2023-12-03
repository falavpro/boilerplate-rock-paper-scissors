# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

import random

# Improved tracking of opponent's history
# Increased the history length from 5 to 10
wtf = {}

def player(prev_play, opponent_history=[]):
    global wtf

    n = 10

    # Added check for empty opponent history
    if prev_play:
        opponent_history.append(prev_play)

    guess = "R"  # default guess

    # Improved prediction strategy using Markov chains
    if len(opponent_history) > n:
        inp = "".join(opponent_history[-n:])

        if "".join(opponent_history[-(n + 1):]) in wtf.keys():
            wtf["".join(opponent_history[-(n + 1):])] += 1
        else:
            wtf["".join(opponent_history[-(n + 1):])] = 1

        possible_plays = [
            inp + "R",
            inp + "P",
            inp + "S",
        ]

        for i in possible_plays:
            if not i in wtf.keys():
                wtf[i] = 0

        # Using Markov chain probabilities to determine guess
        transition_probabilities = {
            k: wtf[k] / sum(wtf.values()) for k in possible_plays
        }
        guess = max(transition_probabilities, key=transition_probabilities.get)[-1:]

    return guess
