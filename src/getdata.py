
from src.scrape import Scrape as scrape
from selenium import webdriver
from tqdm import tqdm
from src.mysql import mysql as mysql
from src.config import end_year, first_year


def fetch_and_prepare_stats():

    df = scraper.read_table_stats_team()
    df = scraper.clean_table_stats_team(df)

    team_name = scraper.read_team_name()

    ids_list_player = scraper.read_players_id()

    df.insert(loc=1, column='year', value= year)
    df.insert(loc=1, column='team_id', value= team_id)
    df.insert(loc=1, column='team', value= team_name)
    df.insert(loc=1, column='player_id', value= ids_list_player)

    return df




def main():

    endpoint = 'http://www.acb.com/club/estadisticas/'
    scraper = scrape(webdriver.Chrome()) #creates the driver Objetct

    scraper.driver.get(endpoint) #goes to statistics page

    table_exist = mysql.check_exist_table()

    for year in range(end_year,first_year,-1):

        print(year)
        scraper.input_year(year)
        teams_id_list = scraper.get_teams_in_year()

        for team_id in tqdm(teams_id_list):
            if table_exist:
                res = mysql.check_team_year_scraped(team_id, year)
                if res:
                    print(f'{team_id} in {year} already scraped')
                    continue
            else:
                pass

            scraper.input_team(team_id)

            df = fetch_and_prepare_stats()

            df.to_sql('player_stats', con=mysql.conn, if_exists = 'append', index=False)























