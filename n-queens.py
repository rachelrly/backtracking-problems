class NQueensSolver:
    def solve():
        solutions = []
        state = set()
        search (state, solutions)
        return solutions

    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        state = []
        self.search(state, solutions, n)
        return solutions

    def is_valid_state(self, state, n):
        return len(state) == n

    def get_candidates(self, state, n):
        if not state:
            return range(n)
            # bring down candidates that aren't valid
        position = len(state)
        candidates = set(range(n))

        for row, col in enumerate(state):
            # discard occupied index
            candidates.discard(col)
            distance = position - row

            candidates.discard(col + dist)
            candidates.discard(col - dist)
        return candidates

    def search(state, solutions):
        if is_valid_state(state):
            solutions.append(state.copy())

            for candidate in get_candidates(state):
                state.add(candidate)
                search(state, solutions)
                state.remove(candidate)