'''v070922
'''
import datetime
import json
import os
import re
import requests
from requests import Request, Session
from bs4 import BeautifulSoup
import pandas as pd


class Site():
    '''v0003'''
    folderres = 'results/'
    
    def __init__(self):
        '''parametr: '''
        #self.dict = dct
        print ('create')#self.dict['domain'])
     
    def mysoup(self,urls):
        response = requests.get(urls)
        return BeautifulSoup(response.text, 'lxml')  
  
    def getlinks_sunl(self,urls):
        quotes = self.mysoup(urls).find_all('a', class_="cl-item-link js-cl-item-link js-cl-item-root-link")
        res = [q.get("href") for q in quotes]
        print(len(res), 'links is ready ' , res[0], '...', res[-1])
        return res
        
        
    def genlinks_sunl(self, task):
        '''task: classes_parsing.Dtask'''
        yield task.dict['urls0']
       # 'urlslast':'https://sunlight.net/catalog/diamonds-all/page-104/'
        text = task.dict['urlslast'].strip().split('/')[-2]
        n = int(re.search(r'\d+',text)[0])
        ch = text[re.search(r'\d+',text).span()[0]-1]
        urls = '/'.join(task.dict['urlslast'].strip().split('/')[0:-2])
        for i in range(2,n):
            pages = f'/page{ch}{i}/'
            #pages = f'&page={i}'#без вставки
            yield urls+pages
                  
        
    def getlinks(self, task)->None:#
        '''create list links and modify object task'''
        genlink = self.genlinks_sunl(task)
        links = []
        i = 0
        for l in genlink:
            print(i, l)
            links += self.getlinks_sunl(l)
            i+=1
        task.dict['links'] = links
        
        
        
    def parcing(self, task):
        def savereserve_csv(data):
            datestr = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')
            filename = self.folderres + '/_reserve_' + task.dict['name'] + datestr + '.csv'
            data.to_csv(filename)
            return filename
        
            
        data = pd.DataFrame(columns=['h1','art','price','price2','gold','gold2','weight','gems','gems2','url'])
        domain = task.dict['domain']
        links = task.dict['links']               
        print('парсинг  ', len(links))
        for i in range(0,len(links)):
            try:
                row = i
                urlcard = domain + links[i]
                response = requests.get(urlcard)
                card = BeautifulSoup(response.text, 'lxml')
                #card = mysoup(urlcard)
                data.loc[row, 'url'] = urlcard
                data.loc[row, 'h1'] = card.find("h1").text.strip()
                data.loc[row, 'art'] = card.find('div', class_="supreme-product-card__product-article-text").text.strip()
                data.loc[row, 'price'] = card.find('div',
                                                   class_="supreme-product-card__price-discount-price").text.strip().replace(
                    '\u202f', '').replace('\xa0', '')
                data.loc[row, 'price2'] = card.find('div', class_="supreme-product-card__price-old").text.strip().replace(
                    '\u202f', '').replace('\xa0', '')
                a = card.find_all('p', class_="supreme-product-card__description supreme-product-card__description_default")
                data.loc[row, 'gold'] = ';'.join([x.text for x in a])
                data.loc[row, 'd1'] = "&".join(
                    [t.text for t in card.find_all('span', class_="supreme-product-card-description__item-text")])
                data.loc[row, 'd0'] = "&".join(
                    [t.text for t in card.find_all('a', class_="supreme-product-card-description__item-text")])
                # print(i, urlcard)
            except (AttributeError, TypeError) as e:
                print('error', e)
            except IndexError:
                print('IndexError')
            except Exception as e:
                print('ошибка:', e)
                input('жду')
            print(i, urlcard)
            if i%100 == 0:
                print('saved', i, savereserve_csv(data))
            
        lastfile = savereserve_csv(data)
        print('saved last', i, lastfile)
        task.dict['datestr'] = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')
        task.dict['parcing'] = lastfile
        return data



      