from pcse.base import WeatherDataContainer

from Input.Loader import Loader
from wofost.Lookup import LookUp
# import vensim.Vensim

# change ranges of pcse meteo
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

if __name__ == '__main__':
    Loader.init_dirs()
    LookUp.create_look_ups()
    # data = LookUp.get_weather_rain("SAP2", "./Input/Data/CABOWE")
    # print(data)
