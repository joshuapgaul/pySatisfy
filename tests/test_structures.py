from structures import Variable, Clause, NEGATIVE_LITERAL, POSITIVE_LITERAL, one_hot_encoding, Circuit, SATStatus

def test_one_hot_encoder():
    v1 = Variable(1)
    v2 = Variable(2)
    v3 = Variable(3)

    actual_clauses = one_hot_encoding([v1, v2, v3])

    expected_clauses = [  
        Clause([ POSITIVE_LITERAL(x) for x in [v1,v2,v3]]), # (v1 or v2 or v2)
        Clause([NEGATIVE_LITERAL(v1), NEGATIVE_LITERAL(v2)]), # (-v1 or -v2)
        Clause([NEGATIVE_LITERAL(v1), NEGATIVE_LITERAL(v3)]), # (-v1 or -v3)
        Clause([NEGATIVE_LITERAL(v2), NEGATIVE_LITERAL(v3)]) # (-v2 or -v3)
    ] 

    for expected_clause in expected_clauses:
        assert expected_clause in actual_clauses
    
    ##Test my one hot encoding enforces at least one and at most one
    circuit = Circuit(actual_clauses)

    assert circuit.evaluate() == SATStatus.POSSIBLE

    cases = [
        ( [True, False, False], SATStatus.SATISFIED ),
        ( [False, True, False], SATStatus.SATISFIED ),
        ( [False, False, True], SATStatus.SATISFIED ),

        ( [True, True, False], SATStatus.UNSATISFIABLE ),
        ( [True, False, True], SATStatus.UNSATISFIABLE ),
        ( [False, True, True], SATStatus.UNSATISFIABLE ),
        
        ( [True, None, False], SATStatus.POSSIBLE ),
        ( [True, False, None], SATStatus.POSSIBLE )
    ]

    for assignments, outcome in cases:
        v1.assignment, v2.assignment, v3.assignment = assignments[0], assignments[1], assignments[2]
        assert circuit.evaluate() == outcome
        v1.assignment, v2.assignment, v3.assignment == None