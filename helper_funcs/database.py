# (c) @PredatorHackerzZ

from configs import Config
from helper_funcus.databasecq import Database

db = Database(Config.MONGODB_URI, Config.SESSION_NAME)
