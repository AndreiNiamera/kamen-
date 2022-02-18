from instapy import InstaPy

session = InstaPy(username="andrya200254", password="Qwe125478qwe")
session.login()

session.like_by_tags(['cars', 'people'], amount=10)

session.follow_user_followers(['friend1', 'friend2', 'friend3'], amount=10, randomize=False)

session.follow_likers(['user1' , 'user2'], photos_grab_amount = 2, follow_likers_per_photo = 3, randomize=True, sleep_delay=600)

session.end()