import os
from dotenv import load_dotenv

import sys
sys.path.append("../")

load_dotenv()


db_name = 'acb_stats_db'
password_mysql = os.getenv("MYSQL_PWD")
user_mysql = os.getenv("MYSQL_USER")

end_year = 2019
first_year = 1989

