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

    def check(self, epsilon=None):
        pass

    def get_destinies(self, current_state, condition):
        if condition in self.transitions[current_state]:
            return set(self.transitions[current_state][condition])
        return set()

class Automata_DFA(Automata_BARE):
    def __init__(self, states, input_symbols, transitions, initial_state, final_states):
        super().__init__(states, input_symbols, transitions, initial_state, final_states)

    def check(self, epsilon=None):
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

class Automata_EpsilonNFA(Automata_BARE):
    def __init__(self, states, input_symbols, transitions, initial_state, final_states):
        super().__init__(states, input_symbols, transitions, initial_state, final_states)

    def check(self, epsilon=None):
        if len(self.initial_states) == 0:
            raise Exception("An initial state is required to solve.")
        elif len(self.initial_states) > 1:
            raise Exception("There must only be one initial state to solve.")
        elif len(self.final_states) == 0:
            raise Exception("At least one final state is required to solve.")

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

    def transform(self, epsilon):
        def getSetToCalculate(table):
            for state in table:
                for condition in table[state]:
                    if not inKeys(table, table[state][condition]):
                        return table[state][condition]
            return set()

        def inKeys(table, setToFind):
            for state in table:
                if table[state]['states'] == setToFind:
                    return True, state
            return False

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
            states_set = getSetToCalculate(table)
            if len(states_set ) == 0:
                break
        # print(table)
        # _, temp = inKeys(table, table['q0']['states'])
        # print(temp)
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
                _, destiny = inKeys(table, table[state][symbol])
                paths[symbol] = [destiny]
            transitions[state] = paths

            for initial_state in self.initial_states:
                if initial_state in table[state]['states']:
                    initial_states.add(state)

            for final_state in self.final_states:
                if final_state in table[state]['states']:
                    final_states.add(state)

        # print("---HERE---")
        # print("States: {}".format(states))
        # print("Input Symbols: {}".format(input_symbols))
        # print("Transitions: {}".format(transitions))
        # print("Initial States: {}".format(self.initial_states))
        # print("Final States: {}".format(final_states))

        return Automata_BARE(states, input_symbols, transitions, self.initial_states, final_states)

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

class Automamta_Merge(Automata_BARE):
    def __init__(self, states, input_symbols, transitions, initial_state, final_states):
        super().__init__(states, input_symbols, transitions, initial_state, final_states)

    def check(self, epsilon=None):
        if len(self.initial_states) == 0:
            raise Exception("An initial state is required to solve.")
        elif len(self.final_states) == 0:
            raise Exception("At least one final state is required to solve.")

        for state in self.transitions:
            for condition in self.transitions[state]:
                if len(self.transitions[state][condition]) != 1:
                    raise Exception("Node '%s' has more than one connection through '%c'." % (state, condition))

        if epsilon in self.input_symbols:
            raise Exception(("Epsilon('%c') not allowed in DFA graphs"%(epsilon)))

    def merge(self):
        def getSetToCalculate(table):
            for state in table:
                for condition in table[state]:
                    if not self.inKeys(table, table[state][condition]):
                        return table[state][condition]
            return set()

        iterator = 0
        table = {}
        estado_actual = ("q%d"%iterator)
        states_set = self.initial_states
        while True:
            table[estado_actual] = {}
            table[estado_actual]['states'] = states_set
            for state in table[estado_actual]['states']:
                for symbol in self.transitions[state]:
                    if symbol not in table[estado_actual]:
                        table[estado_actual][symbol] = set()
                    table[estado_actual][symbol] = table[estado_actual][symbol] | self.get_destinies(state, symbol)
            iterator = iterator + 1
            estado_actual = ("q%d" % iterator)
            states_set = getSetToCalculate(table)
            if len(states_set ) == 0:
                break
        return table

    def inKeys(self, table, setToFind):
        for state in table:
            if table[state]['states'] == setToFind:
                return True, state
        return False


class Automata_Union(Automamta_Merge):
    def __init__(self, states, input_symbols, transitions, initial_state, final_states):
        super().__init__(states, input_symbols, transitions, initial_state, final_states)

    def transform(self, epsilon=None):
        table = self.merge()
        states = set([state for state in table])
        input_symbols = set()
        for state in table:
            for symbol in table[state]:
                if symbol != 'states':
                    input_symbols.add(symbol)
        transitions = {}

        if 'q0' in table:
            initial_states = set(list(['q0']))
        else:
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

            for final_state in self.final_states:
                if final_state in table[state]['states']:
                    final_states.add(state)

        print("---HERE---")
        print("States: {}".format(states))
        print("Input Symbols: {}".format(input_symbols))
        print("Transitions: {}".format(transitions))
        print("Initial States: {}".format(self.initial_states))
        print("Final States: {}".format(final_states))

        return Automata_BARE(states, input_symbols, transitions, initial_states, final_states)

