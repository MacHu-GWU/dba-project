# -*- coding: utf-8 -*-

import os
from dba.mongodb.backup.config import Config

Config.AWS_PROFILE = "sanhe"

HOME = os.path.expanduser("~")
Config.MONGO_BACKUP_DIR = os.path.join(HOME, "Documents", "mongo-backup")
Config.MONGO_BACKUP_S3_BUCKET = "pyrabbit"
Config.MONGO_BACKUP_S3_PREFIX = "mongodb-backup"
