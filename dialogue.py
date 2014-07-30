import os, pygame

# directory variables
main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, 'dialogues')

# image constants
TEXT_1_1 = 'text_1_1.gif'
TEXT_1_2 = 'text_1_2.gif'
TEXT_2_1 = 'text_2_1.gif'
TEXT_2_2 = 'text_2_2.gif'
TEXT_3_1 = 'text_3_1.gif'
TEXT_3_2 = 'text_3_2.gif'
TEXT_5_1 = 'text_5_1.gif'
TEXT_5_2 = 'text_5_2.gif'

dialogue_dict = {1: [TEXT_1_1, TEXT_1_2], \
				 2: [TEXT_2_1, TEXT_2_2], \
				 3: [TEXT_3_1, TEXT_3_2], \
                 5: [TEXT_5_1, TEXT_5_2]}

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

def select_dialogues(screen, character, TILE_SIZE, LEVEL_COUNTER):
	dialogues = []
	if LEVEL_COUNTER in dialogue_dict:
		for text in dialogue_dict[LEVEL_COUNTER]:
			dialogues.append(SpeechSprite(screen, character.x * TILE_SIZE, character.y * TILE_SIZE, text))
	return dialogues

# base class for speech bubble
class SpeechSprite(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.screen = screen
        self.image, self.rect = load_image(image)

    def update(self):
        self.rect.bottomleft = (self.x, self.y)
        self.screen.blit(self.image, self.rect)