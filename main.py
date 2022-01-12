#
#   CS-454 Project 2
#   by Diana Arce-Hernandez, Ryan McAlpine, and Rommel Ravanera
#

from automata.fa.nfa import NFA
from automata.fa.dfa import DFA


def count( dfa, n ):  # n is the length of the string
    if n < 1 or n > 200:
        print("Invalid input")
        return 0

    # current = [0] * len(dfa.states) - Replace w/ dictionary
    # previous = [0] * len(dfa.states) - Replace w/ dictionary
    current = {}
    previous = {}

    # For every state,
    for i in dfa.states:
        # if it is a final state,
        if i in dfa.final_states:
            # change index in previous[] from 0 to 1 to mark it as accepting
            # previous{0, 0, 0, 0, 0, 1, 1, 1, 0}
            previous[i] = 1  # replaces previous for accepting state
        else:
            previous[i] = 0

        current[i] = 0

    # For the input string length
    for i in range(n):
        # For every state in the DFA
        for j in dfa.states:
            sum = 0
            # For every input 0-9
            for k in dfa.transitions[j].values():
                sum += previous[k]
            current[j] = sum
        for k in dfa.states:
            previous[k] = current[k]

    return current['{S}']


if __name__ == '__main__':
    # First, create NFA for weakly divisible by 7:
    nfa = NFA(
        states={'S', '0', '1', '2', '3', '4', '5', '6', 'R', '0c', '1c', '2c', '3c', '4c', '5c', '6c'},
        input_symbols={'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'},
        transitions={
            'S': {'0': {'R'}, '1': {'1', '0c'}, '2': {'2', '0c'}, '3': {'3', '0c'}, '4': {'4', '0c'},
                  '5': {'5', '0c'}, '6': {'6', '0c'}, '7': {'0', '0c'}, '8': {'1', '0c'}, '9': {'2', '0c'}},
            '0': {'0': {'0', '0c'}, '1': {'1', '0c'}, '2': {'2', '0c'}, '3': {'3', '0c'}, '4': {'4', '0c'},
                  '5': {'5', '0c'}, '6': {'6', '0c'}, '7': {'0', '0c'}, '8': {'1', '0c'}, '9': {'2', '0c'}},
            '1': {'0': {'3', '1c'}, '1': {'4', '1c'}, '2': {'5', '1c'}, '3': {'6', '1c'}, '4': {'0', '1c'},
                  '5': {'1', '1c'}, '6': {'2', '1c'}, '7': {'3', '1c'}, '8': {'4', '1c'}, '9': {'5', '1c'}},
            '2': {'0': {'6', '2c'}, '1': {'0', '2c'}, '2': {'1', '2c'}, '3': {'2', '2c'}, '4': {'3', '2c'},
                  '5': {'4', '2c'}, '6': {'5', '2c'}, '7': {'6', '2c'}, '8': {'0', '2c'}, '9': {'1', '2c'}},
            '3': {'0': {'2', '3c'}, '1': {'3', '3c'}, '2': {'4', '3c'}, '3': {'5', '3c'}, '4': {'6', '3c'},
                  '5': {'0', '3c'}, '6': {'1', '3c'}, '7': {'2', '3c'}, '8': {'3', '3c'}, '9': {'4', '3c'}},
            '4': {'0': {'5', '4c'}, '1': {'6', '4c'}, '2': {'0', '4c'}, '3': {'1', '4c'}, '4': {'2', '4c'},
                  '5': {'3', '4c'}, '6': {'4', '4c'}, '7': {'5', '4c'}, '8': {'6', '4c'}, '9': {'0', '4c'}},
            '5': {'0': {'1', '5c'}, '1': {'2', '5c'}, '2': {'3', '5c'}, '3': {'4', '5c'}, '4': {'5', '5c'},
                  '5': {'6', '5c'}, '6': {'0', '5c'}, '7': {'1', '5c'}, '8': {'2', '5c'}, '9': {'3', '5c'}},
            '6': {'0': {'4', '6c'}, '1': {'5', '6c'}, '2': {'6', '6c'}, '3': {'0', '6c'}, '4': {'1', '6c'},
                  '5': {'2', '6c'}, '6': {'3', '6c'}, '7': {'4', '6c'}, '8': {'5', '6c'}, '9': {'6', '6c'}},
            'R': {'0': {'R'}, '1': {'R'}, '2': {'R'}, '3': {'R'}, '4': {'R'},
                  '5': {'R'}, '6': {'R'}, '7': {'R'}, '8': {'R'}, '9': {'R'}},
            '0c': {'0': {'0c'}, '1': {'1c'}, '2': {'2c'}, '3': {'3c'}, '4': {'4c'},
                   '5': {'5c'}, '6': {'6c'}, '7': {'0c'}, '8': {'1c'}, '9': {'2c'}},
            '1c': {'0': {'3c'}, '1': {'4c'}, '2': {'5c'}, '3': {'6c'}, '4': {'0c'},
                   '5': {'1c'}, '6': {'2c'}, '7': {'3c'}, '8': {'4c'}, '9': {'5c'}},
            '2c': {'0': {'6c'}, '1': {'0c'}, '2': {'1c'}, '3': {'2c'}, '4': {'3c'},
                   '5': {'4c'}, '6': {'5c'}, '7': {'6c'}, '8': {'0c'}, '9': {'1c'}},
            '3c': {'0': {'2c'}, '1': {'3c'}, '2': {'4c'}, '3': {'5c'}, '4': {'6c'},
                   '5': {'0c'}, '6': {'1c'}, '7': {'2c'}, '8': {'3c'}, '9': {'4c'}},
            '4c': {'0': {'5c'}, '1': {'6c'}, '2': {'0c'}, '3': {'1c'}, '4': {'2c'},
                   '5': {'3c'}, '6': {'4c'}, '7': {'5c'}, '8': {'6c'}, '9': {'0c'}},
            '5c': {'0': {'1c'}, '1': {'2c'}, '2': {'3c'}, '3': {'4c'}, '4': {'5c'},
                   '5': {'6c'}, '6': {'0c'}, '7': {'1c'}, '8': {'2c'}, '9': {'3c'}},
            '6c': {'0': {'4c'}, '1': {'5c'}, '2': {'6c'}, '3': {'0c'}, '4': {'1c'},
                   '5': {'2c'}, '6': {'3c'}, '7': {'4c'}, '8': {'5c'}, '9': {'6c'}},

        },
        initial_state='S',
        final_states={'0', '0c'}
    )

    # Next, convert the NFA into a DFA
    dfa = DFA.from_nfa(nfa)
    dfa.states = sorted(dfa.states)

    while True:
        k = int(input("Enter an integer between 1 and 200: "))
        print("There are " + str(count(dfa, k)) + " valid strings of length " + str(k) + "\n")
