
class Automata_BARE():
    def __init__(self, states, input_symbols, transitions, initial_state, final_states):
        self.states = states
        self.input_symbols = input_symbols
        self.transitions = transitions
        self.initial_state = initial_state
        self.final_states = final_states

class Automata_DFA(Automata_BARE):
    def __init__(self, states, input_symbols, transitions, initial_state, final_states):
        super(Automata_DFA, self).__init__(states, input_symbols, transitions, initial_state, final_states)

    def solve(self, sequence, epsilon):
        if epsilon in self.input_symbols:
            raise Exception(("Epsilon('%c') not allowed in DFA graphs"%(epsilon)))

        current_state = self.initial_state
        for symbol in sequence:
            if current_state in self.transitions:
                if symbol in self.transitions[current_state]:
                    current_state = self.transitions[current_state][symbol]
                else:
                    raise Exception('{} is NOT a solution'.format(sequence))
            else:
                raise Exception('{} is NOT a valid state'.format(current_state))
        if current_state in self.final_states:
            return current_state
        else:
            raise Exception('{} is NOT a solution'.format(sequence))

class Automata_NFA(Automata_BARE):
    def __init__(self, states, input_symbols, transitions, initial_state, final_states):
        super(Automata_NFA, self).__init__(states, input_symbols, transitions, initial_state, final_states)

    def solve(self, sequence, epsilon):
        if epsilon in self.input_symbols:
            raise Exception(("Epsilon('%c') not allowed in DFA graphs"%(epsilon)))

        current_state = self.initial_state
        for symbol in sequence:
            if current_state in self.transitions:
                if symbol in self.transitions[current_state]:
                    current_state = self.transitions[current_state][symbol]
                else:
                    raise Exception('{} is NOT a solution'.format(sequence))
            else:
                raise Exception('{} is NOT a valid state'.format(current_state))
        if current_state in self.final_states:
            return current_state
        else:
            raise Exception('{} is NOT a solution'.format(sequence))