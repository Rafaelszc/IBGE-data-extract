import pandas as pd
from utils.get_response import get_response
from service.convert_to_numeric import to_numeric

class DataScrap:
    @staticmethod
    def list_city_url(url: str) -> list:
        site = get_response(url)

        table_state_list = site.find_all('tbody', attrs={'class': 'codigos-list'})[1:]
        city_url = []

        for state in table_state_list:
            city_list = state.find_all('a', attrs={'target': '_blank'}, href=True)

            for city in city_list:
                city_url.append(city['href'])
        
        return city_url

    @staticmethod
    def scrap_city_data(url: str) -> pd.DataFrame:
        site = get_response(url)

        city_code = url[-7:]

        city_name_div = site.find('div', attrs={'class': "quick-facts-titulo"})
        city_name = city_name_div.find('h1').get_text()
        print(f'Collecting {city_name} data...')

        city_data_div = site.find_all('ul', attrs={'class': "resultados-padrao"})[0]

        categories_div = city_data_div.find_all('div', attrs={'class': 'ind-label'})
        values_p = city_data_div.find_all('p', attrs={'class': 'ind-value'})

        categories = [categorie.get_text() for categorie in categories_div]

        values = [to_numeric(value.get_text()) for value in values_p]
        
        data_dict = dict(zip(categories, values))
        data = pd.DataFrame(data_dict, index=[0])
        data.insert(0, 'Nome', city_name)
        data.insert(1, 'Código', city_code)

        return data