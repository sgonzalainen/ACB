from src.config import db_name, password_mysql, user_mysql

from sqlalchemy import create_engine

class MysqlConn():
    
    
    def __init__(self):
        
        self.database = db_name
        self.connect_mysql(user_mysql, password_mysql)


    def connect_mysql(self, user, password):

        mysql_url = f'mysql://{user}:{password}@localhost/{self.database}'
        engine = create_engine(mysql_url)
        self.conn = engine.connect()



    def check_team_year_scraped(self,team_id, year):


        query = f"(SELECT * FROM player_stats WHERE team_id = '{team_id}' AND year = '{year}');"

        answer = self.conn.execute(query)

        if answer.fetchone():
            return True
        else:
            return False


    def check_exist_table(self):

        query = f"SHOW TABLES LIKE 'player_stats';"
        answer = self.conn.execute(query)

        if answer.fetchone():
            return True
        else:
            return False


  


mysql = MysqlConn()







