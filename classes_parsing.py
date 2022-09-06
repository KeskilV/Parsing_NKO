'''v070922
.print'''
import datetime
import json
import os


class Dicts():
    '''v0003 '''
    folderlog = 'folder/'
    
    
    def __init__(self, dct:dict):
        self.dict = dct
        self.dict['datestr0'] = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')
        self.dict['datestr'] = None
        if ('name' in dct.keys()) and (dct['name']!=''):
            self.name = dct['name']+ datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')
        else:
            self.name = 'name'+ datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')
        self.dict['name']=self.name
        print('установка :', self.name )

    def check(self):
        return True
        
    def save(self):
        if not self.check():
            print('не правильный словарь')
        if self.dict['datestr'] == None:
            self.dict['datestr'] = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')
        self.filename =  'd_' + self.name + '_' + self.dict['datestr'] + '.json'
        with open(self.folderlog + self.filename, 'w') as writefile:
            json.dump(self.dict, writefile)
            print('dict записан: ', self.filename)
            
    def load(self, filename=None):
        if filename == None:
            files = os.listdir(self.folderlog)
            print([e for e in enumerate(files)])
            i = int(input('введите номер файла: '))
            filename = files[i]
        with open(self.folderlog + files[i], 'r') as writefile:
            self.dict = json.load(writefile)
        print(f'dict загружен :{self.folderlog + filename},\n всего\
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
   
    def print(self):
        def printdict(d):
            print('{', end='')
            for k in d.keys():
                if type(d[k]) is str:
                    print(f"'{k}': '{d[k]}',")
                else:
                    print(f"'{k}': {d[k]},")
            print('}')
            
            
        print(f'task name: {self.name}')    
        if 'links' in self.dict.keys():
            d = self.dict.copy()
            print('links len = ', len(d.pop('links')),'\n')
            printdict(d)
        else:
            printdict(self.dict)
    

