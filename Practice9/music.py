import pygame
import sys
import os

pygame.init()
pygame.mixer.init(frequency=44100)

WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player FIXED")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 100, 220)
GREEN = (50, 180, 90)
RED = (220, 60, 60)

font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()

BASE_DIR = os.path.dirname(__file__)
MUSIC_FOLDER = os.path.join(BASE_DIR, "music")

supported_extensions = (".mp3", ".wav", ".ogg")


def load_playlist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

    files = [
        os.path.join(folder, f)
        for f in os.listdir(folder)
        if f.lower().endswith(supported_extensions)
    ]
    files.sort()
    return files


playlist = load_playlist(MUSIC_FOLDER)
current_index = 0
is_playing = False


def play(index):
    global is_playing
    if not playlist:
        return

    pygame.mixer.music.load(playlist[index])
    pygame.mixer.music.play()
    is_playing = True


def stop():
    global is_playing
    pygame.mixer.music.stop()
    is_playing = False


def next_track():
    global current_index
    if not playlist:
        return
    current_index = (current_index + 1) % len(playlist)
    play(current_index)


def prev_track():
    global current_index
    if not playlist:
        return
    current_index = (current_index - 1) % len(playlist)
    play(current_index)


def draw(text, y, color=BLACK):
    img = font.render(text, True, color)
    screen.blit(img, (20, y))


def main():
    global is_playing

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    play(current_index)

                elif event.key == pygame.K_s:
                    stop()

                elif event.key == pygame.K_n:
                    next_track()

                elif event.key == pygame.K_b:
                    prev_track()

        if playlist and is_playing and not pygame.mixer.music.get_busy():
            next_track()

        screen.fill(WHITE)

        draw("Music Player FIXED", 20, BLUE)
        draw("P=Play  S=Stop  N=Next  B=Back", 70)

        if not playlist:
            draw("Нет музыки в папке /music", 150, RED)
        else:
            track = os.path.basename(playlist[current_index])
            draw(f"Track: {track}", 150)

            status = "Playing" if is_playing else "Stopped"
            draw(f"Status: {status}", 200, GREEN if is_playing else RED)

        pygame.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    main()