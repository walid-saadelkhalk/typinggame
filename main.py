import pygame
import sys
import imageio
from PIL import Image
import numpy as np
import random

pygame.init()
pygame.mixer.init()

# création de la fenêtre
width, height = 709, 401
fenetre = pygame.display.set_mode((width, height))
window_title = pygame.display.set_caption("Typing Game")

# image
image_path = "images/background_menu.png"
background_image = pygame.image.load(image_path)

# Gif fond
gif_path = "images/background_jeu.gif"
background_gif = imageio.mimread(gif_path)
# Conversion des images du GIF
frames = [pygame.image.fromstring(Image.fromarray(img).convert("RGBA").tobytes(), Image.fromarray(img).size, "RGBA") for img in background_gif]


# Animation loop
current_frame = 0
clock = pygame.time.Clock()

# titre menu
titre_font = pygame.font.Font("font/njnaruto.ttf", 70)
titre_jeu = titre_font.render("TYPING KONOHA", True, (216, 62, 17))

# bouton
bouton_font = pygame.font.Font("font/njnaruto.ttf", 30)
bouton_jouer = bouton_font.render("JOUER", True, (216, 62, 17))
bouton_quitter = bouton_font.render("QUITTER", True, (216, 62, 17))

#musique
pygame.mixer.music.load("music/sign.mp3")
pygame.mixer.music.play(2)




text = None
chosen_word = None
pressed_word = None
screen = None


X_naruto = 1515
X_naruto_esquive = 315
X_naruto_clone = 1415
Y_naruto = 275
X_sasuke = 105
Y_sasuke = 275
X_shuriken = 125
Y_shuriken = 260
X_permutation_1 = 1315
X_permutation_2 = 1415
X_naruto_blesse = 1515

shurikens = []



