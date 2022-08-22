from sodapy import Socrata
import pandas as pd

url = {'Violencia Intrafamiliar': "vuyt-mqpw",
       'Homicidio': "ha6j-pa2r",
       'Hurto': "6sqw-8cg5",
       'Delitos Sexuales': "fpe5-yrmw"}


def get_data(directorio, name_data_set):
    client = Socrata("www.datos.gov.co", None)
    key_value_dataset = directorio.get(name_data_set)
    results = client.get(key_value_dataset, limit=5000000)
    result_df = pd.DataFrame.from_records(results)
    return result_df



