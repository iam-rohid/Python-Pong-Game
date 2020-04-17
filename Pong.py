import pygame
import sys
import random

objColor = (240, 240, 240)
bgColor = (20, 20, 20)
ballColor = (200, 200, 20)
playerSpeed = 0
ballSpeedX = 7 * random.choice((1, -1))
ballSpeedY = 7 * random.choice((1, -1))
AiSpeed = 8

playerScore = 0
aiScore = 0


def ballMovement():
    global ballSpeedX, ballSpeedY
    ball.x += ballSpeedX
    ball.y += ballSpeedY

    if ball.top <= 0 or ball.bottom >= winHeight:
        ballSpeedY *= -1

    if ball.left <= 0:
        restart("human")
    if ball.right >= winWidth:
        restart('ai')
    if ball.colliderect(human) or ball.colliderect(ai):
        ballSpeedX *= -1


def playerMovement():
    human.y += playerSpeed

    if human.top <= 0:
        human.top = 0
    if human.bottom >= winHeight:
        human.bottom = winHeight


def AiMovement():
    if ai.top < ball.y:
        ai.top += AiSpeed
    if ai.bottom > ball.y:
        ai.bottom -= AiSpeed

    if ai.top <= 0:
        ai.top = 0
    if ai.bottom >= winHeight:
        ai.bottom = winHeight


def restart(player):
    global playerScore, aiScore
    if player == "human":
        playerScore += 1
    if player == "ai":
        aiScore += 1
    global ballSpeedX, ballSpeedY
    ball.center = (winWidth/2, winHeight/2)
    ballSpeedX *= random.choice((1, -1))
    ballSpeedY *= random.choice((1, -1))


# general setup
pygame.init()
clock = pygame.time.Clock()

# Window Setup
winWidth = 980
winHeight = 720
screen = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("Pong")

ballSize = 20
playerHeight = 120

ball = pygame.Rect(winWidth / 2 - ballSize / 2, winHeight /
                   2 - ballSize/2, ballSize, ballSize)
human = pygame.Rect(winWidth-10, winHeight/2 -
                    playerHeight/2, 10, playerHeight)
ai = pygame.Rect(0, winHeight/2 - playerHeight/2, 10, playerHeight)


def showScore():
    font = pygame.font.SysFont('sans-serif', 40)
    playerScoreText = font.render(f"{playerScore}", True, (200, 200, 200))
    screen.blit(playerScoreText, ((winWidth/2) + 20,
                                  ((winHeight/2) - int(playerScoreText.get_height()/2))))
    aiScoreText = font.render(f"{aiScore}", True, (200, 200, 200))
    screen.blit(aiScoreText, ((winWidth/2) - int(aiScoreText.get_width() + 20),
                              ((winHeight/2) - int(aiScoreText.get_height()/2))))


# Loop
while True:
    # Handling Inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                playerSpeed += 7
            if event.key == pygame.K_UP:
                playerSpeed -= 7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                playerSpeed -= 7
            if event.key == pygame.K_UP:
                playerSpeed += 7

    ballMovement()
    playerMovement()
    AiMovement()
    # Visuals
    screen.fill(bgColor)
    pygame.draw.ellipse(screen, ballColor, ball)
    pygame.draw.rect(screen, objColor, human)
    pygame.draw.rect(screen, objColor, ai)
    pygame.draw.aaline(screen, objColor, (winWidth/2, 0),
                       (winWidth/2, winHeight))
    showScore()
    # Updating the window
    pygame.display.flip()
    clock.tick(60)
