from Post import Post
#from file import class

all_posts_archive = []

# your code here
post1 = Post("Marie","This is my first post")
#object = Constructor(arguments)
#post1 = __init__(self,username,message)  technically in the line 2 rows above
print(post1)
#print(post1.__str__()) technically what's in the line above

#getters and setters
post1.set_message("I changed my message")
print(post1)

print(post1.get_post_id())
print(post1.get_user_name())