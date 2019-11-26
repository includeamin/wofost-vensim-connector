import os
import pcse
import matplotlib as plt
import  pandas as pd

from pcse.util import WOFOST71SiteDataProvider
#from pcse.base_classes import ParameterProvider
from pcse.fileinput import YAMLAgroManagementReader
from pcse.db import NASAPowerWeatherDataProvider
from pcse.models import Wofost71_WLP_FD
from pcse.fileinput import CABOFileReader
from pcse.fileinput.cabo_weather import CABOWeatherDataProvider
from pcse.base.parameter_providers import ParameterProvider

cropd_dir = './Data/CROPD'
soil_dir = './Data/SOILD'
argo_dir = "./Data/Argo"


def cropLoader(name):
    cropFile = os.path.join(cropd_dir, name)
    print('loading crop:', name)
    cropData = CABOFileReader(cropFile)
    return cropData
def soilLoader(soilFileName):
    soildFile = os.path.join(soil_dir,soilFileName)
    print("loading soils",soilFileName)
    solidData = CABOFileReader(soildFile)
    return solidData
def siteloader(wav,co2):

    siteData=WOFOST71SiteDataProvider(WAV=wav, CO2=co2)
    return siteData

def packTheParams(cropName,soilName,siteWav,siteCo2):
    parameters = ParameterProvider(cropdata=cropLoader(cropName),soildata=soilLoader(soilName),sitedata=siteloader(siteWav,siteCo2))
    print("packing all parameters...")
    return  parameters


def agromanagementLoader(name):
    agromanagement_file = os.path.join(argo_dir, name)
    print("loading agromanagement...")
    agromanagement = YAMLAgroManagementReader(agromanagement_file)
    return agromanagement

def custom_weather_provider():
    wdp = CABOWeatherDataProvider(fname='NL2',fpath="./Data/METEO/CABOWE")
    print(wdp.export())
    print(wdp)
    return wdp

def dailyweatherobservations(lat,long):

    wdp = NASAPowerWeatherDataProvider(latitude=lat, longitude=long)
    print(wdp)
    return wdp
def modelInit(cropdName , soilName , wav , co2 , lat , long, agroName):
    wofism = Wofost71_WLP_FD(packTheParams(cropName=cropdName,soilName=soilName,siteWav=wav,siteCo2=co2)
                             ,dailyweatherobservations(lat=lat,long=long),
                             agromanagementLoader(name=agroName))
    print("model initilized")
    return wofism
def runModl(cropdName,soilName,wav,co2,lat,long,agroName,day=None):
    model = modelInit(cropdName=cropdName , soilName=soilName,wav=wav , co2=co2 ,lat=lat , long=long
                      , agroName=agroName)
    print("model running ... ")
    if day is not None:
      model.run_till_terminate()
    else:
        model.run(day)
    modelOutput = model.get_output()
    print("running finished")
    print("len of output" , len(modelOutput))
    print("saved as a CSV file")
    df = pd.DataFrame(modelOutput)
    df.to_csv("Output.csv")

    return  modelOutput

def runModlO():
    model = modelInit(cropdName="SUN1103- fc DI 75.CAB" , soilName="SR4 - Sari.NEW",wav=12 , co2=360 ,lat=36 , long=52
                      , agroName="sugarbeet_calendar.agro")
    print("model running ... ")
    model.run_till_terminate()
    modelOutput = model.get_output()
    print("running finished")
    print("len of output" , len(modelOutput))
    print("saved as a CSV file")
    df = pd.DataFrame(modelOutput)
    df.to_csv("Output.csv")
    print(modelOutput)






def main():
    runModlO()
    #wdp = NASAPowerWeatherDataProvider(latitude=52, longitude=5)
    #print(wdp)
    #pcse.test()

if __name__ == '__main__':
    dailyweatherobservations(35,53)
    custom_weather_provider()
   # main()