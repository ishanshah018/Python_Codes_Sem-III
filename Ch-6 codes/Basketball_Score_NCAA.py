#                    Use the file of "scores.txt"

# (a) Find the average of the points scored over all the games in the file.
# (b) Pick your favorite team and scan through the file to determine how many games they won
#     and how many games they lost.
# (c) Find the team(s) that lost by 30 or more points the most times
# (d) Find all the teams that averaged at least 70 points a game.
# (e) Find all the teams that had winning records but were collectively outscored by their opponents.

# A team is collectively outscored by their opponents if the total number of points the team scored
# over all their games is less than the total number of points their opponents scored in their games
# against the team.

file1 = open("scores.txt", "r")
games = [line.split() for line in file1]
file1.close()

# (a) Find the average of points scored
all_scores = [int(game[2]) for game in games] + [int(game[4]) for game in games]
average_score = sum(all_scores) / len(all_scores)
print("(a) Average points scored: " + str(round(average_score, 2)))

# (b) Wins and losses for a favorite team
favorite_team = "AlcornSt."
wins = 0
losses = 0

for game in games:
    team1 = game[1]
    team1_score = int(game[2])
    team2 = game[3]
    team2_score = int(game[4])
    if team1 == favorite_team:
        if team1_score > team2_score:
            wins += 1
        else:
            losses += 1
    elif team2 == favorite_team:
        if team2_score > team1_score:
            wins += 1
        else:
            losses += 1

print("(b) " + favorite_team + " won " + str(wins) + " games and lost " + str(losses) + " games.")

# (c) Teams that lost by 30 or more points the most times
from collections import Counter

large_loss_teams = []

for game in games:
    team1 = game[1]
    team1_score = int(game[2])
    team2 = game[3]
    team2_score = int(game[4])
    if team1_score - team2_score >= 30:
        large_loss_teams.append(team2)
    elif team2_score - team1_score >= 30:
        large_loss_teams.append(team1)

most_losses = Counter(large_loss_teams).most_common(1)
print("(c) Team that lost by 30+ points the most: " + most_losses[0][0] + " (" + str(most_losses[0][1]) + " times)")

# (d) Teams that averaged at least 70 points per game
from collections import defaultdict

team_scores = defaultdict(list)

for game in games:
    team1 = game[1]
    team1_score = int(game[2])
    team2 = game[3]
    team2_score = int(game[4])
    team_scores[team1].append(team1_score)
    team_scores[team2].append(team2_score)

teams_avg_70 = []
for team, scores in team_scores.items():
    if sum(scores) / len(scores) >= 70:
        teams_avg_70.append(team)

print("(d) Teams that averaged at least 70 points per game: " + ", ".join(teams_avg_70))

# (e) Winning records but collectively outscored
team_totals = defaultdict(lambda: {"scored": 0, "conceded": 0, "wins": 0, "losses": 0})

for game in games:
    team1 = game[1]
    team1_score = int(game[2])
    team2 = game[3]
    team2_score = int(game[4])
    team_totals[team1]["scored"] += team1_score
    team_totals[team1]["conceded"] += team2_score
    team_totals[team2]["scored"] += team2_score
    team_totals[team2]["conceded"] += team1_score

    if team1_score > team2_score:
        team_totals[team1]["wins"] += 1
        team_totals[team2]["losses"] += 1
    else:
        team_totals[team2]["wins"] += 1
        team_totals[team1]["losses"] += 1

outscored_winners = []
for team, stats in team_totals.items():
    if stats["wins"] > stats["losses"] and stats["scored"] < stats["conceded"]:
        outscored_winners.append(team)

print("(e) Teams with winning records but collectively outscored: " + ", ".join(outscored_winners))
