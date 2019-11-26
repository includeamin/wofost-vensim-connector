from Input.Loader import Loader
from pcse.fileinput import CABOWeatherDataProvider


class LookUp:
    @staticmethod
    def get_weather_et0(name,path):
        weather_data = CABOWeatherDataProvider(fname=name, fpath=path)
        data = weather_data.export()
        print(data)
        et0s = [item["ET0"] for item in data]
        return et0s
    @staticmethod
    def create_look_ups():
        paths = Loader.path_maps()
        meteo_maps = Loader.meteo_maps()
        for region in paths.keys():
            for crop in paths[region].keys():
                print(paths[region][crop])
