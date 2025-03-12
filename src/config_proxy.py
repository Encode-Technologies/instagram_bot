import os

if  os.environ.get("ENV") == "prod":
    from config.config import *
else:
    from config.config_dev import *