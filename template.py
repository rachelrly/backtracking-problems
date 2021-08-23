def is_valid_state(state):
    return True


def get_candidates(state):
    # get candidates to see if is valid in next state
    return []

def search(state, solutions):
    # checks if state is valid solution
    if is_valid_state(state):
        # records valid solution as deep copy
        solutions.append(state.copy())
        # return 
        # if you are only looking for one valid solution

        for candidate in get_candidates(state):
            # gets candidates for next valid solution to test
            state.add(candidate)
            # validates state with recursion
            search(state, solutions)
            state.remove(candidate)

def solve():
    solutions = []
    state = set()
    search (state, solutions)
    return solutions