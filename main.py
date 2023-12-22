import pygame
import button
import os

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Python Game")

background_img = pygame.image.load('parallax-forest-preview.png')
bg = pygame.transform.scale(background_img, (800, 600))

# standing image
stationary = pygame.image.load(os.path.join("images/Hero", "standing.png"))

#Hero
left = [None] * 10
for picIndex in range(1, 10):
    left[picIndex - 1] = pygame.image.load(os.path.join("images/Hero", "L" + str(picIndex) + ".png"))
    picIndex += 1

right = [None] * 10
for picIndex in range(1, 10):
    right[picIndex - 1] = pygame.image.load(os.path.join("images/Hero", "R" + str(picIndex) + ".png"))
    picIndex += 1

#enemy


#bullet
bullet_img = pygame.transform.scale(pygame.image.load(os.path.join("images", "light_bullet.png")), (10, 10))

class Hero:
    def __init__(self, x, y):
        #walk
        self.x = x
        self.y = y
        self.vel_x = 10
        self.face_right = True
        self.face_left = False
        self.stepIndex = 0
        #bullet
        self.bullets = []
        self.cool_down_count = 0

    def move_hero(self, userInput):
        if userInput(pygame.K_RIGHT):
            self.x += self.vel_x
            self.face_right = True
            self.face_left = False
        elif userInput(pygame.K_RIGHT):
            self.x -= self.vel_x
            self.face_right = False
            self.face_left = True
        else:
            self.stepIndex = 0

    def draw(self, screen):
        if self.stepIndex >= 9:
            self.stepIndex = 0
        if self.face_left:
            screen.blit(left[self.stepIndex], (self.x, self.y))
            self.stepIndex += 1
        if self.face_right:
            screen.blit(right[self.stepIndex], (self.x, self.y))
            self.stepIndex += 1

    def direction(self):
        if self.face_right:
            return 1
        if self.face_left:
            return -1

    def shoot(self):
        self.cooldown()
        if (userInput[pygame.K_f] and self.cool_down_count == 0):
            bullet = Bullet(x, y, self.direction())
            self.bullets.append(bullet)
            self.cool_down_count = 1
        for bullet in self.bullets:
            bullet.move()
            if bullet.off_screen():
                self.bullets.remove(bullet)

    def cooldown(self):
        if self.cool_down_count >= 10:
            self.cool_down_count = 0
        elif self.cool_down_count > 0:
            self.cool_down_count += 1



class Bullet:
    def __init__(self, x, y, direction):
        self.x = x + 15
        self.y = y + 25
        self.direction = direction

    def draw_bullet(self):
        screen.blit(bullet_img, (self.x, self.y))

    def move(self):
        if self.direction == 1:
            self.x += 15
        if self.direction == -1:
            self.x -= 15

    def off_screen(self):
        return not(self.x >= 0 and self.x <= SCREEN_WIDTH)


class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        screen.blit(enemy_left[0])
        #vid 6:29


# load button images
start_img = pygame.image.load('images/start_btn.png').convert_alpha()
exit_img = pygame.image.load('images/exit_btn.png').convert_alpha()

game_start = False
menu_state = "main"
# create button instances
start_button = button.Button(100, 200, start_img, 0.8)
exit_button = button.Button(450, 200, exit_img, 0.8)

# game variables

game_paused = False

# define font
font = pygame.font.SysFont("arialblack", 30)

# define text color
TEXT_COL = (255, 255, 255)

# load button images
resume_img = pygame.image.load("images/button_resume.png").convert_alpha()
options_img = pygame.image.load("images/button_options.png").convert_alpha()
quit_img = pygame.image.load("images/button_quit.png").convert_alpha()
video_img = pygame.image.load("images/button_video.png").convert_alpha()
audio_img = pygame.image.load("images/button_audio.png").convert_alpha()
keys_img = pygame.image.load("images/button_keys.png").convert_alpha()
back_img = pygame.image.load("images/button_back.png").convert_alpha()

# create button instances
resume_button = button.Button(304, 125, resume_img, 1)
options_button = button.Button(297, 250, options_img, 1)
quit_button = button.Button(336, 375, quit_img, 1)
video_button = button.Button(226, 75, video_img, 1)
audio_button = button.Button(225, 200, audio_img, 1)
keys_button = button.Button(246, 325, keys_img, 1)
back_button = button.Button(332, 450, back_img, 1)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


x = 400
y = 450
vel_x = 5
vel_y = 20
Jump = False
i = 0
width = 800
move_left = False
move_right = False
stepIndex = 0


def draw_game():
    global stepIndex
    for bullet in player.bullets:
        bullet.draw_bullet()
    if stepIndex >= 9:
        stepIndex = 0
    if move_left:
        screen.blit(left[stepIndex], (x, y))
        stepIndex += 1
    elif move_right:
        screen.blit(right[stepIndex], (x, y))
        stepIndex += 1
    else:
        screen.blit(stationary, (x, y))
    # screen.fill((0, 0, 0))
    # screen.blit(background_img, (0, 0))
    pygame.display.update()

player = Hero(400, 525)




# game loop
run = True
while run:

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
        if event.type == pygame.QUIT:
            run = False

    # input
    userInput = pygame.key.get_pressed()
    #player.move_hero(userInput)

    #shoot
    player.shoot()


    screen.fill((52, 78, 91))

    if start_button.draw(screen):
        run = True
        game_start = True

    if exit_button.draw(screen):
        run = False

        # check if game is paused
    if game_paused == True:
        screen.fill((0, 0, 0))

        if menu_state == "main":
            # draw pause screen buttons
            if resume_button.draw(screen):
                game_paused = False
            if options_button.draw(screen):
                menu_state = "options"
            if quit_button.draw(screen):
                run = False
        if menu_state == "options":
            '''draw the different options buttons'''
            if video_button.draw(screen):
                print("Video settings")
            if audio_button.draw(screen):
                print("Audio settings")
            if keys_button.draw(screen):
                print("change key bindings")
            if back_button.draw(screen):
                menu_state = "main"


    elif game_start == True and game_paused == False:
        screen.fill((0, 0, 0))
        screen.blit(bg, (i, 0))
        screen.blit(bg, (width + i, 0))

        if i == -width:
            screen.blit(bg, (width + i, 0))
            i = 0

        i -= 1

        draw_game()

        # Movement
        #print("game started and not pause")

        if userInput[pygame.K_LEFT] and x > 0:
            x -= vel_x
            move_left = True
            move_right = False
        elif userInput[pygame.K_RIGHT] and x < 800 -62:
            x += vel_x
            move_left = False
            move_right = True
        else:
            move_left = False
            move_right = False
            screen.blit(stationary, (x, y))
            #print(stepIndex)

        if Jump is False and userInput[pygame.K_UP]:
            Jump = True
        if Jump is True:

            y -= vel_y
            vel_y -= 1
            if vel_y < -20:
                Jump = False
                vel_y = 20
        print(f"x: {x}, y: {y}, vel_y: {vel_y}")



    else:
        draw_text("Press SPACE to pause", font, TEXT_COL, 1, 1)

    pygame.time.delay(40)
    pygame.display.update()

pygame.quit()
