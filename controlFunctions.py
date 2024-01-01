import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Global variables for volume and AI level
background_music_volume = 20
game_sound_volume = 30
bot1_level = "Medium"
bot2_level = "Medium"

# Load click sound
click_sound = pygame.mixer.Sound("click_sound.mp3")  # Replace with your sound file

# Function to update background music volume
def update_music_volume(value=None):
    global background_music_volume
    if value is not None:
        background_music_volume = int(value)
        pygame.mixer.music.set_volume(background_music_volume / 100)
    return background_music_volume

# Function to update game sound volume
def update_game_sound_volume(value=None):
    global game_sound_volume
    if value is not None:
        game_sound_volume = int(value)
        click_sound.set_volume(game_sound_volume / 100)
    return game_sound_volume

# Function to update AI level
def update_bot1_level(value=None):
    global bot1_level
    if value is not None:
        bot1_level = value
    return bot1_level

def update_bot2_level(value=None):
    global bot2_level
    if value is not None:
        bot2_level = value
    return bot2_level

# Function to play background music
def play_background_music():
    pygame.mixer.music.load("background_music.mp3")  # Replace with your background music file
    pygame.mixer.music.set_volume(background_music_volume / 100)
    pygame.mixer.music.play(-1)  # -1 means loop indefinitely

# Function to play click sound
def play_click_sound():
    click_sound.play()


# Start playing background music when the app starts
play_background_music()
