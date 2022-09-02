import datetime
import json
import os


class Dicts():
    '''v0002 '''
    folderlog = 'tasklogs/'
    name = 'noname'
    
    def __init__(self, dct):
        self.dct = dct
        print('установка :', datetime.datetime.now().strftime('%Y-%m-%d-%H-%M') )
        self.dct['datestr0'] = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')
        self.dct['datestr'] = None
    
    def check(self):
        return True
        
    def save(self):
        if not self.check():
            print('не правильный словарь')
        if self.dct['datestr'] == None:
            self.dct['datestr'] = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')
        self.filename = self.folderlog + 'd_' + self.name + '_' + self.dct['datestr'] + '.json'
        with open(self.filename, 'w') as writefile:
            json.dump(self.dct, writefile)
            print('dict записан: ', self.filename)
            
    def load(self):
        files = os.listdir(self.folderlog)
        print([e for e in enumerate(files)])
        i = int(input('введите номер файла: '))
        with open(self.folderlog + files[i], 'r') as writefile:
            self.dct = json.load(writefile)
        print(f'dict загружен :{self.folderlog + files[i]},\n всего\
        \n загружены атрибуты {self.dct.keys()} \
        ')#{self.dct.values()}')
        print(f'надо определить имя, из какого атрибута взять? \n\
        {[e for e in enumerate(self.dct.keys()) ]}')
        c = int(input('номер: '))
        self.name = self.dct[list(self.dct.keys())[c]]
        print (f'выбрано - {self.name}')
        
        
class Dtask(Dicts):
    '''v0000 Задачи'''
    folderlog = 'tasklogs/'
    def __init__(self, dct):
        print(f'атрибуты для задачи :\
                 name, urls, domain, taskdescr, datestr0 - АВТОМАТОМ\
                 \n папка для сохранений задач {self.folderlog}')
        #TODO DRY
        self.dct = dct
        print('установка :', datetime.datetime.now().strftime('%Y-%m-%d-%H-%M') )
        self.dct['datestr0'] = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')
        self.dct['datestr'] = None
        print(f'coздан {self.dct}')
    
    def check(self):
        return False

class Dlinks1(Dicts):
    '''v0004 save(self, taskname, links, urls, domain, taskdescr, datestr=None)'''
    
    folderlog = 'links/'
    
    def __init__(self, dct={}):
        print(f'атрибуты для линков :\
                taskname, links, urls, domain, taskdescr, datestr=None, datestr0 - АВТОМАТОМ\
                 \n папка для сохранений задач {self.folderlog}')
        self.dct = dct
        self.dct['links'] = []
        

class Dlinks():
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
