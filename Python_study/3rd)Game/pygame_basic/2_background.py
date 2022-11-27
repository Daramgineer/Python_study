#pip3 install pygame
import pygame
pygame.init() #초기화

#화면 크기 설름
screen_width = 480 #가로크기
screen_height = 640 #세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption('JW') #게임 이름

#배경이미지 불러오기
background = pygame.image.load('/Users/jw_cha/Code Develop/Python_game/Python_study-game/pygame_basic/background.jpeg')

#이벤트 루프
running = True #게임이 진행중인가 판단
while running:
    for event in pygame.event.get(): #무조건 존재해야 하는 구문. 입력 체킹
        if event.type == pygame.QUIT: #quit이 입력되는 경우. 종료
            running = False

    screen.fill((0, 0, 255)) #RGB값으로 스크린 채우기
    #screen.blit(background, (0, 0)) #맨왼쪽 맨위가 (0,0) background 이미지 로드
    pygame.display.update() #게임화면 다시그리기, 반드시 지속적으로 호출되어야 함

#게임종료 = pygame종료
pygame.quit()