import pygame
import random

# init
pygame.init()
pygame.mixer.init()

lose_sound = pygame.mixer.Sound("lose.mp3")
lose_sound.set_volume(0.5)

# Variable running game
#isRun = True

# membuat display surface object
#window_lebar = 600
#window_panjang = 400
#window = pygame.display.set_mode((window_lebar, window_panjang))

# ukuran layar
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Run From Snake!")

# warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# object game

# object size
object_size = 15

# object speed
object_speed = 15

# size
size = 20

# ukuran
panjang = 20
lebar = 20

# kecepatan gerak player
speed = 5

# fungsi untuk menampilkan object
def draw_object(object_x, object_y):
    pygame.draw.rect(screen, RED, [object_x, object_y, object_size, object_size])

# fungsi untuk menampilkan pesan di screen
def message(msg, color):
    font_style = pygame.font.SysFont(None, 30)
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width/6, screen_height/3])

# fungsi untuk memutar terus game nya jika tidak kena object
def game_loop():
    game_over = False
    game_close = False

    # posisi awal karakter player
    player_x = screen_width / 2
    player_y = screen_height / 2

    # posisi awal object
    object_x = random.randrange(0, screen_width - object_size)
    object_y = random.randrange(0, screen_height - object_size)

    # arah gerakan object
    object_x_change = object_speed
    object_y_change = object_speed

    clock = pygame.time.Clock()

    score = 0
    start_time = pygame.time.get_ticks()

    while not game_over:
        while game_close == True:
            screen.fill(BLACK)
            message("You Lost! Press C-Play Again or Q-Quit", RED) 
            lose_sound.play()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over == False
                        game_close == True
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and player_x > 0:
                    player_x -= size
                elif event.key == pygame.K_RIGHT and player_x < screen_width - lebar:
                    player_x += size

                elif event.key == pygame.K_UP and player_y > 0:
                    player_y -= size
                elif event.key == pygame.K_DOWN and player_y < screen_height - panjang:
                    player_y += size

        # batasan object agar tetap di dalam screen
        if object_x >= screen_width - object_size or object_x < 0:
            object_x_change = -object_x_change
        if object_y >= screen_height - object_size or object_y < 0:
            object_y_change = -object_y_change

        # update posisi object
        object_x += object_x_change
        object_y += object_y_change

        elapsed_time = pygame.time.get_ticks() - start_time
        if elapsed_time > 1000:
            score += 1
            start_time = pygame.time.get_ticks()

        screen.fill(BLACK)

        # gambar object
        draw_object(object_x, object_y)

        # gambar player
        pygame.draw.rect(screen, GREEN, [player_x, player_y, size, size])

        message("Score : " + str(score), WHITE) # menampilkan sudah berapa score per detik

        pygame.display.update()

        # deteksi ketika bertabrakan
        if (abs(player_x - object_x) < object_size and
            abs(player_y - object_y) < object_size):
            game_close = True
        
        clock.tick(30)
    pygame.quit()
    quit()

game_loop()
#while isRun:
    # delay ketika memencet keyboard press or arrow
#    pygame.time.delay(10)

    # user input, database input
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            isRun = False

    # ambil semua keyboard press
#    keys = pygame.key.get_pressed()

    # ambil ke kiri
#    if keys[pygame.K_LEFT] and x > 0:
#        x -= speed

#    if keys[pygame.K_RIGHT] and x < window_lebar - lebar:
#        x += speed

#    if keys[pygame.K_DOWN] and y < window_panjang - panjang:
#        y += speed

#    if keys[pygame.K_UP] and y > 0:
#        y -= speed

    # update asset
#    window.fill((255,255,255))
#    pygame.draw.rect(window, (255,120,0), (x,y,lebar,panjang))
    # render ke display
#    pygame.display.update()

#pygame.quit()