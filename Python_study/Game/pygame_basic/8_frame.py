#pip3 install pygame
from turtle import delay
import pygame

#################################################################
#기본 초기화 (반드시 해야하는 것들)
pygame.init() #초기화

#화면 크기 설름
screen_width = 480 #가로크기
screen_height = 640 #세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption('JW') #게임 이름

#FPS
clock = pygame.time.Clock()

##################################################################
#1. 사용자 게임 초기화 (배경화면, 게임이미지, 좌표, 폰트 등)

#배경이미지 불러오기
background = pygame.image.load('/Users/jw_cha/Code Develop/Python_game/Python_study-game/pygame_basic/background.jpeg')

#캐릭터(스프라이트) 불러오기
character = pygame.image.load('/Users/jw_cha/Code Develop/Python_game/Python_study-game/pygame_basic/character.png')
character_size = character.get_rect().size #이미지 외적하는 사각형 크기
character_width = character_size[0] #가로크기
character_height = character_size[1] #세로크기
character_x_pos = (screen_width / 2) - (character_width / 2) #화면 가로 중간에 해당하는 곳에 위치
character_y_pos = screen_height - character_height #화면 세로의 가장 아래 해당하는 곳에 위치

#이동할 좌표
to_x = 0
to_y = 0

#이동속도
character_speed = 0.6

#적군 캐릭터
enemy = pygame.image.load('/Users/jw_cha/Code Develop/Python_game/Python_study-game/pygame_basic/enemy.png')
enemy_size = enemy.get_rect().size #이미지 외적하는 사각형 크기
enemy_width = enemy_size[0] #가로크기
enemy_height = enemy_size[1] #세로크기
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) #화면 가로 중간에 해당하는 곳에 위치
enemy_y_pos = (screen_height / 2) - (enemy_height / 2) #화면 세로 중간에 해당하는 곳에 위치

#폰트 정의
game_font = pygame.font.Font(None, 40) #폰트객체 생성,(폰트,크기)

#러닝타임
total_time = 10

#시작시간 정보
start_ticks = pygame.time.get_ticks() #시작 tick 을 받아옴


#이벤트 루프
running = True #게임이 진행중인가 판단
while running:
    dt = clock.tick(60) #게임화면 초당 프레임 수 조절
    #print('fps : ' + str(clock.get.fps())) #FPS 출력

    #2. 이벤트 처리 (키보드, 마우스 입력 등)
    for event in pygame.event.get(): #무조건 존재해야 하는 구문. 입력 체킹
        if event.type == pygame.QUIT: #quit이 입력되는 경우. 종료
            running = False

        if event.type == pygame.KEYDOWN: #방향키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= character_speed #pixel 단위
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP: #방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0 #방향키 뗐으므로 변위 초기화
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    #3. 게임 캐릭터 위치 정의
    #FPS에 따라 이동속도가 영향을 받으면 안됨. 보정 필요(*dt)
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    #화면 벗어남 방지
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width: #좌표계산 기준은 항상 왼쪽 위 꼭지점.
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
    
    #4. 충돌처리
    #충돌처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos 
    enemy_rect.top = enemy_y_pos

    #충돌체크
    if character_rect.colliderect(enemy_rect):
        print('충돌발생')
        running = False

    #5. 화면에 그리기
    screen.fill((0, 0, 255)) #RGB값으로 스크린 채우기
    #screen.blit(background, (0, 0)) #맨왼쪽 맨위가 (0,0) background 이미지 로드
    screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    #타이머 넣기
    #경과시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 #ms단위이므로 s로 변환
    #남은시간 계산
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255)) #출력할 글자, true, 글자색상
    screen.blit(timer, (10, 10))

    if total_time - elapsed_time <= 0:
        print('타임아웃')
        running = False


    pygame.display.update() #게임화면 다시그리기, 반드시 지속적으로 호출되어야 함

#종료직전 잠시 대기
pygame.time.delay(2000)

#게임종료 = pygame종료
pygame.quit()