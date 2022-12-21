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
        pass



class HHVacancy(Vacancy):  # add counter mixin
    """ HeadHunter Vacancy """

    def __str__(self):
        return f'HH: {self.comany_name}, зарплата: {self.salary} руб/мес'



class SJVacancy(Vacancy):  # add counter mixin
    """ SuperJob Vacancy """

    def __str__(self):
        return f'SJ: {self.comany_name}, зарплата: {self.salary} руб/мес'


def sorting(vacancies):
    """ Должен сортировать любой список вакансий по ежемесячной оплате (gt, lt magic methods) """
    pass


def get_top(vacancies, top_count):
    """ Должен возвращать {top_count} записей из вакансий по зарплате (iter, next magic methods) """
    pass