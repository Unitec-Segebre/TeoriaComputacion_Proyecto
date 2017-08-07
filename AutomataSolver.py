
class Automata_BARE():
    def __init__(self, states, input_symbols, transitions, initial_states, final_states):
        self.states = states
        self.input_symbols = input_symbols
        self.transitions = transitions
        self.initial_states = initial_states
        self.final_states = final_states

    def get_destinies(self, current_state, condition):
        if condition in self.transitions[current_state]:
            return set(self.transitions[current_state][condition])
        return set()

class Automata_DFA(Automata_BARE):
    def __init__(self, states, input_symbols, transitions, initial_state, final_states):
        super(Automata_DFA, self).__init__(states, input_symbols, transitions, initial_state, final_states)

    def solve(self, sequence, epsilon):
        if epsilon in self.input_symbols:
            raise Exception(("Epsilon('%c') not allowed in DFA graphs"%(epsilon)))

        current_state = list(self.initial_states)[0]
        for symbol in sequence:
            if current_state in self.transitions:
                if symbol in self.transitions[current_state]:
                    current_state = list(self.transitions[current_state][symbol])[0]
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

        current_states = self.initial_states
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



    def solve(self, sequence, epsilon):
        print("---HERE---")
        print(self.states)
        print(self.input_symbols)
        print(self.transitions)
        print(self.initial_states)
        print(self.final_states)
        # for state in self.transitions:
        #     free_states = set()
        #     print("{}".format(self.closure(epsilon, state, free_states)))

        current_states = self.initial_states
        for symbol in sequence:
            free_states = set()
            for current_state in current_states:
                temp = set()
                free_states = free_states | self.closure(epsilon, current_state, temp)
            current_states = set()
            for state in free_states:
                current_states = current_states | self.get_destinies(state, symbol)
        free_states = set()
        for current_state in current_states:
            temp = set()
            free_states = free_states | self.closure(epsilon, current_state, temp)
        for current_state in free_states:
            if current_state in self.final_states:
                return current_state
        raise Exception('{} is NOT a solution'.format(sequence))


    def closure(self, epsilon, state, free_states):
        free_states.add(state)
        if epsilon in self.transitions[state]:
            for destiny in self.transitions[state][epsilon]:
                if destiny not in free_states:
                    self.closure(epsilon, destiny, free_states)
        return set(free_states)













    # def solve(self, sequence, epsilon):
    #     current_states = [self.initial_states]
    #     for symbol in sequence:
    #         for state in current_states:
    #             states_to_add = []
    #             self.clousure(epsilon, state, states_to_add)
    #             for state_to_add in states_to_add:
    #                 current_states.append(state_to_add)
    #         current_states = list(set(current_states))
    #         current_states_temp = []
    #         for current_state in current_states:
    #             if current_state in self.transitions:
    #                 for arista in self.transitions[current_state]:
    #                     if symbol == arista:
    #                         for destiny in self.transitions[current_state][arista]:
    #                             current_states_temp.append(destiny)
    #             else:
    #                 raise Exception('{} is NOT a valid state'.format(current_state))
    #         current_states = list(set(current_states_temp))
    #         if current_states == []:
    #             break
    #     for current_state in current_states:
    #         if current_state in self.final_states:
    #             return current_state
    #     raise Exception('{} is NOT a solution'.format(sequence))
    #
    # def clousure(self, epsilon, state, list):
    #     if epsilon in self.transitions[state]:
    #         for closure_state in self.transitions[state][epsilon]:
    #             list.append(state)
    #             print(closure_state)
    #             if closure_state in list:
    #                 continue
    #             self.clousure(epsilon, closure_state, list)
    #     return
