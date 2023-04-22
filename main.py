import sys
import pygame
from pygame.locals import *
from pynput import keyboard, mouse
import os
import pkg_resources

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.set_num_channels(32)

base_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

sound_effects = {
    keyboard.Key.enter: pygame.mixer.Sound(os.path.join(base_dir, 'sounds', 'ckletter2.wav')),
    keyboard.Key.backspace: pygame.mixer.Sound(os.path.join(base_dir, 'sounds', 'enter.wav')),
    keyboard.Key.space: pygame.mixer.Sound(os.path.join(base_dir, 'sounds', 'ckletter4.wav')),
    keyboard.Key.tab: pygame.mixer.Sound(os.path.join(base_dir, 'sounds', 'lcletter1.wav')),
    'general': pygame.mixer.Sound(os.path.join(base_dir, 'sounds', 'ckletter3.wav')),
    mouse.Button.left: pygame.mixer.Sound(os.path.join(base_dir, 'sounds', 'letter2.wav')),
}

pressed_keys = set()

def play_sound(key_name):
    if key_name in sound_effects:
        sound_effects[key_name].play()

def on_key_press(key):
    if key not in pressed_keys:
        pressed_keys.add(key)
        if key in sound_effects:
            play_sound(key)
        else:
            play_sound('general')

def on_key_release(key):
    if key in pressed_keys:
        pressed_keys.remove(key)

def on_mouse_click(x, y, button, pressed):
    if pressed and button == mouse.Button.left:
        play_sound(button)

def main():
    pygame.display.init()
    screen = pygame.display.set_mode((1, 1), pygame.NOFRAME)
    pygame.display.iconify()

    with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as key_listener, \
            mouse.Listener(on_click=on_mouse_click) as mouse_listener:
        key_listener.join()
        mouse_listener.join()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