class Automata_Intersection(Automamta_Merge):
    def __init__(self, states, input_symbols, transitions, initial_state, final_states):
        super().__init__(states, input_symbols, transitions, initial_state, final_states)

    def transform(self, epsilon=None):
        table = self.merge()
        states = set([state for state in table])
        input_symbols = set()
        for state in table:
            for symbol in table[state]:
                if symbol != 'states':
                    input_symbols.add(symbol)
        transitions = {}

        if 'q0' in table:
            initial_states = set(list(['q0']))
        else:
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

            if table[state]['states'] == self.final_states:
                final_states.add(state)

        print("---HERE---")
        print("States: {}".format(states))
        print("Input Symbols: {}".format(input_symbols))
        print("Transitions: {}".format(transitions))
        print("Initial States: {}".format(self.initial_states))
        print("Final States: {}".format(final_states))

        return Automata_BARE(states, input_symbols, transitions, initial_states, final_states)

class Automata_Difference(Automamta_Merge):
    def __init__(self, states, input_symbols, transitions, initial_state, final_states):
        super().__init__(states, input_symbols, transitions, initial_state, final_states)

    def transform(self, epsilon=None):
        table = self.merge()
        states = set([state for state in table])
        input_symbols = set()
        for state in table:
            for symbol in table[state]:
                if symbol != 'states':
                    input_symbols.add(symbol)
        transitions = {}

        if 'q0' in table:
            initial_states = set(list(['q0']))
        else:
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

            for final_state in self.getFinalStates({'q0'}):
                if (final_state in table[state]['states']) and (len(self.getFinalStates({'q1'}) & table[state]['states'])) == 0:
                    final_states.add(state)

        print("---HERE---")
        print("States: {}".format(states))
        print("Input Symbols: {}".format(input_symbols))
        print("Transitions: {}".format(transitions))
        print("Initial States: {}".format(self.initial_states))
        print("Final States: {}".format(final_states))

        return Automata_BARE(states, input_symbols, transitions, initial_states, final_states)

    def getFinalStates(self, initialNode):
        nodesToCheck = initialNode
        checkedNodes = set()
        while True:
            for node in nodesToCheck:
                if node in checkedNodes:
                    continue
                for condition in self.transitions[node]:
                    nodesToCheck = nodesToCheck | set(self.transitions[node][condition])
                checkedNodes = checkedNodes | {node}
            if len(nodesToCheck) == len(checkedNodes):
                break
        return set([state for state in checkedNodes if state in self.final_states])

class Automata_Complement(Automata_BARE):
    def __init__(self, states, input_symbols, transitions, initial_state, final_states):
        super().__init__(states, input_symbols, transitions, initial_state, final_states)

    def check(self, epsilon=None):
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

    def transform(self, epsilon=None):
        final_states = set()
        for state in self.states:
            if state not in self.final_states:
                final_states = final_states | {state}

        self.transitions['\u221E'] = {}
        self.states = self.states | {'\u221E'}
        final_states = final_states | {'\u221E'}

        for state in self.transitions:
            for condition in self.input_symbols:
                if condition not in self.transitions[state]:
                    self.transitions[state][condition] = ['\u221E']

        return Automata_BARE(self.states, self.input_symbols, self.transitions, self.initial_states, final_states)

