from matchers import (
    HasAtLeast,
    PlaysIn,
    HasFewerThan,
    All,
    And,
    Or
)

class Query:
    "builds a query for selecting players based on Conjuctive normal form"
    def __init__(self, predicate=All()):
        self.predicate = predicate

    def _append(self, predicate):
        return Query(And(predicate, self.predicate))

    def has_at_least(self, value, attr):
        return self._append(HasAtLeast(value, attr))

    def plays_in(self, team):
        return self._append(PlaysIn(team))

    def has_fewer_than(self, value, attr):
        return self._append(HasFewerThan(value, attr))

    def one_of(self, *any_of):
        return self._append(Or(*any_of))

    def build(self):
        return self.predicate

