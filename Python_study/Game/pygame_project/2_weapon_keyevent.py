#pip3 install pygame
from re import S
from turtle import delay
import pygame
import os

#################################################################
#기본 초기화 (반드시 해야하는 것들)
pygame.init() #초기화

#화면 크기 설름
screen_width = 640 #가로크기
screen_height = 480 #세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption('Pang!~') #게임 이름

#FPS
clock = pygame.time.Clock()

#################################################################도
#1. 사용자 게임 초기화 (배경화면, 게임이미지, 좌표, 폰트 등)
current_path = os.path.dirname(__file__) #현재파일의 위치 반환
image_path = os.path.join(current_path, 'images') #image 폴더위치 반환

#배경만들기
background = pygame.image.load(os.path.join(image_path, 'background.png'))
#stage 만들기
stage = pygame.image.load(os.path.join(image_path, 'stage.png'))
stage_size = stage.get_rect().size
stage_height = stage_size[1] #스테이지 위에 캐릭터를 두기 위해 선언
#캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, 'character.png'))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height
#캐릭터 이동방향
character_to_x = 0
#캐릭터 이동속도
character_speed = 5

#무기만들기
weapon = pygame.image.load(os.path.join(image_path, 'weapon.png'))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
#무기는 중복발사 가능
weapons = []
#무기 이동속도
weapon_speed = 10








#이벤트 루프
running = True #게임이 진행중인가 판단
while running:
    dt = clock.tick(60) #게임화면 초당 프레임 수 조절
    #print('fps : ' + str(clock.get.fps())) #FPS 출력

    #2. 이벤트 처리 (키보드, 마우스 입력 등)
    for event in pygame.event.get(): #무조건 존재해야 하는 구문. 입력 체킹
        if event.type == pygame.QUIT: #quit이 입력되는 경우. 종료
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    #3. 게임 캐릭터 위치 정의
    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    #무기위치 조정
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons] #무기위치를 위로 올림
    #천장에 닿은무기 제거
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]
   
    #4. 충돌처리
    #충돌처리

    #충돌체크

    #5. 화면에 그리기, 순서대로 표기되서 제일 위가 제일 뒤.
    screen.blit(background, (0, 0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() #게임화면 다시그리기, 반드시 지속적으로 호출되어야 함

#게임종료 = pygame종료
pygame.quit()