class Automata_Minimize(Automata_BARE):
    def __init__(self, states, input_symbols, transitions, initial_state, final_states):
        super().__init__(states, input_symbols, transitions, initial_state, final_states)

    def check(self, epsilon=None):
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

    def transform(self, epsilon):
        def findGroup(table, stateToPlace):
            found = False
            for state in table:
                for condition in table[state]:
                    if condition == 'states':
                        continue
                    if condition not in self.transitions[stateToPlace]:
                        found = False
                        break
                    if list(table[state][condition])[0] == findState(table, self.transitions[stateToPlace][condition][0]):
                        found = True
                    else:
                        found = False
                        break
                if found:
                    if (list(table[state]['states'])[0] in self.final_states and stateToPlace in self.final_states) or (list(table[state]['states'])[0] not in self.final_states and stateToPlace not in self.final_states):
                        table[state]['states'] = table[state]['states'] | {stateToPlace}
                        setStates(table)
                        return True
                    else:
                        found = False
            if not found:
                return False
        def setStates(table):
            for state in table:
                for condition in self.transitions[list(table[state]['states'])[0]]:
                    table[state][condition] = {findState(table, self.transitions[list(table[state]['states'])[0]][condition][0])}
        def findState(table, state):
            for newState in table:
                if state in table[newState]['states']:
                    return newState

        iterator = 0
        table = {}
        estado_actual = ("q%d"%iterator)
        table[estado_actual] = {}
        table[estado_actual]['states'] = self.final_states
        if len(self.states) > len(self.final_states):
            iterator+=1
            estado_actual = ("q%d"%iterator)
            table[estado_actual] = {}
            table[estado_actual]['states'] = self.states - self.final_states
        setStates(table)

        previousLen = len(table)
        while True:
            for state in self.states:
                for condition in table[findState(table, state)]:
                    if condition == 'states':
                        continue
                    if list(table[findState(table, state)][condition])[0] != findState(table, self.transitions[state][condition][0]):
                        table[findState(table, state)]['states'].remove(state)
                        if not findGroup(table, state):
                            iterator += 1
                            estado_actual = ("q%d" % iterator)
                            table[estado_actual] = {}
                            table[estado_actual]['states'] = {state}
                            setStates(table)
                            break
            if len(table) == previousLen:
                break
            previousLen = len(table)

        states = set([state for state in table])
        transitions = {}
        initial_states = set()
        final_states = set()
        for state in table:
            paths = {}
            for symbol in table[state]:
                if symbol == 'states':
                    continue
                paths[symbol] = table[state][symbol]
            transitions[state] = paths

            for initial_state in self.initial_states:
                if initial_state in table[state]['states']:
                    initial_states.add(state)

            for final_state in self.final_states:
                if final_state in table[state]['states']:
                    final_states.add(state)

        print("AQUIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
        print(table)
        return Automata_BARE(states, self.input_symbols, transitions, initial_states, final_states)

class Automata_RegularExpression_EpsilonNFA:
    def __init__(self):
        self.transitions = {}
        self.lastNode = 0
        self.WindowTitle = "Regular Expression ⇨ Ɛ-NFA"

    def transform(self, expression, epsilon):
        from parser import parse
        def desipherObject(object, epsilon):
            import ast

            if isinstance(object, ast.Digit):
                return ("%d" % object.number)
            elif isinstance(object, ast.Letter):
                return object.letter
            elif isinstance(object, ast.Concat):
                left = desipherObject(object.left_expr, epsilon)
                self.transitions[("q%d" % self.lastNode)] = {}
                self.transitions[("q%d" % self.lastNode)][left] = set(list(["q%d" % (self.lastNode + 1)]))
                self.lastNode += 1
                self.transitions[("q%d" % self.lastNode)] = {}
                self.transitions[("q%d" % self.lastNode)][epsilon] = set(list(["q%d" % (self.lastNode + 1)]))
                self.lastNode += 1
                right = desipherObject(object.right_expr, epsilon)
                self.transitions[("q%d" % self.lastNode)] = {}
                self.transitions[("q%d" % self.lastNode)][right] = set(list(["q%d" % (self.lastNode + 1)]))
                self.lastNode += 1
                self.transitions[("q%d" % self.lastNode)] = {}
                return epsilon
            elif isinstance(object, ast.Or):
                root = self.lastNode
                self.transitions[("q%d" % self.lastNode)] = {}
                self.transitions[("q%d" % self.lastNode)][epsilon] = set(list(["q%d" % (self.lastNode + 1)]))
                self.lastNode += 1
                left = desipherObject(object.left_expr, epsilon)
                self.transitions[("q%d" % self.lastNode)] = {}
                self.transitions[("q%d" % self.lastNode)][left] = set(list(["q%d" % (self.lastNode + 1)]))
                self.lastNode += 1
                self.transitions[("q%d" % self.lastNode)] = {}
                self.transitions[("q%d" % self.lastNode)][epsilon] = set(list(["q%d" % (self.lastNode + 1)]))
                self.lastNode += 1
                tail = self.lastNode
                self.transitions[("q%d" % root)][epsilon] = self.transitions[("q%d" % root)][
                                                                epsilon] | set(
                    list(["q%d" % (self.lastNode + 1)]))
                self.lastNode += 1
                right = desipherObject(object.right_expr, epsilon)
                self.transitions[("q%d" % self.lastNode)] = {}
                self.transitions[("q%d" % self.lastNode)][right] = set(list(["q%d" % (self.lastNode + 1)]))
                self.lastNode += 1
                self.transitions[("q%d" % self.lastNode)] = {}
                self.transitions[("q%d" % self.lastNode)][epsilon] = set(list(["q%d" % (tail)]))
                self.transitions[("q%d" % tail)] = {}
                self.transitions[("q%d" % tail)][epsilon] = set(list(["q%d" % (self.lastNode + 1)]))
                self.lastNode += 1
                self.transitions[("q%d" % self.lastNode)] = {}
                return epsilon
            elif isinstance(object, ast.Kleene):
                root = self.lastNode
                self.transitions[("q%d" % self.lastNode)] = {}
                self.transitions[("q%d" % self.lastNode)][epsilon] = set(list(["q%d" % (self.lastNode + 1)]))
                self.lastNode += 1
                loop = self.lastNode
                value = desipherObject(object.expression, epsilon)
                self.transitions[("q%d" % self.lastNode)] = {}
                self.transitions[("q%d" % self.lastNode)][value] = set(list(["q%d" % (self.lastNode + 1)]))
                self.lastNode += 1
                self.transitions[("q%d" % self.lastNode)] = {}
                self.transitions[("q%d" % self.lastNode)][epsilon] = set(list(["q%d" % (self.lastNode + 1)]))
                self.transitions[("q%d" % self.lastNode)][epsilon] = self.transitions[("q%d" % self.lastNode)][
                                                                         epsilon] | set(
                    list(["q%d" % (loop)]))
                self.lastNode += 1
                self.transitions[("q%d" % root)][epsilon] = self.transitions[("q%d" % root)][
                                                                epsilon] | set(
                    list(["q%d" % (self.lastNode)]))
                self.transitions[("q%d" % self.lastNode)] = {}
                return epsilon
        expression_tree = parse(expression)
        desipherObject(expression_tree, epsilon)
        states = list()
        for node in range(self.lastNode + 1):
            states.append("q%d" % (node))  ##Change to |=
        states = set(states)
        input_symbols = set()
        for node in self.transitions:
            input_symbols = input_symbols | set(self.transitions[node])
        initial_states = set(list(["q0"]))
        final_states = set(list(["q%d" % self.lastNode]))

        return Automata_BARE(states, input_symbols, self.transitions, initial_states, final_states)

class Automata_Reflection:
    def __init__(self):
        self.WindowTitle = "Reflection"

    def transform(self, expression, epsilon):
        from parser import parse
        def desipherObject(object):
            import ast
            if isinstance(object, ast.Digit):
                return ("%d"%object.number)
            elif isinstance(object, ast.Letter):
                return object.letter
            elif isinstance(object, ast.Concat):
                left = desipherObject(object.left_expr)
                right = desipherObject(object.right_expr)
                return ("%s.%s")%(right, left)
            elif isinstance(object, ast.Or):
                left = desipherObject(object.left_expr)
                right = desipherObject(object.right_expr)
                return ("(%s + %s)") % (left, right)
            elif isinstance(object, ast.Kleene):
                expression = desipherObject(object.expression)
                return ("%s*") % (expression)
        return desipherObject(parse(expression))

class Automata_PDA(Automata_BARE):
    def __init__(self, states, input_symbols, transitions, initial_state, final_states):
        super().__init__(states, input_symbols, transitions, initial_state, final_states)
        self.current_states = []

    def check(self, epsilon=None):
        if len(self.initial_states) == 0:
            raise Exception("An initial state is required to solve.")
        elif len(self.initial_states) > 1:
            raise Exception("There must only be one initial state to solve.")
        elif len(self.final_states) == 0:
            raise Exception("At least one final state is required to solve.")

    def solve(self, sequence, epsilon):
        import queue, copy
        def solveSnapshot(snapshot, new_current_states):
            try:
                pileTop = snapshot['pile'].get()
            except:
                self.current_states.remove(snapshot)
                return
            if len(snapshot['sequence']) > 0:
                if snapshot['sequence'][0] in self.transitions[snapshot['state']]:
                    for destiny in self.transitions[snapshot['state']][snapshot['sequence'][0]]:
                        for popValue in self.transitions[snapshot['state']][snapshot['sequence'][0]][destiny]:
                            if popValue == pileTop:
                                for pushValueGroup in self.transitions[snapshot['state']][snapshot['sequence'][0]][destiny][popValue]:
                                    print(self.transitions[snapshot['state']][snapshot['sequence'][0]][destiny][popValue])
                                    print("Separator")
                                    print(pushValueGroup)
                                    snapshot_to_add = {}
                                    snapshot_to_add['pile'] = queue.LifoQueue()
                                    for item in snapshot['pile'].queue:
                                        snapshot_to_add['pile'].put(item)
                                    for pushValue in pushValueGroup[::-1]:
                                        if pushValue != epsilon:
                                            snapshot_to_add['pile'].put(pushValue)
                                    # if len(snapshot_to_add['pile'].queue) * 2 > len(snapshot['sequence']): ############possible hot fix
                                    #     continue
                                    snapshot_to_add['state'] = destiny
                                    snapshot_to_add['sequence'] = snapshot['sequence']
                                    snapshot_to_add['sequence'] = snapshot_to_add['sequence'][1:]################pass up################
                                    new_current_states.append(snapshot_to_add)
            elif snapshot['state'] in self.final_states:
                return True
            if epsilon in self.transitions[snapshot['state']]:
                for destiny in self.transitions[snapshot['state']][epsilon]:
                    for popValue in self.transitions[snapshot['state']][epsilon][destiny]:
                        if popValue == pileTop:
                            for pushValueGroup in self.transitions[snapshot['state']][epsilon][destiny][popValue]:
                                snapshot_to_add = {}
                                snapshot_to_add['pile'] = queue.LifoQueue()
                                for item in snapshot['pile'].queue:
                                    snapshot_to_add['pile'].put(item)
                                for pushValue in pushValueGroup[::-1]:
                                    if pushValue != epsilon:
                                        snapshot_to_add['pile'].put(pushValue)
                                # if len(snapshot_to_add['pile'].queue) * 2 > len(snapshot['sequence']): ############possible hot fix
                                #     continue
                                snapshot_to_add['state'] = destiny
                                snapshot_to_add['sequence'] = snapshot['sequence']
                                snapshot_to_add['sequence'] = snapshot_to_add['sequence']################remove################
                                new_current_states.append(snapshot_to_add)
            return False

        self.current_states.append({'state': list(self.initial_states)[0], 'sequence': sequence, 'pile': queue.LifoQueue()})
        self.current_states[0]['pile'].put('~')
        while True:
            if len(self.current_states) == 0:
                raise Exception('{} is NOT a solution'.format(sequence))
            new_current_states = []
            for current_state in self.current_states:
                if solveSnapshot(current_state, new_current_states):
                    self.current_states = []
                    return
            self.current_states = new_current_states

class languageDefenition:
    def __init__(self, language):
        self.language = language

    def solve(self, epsilon):
        transitions = {'q0': {epsilon: {'q1': {'~': ['E~']}}}, 'q1': {epsilon: {'q2': {'~': [epsilon]}, 'q1': {}}}}
        for entry in self.language:
            transitions['q1'][epsilon]['q1'][entry] = []
            for pushValues in self.language[entry]:
                transitions['q1'][epsilon]['q1'][entry].append(pushValues)

        for entry in self.language:
            for pushValues in self.language[entry]:
                for symbol in pushValues:
                    if symbol not in transitions['q1'][epsilon]['q1']:
                        transitions['q1'][symbol] = {'q1': {symbol: epsilon}}


        states = ['q0', 'q1', 'q2']
        input_symbols = []
        for key in transitions:
            for symbol in transitions[key]:
                input_symbols.append(symbol)
        initial_states = ['q0']
        final_states = ['q2']

        return Automata_BARE(set(states), set(input_symbols), transitions, set(initial_states), set(final_states))


class languageGenerator(Automata_BARE):
    def __init__(self, states, input_symbols, transitions, initial_state, final_states):
        super().__init__(states, input_symbols, transitions, initial_state, final_states)

    def solve(self, epsilon):
        language = {}
        language['S'] = []
        for final_state in self.final_states:
            language['S'].append("%s%c%s"%(list(self.initial_states)[0],"~", final_state))

        for state in self.states:
            for condition in self.transitions[state]:
                for destiny in self.transitions[state][condition]:
                    for popValue in self.transitions[state][condition][destiny]:
                        for pushValueGroup in self.transitions[state][condition][destiny][popValue]:
                            if pushValueGroup == '?':
                                language["%s%c%s"%(state, popValue, destiny)] = condition

        print(language)