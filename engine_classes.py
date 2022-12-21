from abc import ABC, abstractmethod
from connector import Connector
import requests
import json


class Engine(ABC):
    key_word = 'python'
    per_page = 20
    vacancies_count = 100
    @abstractmethod
    def get_request(self):
        '''
        Реализвация взаимодействия с API (определяется в каждом классе)
        '''
        pass

    @staticmethod
    def get_connector(file_name):
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
    def attrs(self, key_word, per_page, vacancies_count):
        self.key_word = key_word
        self.per_page = per_page
        self.vacancies_count = vacancies_count


class HH(Engine):
    __url = 'https://api.hh.ru/vacancies'
    json_file_name = 'hh_vacancies.json'
    def get_request(self):
        page = 1
        result_hh = []
        while self.per_page * page < self.vacancies_count:
            response_hh = requests.get(f'{self.__url}?text={self.key_word}&page={page}')
            page += 1
            if response_hh.status_code == 200:
                json_hh = response_hh.json()
                result_hh.append(json_hh.get('items'))
        create_file = self.get_connector(self.json_file_name)
        create_file.insert(result_hh)
        return f'В файл {self.json_file_name} записано {self.vacancies_count} вакансий'

class Superjob(Engine):
    def get_request(self):
        pass


if __name__ == '__main__':
    hh_engine = HH()
    result = hh_engine.get_request()
    print(result)