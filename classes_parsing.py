'''v050922
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
        super().__init__(dct)

    def check(self):
        return False

class Dlinks(Dicts):
    '''v0005 save(self, taskname, links, urls, domain, taskdescr, datestr=None)'''
    
    folderlog = 'links/'
    
    def __init__(self, dct:dict):
        ''' parametr: Dtask.dict'''
        super().__init__(dct)
        self.dict['links'] = []
    
    def check(self):
        return False
    

