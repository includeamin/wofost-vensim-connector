from pcse.base import WeatherDataContainer
from pcse.fileinput.cabo_weather import CABOWeatherDataProvider

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


def meteo_creator(name,path,new_rain):
    wdp = CABOWeatherDataProvider(fname='SAP2', fpath="./Input/Data/CABOWE")

    with open("./Input/Data/CABOWE/SAP2.014") as f:
        data = f.readlines()
        start_Data_index = 0
        final_data = ''
        for item in range(len(data)):
            if data[item].__contains__('------------------------------') and item > 0:
                start_Data_index = item
                break
        with open("SAP2.014", 'w') as m:
            for i in range(start_Data_index + 2):
                m.write(data[i])
            for item in range(start_Data_index + 2, len(data)):
                line_data = data[item].split("\t")
                line_data[-1] = "123\n"  # data
                line_data = str.join('\t', line_data)
                print(line_data)
                m.write(line_data)

        # print(start_Data_index)
    # wdp = CABOWeatherDataProvider(fname='new_meteo', fpath="./")
    print("reading")
    wdp = CABOWeatherDataProvider(fname='SAP2', fpath="./")

    print(wdp)




wdp = CABOWeatherDataProvider(fname='SAP2', fpath="./Input/Data/CABOWE")

with open("./Input/Data/CABOWE/SAP2.014") as f:
    data = f.readlines()
    start_Data_index = 0
    final_data = ''
    for item in range(len(data)):
        if data[item].__contains__('------------------------------') and item > 0:
            start_Data_index = item
            break
    with open("SAP2.014",'w') as m:
        for i in range(start_Data_index+2):
            m.write(data[i])
        for item in range(start_Data_index + 2, len(data)):
            line_data = data[item].split("\t")
            line_data[-1] = "123\n"  # data
            line_data = str.join('\t', line_data)
            print(line_data)
            m.write(line_data)


    # print(start_Data_index)
# wdp = CABOWeatherDataProvider(fname='new_meteo', fpath="./")
print("reading")
wdp = CABOWeatherDataProvider(fname='SAP2', fpath="./")

print(wdp)
