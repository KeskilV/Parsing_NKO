'''v050922 before
.dict'''
import datetime
import json
import os


class Dicts():
    '''v0003 '''
    folderlog = 'tasklogs/'
    name = 'noname'
    
    def __init__(self, dct:dict):
        self.dict = dct
        print('установка :', datetime.datetime.now().strftime('%Y-%m-%d-%H-%M') )
        self.dict['datestr0'] = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')
        self.dict['datestr'] = None
        if ('name' in dct.keys()) and (dct['name']!=''):
            self.name = dct['name'] 
        
            
            
    
    def check(self):
        return False
        
    def save(self):
        if not self.check():
            print('не правильный словарь')
        if self.dict['datestr'] == None:
            self.dict['datestr'] = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')
        self.filename = self.folderlog + 'd_' + self.name + '_' + self.dict['datestr'] + '.json'
        with open(self.filename, 'w') as writefile:
            json.dump(self.dict, writefile)
            print('dict записан: ', self.filename)
            
    def load(self):
        files = os.listdir(self.folderlog)
        print([e for e in enumerate(files)])
        i = int(input('введите номер файла: '))
        with open(self.folderlog + files[i], 'r') as writefile:
            self.dict = json.load(writefile)
        print(f'dict загружен :{self.folderlog + files[i]},\n всего\
        \n загружены атрибуты {self.dict.keys()} \
        ')#{self.dict.values()}')
        print(f'надо определить имя, из какого атрибута взять? \n\
        {[e for e in enumerate(self.dict.keys()) ]}')
        c = int(input('номер: '))
        self.name = self.dict[list(self.dict.keys())[c]]
        print (f'выбрано - {self.name}')
        
        
class Dtask(Dicts):
    '''v0000 Задачи'''
    folderlog = 'tasklogs/'
    def __init__(self, dct):
        print(f'атрибуты для задачи :\
                 name, urls, domain, taskdescr, datestr0 - АВТОМАТОМ\
                 \n папка для сохранений задач {self.folderlog}')
        #TODO DRY maybe add supper.init()
        self.dict = dct
        print('установка :', datetime.datetime.now().strftime('%Y-%m-%d-%H-%M') )
        self.dict['datestr0'] = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')
        self.dict['datestr'] = None
        if ('name' in dct.keys()) and (dct['name']!=''):
            self.name = dct['name'] 
        print(f'coздан {self.dict}')
    
    def check(self):
        return False

class Dlinks(Dicts):
    '''v0005 save(self, taskname, links, urls, domain, taskdescr, datestr=None)'''
    
    folderlog = 'links/'
    
    def __init__(self, dct:dict):
        ''' parametr: Dtask.dict'''
        print(f'атрибуты для линков :\
                taskname, links, urls, domain, taskdescr, datestr=None, datestr0 - АВТОМАТОМ\
                 \n папка для сохранений задач {self.folderlog}')
        self.dict = dct
        self.dict['links'] = []
        if ('name' in dct.keys()) and (dct['name']!=''):
            self.name = dct['name'] 
        

class Dlinks0():
    '''v0002 save(self, taskname, links, urls, domain, taskdescr, datestr=None)'''    

    folderlinks = 'links/'

    def save(self, taskname, links, urls, domain, taskdescr, datestr=None):
        self.taskname = taskname
        self.links = links
        self.urls = urls
        self.domain = domain
        self.taskdescr = taskdescr
        print(datestr,'now:', datetime.datetime.now().strftime('%Y-%m-%d-%H-%M') )
        if datestr == None:
            self.datestr = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')
        else:
            self.datestr = datestr
        dlinks = {'taskname': self.taskname,
                  'links': self.links,
                  'datestr': self.datestr,
                  'urls': self.urls,
                  'domain': self.domain,
                  'taskdescr': self.taskdescr}

        with open(self.folderlinks + 'dlinks_' + self.taskname + '_' + self.datestr + '.json', 'w') as writefile:
            json.dump(dlinks, writefile)
            print('линки записаны: ', self.folderlinks + 'dlinks_' + self.taskname + '_' + self.datestr + '.json')

    def load(self):
        files = os.listdir(self.folderlinks)
        print([e for e in enumerate(files)])
        i = int(input('введите номер файла: '))
        with open(self.folderlinks + files[i], 'r') as writefile:
            dlinks = json.load(writefile)
        self.taskname = dlinks['taskname']
        self.links = dlinks['links']
        self.urls = dlinks['urls']
        self.domain = dlinks['domain']
        self.taskdescr = dlinks['taskdescr']
        self.datestr = dlinks['datestr']
        print(f'линки загружены с :{self.folderlinks + files[i]},\n всего\
        {len(self.links)} линков,\n загружены атрибуты {dlinks.keys()} \
        {self.taskname, self.urls, self.domain, self.taskdescr, self.datestr}')
        return self.links
