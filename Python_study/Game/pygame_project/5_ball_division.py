#pip3 install pygame
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

#공만들기 (4개 크기에 대해 따로처리)
ball_images = [
    pygame.image.load(os.path.join(image_path, 'balloon1.png')), 
    pygame.image.load(os.path.join(image_path, 'balloon2.png')),
    pygame.image.load(os.path.join(image_path, 'balloon3.png')),
    pygame.image.load(os.path.join(image_path, 'balloon4.png'))]

#공 크기에 따른 최초 스피드
ball_speed_y = [-18, -15, -12, -9] #큰공 -> 작은공 순
#공들
balls = []
#최초 발생하는 공 추가
balls.append({
    'pos_x' : 50, #공의 x좌표
    'pos_y' : 50, #공의 y좌표
    'img_idx' : 0, #공의 이미지 인덱스
    'to_x' : 3, #공의 x축 속도 -면 왼쪽 
    'to_y' : -6, #공의 y축 속도
    'init_speed_y' : ball_speed_y[0]}) #y 최초속도

#사라질 무기와 공 정보 변수
weapon_to_remove = -1
ball_to_remove = -1

#Font 정의
game_font = pygame.font.Font(None, 40)
total_time = 100
start_ticks = pygame.time.get_ticks() #시작시간

#게임종료 메시지
game_result = 'Game Over'


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

    #공 위치 정의
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val['pos_x']
        ball_pos_y = ball_val['pos_y']
        ball_img_idx = ball_val['img_idx']

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        #양쪽 벽에 닿았을 때 튕겨나오기
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_val['to_x'] = ball_val['to_x'] * -1

        #바닥에 닿았을 떄 튕겨나오기
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val['to_y'] = ball_val['init_speed_y']
        else:
            ball_val['to_y'] += 0.5

        ball_val['pos_x'] += ball_val['to_x']
        ball_val['pos_y'] += ball_val['to_y']

    #4. 충돌처리
    #캐릭터/공 충돌
    character_rec = character.get_rect()
    character_rec.left = character_x_pos
    character_rec.top = character_y_pos

    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val['pos_x']
        ball_pos_y = ball_val['pos_y']
        ball_img_idx = ball_val['img_idx']

        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y

        if character_rec.colliderect(ball_rect):
            running = False
            break

        #공/무기 충돌
        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]

            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y

            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx #해당무기 삭제 설정
                ball_to_remove = ball_idx #해당 공 삭제 설정

                if ball_img_idx < 3: #가장 작은공이 아니면 쪼개지기
                    #현재 공 위치
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]

                    #나눠진 공 정보
                    small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                    small_ball_width = small_ball_rect.size[0]
                    small_ball_height = small_ball_rect.size[1]

                    #왼쪽으로 쪼개지는 공
                    balls.append ({
                        'pos_x' : ball_pos_x + (ball_width / 2) - (small_ball_width / 2), #공의 x좌표
                        'pos_y' : ball_pos_y + (ball_height / 2) - (small_ball_height / 2), #공의 y좌표
                        'img_idx' : ball_img_idx + 1, #공의 이미지 인덱스
                        'to_x' : -3, #공의 x축 속도 -면 왼쪽 
                        'to_y' : -6, #공의 y축 속도
                        'init_speed_y' : ball_speed_y[ball_img_idx + 1]}) #y 최초속도
                    #오른쪽으로 쪼개지는 공
                    balls.append ({
                        'pos_x' : ball_pos_x + (ball_width / 2) - (small_ball_width / 2), #공의 x좌표
                        'pos_y' : ball_pos_y + (ball_height / 2) - (small_ball_height / 2), #공의 y좌표
                        'img_idx' : ball_img_idx + 1, #공의 이미지 인덱스
                        'to_x' : 3, #공의 x축 속도 -면 왼쪽 
                        'to_y' : -6, #공의 y축 속도
                        'init_speed_y' : ball_speed_y[ball_img_idx + 1]}) #y 최초속도
                break
        else : 
            continue
        break

    #충돌된 공/ 무기 없애기
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1

    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1

    #모든공 없앤경우 게임종료
    if len(balls) == 0:
        game_result = 'Mission Complete'
        running = False


    #5. 화면에 그리기, 순서대로 표기되서 제일 위가 제일 뒤.
    screen.blit(background, (0, 0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    for idx, val in enumerate(balls):
        ball_pos_x = val['pos_x']
        ball_pos_y = val['pos_y']
        ball_img_idx = val['img_idx']
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    #경과시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render('Time : {}'.format(int(total_time - elapsed_time)), True, (255, 255, 255))
    screen.blit(timer, (10, 10))

    if total_time - elapsed_time <= 0:
        game_result = 'Time Over'
        running = False

    pygame.display.update() #게임화면 다시그리기, 반드시 지속적으로 호출되어야 함

msg = game_font.render(game_result, True, (255, 255, 0))
msg_rect = msg.get_rect(center =(int(screen_width/2), int(screen_height/2)))
screen.blit(msg, msg_rect)
pygame.display.update()

pygame.time.delay(2000)

#게임종료 = pygame종료
pygame.quit()