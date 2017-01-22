import pygame, sys
from pygame.locals import *

# Number of frames per second
# Change this value to speed up or slow down your game
FPS = 400

#Global Variables to be used through our program

WINDOWWIDTH = 600
WINDOWHEIGHT = 400
LINETHICKNESS = 10
PADDLESIZE = 50
PADDLEOFFSET = 20

EPSILON = 2

# Set up the colours
BLACK     = (0  ,0  ,0  )
WHITE     = (255,255,255)



#Draws the arena the game will be played in. 
def drawArena():
    DISPLAYSURF.fill((0,0,0))
    #Draw outline of arena
    pygame.draw.rect(DISPLAYSURF, WHITE, ((0,0),(WINDOWWIDTH,WINDOWHEIGHT)), LINETHICKNESS*2)
    #Draw centre line
    pygame.draw.line(DISPLAYSURF, WHITE, ((WINDOWWIDTH/2),0),((WINDOWWIDTH/2),WINDOWHEIGHT), (LINETHICKNESS/4))


#Draws the paddle
def drawPaddle(paddle):
    #Stops paddle moving too low
    if paddle.bottom > WINDOWHEIGHT - LINETHICKNESS:
        paddle.bottom = WINDOWHEIGHT - LINETHICKNESS
    #Stops paddle moving too high
    elif paddle.top < LINETHICKNESS:
        paddle.top = LINETHICKNESS
    #Draws paddle
    pygame.draw.rect(DISPLAYSURF, WHITE, paddle)


#draws the ball
def drawBall(ball):
    pygame.draw.rect(DISPLAYSURF, WHITE, ball)

#moves the ball returns new position
def moveBall(ball, ballDirX, ballDirY):
    ball.x += ballDirX *2
    ball.y += ballDirY *2
    return ball 

#Checks for a collision with a wall, and 'bounces' ball off it.
#Returns new direction
def checkEdgeCollision(ball, ballDirX, ballDirY):
    if ball.top <= (LINETHICKNESS+EPSILON/2) or ball.bottom >= (WINDOWHEIGHT - LINETHICKNESS-EPSILON/2):
        #print("top is"+str(ball.top)+" bottom is "+str(ball.bottom))
        ballDirY = ballDirY * -1
    if ball.left <= (LINETHICKNESS+EPSILON/2) or ball.right >= (WINDOWWIDTH - LINETHICKNESS-EPSILON/2):
        ballDirX = ballDirX * -1
        #print("left is"+str(ball.left)+" right is "+str(ball.right))
    return ballDirX, ballDirY

#Checks is the ball has hit a paddle, and 'bounces' ball off it.     
def checkHitBall(ball, paddle1, paddle2, ballDirX):
    if ballDirX == -1 and (paddle1.right >= ball.right or paddle1.right >= ball.right-EPSILON/2) and paddle1.top < ball.top and paddle1.bottom > ball.bottom:
        #print("hit 1")
        return -1
    elif ballDirX == 1 and (paddle2.left <= ball.right or paddle2. left<= ball.left -EPSILON/2) and paddle2.top < ball.top and paddle2.bottom > ball.bottom:
        #print("hit 2")
        return -1
    else: return 1

#Checks to see if a point has been scored returns new score
def checkPointScored(paddle1, ball, score, ballDirX):
    
    #print("ball at"+str(ball.left)+" , "+str(ball.right))
    #2 point for hitting the ball
    if ballDirX == -1 and (paddle1.right >= ball.right or paddle1.right >= ball.right-EPSILON/2) and paddle1.top < ball.top and paddle1.bottom > ball.bottom:
        print("Score +2!")
        score += 5
        return score

    # -5 pts if wall is hit
    elif ballDirX == -1 and (paddle1.right >= ball.right or paddle1.right >= ball.right-EPSILON/2):
        print("Score -5!")
        score -= 0.2
        return score
    # #5 points for beating the other paddle
    # elif ball.right == WINDOWWIDTH - LINETHICKNESS:
    #     score += 5
    #     return score
    #if no points scored, return score unchanged
    else: return score

#Artificial Intelligence of computer player 
def artificialIntelligence(ball, ballDirX, paddle2):
    #If ball is moving away from paddle, center bat
    if ballDirX == -1:
        if paddle2.centery < (WINDOWHEIGHT/2):
            paddle2.y += 1
        elif paddle2.centery > (WINDOWHEIGHT/2):
            paddle2.y -= 1
    #if ball moving towards bat, track its movement. 
    elif ballDirX == 1:
        if paddle2.centery < ball.centery:
            paddle2.y += 1
        else:
            paddle2.y -=1
    return paddle2

#Displays the current score on the screen
def displayScore(score):
    resultSurf = BASICFONT.render('Score = %s' %(score), True, WHITE)
    resultRect = resultSurf.get_rect()
    resultRect.topleft = (WINDOWWIDTH - 150, 25)
    DISPLAYSURF.blit(resultSurf, resultRect)


#Main function
def main():
    pygame.init()
    global DISPLAYSURF
    ##Font information
    global BASICFONT, BASICFONTSIZE
    BASICFONTSIZE = 20
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)

    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT)) 
    pygame.display.set_caption('Pong')

    #Initiate variable and set starting positions
    #any future changes made within rectangles
    ballX = WINDOWWIDTH/2 - LINETHICKNESS/2
    ballY = WINDOWHEIGHT/2 - LINETHICKNESS/2
    playerOnePosition = (WINDOWHEIGHT - PADDLESIZE) /2
    playerTwoPosition = (WINDOWHEIGHT - PADDLESIZE) /2
    score = 0

    #Keeps track of ball direction
    ballDirX = -1 ## -1 = left 1 = right
    ballDirY = -1 ## -1 = up 1 = down

    #Creates Rectangles for ball and paddles.
    paddle1 = pygame.Rect(PADDLEOFFSET,playerOnePosition, LINETHICKNESS,PADDLESIZE)
    paddle2 = pygame.Rect(WINDOWWIDTH - PADDLEOFFSET - LINETHICKNESS, playerTwoPosition, LINETHICKNESS,PADDLESIZE)
    ball = pygame.Rect(ballX, ballY, LINETHICKNESS, LINETHICKNESS)

   
    #Draws the starting position of the Arena
    drawArena()
    drawPaddle(paddle1)
    drawPaddle(paddle2)
    drawBall(ball)

    pygame.mouse.set_visible(0) # make cursor invisible

    
    while True: #main game loop
        
       
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

           
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_UP]:
            paddle1.y -= 10
        if keys_pressed[pygame.K_DOWN]:
            paddle1.y +=10

        
        drawArena()
        drawPaddle(paddle1)
        drawPaddle(paddle2)
        drawBall(ball)

        ball = moveBall(ball, ballDirX, ballDirY)
        ballDirX, ballDirY = checkEdgeCollision(ball, ballDirX, ballDirY)
        score = checkPointScored(paddle1, ball, score, ballDirX)
        ballDirX = ballDirX * checkHitBall(ball, paddle1, paddle2, ballDirX)
        paddle2 = artificialIntelligence (ball, ballDirX, paddle2)

        displayScore(score)

        pygame.display.flip()
        
        FPSCLOCK.tick(FPS)

if __name__=='__main__':
    main()