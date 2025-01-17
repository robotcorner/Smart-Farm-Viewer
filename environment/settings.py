import os
from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv

# dotenv_path = join(dirname(__file__), os.getenv("ENVIRONMENT_FILE"))
# load_dotenv(dotenv_path=dotenv_path, override=True)
load_dotenv(find_dotenv())
APP_HOST = os.environ.get("HOST")
APP_PORT = int(os.environ.get("PORT"))
APP_DEBUG = bool(os.environ.get("DEBUG"))
DEV_TOOLS_PROPS_CHECK = bool(os.environ.get("DEV_TOOLS_PROPS_CHECK"))
DEV_TOOLS_SILENCE_ROUTES = bool(os.environ.get("DEV_TOOLS_SILENCE_ROUTES"))
USE_RELOADER = bool(os.environ.get("USE_RELOADER"))