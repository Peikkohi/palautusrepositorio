from player_reader import PlayerReader
from enum import Enum

class SortBy(Enum):
    POINTS, GOALS, ASSISTS = range(3)

class StatisticsService:
    def __init__(self, reader):
        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, field=SortBy.POINTS):
        methods = [
                lambda player: player.points,
                lambda player: player.goals,
                lambda player: player.assists,
        ]

        sorted_players = sorted(
            self._players,
            reverse=True,
            key=methods[field.value],
        )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result
