bgX = -100
bgY = 0
i = 1
birdX = 50
birdY = 350
x = 0
y = 0
c = 0
c2 = 180
c3 = 190
x2 = 720
add_library("minim")
minim = Minim(this)
ySpeed = 3
xSpeed = 3

def gameOverScreen():
    global x,y,c,c2,c3,x2
    while y < 1280 :
        stroke(c,c2,c3)
        line(0,y,720,y)
        y = y+1
        c = c+.5
        c2 = c2+1
        c3 += 1
        if y < 150:
            c-= 1
            c2 = c2-1
            c3 = c3-1
        if y < 120:
            c=c-.5
            c2 = c2-1
            c3 = c3-1
        if y < 600:
            c=c+1
            c3 = c3-1
        textSize(62)
        fill(0,0,0)
        text("GAME OVER", 120, 150)
        noFill()
        textSize(32)
        fill(0,0,0)
        text("Restart Game", 230, 300)
    img = loadImage("reset.png")
    image(img,80,265,143,47)
    
def startScreen():
    global x, y, c, c2, c3, x2
    while y < 1280:
        stroke(c, c2, c3)
        line(0, y, 720, y)
        y = y + 1
        c = c + .5
        c2 = c2 + 1
        c3 += 1
        if y < 150:
            c -= 1
            c2 = c2 - 1
            c3 = c3 - 1
        if y < 120:
            c2 = c2 - 1
            c3 = c3 - 1
        if y < 100:
            c3 = c3 - 1
        textSize(32)
        fill(0, 225, 0)
        text("Wings of Prey", 225, 150)
        noFill()
        strokeWeight(10)
        rect(200, 100, 255, 80, 10)
        ellipse(145, 287, 5, 5)
        fill(0, 0, 100)
        text("Start Game", 230, 300)
        noFill()
        triangle(200, 290, 120, 250, 120, 340)

'''def barriers():
    global x, y, speedX, speedY
    speedX = 0
    speedY = 0
    #image(birdImage, birdX, birdY, 50, 50)
    if x > mouseX and x < mouseY + 100 and y >= 700:
        speedY = -speedY

    x += speedX
    y += speedY'''

def startGame():
    cityBackground()
    bird()
    firTube()
    secTube()
    thirdTube()
    fourthTube()
    font()
    text("Hint: ", 365, 560)
    text("Just Keep Flying!", 365, 600)
   # barriers()
    borders()
    print(birdX, birdY)


def setup():
    i = 0
    global starting,over
    if i < 10:
        player = minim.loadFile("flappy_1.mp3")
        player.play()

    global backgroundUpload, birdImage
    size(600, 700)
    backgroundUpload = loadImage("Flappy Bird Background.png")
    birdImage = loadImage("Flappy Bird.png")
    starting = True
    over=True

def draw():
    global starting,over
    
    #if over=-False
    if starting:
        # if starting is true, the startScreen function is initialized
        startScreen()
        if mousePressed == True:
            starting = False
    else:
        # if starting is false, the startGame function is initialized, and the
        # game will start
        startGame()

def font():
    fill(255)
    font = createFont("angrybirds-regular.ttf", 32)
    textFont(font)

def cityBackground():
    background(255)
    global bgX
    image(backgroundUpload, bgX, bgY, 800, 700)
    bgX = bgX + 1.5
    if(bgX > 0):
        bgX = -100

def bird():
    global birdX, birdY, ySpeed, xSpeed
    image(birdImage, birdX, birdY, 50, 50)
    fill(0)
    #rect(birdX, birdY, 15, 15)
    birdY = birdY + ySpeed
    birdX = birdX + xSpeed
    # bird movement
    if(mousePressed == True and birdX > 600):
        birdX = 0
    if(mousePressed == True):
        birdY = birdY - (ySpeed / .3)
def cenEllipseW(birdX, w, x):

    centerX = (x)
    (birdX - centerX) * (birdX - centerX) / (w * w)
    return (birdX - centerX) * (birdX - centerX) / (w * w)

def cenEllipseH(birdY, h, y):
    centerY = (y)
    (birdY - centerY) * (birdY - centerY) / (h * h)
    return (birdY - centerY) * (birdY - centerY) / (h * h)

def borders():
    global birdX, birdY, ySpeed, xSpeed
    if (birdY > 560):  # bottom of screen
        ySpeed = 0
        text("Game Over!", 220, 300)
        gameOver()
    if (birdY < 2):
        gameOver()
        ySpeed = 0

    # tube on the left of the screen
    if ((cenEllipseW(birdX, 72.5, 80)) + (cenEllipseH(birdY, 25, 255)) < 1):
        gameOver()
    #tube in the middle at the top of the screen
    if ((cenEllipseW(birdX, 72.5, 286)) + (cenEllipseH(birdY, 25, 400)) < 1):
        gameOver()
    #tube at the bottom of the screen
    if ((cenEllipseW(birdX, 72.5, 505)) + (cenEllipseH(birdY, 25, 255)) < 1):
        gameOver()
    #tube at the right of the screen
    if ((cenEllipseW(birdX, 72.5, 286)) + (cenEllipseH(birdY, 25, 100)) < 1):
        gameOver()
    


def gameOver():
    global xSpeed, ySpeed
    ySpeed = 0
    xSpeed = 0
    text("Game Over!", 220, 300)
def firTube():
    # first tube on top
    # noStroke()
    stroke(12, 153, 12)
    fill(124, 194, 25)
    rect(25, -1, 15, 250)  # left
    rect(55, -1, 50, 250)  # middle
    rect(120, -1, 15, 250)  # right
    fill(12, 153, 12)
    ellipse(80, 255, 145, 50)

def secTube():
    # second tube on bottom
    # noStroke()
    stroke(12, 153, 12)
    fill(124, 194, 25)
    rect(230, 400, 15, 215)  # left
    rect(260, 400, 55, 215)  # middle
    rect(330, 400, 15, 215)  # right
    fill(12, 153, 12)
    ellipse(286, 400, 145, 50)

def thirdTube():
    # third tube on top
    noStroke()
    stroke(12, 153, 12)
    fill(124, 194, 25)
    rect(450, -1, 15, 250)  # left
    rect(480, -1, 50, 250)  # middle
    rect(545, -1, 15, 250)  # right
    fill(12, 153, 12)
    ellipse(505, 255, 145, 50)

def fourthTube():
    # fourth tube in the middle of the top of the screen
    noStroke()
    stroke(12, 153, 12)
    fill(124, 194, 25)
    rect(230, -1, 15, 80)  # left
    rect(260, -1, 50, 80)  # middle
    rect(330, -1, 15, 80)  # right
    fill(12, 153, 12)
    ellipse(286, 100, 145, 50)
