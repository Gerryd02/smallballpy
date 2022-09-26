import pandas as pd
import os

from settings import *

pd.options.display.max_rows = 100
pd.options.display.max_columns = 100
pd.options.display.width = 999

batters = pd.read_csv(BATTERS, encoding="utf-8")
pitchers = pd.read_csv(PITCHERS, encoding="utf-8")
#test

# batters['1B'] = batters['H'] - (batters['2B'] + batters['3B'] + batters['HR'])
# batters['1B_points'] = batters['1B'] * BATTER_POINTS['1B']
# batters['2B_points'] = batters['2B'] * BATTER_POINTS['2B']
# batters['3B_points'] = batters['3B'] * BATTER_POINTS['3B']
# batters['HR_points'] = batters['HR'] * BATTER_POINTS['HR']
# batters['HBP_points'] = batters['HBP_points'] * BATTER_POINTS['HBP']


def get_batters_total_points(batters):
    batters['total_points'] = batters['1B_points'] + batters['2B_points'] + batters['3B_points'] + batters[
        'HR_points'] + \
                              batters['BB_points'] + batters['HBP_points'] + batters['SO_points'] + batters[
                                  'SB_points'] + \
                              batters['CS_points'] + batters['RBI_points'] + batters['R_points']


def add_hr_rib_strikeouts(batters):
    return batters['HR_points'] + batters['RBI_points'] + batters['SO_points']


def add_net_steals(batters):
    return batters['SB_points'] + batters['CS_points']


def get_batter_point_projections(batters):
    return batters[['Player', 'Positions', '1B_points', '2B_points', '3B_points', 'HR_points', 'RBI_points',
                    'BB_points', 'SB_points', 'HBP_points', 'R_points', 'net_steal_points',
                    'hr_rbi_strikeouts', 'total_points']]


point_projections = point_projections.sort_values(by='total_points', ascending=False)
batters.sort_values(by='total_points', ascending=False, inplace=True)

top_1b = get_top_13('1B')
top_2b = get_top_13('2B')
top_3b = get_top_13('3B')
top_ss = get_top_13('SS')
top_c = get_top_13('C')
top_lf = get_top_13('LF')
top_rf = get_top_13('RF')
top_cf = get_top_13('CF')
top_dh = get_top_13('DH')

POSITIONS = {'C': top_c, '1B': top_1b, '2B': top_2b, '3B': top_3b, 'SS': top_ss, 'CF': top_cf,
             'LF': top_lf, 'RF': top_rf, 'DH': top_dh}
position_var = {'C': 0, '1B': 0, '2B': 0, '3B': 0, 'SS': 0, 'CF': 0, 'LF': 0, 'RF': 0, 'DH': 0}

for position, top_players in POSITIONS.items():
    position_var[position] = value_above_replacement(top_players, position)

print(position_var)
