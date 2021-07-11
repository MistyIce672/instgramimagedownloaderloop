from datetime import datetime
from itertools import dropwhile, takewhile
import instaloader
from time import sleep
L = instaloader.Instaloader()
L.login('user','password')


posts = instaloader.Profile.from_username(L.context, "profile here").get_posts()
for post in posts:
   old = (post.date)  

SINCE = (2021,5,20)
temp = old
while 1 > 0:
   new = False
   print( "new was set to false")
   UNTIL = temp
   SINCE = datetime.now()
   print ('xyz is',SINCE)
   posts = instaloader.Profile.from_username(L.context, "profile here").get_posts()
   for post in takewhile(lambda p: p.date > UNTIL, dropwhile(lambda p: p.date > SINCE, posts)):
      if new == False: 
         temp = post.date
         new = True
      print(post.date)
      L.download_post(post, "instagram")
   print("going to sleep")
   sleep(5)