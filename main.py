# import os
# import bot
from bot import InstaFollower

# instagram_follow_bot = InstaFollower(driver_path=os.environ.get(key='CHROME_DRIVER_PATH'))
instagram_follow_bot = InstaFollower()
instagram_follow_bot.login()
instagram_follow_bot.find_followers()
instagram_follow_bot.follow()
