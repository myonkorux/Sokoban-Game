import os, pygame
from silence import TILE_SIZE

# directory variables
main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, 'sprites')

# image constants
WALL_IMG = 'wall.gif'
CHARACTER_IMG = 'character.gif'
BLOCK_IMG = 'block_2.gif'
HOLE_IMG = 'hole.gif'
SET_BLOCK_IMG = 'block_3.gif'
SWITCH_IMG = 'switch.gif'
GOAL_IMG = 'cake.gif'
INSTRUCTION_IMG = 'instructions.gif'
TITLE_IMG = 'title.gif'
END_IMG = 'end.gif'

# function to load image
def load_image(name, colorkey=None):
    fullname = os.path.join(data_dir, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print ('Cannot load image:', fullname)
        raise SystemExit(str(geterror()))
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

# base class for tiles
class TileSprite(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.screen = screen
        self.image, self.rect = load_image(image)

    def update(self):
        self.rect.topleft = (self.x * TILE_SIZE, self.y * TILE_SIZE)
        self.screen.blit(self.image, self.rect)

# base class for moveable sprites
class MoveSprite(pygame.sprite.Sprite):
    # def __init__(self, x, y, image):
    #     pygame.sprite.Sprite.__init__(self)
    #     self.image, self.rect = load_image(image)
    #     self.x = x
    #     self.y = y

    # def update(self):
    #     self.rect.topleft = (self.x * TILE_SIZE, self.y * TILE_SIZE)

    def move_up(self):
        self.y -= 1

    def move_down(self):
        self.y += 1

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

class TitleScreen(TileSprite):
    def __init__(self, screen, x, y):
        TileSprite.__init__(self, screen, x, y, TITLE_IMG)

class EndScreen(TileSprite):
    def __init__(self, screen, x, y):
        TileSprite.__init__(self, screen, x, y, END_IMG)

class InstructionScreen(TileSprite):
    def __init__(self, screen, x, y):
        TileSprite.__init__(self, screen, x, y, INSTRUCTION_IMG)

class CharacterSprite(TileSprite, MoveSprite):
    def __init__(self, screen, x, y):
        TileSprite.__init__(self, screen, x, y, CHARACTER_IMG)

class BlockSprite(TileSprite, MoveSprite):
    def __init__(self, screen, x, y):
        TileSprite.__init__(self, screen, x, y, BLOCK_IMG)

class WallSprite(TileSprite):
    def __init__(self, screen, x, y):
        TileSprite.__init__(self, screen, x, y, WALL_IMG)

class HoleSprite(TileSprite):
    def __init__(self, screen, x, y):
        TileSprite.__init__(self, screen, x, y, HOLE_IMG)

class SwitchSprite(TileSprite):
    def __init__(self, screen, x, y):
        TileSprite.__init__(self, screen, x, y, SWITCH_IMG)

class SetBlockSprite(TileSprite):
    def __init__(self, screen, x, y):
        TileSprite.__init__(self, screen, x, y, SET_BLOCK_IMG)  

class GoalSprite(TileSprite):
    def __init__(self, screen, x, y):
        TileSprite.__init__(self, screen, x, y, GOAL_IMG)



