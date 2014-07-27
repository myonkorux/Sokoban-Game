# BLANK = 0
# WALL = 1
# BLOCK = 2
# CHARACTER = 3
# HOLE = 4
# SWITCH = 5
# SETBLOCK = 6
# GOAL = 7

MAPLIST = []

DEFMAP = [[1,1,1,1,1,1,1,1,1,1,1], \
          [1,0,0,0,0,0,0,0,0,0,1], \
          [1,0,0,0,0,0,0,0,0,0,1], \
          [1,0,0,0,0,0,0,0,0,0,1], \
          [1,0,0,0,0,0,0,0,0,0,1], \
          [1,0,0,0,0,0,0,0,0,0,1], \
          [1,0,0,0,0,0,0,0,0,0,1], \
          [1,0,0,0,0,0,0,0,0,0,1], \
          [1,0,0,0,0,0,0,0,0,0,1], \
          [1,0,0,0,0,0,0,0,0,0,1], \
          [1,1,1,1,1,1,1,1,1,1,1]]

LEVELT = [[1,1,1,1,1,1,1,1,1,1,1], \
          [1,0,0,0,0,0,1,0,0,0,1], \
          [1,0,0,0,0,0,1,0,0,0,1], \
          [1,0,0,4,0,0,1,5,0,0,1], \
          [1,0,0,0,0,0,1,0,0,0,1], \
          [1,0,0,1,2,3,1,0,0,0,1], \
          [1,0,0,2,0,0,4,0,0,0,1], \
          [1,0,0,0,0,0,1,0,0,0,1], \
          [1,0,0,0,0,0,1,0,0,5,1], \
          [1,0,0,0,0,0,1,0,0,0,1], \
          [1,1,1,1,1,1,1,1,1,1,1]]

LEVEL1 = [[1,1,1,1,1,1,1,1,1,1,1], \
          [1,0,0,0,0,1,0,0,0,0,1], \
          [1,0,0,0,0,1,0,0,7,0,1], \
          [1,0,0,0,0,1,0,0,0,0,1], \
          [1,0,0,0,0,1,0,0,0,0,1], \
          [1,0,0,0,0,2,0,0,0,0,1], \
          [1,0,0,0,0,1,0,0,0,0,1], \
          [1,0,0,0,0,1,0,0,0,0,1], \
          [1,0,3,0,0,1,0,0,0,0,1], \
          [1,0,0,0,0,1,0,0,0,0,1], \
          [1,1,1,1,1,1,1,1,1,1,1]]
MAPLIST.append(LEVEL1)

LEVEL2 = [[1,1,1,1,1,1,1,1,1,1,1], \
          [1,0,0,0,0,1,0,0,0,0,1], \
          [1,0,2,0,0,1,0,0,7,0,1], \
          [1,0,0,0,0,1,0,0,0,0,1], \
          [1,0,0,0,0,1,0,0,0,0,1], \
          [1,0,0,0,0,4,0,0,0,0,1], \
          [1,0,0,0,0,1,0,0,0,0,1], \
          [1,0,0,0,0,1,0,0,0,0,1], \
          [1,0,3,0,0,1,0,0,0,0,1], \
          [1,0,0,0,0,1,0,0,0,0,1], \
          [1,1,1,1,1,1,1,1,1,1,1]]
MAPLIST.append(LEVEL2)

LEVEL3 = [[1,1,1,1,1,1,1,1,1,1,1], \
          [1,0,0,0,0,1,0,0,0,0,1], \
          [1,0,0,0,0,1,0,0,7,0,1], \
          [1,0,0,0,0,1,0,0,0,0,1], \
          [1,0,0,0,0,4,4,0,0,0,1], \
          [1,0,2,0,0,1,0,0,0,0,1], \
          [1,0,0,2,0,1,0,0,0,0,1], \
          [1,0,0,0,0,4,4,4,0,0,1], \
          [1,0,3,0,0,1,0,0,0,0,1], \
          [1,0,0,0,0,1,0,0,0,0,1], \
          [1,1,1,1,1,1,1,1,1,1,1]]
MAPLIST.append(LEVEL3)

LEVEL4 = [[1,1,1,1,1,1,1,1,1,1,1], \
          [1,0,0,0,0,0,0,0,0,0,1], \
          [1,0,2,2,0,0,0,0,2,0,1], \
          [1,0,0,5,0,1,0,5,0,0,1], \
          [1,0,0,0,1,1,1,0,0,0,1], \
          [1,0,0,1,1,1,1,1,1,0,1], \
          [1,0,0,0,1,1,1,0,0,0,1], \
          [1,0,0,5,0,1,0,5,0,0,1], \
          [1,0,3,0,0,1,0,0,0,0,1], \
          [1,0,0,0,0,0,0,0,0,0,1], \
          [1,1,1,1,1,1,1,1,1,1,1]]
MAPLIST.append(LEVEL4)

MAPLIST.append(LEVELT)

