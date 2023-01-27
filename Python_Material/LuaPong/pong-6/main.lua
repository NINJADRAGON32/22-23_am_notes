push = require 'push'         --import class
Class = require 'class'
require 'Ball'
require 'Paddle'
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

     --create a paddle
     player1= Paddle(10,30,5,20)
     player2= Paddle(VIRTUAL_WIDTH-10,VIRTUAL_HEIGHT-30,5,20)

     --create a ball
     ball=Ball(VIRTUAL_WIDTH/2-2,VIRTUAL_HEIGHT/2-2,4,4)

     -- preset the ball velocity vector

     --setting up the game to be in a sart mode or main menu

     gameState = 'start'
end

--update runs every time the screen refreshes
function love.update(dt)
     --player 1 or left side movement (the variable)
     if love.keyboard.isDown('w') then
          player1.dy=-PADDLE_SPEED
     elseif love.keyboard.isDown('s') then
          player1.dy=PADDLE_SPEED
     else
          player1.dy=0
     end
     --player 2 or right side movement
     if love.keyboard.isDown('up') then
          player2.dy=-PADDLE_SPEED
     elseif love.keyboard.isDown('down') then
          player2.dy = PADDLE_SPEED
     else
          player2.dy=0
     end
     player1:update(dt)
     player2:update(dt)
     if gameState == 'play' then
          -- pos=init pos + vector*time
          ball:update(dt)
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
               ball:reset()
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
     player1:render()
     player2:render()

     --ball
     ball:render()

     displayFPS()
     --end rendering of virtual res
     push:apply('end')
     --render fps

end
function displayFPS()
    -- simple FPS display across all states
    love.graphics.setFont(smallFont)
    love.graphics.setColor(0, 255, 0, 255)
    love.graphics.print('FPS: ' .. tostring(love.timer.getFPS()), 10, 10)
end