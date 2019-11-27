from Input.input import Coefficient, CropNameMaps, MeteoNameMaps, RegionsVariablesMap, Regions
import os
import pathlib
from shutil import copyfile
import json


class Loader:
    DataFolder = "./OutPut/"
    PathMaps: dict = {}



    @staticmethod
    def get_coefficient():
        return Coefficient

    @staticmethod
    def path_maps() -> dict:
        with open(f"{Loader.DataFolder}path_maps.json", 'r') as f:
            return json.load(f)

    @staticmethod
    def meteo_maps() -> dict:
        return MeteoNameMaps

    @staticmethod
    def get_regions() -> dict:
        return Regions

    @staticmethod
    def get_regions_variables_map():
        return RegionsVariablesMap

    @staticmethod
    def mkdir(path):
        path = f"{Loader.DataFolder}{path}"
        if not os.path.exists(path):
            pathlib.Path(path).mkdir(parents=True, exist_ok=True)

    @staticmethod
    def save_path_map():
        with open(f"{Loader.DataFolder}path_maps.json", 'w') as f:
            json.dump(Loader.PathMaps, f)

    """
    init_dirs : init directories for crops
    """

    @staticmethod
    def init_dirs():
        # create regions directories
        for region in Regions:
            Loader.mkdir(region)
            Loader.PathMaps[region] = {}
        # create vensim model dir
        Loader.mkdir("VensimModel")
        # create each region's crops directories
        for crop in Coefficient.keys():
            for region in Coefficient[crop]:
                if Coefficient[crop][region] != 0:
                    # create each crops directory
                    Loader.mkdir(f"{region}/{crop}")
                    # create sub-directory of each crop
                    Loader.mkdir(f"{region}/{crop}/CROP")
                    Loader.mkdir(f"{region}/{crop}/METEO")
                    Loader.mkdir(f"{region}/{crop}/LOOKUP")
                    # Loader.mkdir(f"{region}/{crop}/VensimModel")
                    # copy data each crop Crop file
                    copyfile(f"./Input/Data/CROP/{CropNameMaps[crop]}",
                             f"{Loader.DataFolder}{region}/{crop}/CROP/{CropNameMaps[crop]}")

                    # add path to path's maps
                    Loader.PathMaps[region][crop] = f'{Loader.DataFolder}{region}/{crop}'
        # save path to json file
        Loader.save_path_map()
