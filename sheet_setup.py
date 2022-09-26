import pandas as pd

from settings import *


def get_batter_points(batters):
    for k, v in BATTER_POINTS.items():
        if k == '1B':
            batters['1B'] = batters['H'] - (batters['2B'] + batters['3B'] + batters['HR'])
            batters['1B_points'] = batters['1B'] * BATTER_POINTS['1B']
        else:
            batters[f'{k}_points'] = batters[k] * BATTER_POINTS[k]
    return batters


def get_top_13(point_projections, position):
    return point_projections[point_projections['Positions'].str.contains(position)].head(13)


def value_above_replacement(data, position):
    top_player = data[data['Positions'].str.contains(position)]['total_points'].max()
    outside_player = data[data['Positions'].str.contains(position)]['total_points'].min()
    return top_player - outside_player
