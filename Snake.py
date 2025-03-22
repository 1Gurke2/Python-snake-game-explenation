import pygame
import random

# Pygame initialisieren
pygame.init()

# Fenstergröße und Farben definieren
width, height = 600, 400 # Setzt die Größe der Variablen für die Map fest
screen = pygame.display.set_mode((width, height)) # Setzt die Größe für die Map fest mit den Variablen
clock = pygame.time.Clock() 

snake_block = 10 # Variable setzt Größe eines Schlangen Segments fest
snake_speed = 15 # Variable setzt Ticks für später fest

# Farben werden deffiniert
black = (0, 0, 0)
green = (0, 255, 0)
red = (213, 50, 80)

# Snake position und Bewegung
x = width // 2 # setzt die Variable x fest als die hälfte der width (width = 600, 600 : 2 = 60)
y = height // 2 # setzt die Variable y fest als die hälfte der height (so ist x und y genau in der mitte)
x_change = 0 # x_change ist auf 0 so schlange bewegt sich nicht auf der x Achse 
y_change = 0 # y_change ist auf 0 so schlange bewegt sich nicht auf der y Achse 

# Snake Körper
snake_body = [(x, y)] # setzt die Schlange auf die zuvor gesetzten Variablen x und y also 60 und 40

# Zufällige Position für das Futter
food_x = random.randrange(0, width, snake_block) # setzt einen random x wert für das essen welcher zwischen 0 und der width 600 liegt
food_y = random.randrange(0, height, snake_block) # setzt einen random y wert für das essen welcher zwischen 0 und der height 400 liegt

# Spiel Schleife
running = True # setzt running auf True
while running: # Solange das Spiel läuft wird alles in der Schleife wiederholt
    for event in pygame.event.get(): # wenn irgendwas passiert wirde alles in der for Schleife gecheckt
        if event.type == pygame.QUIT: # fals das event quit ist ist (schließen des Fensters)
            running = False # setzt variable Running auf False
        if event.type == pygame.KEYDOWN: # fals das event das drücken einer Taste ist ist
            if event.key == pygame.K_LEFT and x_change == 0: # fals die Taste Linkerpfeil ist und x_change 0 ist also die schlange sich nicht auf der x Achse bewegt
                x_change = -snake_block # x_change wird auf -snake_block(10) gesetzt (-10 = Links 10 = rechts)
                y_change = 0 # y_change wird auf 0 gesetzt 
            elif event.key == pygame.K_RIGHT and x_change == 0:
                x_change = snake_block
                y_change = 0
            elif event.key == pygame.K_UP and y_change == 0: # fals die Taste Pfeil nach oben ist und y_change 0 ist also die schlange sich nicht auf der y Achse bewegt
                y_change = -snake_block # y_change wird auf -snake_block(10) gesetzt (-10 = oben 10 = unten)
                x_change = 0 # x_change wird auf 0 gesetzt 
            elif event.key == pygame.K_DOWN and y_change == 0:
                y_change = snake_block
                x_change = 0

    x += x_change # Die x Variable wird um x_change erhöt/veringert was durch Pfeiltaste Rechts/Links geändert werden kann
    y += y_change # Die y Variable wird um y_change erhöt/veringert was durch Pfeiltaste Oben/Unten geändert werden kann

    # Spiel beenden, wenn Snake die Wand berührt
    if x >= width or x < 0 or y >= height or y < 0: # Checkt ob die Schlange (Kopf) den Rand des Bildschirms berührt  
        running = False # setzt variable Running auf False

    # Snake wächst, wenn sie das Futter isst
    snake_body.append((x, y)) # setzt neues Schlangen segment auf die neue x und y possition (geändert durch x_change und y_change)
    if (x, y) == (food_x, food_y): # checkt ob die Kordinaten des Schlangenkopfs und die des essens gleich sind
        food_x = random.randrange(0, width, snake_block) # setzt einen random x wert für das essen welcher zwischen 0 und der width 600 liegt
        food_y = random.randrange(0, height, snake_block) # setzt einen random y wert für das essen welcher zwischen 0 und der height 400 liegt
    else:
        snake_body.pop(0) # Entfernt das erste Segment der Snake, wenn es das Futter nicht isst

    # Snake Körper zeichnen
    screen.fill(black) # macht den Bildschirm Schwarz farbe wurde oben definiert 
    for segment in snake_body: # für jedes segment wird etwas in der Schlange geändert (beispiel 3 segmente: snake_body = [(100, 100), (110, 100), (120, 100)])
        pygame.draw.rect(screen, green, (segment[0], segment[1], snake_block, snake_block)) # bildschirm wird grün gefärbt wo segment position 1(0) und segment position 2(1) ist breite höhe deffiniert durch snake_block(10) 

    # Futter zeichnen
    pygame.draw.rect(screen, red, (food_x, food_y, snake_block, snake_block)) # das essen wird rot und auf die kordinaten food_x/y gesetzt breite und höhe deffiniert durch snake_block(10)

    pygame.display.update() # der bildschirm wird aktualisiert  
    clock.tick(snake_speed) # game update speed

# Pygame beenden
pygame.quit() # bildschirm wird geschlossen game wird beendet