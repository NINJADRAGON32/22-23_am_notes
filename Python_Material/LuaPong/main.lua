-- is this a comment?
-- is a comment

--[[
    multi 
        line        
            comment
  ]]

-- Global Variables
hello='hello'
-- Local Variable
local world= ' world!'

-- Functions
--declare a function tat says hello
function sayhello(text)
    print(text)
    end

-- call a function
sayhello("hello world")
sayhello(hello . . world)

--conditionals
if world == 'world' then
    print('world')
else
    print('hello!')
    end
-- while loops
local i=10
while i!=0 do
    i=i-1
    print(i)
    end

--for loop
for j=10,1,-1 do
    print(j)
    end

--repeat
i=10
repeat
    i=i-1
    print(i)
until 1==0


--tables
--one variable with many characteristics
--tables are similsr to python lists
local person = {}
person.name="ty"
person.age = 87
person.height = 60

--call info 
print(person['name']) -- python dictionarys
print(person.name)
for key, value in pairs(person) do
    print(key,value)
end