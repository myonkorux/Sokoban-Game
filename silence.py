import os, pygame, math, sys
import pygame._view
from pygame.locals import *
from maps import *
from sprites import *

# screen constants
SCREEN_X = 176
SCREEN_Y = 176
TILE_SIZE = 16
LEVEL_COUNTER = 0
# TRANSMAP = [list(i) for i in zip(*MAPLIST[LEVEL_COUNTER])]
BACKGROUND_COLOR = (70, 70, 70)

# map key
BLANK = 0
WALL = 1
BLOCK = 2
CHARACTER = 3
HOLE = 4
SWITCH = 5
SETBLOCK = 6
GOAL = 7

# main game loop - call to restart
def main_loop():
    # initialize pygame and variables
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
    pygame.display.set_caption('Blocks')
    pygame.mouse.set_visible(0)

    # level tracker
    global LEVEL_COUNTER
    TRANSMAP = [list(i) for i in zip(*MAPLIST[LEVEL_COUNTER])]
    
    # end check variables
    switch_check = False
    goal_check = False
    
    # sprite lists
    characters = []
    walls = []
    blocks = []
    holes = []
    setblocks = []
    switches = []
    goals = []

    # read map and populate lists
    for x in range(0, SCREEN_X / TILE_SIZE):
        for y in range(0, SCREEN_Y / TILE_SIZE):
            if TRANSMAP[x][y] == WALL:
                walls.append(WallSprite(screen, x, y))
            elif TRANSMAP[x][y] == BLOCK:
                blocks.append(BlockSprite(screen, x, y))
            elif TRANSMAP[x][y] == CHARACTER:
                characters.append(CharacterSprite(screen, x, y))
                TRANSMAP[x][y] = 0
            elif TRANSMAP[x][y] == HOLE:
                holes.append(HoleSprite(screen, x, y))
            elif TRANSMAP[x][y] == SWITCH:
                switches.append(SwitchSprite(screen, x, y))
            elif TRANSMAP[x][y] == GOAL:
                goals.append(GoalSprite(screen, x, y))

    if len(characters) > 0:
        character = characters[0]
        
    # initialize sprite positions
    for wall in walls:
        wall.update()
    for hole in holes:
        hole.update()
    for switch in switches:
        switch.update()
    for block in blocks:
        block.update()
    for goal in goals:
        goal.update()
    character.update()
    
    while True:
        # initialize default variables
        direction = None
        switch_counter = 0

        # detect key inputs
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    direction = 'up'
                elif event.key == K_DOWN:
                    direction = 'down'
                elif event.key == K_LEFT:
                    direction = 'left'
                elif event.key == K_RIGHT:
                    direction = 'right'
                elif event.key == K_ESCAPE:
                    sys.exit()
                elif event.key == K_r:
                    main_loop()
                elif event.key == K_RETURN:
                    for i in range(len(zip(*TRANSMAP))):
                        print zip(*TRANSMAP)[i]
                elif event.key == K_LSHIFT:
                    for hole in holes:
                        print hole.x, hole.y

        # move character
        if direction == 'up':
            if TRANSMAP[character.x][character.y - 1] != 1 and TRANSMAP[character.x][character.y - 1] != 4:
                character.move_up()
        elif direction == 'down':
            if TRANSMAP[character.x][character.y + 1] != 1 and TRANSMAP[character.x][character.y + 1] != 4:
                character.move_down()
        elif direction == 'left':
            if TRANSMAP[character.x - 1][character.y] != 1 and TRANSMAP[character.x - 1][character.y] != 4:
                character.move_left()
        elif direction == 'right':
            if TRANSMAP[character.x + 1][character.y] != 1 and TRANSMAP[character.x + 1][character.y] != 4:
                character.move_right()
        character.update()

        # move block if character pushes, move character back if block is immovable
        for block in blocks:
            TRANSMAP[block.x][block.y] = 0
            if direction == 'up':
                if pygame.sprite.collide_rect(block, character):
                    if TRANSMAP[block.x][block.y - 1] != 1 and TRANSMAP[block.x][block.y - 1] != 2:
                        block.move_up()
                    else:
                        character.move_down()
            elif direction == 'down':
                if pygame.sprite.collide_rect(block, character):
                    if TRANSMAP[block.x][block.y + 1] != 1 and TRANSMAP[block.x][block.y + 1] != 2:
                        block.move_down()
                    else:
                        character.move_up()
            elif direction == 'left':
                if pygame.sprite.collide_rect(block, character):
                    if TRANSMAP[block.x - 1][block.y] != 1 and TRANSMAP[block.x - 1][block.y] != 2:
                        block.move_left()
                    else:
                        character.move_right()
            elif direction == 'right':
                if pygame.sprite.collide_rect(block, character):
                    if TRANSMAP[block.x + 1][block.y] != 1 and TRANSMAP[block.x + 1][block.y] != 2:
                        block.move_right()
                    else:
                        character.move_left()
            TRANSMAP[block.x][block.y] = 2
        character.update()

        # check block collisions
        for block in blocks:
            for hole in holes:
                if pygame.sprite.collide_rect(block, hole):
                    TRANSMAP[hole.x][hole.y] = SETBLOCK
                    setblocks.append(SetBlockSprite(screen, hole.x, hole.y))
                    blocks.remove(block)
                    holes.remove(hole)
            
        # check switch collisions
        for switch in switches:
            for block in blocks:
                if pygame.sprite.collide_rect(block, switch):
                    switch_counter += 1
            if pygame.sprite.collide_rect(character, switch):
                switch_counter += 1

        # check all switches activated
        if len(switches) > 0 and switch_counter == len(switches):
            switch_check = True

        # check goal reached
        if len(goals) > 0 and pygame.sprite.collide_rect(character, goals[0]):
            goal_check = True

        # check game end
        if switch_check or goal_check:
            LEVEL_COUNTER += 1
            if LEVEL_COUNTER < len(MAPLIST):
                main_loop()
            else:
                sys.exit()

        # update all positions, blit all sprites
        screen.fill(BACKGROUND_COLOR)
        for wall in walls:
            wall.update()
        for hole in holes:
            hole.update()
        for switch in switches:
            switch.update()
        for setblock in setblocks:
            setblock.update()
        for block in blocks:
            block.update()
        for goal in goals:
            goal.update()
        character.update()
        pygame.display.flip()

    pygame.quit()

def main():
    main_loop()

if __name__ == '__main__':
    main()

