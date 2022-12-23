from abc import ABC, abstractmethod
from connector import Connector
import requests



class Engine(ABC):
    key_word = 'python'
    per_page = 20
    vacancies_count = 1000
    @abstractmethod
    def get_request(self):
        '''
        Реализвация взаимодействия с API (определяется в каждом классе)
        '''
        pass

    @staticmethod
    def get_connector(file_name: str):
            '''
            Возвращает экземпляр класса Connector
            '''
            connector = Connector()
            connector.data_file = file_name
            return connector

    @property
    def attrs(self):
        return self.key_word, self.per_page, self.vacancies_count

    @attrs.setter
    def attrs(self, key_word='python', per_page=20, vacancies_count=100):
        self.key_word = key_word
        self.per_page = per_page
        self.vacancies_count = vacancies_count


    def helper_func_request(self, url: str, headers: dict, get_vacancies: str):
        '''
        Вспомогательный метод для взаимодействия с API,
        создает файл с данными по N вакансий (количество определяется параметром - vacancies_count, ключевое слово - key_word)
        '''
        page = 1
        result = []
        while self.per_page * page <= self.vacancies_count:
            response = requests.get(url=url + f'&page={page}',  headers=headers)
            page += 1
            if response.status_code == 200:
                json_file = response.json()
                result += json_file.get(get_vacancies)
        create_file = self.get_connector(self.json_file_name)
        create_file.insert(result)
        return len(result)



class HH(Engine):
    '''
    Класс дополняет функциональность родительской функции helper_func_request под
    параметры площадки hh.ru
    '''

    __url = 'https://api.hh.ru/vacancies'
    json_file_name = 'hh_vacancies.json'
    def get_request(self):
        url = f'{self.__url}?text={self.key_word}'
        headers = {}
        get_vacancies = 'items'
        return f'В файл {self.json_file_name} записано {self.helper_func_request(url, headers, get_vacancies)} вакансий'



class Superjob(Engine):
    '''
    Класс дополняет функциональность родительской функции helper_func_request под
    параметры площадки hh.ru
     '''

    __url = 'https://api.superjob.ru/2.0/vacancies'
    __key = 'v3.r.137223458.3f7c6a4606e064cca622fb48cb7d7409873dd36d.2311f33dc783df505895dfc864565a1c103f69f4'
    json_file_name = 'sj_vacancies.json'
    def get_request(self):
        url = f'{self.__url}?keyword={self.key_word}'
        headers = {'X-Api-App-Id': self.__key,
                   'Authorization': 'Bearer r.000000010000001.example.access_token',
                   'Content-Type': 'application/x-www-form-urlencoded'}
        get_vacancies = 'objects'
        return f'В файл {self.json_file_name} записано {self.helper_func_request(url, headers, get_vacancies)} вакансий'



if __name__ == '__main__':
    hh = HH()
    sj = Superjob()
    print(hh.get_request())
    print(sj.get_request())


