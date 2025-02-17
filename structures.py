from dataclasses import dataclass
from enum import Enum

@dataclass
class Variable:
    name: int
    assignment: bool = None


class SATStatus(Enum):
    POSSIBLE = 1
    SATISFIED = 2
    UNSATISFIABLE = 3

NEGATIVE_LITERAL = lambda variable: Literal(False, variable)
POSITIVE_LITERAL = lambda variable: Literal(True, variable)

@dataclass
class Literal:
    sign: bool
    variable: Variable

    def evaluate(self) -> SATStatus:
        if self.variable.assignment == None:
            return SATStatus.POSSIBLE

        boolean = self.variable.assignment if self.sign else not self.variable.assignment
        return SATStatus.SATISFIED if boolean else SATStatus.UNSATISFIABLE 

@dataclass
class Clause:
    literals: list[Literal]

    def evaluate(self) -> SATStatus:
        stillPossible = False
        for literal in self.literals:
            if literal.evaluate() == SATStatus.SATISFIED:
                return SATStatus.SATISFIED
            if literal.evaluate() == SATStatus.POSSIBLE:
                stillPossible = True
        return SATStatus.POSSIBLE if stillPossible else SATStatus.UNSATISFIABLE

@dataclass
class Circuit:
    clauses: list[Clause]

    def evaluate(self) -> SATStatus:
        for clause in self.clauses:
            evaluation = clause.evaluate()
            if evaluation == SATStatus.UNSATISFIABLE:
                return SATStatus.UNSATISFIABLE
            
            if evaluation == SATStatus.POSSIBLE:
                return SATStatus.POSSIBLE

        return SATStatus.SATISFIED
    
    def query_variables(self) -> list[Variable]:
        variables = []
        variable_names = set([])
        for clause in self.clauses:
            for literal in clause.literals:
                if literal.variable.name not in variable_names:
                    variables.append(literal.variable)
                    variable_names.add(literal.variable.name)
        
        return variables
    

def one_hot_encoding(variables: list[Variable]) -> list[Clause]:
    if len(variables ) < 1:
        raise ValueError('There must be at least one variable for a one hot encoding!')

    AT_LEAST_ONE_CLAUSE = Clause([ POSITIVE_LITERAL(variable) for variable in variables])
    clauses = [AT_LEAST_ONE_CLAUSE]

    ## No more than one clauses
    for x in range(len(variables)):
        for y in range(x + 1, len(variables)):
            clauses.append( Clause([ NEGATIVE_LITERAL(variables[x]), NEGATIVE_LITERAL(variables[y]) ]))
    
    return clauses