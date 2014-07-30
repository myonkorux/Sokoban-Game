import os, pygame, math, sys
import pygame._view
from pygame.locals import *
from maps import *
from sprites import *
from dialogue import *
from audio import *

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
SCENE = 9

# setup game
def setup():
    # initialize pygame and variables
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
    pygame.display.set_caption('Silence')
    pygame.mouse.set_visible(0)
    return screen

# update and draw sprites
def update_all(walls, holes, switches, blocks, goals, setblocks, character, dialogues):
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
    if len(dialogues) > 0:
        dialogues[0].update()

# manage scene events
def run_scene(scene):
    global LEVEL_COUNTER
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()
            elif event.key == K_r:
                main_loop()
            elif event.key == K_RETURN:
                LEVEL_COUNTER += 1
                increase_volume()
                if LEVEL_COUNTER < len(MAPLIST):
                    main_loop()
                else:
                    sys.exit()
    scene.update()
    pygame.display.flip()

# manage game events
def run_game(dialogues):
    global LEVEL_COUNTER
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                if len(dialogues) == 0:
                    return 'up'
                else:
                    return 'next'
            elif event.key == K_DOWN:
                if len(dialogues) == 0:
                    return 'down'
                else:
                    return 'next'
            elif event.key == K_LEFT:
                if len(dialogues) == 0:
                    return 'left'
                else:
                    return 'next'
            elif event.key == K_RIGHT:
                if len(dialogues) == 0:
                    return 'right'
                else:
                    return 'next'
            elif event.key == K_ESCAPE:
                sys.exit()
            elif event.key == K_r:
                main_loop()
            elif event.key == K_RETURN:
                if len(dialogues) > 0:
                    return 'next'
            elif event.key == K_LSHIFT:
                LEVEL_COUNTER += 1
                increase_volume()
                cut_tracks()
                if LEVEL_COUNTER < len(MAPLIST):
                    main_loop()
                else:
                    sys.exit()
    return None

# move character
def move_character(TRANSMAP, character, direction):
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

# move block
def move_block(TRANSMAP, character, direction, blocks):
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

# check game end
def check_win(switches, switch_counter, goals, character):
    # check all switches activated
    if len(switches) > 0 and switch_counter == len(switches):
        switch_check = True
    elif len(switches) == 0:
        switch_check = True
    else:
        switch_check = False

    # check goal reached
    if len(goals) > 0 and pygame.sprite.collide_rect(character, goals[0]):
        goal_check = True
    elif len(goals) == 0:
        goal_check = True
    else:
        goal_check = False

    # check level end
    global LEVEL_COUNTER
    if switch_check and goal_check:
        play_sound()
        LEVEL_COUNTER += 1
        increase_volume()
        cut_tracks()
        if LEVEL_COUNTER < len(MAPLIST):
            main_loop()
        else:
            sys.exit()

# main game loop - call to restart
def main_loop():
    # setup game and set screen
    screen = setup()

    # level tracker
    global LEVEL_COUNTER
    TRANSMAP = [list(i) for i in zip(*MAPLIST[LEVEL_COUNTER])]
    
    # sprite lists
    characters = []
    walls = []
    blocks = []
    holes = []
    setblocks = []
    switches = []
    goals = []

    # check if level is a scene
    if TRANSMAP[0][0] == SCENE:
        if TRANSMAP[1][0] == 2:
            scene = TitleScreen(screen, 0, 0)
        elif TRANSMAP[1][0] == 3:
            stop_music()
            scene = EndScreen(screen, 0, 0)
        while True:
            run_scene(scene)
    else:
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

        # populate list of dialogue bubbles
        dialogues = select_dialogues(screen, character, TILE_SIZE, LEVEL_COUNTER)

        # play music
        play_tracks(len(switches))

        # initialize sprite positions
        update_all(walls, holes, switches, blocks, goals, setblocks, character, dialogues)
        
        while True:
            # initialize default variables
            switch_counter = 0
            unpause_tracks()

            # detect key inputs
            direction = run_game(dialogues)

            # move to next dialogue on enter
            if direction == 'next':
                dialogues.remove(dialogues[0])

            # move character
            move_character(TRANSMAP, character, direction)

            # move block if character pushes, move character back if block is immovable
            move_block(TRANSMAP, character, direction, blocks)

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
                        pause_track(switch_counter)
                if pygame.sprite.collide_rect(character, switch):
                    switch_counter += 1
                    pause_track(switch_counter)

            # check game end
            check_win(switches, switch_counter, goals, character)

            # update all positions, blit all sprites
            screen.fill(BACKGROUND_COLOR)
            update_all(walls, holes, switches, blocks, goals, setblocks, character, dialogues)
            pygame.display.flip()

def main():
    start_music()
    main_loop()

if __name__ == '__main__':
    main()

