"""
Explaining of the stats from original report.
"""

stats_values = {
    0: 'time - min',
    1: 'TF',
    2: 'shots - g1',
    3: 'goals - g2',
    4: 'eff. - %',
    5: 'act',
    6: 'points+',
    7: 'points-',
    8: 'SS - p1',
    9: 'S+ - p1',
    10: 'K+ - p1',
    11: 'P+ - p1',
    12: 'N+ - p1',
    13: 'R1 - s1',
    14: 'R2 - s1',
    15: 'R3 - s1',
    16: '7+ - k1',
    17: 'J+ - p1',
    18: 'SS - p2',
    19: 'S- - p2',
    20: 'K- - p2',
    21: 'P- - p2',
    22: 'N- - p2',
    23: 'R1 - s2',
    24: 'R2 - s2',
    25: 'R3 - s2',
    26: '7- - k2',
    27: 'J- - p2',
    28: 'a plus activity',
    29: 'h plus activity - r',
    30: 'o plus activity',
    31: '+ plus activity',
    32: 'r plus activity',
    33: 't plus activity',
    34: 'B plus activity',
    35: 'c minus activity - b1',
    36: 'L minus activity - b1',
    37: '- minus activity - b1',
    38: 'k minus activity - b1',
    39: 'b minus activity - b1',
    40: '= minus activity - b2',
    41: 'I penalty+',
    42: 'II penalty+',
    43: 'III penalty+',
    44: 'mk penalty+',
    45: '1 penalty- - c',
    46: '2 penalty- - c1',
    47: '3 penalty- - c',
    48: 'mk penalty-',
    49: 'shirt number'
}

"""
Calculation logic
Info: '/' is not division - just symbol eg. 10 goals / 12 shoots
Action Number:
ANu = p1 + p2 + s1 + s2 + k1 + k2 + b1 + b2
ANu = 8 + 9 + 10 + 11 + 12 + 17 + 18 + 19 + 20 + 21 + 22 + 27 + 13 + 14 + 15 + 23 + 24 + 25 + 16 + 26 + 35 + 36 + 37 +
    + 38 + 39 + 40
    
Positional Attack:
PAt = p1 + p2 / p1
PAt = 8 + 9 + 10 + 11 + 12 + 17 + 18 + 19 + 20 + 21 + 22 + 27 / 8 + 9 + 10 + 11 + 12 + 17

Fastbreak Attack:
FAt = s1 + s2 / s1
FAt = 13 + 14 + 15 + 23 + 24 + 25 / 13 + 14 + 15

Penalties (shoots):
PSh = k1 + k2 / k1
PSh = 16 + 26 / 16

Errors:
Err = b1 + b2 / b2
Err = 35 + 36 + 37 + 38 + 39 + 40 / 40

Goals:
Go = p1 + s1 + k1
Go = 8 + 9 + 10 + 11 + 12 + 17 + 13 + 14 + 15 + 16

Goalkeepers eff:
Gk = g1 - g2 / k2
Gk = 2 - 3 / 26

Penalties (shoots) created:
PShCr = r
PShCr = 29

Penalties (2 min):
Pen = c1
Pen = 46

% Efficiency in game:
EffTot = Go / ANu
EffTot = 8 + 9 + 10 + 11 + 12 + 17 + 13 + 14 + 15 + 16 / 8 + 9 + 10 + 11 + 12 + 17 + 18 + 19 + 20 + 21 + 22 + 27 +
          + 13 + 14 + 15 + 23 + 24 + 25 + 16 + 26 + 35 + 36 + 37 + 38 + 39 + 40
"""