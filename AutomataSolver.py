
class Automata_BARE():
    def __init__(self, states, input_symbols, transitions, initial_states, final_states):
        self.states = states
        self.input_symbols = input_symbols
        self.transitions = transitions
        self.initial_states = initial_states
        self.final_states = final_states

class Automata_DFA(Automata_BARE):
    def __init__(self, states, input_symbols, transitions, initial_state, final_states):
        super(Automata_DFA, self).__init__(states, input_symbols, transitions, initial_state, final_states)

    def solve(self, sequence, epsilon):
        if epsilon in self.input_symbols:
            raise Exception(("Epsilon('%c') not allowed in DFA graphs"%(epsilon)))

        current_state = self.initial_states
        for symbol in sequence:
            if current_state in self.transitions:
                if symbol in self.transitions[current_state]:
                    current_state = self.transitions[current_state][symbol][0]
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
            raise Exception(("Epsilon('%c') not allowed in NFA graphs"%(epsilon)))

        current_states = [self.initial_states]
        for symbol in sequence:
            current_states_temp = []
            for current_state in current_states:
                if current_state in self.transitions:
                    for arista in self.transitions[current_state]:
                        if symbol == arista:
                            for destiny in self.transitions[current_state][arista]:
                                current_states_temp.append(destiny)
                else:
                    raise Exception('{} is NOT a valid state'.format(current_state))
            current_states = list(set(current_states_temp))
            if current_states == []:
                break
        for current_state in current_states:
            if current_state in self.final_states:
                return current_state
        raise Exception('{} is NOT a solution'.format(sequence))

class Automata_NFAEpsilon(Automata_BARE):
    def __init__(self, states, input_symbols, transitions, initial_state, final_states):
        super(Automata_NFAEpsilon, self).__init__(states, input_symbols, transitions, initial_state, final_states)
        print("---HERE---")
        print(self.states)
        print(self.input_symbols)
        print(self.transitions)
        print(self.initial_states)
        print(self.final_states)

    def solve(self, sequence, epsilon):
        current_states = [self.initial_states]
        for symbol in sequence:
            current_states_temp = []
            for current_state in current_states:
                if current_state in self.transitions:
                    for arista in self.transitions[current_state]:
                        if symbol == arista:
                            for destiny in self.transitions[current_state][arista]:
                                current_states_temp.append(destiny)
                else:
                    raise Exception('{} is NOT a valid state'.format(current_state))
            current_states = list(set(current_states_temp))
            if current_states == []:
                break
        for current_state in current_states:
            if current_state in self.final_states:
                return current_state
        raise Exception('{} is NOT a solution'.format(sequence))

    def clousure(self, epsilon, state, list):
        if epsilon in self.transitions[state]:
            for closure_state in self.transitions[state][epsilon]:
                self.clousure(epsilon, state, list)
        list.append(state)
        return
