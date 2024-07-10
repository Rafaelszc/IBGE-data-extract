from controler.data_scrap import DataScrap
import pandas as pd

def main():
    data = pd.DataFrame()
    url_list = DataScrap.list_city_url('https://www.ibge.gov.br/explica/codigos-dos-municipios.php')

    for url in url_list:
        data = pd.concat([data, DataScrap.scrap_city_data(url)])

    data.to_csv('resources/output/output.csv', index=False)
    print(data.head(5))

main()