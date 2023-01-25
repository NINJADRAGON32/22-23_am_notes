push = require 'push'         --import class

--physical window
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
--virtual window size:  Your coordinates will be based on this system
VIRTUAL_WIDTH = 432
VIRTUAL_HEIGHT = 243

PADDLE_SPEED = 200



--Runs when the game first starts up, only once... only once
function love.load()
     --nearest-nearest filtering on upscaling and downscaling to prevent blurring of text and graphics
     love.graphics.setDefaultFilter('nearest','nearest')

     -- set the seed or the randomness of the serve
     --if we set the randomness based off of time in theory it is max random
     math.randomseed(os.time())



     --more retro looking font we need to load it in   newFont('file',size)
     smallFont = love.graphics.newFont('font.ttf',8)
     scoreFont = love.graphics.newFont('font.ttf',32)

     --set the font to the retro look
     love.graphics.setFont(smallFont)

     --initialize our virtual res screen inside of the original window size
     push:setupScreen(VIRTUAL_WIDTH,VIRTUAL_HEIGHT,WINDOW_WIDTH,WINDOW_HEIGHT,{
          fullscreen=false,
          resizable=false,
          vsync=true
     })

     -- setup score
     player1Score=0
     player2Score=0

     --set up paddle location
     player1Y=30
     player2Y= VIRTUAL_HEIGHT-50

     -- ball default location
     ballx = VIRTUAL_WIDTH/2-2
     bally = VIRTUAL_HEIGHT/2-2

     -- preset the ball velocity vector
     ballDX = math.random(2) ==1 and 100 or -100  -- secret cheat really a conditional if statement(if 1=100 if 2=-100)
     ballDY = math.random(-50,50)

     --setting up the game to be in a sart mode or main menu

     gameState = 'start'
end

--update runs every time the screen refreshes
function love.update(dt)
     --player 1 or left side movement (the variable)
     if love.keyboard.isDown('w') then
          player1Y = player1Y + -PADDLE_SPEED*dt
     elseif love.keyboard.isDown('s') then
          player1Y = player1Y + PADDLE_SPEED*dt
     end
     --player 2 or right side movement
     if love.keyboard.isDown('up') then
          player2Y = player2Y + -PADDLE_SPEED*dt
     elseif love.keyboard.isDown('down') then
          player2Y = player2Y + PADDLE_SPEED*dt
     end

     if gameState == 'play' then
          -- pos=init pos + vector*time
          ballx = ballx+ballDX*dt
          bally = bally+ballDY*dt
     end
end

function love.keypressed(key)
     --keys can be accessed by string name
     if key =='escape' then
          love.event.quit()
     elseif key =='enter' or key =='return' then
          if gameState=='start'then
               gameState = 'play'
          else 
               gameState = 'start'  
               ballx = VIRTUAL_WIDTH/2-2
               bally = VIRTUAL_HEIGHT/2-2
          
               -- preset the ball velocity vector
               ballDX = math.random(2) ==1 and 100 or -100  -- secret cheat really a conditional if statement(if 1=100 if 2=-100)
               ballDY = math.random(-50,50) * 1.5
          end
     end
end

--Called after update function by Love2D, this draws what is on your screen
function love.draw()
     --begin redering a virtual res
     push:apply('start')

     -- clear the screen AND set the background color(R,G,B,A)
     love.graphics.clear(40,45,52,255)

     love.graphics.printf('Hello Pong!',0,20,VIRTUAL_WIDTH,'center')  --moving to the top of the scren

     love.graphics.setFont(scoreFont)
     love.graphics.print(tostring(player1Score), VIRTUAL_WIDTH / 2 - 50, VIRTUAL_HEIGHT / 3)
     love.graphics.print(tostring(player2Score), VIRTUAL_WIDTH / 2 + 30, VIRTUAL_HEIGHT / 3)

     --love.graphics.rectangle('fill option',x,y,w,h)   --w and h can stretch the paddle....
     --left side paddle
     love.graphics.rectangle('fill',10,player1Y,5,20)
     --right side paddle
     love.graphics.rectangle('fill',VIRTUAL_WIDTH-10,player2Y,5,20)

     --ball
     love.graphics.rectangle('fill', ballx, bally, 4, 4)

     --end rendering of virtual res
     push:apply('end')
end