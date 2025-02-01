from structures import Variable, Literal, Clause, Circuit, SATStatus


def solve(variables: list[Variable], circuit: Circuit) -> SATStatus:
    evaluation = circuit.evaluate()
    if evaluation == SATStatus.SATISFIED:
        return SATStatus.SATISFIED
    
    if len(variables) == 0:
        return SATStatus.UNSATISFIABLE

    if evaluation == SATStatus.POSSIBLE:
        variables[0].assignment = True
        evaluation = solve(variables[1:], circuit)
        if evaluation == SATStatus.UNSATISFIABLE:
            variables[0].assignment = False
            evaluation = solve(variables[1:], circuit)
            if evaluation == SATStatus.UNSATISFIABLE:
                variables[0].assignment = None
                return SATStatus.UNSATISFIABLE

        if evaluation == SATStatus.SATISFIED:
            return SATStatus.SATISFIED
    
    return SATStatus.UNSATISFIABLE