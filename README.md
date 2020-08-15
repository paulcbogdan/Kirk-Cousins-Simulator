# Kirk-Cousins-Simulator
Is Kirk Cousins actually bad against winning teams (5-26; 16%)? Or is this just statistical noise? Original Reddit post: https://www.reddit.com/r/nfl/comments/d5pi91/is_kirk_cousins_actually_bad_against_winning/

I wanted to test how well Kirk Cousins should, in theory, perform against winning teams. I decided to test this by writing a simulation. Code is here. This code runs simulations of a QB playing on the same team for 10 years (16 games per year). Every season the wins and losses of the team are reset, but the QB's wins and losses are not. This 10 year period is simulated many times, and I then looked at what was a QB's win percentage against winning teams after they had played 31 games (Kirk's number of games against winning teams). I then calculated the 90% and 99% confidence intervals using this method.

So first, I tested what happens if a team is counted as a winning team if they became a winning team after the game is already over (so when Kirk loses to a 0-0 team this counts as losing to a winning team). If this is how wins are calculated, then for 31 games played, the expected proportion of wins would be 0.30 [0.17, 0.42]. Kirk, is just right at the edge of this border and would be within a 99% confidence interval [0.10, 0.48]. Because Kirk is within this 99% range, this suggests that even with a mean-spirited way of defining a winning team, Kirk is not necessarily bad!

However, let's think about teams that were winning teams going into the game. Clearly, if every team had just a 50% chance to win, then the expected number of wins against a winning team would be 0.50, and the 90% confidence interval is [0.35, 0.65]. Although, in the NFL, some teams are better than other teams. Hence, to simulate good vs. middling vs. bad teams, I gave each team a random value uniformly selected in the range of (0, 2). This represents their log odds ratio of winning. Then when teams were paired, the likelihood of team A winning was:

       exp(team_A.win_odds_ratio - team_B.win_odds_ratio) / (1+exp(team_A.win_odds_ratio - team_B.win_odds_ratio))

So in an average, random pairing of teams, the favorite had about a 65% chance of winning. This seems in line with what is typical in the NFL. We then find that the expected number of wins at 31 games is 0.42 [0.30, 0.70]. Notably, Kirk falls out of this range, suggesting he is bad against winning teams, but he is within the 99% confidence interval [0.1, 0.77].

However, this range is biased by the fact that teams that are very bad will almost certainly lose to winning teams which causes the interval to become very large. If we only look among teams that had a middling wins-odds-ratio around 1.0, then we find startling results. The expected wins for 31 games is 0.42 [90% = 0.26, 0.58; 99% = 0.19, 0.68]. Kirk falls outside both of these ranges, suggesting that he performs particularly poorly against winning teams. These results may be the most meaningful as they represent the teams run by kirk (middling teams which rarely make the playoffs but have high hopes at the beginning of the season).

Notably, I think if we included some home-field advantage aspect to this simulation, then the ranges would become smaller and Kirk would look even worse.

tl;dr: Kirk is not good against winning teams and this is not just statistical noise.

If anybody sees some major flaws in this or wants to tell me whether "log odds ratio" is the right name for that thing, please do. (EDIT: see https://www.reddit.com/r/nfl/comments/d5pi91/is_kirk_cousins_actually_bad_against_winning/f0nigya/?context=3 for a rebuttal and advanced Kirk stats. EDIT2: https://www.reddit.com/r/nfl/comments/d61xrw/oc_a_statistical_analysis_of_qbs_against_teams/ )

Thanks for reading
