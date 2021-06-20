# (c) @PredatorHackerzZ

from sample_config import Config
from helper_funcs.databasecq import Database

db = Database(sample_config.config.MONGODB_URI, sample_config.config.SESSION_NAME)
