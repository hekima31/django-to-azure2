import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

print("Synchronization")
print("Synchronizations")
print("Synchronization")
print("Synchronization")
print("Synchronization")
print("Synchronization")
print("Synchronization")
print("Synchronization")

# Testing things out here
# print(os.environ.get("GMAIL_USERNAME"))
print(os.environ.get("GMAIL_APP_PASSWORD"))
# print(os.environ.get("OUTLOOK_USERNAME"))
# print(os.environ.get("OUTLOOK_PASSWORD"))
# print(os.getenv("DJANGO_SECRET_KEY"))
print(os.environ.get("DEBUG_VALUE"))
