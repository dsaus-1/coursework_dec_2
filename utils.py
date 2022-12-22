import json

def filter_for_data(file_name, name, salary_from, salary_to, address, city, url, description, description_1=None, description_2=None):
    result = []
    with open(file_name, 'r', encoding='utf-8') as file:
        file_read = json.load(file)

        for vacancy in file_read[0]:
            vcnc_new = {'name': vacancy.get(name), 'url': vacancy.get(url)}

            try:
                vcnc_new['address'] = vacancy[address].get(city)
            except:
                vcnc_new['address'] = None

            if salary_from == salary_to:

                try:
                    salary_from = vacancy[salary_from].get('from')
                except:
                    salary_from = 0
                try:
                    salary_to = vacancy[salary_to].get('to')
                except:
                    salary_to = 0
                try:
                    vcnc_new['description'] = vacancy[description].get(description_1) + ' ' + vacancy[description].get(description_2)
                except:
                    vcnc_new['description'] = None

            else:
                try:
                    salary_from = vacancy[salary_from]
                except:
                    salary_from = 0
                try:
                    salary_to = vacancy[salary_to]
                except:
                    salary_to = 0
                try:
                    vcnc_new['description'] = vacancy[description]
                except:
                    vcnc_new['description'] = None

            if not salary_to:
                vcnc_new['salary'] = salary_from
            else:
                vcnc_new['salary'] = salary_to

            result.append(vcnc_new)

    with open(file_name, 'w', encoding='utf-8') as write_file:
        json.dump(result, write_file)


def init_hh_vacancy_class(file_name, class_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        file_read = json.load(file)
        if file_name == 'hh_vacancies.json':
            name = 'name'
            salary_from = 'salary'
            salary_to = 'salary'
            # address = 'address'
            # city = 'city'
            url = 'alternate_url'
            description = 'snippet'
            description_1 = 'requirement'
            description_2 = 'responsibility'
        else:
            name = 'profession'
            salary_from = 'payment_from'
            salary_to = 'payment_to'
            # address = 'address'
            # city = 'city'
            url = 'link'
            description = 'candidat'

        for vacancy in file_read[0]:

            try:
                address = vacancy[address].get(city)
            except:
                address = None
            if file_name == 'hh_vacancies.json':

                vcnc_new = {'name': vacancy.get(name), 'url': vacancy.get(url)}


#filter_for_data('sj_vacancies.json', 'profession', 'payment_from', 'payment_to', 'town', 'title', 'link', 'candidat')