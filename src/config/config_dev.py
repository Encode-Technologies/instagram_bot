import os

from dotenv import load_dotenv

load_dotenv()

OPEN_API_KEY: str = str(os.getenv("OPENAPI_KEY"))
INSTAGRAM_CLIENT_ID: str = str(os.getenv("INSTAGRAM_CLIENT_ID"))
INSTAGRAM_CLIENT_SECRET: str = str(os.getenv("INSTAGRAM_CLIENT_ID"))
INSTAGRAM_REDIRECT_URI: str = str(os.getenv("INSTAGRAM_REDIRECT_URI"))