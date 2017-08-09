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
        current_states = self.initial_states
        for symbol in sequence:
            free_states = self.closure_set(epsilon, current_states)
            current_states = set()
            for state in free_states:
                current_states = current_states | self.get_destinies(state, symbol)
        current_states = self.closure_set(epsilon, current_states)
        for current_state in current_states:
            if current_state in self.final_states:
                return current_state
        raise Exception('{} is NOT a solution'.format(sequence))

    def closure_set(self, epsilon, states):
        free_states = set()
        for current_state in states:
            temp = set()
            free_states = free_states | self.closure(epsilon, current_state, temp)
        return free_states

    def closure(self, epsilon, state, free_states):
        free_states.add(state)
        if epsilon in self.transitions[state]:
            for destiny in self.transitions[state][epsilon]:
                if destiny not in free_states:
                    self.closure(epsilon, destiny, free_states)
        return set(free_states)

    def transform(self, epsilon):
        iterator = 0
        table = {}
        estado_actual = ("q%d"%iterator)
        states_set = self.initial_states
        while True:
            table[estado_actual] = {}
            table[estado_actual]['states'] = self.closure_set(epsilon, states_set)
            for state in table[estado_actual]['states']:
                for symbol in self.transitions[state]:
                    if symbol == epsilon:
                        continue
                    if symbol not in table[estado_actual]:
                        table[estado_actual][symbol] = set()
                    table[estado_actual][symbol] = table[estado_actual][symbol] | self.closure_set(epsilon, self.get_destinies(state, symbol))
            iterator = iterator + 1
            estado_actual = ("q%d" % iterator)
            states_set = self.getSetToCalculate(table)
            if len(states_set ) == 0:
                break
        print(table)
        _, temp = self.inKeys(table, table['q0']['states'])
        print(temp)
        states = set([state for state in table])
        input_symbols = set()
        for state in table:
            for symbol in table[state]:
                if symbol != 'states':
                    input_symbols.add(symbol)
        transitions = {}
        final_states = set()
        for state in table:
            paths = {}
            for symbol in table[state]:
                if symbol == 'states':
                    continue
                _, destiny = self.inKeys(table, table[state][symbol])
                paths[symbol] = [destiny]
            transitions[state] = paths

            for final_state in self.final_states:
                if final_state in table[state]['states']:
                    final_states.add(state)

        print("---HERE---")
        print("States: {}".format(states))
        print("Input Symbols: {}".format(input_symbols))
        print("Transitions: {}".format(transitions))
        print("Initial States: {}".format(self.initial_states))
        print("Final States: {}".format(final_states))

        return Automata_BARE(states, input_symbols, transitions, self.initial_states, final_states)



    def getSetToCalculate(self, table):
        for state in table:
            for condition in table[state]:
                if not self.inKeys(table, table[state][condition]):
                    return table[state][condition]
        return set()

    def inKeys(self, table, setToFind):
        for state in table:
            if table[state]['states'] == setToFind:
                return True, state
        return False












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
