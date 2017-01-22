import pygame, sys
from pygame.locals import *
import fileinput

FPS = 400

# Global Vars used throughout the whole code
WINDOWWIDTH = 400
WINDOWHEIGHT = 300
LINETHICKNESS = 10
PADDLESIZE = 80
PADDLEOFFSET = 20

EPSILON = 2
INDEX = 5

# Set up the colours
BLACK     = (0,0,0)
WHITE     = (255,255,255)

#Draws the back area of the map
def drawArena():
    DISPLAYSURF.fill((0,0,0))
    pygame.draw.rect(DISPLAYSURF, WHITE, ((0,0),(WINDOWWIDTH,WINDOWHEIGHT)), LINETHICKNESS*2)

#Draws the board
def drawPaddle(paddle):
    #Stops paddle moving too low
    if paddle.bottom > WINDOWHEIGHT - LINETHICKNESS:
        paddle.bottom = WINDOWHEIGHT - LINETHICKNESS
    #Stops paddle moving too high
    elif paddle.top < LINETHICKNESS:
        paddle.top = LINETHICKNESS
    pygame.draw.rect(DISPLAYSURF, WHITE, paddle)

#Draws the ball
def drawBall(ball):
    pygame.draw.rect(DISPLAYSURF, WHITE, ball)

#Moves the ball and returns new position
def moveBall(ball, ballDirX, ballDirY):
    ball.x += ballDirX *2
    ball.y += ballDirY *2
    return ball 

#Checks for collision on objects like wall
def checkEdgeCollision(ball, ballDirX, ballDirY):
    if ball.top <= (LINETHICKNESS+EPSILON/2) or ball.bottom >= (WINDOWHEIGHT - LINETHICKNESS-EPSILON/2):
        print("top is"+str(ball.top)+" bottom is "+str(ball.bottom))
        ballDirY = ballDirY * -1
    if ball.left <= (LINETHICKNESS+EPSILON/2) or ball.right >= (WINDOWWIDTH - LINETHICKNESS-EPSILON/2):
        ballDirX = ballDirX * -1
        print("left is"+str(ball.left)+" right is "+str(ball.right))
    return ballDirX, ballDirY

#Checks to see for bounce from board    
def checkHitBall(ball, paddle1, paddle2, ballDirX):
    if ballDirX == -1 and (paddle1.right >= ball.right or paddle1.right >= ball.right-EPSILON/2) and paddle1.top < ball.top and paddle1.bottom > ball.bottom:
        print("hit 1")
        return -1
    elif ballDirX == 1 and (paddle2.left <= ball.right or paddle2.left<= ball.left -EPSILON/2) and paddle2.top < ball.top and paddle2.bottom > ball.bottom:
        print("hit 2")
        return -1
    else: return 1

def checkPointScored(paddle1, ball, score, ballDirY):
    if ballDirY == 1 and ball.bottom >= paddle1.top-EPSILON and ball.left > paddle1.left and ball.right < paddle1.right:
        score += 2
        return score
    elif ballDirY == 1 and ball.bottom >= paddle1.top-EPSILON:
        print("score -1 "+str(paddle1.top)+" "+str(paddle1.bottom)+ " ball "+ str(ball.top)+" "+ str(ball.bottom))
        score -= 0.2
        return score
    else: return score

def displayScore(score):
    resultSurf = BASICFONT.render('Score = %s' %(score), True, WHITE)
    resultRect = resultSurf.get_rect()
    resultRect.topleft = (WINDOWWIDTH - 150, 25)
    DISPLAYSURF.blit(resultSurf, resultRect)

#Connect to muse
#get position of head (read size number of data)
def get_buffer(size):
    input_holder = []
    fi = fileinput.input()
    print(input_holder)

    for line in fi:
        if (len(input_holder) > size):
            break
        if len(line.split()) > 2 and line.split()[1] == '/muse/acc':
            input_holder.append(float(line.split()[INDEX]))

    fi.close()
    return input_holder

#start game
# while True:
def read_data_from_muse(previous_location, current_location, bench):
    fi = fileinput.input()
    # right_scale = maxup - bench
    # left_scale = bench - maxdown

    for line in fi:
        print("bias is"+str(bench))
        if len(line.split()) > 2 and line.split()[1] == '/muse/acc':
            previous_location.append(float(line.split()[INDEX]))
            previous_location.pop(0)
            current_location.append(float(line.split()[INDEX]))
            current_location.pop(0)

        cur_loc = sum(current_location)/5
        prev_loc = sum(previous_location)/len(previous_location)
        print("cur is at "+str(cur_loc))
        if (cur_loc - prev_loc> 0 ):
            fi.close()
            print(1)
            return 1

        elif (cur_loc - prev_loc< 0):
            fi.close()
            print(-1)
            return -1

        else:
            fi.close()
            print(0)
            return 0
    return 0

#Main function
def main():
    pygame.init()
    global DISPLAYSURF
    global BASICFONT, BASICFONTSIZE
    BASICFONTSIZE = 20
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)

    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT)) 
    pygame.display.set_caption('Pong')

    #Sets starting position
    ballX = WINDOWWIDTH/2 - LINETHICKNESS/2
    ballY = WINDOWHEIGHT/2 - LINETHICKNESS/2
    playerOnePosition = (WINDOWWIDTH - PADDLESIZE) /2
    score = 0

    #Keeps track of ball direction
    ballDirX = -1 ## -1 = left 1 = right
    ballDirY = -1 ## -1 = up 1 = down

    paddle1 = pygame.Rect(playerOnePosition,WINDOWHEIGHT-PADDLEOFFSET ,PADDLESIZE, LINETHICKNESS)
    ball = pygame.Rect(ballX, ballY, LINETHICKNESS, LINETHICKNESS)

    drawArena()
    drawPaddle(paddle1)
    drawBall(ball)

    previous_location = get_buffer(100)
    current_location = get_buffer(5)
    bias = sum(previous_location)/len(previous_location)
    
    count1 = 0
    count2 = 0
    while True: #main game loop
        muse_data = read_data_from_muse(previous_location, current_location, bias)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if (muse_data==1):
            paddle1.x -= 2
        elif (muse_data==-1):
            paddle1.x += 2

        if paddle1.x <= LINETHICKNESS :
            count1+=1
            paddle1.x +=5
        if paddle1.x >= WINDOWWIDTH - PADDLESIZE - LINETHICKNESS:
            count2+=1
            paddle1.x -=5
        
        #After stuck for a while, reset into the middle
        if count1 == 500 or count2 == 500:
            paddle1 = pygame.Rect(playerOnePosition,WINDOWHEIGHT-PADDLEOFFSET ,PADDLESIZE, LINETHICKNESS)
            count1 = 0
            count2 = 0

        drawArena()
        drawPaddle(paddle1)
        drawBall(ball)

        ball = moveBall(ball, ballDirX, ballDirY)
        ballDirX, ballDirY = checkEdgeCollision(ball, ballDirX, ballDirY)
        score = checkPointScored(paddle1, ball, score, ballDirY)

        displayScore(score)

        pygame.display.flip()
        
        FPSCLOCK.tick(FPS)

if __name__=='__main__':
    main()