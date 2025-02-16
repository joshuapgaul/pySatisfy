from backtracker import solve
from structures import Variable, Literal, NEGATIVE_LITERAL, POSITIVE_LITERAL, Clause, Circuit, SATStatus

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

def test_simple_unsatisfiability():
    variable = Variable(1)
    # (-v1) and (v1)
    circuit = Circuit( [ Clause([Literal(False, variable)]), Clause([Literal(True, variable)]) ] )
    evaluation = solve([variable], circuit)
    assert evaluation == SATStatus.UNSATISFIABLE


#(-v1) and (v1 or v2) == SATSIFIABLE
def test_simple_two_clause_satisifiable():
    v1 = Variable(1)
    v2 = Variable(2)

    circuit = Circuit( [Clause([NEGATIVE_LITERAL(v1)]), Clause([POSITIVE_LITERAL(v1), POSITIVE_LITERAL(v2)])])
    evaluation = solve([v1, v2], circuit)
    assert evaluation == SATStatus.SATISFIED

    variables_in_circuit = circuit.query_variables()
    assert len(variables_in_circuit) == 2

    
    variable1_in_circuit = [v for v in variables_in_circuit if v.name == 1].pop()
    assert variable1_in_circuit.assignment == False

    variable2_in_circuit = [v for v in variables_in_circuit if v.name == 2].pop()
    assert variable2_in_circuit.assignment == True