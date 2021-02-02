import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd



class Scrape():
    '''
    Collection of functions used for scraping the website 
    '''

    def __init__(self, driver):
        self.driver = driver




    def input_year(self, year):

        year = str(year)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/div/section/section/div[2]/div[1]/div[2]').click()
        self.driver.find_element_by_css_selector(f"div[data-t2v-id='{year}']").click()
        time.sleep(3)


    def get_teams_in_year(self):

        page = self.driver.page_source
        soup = BeautifulSoup(page, features="lxml")
        teams_html = soup.find(id='listado_equipos').find_all(class_='elemento colorweb_7 mayusculas')

        teams_id_list = [team.get('data-t2v-id') for team in teams_html]

        return teams_id_list


    def input_team(self, team_id):

        
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/div/section/section/div[1]/div/div[2]').click()
        self.driver.find_element_by_css_selector(f"div[data-t2v-id='{team_id}']").click()


    def read_table_stats_team(self):
        page = self.driver.page_source

        df = pd.read_html(page, decimal=',', thousands='.', attrs = {'data-toggle': 'table-estadisticas-clubes'})[0] 
    
        return df


    def read_players_id(self):
        page = self.driver.page_source
        soup = BeautifulSoup(page, features="lxml")

        try:
            ids_html = soup.find_all('table',class_='roboto')[1].find_all('a')

        except IndexError:
            ids_html = soup.find_all('table',class_='roboto')[0].find_all('a')



        #table table-hover
        
        ids_list_player = [row.get('href') for row in ids_html]

        ids_list_player = [row[13:20] for row in ids_list_player]

        

        return ids_list_player


    def read_team_name(self):

        try:
            name = self.driver.find_element_by_xpath('/html/body/div[1]/div/section/div/section/header/div/div[2]/h1').text

        except:
            name = self.driver.find_element_by_xpath('/html/body/div/section/header/div/div[2]/h1').text


        return name

    



    def clean_table_stats_team(self, df):


        columns_2_drop = [df.columns[0], df.columns[4]] #not wanted columns
        df = df.drop(columns_2_drop, axis=1)[:-1] #last row also not wanted , is for whole team

        df.columns = ['player', 'games', 'time', 'points', '3p_conv', '3p_try', '3p_perc', '2p_conv', '2p_try', '2p_perc', 'free_conv','free_try','free_perc','reb_def','ref_att','reb_tot','assis','steals','turnovers','block_fav','block_con','dunks','foults_com','foults_rec','plus_minus_bal','val']

        for col in ['3p_perc', '2p_perc', 'free_perc']:
            
            df[col] = df[col].apply(lambda x: float(x.replace('%','').replace(',','.')) )

        df['time'] =  df.time.apply(lambda x: int(x.split(':')[0]) + round(int(x.split(':')[1])/60,2))

        return df
















