import pygame
pygame.mixer.init()

track1 = pygame.mixer.Sound('audio/track1.ogg')
track2 = pygame.mixer.Sound('audio/track2.ogg')
track3 = pygame.mixer.Sound('audio/track3.ogg')
track4 = pygame.mixer.Sound('audio/track4.ogg')
track5 = pygame.mixer.Sound('audio/track5.ogg')
track6 = pygame.mixer.Sound('audio/track6.ogg')
track7 = pygame.mixer.Sound('audio/track7.ogg')
track8 = pygame.mixer.Sound('audio/track8.ogg')

tracks = [track1, track2, track3, track4, track5, track6, track7, track8]

volume = 0.1
noise = 0.3

def play_sound():
	sound = pygame.mixer.Sound('audio/footsteps.wav')
	sound.play()
	sound.fadeout(3000)

def start_music():
	global volume, tracks
	tracks[0].set_volume(volume)
	tracks[0].play(-1)

def play_tracks(trackCount):
	global volume, tracks
	for x in range(1, trackCount + 1):
		tracks[x].set_volume(noise)
		tracks[x].play(-1)

def increase_volume():
	global volume, tracks
	volume += 0.1
	tracks[0].set_volume(volume)

def stop_music():
	global tracks
	tracks[0].fadeout(1000)
	pygame.time.delay(1000)

def cut_tracks():
	global tracks
	for x in range(1, len(tracks) - 1):
		tracks[x].stop()

def pause_track(trackCounter):
	global tracks
	tracks[trackCounter].set_volume(0)

def unpause_tracks():
	global volume, tracks
	for x in range(1, len(tracks)):
		tracks[x].set_volume(noise)
