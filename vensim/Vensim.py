import pysd
import json

# model = pysd.read_vensim("./Input/Data/VensimModel/Annual data.mdl")
with open("./OutPut/Tj dd/Wheat/LOOKUP/series.txt") as file:
    data = []
    for item in file.readlines():
        data.append(item)

with open('./OutPut/vensim_wofost_lookup.json','r') as j:
    keys = json.load(j)

for item in keys:
    print(keys)

# print(data)
#
# model.set_components(params={"wheat tjj dd":data})
#


# print(model.doc())