def jeu():
    global screen, text, chosen_word, pressed_word, speed, point, word_Y, X_shuriken, Y_shuriken, shurikens, X_naruto_esquive, X_naruto_clone, X_naruto
    global X_permutation_1, X_permutation_2, X_naruto_blesse
    # création de la fenêtre du jeu
    screen = pygame.display.set_mode((width, height))
    window_title = pygame.display.set_caption("Typing Game")

    # Titre du menu
    police = pygame.font.Font("font/PressStart2P-Regular.ttf", 30)
    titre_jeu = police.render("Tapez:", True, (216, 62, 17))

    # score
    point_titre = police.render("Score:", True, (216, 62, 17))


    #image personnages
    chemin_image_naruto = "images/naruto_mudra.png"
    naruto = pygame.image.load(chemin_image_naruto)

    chemin_image_sasuke = "images/sasuke.png"
    sasuke = pygame.image.load(chemin_image_sasuke)

    chemin_image_naruto_esquive = "images/naruto_esquive.png"
    naruto_esquive = pygame.image.load(chemin_image_naruto_esquive)

    chemin_image_naruto_clone = "images/naruto_clone.png"
    naruto_clone = pygame.image.load(chemin_image_naruto_clone)

    chemin_image_naruto_blesse = "images/naruto_blesse2.png"
    naruto_blesse = pygame.image.load(chemin_image_naruto_blesse)

    chemin_naruto_permutation = "images/bois1.png"
    naruto_permutation = pygame.image.load(chemin_naruto_permutation)

    chemin_naruto_permutation2 = "images/bois2.png"
    naruto_permutation2 = pygame.image.load(chemin_naruto_permutation2)

    chemin_image_naruto_blesse = "images/naruto_blesse2.png"
    naruto_blesse = pygame.image.load(chemin_image_naruto_blesse)


    #image attaque
    chemin_image_shuriken_s1 = "images/s1.png"
    shuriken_s1 = pygame.image.load(chemin_image_shuriken_s1)
    chemin_image_shuriken_s2 = "images/s2.png"
    shuriken_s2 = pygame.image.load(chemin_image_shuriken_s2)



    X = 600
    Y = 400
    point = 0
    speed = 0.03
    shuriken_state = 1

    # gestion des mots
    def nouveau_mot():
        global chosen_word, pressed_word, text, pointCaption, speed, point, word_Y, shurikens
        word_Y = 50
        speed += 0.3
        pressed_word = ""
        lines = open("mots.txt").read().splitlines()
        chosen_word = random.choice(lines)
        text = police.render(chosen_word, True, (216, 62, 17))
        shurikens.append([X_shuriken, Y_shuriken])
    nouveau_mot()




    # Boucle d'animation
    global current_frame

    while True:
        word_Y += speed
        X_shuriken += speed   # ajustez le coefficient pour la vitesse du shuriken

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                pressed_word += pygame.key.name(event.key)
                if chosen_word.startswith(pressed_word):
                    if chosen_word == pressed_word:
                        point += len(chosen_word)
                        nouveau_mot()
                        X_shuriken = 125
                        shuriken_state = 1
                else:
                    pressed_word = ""

        # Déplacement du personnage
        if X_shuriken >= X_naruto_esquive - 15:
            X_naruto_esquive = 1000
            X_naruto_clone = 415
            X_permutation_1 = 310
            point = point - 10

        
        if X_shuriken >= X_naruto_clone - 20:
            X_naruto_clone = 1000
            X_naruto = 515
            X_permutation_2 = 390
            point = point - 15
        
        if X_shuriken >= 473:
            X_naruto = 1000
            X_naruto_blesse = 510




        if word_Y < Y:
            # Afficher l'écran de jeu lorsque le mot est encore dans la zone visible
            screen.blit(frames[current_frame], (0, 0))
            screen.blit(titre_jeu, (20, 10))
            screen.blit(point_titre, (500, 10))

            pointCaption = police.render(str(point), True, (216, 62, 17))
            screen.blit(pointCaption, (500, 50))
            screen.blit(text, (20, word_Y))
            screen.blit(naruto, (X_naruto, Y_naruto))
            screen.blit(naruto_esquive, (X_naruto_esquive, Y_naruto - 10))
            screen.blit(naruto_clone, (X_naruto_clone, Y_naruto))
            screen.blit(sasuke, (X_sasuke, Y_sasuke))
            screen.blit(naruto_permutation, (X_permutation_1, Y_naruto + 25))
            screen.blit(naruto_permutation2, (X_permutation_2, Y_naruto + 25))
            screen.blit(naruto_blesse, (X_naruto_blesse, Y_naruto))

            # Alterner entre les images s1 et s2 du shuriken
            if shuriken_state == 1:
                screen.blit(shuriken_s1, (X_shuriken, Y_shuriken))
                shuriken_state = 2
            else:
                screen.blit(shuriken_s2, (X_shuriken, Y_shuriken))
                shuriken_state = 1
        else:
            font = pygame.font.Font("font/njnaruto.ttf", 40)
            text_fin = font.render("ESPACE POUR REJOUER", True, (216, 62, 17))
            screen.blit(text_fin, (140, 120))
            pygame.display.flip()

            event = pygame.event.wait()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                X_shuriken = 125
                X_naruto_esquive = 315
                X_naruto_clone = 1415
                X_naruto = 1515
                X_permutation_1 = 1315
                X_permutation_2 = 1415
                X_naruto_blesse = 1515
                shuriken_state = 1
                return fenetre.blit(background_image, (0, 0))

        pygame.display.flip()

        current_frame = (current_frame + 1) % len(frames)
        clock.tick(10)




# Boucle principale
running = False
while True:
    running = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # bouton jouer
            if width // 2 - bouton_jouer.get_width() // 2 <= event.pos[0] <= width // 2 + bouton_jouer.get_width() // 2 and \
               255 <= event.pos[1] <= 255 + bouton_jouer.get_height():
                jeu()
                running = False

            # bouton quitter
            elif width // 2 - bouton_quitter.get_width() // 2 <= event.pos[0] <= width // 2 + bouton_quitter.get_width() // 2 and \
                 300 <= event.pos[1] <= 300 + bouton_quitter.get_height():
                pygame.quit()
                sys.exit()

    # Afficher l'image
    fenetre.blit(background_image, (0, 0))
    fenetre.blit(titre_jeu, (width // 2 - titre_jeu.get_width() // 2, 30))
    fenetre.blit(bouton_jouer, (width // 2 - bouton_jouer.get_width() // 2, 250))
    fenetre.blit(bouton_quitter, (width // 2 - bouton_quitter.get_width() // 2, 300))
    

    pygame.display.flip()
