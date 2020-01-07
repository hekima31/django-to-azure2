import os
from dotenv import load_dotenv
load_dotenv()

print(os.environ.get("DJANGO_SETTINGS_MODULE"))
print(os.environ.get("DEBUG_VALUE"))
