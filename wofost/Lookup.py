from Input.Loader import Loader
from pcse.fileinput import CABOWeatherDataProvider
from pcse.base.weather import WeatherDataContainer
import json
import fileinput
from shutil import copyfile

import pysd


class LookUp:
    LookupPaths: dict = {key: {} for key in
                         Loader.get_regions()}  # {key: "" for key in Loader.get_regions_variables_map().keys()}
    VensimKeysMap: dict = {}

    @staticmethod
    def get_weather_rain(name, path='./Input/Data/CABOWE'):
        # load meteo file with pcse
        weather_data = CABOWeatherDataProvider(fname=name, fpath=path)
        # export
        data = weather_data.export()
        # extar
        rain = [item["RAIN"] for item in data]

        return rain

    @staticmethod
    def lookup_generator(input, region, crop_name) -> dict:
        # calculate minimum and maximum of rain
        input_min = min(input)
        input_max = max(input)
        # create body of lookup
        lookup_body = ''
        count = 1
        for i in input:
            lookup_body += f",({count},{i})"
            count+=1
        # write lookup to file
        with open(f"{Loader.path_maps()[region][crop_name]}/LOOKUP/lookup.txt", 'w') as file:
            file.write(f"[(1,{input_min}),({len(input)},{input_max})]{lookup_body}\n")
            # todo : removed ( at first of lookup and ) at end of lookup

        print(region,crop_name)
        LookUp.LookupPaths[region][crop_name] = {
            "LookupPath": f"{Loader.path_maps()[region][crop_name]}/LOOKUP/lookup.txt",
            "Keys": Loader.get_regions_variables_map()[region][crop_name]
        }

        LookUp.VensimKeysMap[Loader.get_regions_variables_map()[region][crop_name][
            "KeyInVensimModel"]] = f"{Loader.path_maps()[region][crop_name]}/LOOKUP/lookup.txt"

    @staticmethod
    def save_vensim_wofost_lookup_maps():
        with open(f'{Loader.DataFolder}vensim_wofost_lookup.json', 'w') as file:
            json.dump(LookUp.LookupPaths, file)

        with open(f'{Loader.DataFolder}keysInVensimModelMap.json', 'w') as f:
            json.dump(LookUp.VensimKeysMap, f)

    @staticmethod
    def update_mode_regex():
        import re
        with open(f'./Input/Data/VensimModel/model.mdl', encoding="utf-8") as model_file:
            content = model_file.read()
        print(len(LookUp.VensimKeysMap.keys()))
        for keys in LookUp.VensimKeysMap.keys():
            new_keys = f'<{keys}>'
            if new_keys == '<rapeseed_tjj_dd>':
                print('ija')
            pattern = re.compile(new_keys)
            with open(LookUp.VensimKeysMap[keys]) as lookup_file:
                content = re.sub(pattern, lookup_file.read(), content)

        with open(f'{Loader.DataFolder}VensimModel/model.mdl', 'w', encoding='utf-8') as temp:
            temp.write(content)


    @staticmethod
    def create_look_ups():
        paths = Loader.path_maps()
        meteo_maps = Loader.meteo_maps()
        crop_count = 0
        for region in paths.keys():
            for crop in paths[region].keys():
                crop_count +=1
                # get coefficient of each crop  in their region
                coefficient = Loader.get_coefficient()[crop][region]
                # get each crop rain
                rain = LookUp.get_weather_rain(meteo_maps[crop])
                # create new rain
                new_rain = [item * coefficient for item in rain]

                # init lookups

                LookUp.lookup_generator(new_rain, region, crop)
        print(crop_count)
        print(len(LookUp.VensimKeysMap))
                # print(paths[region][crop], coefficient, new_rain)
        # save vensim wofost and lookup map
        LookUp.save_vensim_wofost_lookup_maps()
        # create vensim model
        LookUp.update_mode_regex()
        model = pysd.read_vensim(f'{Loader.DataFolder}VensimModel/model.mdl')
        print(model.doc())
        stock = model.run()
        stock.plot()


