from Input.input import Coefficient, CropNameMaps, MeteoNameMaps, RegionsVariablesMap, Regions, ArgoMap, SoilMap
import os
import pathlib
from shutil import copyfile
import json


class Loader:
    DataFolder = "./OutPut/"
    PathMaps: dict = {}
    Co2 = 360
    Wav = 100

    @staticmethod
    def get_crop_map(crop):
        return CropNameMaps[crop]

    # return path of crop with region name and crop name
    @staticmethod
    def get_path_with_region_crop(region, crop):
        return f"{Loader.DataFolder}{region}/{crop}"

    # get coefficients
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

    @staticmethod
    def get_soil():
        return SoilMap["Soil"]

    @staticmethod
    def get_argo_by_crop_name(crop_name):
        return ArgoMap[crop_name]

    """
    init_dirs : init directories for crops
    """

    @staticmethod
    def init_dirs():
        # create wofost output folder
        Loader.mkdir('WofostOutPut/csv')
        Loader.mkdir('WofostOutPut/map')
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

    # detect region and crop name from name of vensim output
    @staticmethod
    def detect(name: str):
        name = name.lower()
        # todo : get from input.py
        region = ["Finesk", "zr", "Tjj dd", "Tjdd", "tj"]
        region_map = {'': "Finesk", "zr": "Zarem", "tjj dd": "Tj dd", "tj": "shah R D", 'tjdd': 'Tj dd'}

        crop = ["Tomato",
                "Chickpea",
                "rapeseed",
                "Grainmaize",
                "Apple",
                "Rice",
                "Wheat",
                "Citrus",
                "Sorgum"]
        detected_crop = ''
        for item in crop:
            if name.__contains__(item.lower()):
                detected_crop = item
                break
        detected_region = ''
        for item in region:
            if name.__contains__(item.lower()):
                detected_region = item
                break
        # if detected_region == '':
        #     detected_region = 'Finesk'

        detected_region = region_map[detected_region.lower()]
        return detected_region, detected_crop

    # region, crop = detect('supply of rice zr')
