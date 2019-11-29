import pysd
import amin
from pysd import load

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

    with open("./key_value.json", 'w') as j:
        json.dump(new_dic, j)

    result = {}
    for item in new_dic:
        with open(new_dic[item]) as lkf:
            lookup = lkf.readlines()
            lookup = [float(item) for item in lookup]
            result[item] = lookup
    return result


data = convert_vensim_keys()
for item in data:
    lookups_data[item] = data[item]

print(lookups_data)
# model = pysd.read_vensim("./Input/Data/VensimModel/Annual data.mdl")
# model = load("./Input/Data/VensimModel/Annual data.py")
# model = pysd.load('amin.py')
#
# model.run()
# print(model.components.rapeseed_tj(amin.time()+300))
# time_in_lookup_data = [i for i in range(1,365)]
# for i in range(1,365):
#     print(i)
# print(model.get_components())
# with open("./OutPut/Tj dd/Wheat/LOOKUP/series.txt") as file:
#     data = []
#     for item in file.readlines():
#         print('read',item)
#         data.append(item)
#
# print(data)
#
# model.set_components(params={"wheat tjj dd":data})
#
# # print(model.doc())
# import json
#
# with open('./OutPut/vensim_wofost_lookup.json', 'r') as j:
#     keys = json.load(j)
#
# temp = {}
# for item in keys:
#     for i in keys[item]:
#         # print(item, i, keys[item][i]['Keys']["Vensim"] ,str( keys[item][i]['LookupPath']).replace('lookup','series'))
#         temp[keys[item][i]['Keys']["Vensim"]] = str(keys[item][i]['LookupPath']).replace('lookup', 'series')
#         # for j in keys[item][i]:
#         #     print(item,i,j)
# return_columns = []
# for d in temp:
#     return_columns.append(d)
#     with open(temp[d]) as file:
#         content = file.readlines()
#         content = [float(item) for item in content]
#         print(content)
#         try:
#             model.set_components(params={d: temp[d]})
#         except:
#             print('exeption', d)
#             continue
# # return_columns.remove('Citrus Tj')
#
# stocks = model.run()
# # print(model.doc())
# # print(model.run())
# import pandas
#
# # model.set_components("")
# #
# # stocks = model.run()
#
# stocks.to_csv('temp.csv')
