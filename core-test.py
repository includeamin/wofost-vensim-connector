import pysd
import amin
from pysd import load
from Input.input import keys_in_vensim_output
from Input.Loader import Loader

# lookups maps in the python model of vensim
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


# create vensim keys that should read series [lookup] of any crop for updating lookups in python model of vensim
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


def meteo_creator(ref_path, path, new_rain: list,coefficient):
    # wdp = CABOWeatherDataProvider(fname='SAP2', fpath="./Input/Data/CABOWE")

    with open(f"./Input/Data/CABOWE/{ref_path}") as f:
        data = f.readlines()
        start_Data_index = 0
        # data of meteo start after second ------- we should change data after (+1) index after of --------
        # the first row after ------- should not change
        for item in range(len(data)):
            if data[item].__contains__('------------------------------') and item > 0:
                start_Data_index = item
                break
        with open(path, 'w') as m:
            for i in range(start_Data_index + 2):
                m.write(data[i])
            count = 0
            for item in range(start_Data_index + 2, len(data)):
                # items splites with \t
                line_data = data[item].split("\t")
                line_data[-1] = f"{new_rain[count]/coefficient}\n"  # data
                count += 1
                # joining items with \t again
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
    counter = 0
    wofost_running_path_map = {}
    for item in model_output:
        print("-------------------------------------")
        data = model_output[item]
        data = [float(item) for item in data]
        region, crop = Loader.detect(item)
        crop = str(crop[0]).upper()+crop[1:]
        print('131',region,crop)
        coefficient = Loader.get_coefficient_depend_on_region_crop(region,crop)
        print("coefficient",coefficient)
        old_mete_name = Loader.meteo_maps()[crop]
        new_meteo_path = Loader.get_path_with_region_crop(region, crop) + "/METEO/" + old_mete_name
        print('135',item, old_mete_name, new_meteo_path)
        meteo_creator(old_mete_name, new_meteo_path, data,coefficient)
        wofost_running_path_map["crop"] = new_meteo_path
        counter +=1
        print("-------------------------------------")

    print("number of meteo created",counter)
    print("---------------------------------------------------------------------")


def running_wensim():
    import json
    from wofost.WofostClasse import Wofost
    count = 0
    runned_count = 0
    erro_count =0
    vensim_out_put_map = {}
    with open("./OutPut/vensim_wofost_lookup.json") as file:
        data = json.load(file)
        for region in data:
            for crop in data[region]:
                # print(f"{region}-{crop} create parameters")
                meteo_path = f"{Loader.DataFolder}{region}/{crop}/METEO/" #{Loader.meteo_maps()[crop]}
                crop_path = f"{Loader.DataFolder}{region}/{crop}/CROP/{Loader.get_crop_map(crop)}"
                argo_path = f"./Input/Data/Argo/{Loader.get_argo_by_crop_name(crop)}"
                soil_path = "./Input/Data/Soil/EC1.NEW"
                meteo_name = str(Loader.meteo_maps()[crop]).split('.')[0]
                # print('fsdfsef',meteo_name)
                crop_name = crop
                region_name = region
                wave = Loader.Wav
                co2 = Loader.Co2
                count += 1

                # print(meteo_path)
                # print(f"{region}-{crop} start running model")
                try:
                    output_path = Wofost(crop_path, argo_path, soil_path, meteo_path, meteo_name, wave, co2, region,
                                         crop_name).init_model()
                    vensim_out_put_map[f"{crop_name}-{region_name}"] = output_path
                    runned_count+=1

                except Exception as ex:
                    erro_count+=1
                    import traceback
                    print('171',traceback.print_exc())
                    print(crop_name,region,meteo_name,ex.args)
                    continue
                # print(f"{region}-{crop} running complete in path {output_path}")

        print("count of meteo file", count)
        print("count of success simulation", runned_count)
        print("count of errors",erro_count)



# create_meteo_for_each_crop_of_each_region()
#
model = pysd.load('amin.py')
# # return_columns=keys_in_vensim_output
stocks = model.run(return_columns=keys_in_vensim_output)
create_new_meteo(stocks)
stocks.to_csv("./OutPut/vensim_simualtion_output.csv")
running_wensim()
