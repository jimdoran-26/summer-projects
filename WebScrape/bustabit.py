import requests
import time
import sys
from os import system
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np

#URL = "https://www.bustabit.com/play"
URL = 'https://www.bustabit.com/game/3274896'

def get_bust(url):
    for x in range(1,2):
    #test the connection
            bustb = pd.DataFrame()
            col = -1

            
            res=requests.get(url)
            #html_string = requests.get(url).text

            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            
            #table = soup.find_all('table') # Grab the first table
            print(soup)
            #body = soup.find_all('tbody')[0] # get body within the table
            #tr = soup.find_all('tr')[0] # get tr within the body

            #cur_list = []
            #for td in tr.findAll('td'):
             #   for a in td.findAll('a'):
              #      value = td.get_text()
               #     value = value.strip()
                #    cur_list.append(value)
            #col+=1
            #bustb['col'+str(col)]= cur_list

            time.sleep(5)
        

    #print(bustb)


get_bust(URL)





html_string1 = '''
        <table class="table table-striped table-condensed" style="margin-bottom: 0px;">
        <tbody style="text-align: center;">
        <tr style="background-color: transparent;">

        <td style="opacity: 1; width: 14.29%; border-top-width: 0px;">
        <a href="/game/3274129" style="color: rgb(255, 90, 95);">
        1.65x
        </a>
        </td>

        <td style="opacity: 1; width: 14.29%; border-top-width: 0px;">
        <a href="/game/3274128" style="color: rgb(46, 204, 113);">
        2.01x
        </a>
        </td>

        <td style="opacity: 1; width: 14.29%; border-top-width: 0px;">
        <a href="/game/3274127" style="color: rgb(255, 90, 95);">
        1.42x
        </a>
        </td>

        <td style="opacity: 1; width: 14.29%; border-top-width: 0px;">
        <a href="/game/3274126" style="color: rgb(255, 90, 95);">
        1.84x
        </a>
        </td>

        <td style="opacity: 0.7; width: 14.29%; border-top-width: 0px;">
        <a href="/game/3274125" style="color: rgb(46, 204, 113);">
        6.53x
        </a>
        </td>

        <td style="opacity: 0.5; width: 14.29%; border-top-width: 0px;">
        <a href="/game/3274124" style="color: rgb(255, 90, 95);">
        1.67x
        </a>
        </td>
        
        <td style="opacity: 0.25; width: 14.29%; border-top-width: 0px;">
        <a href="/game/3274123" style="color: rgb(46, 204, 113);">
        8.85x
        </a>
        </td>

        </tr>
        </tbody>
        </table>
        <tr>
    '''



#get_bust(html_string1)
