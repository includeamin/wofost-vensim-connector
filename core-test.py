import pysd
import amin
from pysd import load
from Input.input import keys_in_vensim_output

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
    with open("./OutPut/vensim_wofost_lookup.json") as file:
        keys = json.load(file)
        count = 0
        for item in keys:
            for i in keys[item]:
                key = str(keys[item][i]['Keys']["Vensim"]).replace(" ", "_").lower()
                value = str(keys[item][i]['LookupPath']).replace('lookup', 'series')
                new_dic[key] = value
                count += 1

    for item in lookups_data.keys():
        if item not in new_dic.keys():
            print(item, 'not exist')

    with open("./OutPut/key_value.json", 'w') as j:
        json.dump(new_dic, j)

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



model = pysd.load('amin.py')

stocks = model.run(return_columns=keys_in_vensim_output)
stocks.to_csv("vensim_simualtion_output.csv")


