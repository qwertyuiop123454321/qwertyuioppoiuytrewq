import pygame
import math
import random
import sys
import time
import os


pygame.init()


# -------------------------
# FULLSCREEN MODE
# -------------------------
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()
clock = pygame.time.Clock()


# Wheel settings (recalculate for fullscreen)
center = (WIDTH // 2, HEIGHT // 2)
radius = min(WIDTH, HEIGHT) // 2 - 50
colors = ["red", "blue", "green", "yellow"]
num_segments = len(colors)


# Spin variables
angle = 0
spin_speed = 0
deceleration = 0.05
spinning = False




# -------------------------
# Timed popup alert function
# -------------------------
def timed_alert(message, duration=5):
    font = pygame.font.SysFont(None, 40)
    start_time = time.time()


    while time.time() - start_time < duration:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Wheel window closed — running action now")
                timed_alert("You closed the wheel window!", 2)
                pygame.quit()
                sys.exit()


        screen.fill((255, 200, 200))
        text = font.render(message, True, (0, 0, 0))
        rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, rect)


        pygame.display.flip()
        clock.tick(60)


    return True




# -------------------------
# Drawing functions
# -------------------------
def draw_wheel():
    segment_angle = 360 / num_segments
    start_angle = angle


    for i, color in enumerate(colors):
        pygame.draw.arc(
            screen,
            pygame.Color(color),
            (center[0] - radius, center[1] - radius, radius * 2, radius * 2),
            math.radians(start_angle),
            math.radians(start_angle + segment_angle),
            radius
        )
        start_angle += segment_angle




# -------------------------
# FIXED POINTER (back on wheel)
# -------------------------
def draw_pointer():
    # Position pointer at right edge of wheel
    point_x = center[0] + radius + 10
    point_y = center[1]


    triangle = [
        (point_x, point_y - 20),
        (point_x, point_y + 20),
        (point_x - 40, point_y)
    ]


    pygame.draw.polygon(screen, (0, 0, 0), triangle)




def get_landed_color():
    segment_angle = 360 / num_segments
    normalized_angle = (-angle) % 360
    index = int(normalized_angle // segment_angle)
    return colors[index]




# -------------------------
# Main loop
# -------------------------
running = True


while running:
    for event in pygame.event.get():


        # Quit button
        if event.type == pygame.QUIT:
            print("Wheel window closed — running action now")
            timed_alert("Wrong Choice", 2)
            timed_alert("Computer Shutdown Imminent In: 3", 1)
            timed_alert("Computer Shutdown Imminent In: 2", 1)
            timed_alert("Computer Shutdown Imminent In: 1", 1)
            os.system("shutdown /s /t 0")
            pygame.quit()
            sys.exit()


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                timed_alert("Wrong Choice", 2)
                timed_alert("Computer Shutdown Imminent In: 3", 1)
                timed_alert("Computer Shutdown Imminent In: 2", 1)
                timed_alert("Computer Shutdown Imminent In: 1", 1)
                os.system("shutdown /s /t 0")
                pygame.quit()
                sys.exit()


            if event.key == pygame.K_F11:
                timed_alert("Wrong Choice", 2)
                timed_alert("Computer Shutdown Imminent In: 3", 1)
                timed_alert("Computer Shutdown Imminent In: 2", 1)
                timed_alert("Computer Shutdown Imminent In: 1", 1)
                os.system("shutdown /s /t 0")
                pygame.quit()
                sys.exit()


    # Click to spin
    if event.type == pygame.MOUSEBUTTONDOWN and not spinning:
        mx, my = event.pos
        dist = math.hypot(mx - center[0], my - center[1])


        if dist <= radius:
            spin_speed = random.uniform(20, 30)
            spinning = True


    screen.fill("white")


    if spinning:
        angle += spin_speed
        spin_speed = max(0, spin_speed - deceleration)


        if spin_speed == 0:
            spinning = False
            landed = get_landed_color()
            print("Wheel landed on:", landed)


            if landed == "red":
                timed_alert("Computer Shutdown Imminent In: 3", 1)
                timed_alert("Computer Shutdown Imminent In: 2", 1)
                timed_alert("Computer Shutdown Imminent In: 1", 1)
                os.system("shutdown /s /t 0")
            else:
                timed_alert("You live for today...", 3)
                sys.exit()


    draw_wheel()
    draw_pointer()
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
sys.exit()



