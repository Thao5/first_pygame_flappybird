import pygame
pygame.init()
pygame.display.set_caption('game')
game_font=pygame.font.Font('04B_19.TTF',40)


p = 0.2
bird_y = 0
high_score = 0


score=0
def score_view():
    score_font=game_font.render(f'Score: {int(score)}',True, (255,255,255))
    high_score_font = game_font.render(f'High score: {int(high_score)}',True, (255,255,255))
    high_score_rect = high_score_font.get_rect(center=(200, 50))
    score_rect=score_font.get_rect(center=(200,100))
    screen.blit(high_score_font,high_score_rect)
    screen.blit(score_font,score_rect)


def check_vc():
    if bird_rect.bottom >= 668 or bird_rect.top <= -75:
        return False
    else:
         return True


bg = pygame.image.load(r'FileGame\assets\background-night.png')
bg = pygame.transform.scale2x(bg)
floor = pygame.image.load(r'FileGame\assets\floor.png')
floor=pygame.transform.scale2x(floor)
bird = pygame.image.load(r'FileGame\assets\yellowbird-midflap.png')
bird = pygame.transform.scale2x(bird)
bird_rect = bird.get_rect(center=(100,368))
icon = pygame.image.load(r'FileGame\assets\yellowbird-midflap.png')
pygame.display.set_icon(icon)
screen=pygame.display.set_mode((432,768))
screen_start=pygame.image.load(r'FileGame\assets\message.png')
screen_start=pygame.transform.scale2x(screen_start)
screen_start_rect=screen_start.get_rect(center=(216,384))
run_mode=True
game_mode=True
floor_x = 0
while run_mode:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run_mode=False
            game_mode = False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE and game_mode:
                bird_y-=10
            if event.key==pygame.K_SPACE and game_mode==False:
                game_mode=True
                bird_y =0
                bird_rect.center=(100,368)
                score = 0
    screen.blit(bg,(0,0))
    screen.blit(floor, (floor_x, 600))
    screen.blit(floor, (floor_x+432,600))
    floor_x -= 1
    if (floor_x == -432): floor_x = 0
    score_view()
    if game_mode:
        screen.blit(bird, bird_rect)
        bird_y += p
        bird_rect.centery += bird_y
        score += 0.01
        game_mode = check_vc()
    else:
        if score > high_score: high_score = score
        screen.blit(screen_start,screen_start_rect)
    pygame.display.update()