import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "28669943"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 5992762416:AAFTtztxqjExwJ7UWLwmeWyUEpzDbZTBteY)
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BVtsOHYBuyALhpkVMivImhkpIY48-nJlxQygjyM68UyK3cMy1wwWyUkQ-XldFrJj8orWFRcCb2DjTTrztTnynlTMKDfiiq7gZZT60xT_HooVL3Oat1JbFWZl8_ydi05jhisDY1ersqfmMEwMbdEF6VGHzsoo9-UTZQD_iDwsgP11XyTjS9k398kj9y4gPXVemegLVwLcIXtaZryY2TfZHiREp5z1L9eIZb0ELqtuvMSj8bFHVQjMdiPkEYG4skGBM0ZT9dtS3Oreue7GxWPRwx-6K1WfWyHMJxcbE2_nICH2QZKhxzyi6di_7pK1XiANm0phcgfADmLoDcJQ6-8YbdLo566BN7w=)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
