from jobs_classes import *
import json

def sorting(vacancies: list):
    """ Должен сортировать любой список вакансий по ежемесячной оплате (gt, lt magic methods) """
    return sorted(vacancies, reverse=True)


def get_top(vacancies: list, top_count: int):
    """ Должен возвращать {top_count} записей из вакансий по зарплате (iter, next magic methods) """
    count = 0
    while count < top_count:
        print(vacancies[count], end= '\n\n')
        count += 1




def init_hh_vacancy_class(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as file:
        file_read = json.load(file)
        for vacancy in file_read[0]:
            url = vacancy.get('alternate_url')
            name = vacancy.get('name')
            try:
                description = vacancy['snippet'].get('requirement') + ' ' + vacancy['snippet'].get('responsibility')
            except:
                description = None
            try:
                if vacancy['salary'].get('from'):
                    salary = vacancy['salary'].get('from')
                elif vacancy['salary'].get('to'):
                    salary = vacancy['salary'].get('to')
                if vacancy['salary'].get("currency") == 'USD':
                    salary *= 72
                elif vacancy['salary'].get("currency") == 'EUR':
                    salary *= 77
                elif vacancy['salary'].get("currency") == 'KZT':
                    salary *= 0.15
            except:
                salary = 0

            try:
                company_name = vacancy['employer'].get('name')
            except:
                company_name = None
            HHVacancy.data.append(HHVacancy(name, url, description, salary, company_name))
        return HHVacancy.data

def init_sj_vacancy_class(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as file:
        file_read = json.load(file)
        for vacancy in file_read[0]:
            url = vacancy.get('link')
            name = vacancy.get('profession')
            try:
                description = vacancy.get('candidat')
            except:
                description = None
            try:
                if vacancy.get('payment_from'):
                    salary = vacancy.get('payment_from')
                elif vacancy.get('payment_to'):
                    salary = vacancy.get('payment_to')
            except:
                salary = 0

            try:
                company_name = vacancy.get('firm_name')
            except:
                company_name = None
            SJVacancy.data.append(HHVacancy(name, url, description, salary, company_name))
        return SJVacancy.data




