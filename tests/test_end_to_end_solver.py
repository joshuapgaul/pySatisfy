from backtracker import solve
from structures import Variable, Literal, Clause, Circuit, SATStatus

def test_one_positive_literal_one_clause_circuit():
    variable = Variable(1)
    circuit = Circuit( [ Clause([Literal(True, variable)]) ])
    evaluation = solve([variable], circuit)
    assert evaluation == SATStatus.SATISFIED

    variable_in_circuit = circuit.query_variables()[0]
    assert variable_in_circuit.name == variable.name
    assert variable_in_circuit.assignment == True

def test_one_negative_literal_one_clause_circuit():
    variable = Variable(1)
    circuit = Circuit( [ Clause([Literal(False, variable)]) ])
    evaluation = solve([variable], circuit)
    assert evaluation == SATStatus.SATISFIED

    variable_in_circuit = circuit.query_variables()[0]
    assert variable_in_circuit.name == variable.name
    assert variable_in_circuit.assignment == False