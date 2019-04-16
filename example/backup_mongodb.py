# -*- coding: utf-8 -*-

import backup_mongodb_settings
from dba.mongodb.backup.strategy_backup_every_x_seconds_for_y_seconds import (
    backup_to_local, backup_to_local_and_s3, remove_expired_backup,
)

dbname = "devtest"

backup_to_local(dbname)
backup_to_local_and_s3(dbname)
remove_expired_backup(dbname, period_days=180)
