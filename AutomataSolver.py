class Automata_BARE():
    def __init__(self, states, input_symbols, transitions, initial_states, final_states):
        self.states = states
        self.input_symbols = input_symbols
        self.transitions = transitions
        self.initial_states = initial_states
        self.final_states = final_states

        print("---HERE---")
        print("States: {}".format(states))
        print("Input Symbols: {}".format(input_symbols))
        print("Transitions: {}".format(transitions))
        print("Initial States: {}".format(self.initial_states))
        print("Final States: {}".format(final_states))

    def get_destinies(self, current_state, condition):
        if condition in self.transitions[current_state]:
            return set(self.transitions[current_state][condition])
        return set()

class Automata_DFA(Automata_BARE):
    def __init__(self, states, input_symbols, transitions, initial_state, final_states):
        super(Automata_DFA, self).__init__(states, input_symbols, transitions, initial_state, final_states)

    def check(self, epsilon):
        if len(self.initial_states) == 0:
            raise Exception("An initial state is required to solve.")
        elif len(self.initial_states) > 1:
            raise Exception("There must only be one initial state to solve.")
        elif len(self.final_states) == 0:
            raise Exception("At least one final state is required to solve.")

        for state in self.transitions:
            for condition in self.transitions[state]:
                if len(self.transitions[state][condition]) != 1:
                    raise Exception("Node '%s' has more than one connection through '%c'." % (state, condition))
                
        if epsilon in self.input_symbols:
            raise Exception(("Epsilon('%c') not allowed in DFA graphs"%(epsilon)))

    def solve(self, sequence, epsilon):
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

    def transform(self, epsilon=None):
        import copy
        def removeParenthesis(transitions):
            for state in transitions:
                for condition in transitions[state]:
                    transitions[state][condition] = transitions[state][condition][0]

        def get_expressions(state, transitions):
            self_expression = ""
            expressions = {}
            for condition in transitions[state]:
                if state in transitions[state][condition]:
                    if self_expression == "":
                        self_expression = condition
                    else:
                        self_expression = ("%s+%s"%(self_expression, condition))
                else:
                    expressions[condition] = transitions[state][condition]
            return ("(%s)*"%self_expression), expressions

        regex = ""
        for final_state in self.final_states:
            new_transitions = copy.deepcopy(self.transitions)
            for state_to_eliminate in self.states:
                if state_to_eliminate == list(self.initial_states)[0] or state_to_eliminate == final_state:
                    continue
                temporal_transitions = copy.deepcopy(new_transitions)
                for state in new_transitions:
                    if state == state_to_eliminate:
                        continue
                    for condition in new_transitions[state]:
                        if state_to_eliminate in new_transitions[state][condition]:
                            self_expression, expressions_to_add = get_expressions(state_to_eliminate, new_transitions)
                            for expression_to_add in expressions_to_add:
                                if condition in temporal_transitions[state]:
                                    del temporal_transitions[state][condition]
                                if self_expression == "()*":
                                    temporal_transitions[state][("%s.%s" % (condition, expression_to_add))] = expressions_to_add[expression_to_add]
                                else:
                                    temporal_transitions[state][("%s.%s.%s"%(condition, self_expression, expression_to_add))] = expressions_to_add[expression_to_add]
                del temporal_transitions[state_to_eliminate]
                new_transitions = copy.deepcopy(temporal_transitions)
            if final_state == list(self.initial_states)[0]:
                regexToAdd, _ = get_expressions(final_state, new_transitions)
                if regex == "":
                    regex = regexToAdd
                else:
                    regex = ("%s + %s"%(regex, regexToAdd))
            else:
                to_self_initial = ""
                to_final = ""
                to_self_final = ""
                to_initial = ""
                for state in new_transitions: # remove this loop and replace fot final_state
                    if state == list(self.initial_states)[0]:
                        to_self_initial, to_final_list = get_expressions(state, new_transitions)
                        for to_final_iterator in to_final_list:
                            if to_final == "":
                                to_final = to_final_iterator
                            else:
                                to_final = ("%s+%s"%(to_final, to_final_iterator))
                        to_final = ("(%s)"%to_final)
                    else:
                        to_self_final, to_initial_list = get_expressions(state, new_transitions)
                        for to_initial_iterator in to_initial_list:
                            if to_initial == "":
                                to_initial = to_initial_iterator
                            else:
                                to_initial = ("%s+%s" % (to_initial, to_initial_iterator))
                        to_initial = ("(%s)" % to_initial)

                regexToAdd = ""
                if to_self_initial != "()*":
                    regexToAdd = to_self_initial
                if to_final != "()":
                    if regexToAdd == "":
                        regexToAdd = to_final
                    else:
                        regexToAdd = ("%s.%s"%(regexToAdd, to_final))
                subset_b = ""
                if to_initial != "()":
                    if to_self_initial != "()":
                        subset_b = ("%s.%s.%s"%(to_initial, to_self_initial, to_final))
                    else:
                        subset_b = ("%s.%s"%(to_initial, to_final))
                subset_a = ""
                if to_self_final != "()*":
                    subset_a = to_self_final
                    if subset_b != "":
                        subset_a = ("%s+%s"%(to_self_final, subset_b))
                elif subset_b != "":
                    subset_a = subset_b
                if subset_a != "":
                    if subset_b != "":
                        regexToAdd = ("%s.(%s)*"%(regexToAdd, subset_a))
                    else:
                        regexToAdd = ("%s.%s" % (regexToAdd, subset_a))
            if regex == "":
                regex = regexToAdd
            else:
                regexToAdd = ("%s+%s"%(regex, regexToAdd))

        return regex

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
        initial_states = set()
        final_states = set()
        for state in table:
            paths = {}
            for symbol in table[state]:
                if symbol == 'states':
                    continue
                _, destiny = self.inKeys(table, table[state][symbol])
                paths[symbol] = [destiny]
            transitions[state] = paths

            for initial_state in self.initial_states:
                if initial_state in table[state]['states']:
                    initial_states.add(state)

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
