from enum import Enum

# pylint: disable=invalid-name
class Score(Enum):
    Love, Fifteen, Thirty, Forty = range(4)

class TennisGame:
    OVERTIME = 4

    def __init__(self, player1, player2):
        self.home_player = player1
        self.away_player = player2
        self.scores = {}
        self.scores[player1] = 0
        self.scores[player2] = 0

    def won_point(self, player):
        self.scores[player] += 1

    def get_score(self):
        home_score = self.scores[self.home_player]
        away_score = self.scores[self.away_player]

        if home_score == away_score:
            return (
                    "Deuce"
                    if home_score >= Score.Forty.value else
                    f"{Score(home_score).name}-All"
                    )

        if home_score >= self.OVERTIME or away_score >= self.OVERTIME:
            score_difference = abs(home_score - away_score)
            difference_status = (
                    "Advantage"
                    if score_difference == 1 else 
                    "Win for"
                    )
            ahead = (
                    self.home_player
                    if home_score > away_score else
                    self.away_player
                    )
            return f"{difference_status} {ahead}"

        return f"{Score(home_score).name}-{Score(away_score).name}"
