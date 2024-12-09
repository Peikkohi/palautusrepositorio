from matchers import (
    HasAtLeast,
    PlaysIn,
    HasFewerThan,
    All,
    And,
    Or
)

# class Query:
#     def __init__(self, predicate=lambda _: True):
#         self.predicate = predicate
# 
#     @staticmethod
#     def _conjunction(predicate_a, predicate_b):
#         return lambda player: predicate_a(player) and predicate_b(player)
# 
#     def _append(self, predicate):
#         return Query(self._conjunction(predicate, self.predicate))
# 
#     @staticmethod
#     def _has_at_least(value, attr):
#         return lambda player: getattr(player, attr) >= value
# 
#     def has_at_least(self, value, attr):
#         return self._append(self._has_at_least(value, attr))
# 
#     @staticmethod
#     def _plays_in(team):
#         return lambda player: player.team == team
# 
#     def plays_in(self, team):
#         return self._append(self._plays_in(team))
# 
#     @staticmethod
#     def _negate(predicate):
#         return lambda player: not predicate(player)
# 
#     def has_fewer_than(self, value, attr):
#         return self._append(self._negate(self._has_at_least))
# 
#     @staticmethod
#     def _one_of(*predicates):
#         return lambda player: any(predicate(player) for predicate in predicates)
# 
#     def one_of(self, *predicates):
#         return self._append(self._one_of(*predicates))
# 
#     def build(self):
#         return self.predicate

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

