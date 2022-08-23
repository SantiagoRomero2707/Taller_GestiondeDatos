from API import get_data, url
from punto23 import dataset_calculo_1, dataset_limpio, dataset_calculo_2
from pprint import pprint
data_violencia_intrafamiliar = get_data(url, 'Violencia Intrafamiliar')
# data_homicidio = get_data(url, 'Homicidio') #REVISAR HOMICIDIO
# data_hurto = get_data(url, 'Hurto')
# data_delitos_sexuales = get_data(url, 'Delitos Sexuales')


print("Violencia intrafamiliar")
dataset_final_violencia_intrafamiliar = dataset_limpio(data_violencia_intrafamiliar)
pprint(dataset_calculo_1(dataset_final_violencia_intrafamiliar))
pprint(dataset_calculo_2(dataset_final_violencia_intrafamiliar))
