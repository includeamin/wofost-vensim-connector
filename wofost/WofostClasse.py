from pcse.util import WOFOST71SiteDataProvider
# from pcse.base_classes import ParameterProvider
from pcse.fileinput import YAMLAgroManagementReader
from pcse.db import NASAPowerWeatherDataProvider
from pcse.models import Wofost71_WLP_FD
from pcse.fileinput import CABOFileReader
from pcse.fileinput.cabo_weather import CABOWeatherDataProvider
from pcse.base.parameter_providers import ParameterProvider
import pandas as pd
from pcse.base import WeatherDataContainer

WeatherDataContainer.ranges = {"LAT": (-90., 90.),
                               "LON": (-180., 180.),
                               "ELEV": (-300, 6000),
                               "IRRAD": (0., 40e30),
                               "TMIN": (-50., 60.),
                               "TMAX": (-50., 60.),
                               "VAP": (0.06, 2000000.3),
                               "RAIN": (0, 25),
                               "E0": (0., 20000000.5),
                               "ES0": (0., 2000000.5),
                               "ET0": (0., 2000000.5),
                               "WIND": (0., 100.),
                               "SNOWDEPTH": (0., 250.),
                               "TEMP": (-50., 60.),
                               "TMINRA": (-50., 60.)}


class Wofost:
    def __init__(self, crop_path, argo_path, soil_path, meteo_path, meteo_name, wav, co2, region, crop_name):
        self.crop_name = crop_name
        self.crop_path = crop_path
        self.argo_path = argo_path
        self.soil_path = soil_path
        self.meteo_path = meteo_path
        # load component
        self.soil = CABOFileReader(self.soil_path)
        self.crop = CABOFileReader(self.crop_path)
        print(self.argo_path)
        self.argo = YAMLAgroManagementReader(self.argo_path)
        self.weather = CABOWeatherDataProvider(fname=meteo_name, fpath=self.meteo_path)
        self.site = WOFOST71SiteDataProvider(WAV=wav, CO2=co2)
        self.output_name = f'./OutPut/WofostOutPut/csv/{crop_name}-{region}.csv'

    def save_out_put(self, name):
        pass

    def init_model(self):
        print("packing all parameters...")

        parameters = ParameterProvider(cropdata=self.crop, soildata=self.soil,
                                       sitedata=self.site)

        print('create mode of {}')
        print(self.crop_name)
        print(self.argo_path)
        wofost = Wofost71_WLP_FD(parameters
                                 , self.weather,
                                 self.argo)

        print("runing model of {}")
        wofost.run_till_terminate()

        print("save model out put as e csv file with name of {} ")
        model_out_put = wofost.get_output()
        df = pd.DataFrame(model_out_put)
        df.to_csv(f"{self.output_name}")
        return self.output_name
