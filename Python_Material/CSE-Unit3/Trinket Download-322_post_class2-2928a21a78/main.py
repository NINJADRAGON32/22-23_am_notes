from Post import Post

all_posts_archive = []

# your code here
post1=Post("Marie","this is my first post")
#object = constructor(arguments)
#post1 = __init__(self,username,message)
print(post1)
#print (post1.__str__()) technically whats going on in line 9

#letters and setters
post1.set_message("I changed my message")
print(post1)

print(post1.get_post_id())
print(post1.get_user_name())