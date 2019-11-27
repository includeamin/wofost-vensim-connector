from Input.Loader import Loader
from pcse.fileinput import CABOWeatherDataProvider
from pcse.base.weather import WeatherDataContainer
import json


class LookUp:
    LookupPaths: dict = {key: {} for key in
                         Loader.get_regions()}  # {key: "" for key in Loader.get_regions_variables_map().keys()}

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
        for i in input:
            lookup_body += f",({input.index(i)},{i})"
        # write lookup to file
        with open(f"{Loader.path_maps()[region][crop_name]}/LOOKUP/lookup.txt", 'w') as file:
            file.write(f"([(1,{input_min}),({len(input)},{input_max})]{lookup_body})\n")
        # create lookup map
        # print(region, crop_name)

        # lookup_map = {
        #     Loader.get_regions_variables_map()[region][crop_name]:
        #         f"{Loader.DataFolder}{Loader.path_maps()[region][crop_name]}/LOOKUP"
        # }

        # print(region, crop_name, Loader.get_regions_variables_map()[region][crop_name])
        # print(Loader.get_regions_variables_map()[region][crop_name])

        LookUp.LookupPaths[region][crop_name] = {
            "LookupPath": f"{Loader.path_maps()[region][crop_name]}/LOOKUP/lookup.txt",
            "Keys": Loader.get_regions_variables_map()[region][crop_name]
        }

        # lookup_vensim_wofost_map = {
        #
        # }

        # lookup_map = {
        #     "Region":"",
        #     ""
        # }

        # LookUp.LookupPaths[Loader.get_regions_variables_map()[region][
        #     crop_name]] = f"{Loader.DataFolder}{Loader.path_maps()[region][crop_name]}/LOOKUP"

        # return lookup_map

    @staticmethod
    def save_vensim_wofost_lookup_maps():
        with open(f'{Loader.DataFolder}vensim_wofost_lookup.json', 'w') as file:
            json.dump(LookUp.LookupPaths, file)

    @staticmethod
    def create_vensim_model():
        with open("./Input/Data/VensimModel/model.mdl") as file:
            pass

    @staticmethod
    def create_look_ups():
        paths = Loader.path_maps()
        meteo_maps = Loader.meteo_maps()
        for region in paths.keys():
            for crop in paths[region].keys():
                # get coefficient of each crop  in their region
                coefficient = Loader.get_coefficient()[crop][region]
                # get each crop rain
                rain = LookUp.get_weather_rain(meteo_maps[crop])
                # create new rain
                new_rain = [item * coefficient for item in rain]

                # init lookups

                LookUp.lookup_generator(new_rain, region, crop)

                print(paths[region][crop], coefficient, new_rain)
        LookUp.save_vensim_wofost_lookup_maps()
