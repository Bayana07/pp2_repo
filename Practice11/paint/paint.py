import pygame
import math

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))

colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)
colorUI_BG = (50, 50, 50)
colorHIGHLIGHT = (255, 255, 0)

base_layer.fill(colorBLACK)

current_color = colorRED
current_tool = 'rect'

clock = pygame.time.Clock()

LMBpressed = False
THICKNESS = 5

currX = 0
currY = 0
prevX = 0
prevY = 0

UI_HEIGHT = 50

palette = [
    (pygame.Rect(10, 10, 30, 30), colorRED),
    (pygame.Rect(50, 10, 30, 30), colorGREEN),
    (pygame.Rect(90, 10, 30, 30), colorBLUE),
    (pygame.Rect(130, 10, 30, 30), colorWHITE)
]

font = pygame.font.SysFont(None, 24)

ui_text = font.render(
    "1-Rect 2-Circle 3-Eraser 4-Square 5-RTriangle 6-ETriangle 7-Rhombus | +/- thickness",
    True, colorWHITE
)

def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2),
                       abs(x1 - x2), abs(y1 - y2))


def draw_square(surface, color, x1, y1, x2, y2, thickness):
    size = min(abs(x2 - x1), abs(y2 - y1))
    rect = pygame.Rect(x1, y1, size, size)
    pygame.draw.rect(surface, color, rect, thickness)

# 🔺 ПРЯМОУГОЛЬНЫЙ ТРЕУГОЛЬНИК
def draw_right_triangle(surface, color, x1, y1, x2, y2, thickness):
    points = [(x1, y1), (x1, y2), (x2, y2)]
    pygame.draw.polygon(surface, color, points, thickness)


def draw_equilateral_triangle(surface, color, x1, y1, x2, y2, thickness):
    base = x2 - x1
    height = int(abs(base) * math.sqrt(3) / 2)

    points = [
        (x1, y2),
        (x2, y2),
        ((x1 + x2) // 2, y2 - height)
    ]
    pygame.draw.polygon(surface, color, points, thickness)


def draw_rhombus(surface, color, x1, y1, x2, y2, thickness):
    mx = (x1 + x2) // 2
    my = (y1 + y2) // 2

    points = [
        (mx, y1),
        (x2, my),
        (mx, y2),
        (x1, my)
    ]
    pygame.draw.polygon(surface, color, points, thickness)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_EQUALS:
                THICKNESS += 1
            if event.key == pygame.K_MINUS:
                THICKNESS = max(1, THICKNESS - 1)

            if event.key == pygame.K_1:
                current_tool = 'rect'
            if event.key == pygame.K_2:
                current_tool = 'circle'
            if event.key == pygame.K_3:
                current_tool = 'eraser'
            if event.key == pygame.K_4:
                current_tool = 'square'
            if event.key == pygame.K_5:
                current_tool = 'right_triangle'
            if event.key == pygame.K_6:
                current_tool = 'equilateral_triangle'
            if event.key == pygame.K_7:
                current_tool = 'rhombus'

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            clicked_palette = False

            for rect, color in palette:
                if rect.collidepoint(event.pos):
                    current_color = color
                    clicked_palette = True
                    break

            if not clicked_palette and event.pos[1] > UI_HEIGHT:
                LMBpressed = True
                prevX, prevY = event.pos
                currX, currY = event.pos

        if event.type == pygame.MOUSEMOTION:
            if LMBpressed:
                currX, currY = event.pos

                # ластик
                if current_tool == 'eraser':
                    pygame.draw.circle(base_layer, colorBLACK,
                                       (currX, currY), THICKNESS * 2)

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:

            if LMBpressed:
                LMBpressed = False
                currX, currY = event.pos

                if current_tool == 'rect':
                    pygame.draw.rect(base_layer, current_color,
                                     calculate_rect(prevX, prevY, currX, currY),
                                     THICKNESS)

                elif current_tool == 'circle':
                    rect = calculate_rect(prevX, prevY, currX, currY)
                    pygame.draw.ellipse(base_layer, current_color, rect, THICKNESS)

                elif current_tool == 'square':
                    draw_square(base_layer, current_color,
                                prevX, prevY, currX, currY, THICKNESS)

                elif current_tool == 'right_triangle':
                    draw_right_triangle(base_layer, current_color,
                                        prevX, prevY, currX, currY, THICKNESS)

                elif current_tool == 'equilateral_triangle':
                    draw_equilateral_triangle(base_layer, current_color,
                                              prevX, prevY, currX, currY, THICKNESS)

                elif current_tool == 'rhombus':
                    draw_rhombus(base_layer, current_color,
                                 prevX, prevY, currX, currY, THICKNESS)

    screen.blit(base_layer, (0, 0))

    if LMBpressed:
        if current_tool == 'rect':
            pygame.draw.rect(screen, current_color,
                             calculate_rect(prevX, prevY, currX, currY), THICKNESS)

        elif current_tool == 'circle':
            rect = calculate_rect(prevX, prevY, currX, currY)
            pygame.draw.ellipse(screen, current_color, rect, THICKNESS)

    pygame.draw.rect(screen, colorUI_BG, (0, 0, WIDTH, UI_HEIGHT))

    for rect, color in palette:
        pygame.draw.rect(screen, color, rect)

        if color == current_color:
            pygame.draw.rect(screen, colorHIGHLIGHT, rect, 3)
        else:
            pygame.draw.rect(screen, colorBLACK, rect, 1)

    screen.blit(ui_text, (180, 16))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()