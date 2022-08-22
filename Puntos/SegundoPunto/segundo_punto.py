from API import get_data, url
from punto23 import dataset_limpio
from pprint import pprint
data_violencia_intrafamiliar = get_data(url, 'Violencia Intrafamiliar')
# data_homicidio = get_data(url, 'Homicidio')
# data_hurto = get_data(url, 'Hurto')
# data_delitos_sexuales = get_data(url, 'Delitos Sexuales')


pprint(dataset_limpio(data_violencia_intrafamiliar))
