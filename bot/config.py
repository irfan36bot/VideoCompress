# (c) @AbirHasan2005

from bot.get_cfg import get_config

class Config(object):
    # You can keep this default
    SESSION_NAME = get_config("SESSION_NAME", "AHCompressorBot")
    # Put MongoDB URL
    DATABASE_URL = "mongodb+srv://Irfan:786or786@cluster0.2jjhd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    # get a token from @BotFather
    TG_BOT_TOKEN = "5791746051:AAGtutE1aeaeOO1EmG8guAa9pZvRNxQG4jk"
    # The Telegram API things
    APP_ID = 10956858
    API_HASH = "cceefd3382b44d4d85be2d83201102b7"
    LOG_CHANNEL = "LogChannelDSBot"
    UPDATES_CHANNEL = "DS_Botz"
     # Get these values from my.telegram.org
    # array to store the channel ID who are authorized to use the bot
    AUTH_USERS = "1125671241"
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = get_config("DOWNLOAD_LOCATION", "/app/downloads")
    # Telegram maximum file upload size
    BOT_USERNAME = get_config("BOT_USERNAME", "")
    MAX_FILE_SIZE = 2097152000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 2097152000
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = get_config("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = get_config("HTTP_PROXY", None)
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # add config vars for the display progress
    FINISHED_PROGRESS_STR = get_config("FINISHED_PROGRESS_STR", "▓")
    UN_FINISHED_PROGRESS_STR = get_config("UN_FINISHED_PROGRESS_STR", "░")
    LOG_FILE_ZZGEVC = get_config("LOG_FILE_ZZGEVC", "Log.txt")
      # because, https://t.me/c/1494623325/5603
    SHOULD_USE_BUTTONS = get_config("SHOULD_USE_BUTTONS", False)
