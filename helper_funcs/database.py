# (c) @PredatorHackerzZ

from sample_config import Config
from helper_funcs.databasecq import Database

db = Database(Config.MongoDB_URI, Config.SESSION_NAME)
