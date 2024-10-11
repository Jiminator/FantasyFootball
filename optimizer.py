from itertools import combinations

def optimize_lineup(players):
    # Filter out unhealthy players
    healthy_players = [p for p in players if p[3] == 'healthy']
    
    # Separate players by roles
    qbs = [p for p in healthy_players if p[2] == 'QB']
    rbs = [p for p in healthy_players if p[2] == 'RB']
    wrs = [p for p in healthy_players if p[2] == 'WR']
    tes = [p for p in healthy_players if p[2] == 'TE']
    
    # If there aren't enough players for a valid lineup, return None
    if len(qbs) < 1 or len(rbs) < 2 or len(wrs) < 2 or len(tes) < 1:
        return None
    
    # Helper function to calculate total projected points
    def projected_points(lineup):
        return sum(player[1] for player in lineup)
    
    best_lineup = None
    best_points = 0
    
    # Iterate through all valid combinations of 1 QB, 2 RB, 2 WR, 1 TE
    for qb in combinations(qbs, 1):
        for rb_pair in combinations(rbs, 2):
            for wr_pair in combinations(wrs, 2):
                for te in combinations(tes, 1):
                    # Flex can be a WR, RB, or TE (excluding the selected QB, RBs, WRs, and TE)
                    remaining_players = [p for p in healthy_players if p not in qb + rb_pair + wr_pair + te and p[2] in ['RB', 'WR', 'TE']]
                    for flex in combinations(remaining_players, 1):
                        lineup = qb + rb_pair + wr_pair + te + flex
                        points = projected_points(lineup)
                        if points > best_points:
                            best_points = points
                            best_lineup = lineup
    
    return best_lineup, best_points
# Example usage:
players = [
    ('Love', 18, 'QB', 'healthy'),
    ('Irving', 10, 'RB', 'healthy'),
    ('Jacobs', 14.8, 'RB', 'healthy'),
    ('Higgins', 14.7, 'WR', 'healthy'),
    ('Brown', 17.0, 'WR', 'healthy'),
    ('Kmet', 7.3, 'TE', 'healthy'),
    ('Hopkins', 10.5, 'WR', 'healthy'),
    ('Allgeier', 8.2, 'RB', 'healthy'),
    ('Pat', 8.1, 'TE', 'Q'),
    ('Goff', 14.4, 'QB', 'healthy'),
    ('Mixon', 16.9, 'RB', 'Q'),
    ('Odunze', 10.1, 'WR', 'healthy'),
    ('Shakir', 9.9, 'WR', 'Q'),
    ('Williams', 0, 'RB', 'Q'),
    ('Rice', 0, 'WR', 'Q'),
]

best_lineup, points = optimize_lineup(players)
print(f'Best lineup: {best_lineup}')
print(f'Total projected points: {points}')