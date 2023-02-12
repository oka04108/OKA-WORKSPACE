import pygame,random

#초기화 
pygame.init()

score = 0

#FPS
clock = pygame.time.Clock()

#화면 설정
screen_width = 400
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 제목 설정
pygame.display.set_caption("Avoid Meteor!")

#폰트 설정
gamefont = pygame.font.Font(None,40)

#배경 이미지 설정
#배경 이미지 불러와야 합니다.
background = pygame.image.load("...\\background.png")

to_x = 0
to_y = 0

#우주선 캐릭터 이미지 설정
#우주선 이미지 불러와야 합니다. 
spaceship = pygame.image.load("...\\spaceship.png")
spaceship_size = spaceship.get_rect().size
spaceship_width = spaceship_size[0]
spaceship_height = spaceship_size[1]
spaceship_x_pos = screen_width/2 - spaceship_width/2
spaceship_y_pos = screen_height - spaceship_height

#운석 생성
randomNumber = 30
MeteorSpeed = 15

#운석 캐릭터 이미지 설정
#운석 이미지 불러와야합니다.
meteor = pygame.image.load("...\\meteor.png")
meteor_size = meteor.get_rect().size
meteor_width = meteor_size[0]
meteor_height = meteor_size[1]
meteor_x_pos = 500
meteor_y_pos = 0

#우주선 속도
spacehsip_speed = 0.6

#FPS
clock = pygame.time.Clock()


running = True
while running:
    dt = clock.tick(20) #초당 프레임 수 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= spacehsip_speed
            elif event.key == pygame.K_RIGHT:
                to_x += spacehsip_speed
            elif event.key == pygame.K_UP:
                to_y -= spacehsip_speed
            elif event.key == pygame.K_DOWN:
                to_y += spacehsip_speed
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    # 우주선 이동 & 프레임 맞추기
    spaceship_x_pos += to_x * dt
    spaceship_y_pos += to_y * dt

    #창 경계 설정
    if spaceship_x_pos < 0:
        spaceship_x_pos = 0
    elif spaceship_x_pos > screen_width - spaceship_width:
        spaceship_x_pos = screen_width - spaceship_width

    if spaceship_y_pos < 0:
        spaceship_y_pos = 0
    elif spaceship_y_pos > screen_height - spaceship_height:
        spaceship_y_pos = screen_height - spaceship_height

    if meteor_y_pos > screen_height:
        meteor_y_pos = 0
        meteor_x_pos = random.randrange(1,400)
        score += 1

    if score>0:
        if score % 10 == 0:
            MeteorSpeed += 0.5
    
    #운석 떨어지는 속도 
    meteor_y_pos += MeteorSpeed
    
    #충돌 설정
    spaceship_rect = spaceship.get_rect()
    spaceship_rect.left = spaceship_x_pos
    spaceship_rect.top = spaceship_y_pos

    meteor_rect = meteor.get_rect()
    meteor_rect.left = meteor_x_pos
    meteor_rect.top = meteor_y_pos
    

    totalscore = gamefont.render(str(score),True,(200,200,200))

    if spaceship_rect.colliderect(meteor_rect):
        running = False

    screen.blit(background,(0, 0)) #배경 그리기
    screen.blit(spaceship,(spaceship_x_pos,spaceship_y_pos)) #캐릭터 그리기
    screen.blit(meteor, (meteor_x_pos,meteor_y_pos))
    screen.blit(totalscore, (10,20))    

    pygame.display.update() #게임 화면 다시 그리기

pygame.time.delay(2000)
#pygame 종료 
pygame.quit()
