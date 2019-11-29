import pysd
import amin
from pysd import load
from Input.input import keys_in_vensim_output
from Input.Loader import Loader

lookups_data = {
    "wheat_tjj_dd": [],
    "tomato_tjj_dd": [],
    "grain_maiz_tjj_dd": [],
    "rapeseed_tjj_dd": [],
    "rice_tjj_dd": [],
    "sorgum_tjj_dd": [],  # 26
    "apple_tjj_dd": [],
    "citrud_tjj_dd": [],
    "apple_zr": [],
    "rapeseed_zr": [],
    'citrus_zr': [],
    "rice_zr": [],
    "apple_tj": [],
    "tomato_tj": [],
    "rapeseed_tj": [],
    "rice_tj": [],
    "citrs_tj": [],
    "wheat_tj": [],
    "apple": [],
    "rice": [],
    "chickpea": [],
    "citrus": [],
    "rapeseed": [],
    "grainmaize": [],
    "tomato": [],
    "wheat": []

}


def convert_vensim_keys():
    import json

    new_dic = {}
    old_meteo_path_dics = {}
    with open("./OutPut/vensim_wofost_lookup.json") as file:
        keys = json.load(file)
        count = 0
        for item in keys:
            for i in keys[item]:
                key = str(keys[item][i]['Keys']["Vensim"]).replace(" ", "_").lower()
                value = str(keys[item][i]['LookupPath']).replace('lookup', 'series')
                old_meteo_path_dics[key] = f"{Loader.DataFolder}Data/CABOWE/{Loader.meteo_maps()[i]}"
                new_dic[key] = value
                count += 1

    for item in lookups_data.keys():
        if item not in new_dic.keys():
            print(item, 'not exist')

    with open("./OutPut/key_value.json", 'w') as j:
        json.dump(new_dic, j)

    with open("./OutPut/meteo_old_map.json", 'w') as f:
        json.dump(old_meteo_path_dics, f)

    result = {}
    for item in new_dic:
        with open(new_dic[item]) as lkf:
            lookup = lkf.readlines()
            lookup = [float(item) for item in lookup]
            result[item] = lookup
    return result


def create_parameters_that_requeired_in_vensim_output():
    import json
    new_dic = []
    with open("./OutPut/vensim_wofost_lookup.json") as file:
        keys = json.load(file)
        count = 0
        for item in keys:
            for i in keys[item]:
                key = str(keys[item][i]['Keys']["Wofost"])
                new_dic.append(f'"""{key}"""')
                count += 1
    print("paramters that we want after running vensim", new_dic)
    return new_dic


def meteo_creator(ref_path, path, new_rain: list):
    # wdp = CABOWeatherDataProvider(fname='SAP2', fpath="./Input/Data/CABOWE")

    with open(f"./Input/Data/CABOWE/{ref_path}") as f:
        data = f.readlines()
        start_Data_index = 0
        for item in range(len(data)):
            if data[item].__contains__('------------------------------') and item > 0:
                start_Data_index = item
                break
        with open(path, 'w') as m:
            for i in range(start_Data_index + 2):
                m.write(data[i])
            count = 0
            for item in range(start_Data_index + 2, len(data)):
                line_data = data[item].split("\t")
                line_data[-1] = f"{new_rain[count]}\n"  # data
                count += 1
                line_data = str.join('\t', line_data)
                # print(line_data)
                m.write(line_data)

        # print(start_Data_index)
    # wdp = CABOWeatherDataProvider(fname='new_meteo', fpath="./")
    # print("reading")
    # wdp = CABOWeatherDataProvider(fname='SAP2', fpath="./")
    #
    # print(wdp)


def create_new_meteo(model_output):
    for item in model_output:
        data = model_output[item]
        data = [float(item) for item in data]
        region, crop = Loader.detect(item)
        old_mete_name = Loader.meteo_maps()[crop]
        new_meteo_path = Loader.get_path_with_region_crop(region, crop) + "/METEO/"+old_mete_name
        print(item, old_mete_name,new_meteo_path)
        meteo_creator(old_mete_name, new_meteo_path, data)


# create_meteo_for_each_crop_of_each_region()

model = pysd.load('amin.py')
# return_columns=keys_in_vensim_output
stocks = model.run(return_columns=keys_in_vensim_output)
create_new_meteo(stocks)
stocks.to_csv("./OutPut/vensim_simualtion_output.csv")
