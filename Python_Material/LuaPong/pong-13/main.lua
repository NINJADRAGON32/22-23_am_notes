push = require 'push'         --import class
Class = require 'class'
require 'Ball'
require 'Paddle'
--physical window
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
--virtual window size:  Your coordinates will be based on this system
VIRTUAL_WIDTH = 432
VIRTUAL_HEIGHT = 432

PADDLE_SPEED = 200



--Runs when the game first starts up, only once... only once
function love.load()
     --nearest-nearest filtering on upscaling and downscaling to prevent blurring of text and graphics
     love.graphics.setDefaultFilter('nearest','nearest')


     --set the title
     love.window.setTitle('Pong')

     -- set the seed or the randomness of the serve
     --if we set the randomness based off of time in theory it is max random
     math.randomseed(os.time())



     --more retro looking font we need to load it in   newFont('file',size)
     smallFont = love.graphics.newFont('font.ttf',8)
     scoreFont = love.graphics.newFont('font.ttf',32)
     largeFont = love.graphics.newFont('font.ttf', 16)

     --set the font to the retro look
     love.graphics.setFont(smallFont)

     sounds = {
          ['paddle_hit'] = love.audio.newSource('sounds/paddle_hit.wav','static'),
          ['score'] = love.audio.newSource('sounds/score.wav','static'),
          ['wall_hit'] = love.audio.newSource('sounds/wall_hit.wav','static')
     }

     --initialize our virtual res screen inside of the original window size
     push:setupScreen(VIRTUAL_WIDTH,VIRTUAL_HEIGHT,WINDOW_WIDTH,WINDOW_HEIGHT,{
          fullscreen=false,
          resizable=false,
          vsync=true
     })

     -- setup score
     player1Score=7
     player2Score=7
     player3Score=7
     player4Score=7

     --create a paddle
     player1= Paddle(10,30,5,20)
     player2= Paddle(VIRTUAL_WIDTH-10,VIRTUAL_HEIGHT-30,5,20)
     player3= Paddle(150,20,20,5)
     player4= Paddle(VIRTUAL_WIDTH-10,VIRTUAL_HEIGHT-30,20,5)

     --create a ball
     ball=Ball(VIRTUAL_WIDTH/2-2,VIRTUAL_HEIGHT/2-2,4,4)

     -- preset the ball velocity vector

     --setting up the game to be in a sart mode or main menu
     servingPlayer = 1
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
     --player 3 or top movement
     if love.keyboard.isDown('a') then
          player3.dx=-PADDLE_SPEED
     elseif love.keyboard.isDown('d') then
          player3.dx=PADDLE_SPEED
     else
          player3.dx=0
     end
     --player 4 or bottom movement
     if love.keyboard.isDown('left') then
          player4.dx=-PADDLE_SPEED
     elseif love.keyboard.isDown('right') then
          player4.dx = PADDLE_SPEED
     else
          player4.dx=0
     end


     if gameState == 'serve' then
          if servingPlayer == 1 then
               ball.dx = math.random(140,200)
          else 
               ball.dx = -math.random(140,200)
          end
          ball.dy = math.random(-50,50)
     elseif gameState == 'play' then
          
          if ball:collides(player1) then
               ball.dx = -ball.dx * 1.03
               ball.x = player1.x+5

               if ball.dy<0 then 
                    ball.dy= -math.random(10,150)
               else
                    ball.dy= math.random(10,150)
               end
               sounds['paddle_hit']:play()
          end
          if ball:collides(player2) then
               ball.dx = -ball.dx * 1.03
               ball.x = player2.x-5

               if ball.dy<0 then 
                    ball.dy= -math.random(10,150)
               else
                    ball.dy= math.random(10,150)
               end
               sounds['paddle_hit']:play()
          end
          if ball:collides(player3) then
               ball.dy = -ball.dy * 1.03
               ball.y = player3.y+5

               if ball.dx<0 then 
                    ball.dx= -math.random(10,150)
               else
                    ball.dx= math.random(10,150)
               end
               sounds['paddle_hit']:play()
          end
          if ball:collides(player4) then
               ball.dy = -ball.dy * 1.03
               ball.y = player4.y-5

               if ball.dx<0 then 
                    ball.dx= -math.random(10,150)
               else
                    ball.dx= math.random(10,150)
               end
               sounds['paddle_hit']:play()
          end
          -- if ball.y<=0 then
          --      ball.y=0
          --      ball.dy= -ball.dy
          --      sounds['wall_hit']:play()
          -- end
          -- if ball.y>= VIRTUAL_HEIGHT-4 then
          --      ball.y = VIRTUAL_HEIGHT-4
          --      ball.dy = -ball.dy
          --      sounds['wall_hit']:play()
          -- end

          ball:update(dt)
     end


     if ball.x < 0 then
          player1Score = player1Score - 1
          servingPlayer = 2
          if player1Score ==0 then
               winningPlayer=1
               gameState='done' 
          else

               gameState = 'serve'
          end
          ball:reset()
          sounds['score']:play()
     end
     if ball.y < 0 then
          player3Score = player3Score - 1
          servingPlayer = 2
          if player3Score ==0 then
               winningPlayer=3
               gameState='done' 
          else

               gameState = 'serve'
          end
          ball:reset()
          sounds['score']:play()
     end
     if ball.x > VIRTUAL_WIDTH then
          player2Score = player2Score - 1
          servingPlayer = 1
          if player2Score ==0 then
               winningPlayer=2
               gameState='done' 
          else
               gameState = 'serve'
          end
          ball:reset()
          sounds['score']:play()
     end
     if ball.y > VIRTUAL_HEIGHT then
          player4Score = player4Score - 1
          servingPlayer = 1
          if player4Score ==0 then
               winningPlayer=4
               gameState='done' 
          else
               gameState = 'serve'
          end
          ball:reset()
          sounds['score']:play()
     end




     player1:update(dt,1)
     player2:update(dt,2) 
     player3:update(dt,3)
     player4:update(dt,4) 
