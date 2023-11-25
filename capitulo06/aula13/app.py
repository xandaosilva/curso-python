import os
from dotenv import load_dotenv

load_dotenv()

db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_port = os.getenv("DB_PORT")
db_host = os.getenv("DB_HOST")

print(db_user, db_pass, db_port, db_host)
