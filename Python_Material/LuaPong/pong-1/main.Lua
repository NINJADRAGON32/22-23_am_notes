--[[ 
    love 2 d looks for functions 
         it has a certain orer for functions to run
]]

-- screen ratio 16:9 ...... remeber this ......
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
function love.load()
love.window.setMode(WINDOW_WIDTH,WINDOW_HEIGHT,{
    fullscreen =false,
    resizable =false,
    vsync = true
    })
end

function love.update()
end

-- Called after the love function after Love ,n this rdraws what is on your screen
function love.draw()
    love.graphics.printf(
        'hello pong!' , 
        0,                   -- startingx
        WINDOW_HEIGHT/2 - 6, -- startingy
        WINDOW_WIDTH,        -- center align (left or right)
        'center')
end 