end

function love.keypressed(key)
     --keys can be accessed by string name
     if key =='escape' then
          love.event.quit()
     elseif key =='enter' or key =='return' then
          if gameState=='start'then
               gameState = 'serve'
          elseif gameState == 'serve' then
               gameState = 'play'  
          elseif gameState == 'done' then
               gameState = 'serve'
               player1Score = 0
               player2Score = 0
               ball:reset()
               if winningPlayer ==1 then
                    servingPlayer = 2
               else
                    servingPlayer = 1
               end
          end
     end
end

--Called after update function by Love2D, this draws what is on your screen
function love.draw()
     --begin redering a virtual res
     push:apply('start')

     -- clear the screen AND set the background color(R,G,B,A)
     love.graphics.clear(40,45,52,255)

     if gameState == 'start' then
          love.graphics.setFont(smallFont)
          love.graphics.printf('Welcome to Pong!', 0, 10, VIRTUAL_WIDTH, 'center')
          love.graphics.printf('Press Enter to begin!', 0, 20, VIRTUAL_WIDTH, 'center')
     elseif gameState == 'serve' then
          love.graphics.setFont(smallFont)
          love.graphics.printf('Player ' .. tostring(servingPlayer) .. "'s serve!", 
              0, 10, VIRTUAL_WIDTH, 'center')
          love.graphics.printf('Press Enter to serve!', 0, 20, VIRTUAL_WIDTH, 'center')
     elseif gameState == 'play' then
          -- no UI messages to display in play
     elseif gameState == 'done' then
          love.graphics.setFont(largeFont)
          love.graphics.printf('Player ' .. tostring(winningPlayer) .. ' wins!',
            0, 10, VIRTUAL_WIDTH, 'center')
          love.graphics.setFont(smallFont)
          love.graphics.printf('Press Enter to restart!', 0, 30, VIRTUAL_WIDTH, 'center')
      end

     love.graphics.setFont(scoreFont)
     love.graphics.print(tostring(player1Score), VIRTUAL_WIDTH / 2 - 50, VIRTUAL_HEIGHT / 3)
     love.graphics.print(tostring(player2Score), VIRTUAL_WIDTH / 2 + 30, VIRTUAL_HEIGHT / 3)
     love.graphics.print(tostring(player3Score), VIRTUAL_WIDTH / 2 - 50, VIRTUAL_HEIGHT / 4+100)
     love.graphics.print(tostring(player4Score), VIRTUAL_WIDTH / 2 + 30, VIRTUAL_HEIGHT / 4+100)

     --love.graphics.rectangle('fill option',x,y,w,h)   --w and h can stretch the paddle....
     --left side paddle
     player1:render()
     player2:render()
     player3:render()
     player4:render()

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
--[[
    Called by LÖVE whenever we resize the screen; here, we just want to pass in the
    width and height to push so our virtual resolution can be resized as needed.
]]
function love.resize(w, h)
    push:resize(w, h)
end