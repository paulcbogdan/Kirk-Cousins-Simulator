import random
from copy import deepcopy
import statistics as stat
from math import exp
 
print(exp(1))
class Team():
    def __init__(self, qb_wins_threshold=0.51, winning_teams=True, win_odds_ratio=1):
        self.wins = 0
        self.losses = 0
        self.qb_wins = 0
        self.qb_losses = 0
        self.qb_wins_threshold = qb_wins_threshold
        self.winning_teams = winning_teams
        self.win_odds_ratio = win_odds_ratio
 
    def reset_season(self):
        self.wins = 0
        self.losses = 0
 
    def win(self):
        self.wins += 1
 
    def win_update_qb(self, other_team):
        if self.qb_wins_threshold == None:
            return
        if other_team.win_loss() > self.qb_wins_threshold and self.winning_teams:
            self.qb_wins += 1
        elif other_team.win_loss() < self.qb_wins_threshold and not self.winning_teams:
            self.qb_wins += 1
 
    def loss(self):
        self.losses += 1
 
    def loss_update_qb(self, other_team):
        if self.qb_wins_threshold == None:
            return
        if other_team.win_loss() > self.qb_wins_threshold and self.winning_teams:
            self.qb_losses += 1
        elif other_team.win_loss() < self.qb_wins_threshold and not self.winning_teams:
            self.qb_losses += 1
 
    def win_loss(self):
        if self.wins + self.losses == 0:
            return None
        else:
            return self.wins / (self.wins+self.losses)
 
    def get_QB_stats(self):
        num_games = self.qb_wins + self.qb_losses
        return (num_games, self.qb_wins)
 
class stats_manager():
    def __init__(self):
        self.num_games_dict = {}
 
    def update(self, tup):
        if tup[0] == 0:
            return
        if tup[0] not in self.num_games_dict:
            self.num_games_dict[tup[0]] = []
        self.num_games_dict[tup[0]].append(tup[1] / tup[0])
 
    def print_stats(self, lower=0.005, higher=0.995):
        num_games = list(self.num_games_dict.keys())
        num_games.sort()
        for num in num_games:
            self.num_games_dict[num].sort()
            low_idx = int(len(self.num_games_dict[num])*lower)
            high_idx = int(len(self.num_games_dict[num])*higher)
            low_val = self.num_games_dict[num][low_idx]
            mid_val = stat.median(self.num_games_dict[num])
            high_val = self.num_games_dict[num][high_idx]
            print('Num games:', num, 'low:', round(low_val,2), 'mid:', round(mid_val,2), 'high:', round(high_val,2), 'n =', len(self.num_games_dict[num]))
 
 
sm = stats_manager()
 
num_sims = 1000
 
for sim in range(num_sims):
    num_teams = 32
    teams = [Team(win_odds_ratio=1) for i in range(0, num_teams)]
    team_map = {}
    i = 0
    for team in teams:
        team_map[i] = team
        i += 1
    season_len = 16
    num_seasons = 10
 
    for season in range(num_seasons):
        for game in range(season_len):
            random_team_order = [i for i in range(num_teams)]
            random.shuffle(random_team_order)
            random_team_pairs = [(random_team_order[i], random_team_order[i+1]) for i in range(0, num_teams, 2)]
            for idx_A, idx_B in random_team_pairs:
                team_A = team_map[idx_A]
                team_B = team_map[idx_B]
                if random.random() > exp(team_A.win_odds_ratio - team_B.win_odds_ratio) / (1+exp(team_A.win_odds_ratio - team_B.win_odds_ratio)):
                    team_A.win()
                    team_B.loss()
                    team_A.win_update_qb(team_B)
                    team_B.loss_update_qb(team_A)
                else:
                    team_A.loss()
                    team_B.win()
                    team_B.win_update_qb(team_A)
                    team_A.loss_update_qb(team_B)
 
            for team in teams:
                #if 2.5 > team.win_odds_ratio > 1.5:
                sm.update(team.get_QB_stats())
        for team in teams:
            team.reset_season()
 
avg = []
for team_A in teams:
    for team_B in teams:
        favorite = 0.5 + abs(0.5-exp(team_A.win_odds_ratio - team_B.win_odds_ratio) / (1+exp(team_A.win_odds_ratio - team_B.win_odds_ratio)))
        avg.append(favorite)
 
sm.print_stats()
print('Avg favorite:', stat.mean(avg))
 
#for team in teams:
#    print(team.get_QB_stats())