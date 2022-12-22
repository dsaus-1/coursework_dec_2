from connector import Connector
import json


class Vacancy:
    __slots__ = ('name_vacancy', 'url_vacancy', 'description_vacancy', 'salary_vacancy')

    def __init__(self, name_vacancy, url_vacancy, description_vacancy, salary_vacancy):
        self.name_vacancy = name_vacancy
        self.url_vacancy = url_vacancy
        self.description_vacancy = description_vacancy
        self.salary_vacancy = salary_vacancy

    def __str__(self):
        return f'{self.name_vacancy}\nСсылка на вакансию - {self.url_vacancy}\nОписание: {self.description_vacancy}\nЗП: {self.salary_vacancy}'

    def __repr__(self):
        return f'{self.name_vacancy}\nСсылка на вакансию - {self.url_vacancy}\nОписание: {self.description_vacancy}\nЗП: {self.salary_vacancy}'



class CountMixin:

    @property
    def get_count_of_vacancy(self):
        """
        Вернуть количество вакансий от текущего сервиса.
        Получать количество необходимо динамически из файла.
        """
        connector = Connector()
        connector.data_file = self.json_file_name
        return len(connector.read_file())



class HHVacancy(Vacancy, CountMixin):
    """ HeadHunter Vacancy """
    json_file_name = 'hh_vacancies.json'

    def __str__(self):
        return f'HH: {self.company_name}, зарплата: {self.salary} руб/мес'



class SJVacancy(Vacancy, CountMixin):
    """ SuperJob Vacancy """
    json_file_name = 'sj_vacancies.json'

    def __str__(self):
        return f'SJ: {self.company_name}, зарплата: {self.salary} руб/мес'


def sorting(vacancies):
    """ Должен сортировать любой список вакансий по ежемесячной оплате (gt, lt magic methods) """
    pass


def get_top(vacancies, top_count):
    """ Должен возвращать {top_count} записей из вакансий по зарплате (iter, next magic methods) """
    pass


s = SJVacancy(1, 2, 3, 4)
print(s.__class__.__name__)
print(s.get_count_of_vacancy)