import pygame
import csv
import random
import time

filename = 'dictionary.csv'
dictionary = []

with open(filename) as f:
    file = csv.reader(f)
    header = next(file)
    for row in file:
        dictionary.append(row[0])

for c in range(10):
    words = [dictionary[random.randint(0, len(dictionary)-1)].lower() for x in range(40)]
    txt = []

    length = 0
    j = 0
    for i in range(0, 40, 10):
        txt.append(' '.join(words[i:i+10]))
        length += len(txt[j])
        j += 1
    print(length)
    
    if length + 3 < 340:
        break
length += 3
    
pygame.init()

window = pygame.display.set_mode((575, 500))

color = (255, 255, 255)
window.fill(color)
pygame.display.flip()

font = pygame.font.Font("freesansbold.ttf", 11)
big_font = pygame.font.Font('freesansbold.ttf', 24)
text_line1 = font.render(txt[0], True, (0, 0, 0))
text_line2 = font.render(txt[1], True, (0,0,0))
text_line3 = font.render(txt[2], True, (0, 0, 0))
text_line4 = font.render(txt[3], True, (0, 0, 0))
window.blit(text_line1, (25,15))  
window.blit(text_line2, (25,30))
window.blit(text_line3, (25,45))
window.blit(text_line4, (25,60))

user_text = ''
input_rect = pygame.Rect(25, 150, 525, 250)
active = False
first_key_press = False

start = 0
end = 0
times = []



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(times)
            pygame.quit()
            quit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
        
        if event.type == pygame.KEYDOWN:
            if first_key_press == False:
                start = time.time()
                first_key_press = True
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += event.unicode
                if event.key == pygame.K_SPACE:
                    end = time.time()
                    times.append(end - start)
                    start = time.time()
 
    pygame.draw.rect(window, (100,100,100), input_rect)
    if len(user_text) <= 85:
        text_surface_line1 = font.render(user_text[0:84], True, (255,255,255))
        window.blit(text_surface_line1, (input_rect.x+5, input_rect.y+5))
    if 86 <= len(user_text) <= 170:
        text_surface_line2 = font.render(user_text[85:169], True, (255,255,255))
        window.blit(text_surface_line1, (input_rect.x+5, input_rect.y+5))
        window.blit(text_surface_line2, (input_rect.x+5, input_rect.y+20))
    if 171 <= len(user_text) <= 255:
        text_surface_line3 = font.render(user_text[170:254], True, (255,255,255))
        window.blit(text_surface_line1, (input_rect.x+5, input_rect.y+5))
        window.blit(text_surface_line2, (input_rect.x+5, input_rect.y+20))
        window.blit(text_surface_line3, (input_rect.x+5, input_rect.y+35))
    if 256 <= len(user_text) <= 340:
        text_surface_line4 = font.render(user_text[255:340], True, (255,255,255))
        window.blit(text_surface_line1, (input_rect.x+5, input_rect.y+5))
        window.blit(text_surface_line2, (input_rect.x+5, input_rect.y+20))
        window.blit(text_surface_line3, (input_rect.x+5, input_rect.y+35))
        window.blit(text_surface_line4, (input_rect.x+5, input_rect.y+50))

    
    if len(user_text) == length:
        wpm = 0
        for k in range(len(times)):
            wpm += (60/times[k])
        wpm_avg = wpm / len(times)
        str_wpm_avg = 'WPM:' + ' ' + str(round(wpm_avg))
        display_wpm = big_font.render((str_wpm_avg), True, (0,0,0))
        window.blit(display_wpm, (input_rect.x+200, input_rect.y-30))
    pygame.display.update()