
class Saver_DFA():
    def __init__(self, type, states, input_symbols, transitions, initial_states, final_states):
        self.type = type
        self.states = states
        self.input_symbols = input_symbols
        self.transitions = transitions
        self.initial_states = initial_states
        self.final_states = final_states