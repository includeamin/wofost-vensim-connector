"""
Python model "amin.py"
Translated using PySD version 0.10.0
"""
from __future__ import division
import numpy as np
from pysd import utils
import xarray as xr

from pysd.py_backend.functions import cache
from pysd.py_backend import functions
from Input.Loader import Loader

time_in_lookup_data = [i for i in range(1, 366)]


## added by includeamin to initialise lookup data
def convert_vensim_keys():
    import json
    old_meteo_path_dics = {}

    new_dic = {}
    with open("./OutPut/vensim_wofost_lookup.json") as file:
        keys = json.load(file)
        count = 0
        for item in keys:
            for i in keys[item]:
                key = str(keys[item][i]['Keys']["Vensim"]).replace(" ", "_").lower()
                value = str(keys[item][i]['LookupPath']).replace('lookup', 'series')
                new_dic[key] = value
                old_meteo_path_dics[key] = f"{Loader.DataFolder}Data/CABOWE/{Loader.meteo_maps()[i]}"

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
data = convert_vensim_keys()
for item in data:
    lookups_data[item] = data[item]

_subscript_dict = {}

_namespace = {
    'TIME': 'time',
    'Time': 'time',
    'Wr Sup befr Finesk': 'wr_sup_befr_finesk',
    'wr sup bfr Zr dam': 'wr_sup_bfr_zr_dam',
    '"sup-Wheat tjj dd"': 'supwheat_tjj_dd',
    '"sup-Citrus tjj dd"': 'supcitrus_tjj_dd',
    'Agri sup frm SW': 'agri_sup_frm_sw',
    '"Agri def aftr ab-bn sup"': 'agri_def_aftr_abbn_sup',
    '"Sup- Rice tjj dd"': 'sup_rice_tjj_dd',
    '"sup-Apple tjj dd"': 'supapple_tjj_dd',
    '"sup-Sorgum tjdd"': 'supsorgum_tjdd',
    '"Sup-grainmaize Tjdd"': 'supgrainmaize_tjdd',
    '"Sup-tomato tjdd"': 'suptomato_tjdd',
    'Agri def aftr SW sup': 'agri_def_aftr_sw_sup',
    '"sup-Rapeseed tjdd"': 'suprapeseed_tjdd',
    '"Agri sup frm Ab-bn"': 'agri_sup_frm_abbn',
    'ShRd deficit': 'shrd_deficit',
    'Zr agri deficit': 'zr_agri_deficit',
    'Finesk deficit': 'finesk_deficit',
    'supply of rice zr': 'supply_of_rice_zr',
    'supply of tomato tj': 'supply_of_tomato_tj',
    'supply of wheat': 'supply_of_wheat',
    'spply of wheat Tj': 'spply_of_wheat_tj',
    'Supply of apple zr': 'supply_of_apple_zr',
    'supply of rapeseed Tj': 'supply_of_rapeseed_tj',
    'supply of apple Tj': 'supply_of_apple_tj',
    'supply of Rice Tj': 'supply_of_rice_tj',
    'supply of citrus Tj': 'supply_of_citrus_tj',
    'supply of citrus zr': 'supply_of_citrus_zr',
    'supply of rapeseed zr': 'supply_of_rapeseed_zr',
    'supply of apple': 'supply_of_apple',
    'supply of tomato': 'supply_of_tomato',
    'supply of grainmaize': 'supply_of_grainmaize',
    'supply of chickpea': 'supply_of_chickpea',
    'supply of rice': 'supply_of_rice',
    'supply of rapeseed': 'supply_of_rapeseed',
    'supply of citrus': 'supply_of_citrus',
    'Agri Tajan Dam Coef': 'agri_tajan_dam_coef',
    'wheat tjj dd': 'wheat_tjj_dd',
    '"Ab-bn inflow"': 'abbn_inflow',
    '"Ab-bn outflow"': 'abbn_outflow',
    'citrud tjj dd': 'citrud_tjj_dd',
    'tomato tjj dd': 'tomato_tjj_dd',
    'grain maiz tjj dd': 'grain_maiz_tjj_dd',
    'Agri Dem aftr Div': 'agri_dem_aftr_div',
    'rapeseed tjj dd': 'rapeseed_tjj_dd',
    'rice tjj dd': 'rice_tjj_dd',
    'sorgum tjj dd': 'sorgum_tjj_dd',
    'apple tjj dd': 'apple_tjj_dd',
    'wr Def Tj bfr Zr': 'wr_def_tj_bfr_zr',
    'wr Dem Tj bfr Zr': 'wr_dem_tj_bfr_zr',
    'wr sup Tj bfr Zr': 'wr_sup_tj_bfr_zr',
    '"Citrus Bfr Tajan D.D"': 'citrus_bfr_tajan_dd',
    'apple zr': 'apple_zr',
    'rapeseed zr': 'rapeseed_zr',
    'zr agri dem': 'zr_agri_dem',
    'zr agri sup': 'zr_agri_sup',
    'citrus zr': 'citrus_zr',
    'Tj Agri Sup': 'tj_agri_sup',
    'Tj Total Demand': 'tj_total_demand',
    'rice zr': 'rice_zr',
    '"supply Agricul-1Finesk"': 'supply_agricul1finesk',
    'apple Tj': 'apple_tj',
    'Tj Agri Dem': 'tj_agri_dem',
    'tomato Tj': 'tomato_tj',
    'Rapeseed Tj': 'rapeseed_tj',
    'Rice Tj': 'rice_tj',
    'zr total sup': 'zr_total_sup',
    'zr total dem': 'zr_total_dem',
    'Citrs Tj': 'citrs_tj',
    'wheat Tj': 'wheat_tj',
    'Finesk Dam outflow': 'finesk_dam_outflow',
    'Agric supply after Finesk': 'agric_supply_after_finesk',
    '"Agricul-1Demand finesk"': 'agricul1demand_finesk',
    'apple': 'apple',
    'rice': 'rice',
    'chickpea': 'chickpea',
    'citrus': 'citrus',
    'rapeseed': 'rapeseed',
    'grainmaize': 'grainmaize',
    'tomato': 'tomato',
    '"mini-Sfinesk"': 'minisfinesk',
    'wheat': 'wheat',
    'Agri sup frm GW': 'agri_sup_frm_gw',
    '"Ab-bn Eva"': 'abbn_eva',
    'Tj Dom Sup': 'tj_dom_sup',
    'Zr aftr Dam': 'zr_aftr_dam',
    'Tj Evaporation': 'tj_evaporation',
    'zr agri dev sup': 'zr_agri_dev_sup',
    'Tj Ind Sup': 'tj_ind_sup',
    'Evaporation': 'evaporation',
    'ovr Reso in out system': 'ovr_reso_in_out_system',
    'zr Dim sup': 'zr_dim_sup',
    'River aftr Finesk Dam': 'river_aftr_finesk_dam',
    'Shirinrood upstream': 'shirinrood_upstream',
    '"Total Demand-1Finesk"': 'total_demand1finesk',
    'zr Ind sup': 'zr_ind_sup',
    'Zr inflow': 'zr_inflow',
    'Dom Sup after Finesk': 'dom_sup_after_finesk',
    'wr def bfr div': 'wr_def_bfr_div',
    'Env Tj sup': 'env_tj_sup',
    'Wr Dem aftr Zr Dam': 'wr_dem_aftr_zr_dam',
    'Tj aftr Div': 'tj_aftr_div',
    'wr Dem Shirinrood': 'wr_dem_shirinrood',
    'Finesk Upstream': 'finesk_upstream',
    'Inflow Finesk': 'inflow_finesk',
    'wr Sup Shirinrood': 'wr_sup_shirinrood',
    'Tajan Befr zarem': 'tajan_befr_zarem',
    'Tj Env Sup': 'tj_env_sup',
    'Tajan Dam upstream': 'tajan_dam_upstream',
    'Supply envi Finesk': 'supply_envi_finesk',
    '"Supply Domes-1Finesk"': 'supply_domes1finesk',
    'Zr evap': 'zr_evap',
    'Tj bfr Div': 'tj_bfr_div',
    'zr wr sup': 'zr_wr_sup',
    'zr Env sup': 'zr_env_sup',
    'wr sup bfr div': 'wr_sup_bfr_div',
    '"Ab-bn max vol"': 'abbn_max_vol',
    '"Ab-bn min vol"': 'abbn_min_vol',
    '"Ab-bn Spill"': 'abbn_spill',
    '"Ab-bn"': 'abbn',
    'GW Res': 'gw_res',
    'Tj Div': 'tj_div',
    'Intrfl aftr Div': 'intrfl_aftr_div',
    '"area ab-bn"': 'area_abbn',
    'Env Tj Dem': 'env_tj_dem',
    'Tj bfr Sea': 'tj_bfr_sea',
    'wr dem bfr div': 'wr_dem_bfr_div',
    '"monthly evp ab-bn"': 'monthly_evp_abbn',
    '"Tj Div aftr Ab-bn Spill"': 'tj_div_aftr_abbn_spill',
    'over Reso bfr Div': 'over_reso_bfr_div',
    'zr Env dem': 'zr_env_dem',
    'agri zr dam coef': 'agri_zr_dam_coef',
    'agri zr dev coef': 'agri_zr_dev_coef',
    'zr Ind': 'zr_ind',
    'zr max vol': 'zr_max_vol',
    'zr min vol': 'zr_min_vol',
    'Zr Spill': 'zr_spill',
    'wr Dem bfr Zr dam': 'wr_dem_bfr_zr_dam',
    'Tj aftr Zr': 'tj_aftr_zr',
    'Wr sup aftr Zr Dam': 'wr_sup_aftr_zr_dam',
    'inter aftr Zr Dam': 'inter_aftr_zr_dam',
    'zr agri dev dem': 'zr_agri_dev_dem',
    '"Zr area (km^2)"': 'zr_area_km2',
    'Zr bfr Tj': 'zr_bfr_tj',
    'zr dom dem': 'zr_dom_dem',
    'zr ele': 'zr_ele',
    'zr vol area curve': 'zr_vol_area_curve',
    'Total Inter Zr2Div': 'total_inter_zr2div',
    'zr upstream': 'zr_upstream',
    'Zr onthly evap': 'zr_onthly_evap',
    'Zr outflow': 'zr_outflow',
    'Zr reservoir': 'zr_reservoir',
    'zr vol ele curve': 'zr_vol_ele_curve',
    'wr def aftr Zr Dam': 'wr_def_aftr_zr_dam',
    'Zr wr dem': 'zr_wr_dem',
    'Zr Dam outflow': 'zr_dam_outflow',
    'Tajan Dam outflow': 'tajan_dam_outflow',
    '"Tajan Res (MCM)"': 'tajan_res_mcm',
    'Tatal Inter Tajan Dam2zarem': 'tatal_inter_tajan_dam2zarem',
    'Tj Volume area curve': 'tj_volume_area_curve',
    'Tj Env Dem': 'tj_env_dem',
    'Tj Outflow': 'tj_outflow',
    'Tj Ind Dem': 'tj_ind_dem',
    'Tj inflow': 'tj_inflow',
    'Tj max Volume': 'tj_max_volume',
    'Tj Min Volume': 'tj_min_volume',
    'Tj Monthly Evaporation': 'tj_monthly_evaporation',
    'Tj Spill': 'tj_spill',
    'Total Sup': 'total_sup',
    '"Tj Area(km^2)"': 'tj_areakm2',
    'Tj Dom Dem': 'tj_dom_dem',
    'After Finesk Interflow': 'after_finesk_interflow',
    '"Domes-1 Demad finesk"': 'domes1_demad_finesk',
    'envi Demand Finesk': 'envi_demand_finesk',
    'Finesk 0': 'finesk_0',
    'Finesk Dam': 'finesk_dam',
    '"Max-volume Finesk"': 'maxvolume_finesk',
    '"monthly evaporation -1 Finesk"': 'monthly_evaporation_1_finesk',
    '"normal evaporation -1 Finesk"': 'normal_evaporation_1_finesk',
    '"normal period -1 Finesk"': 'normal_period_1_finesk',
    'outflow Finesk': 'outflow_finesk',
    'Parvarij station': 'parvarij_station',
    'Spill Finesk': 'spill_finesk',
    '"surface -1 Finesk"': 'surface_1_finesk',
    '"surface 0-1 Finesk"': 'surface_01_finesk',
    '"volume -1 surface Look up Finesk"': 'volume_1_surface_look_up_finesk',
    'Wr Dem befr Finesk': 'wr_dem_befr_finesk',
    'FINAL TIME': 'final_time',
    'INITIAL TIME': 'initial_time',
    'SAVEPER': 'saveper',
    'TIME STEP': 'time_step'
}

__pysd_version__ = "0.10.0"

__data = {'scope': None, 'time': lambda: 0}


def _init_outer_references(data):
    for key in data:
        __data[key] = data[key]


def time():
    return __data['time']()


@cache('step')
def wr_sup_befr_finesk():
    """
    Real Name: b'Wr Sup befr Finesk'
    Original Eqn: b'MIN(Finesk Upstream (Time), Wr Dem befr Finesk (Time))'
    Units: b'MCM/Month'
    Limits: (None, None)
    Type: component

    b''
    """
    return np.minimum(finesk_upstream(time()), wr_dem_befr_finesk(time()))


@cache('step')
def wr_sup_bfr_zr_dam():
    """
    Real Name: b'wr sup bfr Zr dam'
    Original Eqn: b'MIN(zr upstream(Time), wr Dem bfr Zr dam (Time))'
    Units: b'MCM/Month'
    Limits: (None, None)
    Type: component

    b''
    """
    return np.minimum(zr_upstream(time()), wr_dem_bfr_zr_dam(time()))


@cache('step')
def supwheat_tjj_dd():
    """
    Real Name: b'"sup-Wheat tjj dd"'
    Original Eqn: b'IF THEN ELSE(wheat tjj dd(Time)<"Agri sup frm Ab-bn"-"sup-Apple tjj dd"-"sup-Citrus tjj dd"\\\\ -"Sup- Rice tjj dd"-"Sup-tomato tjdd" -"Sup-grainmaize Tjdd"-"sup-Sorgum tjdd"-"sup-Rapeseed tjdd", wheat tjj dd(Time) , 0\\\\ )'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.if_then_else(
        wheat_tjj_dd(time()) <
        agri_sup_frm_abbn() - supapple_tjj_dd() - supcitrus_tjj_dd() - sup_rice_tjj_dd() -
        suptomato_tjdd() - supgrainmaize_tjdd() - supsorgum_tjdd() - suprapeseed_tjdd(),
        wheat_tjj_dd(time()), 0)


@cache('step')
def supcitrus_tjj_dd():
    """
    Real Name: b'"sup-Citrus tjj dd"'
    Original Eqn: b'IF THEN ELSE(citrud tjj dd(Time)<"Agri sup frm Ab-bn", citrud tjj dd(Time) , 0 )'
    Units: b''
    Limits: (None, None)
    Type: component

    b'IF THEN ELSE(apple zr(Time)<zr agri sup-supply of citrus zr, apple \\n    \\t\\tzr(Time), 0)'
    """
    return functions.if_then_else(
        citrud_tjj_dd(time()) < agri_sup_frm_abbn(), citrud_tjj_dd(time()), 0)


@cache('step')
def agri_sup_frm_sw():
    """
    Real Name: b'Agri sup frm SW'
    Original Eqn: b'MIN("Agri def aftr ab-bn sup", "Tj Div aftr Ab-bn Spill")'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return np.minimum(agri_def_aftr_abbn_sup(), tj_div_aftr_abbn_spill())


@cache('step')
def agri_def_aftr_abbn_sup():
    """
    Real Name: b'"Agri def aftr ab-bn sup"'
    Original Eqn: b'"Agri sup frm Ab-bn"-Agri Dem aftr Div'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return agri_sup_frm_abbn() - agri_dem_aftr_div()


@cache('step')
def sup_rice_tjj_dd():
    """
    Real Name: b'"Sup- Rice tjj dd"'
    Original Eqn: b'IF THEN ELSE(rice tjj dd(Time)<"Agri sup frm Ab-bn"-"sup-Apple tjj dd"-"sup-Citrus tjj dd"\\\\ ,rice tjj dd(Time) , 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b'third priority'
    """
    return functions.if_then_else(
        rice_tjj_dd(time()) < agri_sup_frm_abbn() - supapple_tjj_dd() - supcitrus_tjj_dd(),
        rice_tjj_dd(time()), 0)


@cache('step')
def supapple_tjj_dd():
    """
    Real Name: b'"sup-Apple tjj dd"'
    Original Eqn: b'IF THEN ELSE(apple tjj dd(Time)<"Agri sup frm Ab-bn"-"sup-Citrus tjj dd", apple tjj dd\\\\ (Time), 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b'second priority'
    """
    return functions.if_then_else(
        apple_tjj_dd(time()) < agri_sup_frm_abbn() - supcitrus_tjj_dd(), apple_tjj_dd(time()), 0)


@cache('step')
def supsorgum_tjdd():
    """
    Real Name: b'"sup-Sorgum tjdd"'
    Original Eqn: b'IF THEN ELSE(sorgum tjj dd(Time)<"Agri sup frm Ab-bn"-"sup-Apple tjj dd"-"sup-Citrus tjj dd"\\\\ -"Sup- Rice tjj dd"-"Sup-tomato tjdd"-"Sup-grainmaize Tjdd", sorgum tjj dd(Time) , \\\\ 0)'
    Units: b'MCM/Month'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.if_then_else(
        sorgum_tjj_dd(time()) < agri_sup_frm_abbn() - supapple_tjj_dd() - supcitrus_tjj_dd() -
        sup_rice_tjj_dd() - suptomato_tjdd() - supgrainmaize_tjdd(), sorgum_tjj_dd(time()), 0)


@cache('step')
def supgrainmaize_tjdd():
    """
    Real Name: b'"Sup-grainmaize Tjdd"'
    Original Eqn: b'IF THEN ELSE(grain maiz tjj dd(Time)<"Agri sup frm Ab-bn"-"sup-Apple tjj dd"-"sup-Citrus tjj dd"\\\\ -"Sup- Rice tjj dd"-"Sup-tomato tjdd" , grain maiz tjj dd(Time) , 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b'fifth priority'
    """
    return functions.if_then_else(
        grain_maiz_tjj_dd(time()) < agri_sup_frm_abbn() - supapple_tjj_dd() - supcitrus_tjj_dd() -
        sup_rice_tjj_dd() - suptomato_tjdd(), grain_maiz_tjj_dd(time()), 0)


@cache('step')
def suptomato_tjdd():
    """
    Real Name: b'"Sup-tomato tjdd"'
    Original Eqn: b'IF THEN ELSE(tomato tjj dd(Time)<"Agri sup frm Ab-bn"-"sup-Apple tjj dd"-"sup-Citrus tjj dd"\\\\ -"Sup- Rice tjj dd", tomato tjj dd(Time) , 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b'forth priority'
    """
    return functions.if_then_else(
        tomato_tjj_dd(time()) <
        agri_sup_frm_abbn() - supapple_tjj_dd() - supcitrus_tjj_dd() - sup_rice_tjj_dd(),
        tomato_tjj_dd(time()), 0)


@cache('step')
def agri_def_aftr_sw_sup():
    """
    Real Name: b'Agri def aftr SW sup'
    Original Eqn: b'"Agri def aftr ab-bn sup"-Agri sup frm SW'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return agri_def_aftr_abbn_sup() - agri_sup_frm_sw()


@cache('step')
def suprapeseed_tjdd():
    """
    Real Name: b'"sup-Rapeseed tjdd"'
    Original Eqn: b'IF THEN ELSE(rapeseed tjj dd(Time)<"Agri sup frm Ab-bn"-"sup-Apple tjj dd"-"sup-Citrus tjj dd"\\\\ -"Sup- Rice tjj dd"-"Sup-tomato tjdd"-"Sup-grainmaize Tjdd", rapeseed tjj dd(Time) \\\\ , 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b'sixth priority'
    """
    return functions.if_then_else(
        rapeseed_tjj_dd(time()) < agri_sup_frm_abbn() - supapple_tjj_dd() - supcitrus_tjj_dd() -
        sup_rice_tjj_dd() - suptomato_tjdd() - supgrainmaize_tjdd(), rapeseed_tjj_dd(time()), 0)


@cache('step')
def agri_sup_frm_abbn():
    """
    Real Name: b'"Agri sup frm Ab-bn"'
    Original Eqn: b'MIN( "Ab-bn outflow" , Agri Dem aftr Div )'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return np.minimum(abbn_outflow(), agri_dem_aftr_div())


@cache('step')
def shrd_deficit():
    """
    Real Name: b'ShRd deficit'
    Original Eqn: b'Tj Agri Dem-Tj Agri Sup'
    Units: b'MCM'
    Limits: (None, None)
    Type: component

    b''
    """
    return tj_agri_dem() - tj_agri_sup()


@cache('step')
def zr_agri_deficit():
    """
    Real Name: b'Zr agri deficit'
    Original Eqn: b'zr agri dem-zr agri sup'
    Units: b'MCM'
    Limits: (None, None)
    Type: component

    b''
    """
    return zr_agri_dem() - zr_agri_sup()


@cache('step')
def finesk_deficit():
    """
    Real Name: b'Finesk deficit'
    Original Eqn: b'"Agricul-1Demand finesk"-"supply Agricul-1Finesk"'
    Units: b'MCM'
    Limits: (None, None)
    Type: component

    b''
    """
    return agricul1demand_finesk() - supply_agricul1finesk()


@cache('step')
def supply_of_rice_zr():
    """
    Real Name: b'supply of rice zr'
    Original Eqn: b'IF THEN ELSE(rice zr(Time)<zr agri sup-Supply of apple zr-supply of citrus zr, rice zr\\\\ (Time) , 0)'
    Units: b'MCM'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.if_then_else(
        rice_zr(time()) < zr_agri_sup() - supply_of_apple_zr() - supply_of_citrus_zr(),
        rice_zr(time()), 0)


@cache('step')
def supply_of_tomato_tj():
    """
    Real Name: b'supply of tomato tj'
    Original Eqn: b'IF THEN ELSE( tomato Tj(Time)<Tj Agri Sup-supply of Rice Tj-supply of apple Tj-supply of citrus Tj\\\\ , tomato Tj(Time) , 0 )'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.if_then_else(
        tomato_tj(time()) <
        tj_agri_sup() - supply_of_rice_tj() - supply_of_apple_tj() - supply_of_citrus_tj(),
        tomato_tj(time()), 0)


@cache('step')
def supply_of_wheat():
    """
    Real Name: b'supply of wheat'
    Original Eqn: b'IF THEN ELSE(wheat(Time)<"supply Agricul-1Finesk"-supply of apple-supply of rice-supply of chickpea\\\\ -supply of citrus-supply of grainmaize-supply of rapeseed-supply of tomato, wheat(Time\\\\ ) , 0 )'
    Units: b'MCM'
    Limits: (None, None)
    Type: component

    b'third priority'
    """
    return functions.if_then_else(
        wheat(time()) <
        supply_agricul1finesk() - supply_of_apple() - supply_of_rice() - supply_of_chickpea() -
        supply_of_citrus() - supply_of_grainmaize() - supply_of_rapeseed() - supply_of_tomato(),
        wheat(time()), 0)


@cache('step')
def spply_of_wheat_tj():
    """
    Real Name: b'spply of wheat Tj'
    Original Eqn: b'IF THEN ELSE( wheat Tj(Time)<Tj Agri Sup-supply of apple Tj-supply of Rice Tj-supply of citrus Tj\\\\ -supply of tomato tj-supply of rapeseed Tj , wheat Tj(Time) , 0 )'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.if_then_else(
        wheat_tj(time()) < tj_agri_sup() - supply_of_apple_tj() - supply_of_rice_tj() -
        supply_of_citrus_tj() - supply_of_tomato_tj() - supply_of_rapeseed_tj(), wheat_tj(time()),
        0)


@cache('step')
def supply_of_apple_zr():
    """
    Real Name: b'Supply of apple zr'
    Original Eqn: b'IF THEN ELSE(apple zr(Time)<zr agri sup-supply of citrus zr, apple zr(Time), 0)'
    Units: b'MCM'
    Limits: (None, None)
    Type: component

    b'first priotiry'
    """
    return functions.if_then_else(
        apple_zr(time()) < zr_agri_sup() - supply_of_citrus_zr(), apple_zr(time()), 0)


@cache('step')
def supply_of_rapeseed_tj():
    """
    Real Name: b'supply of rapeseed Tj'
    Original Eqn: b'IF THEN ELSE(Rapeseed Tj(Time)<Tj Agri Sup-supply of Rice Tj-supply of apple Tj-supply of citrus Tj\\\\ -supply of tomato tj, Rapeseed Tj(Time) , 0 )'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.if_then_else(
        rapeseed_tj(time()) < tj_agri_sup() - supply_of_rice_tj() - supply_of_apple_tj() -
        supply_of_citrus_tj() - supply_of_tomato_tj(), rapeseed_tj(time()), 0)


@cache('step')
def supply_of_apple_tj():
    """
    Real Name: b'supply of apple Tj'
    Original Eqn: b'IF THEN ELSE( Tj Agri Sup-supply of citrus Tj>apple Tj(Time), apple Tj(Time) , 0 )'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.if_then_else(tj_agri_sup() - supply_of_citrus_tj() > apple_tj(time()),
                                  apple_tj(time()), 0)


@cache('step')
def supply_of_rice_tj():
    """
    Real Name: b'supply of Rice Tj'
    Original Eqn: b'IF THEN ELSE(Rice Tj(Time)<Tj Agri Sup-supply of apple Tj-supply of citrus Tj, Rice Tj\\\\ (Time), 0 )'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.if_then_else(
        rice_tj(time()) < tj_agri_sup() - supply_of_apple_tj() - supply_of_citrus_tj(),
        rice_tj(time()), 0)


@cache('step')
def supply_of_citrus_tj():
    """
    Real Name: b'supply of citrus Tj'
    Original Eqn: b'IF THEN ELSE(Citrs Tj(Time)<Tj Agri Sup, Citrs Tj(Time) , 0 )'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.if_then_else(citrs_tj(time()) < tj_agri_sup(), citrs_tj(time()), 0)


@cache('step')
def supply_of_citrus_zr():
    """
    Real Name: b'supply of citrus zr'
    Original Eqn: b'IF THEN ELSE(citrus zr(Time)<zr agri sup, citrus zr(Time) , 0 )'
    Units: b'MCM'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.if_then_else(citrus_zr(time()) < zr_agri_sup(), citrus_zr(time()), 0)


@cache('step')
def supply_of_rapeseed_zr():
    """
    Real Name: b'supply of rapeseed zr'
    Original Eqn: b'IF THEN ELSE(rapeseed zr(Time)<zr agri sup-Supply of apple zr-supply of citrus zr-supply of rice zr\\\\ , rapeseed zr(Time) , 0)'
    Units: b'MCM'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.if_then_else(
        rapeseed_zr(time()) <
        zr_agri_sup() - supply_of_apple_zr() - supply_of_citrus_zr() - supply_of_rice_zr(),
        rapeseed_zr(time()), 0)


@cache('step')
def supply_of_apple():
    """
    Real Name: b'supply of apple'
    Original Eqn: b'IF THEN ELSE(apple(Time)< "supply Agricul-1Finesk"-supply of citrus,apple(Time) , 0 \\\\ )'
    Units: b'MCM'
    Limits: (None, None)
    Type: component

    b'second priority'
    """
    return functions.if_then_else(
        apple(time()) < supply_agricul1finesk() - supply_of_citrus(), apple(time()), 0)


@cache('step')
def supply_of_tomato():
    """
    Real Name: b'supply of tomato'
    Original Eqn: b'IF THEN ELSE(tomato(Time)<"supply Agricul-1Finesk"-supply of apple-supply of rice-supply of citrus\\\\ ,tomato (Time), 0 )'
    Units: b'MCM'
    Limits: (None, None)
    Type: component

    b'fifth priority'
    """
    return functions.if_then_else(
        tomato(time()) <
        supply_agricul1finesk() - supply_of_apple() - supply_of_rice() - supply_of_citrus(),
        tomato(time()), 0)


@cache('step')
def supply_of_grainmaize():
    """
    Real Name: b'supply of grainmaize'
    Original Eqn: b'IF THEN ELSE(grainmaize(Time)<"supply Agricul-1Finesk"-supply of apple-supply of rice\\\\ -supply of citrus- supply of tomato, grainmaize(Time) , 0 )'
    Units: b'MCM'
    Limits: (None, None)
    Type: component

    b'eightth priority'
    """
    return functions.if_then_else(
        grainmaize(time()) < supply_agricul1finesk() - supply_of_apple() - supply_of_rice() -
        supply_of_citrus() - supply_of_tomato(), grainmaize(time()), 0)


@cache('step')
def supply_of_chickpea():
    """
    Real Name: b'supply of chickpea'
    Original Eqn: b'IF THEN ELSE(chickpea(Time)<"supply Agricul-1Finesk"-supply of apple-supply of rice-\\\\ supply of citrus-supply of tomato-supply of grainmaize , chickpea(Time) , 0 )'
    Units: b'MCM'
    Limits: (None, None)
    Type: component

    b'seventh priority'
    """
    return functions.if_then_else(
        chickpea(time()) < supply_agricul1finesk() - supply_of_apple() - supply_of_rice() -
        supply_of_citrus() - supply_of_tomato() - supply_of_grainmaize(), chickpea(time()), 0)


@cache('step')
def supply_of_rice():
    """
    Real Name: b'supply of rice'
    Original Eqn: b'IF THEN ELSE(rice(Time)<"supply Agricul-1Finesk"-supply of apple-supply of citrus, rice\\\\ (Time) , 0 )'
    Units: b'MCM'
    Limits: (None, None)
    Type: component

    b'second priority'
    """
    return functions.if_then_else(
        rice(time()) < supply_agricul1finesk() - supply_of_apple() - supply_of_citrus(),
        rice(time()), 0)


@cache('step')
def supply_of_rapeseed():
    """
    Real Name: b'supply of rapeseed'
    Original Eqn: b'IF THEN ELSE(rapeseed(Time)<"supply Agricul-1Finesk"-supply of apple-supply of rice-\\\\ supply of citrus-supply of tomato-supply of grainmaize-supply of rice, rapeseed(Time\\\\ ) , 0 )'
    Units: b'MCM'
    Limits: (None, None)
    Type: component

    b'sixth priority'
    """
    return functions.if_then_else(
        rapeseed(time()) < supply_agricul1finesk() - supply_of_apple() - supply_of_rice() -
        supply_of_citrus() - supply_of_tomato() - supply_of_grainmaize() - supply_of_rice(),
        rapeseed(time()), 0)


@cache('step')
def supply_of_citrus():
    """
    Real Name: b'supply of citrus'
    Original Eqn: b'IF THEN ELSE(citrus(Time)<"Supply Domes-1Finesk", citrus(Time) , 0 )'
    Units: b'MCM'
    Limits: (None, None)
    Type: component

    b'first priority'
    """
    return functions.if_then_else(citrus(time()) < supply_domes1finesk(), citrus(time()), 0)


@cache('run')
def agri_tajan_dam_coef():
    """
    Real Name: b'Agri Tajan Dam Coef'
    Original Eqn: b'0.9'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.9


def wheat_tjj_dd(x):
    """
    Real Name: b'wheat tjj dd'
    Original Eqn: b'( [(1,0)-(365,0.4)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0\\\\ ),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23,\\\\ 0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35\\\\ ,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47\\\\ ,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94,0),(95\\\\ ,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105,0),(106\\\\ ,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0),(116,0)\\\\ ,(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126,0),(127\\\\ ,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0),(137,0)\\\\ ,(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147,0),(148\\\\ ,0),(149,0),(150,0),(151,0),(152,0),(153,0),(154,0),(155,0),(156,0),(157,0),(158,0)\\\\ ,(159,0),(160,0),(161,0),(162,0),(163,0),(164,0),(165,0),(166,0),(167,0),(168,0),(169\\\\ ,0),(170,0),(171,0),(172,0),(173,0),(174,0),(175,0),(176,0),(177,0),(178,0),(179,0)\\\\ ,(180,0),(181,0.33945),(182,0.33945),(183,0.33945),(184,0.33945),(185,0.33945),(186\\\\ ,0.33945),(187,0.33945),(188,0.33945),(189,0.33945),(190,0.33945),(191,0.33945),(192\\\\ ,0.33945),(193,0.33945),(194,0.33945),(195,0.33945),(196,0.33945),(197,0.33945),(198\\\\ ,0.33945),(199,0.33945),(200,0.33945),(201,0.33945),(202,0.33945),(203,0.33945),(204\\\\ ,0.33945),(205,0.33945),(206,0.33945),(207,0.33945),(208,0.33945),(209,0.33945),(210\\\\ ,0.33945),(211,0.1115),(212,0.1115),(213,0.1115),(214,0.1115),(215,0.1115),(216,0.1115\\\\ ),(217,0.1115),(218,0.1115),(219,0.1115),(220,0.1115),(221,0.1115),(222,0.1115),(223\\\\ ,0.1115),(224,0.1115),(225,0.1115),(226,0.1115),(227,0.1115),(228,0.1115),(229,0.1115\\\\ ),(230,0.1115),(231,0.1115),(232,0.1115),(233,0.1115),(234,0.1115),(235,0.1115),(236\\\\ ,0.1115),(237,0.1115),(238,0.1115),(239,0.1115),(240,0.1115),(241,0.02171),(242,0.02171\\\\ ),(243,0.02171),(244,0.02171),(245,0.02171),(246,0.02171),(247,0.02171),(248,0.02171\\\\ ),(249,0.02171),(250,0.02171),(251,0.02171),(252,0.02171),(253,0.02171),(254,0.02171\\\\ ),(255,0.02171),(256,0.02171),(257,0.02171),(258,0.02171),(259,0.02171),(260,0.02171\\\\ ),(261,0.02171),(262,0.02171),(263,0.02171),(264,0.02171),(265,0.02171),(266,0.02171\\\\ ),(267,0.02171),(268,0.02171),(269,0.02171),(270,0.02171),(271,0),(272,0),(273,0),(\\\\ 274,0),(275,0),(276,0),(277,0),(278,0),(279,0),(280,0),(281,0),(282,0),(283,0),(284\\\\ ,0),(285,0),(286,0),(287,0),(288,0),(289,0),(290,0),(291,0),(292,0),(293,0),(294,0)\\\\ ,(295,0),(296,0),(297,0),(298,0),(299,0),(300,0),(301,0),(302,0),(303,0),(304,0),(305\\\\ ,0),(306,0),(307,0),(308,0),(309,0),(310,0),(311,0),(312,0),(313,0),(314,0),(315,0)\\\\ ,(316,0),(317,0),(318,0),(319,0),(320,0),(321,0),(322,0),(323,0),(324,0),(325,0),(326\\\\ ,0),(327,0),(328,0),(329,0),(330,0),(331,0),(332,0),(333,0),(334,0),(335,0),(336,0)\\\\ ,(337,0),(338,0),(339,0),(340,0),(341,0),(342,0),(343,0),(344,0),(345,0),(346,0),(347\\\\ ,0),(348,0),(349,0),(350,0),(351,0),(352,0),(353,0),(354,0),(355,0),(356,0),(357,0)\\\\ ,(358,0),(359,0),(360,0),(361,0),(362,0),(363,0),(364,0),(365,0))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b'forth priority'
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], lookups_data["wheat_tjj_dd"]
                            # [
                            #
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0.33945, 0.33945, 0.33945, 0.33945, 0.33945, 0.33945, 0.33945, 0.33945, 0.33945,
                            #     0.33945,
                            #     0.33945, 0.33945, 0.33945, 0.33945, 0.33945, 0.33945, 0.33945, 0.33945, 0.33945,
                            #     0.33945,
                            #     0.33945, 0.33945, 0.33945, 0.33945, 0.33945, 0.33945, 0.33945, 0.33945, 0.33945,
                            #     0.33945,
                            #     0.1115, 0.1115, 0.1115, 0.1115, 0.1115, 0.1115, 0.1115, 0.1115, 0.1115, 0.1115, 0.1115,
                            #     0.1115, 0.1115, 0.1115, 0.1115, 0.1115, 0.1115, 0.1115, 0.1115, 0.1115, 0.1115, 0.1115,
                            #     0.1115, 0.1115, 0.1115, 0.1115, 0.1115, 0.1115, 0.1115, 0.1115, 0.02171, 0.02171,
                            #     0.02171,
                            #     0.02171, 0.02171, 0.02171, 0.02171, 0.02171, 0.02171, 0.02171, 0.02171, 0.02171,
                            #     0.02171,
                            #     0.02171, 0.02171, 0.02171, 0.02171, 0.02171, 0.02171, 0.02171, 0.02171, 0.02171,
                            #     0.02171,
                            #     0.02171, 0.02171, 0.02171, 0.02171, 0.02171, 0.02171, 0.02171, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                            # ]
                            )


@cache('step')
def abbn_inflow():
    """
    Real Name: b'"Ab-bn inflow"'
    Original Eqn: b'IF THEN ELSE(Agri Dem aftr Div >=Tj aftr Div,0,Tj aftr Div-Agri Dem aftr Div )'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.if_then_else(agri_dem_aftr_div() >= tj_aftr_div(), 0,
                                  tj_aftr_div() - agri_dem_aftr_div())


@cache('step')
def abbn_outflow():
    """
    Real Name: b'"Ab-bn outflow"'
    Original Eqn: b'IF THEN ELSE("Ab-bn"-"Ab-bn min vol"+"Ab-bn inflow"-"Ab-bn Eva">=Agri Dem aftr Div ,\\\\ Agri Dem aftr Div , Max (0, "Ab-bn"-"Ab-bn min vol"+"Ab-bn inflow"-"Ab-bn Eva" ) )'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.if_then_else(
        abbn() - abbn_min_vol() + abbn_inflow() - abbn_eva() >= agri_dem_aftr_div(),
        agri_dem_aftr_div(), np.maximum(0,
                                        abbn() - abbn_min_vol() + abbn_inflow() - abbn_eva()))


def citrud_tjj_dd(x):
    """
    Real Name: b'citrud tjj dd'
    Original Eqn: b'( [(1,0)-(12,40)],(1,1.28628),(2,0),(3,0),(4,0),(5,0),(6,0),(7,31.6279),(8,13.9557),(9\\\\ ,15.9835),(10,16.4319),(11,13.5213),(12,8.76044))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b'second priority'
    """
    return functions.lookup(
        x, time_in_lookup_data,
        lookups_data["citrud_tjj_dd"]
        # [1.28628, 0, 0, 0, 0, 0, 31.6279, 13.9557, 15.9835, 16.4319, 13.5213, 8.76044]
    )


def tomato_tjj_dd(x):
    """
    Real Name: b'tomato tjj dd'
    Original Eqn: b'( [(1,0)-(365,0.001)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11\\\\ ,0),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23\\\\ ,0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35\\\\ ,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47\\\\ ,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94,0),(95\\\\ ,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105,0),(106\\\\ ,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0),(116,0)\\\\ ,(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126,0),(127\\\\ ,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0),(137,0)\\\\ ,(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147,0),(148\\\\ ,0),(149,0),(150,0),(151,0),(152,0),(153,0),(154,0),(155,0),(156,0),(157,0),(158,0)\\\\ ,(159,0),(160,0),(161,0),(162,0),(163,0),(164,0),(165,0),(166,0),(167,0),(168,0),(169\\\\ ,0),(170,0),(171,0),(172,0),(173,0),(174,0),(175,0),(176,0),(177,0),(178,0),(179,0)\\\\ ,(180,0),(181,0),(182,0),(183,0),(184,0),(185,0),(186,0),(187,0),(188,0),(189,0),(190\\\\ ,0),(191,0),(192,0),(193,0),(194,0),(195,0),(196,0),(197,0),(198,0),(199,0),(200,0)\\\\ ,(201,0),(202,0),(203,0),(204,0),(205,0),(206,0),(207,0),(208,0),(209,0),(210,0),(211\\\\ ,0.00019),(212,0.00019),(213,0.00019),(214,0.00019),(215,0.00019),(216,0.00019),(217\\\\ ,0.00019),(218,0.00019),(219,0.00019),(220,0.00019),(221,0.00019),(222,0.00019),(223\\\\ ,0.00019),(224,0.00019),(225,0.00019),(226,0.00019),(227,0.00019),(228,0.00019),(229\\\\ ,0.00019),(230,0.00019),(231,0.00019),(232,0.00019),(233,0.00019),(234,0.00019),(235\\\\ ,0.00019),(236,0.00019),(237,0.00019),(238,0.00019),(239,0.00019),(240,0.00019),(241\\\\ ,0.00051),(242,0.00051),(243,0.00051),(244,0.00051),(245,0.00051),(246,0.00051),(247\\\\ ,0.00051),(248,0.00051),(249,0.00051),(250,0.00051),(251,0.00051),(252,0.00051),(253\\\\ ,0.00051),(254,0.00051),(255,0.00051),(256,0.00051),(257,0.00051),(258,0.00051),(259\\\\ ,0.00051),(260,0.00051),(261,0.00051),(262,0.00051),(263,0.00051),(264,0.00051),(265\\\\ ,0.00051),(266,0.00051),(267,0.00051),(268,0.00051),(269,0.00051),(270,0.00051),(271\\\\ ,0.00099),(272,0.00099),(273,0.00099),(274,0.00099),(275,0.00099),(276,0.00099),(277\\\\ ,0.00099),(278,0.00099),(279,0.00099),(280,0.00099),(281,0.00099),(282,0.00099),(283\\\\ ,0.00099),(284,0.00099),(285,0.00099),(286,0.00099),(287,0.00099),(288,0.00099),(289\\\\ ,0.00099),(290,0.00099),(291,0.00099),(292,0.00099),(293,0.00099),(294,0.00099),(295\\\\ ,0.00099),(296,0.00099),(297,0.00099),(298,0.00099),(299,0.00099),(300,0.00099),(301\\\\ ,0.00097),(302,0.00097),(303,0.00097),(304,0.00097),(305,0.00097),(306,0.00097),(307\\\\ ,0.00097),(308,0.00097),(309,0.00097),(310,0.00097),(311,0.00097),(312,0.00097),(313\\\\ ,0.00097),(314,0.00097),(315,0.00097),(316,0.00097),(317,0.00097),(318,0.00097),(319\\\\ ,0.00097),(320,0.00097),(321,0.00097),(322,0.00097),(323,0.00097),(324,0.00097),(325\\\\ ,0.00097),(326,0.00097),(327,0.00097),(328,0.00097),(329,0.00097),(330,0.00097),(331\\\\ ,0.00063),(332,0.00063),(333,0.00063),(334,0.00063),(335,0.00063),(336,0.00063),(337\\\\ ,0.00063),(338,0.00063),(339,0.00063),(340,0.00063),(341,0.00063),(342,0.00063),(343\\\\ ,0.00063),(344,0.00063),(345,0.00063),(346,0.00063),(347,0.00063),(348,0.00063),(349\\\\ ,0.00063),(350,0.00063),(351,0.00063),(352,0.00063),(353,0.00063),(354,0.00063),(355\\\\ ,0.00063),(356,0.00063),(357,0.00063),(358,0.00063),(359,0.00063),(360,0.00063),(361\\\\ ,0.00063),(362,0.00063),(363,0.00063),(364,0.00063),(365,0.00063))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], lookups_data["tomato_tjj_dd"]
                            # [
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0.00019, 0.00019, 0.00019, 0.00019, 0.00019, 0.00019, 0.00019, 0.00019, 0.00019,
                            #     0.00019,
                            #     0.00019, 0.00019, 0.00019, 0.00019, 0.00019, 0.00019, 0.00019, 0.00019, 0.00019,
                            #     0.00019,
                            #     0.00019, 0.00019, 0.00019, 0.00019, 0.00019, 0.00019, 0.00019, 0.00019, 0.00019,
                            #     0.00019,
                            #     0.00051, 0.00051, 0.00051, 0.00051, 0.00051, 0.00051, 0.00051, 0.00051, 0.00051,
                            #     0.00051,
                            #     0.00051, 0.00051, 0.00051, 0.00051, 0.00051, 0.00051, 0.00051, 0.00051, 0.00051,
                            #     0.00051,
                            #     0.00051, 0.00051, 0.00051, 0.00051, 0.00051, 0.00051, 0.00051, 0.00051, 0.00051,
                            #     0.00051,
                            #     0.00099, 0.00099, 0.00099, 0.00099, 0.00099, 0.00099, 0.00099, 0.00099, 0.00099,
                            #     0.00099,
                            #     0.00099, 0.00099, 0.00099, 0.00099, 0.00099, 0.00099, 0.00099, 0.00099, 0.00099,
                            #     0.00099,
                            #     0.00099, 0.00099, 0.00099, 0.00099, 0.00099, 0.00099, 0.00099, 0.00099, 0.00099,
                            #     0.00099,
                            #     0.00097, 0.00097, 0.00097, 0.00097, 0.00097, 0.00097, 0.00097, 0.00097, 0.00097,
                            #     0.00097,
                            #     0.00097, 0.00097, 0.00097, 0.00097, 0.00097, 0.00097, 0.00097, 0.00097, 0.00097,
                            #     0.00097,
                            #     0.00097, 0.00097, 0.00097, 0.00097, 0.00097, 0.00097, 0.00097, 0.00097, 0.00097,
                            #     0.00097,
                            #     0.00063, 0.00063, 0.00063, 0.00063, 0.00063, 0.00063, 0.00063, 0.00063, 0.00063,
                            #     0.00063,
                            #     0.00063, 0.00063, 0.00063, 0.00063, 0.00063, 0.00063, 0.00063, 0.00063, 0.00063,
                            #     0.00063,
                            #     0.00063, 0.00063, 0.00063, 0.00063, 0.00063, 0.00063, 0.00063, 0.00063, 0.00063,
                            #     0.00063,
                            #     0.00063, 0.00063, 0.00063, 0.00063, 0.00063
                            # ]
                            )


def grain_maiz_tjj_dd(x):
    """
    Real Name: b'grain maiz tjj dd'
    Original Eqn: b'( [(1,0)-(365,0.2)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0\\\\ ),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23,\\\\ 0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35\\\\ ,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47\\\\ ,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94,0),(95\\\\ ,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105,0),(106\\\\ ,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0),(116,0)\\\\ ,(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126,0),(127\\\\ ,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0),(137,0)\\\\ ,(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147,0),(148\\\\ ,0),(149,0),(150,0),(151,0),(152,0),(153,0),(154,0),(155,0),(156,0),(157,0),(158,0)\\\\ ,(159,0),(160,0),(161,0),(162,0),(163,0),(164,0),(165,0),(166,0),(167,0),(168,0),(169\\\\ ,0),(170,0),(171,0),(172,0),(173,0),(174,0),(175,0),(176,0),(177,0),(178,0),(179,0)\\\\ ,(180,0),(181,0),(182,0),(183,0),(184,0),(185,0),(186,0),(187,0),(188,0),(189,0),(190\\\\ ,0),(191,0),(192,0),(193,0),(194,0),(195,0),(196,0),(197,0),(198,0),(199,0),(200,0)\\\\ ,(201,0),(202,0),(203,0),(204,0),(205,0),(206,0),(207,0),(208,0),(209,0),(210,0),(211\\\\ ,0),(212,0),(213,0),(214,0),(215,0),(216,0),(217,0),(218,0),(219,0),(220,0),(221,0)\\\\ ,(222,0),(223,0),(224,0),(225,0),(226,0),(227,0),(228,0),(229,0),(230,0),(231,0),(232\\\\ ,0),(233,0),(234,0),(235,0),(236,0),(237,0),(238,0),(239,0),(240,0),(241,0.03701),(\\\\ 242,0.03701),(243,0.03701),(244,0.03701),(245,0.03701),(246,0.03701),(247,0.03701),\\\\ (248,0.03701),(249,0.03701),(250,0.03701),(251,0.03701),(252,0.03701),(253,0.03701)\\\\ ,(254,0.03701),(255,0.03701),(256,0.03701),(257,0.03701),(258,0.03701),(259,0.03701\\\\ ),(260,0.03701),(261,0.03701),(262,0.03701),(263,0.03701),(264,0.03701),(265,0.03701\\\\ ),(266,0.03701),(267,0.03701),(268,0.03701),(269,0.03701),(270,0.03701),(271,0.04925\\\\ ),(272,0.04925),(273,0.04925),(274,0.04925),(275,0.04925),(276,0.04925),(277,0.04925\\\\ ),(278,0.04925),(279,0.04925),(280,0.04925),(281,0.04925),(282,0.04925),(283,0.04925\\\\ ),(284,0.04925),(285,0.04925),(286,0.04925),(287,0.04925),(288,0.04925),(289,0.04925\\\\ ),(290,0.04925),(291,0.04925),(292,0.04925),(293,0.04925),(294,0.04925),(295,0.04925\\\\ ),(296,0.04925),(297,0.04925),(298,0.04925),(299,0.04925),(300,0.04925),(301,0.14454\\\\ ),(302,0.14454),(303,0.14454),(304,0.14454),(305,0.14454),(306,0.14454),(307,0.14454\\\\ ),(308,0.14454),(309,0.14454),(310,0.14454),(311,0.14454),(312,0.14454),(313,0.14454\\\\ ),(314,0.14454),(315,0.14454),(316,0.14454),(317,0.14454),(318,0.14454),(319,0.14454\\\\ ),(320,0.14454),(321,0.14454),(322,0.14454),(323,0.14454),(324,0.14454),(325,0.14454\\\\ ),(326,0.14454),(327,0.14454),(328,0.14454),(329,0.14454),(330,0.14454),(331,0.05342\\\\ ),(332,0.05342),(333,0.05342),(334,0.05342),(335,0.05342),(336,0.05342),(337,0.05342\\\\ ),(338,0.05342),(339,0.05342),(340,0.05342),(341,0.05342),(342,0.05342),(343,0.05342\\\\ ),(344,0.05342),(345,0.05342),(346,0.05342),(347,0.05342),(348,0.05342),(349,0.05342\\\\ ),(350,0.05342),(351,0.05342),(352,0.05342),(353,0.05342),(354,0.05342),(355,0.05342\\\\ ),(356,0.05342),(357,0.05342),(358,0.05342),(359,0.05342),(360,0.05342),(361,0.05342\\\\ ),(362,0.05342),(363,0.05342),(364,0.05342),(365,0.05342))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], lookups_data["grain_maiz_tjj_dd"]
                            # [
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0.03701, 0.03701, 0.03701, 0.03701, 0.03701, 0.03701, 0.03701, 0.03701, 0.03701,
                            #     0.03701,
                            #     0.03701, 0.03701, 0.03701, 0.03701, 0.03701, 0.03701, 0.03701, 0.03701, 0.03701,
                            #     0.03701,
                            #     0.03701, 0.03701, 0.03701, 0.03701, 0.03701, 0.03701, 0.03701, 0.03701, 0.03701,
                            #     0.03701,
                            #     0.04925, 0.04925, 0.04925, 0.04925, 0.04925, 0.04925, 0.04925, 0.04925, 0.04925,
                            #     0.04925,
                            #     0.04925, 0.04925, 0.04925, 0.04925, 0.04925, 0.04925, 0.04925, 0.04925, 0.04925,
                            #     0.04925,
                            #     0.04925, 0.04925, 0.04925, 0.04925, 0.04925, 0.04925, 0.04925, 0.04925, 0.04925,
                            #     0.04925,
                            #     0.14454, 0.14454, 0.14454, 0.14454, 0.14454, 0.14454, 0.14454, 0.14454, 0.14454,
                            #     0.14454,
                            #     0.14454, 0.14454, 0.14454, 0.14454, 0.14454, 0.14454, 0.14454, 0.14454, 0.14454,
                            #     0.14454,
                            #     0.14454, 0.14454, 0.14454, 0.14454, 0.14454, 0.14454, 0.14454, 0.14454, 0.14454,
                            #     0.14454,
                            #     0.05342, 0.05342, 0.05342, 0.05342, 0.05342, 0.05342, 0.05342, 0.05342, 0.05342,
                            #     0.05342,
                            #     0.05342, 0.05342, 0.05342, 0.05342, 0.05342, 0.05342, 0.05342, 0.05342, 0.05342,
                            #     0.05342,
                            #     0.05342, 0.05342, 0.05342, 0.05342, 0.05342, 0.05342, 0.05342, 0.05342, 0.05342,
                            #     0.05342,
                            #     0.05342, 0.05342, 0.05342, 0.05342, 0.05342
                            # ]
                            )


@cache('step')
def agri_dem_aftr_div():
    """
    Real Name: b'Agri Dem aftr Div'
    Original Eqn: b'apple tjj dd(Time)+citrud tjj dd(Time)+grain maiz tjj dd(Time)+rapeseed tjj dd(Time)\\\\ +sorgum tjj dd(Time)+tomato tjj dd(Time)+wheat tjj dd(Time)+rice tjj dd(Time)'
    Units: b'MCM/Month'
    Limits: (None, None)
    Type: component

    b''
    """
    return apple_tjj_dd(time()) + citrud_tjj_dd(time()) + grain_maiz_tjj_dd(
        time()) + rapeseed_tjj_dd(time()) + sorgum_tjj_dd(time()) + tomato_tjj_dd(
        time()) + wheat_tjj_dd(time()) + rice_tjj_dd(time())


def rapeseed_tjj_dd(x):
    """
    Real Name: b'rapeseed tjj dd'
    Original Eqn: b'( [(1,0)-(365,0.03)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,\\\\ 0),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23\\\\ ,0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35\\\\ ,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47\\\\ ,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94,0),(95\\\\ ,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105,0),(106\\\\ ,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0),(116,0)\\\\ ,(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126,0),(127\\\\ ,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0),(137,0)\\\\ ,(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147,0),(148\\\\ ,0),(149,0),(150,0),(151,0),(152,0),(153,0),(154,0),(155,0),(156,0),(157,0),(158,0)\\\\ ,(159,0),(160,0),(161,0),(162,0),(163,0),(164,0),(165,0),(166,0),(167,0),(168,0),(169\\\\ ,0),(170,0),(171,0),(172,0),(173,0),(174,0),(175,0),(176,0),(177,0),(178,0),(179,0)\\\\ ,(180,0),(181,0),(182,0),(183,0),(184,0),(185,0),(186,0),(187,0),(188,0),(189,0),(190\\\\ ,0),(191,0),(192,0),(193,0),(194,0),(195,0),(196,0),(197,0),(198,0),(199,0),(200,0)\\\\ ,(201,0),(202,0),(203,0),(204,0),(205,0),(206,0),(207,0),(208,0),(209,0),(210,0),(211\\\\ ,0.00454),(212,0.00454),(213,0.00454),(214,0.00454),(215,0.00454),(216,0.00454),(217\\\\ ,0.00454),(218,0.00454),(219,0.00454),(220,0.00454),(221,0.00454),(222,0.00454),(223\\\\ ,0.00454),(224,0.00454),(225,0.00454),(226,0.00454),(227,0.00454),(228,0.00454),(229\\\\ ,0.00454),(230,0.00454),(231,0.00454),(232,0.00454),(233,0.00454),(234,0.00454),(235\\\\ ,0.00454),(236,0.00454),(237,0.00454),(238,0.00454),(239,0.00454),(240,0.00454),(241\\\\ ,0.01645),(242,0.01645),(243,0.01645),(244,0.01645),(245,0.01645),(246,0.01645),(247\\\\ ,0.01645),(248,0.01645),(249,0.01645),(250,0.01645),(251,0.01645),(252,0.01645),(253\\\\ ,0.01645),(254,0.01645),(255,0.01645),(256,0.01645),(257,0.01645),(258,0.01645),(259\\\\ ,0.01645),(260,0.01645),(261,0.01645),(262,0.01645),(263,0.01645),(264,0.01645),(265\\\\ ,0.01645),(266,0.01645),(267,0.01645),(268,0.01645),(269,0.01645),(270,0.01645),(271\\\\ ,0.02535),(272,0.02535),(273,0.02535),(274,0.02535),(275,0.02535),(276,0.02535),(277\\\\ ,0.02535),(278,0.02535),(279,0.02535),(280,0.02535),(281,0.02535),(282,0.02535),(283\\\\ ,0.02535),(284,0.02535),(285,0.02535),(286,0.02535),(287,0.02535),(288,0.02535),(289\\\\ ,0.02535),(290,0.02535),(291,0.02535),(292,0.02535),(293,0.02535),(294,0.02535),(295\\\\ ,0.02535),(296,0.02535),(297,0.02535),(298,0.02535),(299,0.02535),(300,0.02535),(301\\\\ ,0.02199),(302,0.02199),(303,0.02199),(304,0.02199),(305,0.02199),(306,0.02199),(307\\\\ ,0.02199),(308,0.02199),(309,0.02199),(310,0.02199),(311,0.02199),(312,0.02199),(313\\\\ ,0.02199),(314,0.02199),(315,0.02199),(316,0.02199),(317,0.02199),(318,0.02199),(319\\\\ ,0.02199),(320,0.02199),(321,0.02199),(322,0.02199),(323,0.02199),(324,0.02199),(325\\\\ ,0.02199),(326,0.02199),(327,0.02199),(328,0.02199),(329,0.02199),(330,0.02199),(331\\\\ ,0.01203),(332,0.01203),(333,0.01203),(334,0.01203),(335,0.01203),(336,0.01203),(337\\\\ ,0.01203),(338,0.01203),(339,0.01203),(340,0.01203),(341,0.01203),(342,0.01203),(343\\\\ ,0.01203),(344,0.01203),(345,0.01203),(346,0.01203),(347,0.01203),(348,0.01203),(349\\\\ ,0.01203),(350,0.01203),(351,0.01203),(352,0.01203),(353,0.01203),(354,0.01203),(355\\\\ ,0.01203),(356,0.01203),(357,0.01203),(358,0.01203),(359,0.01203),(360,0.01203),(361\\\\ ,0.01203),(362,0.01203),(363,0.01203),(364,0.01203),(365,0.01203))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b'sixth priority'
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], lookups_data["rapeseed_tjj_dd"]
                            # [
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0.00454, 0.00454, 0.00454, 0.00454, 0.00454, 0.00454, 0.00454, 0.00454, 0.00454,
                            #     0.00454,
                            #     0.00454, 0.00454, 0.00454, 0.00454, 0.00454, 0.00454, 0.00454, 0.00454, 0.00454,
                            #     0.00454,
                            #     0.00454, 0.00454, 0.00454, 0.00454, 0.00454, 0.00454, 0.00454, 0.00454, 0.00454,
                            #     0.00454,
                            #     0.01645, 0.01645, 0.01645, 0.01645, 0.01645, 0.01645, 0.01645, 0.01645, 0.01645,
                            #     0.01645,
                            #     0.01645, 0.01645, 0.01645, 0.01645, 0.01645, 0.01645, 0.01645, 0.01645, 0.01645,
                            #     0.01645,
                            #     0.01645, 0.01645, 0.01645, 0.01645, 0.01645, 0.01645, 0.01645, 0.01645, 0.01645,
                            #     0.01645,
                            #     0.02535, 0.02535, 0.02535, 0.02535, 0.02535, 0.02535, 0.02535, 0.02535, 0.02535,
                            #     0.02535,
                            #     0.02535, 0.02535, 0.02535, 0.02535, 0.02535, 0.02535, 0.02535, 0.02535, 0.02535,
                            #     0.02535,
                            #     0.02535, 0.02535, 0.02535, 0.02535, 0.02535, 0.02535, 0.02535, 0.02535, 0.02535,
                            #     0.02535,
                            #     0.02199, 0.02199, 0.02199, 0.02199, 0.02199, 0.02199, 0.02199, 0.02199, 0.02199,
                            #     0.02199,
                            #     0.02199, 0.02199, 0.02199, 0.02199, 0.02199, 0.02199, 0.02199, 0.02199, 0.02199,
                            #     0.02199,
                            #     0.02199, 0.02199, 0.02199, 0.02199, 0.02199, 0.02199, 0.02199, 0.02199, 0.02199,
                            #     0.02199,
                            #     0.01203, 0.01203, 0.01203, 0.01203, 0.01203, 0.01203, 0.01203, 0.01203, 0.01203,
                            #     0.01203,
                            #     0.01203, 0.01203, 0.01203, 0.01203, 0.01203, 0.01203, 0.01203, 0.01203, 0.01203,
                            #     0.01203,
                            #     0.01203, 0.01203, 0.01203, 0.01203, 0.01203, 0.01203, 0.01203, 0.01203, 0.01203,
                            #     0.01203,
                            #     0.01203, 0.01203, 0.01203, 0.01203, 0.01203
                            # ]
                            )


def rice_tjj_dd(x):
    """
    Real Name: b'rice tjj dd'
    Original Eqn: b'( [(1,0)-(365,3)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0),\\\\ (12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23,0)\\\\ ,(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35,0\\\\ ),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47,\\\\ 0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94,0),(95\\\\ ,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105,0),(106\\\\ ,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0),(116,0)\\\\ ,(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126,0),(127\\\\ ,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0),(137,0)\\\\ ,(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147,0),(148\\\\ ,0),(149,0),(150,0),(151,0),(152,0),(153,0),(154,0),(155,0),(156,0),(157,0),(158,0)\\\\ ,(159,0),(160,0),(161,0),(162,0),(163,0),(164,0),(165,0),(166,0),(167,0),(168,0),(169\\\\ ,0),(170,0),(171,0),(172,0),(173,0),(174,0),(175,0),(176,0),(177,0),(178,0),(179,0)\\\\ ,(180,0),(181,0),(182,0),(183,0),(184,0),(185,0),(186,0),(187,0),(188,0),(189,0),(190\\\\ ,0),(191,0),(192,0),(193,0),(194,0),(195,0),(196,0),(197,0),(198,0),(199,0),(200,0)\\\\ ,(201,0),(202,0),(203,0),(204,0),(205,0),(206,0),(207,0),(208,0),(209,0),(210,0),(211\\\\ ,2.49088),(212,2.49088),(213,2.49088),(214,2.49088),(215,2.49088),(216,2.49088),(217\\\\ ,2.49088),(218,2.49088),(219,2.49088),(220,2.49088),(221,2.49088),(222,2.49088),(223\\\\ ,2.49088),(224,2.49088),(225,2.49088),(226,2.49088),(227,2.49088),(228,2.49088),(229\\\\ ,2.49088),(230,2.49088),(231,2.49088),(232,2.49088),(233,2.49088),(234,2.49088),(235\\\\ ,2.49088),(236,2.49088),(237,2.49088),(238,2.49088),(239,2.49088),(240,2.49088),(241\\\\ ,2.6042),(242,2.6042),(243,2.6042),(244,2.6042),(245,2.6042),(246,2.6042),(247,2.6042\\\\ ),(248,2.6042),(249,2.6042),(250,2.6042),(251,2.6042),(252,2.6042),(253,2.6042),(254\\\\ ,2.6042),(255,2.6042),(256,2.6042),(257,2.6042),(258,2.6042),(259,2.6042),(260,2.6042\\\\ ),(261,2.6042),(262,2.6042),(263,2.6042),(264,2.6042),(265,2.6042),(266,2.6042),(267\\\\ ,2.6042),(268,2.6042),(269,2.6042),(270,2.6042),(271,2.51634),(272,2.51634),(273,2.51634\\\\ ),(274,2.51634),(275,2.51634),(276,2.51634),(277,2.51634),(278,2.51634),(279,2.51634\\\\ ),(280,2.51634),(281,2.51634),(282,2.51634),(283,2.51634),(284,2.51634),(285,2.51634\\\\ ),(286,2.51634),(287,2.51634),(288,2.51634),(289,2.51634),(290,2.51634),(291,2.51634\\\\ ),(292,2.51634),(293,2.51634),(294,2.51634),(295,2.51634),(296,2.51634),(297,2.51634\\\\ ),(298,2.51634),(299,2.51634),(300,2.51634),(301,2.51634),(302,2.51634),(303,2.51634\\\\ ),(304,2.51634),(305,2.51634),(306,2.51634),(307,2.51634),(308,2.51634),(309,2.51634\\\\ ),(310,2.51634),(311,2.51634),(312,2.51634),(313,2.51634),(314,2.51634),(315,2.51634\\\\ ),(316,2.51634),(317,2.51634),(318,2.51634),(319,2.51634),(320,2.51634),(321,2.51634\\\\ ),(322,2.51634),(323,2.51634),(324,2.51634),(325,2.51634),(326,2.51634),(327,2.51634\\\\ ),(328,2.51634),(329,2.51634),(330,2.51634),(331,0.48111),(332,0.48111),(333,0.48111\\\\ ),(334,0.48111),(335,0.48111),(336,0.48111),(337,0.48111),(338,0.48111),(339,0.48111\\\\ ),(340,0.48111),(341,0.48111),(342,0.48111),(343,0.48111),(344,0.48111),(345,0.48111\\\\ ),(346,0.48111),(347,0.48111),(348,0.48111),(349,0.48111),(350,0.48111),(351,0.48111\\\\ ),(352,0.48111),(353,0.48111),(354,0.48111),(355,0.48111),(356,0.48111),(357,0.48111\\\\ ),(358,0.48111),(359,0.48111),(360,0.48111),(361,0.48111),(362,0.48111),(363,0.48111\\\\ ),(364,0.48111),(365,0.48111))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b'first priority'
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], lookups_data["rapeseed_tjj_dd"]
                            # [
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     2.49088, 2.49088, 2.49088, 2.49088, 2.49088, 2.49088, 2.49088, 2.49088, 2.49088,
                            #     2.49088,
                            #     2.49088, 2.49088, 2.49088, 2.49088, 2.49088, 2.49088, 2.49088, 2.49088, 2.49088,
                            #     2.49088,
                            #     2.49088, 2.49088, 2.49088, 2.49088, 2.49088, 2.49088, 2.49088, 2.49088, 2.49088,
                            #     2.49088,
                            #     2.6042, 2.6042, 2.6042, 2.6042, 2.6042, 2.6042, 2.6042, 2.6042, 2.6042, 2.6042, 2.6042,
                            #     2.6042, 2.6042, 2.6042, 2.6042, 2.6042, 2.6042, 2.6042, 2.6042, 2.6042, 2.6042, 2.6042,
                            #     2.6042, 2.6042, 2.6042, 2.6042, 2.6042, 2.6042, 2.6042, 2.6042, 2.51634, 2.51634,
                            #     2.51634,
                            #     2.51634, 2.51634, 2.51634, 2.51634, 2.51634, 2.51634, 2.51634, 2.51634, 2.51634,
                            #     2.51634,
                            #     2.51634, 2.51634, 2.51634, 2.51634, 2.51634, 2.51634, 2.51634, 2.51634, 2.51634,
                            #     2.51634,
                            #     2.51634, 2.51634, 2.51634, 2.51634, 2.51634, 2.51634, 2.51634, 2.51634, 2.51634,
                            #     2.51634,
                            #     2.51634, 2.51634, 2.51634, 2.51634, 2.51634, 2.51634, 2.51634, 2.51634, 2.51634,
                            #     2.51634,
                            #     2.51634, 2.51634, 2.51634, 2.51634, 2.51634, 2.51634, 2.51634, 2.51634, 2.51634,
                            #     2.51634,
                            #     2.51634, 2.51634, 2.51634, 2.51634, 2.51634, 2.51634, 2.51634, 0.48111, 0.48111,
                            #     0.48111,
                            #     0.48111, 0.48111, 0.48111, 0.48111, 0.48111, 0.48111, 0.48111, 0.48111, 0.48111,
                            #     0.48111,
                            #     0.48111, 0.48111, 0.48111, 0.48111, 0.48111, 0.48111, 0.48111, 0.48111, 0.48111,
                            #     0.48111,
                            #     0.48111, 0.48111, 0.48111, 0.48111, 0.48111, 0.48111, 0.48111, 0.48111, 0.48111,
                            #     0.48111,
                            #     0.48111, 0.48111
                            # ]
                            )


def sorgum_tjj_dd(x):
    """
    Real Name: b'sorgum tjj dd'
    Original Eqn: b'( [(1,0)-(365,0.3)],(1,0.02199),(2,0.02199),(3,0.02199),(4,0.02199),(5,0.02199),(6,0.02199\\\\ ),(7,0.02199),(8,0.02199),(9,0.02199),(10,0.02199),(11,0.02199),(12,0.02199),(13,0.02199\\\\ ),(14,0.02199),(15,0.02199),(16,0.02199),(17,0.02199),(18,0.02199),(19,0.02199),(20\\\\ ,0.02199),(21,0.02199),(22,0.02199),(23,0.02199),(24,0.02199),(25,0.02199),(26,0.02199\\\\ ),(27,0.02199),(28,0.02199),(29,0.02199),(30,0.02199),(31,0),(32,0),(33,0),(34,0),(\\\\ 35,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),\\\\ (47,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0)\\\\ ,(59,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0\\\\ ),(71,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,\\\\ 0),(83,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94\\\\ ,0),(95,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105\\\\ ,0),(106,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0)\\\\ ,(116,0),(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126\\\\ ,0),(127,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0)\\\\ ,(137,0),(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147\\\\ ,0),(148,0),(149,0),(150,0),(151,0),(152,0),(153,0),(154,0),(155,0),(156,0),(157,0)\\\\ ,(158,0),(159,0),(160,0),(161,0),(162,0),(163,0),(164,0),(165,0),(166,0),(167,0),(168\\\\ ,0),(169,0),(170,0),(171,0),(172,0),(173,0),(174,0),(175,0),(176,0),(177,0),(178,0)\\\\ ,(179,0),(180,0),(181,0.24032),(182,0.24032),(183,0.24032),(184,0.24032),(185,0.24032\\\\ ),(186,0.24032),(187,0.24032),(188,0.24032),(189,0.24032),(190,0.24032),(191,0.24032\\\\ ),(192,0.24032),(193,0.24032),(194,0.24032),(195,0.24032),(196,0.24032),(197,0.24032\\\\ ),(198,0.24032),(199,0.24032),(200,0.24032),(201,0.24032),(202,0.24032),(203,0.24032\\\\ ),(204,0.24032),(205,0.24032),(206,0.24032),(207,0.24032),(208,0.24032),(209,0.24032\\\\ ),(210,0.24032),(211,0.0919),(212,0.0919),(213,0.0919),(214,0.0919),(215,0.0919),(216\\\\ ,0.0919),(217,0.0919),(218,0.0919),(219,0.0919),(220,0.0919),(221,0.0919),(222,0.0919\\\\ ),(223,0.0919),(224,0.0919),(225,0.0919),(226,0.0919),(227,0.0919),(228,0.0919),(229\\\\ ,0.0919),(230,0.0919),(231,0.0919),(232,0.0919),(233,0.0919),(234,0.0919),(235,0.0919\\\\ ),(236,0.0919),(237,0.0919),(238,0.0919),(239,0.0919),(240,0.0919),(241,0.07149),(242\\\\ ,0.07149),(243,0.07149),(244,0.07149),(245,0.07149),(246,0.07149),(247,0.07149),(248\\\\ ,0.07149),(249,0.07149),(250,0.07149),(251,0.07149),(252,0.07149),(253,0.07149),(254\\\\ ,0.07149),(255,0.07149),(256,0.07149),(257,0.07149),(258,0.07149),(259,0.07149),(260\\\\ ,0.07149),(261,0.07149),(262,0.07149),(263,0.07149),(264,0.07149),(265,0.07149),(266\\\\ ,0.07149),(267,0.07149),(268,0.07149),(269,0.07149),(270,0.07149),(271,0.06803),(272\\\\ ,0.06803),(273,0.06803),(274,0.06803),(275,0.06803),(276,0.06803),(277,0.06803),(278\\\\ ,0.06803),(279,0.06803),(280,0.06803),(281,0.06803),(282,0.06803),(283,0.06803),(284\\\\ ,0.06803),(285,0.06803),(286,0.06803),(287,0.06803),(288,0.06803),(289,0.06803),(290\\\\ ,0.06803),(291,0.06803),(292,0.06803),(293,0.06803),(294,0.06803),(295,0.06803),(296\\\\ ,0.06803),(297,0.06803),(298,0.06803),(299,0.06803),(300,0.06803),(301,0.06803),(302\\\\ ,0.06803),(303,0.06803),(304,0.06803),(305,0.06803),(306,0.06803),(307,0.06803),(308\\\\ ,0.06803),(309,0.06803),(310,0.06803),(311,0.06803),(312,0.06803),(313,0.06803),(314\\\\ ,0.06803),(315,0.06803),(316,0.06803),(317,0.06803),(318,0.06803),(319,0.06803),(320\\\\ ,0.06803),(321,0.06803),(322,0.06803),(323,0.06803),(324,0.06803),(325,0.06803),(326\\\\ ,0.06803),(327,0.06803),(328,0.06803),(329,0.06803),(330,0.06803),(331,0.04992),(332\\\\ ,0.04992),(333,0.04992),(334,0.04992),(335,0.04992),(336,0.04992),(337,0.04992),(338\\\\ ,0.04992),(339,0.04992),(340,0.04992),(341,0.04992),(342,0.04992),(343,0.04992),(344\\\\ ,0.04992),(345,0.04992),(346,0.04992),(347,0.04992),(348,0.04992),(349,0.04992),(350\\\\ ,0.04992),(351,0.04992),(352,0.04992),(353,0.04992),(354,0.04992),(355,0.04992),(356\\\\ ,0.04992),(357,0.04992),(358,0.04992),(359,0.04992),(360,0.04992),(361,0.04992),(362\\\\ ,0.04992),(363,0.04992),(364,0.04992),(365,0.04992))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], lookups_data["sorgum_tjj_dd"]
                            # [
                            #     0.02199, 0.02199, 0.02199, 0.02199, 0.02199, 0.02199, 0.02199, 0.02199, 0.02199,
                            #     0.02199,
                            #     0.02199, 0.02199, 0.02199, 0.02199, 0.02199, 0.02199, 0.02199, 0.02199, 0.02199,
                            #     0.02199,
                            #     0.02199, 0.02199, 0.02199, 0.02199, 0.02199, 0.02199, 0.02199, 0.02199, 0.02199,
                            #     0.02199,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0.24032, 0.24032, 0.24032, 0.24032, 0.24032, 0.24032, 0.24032, 0.24032, 0.24032,
                            #     0.24032,
                            #     0.24032, 0.24032, 0.24032, 0.24032, 0.24032, 0.24032, 0.24032, 0.24032, 0.24032,
                            #     0.24032,
                            #     0.24032, 0.24032, 0.24032, 0.24032, 0.24032, 0.24032, 0.24032, 0.24032, 0.24032,
                            #     0.24032,
                            #     0.0919, 0.0919, 0.0919, 0.0919, 0.0919, 0.0919, 0.0919, 0.0919, 0.0919, 0.0919, 0.0919,
                            #     0.0919, 0.0919, 0.0919, 0.0919, 0.0919, 0.0919, 0.0919, 0.0919, 0.0919, 0.0919, 0.0919,
                            #     0.0919, 0.0919, 0.0919, 0.0919, 0.0919, 0.0919, 0.0919, 0.0919, 0.07149, 0.07149,
                            #     0.07149,
                            #     0.07149, 0.07149, 0.07149, 0.07149, 0.07149, 0.07149, 0.07149, 0.07149, 0.07149,
                            #     0.07149,
                            #     0.07149, 0.07149, 0.07149, 0.07149, 0.07149, 0.07149, 0.07149, 0.07149, 0.07149,
                            #     0.07149,
                            #     0.07149, 0.07149, 0.07149, 0.07149, 0.07149, 0.07149, 0.07149, 0.06803, 0.06803,
                            #     0.06803,
                            #     0.06803, 0.06803, 0.06803, 0.06803, 0.06803, 0.06803, 0.06803, 0.06803, 0.06803,
                            #     0.06803,
                            #     0.06803, 0.06803, 0.06803, 0.06803, 0.06803, 0.06803, 0.06803, 0.06803, 0.06803,
                            #     0.06803,
                            #     0.06803, 0.06803, 0.06803, 0.06803, 0.06803, 0.06803, 0.06803, 0.06803, 0.06803,
                            #     0.06803,
                            #     0.06803, 0.06803, 0.06803, 0.06803, 0.06803, 0.06803, 0.06803, 0.06803, 0.06803,
                            #     0.06803,
                            #     0.06803, 0.06803, 0.06803, 0.06803, 0.06803, 0.06803, 0.06803, 0.06803, 0.06803,
                            #     0.06803,
                            #     0.06803, 0.06803, 0.06803, 0.06803, 0.06803, 0.06803, 0.06803, 0.04992, 0.04992,
                            #     0.04992,
                            #     0.04992, 0.04992, 0.04992, 0.04992, 0.04992, 0.04992, 0.04992, 0.04992, 0.04992,
                            #     0.04992,
                            #     0.04992, 0.04992, 0.04992, 0.04992, 0.04992, 0.04992, 0.04992, 0.04992, 0.04992,
                            #     0.04992,
                            #     0.04992, 0.04992, 0.04992, 0.04992, 0.04992, 0.04992, 0.04992, 0.04992, 0.04992,
                            #     0.04992,
                            #     0.04992, 0.04992
                            # ]
                            )


def apple_tjj_dd(x):
    """
    Real Name: b'apple tjj dd'
    Original Eqn: b'( [(1,0)-(365,0.2)],(1,0.03213),(2,0.03213),(3,0.03213),(4,0.03213),(5,0.03213),(6,0.03213\\\\ ),(7,0.03213),(8,0.03213),(9,0.03213),(10,0.03213),(11,0.03213),(12,0.03213),(13,0.03213\\\\ ),(14,0.03213),(15,0.03213),(16,0.03213),(17,0.03213),(18,0.03213),(19,0.03213),(20\\\\ ,0.03213),(21,0.03213),(22,0.03213),(23,0.03213),(24,0.03213),(25,0.03213),(26,0.03213\\\\ ),(27,0.03213),(28,0.03213),(29,0.03213),(30,0.03213),(31,0),(32,0),(33,0),(34,0),(\\\\ 35,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),\\\\ (47,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0)\\\\ ,(59,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0\\\\ ),(71,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,\\\\ 0),(83,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94\\\\ ,0),(95,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105\\\\ ,0),(106,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0)\\\\ ,(116,0),(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126\\\\ ,0),(127,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0)\\\\ ,(137,0),(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147\\\\ ,0),(148,0),(149,0),(150,0),(151,0),(152,0),(153,0),(154,0),(155,0),(156,0),(157,0)\\\\ ,(158,0),(159,0),(160,0),(161,0),(162,0),(163,0),(164,0),(165,0),(166,0),(167,0),(168\\\\ ,0),(169,0),(170,0),(171,0),(172,0),(173,0),(174,0),(175,0),(176,0),(177,0),(178,0)\\\\ ,(179,0),(180,0),(181,0),(182,0),(183,0),(184,0),(185,0),(186,0),(187,0),(188,0),(189\\\\ ,0),(190,0),(191,0),(192,0),(193,0),(194,0),(195,0),(196,0),(197,0),(198,0),(199,0)\\\\ ,(200,0),(201,0),(202,0),(203,0),(204,0),(205,0),(206,0),(207,0),(208,0),(209,0),(210\\\\ ,0),(211,0.03984),(212,0.03984),(213,0.03984),(214,0.03984),(215,0.03984),(216,0.03984\\\\ ),(217,0.03984),(218,0.03984),(219,0.03984),(220,0.03984),(221,0.03984),(222,0.03984\\\\ ),(223,0.03984),(224,0.03984),(225,0.03984),(226,0.03984),(227,0.03984),(228,0.03984\\\\ ),(229,0.03984),(230,0.03984),(231,0.03984),(232,0.03984),(233,0.03984),(234,0.03984\\\\ ),(235,0.03984),(236,0.03984),(237,0.03984),(238,0.03984),(239,0.03984),(240,0.03984\\\\ ),(241,0.06931),(242,0.06931),(243,0.06931),(244,0.06931),(245,0.06931),(246,0.06931\\\\ ),(247,0.06931),(248,0.06931),(249,0.06931),(250,0.06931),(251,0.06931),(252,0.06931\\\\ ),(253,0.06931),(254,0.06931),(255,0.06931),(256,0.06931),(257,0.06931),(258,0.06931\\\\ ),(259,0.06931),(260,0.06931),(261,0.06931),(262,0.06931),(263,0.06931),(264,0.06931\\\\ ),(265,0.06931),(266,0.06931),(267,0.06931),(268,0.06931),(269,0.06931),(270,0.06931\\\\ ),(271,0.10976),(272,0.10976),(273,0.10976),(274,0.10976),(275,0.10976),(276,0.10976\\\\ ),(277,0.10976),(278,0.10976),(279,0.10976),(280,0.10976),(281,0.10976),(282,0.10976\\\\ ),(283,0.10976),(284,0.10976),(285,0.10976),(286,0.10976),(287,0.10976),(288,0.10976\\\\ ),(289,0.10976),(290,0.10976),(291,0.10976),(292,0.10976),(293,0.10976),(294,0.10976\\\\ ),(295,0.10976),(296,0.10976),(297,0.10976),(298,0.10976),(299,0.10976),(300,0.10976\\\\ ),(301,0.10976),(302,0.10976),(303,0.10976),(304,0.10976),(305,0.10976),(306,0.10976\\\\ ),(307,0.10976),(308,0.10976),(309,0.10976),(310,0.10976),(311,0.10976),(312,0.10976\\\\ ),(313,0.10976),(314,0.10976),(315,0.10976),(316,0.10976),(317,0.10976),(318,0.10976\\\\ ),(319,0.10976),(320,0.10976),(321,0.10976),(322,0.10976),(323,0.10976),(324,0.10976\\\\ ),(325,0.10976),(326,0.10976),(327,0.10976),(328,0.10976),(329,0.10976),(330,0.10976\\\\ ),(331,0.08962),(332,0.08962),(333,0.08962),(334,0.08962),(335,0.08962),(336,0.08962\\\\ ),(337,0.08962),(338,0.08962),(339,0.08962),(340,0.08962),(341,0.08962),(342,0.08962\\\\ ),(343,0.08962),(344,0.08962),(345,0.08962),(346,0.08962),(347,0.08962),(348,0.08962\\\\ ),(349,0.08962),(350,0.08962),(351,0.08962),(352,0.08962),(353,0.08962),(354,0.08962\\\\ ),(355,0.08962),(356,0.08962),(357,0.08962),(358,0.08962),(359,0.08962),(360,0.08962\\\\ ),(361,0.08962),(362,0.08962),(363,0.08962),(364,0.08962),(365,0.08962))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b'third priority'
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], lookups_data["apple_tjj_dd"]
                            # [
                            #     0.03213, 0.03213, 0.03213, 0.03213, 0.03213, 0.03213, 0.03213, 0.03213, 0.03213,
                            #     0.03213,
                            #     0.03213, 0.03213, 0.03213, 0.03213, 0.03213, 0.03213, 0.03213, 0.03213, 0.03213,
                            #     0.03213,
                            #     0.03213, 0.03213, 0.03213, 0.03213, 0.03213, 0.03213, 0.03213, 0.03213, 0.03213,
                            #     0.03213,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0.03984, 0.03984, 0.03984, 0.03984, 0.03984, 0.03984, 0.03984, 0.03984, 0.03984,
                            #     0.03984,
                            #     0.03984, 0.03984, 0.03984, 0.03984, 0.03984, 0.03984, 0.03984, 0.03984, 0.03984,
                            #     0.03984,
                            #     0.03984, 0.03984, 0.03984, 0.03984, 0.03984, 0.03984, 0.03984, 0.03984, 0.03984,
                            #     0.03984,
                            #     0.06931, 0.06931, 0.06931, 0.06931, 0.06931, 0.06931, 0.06931, 0.06931, 0.06931,
                            #     0.06931,
                            #     0.06931, 0.06931, 0.06931, 0.06931, 0.06931, 0.06931, 0.06931, 0.06931, 0.06931,
                            #     0.06931,
                            #     0.06931, 0.06931, 0.06931, 0.06931, 0.06931, 0.06931, 0.06931, 0.06931, 0.06931,
                            #     0.06931,
                            #     0.10976, 0.10976, 0.10976, 0.10976, 0.10976, 0.10976, 0.10976, 0.10976, 0.10976,
                            #     0.10976,
                            #     0.10976, 0.10976, 0.10976, 0.10976, 0.10976, 0.10976, 0.10976, 0.10976, 0.10976,
                            #     0.10976,
                            #     0.10976, 0.10976, 0.10976, 0.10976, 0.10976, 0.10976, 0.10976, 0.10976, 0.10976,
                            #     0.10976,
                            #     0.10976, 0.10976, 0.10976, 0.10976, 0.10976, 0.10976, 0.10976, 0.10976, 0.10976,
                            #     0.10976,
                            #     0.10976, 0.10976, 0.10976, 0.10976, 0.10976, 0.10976, 0.10976, 0.10976, 0.10976,
                            #     0.10976,
                            #     0.10976, 0.10976, 0.10976, 0.10976, 0.10976, 0.10976, 0.10976, 0.10976, 0.10976,
                            #     0.10976,
                            #     0.08962, 0.08962, 0.08962, 0.08962, 0.08962, 0.08962, 0.08962, 0.08962, 0.08962,
                            #     0.08962,
                            #     0.08962, 0.08962, 0.08962, 0.08962, 0.08962, 0.08962, 0.08962, 0.08962, 0.08962,
                            #     0.08962,
                            #     0.08962, 0.08962, 0.08962, 0.08962, 0.08962, 0.08962, 0.08962, 0.08962, 0.08962,
                            #     0.08962,
                            #     0.08962, 0.08962, 0.08962, 0.08962, 0.08962
                            # ]
                            )


@cache('step')
def wr_def_tj_bfr_zr():
    """
    Real Name: b'wr Def Tj bfr Zr'
    Original Eqn: b'wr Dem Tj bfr Zr -wr sup Tj bfr Zr'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return wr_dem_tj_bfr_zr() - wr_sup_tj_bfr_zr()


@cache('step')
def wr_dem_tj_bfr_zr():
    """
    Real Name: b'wr Dem Tj bfr Zr'
    Original Eqn: b'"Citrus Bfr Tajan D.D"(Time)'
    Units: b'MCM/Month'
    Limits: (None, None)
    Type: component

    b''
    """
    return citrus_bfr_tajan_dd(time())


@cache('step')
def wr_sup_tj_bfr_zr():
    """
    Real Name: b'wr sup Tj bfr Zr'
    Original Eqn: b'MIN(Tajan Befr zarem, wr Dem Tj bfr Zr )'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return np.minimum(tajan_befr_zarem(), wr_dem_tj_bfr_zr())


def citrus_bfr_tajan_dd(x):
    """
    Real Name: b'"Citrus Bfr Tajan D.D"'
    Original Eqn: b'( [(1,0)-(365,0.04)],(1,0.00094),(2,0.00094),(3,0.00094),(4,0.00094),(5,0.00094),(6,0.00094\\\\ ),(7,0.00094),(8,0.00094),(9,0.00094),(10,0.00094),(11,0.00094),(12,0.00094),(13,0.00094\\\\ ),(14,0.00094),(15,0.00094),(16,0.00094),(17,0.00094),(18,0.00094),(19,0.00094),(20\\\\ ,0.00094),(21,0.00094),(22,0.00094),(23,0.00094),(24,0.00094),(25,0.00094),(26,0.00094\\\\ ),(27,0.00094),(28,0.00094),(29,0.00094),(30,0.00094),(31,0),(32,0),(33,0),(34,0),(\\\\ 35,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),\\\\ (47,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0)\\\\ ,(59,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0\\\\ ),(71,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,\\\\ 0),(83,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94\\\\ ,0),(95,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105\\\\ ,0),(106,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0)\\\\ ,(116,0),(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126\\\\ ,0),(127,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0)\\\\ ,(137,0),(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147\\\\ ,0),(148,0),(149,0),(150,0),(151,0),(152,0),(153,0),(154,0),(155,0),(156,0),(157,0)\\\\ ,(158,0),(159,0),(160,0),(161,0),(162,0),(163,0),(164,0),(165,0),(166,0),(167,0),(168\\\\ ,0),(169,0),(170,0),(171,0),(172,0),(173,0),(174,0),(175,0),(176,0),(177,0),(178,0)\\\\ ,(179,0),(180,0),(181,0.01846),(182,0.01846),(183,0.01846),(184,0.01846),(185,0.01846\\\\ ),(186,0.01846),(187,0.01846),(188,0.01846),(189,0.01846),(190,0.01846),(191,0.01846\\\\ ),(192,0.01846),(193,0.01846),(194,0.01846),(195,0.01846),(196,0.01846),(197,0.01846\\\\ ),(198,0.01846),(199,0.01846),(200,0.01846),(201,0.01846),(202,0.01846),(203,0.01846\\\\ ),(204,0.01846),(205,0.01846),(206,0.01846),(207,0.01846),(208,0.01846),(209,0.01846\\\\ ),(210,0.01846),(211,0.03598),(212,0.03598),(213,0.03598),(214,0.03598),(215,0.03598\\\\ ),(216,0.03598),(217,0.03598),(218,0.03598),(219,0.03598),(220,0.03598),(221,0.03598\\\\ ),(222,0.03598),(223,0.03598),(224,0.03598),(225,0.03598),(226,0.03598),(227,0.03598\\\\ ),(228,0.03598),(229,0.03598),(230,0.03598),(231,0.03598),(232,0.03598),(233,0.03598\\\\ ),(234,0.03598),(235,0.03598),(236,0.03598),(237,0.03598),(238,0.03598),(239,0.03598\\\\ ),(240,0.03598),(241,0.03425),(242,0.03425),(243,0.03425),(244,0.03425),(245,0.03425\\\\ ),(246,0.03425),(247,0.03425),(248,0.03425),(249,0.03425),(250,0.03425),(251,0.03425\\\\ ),(252,0.03425),(253,0.03425),(254,0.03425),(255,0.03425),(256,0.03425),(257,0.03425\\\\ ),(258,0.03425),(259,0.03425),(260,0.03425),(261,0.03425),(262,0.03425),(263,0.03425\\\\ ),(264,0.03425),(265,0.03425),(266,0.03425),(267,0.03425),(268,0.03425),(269,0.03425\\\\ ),(270,0.03425),(271,0.03674),(272,0.03674),(273,0.03674),(274,0.03674),(275,0.03674\\\\ ),(276,0.03674),(277,0.03674),(278,0.03674),(279,0.03674),(280,0.03674),(281,0.03674\\\\ ),(282,0.03674),(283,0.03674),(284,0.03674),(285,0.03674),(286,0.03674),(287,0.03674\\\\ ),(288,0.03674),(289,0.03674),(290,0.03674),(291,0.03674),(292,0.03674),(293,0.03674\\\\ ),(294,0.03674),(295,0.03674),(296,0.03674),(297,0.03674),(298,0.03674),(299,0.03674\\\\ ),(300,0.03674),(301,0.03163),(302,0.03163),(303,0.03163),(304,0.03163),(305,0.03163\\\\ ),(306,0.03163),(307,0.03163),(308,0.03163),(309,0.03163),(310,0.03163),(311,0.03163\\\\ ),(312,0.03163),(313,0.03163),(314,0.03163),(315,0.03163),(316,0.03163),(317,0.03163\\\\ ),(318,0.03163),(319,0.03163),(320,0.03163),(321,0.03163),(322,0.03163),(323,0.03163\\\\ ),(324,0.03163),(325,0.03163),(326,0.03163),(327,0.03163),(328,0.03163),(329,0.03163\\\\ ),(330,0.03163),(331,0.01029),(332,0.01029),(333,0.01029),(334,0.01029),(335,0.01029\\\\ ),(336,0.01029),(337,0.01029),(338,0.01029),(339,0.01029),(340,0.01029),(341,0.01029\\\\ ),(342,0.01029),(343,0.01029),(344,0.01029),(345,0.01029),(346,0.01029),(347,0.01029\\\\ ),(348,0.01029),(349,0.01029),(350,0.01029),(351,0.01029),(352,0.01029),(353,0.01029\\\\ ),(354,0.01029),(355,0.01029),(356,0.01029),(357,0.01029),(358,0.01029),(359,0.01029\\\\ ),(360,0.01029),(361,0.01029),(362,0.01029),(363,0.01029),(364,0.01029),(365,0.01029\\\\ ))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], [
                                0.00094, 0.00094, 0.00094, 0.00094, 0.00094, 0.00094, 0.00094, 0.00094, 0.00094,
                                0.00094,
                                0.00094, 0.00094, 0.00094, 0.00094, 0.00094, 0.00094, 0.00094, 0.00094, 0.00094,
                                0.00094,
                                0.00094, 0.00094, 0.00094, 0.00094, 0.00094, 0.00094, 0.00094, 0.00094, 0.00094,
                                0.00094,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0.01846, 0.01846, 0.01846, 0.01846, 0.01846, 0.01846, 0.01846, 0.01846, 0.01846,
                                0.01846,
                                0.01846, 0.01846, 0.01846, 0.01846, 0.01846, 0.01846, 0.01846, 0.01846, 0.01846,
                                0.01846,
                                0.01846, 0.01846, 0.01846, 0.01846, 0.01846, 0.01846, 0.01846, 0.01846, 0.01846,
                                0.01846,
                                0.03598, 0.03598, 0.03598, 0.03598, 0.03598, 0.03598, 0.03598, 0.03598, 0.03598,
                                0.03598,
                                0.03598, 0.03598, 0.03598, 0.03598, 0.03598, 0.03598, 0.03598, 0.03598, 0.03598,
                                0.03598,
                                0.03598, 0.03598, 0.03598, 0.03598, 0.03598, 0.03598, 0.03598, 0.03598, 0.03598,
                                0.03598,
                                0.03425, 0.03425, 0.03425, 0.03425, 0.03425, 0.03425, 0.03425, 0.03425, 0.03425,
                                0.03425,
                                0.03425, 0.03425, 0.03425, 0.03425, 0.03425, 0.03425, 0.03425, 0.03425, 0.03425,
                                0.03425,
                                0.03425, 0.03425, 0.03425, 0.03425, 0.03425, 0.03425, 0.03425, 0.03425, 0.03425,
                                0.03425,
                                0.03674, 0.03674, 0.03674, 0.03674, 0.03674, 0.03674, 0.03674, 0.03674, 0.03674,
                                0.03674,
                                0.03674, 0.03674, 0.03674, 0.03674, 0.03674, 0.03674, 0.03674, 0.03674, 0.03674,
                                0.03674,
                                0.03674, 0.03674, 0.03674, 0.03674, 0.03674, 0.03674, 0.03674, 0.03674, 0.03674,
                                0.03674,
                                0.03163, 0.03163, 0.03163, 0.03163, 0.03163, 0.03163, 0.03163, 0.03163, 0.03163,
                                0.03163,
                                0.03163, 0.03163, 0.03163, 0.03163, 0.03163, 0.03163, 0.03163, 0.03163, 0.03163,
                                0.03163,
                                0.03163, 0.03163, 0.03163, 0.03163, 0.03163, 0.03163, 0.03163, 0.03163, 0.03163,
                                0.03163,
                                0.01029, 0.01029, 0.01029, 0.01029, 0.01029, 0.01029, 0.01029, 0.01029, 0.01029,
                                0.01029,
                                0.01029, 0.01029, 0.01029, 0.01029, 0.01029, 0.01029, 0.01029, 0.01029, 0.01029,
                                0.01029,
                                0.01029, 0.01029, 0.01029, 0.01029, 0.01029, 0.01029, 0.01029, 0.01029, 0.01029,
                                0.01029,
                                0.01029, 0.01029, 0.01029, 0.01029, 0.01029
                            ])


def apple_zr(x):
    """
    Real Name: b'apple zr'
    Original Eqn: b'( [(1,0)-(365,0.4)],(1,0.37),(2,0.37),(3,0.37),(4,0.37),(5,0.37),(6,0.37),(7,0.37),(8,\\\\ 0.37),(9,0.37),(10,0.37),(11,0.37),(12,0.37),(13,0.37),(14,0.37),(15,0.37),(16,0.37\\\\ ),(17,0.37),(18,0.37),(19,0.37),(20,0.37),(21,0.37),(22,0.37),(23,0.37),(24,0.37),(\\\\ 25,0.37),(26,0.37),(27,0.37),(28,0.37),(29,0.37),(30,0.37),(31,0),(32,0),(33,0),(34\\\\ ,0),(35,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46\\\\ ,0),(47,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58\\\\ ,0),(59,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70\\\\ ,0),(71,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82\\\\ ,0),(83,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94\\\\ ,0),(95,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105\\\\ ,0),(106,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0)\\\\ ,(116,0),(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126\\\\ ,0),(127,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0)\\\\ ,(137,0),(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147\\\\ ,0),(148,0),(149,0),(150,0),(151,0),(152,0),(153,0),(154,0),(155,0),(156,0),(157,0)\\\\ ,(158,0),(159,0),(160,0),(161,0),(162,0),(163,0),(164,0),(165,0),(166,0),(167,0),(168\\\\ ,0),(169,0),(170,0),(171,0),(172,0),(173,0),(174,0),(175,0),(176,0),(177,0),(178,0)\\\\ ,(179,0),(180,0),(181,0),(182,0),(183,0),(184,0),(185,0),(186,0),(187,0),(188,0),(189\\\\ ,0),(190,0),(191,0),(192,0),(193,0),(194,0),(195,0),(196,0),(197,0),(198,0),(199,0)\\\\ ,(200,0),(201,0),(202,0),(203,0),(204,0),(205,0),(206,0),(207,0),(208,0),(209,0),(210\\\\ ,0),(211,0),(212,0),(213,0),(214,0),(215,0),(216,0),(217,0),(218,0),(219,0),(220,0)\\\\ ,(221,0),(222,0),(223,0),(224,0),(225,0),(226,0),(227,0),(228,0),(229,0),(230,0),(231\\\\ ,0),(232,0),(233,0),(234,0),(235,0),(236,0),(237,0),(238,0),(239,0),(240,0),(241,0)\\\\ ,(242,0),(243,0),(244,0),(245,0),(246,0),(247,0),(248,0),(249,0),(250,0),(251,0),(252\\\\ ,0),(253,0),(254,0),(255,0),(256,0),(257,0),(258,0),(259,0),(260,0),(261,0),(262,0)\\\\ ,(263,0),(264,0),(265,0),(266,0),(267,0),(268,0),(269,0),(270,0),(271,0),(272,0),(273\\\\ ,0),(274,0),(275,0),(276,0),(277,0),(278,0),(279,0),(280,0),(281,0),(282,0),(283,0)\\\\ ,(284,0),(285,0),(286,0),(287,0),(288,0),(289,0),(290,0),(291,0),(292,0),(293,0),(294\\\\ ,0),(295,0),(296,0),(297,0),(298,0),(299,0),(300,0),(301,0),(302,0),(303,0),(304,0)\\\\ ,(305,0),(306,0),(307,0),(308,0),(309,0),(310,0),(311,0),(312,0),(313,0),(314,0),(315\\\\ ,0),(316,0),(317,0),(318,0),(319,0),(320,0),(321,0),(322,0),(323,0),(324,0),(325,0)\\\\ ,(326,0),(327,0),(328,0),(329,0),(330,0),(331,0),(332,0),(333,0),(334,0),(335,0),(336\\\\ ,0),(337,0),(338,0),(339,0),(340,0),(341,0),(342,0),(343,0),(344,0),(345,0),(346,0)\\\\ ,(347,0),(348,0),(349,0),(350,0),(351,0),(352,0),(353,0),(354,0),(355,0),(356,0),(357\\\\ ,0),(358,0),(359,0),(360,0),(361,0),(362,0),(363,0),(364,0),(365,0))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b'first priority'
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], lookups_data["apple_zr"]
                            # [
                            #     0.37, 0.37, 0.37, 0.37, 0.37, 0.37, 0.37, 0.37, 0.37, 0.37, 0.37, 0.37, 0.37, 0.37,
                            #     0.37,
                            #     0.37, 0.37, 0.37, 0.37, 0.37, 0.37, 0.37, 0.37, 0.37, 0.37, 0.37, 0.37, 0.37, 0.37,
                            #     0.37,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0
                            # ]
                            )


def rapeseed_zr(x):
    """
    Real Name: b'rapeseed zr'
    Original Eqn: b'( [(1,0)-(365,0.0003)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11\\\\ ,0),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23\\\\ ,0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35\\\\ ,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47\\\\ ,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94,0),(95\\\\ ,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105,0),(106\\\\ ,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0),(116,0)\\\\ ,(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126,0),(127\\\\ ,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0),(137,0)\\\\ ,(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147,0),(148\\\\ ,0),(149,0),(150,0),(151,0),(152,0),(153,0),(154,0),(155,0),(156,0),(157,0),(158,0)\\\\ ,(159,0),(160,0),(161,0),(162,0),(163,0),(164,0),(165,0),(166,0),(167,0),(168,0),(169\\\\ ,0),(170,0),(171,0),(172,0),(173,0),(174,0),(175,0),(176,0),(177,0),(178,0),(179,0)\\\\ ,(180,0),(181,0),(182,0),(183,0),(184,0),(185,0),(186,0),(187,0),(188,0),(189,0),(190\\\\ ,0),(191,0),(192,0),(193,0),(194,0),(195,0),(196,0),(197,0),(198,0),(199,0),(200,0)\\\\ ,(201,0),(202,0),(203,0),(204,0),(205,0),(206,0),(207,0),(208,0),(209,0),(210,0),(211\\\\ ,6e-005),(212,6e-005),(213,6e-005),(214,6e-005),(215,6e-005),(216,6e-005),(217,6e-005\\\\ ),(218,6e-005),(219,6e-005),(220,6e-005),(221,6e-005),(222,6e-005),(223,6e-005),(224\\\\ ,6e-005),(225,6e-005),(226,6e-005),(227,6e-005),(228,6e-005),(229,6e-005),(230,6e-005\\\\ ),(231,6e-005),(232,6e-005),(233,6e-005),(234,6e-005),(235,6e-005),(236,6e-005),(237\\\\ ,6e-005),(238,6e-005),(239,6e-005),(240,6e-005),(241,0.00022),(242,0.00022),(243,0.00022\\\\ ),(244,0.00022),(245,0.00022),(246,0.00022),(247,0.00022),(248,0.00022),(249,0.00022\\\\ ),(250,0.00022),(251,0.00022),(252,0.00022),(253,0.00022),(254,0.00022),(255,0.00022\\\\ ),(256,0.00022),(257,0.00022),(258,0.00022),(259,0.00022),(260,0.00022),(261,0.00022\\\\ ),(262,0.00022),(263,0.00022),(264,0.00022),(265,0.00022),(266,0.00022),(267,0.00022\\\\ ),(268,0.00022),(269,0.00022),(270,0.00022),(271,0.00027),(272,0.00027),(273,0.00027\\\\ ),(274,0.00027),(275,0.00027),(276,0.00027),(277,0.00027),(278,0.00027),(279,0.00027\\\\ ),(280,0.00027),(281,0.00027),(282,0.00027),(283,0.00027),(284,0.00027),(285,0.00027\\\\ ),(286,0.00027),(287,0.00027),(288,0.00027),(289,0.00027),(290,0.00027),(291,0.00027\\\\ ),(292,0.00027),(293,0.00027),(294,0.00027),(295,0.00027),(296,0.00027),(297,0.00027\\\\ ),(298,0.00027),(299,0.00027),(300,0.00027),(301,0.00021),(302,0.00021),(303,0.00021\\\\ ),(304,0.00021),(305,0.00021),(306,0.00021),(307,0.00021),(308,0.00021),(309,0.00021\\\\ ),(310,0.00021),(311,0.00021),(312,0.00021),(313,0.00021),(314,0.00021),(315,0.00021\\\\ ),(316,0.00021),(317,0.00021),(318,0.00021),(319,0.00021),(320,0.00021),(321,0.00021\\\\ ),(322,0.00021),(323,0.00021),(324,0.00021),(325,0.00021),(326,0.00021),(327,0.00021\\\\ ),(328,0.00021),(329,0.00021),(330,0.00021),(331,0.00013),(332,0.00013),(333,0.00013\\\\ ),(334,0.00013),(335,0.00013),(336,0.00013),(337,0.00013),(338,0.00013),(339,0.00013\\\\ ),(340,0.00013),(341,0.00013),(342,0.00013),(343,0.00013),(344,0.00013),(345,0.00013\\\\ ),(346,0.00013),(347,0.00013),(348,0.00013),(349,0.00013),(350,0.00013),(351,0.00013\\\\ ),(352,0.00013),(353,0.00013),(354,0.00013),(355,0.00013),(356,0.00013),(357,0.00013\\\\ ),(358,0.00013),(359,0.00013),(360,0.00013),(361,0.00013),(362,0.00013),(363,0.00013\\\\ ),(364,0.00013),(365,0.00013))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    # todo : here
    return functions.lookup(x, time_in_lookup_data, lookups_data["rapeseed_zr"]
                            # [
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     6e-005, 6e-005, 6e-005, 6e-005, 6e-005, 6e-005, 6e-005, 6e-005, 6e-005, 6e-005, 6e-005,
                            #     6e-005, 6e-005, 6e-005, 6e-005, 6e-005, 6e-005, 6e-005, 6e-005, 6e-005, 6e-005, 6e-005,
                            #     6e-005, 6e-005, 6e-005, 6e-005, 6e-005, 6e-005, 6e-005, 6e-005, 0.00022, 0.00022, 0.00022,
                            #     0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.00022,
                            #     0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.00022,
                            #     0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.00027, 0.00027, 0.00027,
                            #     0.00027, 0.00027, 0.00027, 0.00027, 0.00027, 0.00027, 0.00027, 0.00027, 0.00027, 0.00027,
                            #     0.00027, 0.00027, 0.00027, 0.00027, 0.00027, 0.00027, 0.00027, 0.00027, 0.00027, 0.00027,
                            #     0.00027, 0.00027, 0.00027, 0.00027, 0.00027, 0.00027, 0.00027, 0.00021, 0.00021, 0.00021,
                            #     0.00021, 0.00021, 0.00021, 0.00021, 0.00021, 0.00021, 0.00021, 0.00021, 0.00021, 0.00021,
                            #     0.00021, 0.00021, 0.00021, 0.00021, 0.00021, 0.00021, 0.00021, 0.00021, 0.00021, 0.00021,
                            #     0.00021, 0.00021, 0.00021, 0.00021, 0.00021, 0.00021, 0.00021, 0.00013, 0.00013, 0.00013,
                            #     0.00013, 0.00013, 0.00013, 0.00013, 0.00013, 0.00013, 0.00013, 0.00013, 0.00013, 0.00013,
                            #     0.00013, 0.00013, 0.00013, 0.00013, 0.00013, 0.00013, 0.00013, 0.00013, 0.00013, 0.00013,
                            #     0.00013, 0.00013, 0.00013, 0.00013, 0.00013, 0.00013, 0.00013, 0.00013, 0.00013, 0.00013,
                            #     0.00013, 0.00013
                            # ]
                            )


@cache('step')
def zr_agri_dem():
    """
    Real Name: b'zr agri dem'
    Original Eqn: b'apple zr(Time)+citrus zr(Time)+rapeseed zr(Time)+rice zr(Time)'
    Units: b'MCM'
    Limits: (None, None)
    Type: component

    b''
    """
    return apple_zr(time()) + citrus_zr(time()) + rapeseed_zr(time()) + rice_zr(time())


@cache('step')
def zr_agri_sup():
    """
    Real Name: b'zr agri sup'
    Original Eqn: b'MIN((zr agri dem *agri zr dam coef), (Zr outflow-zr Dim sup-zr wr sup-zr Env sup-zr Ind sup\\\\ ) )'
    Units: b'MCM'
    Limits: (None, None)
    Type: component

    b''
    """
    return np.minimum((zr_agri_dem() * agri_zr_dam_coef()),
                      (zr_outflow() - zr_dim_sup() - zr_wr_sup() - zr_env_sup() - zr_ind_sup()))


def citrus_zr(x):
    """
    Real Name: b'citrus zr'
    Original Eqn: b'( [(1,0)-(365,0.04)],(1,0.00474),(2,0.00474),(3,0.00474),(4,0.00474),(5,0.00474),(6,0.00474\\\\ ),(7,0.00474),(8,0.00474),(9,0.00474),(10,0.00474),(11,0.00474),(12,0.00474),(13,0.00474\\\\ ),(14,0.00474),(15,0.00474),(16,0.00474),(17,0.00474),(18,0.00474),(19,0.00474),(20\\\\ ,0.00474),(21,0.00474),(22,0.00474),(23,0.00474),(24,0.00474),(25,0.00474),(26,0.00474\\\\ ),(27,0.00474),(28,0.00474),(29,0.00474),(30,0.00474),(31,0),(32,0),(33,0),(34,0),(\\\\ 35,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),\\\\ (47,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0)\\\\ ,(59,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0\\\\ ),(71,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,\\\\ 0),(83,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94\\\\ ,0),(95,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105\\\\ ,0),(106,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0)\\\\ ,(116,0),(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126\\\\ ,0),(127,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0)\\\\ ,(137,0),(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147\\\\ ,0),(148,0),(149,0),(150,0),(151,0),(152,0),(153,0),(154,0),(155,0),(156,0),(157,0)\\\\ ,(158,0),(159,0),(160,0),(161,0),(162,0),(163,0),(164,0),(165,0),(166,0),(167,0),(168\\\\ ,0),(169,0),(170,0),(171,0),(172,0),(173,0),(174,0),(175,0),(176,0),(177,0),(178,0)\\\\ ,(179,0),(180,0),(181,0.03133),(182,0.03133),(183,0.03133),(184,0.03133),(185,0.03133\\\\ ),(186,0.03133),(187,0.03133),(188,0.03133),(189,0.03133),(190,0.03133),(191,0.03133\\\\ ),(192,0.03133),(193,0.03133),(194,0.03133),(195,0.03133),(196,0.03133),(197,0.03133\\\\ ),(198,0.03133),(199,0.03133),(200,0.03133),(201,0.03133),(202,0.03133),(203,0.03133\\\\ ),(204,0.03133),(205,0.03133),(206,0.03133),(207,0.03133),(208,0.03133),(209,0.03133\\\\ ),(210,0.03133),(211,0.01849),(212,0.01849),(213,0.01849),(214,0.01849),(215,0.01849\\\\ ),(216,0.01849),(217,0.01849),(218,0.01849),(219,0.01849),(220,0.01849),(221,0.01849\\\\ ),(222,0.01849),(223,0.01849),(224,0.01849),(225,0.01849),(226,0.01849),(227,0.01849\\\\ ),(228,0.01849),(229,0.01849),(230,0.01849),(231,0.01849),(232,0.01849),(233,0.01849\\\\ ),(234,0.01849),(235,0.01849),(236,0.01849),(237,0.01849),(238,0.01849),(239,0.01849\\\\ ),(240,0.01849),(241,0.02193),(242,0.02193),(243,0.02193),(244,0.02193),(245,0.02193\\\\ ),(246,0.02193),(247,0.02193),(248,0.02193),(249,0.02193),(250,0.02193),(251,0.02193\\\\ ),(252,0.02193),(253,0.02193),(254,0.02193),(255,0.02193),(256,0.02193),(257,0.02193\\\\ ),(258,0.02193),(259,0.02193),(260,0.02193),(261,0.02193),(262,0.02193),(263,0.02193\\\\ ),(264,0.02193),(265,0.02193),(266,0.02193),(267,0.02193),(268,0.02193),(269,0.02193\\\\ ),(270,0.02193),(271,0.01867),(272,0.01867),(273,0.01867),(274,0.01867),(275,0.01867\\\\ ),(276,0.01867),(277,0.01867),(278,0.01867),(279,0.01867),(280,0.01867),(281,0.01867\\\\ ),(282,0.01867),(283,0.01867),(284,0.01867),(285,0.01867),(286,0.01867),(287,0.01867\\\\ ),(288,0.01867),(289,0.01867),(290,0.01867),(291,0.01867),(292,0.01867),(293,0.01867\\\\ ),(294,0.01867),(295,0.01867),(296,0.01867),(297,0.01867),(298,0.01867),(299,0.01867\\\\ ),(300,0.01867),(301,0.01386),(302,0.01386),(303,0.01386),(304,0.01386),(305,0.01386\\\\ ),(306,0.01386),(307,0.01386),(308,0.01386),(309,0.01386),(310,0.01386),(311,0.01386\\\\ ),(312,0.01386),(313,0.01386),(314,0.01386),(315,0.01386),(316,0.01386),(317,0.01386\\\\ ),(318,0.01386),(319,0.01386),(320,0.01386),(321,0.01386),(322,0.01386),(323,0.01386\\\\ ),(324,0.01386),(325,0.01386),(326,0.01386),(327,0.01386),(328,0.01386),(329,0.01386\\\\ ),(330,0.01386),(331,0.01012),(332,0.01012),(333,0.01012),(334,0.01012),(335,0.01012\\\\ ),(336,0.01012),(337,0.01012),(338,0.01012),(339,0.01012),(340,0.01012),(341,0.01012\\\\ ),(342,0.01012),(343,0.01012),(344,0.01012),(345,0.01012),(346,0.01012),(347,0.01012\\\\ ),(348,0.01012),(349,0.01012),(350,0.01012),(351,0.01012),(352,0.01012),(353,0.01012\\\\ ),(354,0.01012),(355,0.01012),(356,0.01012),(357,0.01012),(358,0.01012),(359,0.01012\\\\ ),(360,0.01012),(361,0.01012),(362,0.01012),(363,0.01012),(364,0.01012),(365,0.01012\\\\ ))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], lookups_data["citrus_zr"]
                            # [
                            #     0.00474, 0.00474, 0.00474, 0.00474, 0.00474, 0.00474, 0.00474, 0.00474, 0.00474,
                            #     0.00474,
                            #     0.00474, 0.00474, 0.00474, 0.00474, 0.00474, 0.00474, 0.00474, 0.00474, 0.00474,
                            #     0.00474,
                            #     0.00474, 0.00474, 0.00474, 0.00474, 0.00474, 0.00474, 0.00474, 0.00474, 0.00474,
                            #     0.00474,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0.03133, 0.03133, 0.03133, 0.03133, 0.03133, 0.03133, 0.03133, 0.03133, 0.03133,
                            #     0.03133,
                            #     0.03133, 0.03133, 0.03133, 0.03133, 0.03133, 0.03133, 0.03133, 0.03133, 0.03133,
                            #     0.03133,
                            #     0.03133, 0.03133, 0.03133, 0.03133, 0.03133, 0.03133, 0.03133, 0.03133, 0.03133,
                            #     0.03133,
                            #     0.01849, 0.01849, 0.01849, 0.01849, 0.01849, 0.01849, 0.01849, 0.01849, 0.01849,
                            #     0.01849,
                            #     0.01849, 0.01849, 0.01849, 0.01849, 0.01849, 0.01849, 0.01849, 0.01849, 0.01849,
                            #     0.01849,
                            #     0.01849, 0.01849, 0.01849, 0.01849, 0.01849, 0.01849, 0.01849, 0.01849, 0.01849,
                            #     0.01849,
                            #     0.02193, 0.02193, 0.02193, 0.02193, 0.02193, 0.02193, 0.02193, 0.02193, 0.02193,
                            #     0.02193,
                            #     0.02193, 0.02193, 0.02193, 0.02193, 0.02193, 0.02193, 0.02193, 0.02193, 0.02193,
                            #     0.02193,
                            #     0.02193, 0.02193, 0.02193, 0.02193, 0.02193, 0.02193, 0.02193, 0.02193, 0.02193,
                            #     0.02193,
                            #     0.01867, 0.01867, 0.01867, 0.01867, 0.01867, 0.01867, 0.01867, 0.01867, 0.01867,
                            #     0.01867,
                            #     0.01867, 0.01867, 0.01867, 0.01867, 0.01867, 0.01867, 0.01867, 0.01867, 0.01867,
                            #     0.01867,
                            #     0.01867, 0.01867, 0.01867, 0.01867, 0.01867, 0.01867, 0.01867, 0.01867, 0.01867,
                            #     0.01867,
                            #     0.01386, 0.01386, 0.01386, 0.01386, 0.01386, 0.01386, 0.01386, 0.01386, 0.01386,
                            #     0.01386,
                            #     0.01386, 0.01386, 0.01386, 0.01386, 0.01386, 0.01386, 0.01386, 0.01386, 0.01386,
                            #     0.01386,
                            #     0.01386, 0.01386, 0.01386, 0.01386, 0.01386, 0.01386, 0.01386, 0.01386, 0.01386,
                            #     0.01386,
                            #     0.01012, 0.01012, 0.01012, 0.01012, 0.01012, 0.01012, 0.01012, 0.01012, 0.01012,
                            #     0.01012,
                            #     0.01012, 0.01012, 0.01012, 0.01012, 0.01012, 0.01012, 0.01012, 0.01012, 0.01012,
                            #     0.01012,
                            #     0.01012, 0.01012, 0.01012, 0.01012, 0.01012, 0.01012, 0.01012, 0.01012, 0.01012,
                            #     0.01012,
                            #     0.01012, 0.01012, 0.01012, 0.01012, 0.01012
                            # ]
                            )


@cache('step')
def tj_agri_sup():
    """
    Real Name: b'Tj Agri Sup'
    Original Eqn: b'MIN(Tj Agri Dem *Agri Tajan Dam Coef, (Tj Outflow-Tj Dom Sup-Tj Env Sup-Tj Ind Sup))'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return np.minimum(tj_agri_dem() * agri_tajan_dam_coef(),
                      (tj_outflow() - tj_dom_sup() - tj_env_sup() - tj_ind_sup()))


@cache('step')
def tj_total_demand():
    """
    Real Name: b'Tj Total Demand'
    Original Eqn: b'Tj Dom Dem (Time)+Tj Ind Dem (Time)+(Tj Agri Dem *Agri Tajan Dam Coef)+Tj Env Dem (Time\\\\ )'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return tj_dom_dem(time()) + tj_ind_dem(
        time()) + (tj_agri_dem() * agri_tajan_dam_coef()) + tj_env_dem(time())


def rice_zr(x):
    """
    Real Name: b'rice zr'
    Original Eqn: b'( [(1,0)-(365,0.4)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0\\\\ ),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23,\\\\ 0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35\\\\ ,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47\\\\ ,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94,0),(95\\\\ ,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105,0),(106\\\\ ,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0),(116,0)\\\\ ,(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126,0),(127\\\\ ,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0),(137,0)\\\\ ,(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147,0),(148\\\\ ,0),(149,0),(150,0),(151,0),(152,0),(153,0),(154,0),(155,0),(156,0),(157,0),(158,0)\\\\ ,(159,0),(160,0),(161,0),(162,0),(163,0),(164,0),(165,0),(166,0),(167,0),(168,0),(169\\\\ ,0),(170,0),(171,0),(172,0),(173,0),(174,0),(175,0),(176,0),(177,0),(178,0),(179,0)\\\\ ,(180,0),(181,0),(182,0),(183,0),(184,0),(185,0),(186,0),(187,0),(188,0),(189,0),(190\\\\ ,0),(191,0),(192,0),(193,0),(194,0),(195,0),(196,0),(197,0),(198,0),(199,0),(200,0)\\\\ ,(201,0),(202,0),(203,0),(204,0),(205,0),(206,0),(207,0),(208,0),(209,0),(210,0),(211\\\\ ,0.35),(212,0.35),(213,0.35),(214,0.35),(215,0.35),(216,0.35),(217,0.35),(218,0.35)\\\\ ,(219,0.35),(220,0.35),(221,0.35),(222,0.35),(223,0.35),(224,0.35),(225,0.35),(226,\\\\ 0.35),(227,0.35),(228,0.35),(229,0.35),(230,0.35),(231,0.35),(232,0.35),(233,0.35),\\\\ (234,0.35),(235,0.35),(236,0.35),(237,0.35),(238,0.35),(239,0.35),(240,0.35),(241,0.38\\\\ ),(242,0.38),(243,0.38),(244,0.38),(245,0.38),(246,0.38),(247,0.38),(248,0.38),(249\\\\ ,0.38),(250,0.38),(251,0.38),(252,0.38),(253,0.38),(254,0.38),(255,0.38),(256,0.38)\\\\ ,(257,0.38),(258,0.38),(259,0.38),(260,0.38),(261,0.38),(262,0.38),(263,0.38),(264,\\\\ 0.38),(265,0.38),(266,0.38),(267,0.38),(268,0.38),(269,0.38),(270,0.38),(271,0.3),(\\\\ 272,0.3),(273,0.3),(274,0.3),(275,0.3),(276,0.3),(277,0.3),(278,0.3),(279,0.3),(280\\\\ ,0.3),(281,0.3),(282,0.3),(283,0.3),(284,0.3),(285,0.3),(286,0.3),(287,0.3),(288,0.3\\\\ ),(289,0.3),(290,0.3),(291,0.3),(292,0.3),(293,0.3),(294,0.3),(295,0.3),(296,0.3),(\\\\ 297,0.3),(298,0.3),(299,0.3),(300,0.3),(301,0.22),(302,0.22),(303,0.22),(304,0.22),\\\\ (305,0.22),(306,0.22),(307,0.22),(308,0.22),(309,0.22),(310,0.22),(311,0.22),(312,0.22\\\\ ),(313,0.22),(314,0.22),(315,0.22),(316,0.22),(317,0.22),(318,0.22),(319,0.22),(320\\\\ ,0.22),(321,0.22),(322,0.22),(323,0.22),(324,0.22),(325,0.22),(326,0.22),(327,0.22)\\\\ ,(328,0.22),(329,0.22),(330,0.22),(331,0.06),(332,0.06),(333,0.06),(334,0.06),(335,\\\\ 0.06),(336,0.06),(337,0.06),(338,0.06),(339,0.06),(340,0.06),(341,0.06),(342,0.06),\\\\ (343,0.06),(344,0.06),(345,0.06),(346,0.06),(347,0.06),(348,0.06),(349,0.06),(350,0.06\\\\ ),(351,0.06),(352,0.06),(353,0.06),(354,0.06),(355,0.06),(356,0.06),(357,0.06),(358\\\\ ,0.06),(359,0.06),(360,0.06),(361,0.06),(362,0.06),(363,0.06),(364,0.06),(365,0.06)\\\\ )'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], lookups_data["rice_zr"]
                            # [
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35,
                            #     0.35,
                            #     0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35,
                            #     0.35,
                            #     0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38,
                            #     0.38,
                            #     0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38,
                            #     0.38,
                            #     0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
                            #     0.3,
                            #     0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.22, 0.22, 0.22, 0.22,
                            #     0.22,
                            #     0.22, 0.22, 0.22, 0.22, 0.22, 0.22, 0.22, 0.22, 0.22, 0.22, 0.22, 0.22, 0.22, 0.22,
                            #     0.22,
                            #     0.22, 0.22, 0.22, 0.22, 0.22, 0.22, 0.22, 0.22, 0.22, 0.22, 0.06, 0.06, 0.06, 0.06,
                            #     0.06,
                            #     0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06,
                            #     0.06,
                            #     0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06
                            # ]
                            )


@cache('step')
def supply_agricul1finesk():
    """
    Real Name: b'"supply Agricul-1Finesk"'
    Original Eqn: b'MIN("Agricul-1Demand finesk", (outflow Finesk -"Supply Domes-1Finesk"-Supply envi Finesk\\\\ ))'
    Units: b'MCM'
    Limits: (None, None)
    Type: component

    b''
    """
    return np.minimum(agricul1demand_finesk(),
                      (outflow_finesk() - supply_domes1finesk() - supply_envi_finesk()))


def apple_tj(x):
    """
    Real Name: b'apple Tj'
    Original Eqn: b'( [(1,0)-(365,0.2)],(1,0.02985),(2,0.02985),(3,0.02985),(4,0.02985),(5,0.02985),(6,0.02985\\\\ ),(7,0.02985),(8,0.02985),(9,0.02985),(10,0.02985),(11,0.02985),(12,0.02985),(13,0.02985\\\\ ),(14,0.02985),(15,0.02985),(16,0.02985),(17,0.02985),(18,0.02985),(19,0.02985),(20\\\\ ,0.02985),(21,0.02985),(22,0.02985),(23,0.02985),(24,0.02985),(25,0.02985),(26,0.02985\\\\ ),(27,0.02985),(28,0.02985),(29,0.02985),(30,0.02985),(31,0),(32,0),(33,0),(34,0),(\\\\ 35,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),\\\\ (47,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0)\\\\ ,(59,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0\\\\ ),(71,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,\\\\ 0),(83,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94\\\\ ,0),(95,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105\\\\ ,0),(106,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0)\\\\ ,(116,0),(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126\\\\ ,0),(127,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0)\\\\ ,(137,0),(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147\\\\ ,0),(148,0),(149,0),(150,0),(151,0),(152,0),(153,0),(154,0),(155,0),(156,0),(157,0)\\\\ ,(158,0),(159,0),(160,0),(161,0),(162,0),(163,0),(164,0),(165,0),(166,0),(167,0),(168\\\\ ,0),(169,0),(170,0),(171,0),(172,0),(173,0),(174,0),(175,0),(176,0),(177,0),(178,0)\\\\ ,(179,0),(180,0),(181,0),(182,0),(183,0),(184,0),(185,0),(186,0),(187,0),(188,0),(189\\\\ ,0),(190,0),(191,0),(192,0),(193,0),(194,0),(195,0),(196,0),(197,0),(198,0),(199,0)\\\\ ,(200,0),(201,0),(202,0),(203,0),(204,0),(205,0),(206,0),(207,0),(208,0),(209,0),(210\\\\ ,0),(211,0.04676),(212,0.04676),(213,0.04676),(214,0.04676),(215,0.04676),(216,0.04676\\\\ ),(217,0.04676),(218,0.04676),(219,0.04676),(220,0.04676),(221,0.04676),(222,0.04676\\\\ ),(223,0.04676),(224,0.04676),(225,0.04676),(226,0.04676),(227,0.04676),(228,0.04676\\\\ ),(229,0.04676),(230,0.04676),(231,0.04676),(232,0.04676),(233,0.04676),(234,0.04676\\\\ ),(235,0.04676),(236,0.04676),(237,0.04676),(238,0.04676),(239,0.04676),(240,0.04676\\\\ ),(241,0.07893),(242,0.07893),(243,0.07893),(244,0.07893),(245,0.07893),(246,0.07893\\\\ ),(247,0.07893),(248,0.07893),(249,0.07893),(250,0.07893),(251,0.07893),(252,0.07893\\\\ ),(253,0.07893),(254,0.07893),(255,0.07893),(256,0.07893),(257,0.07893),(258,0.07893\\\\ ),(259,0.07893),(260,0.07893),(261,0.07893),(262,0.07893),(263,0.07893),(264,0.07893\\\\ ),(265,0.07893),(266,0.07893),(267,0.07893),(268,0.07893),(269,0.07893),(270,0.07893\\\\ ),(271,0.12202),(272,0.12202),(273,0.12202),(274,0.12202),(275,0.12202),(276,0.12202\\\\ ),(277,0.12202),(278,0.12202),(279,0.12202),(280,0.12202),(281,0.12202),(282,0.12202\\\\ ),(283,0.12202),(284,0.12202),(285,0.12202),(286,0.12202),(287,0.12202),(288,0.12202\\\\ ),(289,0.12202),(290,0.12202),(291,0.12202),(292,0.12202),(293,0.12202),(294,0.12202\\\\ ),(295,0.12202),(296,0.12202),(297,0.12202),(298,0.12202),(299,0.12202),(300,0.12202\\\\ ),(301,0.11619),(302,0.11619),(303,0.11619),(304,0.11619),(305,0.11619),(306,0.11619\\\\ ),(307,0.11619),(308,0.11619),(309,0.11619),(310,0.11619),(311,0.11619),(312,0.11619\\\\ ),(313,0.11619),(314,0.11619),(315,0.11619),(316,0.11619),(317,0.11619),(318,0.11619\\\\ ),(319,0.11619),(320,0.11619),(321,0.11619),(322,0.11619),(323,0.11619),(324,0.11619\\\\ ),(325,0.11619),(326,0.11619),(327,0.11619),(328,0.11619),(329,0.11619),(330,0.11619\\\\ ),(331,0.10953),(332,0.10953),(333,0.10953),(334,0.10953),(335,0.10953),(336,0.10953\\\\ ),(337,0.10953),(338,0.10953),(339,0.10953),(340,0.10953),(341,0.10953),(342,0.10953\\\\ ),(343,0.10953),(344,0.10953),(345,0.10953),(346,0.10953),(347,0.10953),(348,0.10953\\\\ ),(349,0.10953),(350,0.10953),(351,0.10953),(352,0.10953),(353,0.10953),(354,0.10953\\\\ ),(355,0.10953),(356,0.10953),(357,0.10953),(358,0.10953),(359,0.10953),(360,0.10953\\\\ ),(361,0.10953),(362,0.10953),(363,0.10953),(364,0.10953),(365,0.10953))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b'second priority'
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], lookups_data["apple_tj"]
                            # [
                            #     0.02985, 0.02985, 0.02985, 0.02985, 0.02985, 0.02985, 0.02985, 0.02985, 0.02985,
                            #     0.02985,
                            #     0.02985, 0.02985, 0.02985, 0.02985, 0.02985, 0.02985, 0.02985, 0.02985, 0.02985,
                            #     0.02985,
                            #     0.02985, 0.02985, 0.02985, 0.02985, 0.02985, 0.02985, 0.02985, 0.02985, 0.02985,
                            #     0.02985,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0.04676, 0.04676, 0.04676, 0.04676, 0.04676, 0.04676, 0.04676, 0.04676, 0.04676,
                            #     0.04676,
                            #     0.04676, 0.04676, 0.04676, 0.04676, 0.04676, 0.04676, 0.04676, 0.04676, 0.04676,
                            #     0.04676,
                            #     0.04676, 0.04676, 0.04676, 0.04676, 0.04676, 0.04676, 0.04676, 0.04676, 0.04676,
                            #     0.04676,
                            #     0.07893, 0.07893, 0.07893, 0.07893, 0.07893, 0.07893, 0.07893, 0.07893, 0.07893,
                            #     0.07893,
                            #     0.07893, 0.07893, 0.07893, 0.07893, 0.07893, 0.07893, 0.07893, 0.07893, 0.07893,
                            #     0.07893,
                            #     0.07893, 0.07893, 0.07893, 0.07893, 0.07893, 0.07893, 0.07893, 0.07893, 0.07893,
                            #     0.07893,
                            #     0.12202, 0.12202, 0.12202, 0.12202, 0.12202, 0.12202, 0.12202, 0.12202, 0.12202,
                            #     0.12202,
                            #     0.12202, 0.12202, 0.12202, 0.12202, 0.12202, 0.12202, 0.12202, 0.12202, 0.12202,
                            #     0.12202,
                            #     0.12202, 0.12202, 0.12202, 0.12202, 0.12202, 0.12202, 0.12202, 0.12202, 0.12202,
                            #     0.12202,
                            #     0.11619, 0.11619, 0.11619, 0.11619, 0.11619, 0.11619, 0.11619, 0.11619, 0.11619,
                            #     0.11619,
                            #     0.11619, 0.11619, 0.11619, 0.11619, 0.11619, 0.11619, 0.11619, 0.11619, 0.11619,
                            #     0.11619,
                            #     0.11619, 0.11619, 0.11619, 0.11619, 0.11619, 0.11619, 0.11619, 0.11619, 0.11619,
                            #     0.11619,
                            #     0.10953, 0.10953, 0.10953, 0.10953, 0.10953, 0.10953, 0.10953, 0.10953, 0.10953,
                            #     0.10953,
                            #     0.10953, 0.10953, 0.10953, 0.10953, 0.10953, 0.10953, 0.10953, 0.10953, 0.10953,
                            #     0.10953,
                            #     0.10953, 0.10953, 0.10953, 0.10953, 0.10953, 0.10953, 0.10953, 0.10953, 0.10953,
                            #     0.10953,
                            #     0.10953, 0.10953, 0.10953, 0.10953, 0.10953
                            # ]
                            )


@cache('step')
def tj_agri_dem():
    """
    Real Name: b'Tj Agri Dem'
    Original Eqn: b'apple Tj(Time)+Citrs Tj(Time)+Rapeseed Tj(Time)+Rice Tj(Time)+tomato Tj(Time)+wheat Tj\\\\ (Time)'
    Units: b'MCM/Month'
    Limits: (None, None)
    Type: component

    b''
    """
    return apple_tj(time()) + citrs_tj(time()) + rapeseed_tj(time()) + rice_tj(time()) + tomato_tj(
        time()) + wheat_tj(time())


def tomato_tj(x):
    """
    Real Name: b'tomato Tj'
    Original Eqn: b'( [(1,0)-(365,0.002)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11\\\\ ,0),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23\\\\ ,0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35\\\\ ,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47\\\\ ,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94,0),(95\\\\ ,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105,0),(106\\\\ ,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0),(116,0)\\\\ ,(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126,0),(127\\\\ ,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0),(137,0)\\\\ ,(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147,0),(148\\\\ ,0),(149,0),(150,0),(151,0),(152,0),(153,0),(154,0),(155,0),(156,0),(157,0),(158,0)\\\\ ,(159,0),(160,0),(161,0),(162,0),(163,0),(164,0),(165,0),(166,0),(167,0),(168,0),(169\\\\ ,0),(170,0),(171,0),(172,0),(173,0),(174,0),(175,0),(176,0),(177,0),(178,0),(179,0)\\\\ ,(180,0),(181,0),(182,0),(183,0),(184,0),(185,0),(186,0),(187,0),(188,0),(189,0),(190\\\\ ,0),(191,0),(192,0),(193,0),(194,0),(195,0),(196,0),(197,0),(198,0),(199,0),(200,0)\\\\ ,(201,0),(202,0),(203,0),(204,0),(205,0),(206,0),(207,0),(208,0),(209,0),(210,0),(211\\\\ ,0.00023),(212,0.00023),(213,0.00023),(214,0.00023),(215,0.00023),(216,0.00023),(217\\\\ ,0.00023),(218,0.00023),(219,0.00023),(220,0.00023),(221,0.00023),(222,0.00023),(223\\\\ ,0.00023),(224,0.00023),(225,0.00023),(226,0.00023),(227,0.00023),(228,0.00023),(229\\\\ ,0.00023),(230,0.00023),(231,0.00023),(232,0.00023),(233,0.00023),(234,0.00023),(235\\\\ ,0.00023),(236,0.00023),(237,0.00023),(238,0.00023),(239,0.00023),(240,0.00023),(241\\\\ ,0.00059),(242,0.00059),(243,0.00059),(244,0.00059),(245,0.00059),(246,0.00059),(247\\\\ ,0.00059),(248,0.00059),(249,0.00059),(250,0.00059),(251,0.00059),(252,0.00059),(253\\\\ ,0.00059),(254,0.00059),(255,0.00059),(256,0.00059),(257,0.00059),(258,0.00059),(259\\\\ ,0.00059),(260,0.00059),(261,0.00059),(262,0.00059),(263,0.00059),(264,0.00059),(265\\\\ ,0.00059),(266,0.00059),(267,0.00059),(268,0.00059),(269,0.00059),(270,0.00059),(271\\\\ ,0.00112),(272,0.00112),(273,0.00112),(274,0.00112),(275,0.00112),(276,0.00112),(277\\\\ ,0.00112),(278,0.00112),(279,0.00112),(280,0.00112),(281,0.00112),(282,0.00112),(283\\\\ ,0.00112),(284,0.00112),(285,0.00112),(286,0.00112),(287,0.00112),(288,0.00112),(289\\\\ ,0.00112),(290,0.00112),(291,0.00112),(292,0.00112),(293,0.00112),(294,0.00112),(295\\\\ ,0.00112),(296,0.00112),(297,0.00112),(298,0.00112),(299,0.00112),(300,0.00112),(301\\\\ ,0.00113),(302,0.00113),(303,0.00113),(304,0.00113),(305,0.00113),(306,0.00113),(307\\\\ ,0.00113),(308,0.00113),(309,0.00113),(310,0.00113),(311,0.00113),(312,0.00113),(313\\\\ ,0.00113),(314,0.00113),(315,0.00113),(316,0.00113),(317,0.00113),(318,0.00113),(319\\\\ ,0.00113),(320,0.00113),(321,0.00113),(322,0.00113),(323,0.00113),(324,0.00113),(325\\\\ ,0.00113),(326,0.00113),(327,0.00113),(328,0.00113),(329,0.00113),(330,0.00113),(331\\\\ ,0.00079),(332,0.00079),(333,0.00079),(334,0.00079),(335,0.00079),(336,0.00079),(337\\\\ ,0.00079),(338,0.00079),(339,0.00079),(340,0.00079),(341,0.00079),(342,0.00079),(343\\\\ ,0.00079),(344,0.00079),(345,0.00079),(346,0.00079),(347,0.00079),(348,0.00079),(349\\\\ ,0.00079),(350,0.00079),(351,0.00079),(352,0.00079),(353,0.00079),(354,0.00079),(355\\\\ ,0.00079),(356,0.00079),(357,0.00079),(358,0.00079),(359,0.00079),(360,0.00079),(361\\\\ ,0.00079),(362,0.00079),(363,0.00079),(364,0.00079),(365,0.00079))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b'forth priority'
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], lookups_data["tomato_tj"]
                            # [
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0.00023, 0.00023, 0.00023, 0.00023, 0.00023, 0.00023, 0.00023, 0.00023, 0.00023,
                            #     0.00023,
                            #     0.00023, 0.00023, 0.00023, 0.00023, 0.00023, 0.00023, 0.00023, 0.00023, 0.00023,
                            #     0.00023,
                            #     0.00023, 0.00023, 0.00023, 0.00023, 0.00023, 0.00023, 0.00023, 0.00023, 0.00023,
                            #     0.00023,
                            #     0.00059, 0.00059, 0.00059, 0.00059, 0.00059, 0.00059, 0.00059, 0.00059, 0.00059,
                            #     0.00059,
                            #     0.00059, 0.00059, 0.00059, 0.00059, 0.00059, 0.00059, 0.00059, 0.00059, 0.00059,
                            #     0.00059,
                            #     0.00059, 0.00059, 0.00059, 0.00059, 0.00059, 0.00059, 0.00059, 0.00059, 0.00059,
                            #     0.00059,
                            #     0.00112, 0.00112, 0.00112, 0.00112, 0.00112, 0.00112, 0.00112, 0.00112, 0.00112,
                            #     0.00112,
                            #     0.00112, 0.00112, 0.00112, 0.00112, 0.00112, 0.00112, 0.00112, 0.00112, 0.00112,
                            #     0.00112,
                            #     0.00112, 0.00112, 0.00112, 0.00112, 0.00112, 0.00112, 0.00112, 0.00112, 0.00112,
                            #     0.00112,
                            #     0.00113, 0.00113, 0.00113, 0.00113, 0.00113, 0.00113, 0.00113, 0.00113, 0.00113,
                            #     0.00113,
                            #     0.00113, 0.00113, 0.00113, 0.00113, 0.00113, 0.00113, 0.00113, 0.00113, 0.00113,
                            #     0.00113,
                            #     0.00113, 0.00113, 0.00113, 0.00113, 0.00113, 0.00113, 0.00113, 0.00113, 0.00113,
                            #     0.00113,
                            #     0.00079, 0.00079, 0.00079, 0.00079, 0.00079, 0.00079, 0.00079, 0.00079, 0.00079,
                            #     0.00079,
                            #     0.00079, 0.00079, 0.00079, 0.00079, 0.00079, 0.00079, 0.00079, 0.00079, 0.00079,
                            #     0.00079,
                            #     0.00079, 0.00079, 0.00079, 0.00079, 0.00079, 0.00079, 0.00079, 0.00079, 0.00079,
                            #     0.00079,
                            #     0.00079, 0.00079, 0.00079, 0.00079, 0.00079
                            # ]
                            )


def rapeseed_tj(x):
    """
    Real Name: b'Rapeseed Tj'
    Original Eqn: b'( [(1,0)-(365,0.0002)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11\\\\ ,0),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23\\\\ ,0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35\\\\ ,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47\\\\ ,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94,0),(95\\\\ ,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105,0),(106\\\\ ,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0),(116,0)\\\\ ,(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126,0),(127\\\\ ,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0),(137,0)\\\\ ,(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147,0),(148\\\\ ,0),(149,0),(150,0),(151,0),(152,0),(153,0),(154,0),(155,0),(156,0),(157,0),(158,0)\\\\ ,(159,0),(160,0),(161,0),(162,0),(163,0),(164,0),(165,0),(166,0),(167,0),(168,0),(169\\\\ ,0),(170,0),(171,0),(172,0),(173,0),(174,0),(175,0),(176,0),(177,0),(178,0),(179,0)\\\\ ,(180,0),(181,0),(182,0),(183,0),(184,0),(185,0),(186,0),(187,0),(188,0),(189,0),(190\\\\ ,0),(191,0),(192,0),(193,0),(194,0),(195,0),(196,0),(197,0),(198,0),(199,0),(200,0)\\\\ ,(201,0),(202,0),(203,0),(204,0),(205,0),(206,0),(207,0),(208,0),(209,0),(210,0),(211\\\\ ,2e-005),(212,2e-005),(213,2e-005),(214,2e-005),(215,2e-005),(216,2e-005),(217,2e-005\\\\ ),(218,2e-005),(219,2e-005),(220,2e-005),(221,2e-005),(222,2e-005),(223,2e-005),(224\\\\ ,2e-005),(225,2e-005),(226,2e-005),(227,2e-005),(228,2e-005),(229,2e-005),(230,2e-005\\\\ ),(231,2e-005),(232,2e-005),(233,2e-005),(234,2e-005),(235,2e-005),(236,2e-005),(237\\\\ ,2e-005),(238,2e-005),(239,2e-005),(240,2e-005),(241,8e-005),(242,8e-005),(243,8e-005\\\\ ),(244,8e-005),(245,8e-005),(246,8e-005),(247,8e-005),(248,8e-005),(249,8e-005),(250\\\\ ,8e-005),(251,8e-005),(252,8e-005),(253,8e-005),(254,8e-005),(255,8e-005),(256,8e-005\\\\ ),(257,8e-005),(258,8e-005),(259,8e-005),(260,8e-005),(261,8e-005),(262,8e-005),(263\\\\ ,8e-005),(264,8e-005),(265,8e-005),(266,8e-005),(267,8e-005),(268,8e-005),(269,8e-005\\\\ ),(270,8e-005),(271,0.00013),(272,0.00013),(273,0.00013),(274,0.00013),(275,0.00013\\\\ ),(276,0.00013),(277,0.00013),(278,0.00013),(279,0.00013),(280,0.00013),(281,0.00013\\\\ ),(282,0.00013),(283,0.00013),(284,0.00013),(285,0.00013),(286,0.00013),(287,0.00013\\\\ ),(288,0.00013),(289,0.00013),(290,0.00013),(291,0.00013),(292,0.00013),(293,0.00013\\\\ ),(294,0.00013),(295,0.00013),(296,0.00013),(297,0.00013),(298,0.00013),(299,0.00013\\\\ ),(300,0.00013),(301,0.00011),(302,0.00011),(303,0.00011),(304,0.00011),(305,0.00011\\\\ ),(306,0.00011),(307,0.00011),(308,0.00011),(309,0.00011),(310,0.00011),(311,0.00011\\\\ ),(312,0.00011),(313,0.00011),(314,0.00011),(315,0.00011),(316,0.00011),(317,0.00011\\\\ ),(318,0.00011),(319,0.00011),(320,0.00011),(321,0.00011),(322,0.00011),(323,0.00011\\\\ ),(324,0.00011),(325,0.00011),(326,0.00011),(327,0.00011),(328,0.00011),(329,0.00011\\\\ ),(330,0.00011),(331,7e-005),(332,7e-005),(333,7e-005),(334,7e-005),(335,7e-005),(336\\\\ ,7e-005),(337,7e-005),(338,7e-005),(339,7e-005),(340,7e-005),(341,7e-005),(342,7e-005\\\\ ),(343,7e-005),(344,7e-005),(345,7e-005),(346,7e-005),(347,7e-005),(348,7e-005),(349\\\\ ,7e-005),(350,7e-005),(351,7e-005),(352,7e-005),(353,7e-005),(354,7e-005),(355,7e-005\\\\ ),(356,7e-005),(357,7e-005),(358,7e-005),(359,7e-005),(360,7e-005),(361,7e-005),(362\\\\ ,7e-005),(363,7e-005),(364,7e-005),(365,7e-005))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b'sixth priority'
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], lookups_data["rapeseed_tj"]
                            # [
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005,
                            #     2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005,
                            #     2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 8e-005, 8e-005, 8e-005,
                            #     8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005,
                            #     8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005,
                            #     8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 0.00013, 0.00013, 0.00013, 0.00013, 0.00013,
                            #     0.00013, 0.00013, 0.00013, 0.00013, 0.00013, 0.00013, 0.00013, 0.00013, 0.00013,
                            #     0.00013,
                            #     0.00013, 0.00013, 0.00013, 0.00013, 0.00013, 0.00013, 0.00013, 0.00013, 0.00013,
                            #     0.00013,
                            #     0.00013, 0.00013, 0.00013, 0.00013, 0.00013, 0.00011, 0.00011, 0.00011, 0.00011,
                            #     0.00011,
                            #     0.00011, 0.00011, 0.00011, 0.00011, 0.00011, 0.00011, 0.00011, 0.00011, 0.00011,
                            #     0.00011,
                            #     0.00011, 0.00011, 0.00011, 0.00011, 0.00011, 0.00011, 0.00011, 0.00011, 0.00011,
                            #     0.00011,
                            #     0.00011, 0.00011, 0.00011, 0.00011, 0.00011, 7e-005, 7e-005, 7e-005, 7e-005, 7e-005,
                            #     7e-005, 7e-005, 7e-005, 7e-005, 7e-005, 7e-005, 7e-005, 7e-005, 7e-005, 7e-005, 7e-005,
                            #     7e-005, 7e-005, 7e-005, 7e-005, 7e-005, 7e-005, 7e-005, 7e-005, 7e-005, 7e-005, 7e-005,
                            #     7e-005, 7e-005, 7e-005, 7e-005, 7e-005, 7e-005, 7e-005, 7e-005
                            # ]
                            )


def rice_tj(x):
    """
    Real Name: b'Rice Tj'
    Original Eqn: b'( [(1,0)-(365,1)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0),\\\\ (12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23,0)\\\\ ,(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35,0\\\\ ),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47,\\\\ 0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94,0),(95\\\\ ,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105,0),(106\\\\ ,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0),(116,0)\\\\ ,(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126,0),(127\\\\ ,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0),(137,0)\\\\ ,(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147,0),(148\\\\ ,0),(149,0),(150,0),(151,0),(152,0),(153,0),(154,0),(155,0),(156,0),(157,0),(158,0)\\\\ ,(159,0),(160,0),(161,0),(162,0),(163,0),(164,0),(165,0),(166,0),(167,0),(168,0),(169\\\\ ,0),(170,0),(171,0),(172,0),(173,0),(174,0),(175,0),(176,0),(177,0),(178,0),(179,0)\\\\ ,(180,0),(181,0),(182,0),(183,0),(184,0),(185,0),(186,0),(187,0),(188,0),(189,0),(190\\\\ ,0),(191,0),(192,0),(193,0),(194,0),(195,0),(196,0),(197,0),(198,0),(199,0),(200,0)\\\\ ,(201,0),(202,0),(203,0),(204,0),(205,0),(206,0),(207,0),(208,0),(209,0),(210,0),(211\\\\ ,0.95607),(212,0.95607),(213,0.95607),(214,0.95607),(215,0.95607),(216,0.95607),(217\\\\ ,0.95607),(218,0.95607),(219,0.95607),(220,0.95607),(221,0.95607),(222,0.95607),(223\\\\ ,0.95607),(224,0.95607),(225,0.95607),(226,0.95607),(227,0.95607),(228,0.95607),(229\\\\ ,0.95607),(230,0.95607),(231,0.95607),(232,0.95607),(233,0.95607),(234,0.95607),(235\\\\ ,0.95607),(236,0.95607),(237,0.95607),(238,0.95607),(239,0.95607),(240,0.95607),(241\\\\ ,0.9699),(242,0.9699),(243,0.9699),(244,0.9699),(245,0.9699),(246,0.9699),(247,0.9699\\\\ ),(248,0.9699),(249,0.9699),(250,0.9699),(251,0.9699),(252,0.9699),(253,0.9699),(254\\\\ ,0.9699),(255,0.9699),(256,0.9699),(257,0.9699),(258,0.9699),(259,0.9699),(260,0.9699\\\\ ),(261,0.9699),(262,0.9699),(263,0.9699),(264,0.9699),(265,0.9699),(266,0.9699),(267\\\\ ,0.9699),(268,0.9699),(269,0.9699),(270,0.9699),(271,0.91494),(272,0.91494),(273,0.91494\\\\ ),(274,0.91494),(275,0.91494),(276,0.91494),(277,0.91494),(278,0.91494),(279,0.91494\\\\ ),(280,0.91494),(281,0.91494),(282,0.91494),(283,0.91494),(284,0.91494),(285,0.91494\\\\ ),(286,0.91494),(287,0.91494),(288,0.91494),(289,0.91494),(290,0.91494),(291,0.91494\\\\ ),(292,0.91494),(293,0.91494),(294,0.91494),(295,0.91494),(296,0.91494),(297,0.91494\\\\ ),(298,0.91494),(299,0.91494),(300,0.91494),(301,0.76401),(302,0.76401),(303,0.76401\\\\ ),(304,0.76401),(305,0.76401),(306,0.76401),(307,0.76401),(308,0.76401),(309,0.76401\\\\ ),(310,0.76401),(311,0.76401),(312,0.76401),(313,0.76401),(314,0.76401),(315,0.76401\\\\ ),(316,0.76401),(317,0.76401),(318,0.76401),(319,0.76401),(320,0.76401),(321,0.76401\\\\ ),(322,0.76401),(323,0.76401),(324,0.76401),(325,0.76401),(326,0.76401),(327,0.76401\\\\ ),(328,0.76401),(329,0.76401),(330,0.76401),(331,0.19231),(332,0.19231),(333,0.19231\\\\ ),(334,0.19231),(335,0.19231),(336,0.19231),(337,0.19231),(338,0.19231),(339,0.19231\\\\ ),(340,0.19231),(341,0.19231),(342,0.19231),(343,0.19231),(344,0.19231),(345,0.19231\\\\ ),(346,0.19231),(347,0.19231),(348,0.19231),(349,0.19231),(350,0.19231),(351,0.19231\\\\ ),(352,0.19231),(353,0.19231),(354,0.19231),(355,0.19231),(356,0.19231),(357,0.19231\\\\ ),(358,0.19231),(359,0.19231),(360,0.19231),(361,0.19231),(362,0.19231),(363,0.19231\\\\ ),(364,0.19231),(365,0.19231))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b'first priority'
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], lookups_data["rice_tj"]
                            # [
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0.95607, 0.95607, 0.95607, 0.95607, 0.95607, 0.95607, 0.95607, 0.95607, 0.95607,
                            #     0.95607,
                            #     0.95607, 0.95607, 0.95607, 0.95607, 0.95607, 0.95607, 0.95607, 0.95607, 0.95607,
                            #     0.95607,
                            #     0.95607, 0.95607, 0.95607, 0.95607, 0.95607, 0.95607, 0.95607, 0.95607, 0.95607,
                            #     0.95607,
                            #     0.9699, 0.9699, 0.9699, 0.9699, 0.9699, 0.9699, 0.9699, 0.9699, 0.9699, 0.9699, 0.9699,
                            #     0.9699, 0.9699, 0.9699, 0.9699, 0.9699, 0.9699, 0.9699, 0.9699, 0.9699, 0.9699, 0.9699,
                            #     0.9699, 0.9699, 0.9699, 0.9699, 0.9699, 0.9699, 0.9699, 0.9699, 0.91494, 0.91494,
                            #     0.91494,
                            #     0.91494, 0.91494, 0.91494, 0.91494, 0.91494, 0.91494, 0.91494, 0.91494, 0.91494,
                            #     0.91494,
                            #     0.91494, 0.91494, 0.91494, 0.91494, 0.91494, 0.91494, 0.91494, 0.91494, 0.91494,
                            #     0.91494,
                            #     0.91494, 0.91494, 0.91494, 0.91494, 0.91494, 0.91494, 0.91494, 0.76401, 0.76401,
                            #     0.76401,
                            #     0.76401, 0.76401, 0.76401, 0.76401, 0.76401, 0.76401, 0.76401, 0.76401, 0.76401,
                            #     0.76401,
                            #     0.76401, 0.76401, 0.76401, 0.76401, 0.76401, 0.76401, 0.76401, 0.76401, 0.76401,
                            #     0.76401,
                            #     0.76401, 0.76401, 0.76401, 0.76401, 0.76401, 0.76401, 0.76401, 0.19231, 0.19231,
                            #     0.19231,
                            #     0.19231, 0.19231, 0.19231, 0.19231, 0.19231, 0.19231, 0.19231, 0.19231, 0.19231,
                            #     0.19231,
                            #     0.19231, 0.19231, 0.19231, 0.19231, 0.19231, 0.19231, 0.19231, 0.19231, 0.19231,
                            #     0.19231,
                            #     0.19231, 0.19231, 0.19231, 0.19231, 0.19231, 0.19231, 0.19231, 0.19231, 0.19231,
                            #     0.19231,
                            #     0.19231, 0.19231
                            # ]
                            )


@cache('step')
def zr_total_sup():
    """
    Real Name: b'zr total sup'
    Original Eqn: b'zr agri sup+zr Dim sup+zr wr sup+zr Env sup+zr agri dev sup+zr Ind sup'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return zr_agri_sup() + zr_dim_sup() + zr_wr_sup() + zr_env_sup() + zr_agri_dev_sup(
    ) + zr_ind_sup()


@cache('step')
def zr_total_dem():
    """
    Real Name: b'zr total dem'
    Original Eqn: b'(zr agri dem *agri zr dam coef)+(zr agri dev dem (Time)*agri zr dev coef)+zr dom dem\\\\ (Time)+zr Env dem (Time)+zr Ind (Time)+Zr wr dem (Time)'
    Units: b'MCM/Month'
    Limits: (None, None)
    Type: component

    b'(Zr Agri dem*"Agri Zaram dam Coef.")+("Zr Agri Develop.dem"*"Agri Zaram \\n    \\t\\tdam Develop. Coef.")+Zr Dom dem+Zr Env dem+"Zr Ind. Dem"+Zr wr dem'
    """
    return (zr_agri_dem() *
            agri_zr_dam_coef()) + (zr_agri_dev_dem(time()) * agri_zr_dev_coef()) + zr_dom_dem(
        time()) + zr_env_dem(time()) + zr_ind(time()) + zr_wr_dem(time())


def citrs_tj(x):
    """
    Real Name: b'Citrs Tj'
    Original Eqn: b'( [(1,0)-(365,0.5)],(1,0.00082),(2,0.00082),(3,0.00082),(4,0.00082),(5,0.00082),(6,0.00082\\\\ ),(7,0.00082),(8,0.00082),(9,0.00082),(10,0.00082),(11,0.00082),(12,0.00082),(13,0.00082\\\\ ),(14,0.00082),(15,0.00082),(16,0.00082),(17,0.00082),(18,0.00082),(19,0.00082),(20\\\\ ,0.00082),(21,0.00082),(22,0.00082),(23,0.00082),(24,0.00082),(25,0.00082),(26,0.00082\\\\ ),(27,0.00082),(28,0.00082),(29,0.00082),(30,0.00082),(31,0),(32,0),(33,0),(34,0),(\\\\ 35,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),\\\\ (47,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0)\\\\ ,(59,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0\\\\ ),(71,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,\\\\ 0),(83,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94\\\\ ,0),(95,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105\\\\ ,0),(106,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0)\\\\ ,(116,0),(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126\\\\ ,0),(127,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0)\\\\ ,(137,0),(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147\\\\ ,0),(148,0),(149,0),(150,0),(151,0),(152,0),(153,0),(154,0),(155,0),(156,0),(157,0)\\\\ ,(158,0),(159,0),(160,0),(161,0),(162,0),(163,0),(164,0),(165,0),(166,0),(167,0),(168\\\\ ,0),(169,0),(170,0),(171,0),(172,0),(173,0),(174,0),(175,0),(176,0),(177,0),(178,0)\\\\ ,(179,0),(180,0),(181,0.49264),(182,0.49264),(183,0.49264),(184,0.49264),(185,0.49264\\\\ ),(186,0.49264),(187,0.49264),(188,0.49264),(189,0.49264),(190,0.49264),(191,0.49264\\\\ ),(192,0.49264),(193,0.49264),(194,0.49264),(195,0.49264),(196,0.49264),(197,0.49264\\\\ ),(198,0.49264),(199,0.49264),(200,0.49264),(201,0.49264),(202,0.49264),(203,0.49264\\\\ ),(204,0.49264),(205,0.49264),(206,0.49264),(207,0.49264),(208,0.49264),(209,0.49264\\\\ ),(210,0.49264),(211,0.01118),(212,0.01118),(213,0.01118),(214,0.01118),(215,0.01118\\\\ ),(216,0.01118),(217,0.01118),(218,0.01118),(219,0.01118),(220,0.01118),(221,0.01118\\\\ ),(222,0.01118),(223,0.01118),(224,0.01118),(225,0.01118),(226,0.01118),(227,0.01118\\\\ ),(228,0.01118),(229,0.01118),(230,0.01118),(231,0.01118),(232,0.01118),(233,0.01118\\\\ ),(234,0.01118),(235,0.01118),(236,0.01118),(237,0.01118),(238,0.01118),(239,0.01118\\\\ ),(240,0.01118),(241,0.01242),(242,0.01242),(243,0.01242),(244,0.01242),(245,0.01242\\\\ ),(246,0.01242),(247,0.01242),(248,0.01242),(249,0.01242),(250,0.01242),(251,0.01242\\\\ ),(252,0.01242),(253,0.01242),(254,0.01242),(255,0.01242),(256,0.01242),(257,0.01242\\\\ ),(258,0.01242),(259,0.01242),(260,0.01242),(261,0.01242),(262,0.01242),(263,0.01242\\\\ ),(264,0.01242),(265,0.01242),(266,0.01242),(267,0.01242),(268,0.01242),(269,0.01242\\\\ ),(270,0.01242),(271,0.01247),(272,0.01247),(273,0.01247),(274,0.01247),(275,0.01247\\\\ ),(276,0.01247),(277,0.01247),(278,0.01247),(279,0.01247),(280,0.01247),(281,0.01247\\\\ ),(282,0.01247),(283,0.01247),(284,0.01247),(285,0.01247),(286,0.01247),(287,0.01247\\\\ ),(288,0.01247),(289,0.01247),(290,0.01247),(291,0.01247),(292,0.01247),(293,0.01247\\\\ ),(294,0.01247),(295,0.01247),(296,0.01247),(297,0.01247),(298,0.01247),(299,0.01247\\\\ ),(300,0.01247),(301,0.01247),(302,0.01247),(303,0.01247),(304,0.01247),(305,0.01247\\\\ ),(306,0.01247),(307,0.01247),(308,0.01247),(309,0.01247),(310,0.01247),(311,0.01247\\\\ ),(312,0.01247),(313,0.01247),(314,0.01247),(315,0.01247),(316,0.01247),(317,0.01247\\\\ ),(318,0.01247),(319,0.01247),(320,0.01247),(321,0.01247),(322,0.01247),(323,0.01247\\\\ ),(324,0.01247),(325,0.01247),(326,0.01247),(327,0.01247),(328,0.01247),(329,0.01247\\\\ ),(330,0.01247),(331,0.00731),(332,0.00731),(333,0.00731),(334,0.00731),(335,0.00731\\\\ ),(336,0.00731),(337,0.00731),(338,0.00731),(339,0.00731),(340,0.00731),(341,0.00731\\\\ ),(342,0.00731),(343,0.00731),(344,0.00731),(345,0.00731),(346,0.00731),(347,0.00731\\\\ ),(348,0.00731),(349,0.00731),(350,0.00731),(351,0.00731),(352,0.00731),(353,0.00731\\\\ ),(354,0.00731),(355,0.00731),(356,0.00731),(357,0.00731),(358,0.00731),(359,0.00731\\\\ ),(360,0.00731),(361,0.00731),(362,0.00731),(363,0.00731),(364,0.00731),(365,0.00731\\\\ ))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b'third priority'
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], lookups_data["citrs_tj"]
                            # [
                            #     0.00082, 0.00082, 0.00082, 0.00082, 0.00082, 0.00082, 0.00082, 0.00082, 0.00082,
                            #     0.00082,
                            #     0.00082, 0.00082, 0.00082, 0.00082, 0.00082, 0.00082, 0.00082, 0.00082, 0.00082,
                            #     0.00082,
                            #     0.00082, 0.00082, 0.00082, 0.00082, 0.00082, 0.00082, 0.00082, 0.00082, 0.00082,
                            #     0.00082,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0.49264, 0.49264, 0.49264, 0.49264, 0.49264, 0.49264, 0.49264, 0.49264, 0.49264,
                            #     0.49264,
                            #     0.49264, 0.49264, 0.49264, 0.49264, 0.49264, 0.49264, 0.49264, 0.49264, 0.49264,
                            #     0.49264,
                            #     0.49264, 0.49264, 0.49264, 0.49264, 0.49264, 0.49264, 0.49264, 0.49264, 0.49264,
                            #     0.49264,
                            #     0.01118, 0.01118, 0.01118, 0.01118, 0.01118, 0.01118, 0.01118, 0.01118, 0.01118,
                            #     0.01118,
                            #     0.01118, 0.01118, 0.01118, 0.01118, 0.01118, 0.01118, 0.01118, 0.01118, 0.01118,
                            #     0.01118,
                            #     0.01118, 0.01118, 0.01118, 0.01118, 0.01118, 0.01118, 0.01118, 0.01118, 0.01118,
                            #     0.01118,
                            #     0.01242, 0.01242, 0.01242, 0.01242, 0.01242, 0.01242, 0.01242, 0.01242, 0.01242,
                            #     0.01242,
                            #     0.01242, 0.01242, 0.01242, 0.01242, 0.01242, 0.01242, 0.01242, 0.01242, 0.01242,
                            #     0.01242,
                            #     0.01242, 0.01242, 0.01242, 0.01242, 0.01242, 0.01242, 0.01242, 0.01242, 0.01242,
                            #     0.01242,
                            #     0.01247, 0.01247, 0.01247, 0.01247, 0.01247, 0.01247, 0.01247, 0.01247, 0.01247,
                            #     0.01247,
                            #     0.01247, 0.01247, 0.01247, 0.01247, 0.01247, 0.01247, 0.01247, 0.01247, 0.01247,
                            #     0.01247,
                            #     0.01247, 0.01247, 0.01247, 0.01247, 0.01247, 0.01247, 0.01247, 0.01247, 0.01247,
                            #     0.01247,
                            #     0.01247, 0.01247, 0.01247, 0.01247, 0.01247, 0.01247, 0.01247, 0.01247, 0.01247,
                            #     0.01247,
                            #     0.01247, 0.01247, 0.01247, 0.01247, 0.01247, 0.01247, 0.01247, 0.01247, 0.01247,
                            #     0.01247,
                            #     0.01247, 0.01247, 0.01247, 0.01247, 0.01247, 0.01247, 0.01247, 0.01247, 0.01247,
                            #     0.01247,
                            #     0.00731, 0.00731, 0.00731, 0.00731, 0.00731, 0.00731, 0.00731, 0.00731, 0.00731,
                            #     0.00731,
                            #     0.00731, 0.00731, 0.00731, 0.00731, 0.00731, 0.00731, 0.00731, 0.00731, 0.00731,
                            #     0.00731,
                            #     0.00731, 0.00731, 0.00731, 0.00731, 0.00731, 0.00731, 0.00731, 0.00731, 0.00731,
                            #     0.00731,
                            #     0.00731, 0.00731, 0.00731, 0.00731, 0.00731
                            # ]
                            )


def wheat_tj(x):
    """
    Real Name: b'wheat Tj'
    Original Eqn: b'( [(1,0)-(365,0.03)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,\\\\ 0),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23\\\\ ,0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35\\\\ ,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47\\\\ ,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94,0),(95\\\\ ,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105,0),(106\\\\ ,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0),(116,0)\\\\ ,(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126,0),(127\\\\ ,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0),(137,0)\\\\ ,(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147,0),(148\\\\ ,0),(149,0),(150,0),(151,0),(152,0),(153,0),(154,0),(155,0),(156,0),(157,0),(158,0)\\\\ ,(159,0),(160,0),(161,0),(162,0),(163,0),(164,0),(165,0),(166,0),(167,0),(168,0),(169\\\\ ,0),(170,0),(171,0),(172,0),(173,0),(174,0),(175,0),(176,0),(177,0),(178,0),(179,0)\\\\ ,(180,0),(181,0.02469),(182,0.02469),(183,0.02469),(184,0.02469),(185,0.02469),(186\\\\ ,0.02469),(187,0.02469),(188,0.02469),(189,0.02469),(190,0.02469),(191,0.02469),(192\\\\ ,0.02469),(193,0.02469),(194,0.02469),(195,0.02469),(196,0.02469),(197,0.02469),(198\\\\ ,0.02469),(199,0.02469),(200,0.02469),(201,0.02469),(202,0.02469),(203,0.02469),(204\\\\ ,0.02469),(205,0.02469),(206,0.02469),(207,0.02469),(208,0.02469),(209,0.02469),(210\\\\ ,0.02469),(211,0.00042),(212,0.00042),(213,0.00042),(214,0.00042),(215,0.00042),(216\\\\ ,0.00042),(217,0.00042),(218,0.00042),(219,0.00042),(220,0.00042),(221,0.00042),(222\\\\ ,0.00042),(223,0.00042),(224,0.00042),(225,0.00042),(226,0.00042),(227,0.00042),(228\\\\ ,0.00042),(229,0.00042),(230,0.00042),(231,0.00042),(232,0.00042),(233,0.00042),(234\\\\ ,0.00042),(235,0.00042),(236,0.00042),(237,0.00042),(238,0.00042),(239,0.00042),(240\\\\ ,0.00042),(241,8e-005),(242,8e-005),(243,8e-005),(244,8e-005),(245,8e-005),(246,8e-005\\\\ ),(247,8e-005),(248,8e-005),(249,8e-005),(250,8e-005),(251,8e-005),(252,8e-005),(253\\\\ ,8e-005),(254,8e-005),(255,8e-005),(256,8e-005),(257,8e-005),(258,8e-005),(259,8e-005\\\\ ),(260,8e-005),(261,8e-005),(262,8e-005),(263,8e-005),(264,8e-005),(265,8e-005),(266\\\\ ,8e-005),(267,8e-005),(268,8e-005),(269,8e-005),(270,8e-005),(271,0),(272,0),(273,0\\\\ ),(274,0),(275,0),(276,0),(277,0),(278,0),(279,0),(280,0),(281,0),(282,0),(283,0),(\\\\ 284,0),(285,0),(286,0),(287,0),(288,0),(289,0),(290,0),(291,0),(292,0),(293,0),(294\\\\ ,0),(295,0),(296,0),(297,0),(298,0),(299,0),(300,0),(301,0),(302,0),(303,0),(304,0)\\\\ ,(305,0),(306,0),(307,0),(308,0),(309,0),(310,0),(311,0),(312,0),(313,0),(314,0),(315\\\\ ,0),(316,0),(317,0),(318,0),(319,0),(320,0),(321,0),(322,0),(323,0),(324,0),(325,0)\\\\ ,(326,0),(327,0),(328,0),(329,0),(330,0),(331,0),(332,0),(333,0),(334,0),(335,0),(336\\\\ ,0),(337,0),(338,0),(339,0),(340,0),(341,0),(342,0),(343,0),(344,0),(345,0),(346,0)\\\\ ,(347,0),(348,0),(349,0),(350,0),(351,0),(352,0),(353,0),(354,0),(355,0),(356,0),(357\\\\ ,0),(358,0),(359,0),(360,0),(361,0),(362,0),(363,0),(364,0),(365,0))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b'fifth priority'
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], lookups_data["wheat_tj"]
                            # [
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0.02469, 0.02469, 0.02469, 0.02469, 0.02469, 0.02469, 0.02469, 0.02469, 0.02469,
                            #     0.02469,
                            #     0.02469, 0.02469, 0.02469, 0.02469, 0.02469, 0.02469, 0.02469, 0.02469, 0.02469,
                            #     0.02469,
                            #     0.02469, 0.02469, 0.02469, 0.02469, 0.02469, 0.02469, 0.02469, 0.02469, 0.02469,
                            #     0.02469,
                            #     0.00042, 0.00042, 0.00042, 0.00042, 0.00042, 0.00042, 0.00042, 0.00042, 0.00042,
                            #     0.00042,
                            #     0.00042, 0.00042, 0.00042, 0.00042, 0.00042, 0.00042, 0.00042, 0.00042, 0.00042,
                            #     0.00042,
                            #     0.00042, 0.00042, 0.00042, 0.00042, 0.00042, 0.00042, 0.00042, 0.00042, 0.00042,
                            #     0.00042,
                            #     8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005,
                            #     8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005,
                            #     8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                            # ]
                            )


@cache('step')
def finesk_dam_outflow():
    """
    Real Name: b'Finesk Dam outflow'
    Original Eqn: b'Spill Finesk+Supply envi Finesk+"supply Agricul-1Finesk"+"Supply Domes-1Finesk"'
    Units: b'MCM/Month'
    Limits: (None, None)
    Type: component

    b''
    """
    return spill_finesk() + supply_envi_finesk() + supply_agricul1finesk() + supply_domes1finesk()


@cache('step')
def agric_supply_after_finesk():
    """
    Real Name: b'Agric supply after Finesk'
    Original Eqn: b'MIN(River aftr Finesk Dam-Dom Sup after Finesk, "Agricul-1Demand finesk")'
    Units: b'MCM'
    Limits: (None, None)
    Type: component

    b''
    """
    return np.minimum(river_aftr_finesk_dam() - dom_sup_after_finesk(), agricul1demand_finesk())


@cache('step')
def agricul1demand_finesk():
    """
    Real Name: b'"Agricul-1Demand finesk"'
    Original Eqn: b'apple(Time)+citrus(Time)+chickpea(Time)+grainmaize(Time)+rapeseed(Time)+rice(Time)+tomato\\\\ (Time)+wheat(Time)'
    Units: b'MCM/Month'
    Limits: (None, None)
    Type: component

    b''
    """
    return apple(time()) + citrus(time()) + chickpea(time()) + grainmaize(time()) + rapeseed(
        time()) + rice(time()) + tomato(time()) + wheat(time())


def apple(x):
    """
    Real Name: b'apple'
    Original Eqn: b'( [(1,0)-(365,0.03)],(1,0.00516),(2,0.00516),(3,0.00516),(4,0.00516),(5,0.00516),(6,0.00516\\\\ ),(7,0.00516),(8,0.00516),(9,0.00516),(10,0.00516),(11,0.00516),(12,0.00516),(13,0.00516\\\\ ),(14,0.00516),(15,0.00516),(16,0.00516),(17,0.00516),(18,0.00516),(19,0.00516),(20\\\\ ,0.00516),(21,0.00516),(22,0.00516),(23,0.00516),(24,0.00516),(25,0.00516),(26,0.00516\\\\ ),(27,0.00516),(28,0.00516),(29,0.00516),(30,0.00516),(31,0),(32,0),(33,0),(34,0),(\\\\ 35,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),\\\\ (47,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0)\\\\ ,(59,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0\\\\ ),(71,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,\\\\ 0),(83,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94\\\\ ,0),(95,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105\\\\ ,0),(106,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0)\\\\ ,(116,0),(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126\\\\ ,0),(127,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0)\\\\ ,(137,0),(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147\\\\ ,0),(148,0),(149,0),(150,0),(151,0),(152,0),(153,0),(154,0),(155,0),(156,0),(157,0)\\\\ ,(158,0),(159,0),(160,0),(161,0),(162,0),(163,0),(164,0),(165,0),(166,0),(167,0),(168\\\\ ,0),(169,0),(170,0),(171,0),(172,0),(173,0),(174,0),(175,0),(176,0),(177,0),(178,0)\\\\ ,(179,0),(180,0),(181,0),(182,0),(183,0),(184,0),(185,0),(186,0),(187,0),(188,0),(189\\\\ ,0),(190,0),(191,0),(192,0),(193,0),(194,0),(195,0),(196,0),(197,0),(198,0),(199,0)\\\\ ,(200,0),(201,0),(202,0),(203,0),(204,0),(205,0),(206,0),(207,0),(208,0),(209,0),(210\\\\ ,0),(211,0.00471),(212,0.00471),(213,0.00471),(214,0.00471),(215,0.00471),(216,0.00471\\\\ ),(217,0.00471),(218,0.00471),(219,0.00471),(220,0.00471),(221,0.00471),(222,0.00471\\\\ ),(223,0.00471),(224,0.00471),(225,0.00471),(226,0.00471),(227,0.00471),(228,0.00471\\\\ ),(229,0.00471),(230,0.00471),(231,0.00471),(232,0.00471),(233,0.00471),(234,0.00471\\\\ ),(235,0.00471),(236,0.00471),(237,0.00471),(238,0.00471),(239,0.00471),(240,0.00471\\\\ ),(241,0.01233),(242,0.01233),(243,0.01233),(244,0.01233),(245,0.01233),(246,0.01233\\\\ ),(247,0.01233),(248,0.01233),(249,0.01233),(250,0.01233),(251,0.01233),(252,0.01233\\\\ ),(253,0.01233),(254,0.01233),(255,0.01233),(256,0.01233),(257,0.01233),(258,0.01233\\\\ ),(259,0.01233),(260,0.01233),(261,0.01233),(262,0.01233),(263,0.01233),(264,0.01233\\\\ ),(265,0.01233),(266,0.01233),(267,0.01233),(268,0.01233),(269,0.01233),(270,0.01233\\\\ ),(271,0.02669),(272,0.02669),(273,0.02669),(274,0.02669),(275,0.02669),(276,0.02669\\\\ ),(277,0.02669),(278,0.02669),(279,0.02669),(280,0.02669),(281,0.02669),(282,0.02669\\\\ ),(283,0.02669),(284,0.02669),(285,0.02669),(286,0.02669),(287,0.02669),(288,0.02669\\\\ ),(289,0.02669),(290,0.02669),(291,0.02669),(292,0.02669),(293,0.02669),(294,0.02669\\\\ ),(295,0.02669),(296,0.02669),(297,0.02669),(298,0.02669),(299,0.02669),(300,0.02669\\\\ ),(301,0.02638),(302,0.02638),(303,0.02638),(304,0.02638),(305,0.02638),(306,0.02638\\\\ ),(307,0.02638),(308,0.02638),(309,0.02638),(310,0.02638),(311,0.02638),(312,0.02638\\\\ ),(313,0.02638),(314,0.02638),(315,0.02638),(316,0.02638),(317,0.02638),(318,0.02638\\\\ ),(319,0.02638),(320,0.02638),(321,0.02638),(322,0.02638),(323,0.02638),(324,0.02638\\\\ ),(325,0.02638),(326,0.02638),(327,0.02638),(328,0.02638),(329,0.02638),(330,0.02638\\\\ ),(331,0.02146),(332,0.02146),(333,0.02146),(334,0.02146),(335,0.02146),(336,0.02146\\\\ ),(337,0.02146),(338,0.02146),(339,0.02146),(340,0.02146),(341,0.02146),(342,0.02146\\\\ ),(343,0.02146),(344,0.02146),(345,0.02146),(346,0.02146),(347,0.02146),(348,0.02146\\\\ ),(349,0.02146),(350,0.02146),(351,0.02146),(352,0.02146),(353,0.02146),(354,0.02146\\\\ ),(355,0.02146),(356,0.02146),(357,0.02146),(358,0.02146),(359,0.02146),(360,0.02146\\\\ ),(361,0.02146),(362,0.02146),(363,0.02146),(364,0.02146),(365,0.02146))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], lookups_data["apple"]
                            # [
                            #     0.00516, 0.00516, 0.00516, 0.00516, 0.00516, 0.00516, 0.00516, 0.00516, 0.00516,
                            #     0.00516,
                            #     0.00516, 0.00516, 0.00516, 0.00516, 0.00516, 0.00516, 0.00516, 0.00516, 0.00516,
                            #     0.00516,
                            #     0.00516, 0.00516, 0.00516, 0.00516, 0.00516, 0.00516, 0.00516, 0.00516, 0.00516,
                            #     0.00516,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0.00471, 0.00471, 0.00471, 0.00471, 0.00471, 0.00471, 0.00471, 0.00471, 0.00471,
                            #     0.00471,
                            #     0.00471, 0.00471, 0.00471, 0.00471, 0.00471, 0.00471, 0.00471, 0.00471, 0.00471,
                            #     0.00471,
                            #     0.00471, 0.00471, 0.00471, 0.00471, 0.00471, 0.00471, 0.00471, 0.00471, 0.00471,
                            #     0.00471,
                            #     0.01233, 0.01233, 0.01233, 0.01233, 0.01233, 0.01233, 0.01233, 0.01233, 0.01233,
                            #     0.01233,
                            #     0.01233, 0.01233, 0.01233, 0.01233, 0.01233, 0.01233, 0.01233, 0.01233, 0.01233,
                            #     0.01233,
                            #     0.01233, 0.01233, 0.01233, 0.01233, 0.01233, 0.01233, 0.01233, 0.01233, 0.01233,
                            #     0.01233,
                            #     0.02669, 0.02669, 0.02669, 0.02669, 0.02669, 0.02669, 0.02669, 0.02669, 0.02669,
                            #     0.02669,
                            #     0.02669, 0.02669, 0.02669, 0.02669, 0.02669, 0.02669, 0.02669, 0.02669, 0.02669,
                            #     0.02669,
                            #     0.02669, 0.02669, 0.02669, 0.02669, 0.02669, 0.02669, 0.02669, 0.02669, 0.02669,
                            #     0.02669,
                            #     0.02638, 0.02638, 0.02638, 0.02638, 0.02638, 0.02638, 0.02638, 0.02638, 0.02638,
                            #     0.02638,
                            #     0.02638, 0.02638, 0.02638, 0.02638, 0.02638, 0.02638, 0.02638, 0.02638, 0.02638,
                            #     0.02638,
                            #     0.02638, 0.02638, 0.02638, 0.02638, 0.02638, 0.02638, 0.02638, 0.02638, 0.02638,
                            #     0.02638,
                            #     0.02146, 0.02146, 0.02146, 0.02146, 0.02146, 0.02146, 0.02146, 0.02146, 0.02146,
                            #     0.02146,
                            #     0.02146, 0.02146, 0.02146, 0.02146, 0.02146, 0.02146, 0.02146, 0.02146, 0.02146,
                            #     0.02146,
                            #     0.02146, 0.02146, 0.02146, 0.02146, 0.02146, 0.02146, 0.02146, 0.02146, 0.02146,
                            #     0.02146,
                            #     0.02146, 0.02146, 0.02146, 0.02146, 0.02146
                            # ]
                            )


def rice(x):
    """
    Real Name: b'rice'
    Original Eqn: b'( [(1,0)-(365,0.07)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,\\\\ 0),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23\\\\ ,0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35\\\\ ,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47\\\\ ,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94,0),(95\\\\ ,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105,0),(106\\\\ ,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0),(116,0)\\\\ ,(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126,0),(127\\\\ ,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0),(137,0)\\\\ ,(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147,0),(148\\\\ ,0),(149,0),(150,0),(151,0),(152,0),(153,0),(154,0),(155,0),(156,0),(157,0),(158,0)\\\\ ,(159,0),(160,0),(161,0),(162,0),(163,0),(164,0),(165,0),(166,0),(167,0),(168,0),(169\\\\ ,0),(170,0),(171,0),(172,0),(173,0),(174,0),(175,0),(176,0),(177,0),(178,0),(179,0)\\\\ ,(180,0),(181,0),(182,0),(183,0),(184,0),(185,0),(186,0),(187,0),(188,0),(189,0),(190\\\\ ,0),(191,0),(192,0),(193,0),(194,0),(195,0),(196,0),(197,0),(198,0),(199,0),(200,0)\\\\ ,(201,0),(202,0),(203,0),(204,0),(205,0),(206,0),(207,0),(208,0),(209,0),(210,0),(211\\\\ ,0.03153),(212,0.03153),(213,0.03153),(214,0.03153),(215,0.03153),(216,0.03153),(217\\\\ ,0.03153),(218,0.03153),(219,0.03153),(220,0.03153),(221,0.03153),(222,0.03153),(223\\\\ ,0.03153),(224,0.03153),(225,0.03153),(226,0.03153),(227,0.03153),(228,0.03153),(229\\\\ ,0.03153),(230,0.03153),(231,0.03153),(232,0.03153),(233,0.03153),(234,0.03153),(235\\\\ ,0.03153),(236,0.03153),(237,0.03153),(238,0.03153),(239,0.03153),(240,0.03153),(241\\\\ ,0.04965),(242,0.04965),(243,0.04965),(244,0.04965),(245,0.04965),(246,0.04965),(247\\\\ ,0.04965),(248,0.04965),(249,0.04965),(250,0.04965),(251,0.04965),(252,0.04965),(253\\\\ ,0.04965),(254,0.04965),(255,0.04965),(256,0.04965),(257,0.04965),(258,0.04965),(259\\\\ ,0.04965),(260,0.04965),(261,0.04965),(262,0.04965),(263,0.04965),(264,0.04965),(265\\\\ ,0.04965),(266,0.04965),(267,0.04965),(268,0.04965),(269,0.04965),(270,0.04965),(271\\\\ ,0.06557),(272,0.06557),(273,0.06557),(274,0.06557),(275,0.06557),(276,0.06557),(277\\\\ ,0.06557),(278,0.06557),(279,0.06557),(280,0.06557),(281,0.06557),(282,0.06557),(283\\\\ ,0.06557),(284,0.06557),(285,0.06557),(286,0.06557),(287,0.06557),(288,0.06557),(289\\\\ ,0.06557),(290,0.06557),(291,0.06557),(292,0.06557),(293,0.06557),(294,0.06557),(295\\\\ ,0.06557),(296,0.06557),(297,0.06557),(298,0.06557),(299,0.06557),(300,0.06557),(301\\\\ ,0.05683),(302,0.05683),(303,0.05683),(304,0.05683),(305,0.05683),(306,0.05683),(307\\\\ ,0.05683),(308,0.05683),(309,0.05683),(310,0.05683),(311,0.05683),(312,0.05683),(313\\\\ ,0.05683),(314,0.05683),(315,0.05683),(316,0.05683),(317,0.05683),(318,0.05683),(319\\\\ ,0.05683),(320,0.05683),(321,0.05683),(322,0.05683),(323,0.05683),(324,0.05683),(325\\\\ ,0.05683),(326,0.05683),(327,0.05683),(328,0.05683),(329,0.05683),(330,0.05683),(331\\\\ ,0.01234),(332,0.01234),(333,0.01234),(334,0.01234),(335,0.01234),(336,0.01234),(337\\\\ ,0.01234),(338,0.01234),(339,0.01234),(340,0.01234),(341,0.01234),(342,0.01234),(343\\\\ ,0.01234),(344,0.01234),(345,0.01234),(346,0.01234),(347,0.01234),(348,0.01234),(349\\\\ ,0.01234),(350,0.01234),(351,0.01234),(352,0.01234),(353,0.01234),(354,0.01234),(355\\\\ ,0.01234),(356,0.01234),(357,0.01234),(358,0.01234),(359,0.01234),(360,0.01234),(361\\\\ ,0.01234),(362,0.01234),(363,0.01234),(364,0.01234),(365,0.01234))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], lookups_data["rice"]
                            # [
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0.03153, 0.03153, 0.03153, 0.03153, 0.03153, 0.03153, 0.03153, 0.03153, 0.03153,
                            #     0.03153,
                            #     0.03153, 0.03153, 0.03153, 0.03153, 0.03153, 0.03153, 0.03153, 0.03153, 0.03153,
                            #     0.03153,
                            #     0.03153, 0.03153, 0.03153, 0.03153, 0.03153, 0.03153, 0.03153, 0.03153, 0.03153,
                            #     0.03153,
                            #     0.04965, 0.04965, 0.04965, 0.04965, 0.04965, 0.04965, 0.04965, 0.04965, 0.04965,
                            #     0.04965,
                            #     0.04965, 0.04965, 0.04965, 0.04965, 0.04965, 0.04965, 0.04965, 0.04965, 0.04965,
                            #     0.04965,
                            #     0.04965, 0.04965, 0.04965, 0.04965, 0.04965, 0.04965, 0.04965, 0.04965, 0.04965,
                            #     0.04965,
                            #     0.06557, 0.06557, 0.06557, 0.06557, 0.06557, 0.06557, 0.06557, 0.06557, 0.06557,
                            #     0.06557,
                            #     0.06557, 0.06557, 0.06557, 0.06557, 0.06557, 0.06557, 0.06557, 0.06557, 0.06557,
                            #     0.06557,
                            #     0.06557, 0.06557, 0.06557, 0.06557, 0.06557, 0.06557, 0.06557, 0.06557, 0.06557,
                            #     0.06557,
                            #     0.05683, 0.05683, 0.05683, 0.05683, 0.05683, 0.05683, 0.05683, 0.05683, 0.05683,
                            #     0.05683,
                            #     0.05683, 0.05683, 0.05683, 0.05683, 0.05683, 0.05683, 0.05683, 0.05683, 0.05683,
                            #     0.05683,
                            #     0.05683, 0.05683, 0.05683, 0.05683, 0.05683, 0.05683, 0.05683, 0.05683, 0.05683,
                            #     0.05683,
                            #     0.01234, 0.01234, 0.01234, 0.01234, 0.01234, 0.01234, 0.01234, 0.01234, 0.01234,
                            #     0.01234,
                            #     0.01234, 0.01234, 0.01234, 0.01234, 0.01234, 0.01234, 0.01234, 0.01234, 0.01234,
                            #     0.01234,
                            #     0.01234, 0.01234, 0.01234, 0.01234, 0.01234, 0.01234, 0.01234, 0.01234, 0.01234,
                            #     0.01234,
                            #     0.01234, 0.01234, 0.01234, 0.01234, 0.01234
                            # ]
                            )


def chickpea(x):
    """
    Real Name: b'chickpea'
    Original Eqn: b'( [(1,0)-(365,0.0002)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11\\\\ ,0),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23\\\\ ,0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35\\\\ ,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47\\\\ ,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94,0),(95\\\\ ,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105,0),(106\\\\ ,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0),(116,0)\\\\ ,(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126,0),(127\\\\ ,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0),(137,0)\\\\ ,(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147,0),(148\\\\ ,0),(149,0),(150,0),(151,0),(152,0),(153,0),(154,0),(155,0),(156,0),(157,0),(158,0)\\\\ ,(159,0),(160,0),(161,0),(162,0),(163,0),(164,0),(165,0),(166,0),(167,0),(168,0),(169\\\\ ,0),(170,0),(171,0),(172,0),(173,0),(174,0),(175,0),(176,0),(177,0),(178,0),(179,0)\\\\ ,(180,0),(181,0),(182,0),(183,0),(184,0),(185,0),(186,0),(187,0),(188,0),(189,0),(190\\\\ ,0),(191,0),(192,0),(193,0),(194,0),(195,0),(196,0),(197,0),(198,0),(199,0),(200,0)\\\\ ,(201,0),(202,0),(203,0),(204,0),(205,0),(206,0),(207,0),(208,0),(209,0),(210,0),(211\\\\ ,2e-005),(212,2e-005),(213,2e-005),(214,2e-005),(215,2e-005),(216,2e-005),(217,2e-005\\\\ ),(218,2e-005),(219,2e-005),(220,2e-005),(221,2e-005),(222,2e-005),(223,2e-005),(224\\\\ ,2e-005),(225,2e-005),(226,2e-005),(227,2e-005),(228,2e-005),(229,2e-005),(230,2e-005\\\\ ),(231,2e-005),(232,2e-005),(233,2e-005),(234,2e-005),(235,2e-005),(236,2e-005),(237\\\\ ,2e-005),(238,2e-005),(239,2e-005),(240,2e-005),(241,8e-005),(242,8e-005),(243,8e-005\\\\ ),(244,8e-005),(245,8e-005),(246,8e-005),(247,8e-005),(248,8e-005),(249,8e-005),(250\\\\ ,8e-005),(251,8e-005),(252,8e-005),(253,8e-005),(254,8e-005),(255,8e-005),(256,8e-005\\\\ ),(257,8e-005),(258,8e-005),(259,8e-005),(260,8e-005),(261,8e-005),(262,8e-005),(263\\\\ ,8e-005),(264,8e-005),(265,8e-005),(266,8e-005),(267,8e-005),(268,8e-005),(269,8e-005\\\\ ),(270,8e-005),(271,0.00011),(272,0.00011),(273,0.00011),(274,0.00011),(275,0.00011\\\\ ),(276,0.00011),(277,0.00011),(278,0.00011),(279,0.00011),(280,0.00011),(281,0.00011\\\\ ),(282,0.00011),(283,0.00011),(284,0.00011),(285,0.00011),(286,0.00011),(287,0.00011\\\\ ),(288,0.00011),(289,0.00011),(290,0.00011),(291,0.00011),(292,0.00011),(293,0.00011\\\\ ),(294,0.00011),(295,0.00011),(296,0.00011),(297,0.00011),(298,0.00011),(299,0.00011\\\\ ),(300,0.00011),(301,2e-005),(302,2e-005),(303,2e-005),(304,2e-005),(305,2e-005),(306\\\\ ,2e-005),(307,2e-005),(308,2e-005),(309,2e-005),(310,2e-005),(311,2e-005),(312,2e-005\\\\ ),(313,2e-005),(314,2e-005),(315,2e-005),(316,2e-005),(317,2e-005),(318,2e-005),(319\\\\ ,2e-005),(320,2e-005),(321,2e-005),(322,2e-005),(323,2e-005),(324,2e-005),(325,2e-005\\\\ ),(326,2e-005),(327,2e-005),(328,2e-005),(329,2e-005),(330,2e-005),(331,0),(332,0),\\\\ (333,0),(334,0),(335,0),(336,0),(337,0),(338,0),(339,0),(340,0),(341,0),(342,0),(343\\\\ ,0),(344,0),(345,0),(346,0),(347,0),(348,0),(349,0),(350,0),(351,0),(352,0),(353,0)\\\\ ,(354,0),(355,0),(356,0),(357,0),(358,0),(359,0),(360,0),(361,0),(362,0),(363,0),(364\\\\ ,0),(365,0))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], lookups_data["chickpea"]
                            # [
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005,
                            #     2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005,
                            #     2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 8e-005, 8e-005, 8e-005,
                            #     8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005,
                            #     8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005,
                            #     8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 0.00011, 0.00011, 0.00011, 0.00011, 0.00011,
                            #     0.00011, 0.00011, 0.00011, 0.00011, 0.00011, 0.00011, 0.00011, 0.00011, 0.00011,
                            #     0.00011,
                            #     0.00011, 0.00011, 0.00011, 0.00011, 0.00011, 0.00011, 0.00011, 0.00011, 0.00011,
                            #     0.00011,
                            #     0.00011, 0.00011, 0.00011, 0.00011, 0.00011, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005,
                            #     2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005,
                            #     2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005,
                            #     2e-005, 2e-005, 2e-005, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                            # ]
                            )


def citrus(x):
    """
    Real Name: b'citrus'
    Original Eqn: b'( [(1,0)-(365,0.002)],(1,6e-005),(2,6e-005),(3,6e-005),(4,6e-005),(5,6e-005),(6,6e-005\\\\ ),(7,6e-005),(8,6e-005),(9,6e-005),(10,6e-005),(11,6e-005),(12,6e-005),(13,6e-005),\\\\ (14,6e-005),(15,6e-005),(16,6e-005),(17,6e-005),(18,6e-005),(19,6e-005),(20,6e-005)\\\\ ,(21,6e-005),(22,6e-005),(23,6e-005),(24,6e-005),(25,6e-005),(26,6e-005),(27,6e-005\\\\ ),(28,6e-005),(29,6e-005),(30,6e-005),(31,0),(32,0),(33,0),(34,0),(35,0),(36,0),(37\\\\ ,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47,0),(48,0),(49\\\\ ,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59,0),(60,0),(61\\\\ ,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71,0),(72,0),(73\\\\ ,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83,0),(84,0),(85\\\\ ,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94,0),(95,0),(96,0),(97\\\\ ,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105,0),(106,0),(107,0),(\\\\ 108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0),(116,0),(117,0),(118\\\\ ,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126,0),(127,0),(128,0)\\\\ ,(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0),(137,0),(138,0),(139\\\\ ,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147,0),(148,0),(149,0)\\\\ ,(150,0),(151,0),(152,0),(153,0),(154,0),(155,0),(156,0),(157,0),(158,0),(159,0),(160\\\\ ,0),(161,0),(162,0),(163,0),(164,0),(165,0),(166,0),(167,0),(168,0),(169,0),(170,0)\\\\ ,(171,0),(172,0),(173,0),(174,0),(175,0),(176,0),(177,0),(178,0),(179,0),(180,0),(181\\\\ ,0.00061),(182,0.00061),(183,0.00061),(184,0.00061),(185,0.00061),(186,0.00061),(187\\\\ ,0.00061),(188,0.00061),(189,0.00061),(190,0.00061),(191,0.00061),(192,0.00061),(193\\\\ ,0.00061),(194,0.00061),(195,0.00061),(196,0.00061),(197,0.00061),(198,0.00061),(199\\\\ ,0.00061),(200,0.00061),(201,0.00061),(202,0.00061),(203,0.00061),(204,0.00061),(205\\\\ ,0.00061),(206,0.00061),(207,0.00061),(208,0.00061),(209,0.00061),(210,0.00061),(211\\\\ ,0.0005),(212,0.0005),(213,0.0005),(214,0.0005),(215,0.0005),(216,0.0005),(217,0.0005\\\\ ),(218,0.0005),(219,0.0005),(220,0.0005),(221,0.0005),(222,0.0005),(223,0.0005),(224\\\\ ,0.0005),(225,0.0005),(226,0.0005),(227,0.0005),(228,0.0005),(229,0.0005),(230,0.0005\\\\ ),(231,0.0005),(232,0.0005),(233,0.0005),(234,0.0005),(235,0.0005),(236,0.0005),(237\\\\ ,0.0005),(238,0.0005),(239,0.0005),(240,0.0005),(241,0.00086),(242,0.00086),(243,0.00086\\\\ ),(244,0.00086),(245,0.00086),(246,0.00086),(247,0.00086),(248,0.00086),(249,0.00086\\\\ ),(250,0.00086),(251,0.00086),(252,0.00086),(253,0.00086),(254,0.00086),(255,0.00086\\\\ ),(256,0.00086),(257,0.00086),(258,0.00086),(259,0.00086),(260,0.00086),(261,0.00086\\\\ ),(262,0.00086),(263,0.00086),(264,0.00086),(265,0.00086),(266,0.00086),(267,0.00086\\\\ ),(268,0.00086),(269,0.00086),(270,0.00086),(271,0.00122),(272,0.00122),(273,0.00122\\\\ ),(274,0.00122),(275,0.00122),(276,0.00122),(277,0.00122),(278,0.00122),(279,0.00122\\\\ ),(280,0.00122),(281,0.00122),(282,0.00122),(283,0.00122),(284,0.00122),(285,0.00122\\\\ ),(286,0.00122),(287,0.00122),(288,0.00122),(289,0.00122),(290,0.00122),(291,0.00122\\\\ ),(292,0.00122),(293,0.00122),(294,0.00122),(295,0.00122),(296,0.00122),(297,0.00122\\\\ ),(298,0.00122),(299,0.00122),(300,0.00122),(301,0.00122),(302,0.00122),(303,0.00122\\\\ ),(304,0.00122),(305,0.00122),(306,0.00122),(307,0.00122),(308,0.00122),(309,0.00122\\\\ ),(310,0.00122),(311,0.00122),(312,0.00122),(313,0.00122),(314,0.00122),(315,0.00122\\\\ ),(316,0.00122),(317,0.00122),(318,0.00122),(319,0.00122),(320,0.00122),(321,0.00122\\\\ ),(322,0.00122),(323,0.00122),(324,0.00122),(325,0.00122),(326,0.00122),(327,0.00122\\\\ ),(328,0.00122),(329,0.00122),(330,0.00122),(331,0.00064),(332,0.00064),(333,0.00064\\\\ ),(334,0.00064),(335,0.00064),(336,0.00064),(337,0.00064),(338,0.00064),(339,0.00064\\\\ ),(340,0.00064),(341,0.00064),(342,0.00064),(343,0.00064),(344,0.00064),(345,0.00064\\\\ ),(346,0.00064),(347,0.00064),(348,0.00064),(349,0.00064),(350,0.00064),(351,0.00064\\\\ ),(352,0.00064),(353,0.00064),(354,0.00064),(355,0.00064),(356,0.00064),(357,0.00064\\\\ ),(358,0.00064),(359,0.00064),(360,0.00064),(361,0.00064),(362,0.00064),(363,0.00064\\\\ ),(364,0.00064),(365,0.00064))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], lookups_data["citrus"]
                            # [
                            #     6e-005, 6e-005, 6e-005, 6e-005, 6e-005, 6e-005, 6e-005, 6e-005, 6e-005, 6e-005, 6e-005,
                            #     6e-005, 6e-005, 6e-005, 6e-005, 6e-005, 6e-005, 6e-005, 6e-005, 6e-005, 6e-005, 6e-005,
                            #     6e-005, 6e-005, 6e-005, 6e-005, 6e-005, 6e-005, 6e-005, 6e-005, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.00061, 0.00061,
                            #     0.00061,
                            #     0.00061, 0.00061, 0.00061, 0.00061, 0.00061, 0.00061, 0.00061, 0.00061, 0.00061,
                            #     0.00061,
                            #     0.00061, 0.00061, 0.00061, 0.00061, 0.00061, 0.00061, 0.00061, 0.00061, 0.00061,
                            #     0.00061,
                            #     0.00061, 0.00061, 0.00061, 0.00061, 0.00061, 0.00061, 0.00061, 0.0005, 0.0005, 0.0005,
                            #     0.0005, 0.0005, 0.0005, 0.0005, 0.0005, 0.0005, 0.0005, 0.0005, 0.0005, 0.0005, 0.0005,
                            #     0.0005, 0.0005, 0.0005, 0.0005, 0.0005, 0.0005, 0.0005, 0.0005, 0.0005, 0.0005, 0.0005,
                            #     0.0005, 0.0005, 0.0005, 0.0005, 0.0005, 0.00086, 0.00086, 0.00086, 0.00086, 0.00086,
                            #     0.00086, 0.00086, 0.00086, 0.00086, 0.00086, 0.00086, 0.00086, 0.00086, 0.00086,
                            #     0.00086,
                            #     0.00086, 0.00086, 0.00086, 0.00086, 0.00086, 0.00086, 0.00086, 0.00086, 0.00086,
                            #     0.00086,
                            #     0.00086, 0.00086, 0.00086, 0.00086, 0.00086, 0.00122, 0.00122, 0.00122, 0.00122,
                            #     0.00122,
                            #     0.00122, 0.00122, 0.00122, 0.00122, 0.00122, 0.00122, 0.00122, 0.00122, 0.00122,
                            #     0.00122,
                            #     0.00122, 0.00122, 0.00122, 0.00122, 0.00122, 0.00122, 0.00122, 0.00122, 0.00122,
                            #     0.00122,
                            #     0.00122, 0.00122, 0.00122, 0.00122, 0.00122, 0.00122, 0.00122, 0.00122, 0.00122,
                            #     0.00122,
                            #     0.00122, 0.00122, 0.00122, 0.00122, 0.00122, 0.00122, 0.00122, 0.00122, 0.00122,
                            #     0.00122,
                            #     0.00122, 0.00122, 0.00122, 0.00122, 0.00122, 0.00122, 0.00122, 0.00122, 0.00122,
                            #     0.00122,
                            #     0.00122, 0.00122, 0.00122, 0.00122, 0.00122, 0.00064, 0.00064, 0.00064, 0.00064,
                            #     0.00064,
                            #     0.00064, 0.00064, 0.00064, 0.00064, 0.00064, 0.00064, 0.00064, 0.00064, 0.00064,
                            #     0.00064,
                            #     0.00064, 0.00064, 0.00064, 0.00064, 0.00064, 0.00064, 0.00064, 0.00064, 0.00064,
                            #     0.00064,
                            #     0.00064, 0.00064, 0.00064, 0.00064, 0.00064, 0.00064, 0.00064, 0.00064, 0.00064, 0.00064
                            # ]
                            )


def rapeseed(x):
    """
    Real Name: b'rapeseed'
    Original Eqn: b'( [(1,0)-(365,0.0003)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11\\\\ ,0),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23\\\\ ,0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35\\\\ ,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47\\\\ ,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94,0),(95\\\\ ,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105,0),(106\\\\ ,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0),(116,0)\\\\ ,(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126,0),(127\\\\ ,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0),(137,0)\\\\ ,(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147,0),(148\\\\ ,0),(149,0),(150,0),(151,0),(152,0),(153,0),(154,0),(155,0),(156,0),(157,0),(158,0)\\\\ ,(159,0),(160,0),(161,0),(162,0),(163,0),(164,0),(165,0),(166,0),(167,0),(168,0),(169\\\\ ,0),(170,0),(171,0),(172,0),(173,0),(174,0),(175,0),(176,0),(177,0),(178,0),(179,0)\\\\ ,(180,0),(181,0),(182,0),(183,0),(184,0),(185,0),(186,0),(187,0),(188,0),(189,0),(190\\\\ ,0),(191,0),(192,0),(193,0),(194,0),(195,0),(196,0),(197,0),(198,0),(199,0),(200,0)\\\\ ,(201,0),(202,0),(203,0),(204,0),(205,0),(206,0),(207,0),(208,0),(209,0),(210,0),(211\\\\ ,2e-005),(212,2e-005),(213,2e-005),(214,2e-005),(215,2e-005),(216,2e-005),(217,2e-005\\\\ ),(218,2e-005),(219,2e-005),(220,2e-005),(221,2e-005),(222,2e-005),(223,2e-005),(224\\\\ ,2e-005),(225,2e-005),(226,2e-005),(227,2e-005),(228,2e-005),(229,2e-005),(230,2e-005\\\\ ),(231,2e-005),(232,2e-005),(233,2e-005),(234,2e-005),(235,2e-005),(236,2e-005),(237\\\\ ,2e-005),(238,2e-005),(239,2e-005),(240,2e-005),(241,0.0001),(242,0.0001),(243,0.0001\\\\ ),(244,0.0001),(245,0.0001),(246,0.0001),(247,0.0001),(248,0.0001),(249,0.0001),(250\\\\ ,0.0001),(251,0.0001),(252,0.0001),(253,0.0001),(254,0.0001),(255,0.0001),(256,0.0001\\\\ ),(257,0.0001),(258,0.0001),(259,0.0001),(260,0.0001),(261,0.0001),(262,0.0001),(263\\\\ ,0.0001),(264,0.0001),(265,0.0001),(266,0.0001),(267,0.0001),(268,0.0001),(269,0.0001\\\\ ),(270,0.0001),(271,0.00022),(272,0.00022),(273,0.00022),(274,0.00022),(275,0.00022\\\\ ),(276,0.00022),(277,0.00022),(278,0.00022),(279,0.00022),(280,0.00022),(281,0.00022\\\\ ),(282,0.00022),(283,0.00022),(284,0.00022),(285,0.00022),(286,0.00022),(287,0.00022\\\\ ),(288,0.00022),(289,0.00022),(290,0.00022),(291,0.00022),(292,0.00022),(293,0.00022\\\\ ),(294,0.00022),(295,0.00022),(296,0.00022),(297,0.00022),(298,0.00022),(299,0.00022\\\\ ),(300,0.00022),(301,0.0002),(302,0.0002),(303,0.0002),(304,0.0002),(305,0.0002),(306\\\\ ,0.0002),(307,0.0002),(308,0.0002),(309,0.0002),(310,0.0002),(311,0.0002),(312,0.0002\\\\ ),(313,0.0002),(314,0.0002),(315,0.0002),(316,0.0002),(317,0.0002),(318,0.0002),(319\\\\ ,0.0002),(320,0.0002),(321,0.0002),(322,0.0002),(323,0.0002),(324,0.0002),(325,0.0002\\\\ ),(326,0.0002),(327,0.0002),(328,0.0002),(329,0.0002),(330,0.0002),(331,0.0001),(332\\\\ ,0.0001),(333,0.0001),(334,0.0001),(335,0.0001),(336,0.0001),(337,0.0001),(338,0.0001\\\\ ),(339,0.0001),(340,0.0001),(341,0.0001),(342,0.0001),(343,0.0001),(344,0.0001),(345\\\\ ,0.0001),(346,0.0001),(347,0.0001),(348,0.0001),(349,0.0001),(350,0.0001),(351,0.0001\\\\ ),(352,0.0001),(353,0.0001),(354,0.0001),(355,0.0001),(356,0.0001),(357,0.0001),(358\\\\ ,0.0001),(359,0.0001),(360,0.0001),(361,0.0001),(362,0.0001),(363,0.0001),(364,0.0001\\\\ ),(365,0.0001))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], lookups_data["rapeseed"]
                            # [
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005,
                            #     2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005,
                            #     2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 0.0001, 0.0001, 0.0001,
                            #     0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001,
                            #     0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001,
                            #     0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.00022, 0.00022, 0.00022, 0.00022, 0.00022,
                            #     0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.00022,
                            #     0.00022,
                            #     0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.00022,
                            #     0.00022,
                            #     0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.0002, 0.0002, 0.0002, 0.0002, 0.0002,
                            #     0.0002, 0.0002, 0.0002, 0.0002, 0.0002, 0.0002, 0.0002, 0.0002, 0.0002, 0.0002, 0.0002,
                            #     0.0002, 0.0002, 0.0002, 0.0002, 0.0002, 0.0002, 0.0002, 0.0002, 0.0002, 0.0002, 0.0002,
                            #     0.0002, 0.0002, 0.0002, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001,
                            #     0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001,
                            #     0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001,
                            #     0.0001, 0.0001, 0.0001, 0.0001, 0.0001
                            # ]
                            )


def grainmaize(x):
    """
    Real Name: b'grainmaize'
    Original Eqn: b'( [(1,0)-(365,0.0002)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11\\\\ ,0),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23\\\\ ,0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35\\\\ ,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47\\\\ ,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94,0),(95\\\\ ,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105,0),(106\\\\ ,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0),(116,0)\\\\ ,(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126,0),(127\\\\ ,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0),(137,0)\\\\ ,(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147,0),(148\\\\ ,0),(149,0),(150,0),(151,0),(152,0),(153,0),(154,0),(155,0),(156,0),(157,0),(158,0)\\\\ ,(159,0),(160,0),(161,0),(162,0),(163,0),(164,0),(165,0),(166,0),(167,0),(168,0),(169\\\\ ,0),(170,0),(171,0),(172,0),(173,0),(174,0),(175,0),(176,0),(177,0),(178,0),(179,0)\\\\ ,(180,0),(181,0),(182,0),(183,0),(184,0),(185,0),(186,0),(187,0),(188,0),(189,0),(190\\\\ ,0),(191,0),(192,0),(193,0),(194,0),(195,0),(196,0),(197,0),(198,0),(199,0),(200,0)\\\\ ,(201,0),(202,0),(203,0),(204,0),(205,0),(206,0),(207,0),(208,0),(209,0),(210,0),(211\\\\ ,0),(212,0),(213,0),(214,0),(215,0),(216,0),(217,0),(218,0),(219,0),(220,0),(221,0)\\\\ ,(222,0),(223,0),(224,0),(225,0),(226,0),(227,0),(228,0),(229,0),(230,0),(231,0),(232\\\\ ,0),(233,0),(234,0),(235,0),(236,0),(237,0),(238,0),(239,0),(240,0),(241,2e-005),(242\\\\ ,2e-005),(243,2e-005),(244,2e-005),(245,2e-005),(246,2e-005),(247,2e-005),(248,2e-005\\\\ ),(249,2e-005),(250,2e-005),(251,2e-005),(252,2e-005),(253,2e-005),(254,2e-005),(255\\\\ ,2e-005),(256,2e-005),(257,2e-005),(258,2e-005),(259,2e-005),(260,2e-005),(261,2e-005\\\\ ),(262,2e-005),(263,2e-005),(264,2e-005),(265,2e-005),(266,2e-005),(267,2e-005),(268\\\\ ,2e-005),(269,2e-005),(270,2e-005),(271,4e-005),(272,4e-005),(273,4e-005),(274,4e-005\\\\ ),(275,4e-005),(276,4e-005),(277,4e-005),(278,4e-005),(279,4e-005),(280,4e-005),(281\\\\ ,4e-005),(282,4e-005),(283,4e-005),(284,4e-005),(285,4e-005),(286,4e-005),(287,4e-005\\\\ ),(288,4e-005),(289,4e-005),(290,4e-005),(291,4e-005),(292,4e-005),(293,4e-005),(294\\\\ ,4e-005),(295,4e-005),(296,4e-005),(297,4e-005),(298,4e-005),(299,4e-005),(300,4e-005\\\\ ),(301,0.00013),(302,0.00013),(303,0.00013),(304,0.00013),(305,0.00013),(306,0.00013\\\\ ),(307,0.00013),(308,0.00013),(309,0.00013),(310,0.00013),(311,0.00013),(312,0.00013\\\\ ),(313,0.00013),(314,0.00013),(315,0.00013),(316,0.00013),(317,0.00013),(318,0.00013\\\\ ),(319,0.00013),(320,0.00013),(321,0.00013),(322,0.00013),(323,0.00013),(324,0.00013\\\\ ),(325,0.00013),(326,0.00013),(327,0.00013),(328,0.00013),(329,0.00013),(330,0.00013\\\\ ),(331,4e-005),(332,4e-005),(333,4e-005),(334,4e-005),(335,4e-005),(336,4e-005),(337\\\\ ,4e-005),(338,4e-005),(339,4e-005),(340,4e-005),(341,4e-005),(342,4e-005),(343,4e-005\\\\ ),(344,4e-005),(345,4e-005),(346,4e-005),(347,4e-005),(348,4e-005),(349,4e-005),(350\\\\ ,4e-005),(351,4e-005),(352,4e-005),(353,4e-005),(354,4e-005),(355,4e-005),(356,4e-005\\\\ ),(357,4e-005),(358,4e-005),(359,4e-005),(360,4e-005),(361,4e-005),(362,4e-005),(363\\\\ ,4e-005),(364,4e-005),(365,4e-005))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], lookups_data["grainmaize"]
                            # [
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005,
                            #     2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005,
                            #     2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 4e-005, 4e-005, 4e-005,
                            #     4e-005, 4e-005, 4e-005, 4e-005, 4e-005, 4e-005, 4e-005, 4e-005, 4e-005, 4e-005, 4e-005,
                            #     4e-005, 4e-005, 4e-005, 4e-005, 4e-005, 4e-005, 4e-005, 4e-005, 4e-005, 4e-005, 4e-005,
                            #     4e-005, 4e-005, 4e-005, 4e-005, 4e-005, 0.00013, 0.00013, 0.00013, 0.00013, 0.00013,
                            #     0.00013, 0.00013, 0.00013, 0.00013, 0.00013, 0.00013, 0.00013, 0.00013, 0.00013,
                            #     0.00013,
                            #     0.00013, 0.00013, 0.00013, 0.00013, 0.00013, 0.00013, 0.00013, 0.00013, 0.00013,
                            #     0.00013,
                            #     0.00013, 0.00013, 0.00013, 0.00013, 0.00013, 4e-005, 4e-005, 4e-005, 4e-005, 4e-005,
                            #     4e-005, 4e-005, 4e-005, 4e-005, 4e-005, 4e-005, 4e-005, 4e-005, 4e-005, 4e-005, 4e-005,
                            #     4e-005, 4e-005, 4e-005, 4e-005, 4e-005, 4e-005, 4e-005, 4e-005, 4e-005, 4e-005, 4e-005,
                            #     4e-005, 4e-005, 4e-005, 4e-005, 4e-005, 4e-005, 4e-005, 4e-005
                            # ]
                            )


def tomato(x):
    """
    Real Name: b'tomato'
    Original Eqn: b'( [(1,0)-(365,0.0003)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11\\\\ ,0),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23\\\\ ,0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35\\\\ ,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47\\\\ ,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94,0),(95\\\\ ,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105,0),(106\\\\ ,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0),(116,0)\\\\ ,(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126,0),(127\\\\ ,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0),(137,0)\\\\ ,(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147,0),(148\\\\ ,0),(149,0),(150,0),(151,0),(152,0),(153,0),(154,0),(155,0),(156,0),(157,0),(158,0)\\\\ ,(159,0),(160,0),(161,0),(162,0),(163,0),(164,0),(165,0),(166,0),(167,0),(168,0),(169\\\\ ,0),(170,0),(171,0),(172,0),(173,0),(174,0),(175,0),(176,0),(177,0),(178,0),(179,0)\\\\ ,(180,0),(181,0),(182,0),(183,0),(184,0),(185,0),(186,0),(187,0),(188,0),(189,0),(190\\\\ ,0),(191,0),(192,0),(193,0),(194,0),(195,0),(196,0),(197,0),(198,0),(199,0),(200,0)\\\\ ,(201,0),(202,0),(203,0),(204,0),(205,0),(206,0),(207,0),(208,0),(209,0),(210,0),(211\\\\ ,2e-005),(212,2e-005),(213,2e-005),(214,2e-005),(215,2e-005),(216,2e-005),(217,2e-005\\\\ ),(218,2e-005),(219,2e-005),(220,2e-005),(221,2e-005),(222,2e-005),(223,2e-005),(224\\\\ ,2e-005),(225,2e-005),(226,2e-005),(227,2e-005),(228,2e-005),(229,2e-005),(230,2e-005\\\\ ),(231,2e-005),(232,2e-005),(233,2e-005),(234,2e-005),(235,2e-005),(236,2e-005),(237\\\\ ,2e-005),(238,2e-005),(239,2e-005),(240,2e-005),(241,8e-005),(242,8e-005),(243,8e-005\\\\ ),(244,8e-005),(245,8e-005),(246,8e-005),(247,8e-005),(248,8e-005),(249,8e-005),(250\\\\ ,8e-005),(251,8e-005),(252,8e-005),(253,8e-005),(254,8e-005),(255,8e-005),(256,8e-005\\\\ ),(257,8e-005),(258,8e-005),(259,8e-005),(260,8e-005),(261,8e-005),(262,8e-005),(263\\\\ ,8e-005),(264,8e-005),(265,8e-005),(266,8e-005),(267,8e-005),(268,8e-005),(269,8e-005\\\\ ),(270,8e-005),(271,0.00022),(272,0.00022),(273,0.00022),(274,0.00022),(275,0.00022\\\\ ),(276,0.00022),(277,0.00022),(278,0.00022),(279,0.00022),(280,0.00022),(281,0.00022\\\\ ),(282,0.00022),(283,0.00022),(284,0.00022),(285,0.00022),(286,0.00022),(287,0.00022\\\\ ),(288,0.00022),(289,0.00022),(290,0.00022),(291,0.00022),(292,0.00022),(293,0.00022\\\\ ),(294,0.00022),(295,0.00022),(296,0.00022),(297,0.00022),(298,0.00022),(299,0.00022\\\\ ),(300,0.00022),(301,0.00022),(302,0.00022),(303,0.00022),(304,0.00022),(305,0.00022\\\\ ),(306,0.00022),(307,0.00022),(308,0.00022),(309,0.00022),(310,0.00022),(311,0.00022\\\\ ),(312,0.00022),(313,0.00022),(314,0.00022),(315,0.00022),(316,0.00022),(317,0.00022\\\\ ),(318,0.00022),(319,0.00022),(320,0.00022),(321,0.00022),(322,0.00022),(323,0.00022\\\\ ),(324,0.00022),(325,0.00022),(326,0.00022),(327,0.00022),(328,0.00022),(329,0.00022\\\\ ),(330,0.00022),(331,0.00014),(332,0.00014),(333,0.00014),(334,0.00014),(335,0.00014\\\\ ),(336,0.00014),(337,0.00014),(338,0.00014),(339,0.00014),(340,0.00014),(341,0.00014\\\\ ),(342,0.00014),(343,0.00014),(344,0.00014),(345,0.00014),(346,0.00014),(347,0.00014\\\\ ),(348,0.00014),(349,0.00014),(350,0.00014),(351,0.00014),(352,0.00014),(353,0.00014\\\\ ),(354,0.00014),(355,0.00014),(356,0.00014),(357,0.00014),(358,0.00014),(359,0.00014\\\\ ),(360,0.00014),(361,0.00014),(362,0.00014),(363,0.00014),(364,0.00014),(365,0.00014\\\\ ))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], lookups_data["tomato"]
                            # [
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005,
                            #     2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005,
                            #     2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 2e-005, 8e-005, 8e-005, 8e-005,
                            #     8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005,
                            #     8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 8e-005,
                            #     8e-005, 8e-005, 8e-005, 8e-005, 8e-005, 0.00022, 0.00022, 0.00022, 0.00022, 0.00022,
                            #     0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.00022,
                            #     0.00022,
                            #     0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.00022,
                            #     0.00022,
                            #     0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.00022,
                            #     0.00022,
                            #     0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.00022,
                            #     0.00022,
                            #     0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.00022,
                            #     0.00022,
                            #     0.00022, 0.00022, 0.00022, 0.00022, 0.00022, 0.00014, 0.00014, 0.00014, 0.00014,
                            #     0.00014,
                            #     0.00014, 0.00014, 0.00014, 0.00014, 0.00014, 0.00014, 0.00014, 0.00014, 0.00014,
                            #     0.00014,
                            #     0.00014, 0.00014, 0.00014, 0.00014, 0.00014, 0.00014, 0.00014, 0.00014, 0.00014,
                            #     0.00014,
                            #     0.00014, 0.00014, 0.00014, 0.00014, 0.00014, 0.00014, 0.00014, 0.00014, 0.00014, 0.00014
                            # ]
                            )


@cache('run')
def minisfinesk():
    """
    Real Name: b'"mini-Sfinesk"'
    Original Eqn: b'2.27'
    Units: b'MCM'
    Limits: (None, None)
    Type: constant

    b'\\u0627\\u062d\\u062a\\u0645\\u0627\\u0644\\u0627 \\u0633\\u0637\\u062d \\u0633\\u062f \\u0641\\u0646\\u06cc\\u06a9'
    """
    return 2.27


def wheat(x):
    """
    Real Name: b'wheat'
    Original Eqn: b'( [(1,0)-(365,0.02)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,\\\\ 0),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23\\\\ ,0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35\\\\ ,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47\\\\ ,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94,0),(95\\\\ ,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105,0),(106\\\\ ,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0),(116,0)\\\\ ,(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126,0),(127\\\\ ,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0),(137,0)\\\\ ,(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147,0),(148\\\\ ,0),(149,0),(150,0),(151,0),(152,0),(153,0),(154,0),(155,0),(156,0),(157,0),(158,0)\\\\ ,(159,0),(160,0),(161,0),(162,0),(163,0),(164,0),(165,0),(166,0),(167,0),(168,0),(169\\\\ ,0),(170,0),(171,0),(172,0),(173,0),(174,0),(175,0),(176,0),(177,0),(178,0),(179,0)\\\\ ,(180,0),(181,0.01399),(182,0.01399),(183,0.01399),(184,0.01399),(185,0.01399),(186\\\\ ,0.01399),(187,0.01399),(188,0.01399),(189,0.01399),(190,0.01399),(191,0.01399),(192\\\\ ,0.01399),(193,0.01399),(194,0.01399),(195,0.01399),(196,0.01399),(197,0.01399),(198\\\\ ,0.01399),(199,0.01399),(200,0.01399),(201,0.01399),(202,0.01399),(203,0.01399),(204\\\\ ,0.01399),(205,0.01399),(206,0.01399),(207,0.01399),(208,0.01399),(209,0.01399),(210\\\\ ,0.01399),(211,0.00861),(212,0.00861),(213,0.00861),(214,0.00861),(215,0.00861),(216\\\\ ,0.00861),(217,0.00861),(218,0.00861),(219,0.00861),(220,0.00861),(221,0.00861),(222\\\\ ,0.00861),(223,0.00861),(224,0.00861),(225,0.00861),(226,0.00861),(227,0.00861),(228\\\\ ,0.00861),(229,0.00861),(230,0.00861),(231,0.00861),(232,0.00861),(233,0.00861),(234\\\\ ,0.00861),(235,0.00861),(236,0.00861),(237,0.00861),(238,0.00861),(239,0.00861),(240\\\\ ,0.00861),(241,0.00252),(242,0.00252),(243,0.00252),(244,0.00252),(245,0.00252),(246\\\\ ,0.00252),(247,0.00252),(248,0.00252),(249,0.00252),(250,0.00252),(251,0.00252),(252\\\\ ,0.00252),(253,0.00252),(254,0.00252),(255,0.00252),(256,0.00252),(257,0.00252),(258\\\\ ,0.00252),(259,0.00252),(260,0.00252),(261,0.00252),(262,0.00252),(263,0.00252),(264\\\\ ,0.00252),(265,0.00252),(266,0.00252),(267,0.00252),(268,0.00252),(269,0.00252),(270\\\\ ,0.00252),(271,0),(272,0),(273,0),(274,0),(275,0),(276,0),(277,0),(278,0),(279,0),(\\\\ 280,0),(281,0),(282,0),(283,0),(284,0),(285,0),(286,0),(287,0),(288,0),(289,0),(290\\\\ ,0),(291,0),(292,0),(293,0),(294,0),(295,0),(296,0),(297,0),(298,0),(299,0),(300,0)\\\\ ,(301,0),(302,0),(303,0),(304,0),(305,0),(306,0),(307,0),(308,0),(309,0),(310,0),(311\\\\ ,0),(312,0),(313,0),(314,0),(315,0),(316,0),(317,0),(318,0),(319,0),(320,0),(321,0)\\\\ ,(322,0),(323,0),(324,0),(325,0),(326,0),(327,0),(328,0),(329,0),(330,0),(331,0),(332\\\\ ,0),(333,0),(334,0),(335,0),(336,0),(337,0),(338,0),(339,0),(340,0),(341,0),(342,0)\\\\ ,(343,0),(344,0),(345,0),(346,0),(347,0),(348,0),(349,0),(350,0),(351,0),(352,0),(353\\\\ ,0),(354,0),(355,0),(356,0),(357,0),(358,0),(359,0),(360,0),(361,0),(362,0),(363,0)\\\\ ,(364,0),(365,0))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], lookups_data["wheat"]
                            # [
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0.01399, 0.01399, 0.01399, 0.01399, 0.01399, 0.01399, 0.01399, 0.01399, 0.01399,
                            #     0.01399,
                            #     0.01399, 0.01399, 0.01399, 0.01399, 0.01399, 0.01399, 0.01399, 0.01399, 0.01399,
                            #     0.01399,
                            #     0.01399, 0.01399, 0.01399, 0.01399, 0.01399, 0.01399, 0.01399, 0.01399, 0.01399,
                            #     0.01399,
                            #     0.00861, 0.00861, 0.00861, 0.00861, 0.00861, 0.00861, 0.00861, 0.00861, 0.00861,
                            #     0.00861,
                            #     0.00861, 0.00861, 0.00861, 0.00861, 0.00861, 0.00861, 0.00861, 0.00861, 0.00861,
                            #     0.00861,
                            #     0.00861, 0.00861, 0.00861, 0.00861, 0.00861, 0.00861, 0.00861, 0.00861, 0.00861,
                            #     0.00861,
                            #     0.00252, 0.00252, 0.00252, 0.00252, 0.00252, 0.00252, 0.00252, 0.00252, 0.00252,
                            #     0.00252,
                            #     0.00252, 0.00252, 0.00252, 0.00252, 0.00252, 0.00252, 0.00252, 0.00252, 0.00252,
                            #     0.00252,
                            #     0.00252, 0.00252, 0.00252, 0.00252, 0.00252, 0.00252, 0.00252, 0.00252, 0.00252,
                            #     0.00252,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            #     0,
                            #     0, 0, 0, 0, 0
                            # ]
                            )


@cache('step')
def agri_sup_frm_gw():
    """
    Real Name: b'Agri sup frm GW'
    Original Eqn: b'MIN(Agri def aftr SW sup, GW Res )'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return np.minimum(agri_def_aftr_sw_sup(), gw_res())


@cache('step')
def abbn_eva():
    """
    Real Name: b'"Ab-bn Eva"'
    Original Eqn: b'Max(0,"monthly evp ab-bn" (Time)*"area ab-bn"/1000)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return np.maximum(0, monthly_evp_abbn(time()) * area_abbn() / 1000)


@cache('step')
def tj_dom_sup():
    """
    Real Name: b'Tj Dom Sup'
    Original Eqn: b'MIN(Tj Outflow, Tj Dom Dem (Time))'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return np.minimum(tj_outflow(), tj_dom_dem(time()))


@cache('step')
def zr_aftr_dam():
    """
    Real Name: b'Zr aftr Dam'
    Original Eqn: b'inter aftr Zr Dam (Time)+Zr Dam outflow'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return inter_aftr_zr_dam(time()) + zr_dam_outflow()


@cache('step')
def tj_evaporation():
    """
    Real Name: b'Tj Evaporation'
    Original Eqn: b'Max(0,Tj Monthly Evaporation (Time)*"Tj Area(km^2)"/1000)'
    Units: b'MCM/Month'
    Limits: (None, None)
    Type: component

    b''
    """
    return np.maximum(0, tj_monthly_evaporation(time()) * tj_areakm2() / 1000)


@cache('step')
def zr_agri_dev_sup():
    """
    Real Name: b'zr agri dev sup'
    Original Eqn: b'MIN((zr agri dev dem (Time)*agri zr dev coef), (Zr outflow-zr Dim sup-zr wr sup-zr Env sup -zr agri sup-zr Ind sup) )'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return np.minimum(
        (zr_agri_dev_dem(time()) * agri_zr_dev_coef()),
        (zr_outflow() - zr_dim_sup() - zr_wr_sup() - zr_env_sup() - zr_agri_sup() - zr_ind_sup()))


@cache('step')
def tj_ind_sup():
    """
    Real Name: b'Tj Ind Sup'
    Original Eqn: b'MIN(Tj Ind Dem (Time), (Tj Outflow-Tj Dom Sup-Tj Env Sup))'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return np.minimum(tj_ind_dem(time()), (tj_outflow() - tj_dom_sup() - tj_env_sup()))


@cache('step')
def evaporation():
    """
    Real Name: b'Evaporation'
    Original Eqn: b'Max(0,"monthly evaporation -1 Finesk" (Time)*"normal evaporation -1 Finesk"*"surface -1 Finesk"\\\\ )'
    Units: b'MCM/Month'
    Limits: (None, None)
    Type: component

    b''
    """
    return np.maximum(
        0,
        monthly_evaporation_1_finesk(time()) * normal_evaporation_1_finesk() * surface_1_finesk())


@cache('step')
def ovr_reso_in_out_system():
    """
    Real Name: b'ovr Reso in out system'
    Original Eqn: b'IF THEN ELSE(Tj bfr Sea<=Env Tj Dem (Time), 0, Tj bfr Sea-Env Tj Dem (Time))'
    Units: b''
    Limits: (None, None)
    Type: component

    b'\\u0645\\u0642\\u0627\\u062f\\u06cc\\u0631 \\u0622\\u0628\\u062f\\u0647\\u06cc \\u0645\\u0627\\u0632\\u0627\\u062f \\u0631\\u0648\\u062f\\u062e\\u0627\\u0646\\u0647 \\u062a\\u062c\\u0646 \\u0642\\u0627\\u0628\\u0644 \\n    \\t\\t\\u0627\\u0646\\u062a\\u0642\\u0627\\u0644 \\u0628\\u0647 \\u062d\\u0648\\u0636\\u0647 \\u0645\\u062c\\u0627\\u0648\\u0631 \\u0627\\u0632 \\u0645\\u0642\\u0637\\u0639 \\u0622\\u0628 \\u062f\\u0631\\u06cc\\u0627'
    """
    return functions.if_then_else(tj_bfr_sea() <= env_tj_dem(time()), 0,
                                  tj_bfr_sea() - env_tj_dem(time()))


@cache('step')
def zr_dim_sup():
    """
    Real Name: b'zr Dim sup'
    Original Eqn: b'MIN(Zr outflow, zr dom dem (Time))'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return np.minimum(zr_outflow(), zr_dom_dem(time()))


@cache('step')
def river_aftr_finesk_dam():
    """
    Real Name: b'River aftr Finesk Dam'
    Original Eqn: b'After Finesk Interflow (Time)+Finesk Dam outflow'
    Units: b'MCM/Month'
    Limits: (None, None)
    Type: component

    b''
    """
    return after_finesk_interflow(time()) + finesk_dam_outflow()


def shirinrood_upstream(x):
    """
    Real Name: b'Shirinrood upstream'
    Original Eqn: b'( [(1,0)-(365,0.8)],(1,0.31354),(2,0.31354),(3,0.31354),(4,0.31354),(5,0.31354),(6,0.31354\\\\ ),(7,0.31354),(8,0.31354),(9,0.31354),(10,0.31354),(11,0.31354),(12,0.31354),(13,0.31354\\\\ ),(14,0.31354),(15,0.31354),(16,0.31354),(17,0.31354),(18,0.31354),(19,0.31354),(20\\\\ ,0.31354),(21,0.31354),(22,0.31354),(23,0.31354),(24,0.31354),(25,0.31354),(26,0.31354\\\\ ),(27,0.31354),(28,0.31354),(29,0.31354),(30,0.31354),(31,0.51477),(32,0.51477),(33\\\\ ,0.51477),(34,0.51477),(35,0.51477),(36,0.51477),(37,0.51477),(38,0.51477),(39,0.51477\\\\ ),(40,0.51477),(41,0.51477),(42,0.51477),(43,0.51477),(44,0.51477),(45,0.51477),(46\\\\ ,0.51477),(47,0.51477),(48,0.51477),(49,0.51477),(50,0.51477),(51,0.51477),(52,0.51477\\\\ ),(53,0.51477),(54,0.51477),(55,0.51477),(56,0.51477),(57,0.51477),(58,0.51477),(59\\\\ ,0.51477),(60,0.51477),(61,0.26542),(62,0.26542),(63,0.26542),(64,0.26542),(65,0.26542\\\\ ),(66,0.26542),(67,0.26542),(68,0.26542),(69,0.26542),(70,0.26542),(71,0.26542),(72\\\\ ,0.26542),(73,0.26542),(74,0.26542),(75,0.26542),(76,0.26542),(77,0.26542),(78,0.26542\\\\ ),(79,0.26542),(80,0.26542),(81,0.26542),(82,0.26542),(83,0.26542),(84,0.26542),(85\\\\ ,0.26542),(86,0.26542),(87,0.26542),(88,0.26542),(89,0.26542),(90,0.26542),(91,0.27026\\\\ ),(92,0.27026),(93,0.27026),(94,0.27026),(95,0.27026),(96,0.27026),(97,0.27026),(98\\\\ ,0.27026),(99,0.27026),(100,0.27026),(101,0.27026),(102,0.27026),(103,0.27026),(104\\\\ ,0.27026),(105,0.27026),(106,0.27026),(107,0.27026),(108,0.27026),(109,0.27026),(110\\\\ ,0.27026),(111,0.27026),(112,0.27026),(113,0.27026),(114,0.27026),(115,0.27026),(116\\\\ ,0.27026),(117,0.27026),(118,0.27026),(119,0.27026),(120,0.27026),(121,0.32409),(122\\\\ ,0.32409),(123,0.32409),(124,0.32409),(125,0.32409),(126,0.32409),(127,0.32409),(128\\\\ ,0.32409),(129,0.32409),(130,0.32409),(131,0.32409),(132,0.32409),(133,0.32409),(134\\\\ ,0.32409),(135,0.32409),(136,0.32409),(137,0.32409),(138,0.32409),(139,0.32409),(140\\\\ ,0.32409),(141,0.32409),(142,0.32409),(143,0.32409),(144,0.32409),(145,0.32409),(146\\\\ ,0.32409),(147,0.32409),(148,0.32409),(149,0.32409),(150,0.32409),(151,0.32722),(152\\\\ ,0.32722),(153,0.32722),(154,0.32722),(155,0.32722),(156,0.32722),(157,0.32722),(158\\\\ ,0.32722),(159,0.32722),(160,0.32722),(161,0.32722),(162,0.32722),(163,0.32722),(164\\\\ ,0.32722),(165,0.32722),(166,0.32722),(167,0.32722),(168,0.32722),(169,0.32722),(170\\\\ ,0.32722),(171,0.32722),(172,0.32722),(173,0.32722),(174,0.32722),(175,0.32722),(176\\\\ ,0.32722),(177,0.32722),(178,0.32722),(179,0.32722),(180,0.32722),(181,0.73235),(182\\\\ ,0.73235),(183,0.73235),(184,0.73235),(185,0.73235),(186,0.73235),(187,0.73235),(188\\\\ ,0.73235),(189,0.73235),(190,0.73235),(191,0.73235),(192,0.73235),(193,0.73235),(194\\\\ ,0.73235),(195,0.73235),(196,0.73235),(197,0.73235),(198,0.73235),(199,0.73235),(200\\\\ ,0.73235),(201,0.73235),(202,0.73235),(203,0.73235),(204,0.73235),(205,0.73235),(206\\\\ ,0.73235),(207,0.73235),(208,0.73235),(209,0.73235),(210,0.73235),(211,0.32645),(212\\\\ ,0.32645),(213,0.32645),(214,0.32645),(215,0.32645),(216,0.32645),(217,0.32645),(218\\\\ ,0.32645),(219,0.32645),(220,0.32645),(221,0.32645),(222,0.32645),(223,0.32645),(224\\\\ ,0.32645),(225,0.32645),(226,0.32645),(227,0.32645),(228,0.32645),(229,0.32645),(230\\\\ ,0.32645),(231,0.32645),(232,0.32645),(233,0.32645),(234,0.32645),(235,0.32645),(236\\\\ ,0.32645),(237,0.32645),(238,0.32645),(239,0.32645),(240,0.32645),(241,0.30768),(242\\\\ ,0.30768),(243,0.30768),(244,0.30768),(245,0.30768),(246,0.30768),(247,0.30768),(248\\\\ ,0.30768),(249,0.30768),(250,0.30768),(251,0.30768),(252,0.30768),(253,0.30768),(254\\\\ ,0.30768),(255,0.30768),(256,0.30768),(257,0.30768),(258,0.30768),(259,0.30768),(260\\\\ ,0.30768),(261,0.30768),(262,0.30768),(263,0.30768),(264,0.30768),(265,0.30768),(266\\\\ ,0.30768),(267,0.30768),(268,0.30768),(269,0.30768),(270,0.30768),(271,0.31673),(272\\\\ ,0.31673),(273,0.31673),(274,0.31673),(275,0.31673),(276,0.31673),(277,0.31673),(278\\\\ ,0.31673),(279,0.31673),(280,0.31673),(281,0.31673),(282,0.31673),(283,0.31673),(284\\\\ ,0.31673),(285,0.31673),(286,0.31673),(287,0.31673),(288,0.31673),(289,0.31673),(290\\\\ ,0.31673),(291,0.31673),(292,0.31673),(293,0.31673),(294,0.31673),(295,0.31673),(296\\\\ ,0.31673),(297,0.31673),(298,0.31673),(299,0.31673),(300,0.31673),(301,0.31243),(302\\\\ ,0.31243),(303,0.31243),(304,0.31243),(305,0.31243),(306,0.31243),(307,0.31243),(308\\\\ ,0.31243),(309,0.31243),(310,0.31243),(311,0.31243),(312,0.31243),(313,0.31243),(314\\\\ ,0.31243),(315,0.31243),(316,0.31243),(317,0.31243),(318,0.31243),(319,0.31243),(320\\\\ ,0.31243),(321,0.31243),(322,0.31243),(323,0.31243),(324,0.31243),(325,0.31243),(326\\\\ ,0.31243),(327,0.31243),(328,0.31243),(329,0.31243),(330,0.31243),(331,0.15322),(332\\\\ ,0.15322),(333,0.15322),(334,0.15322),(335,0.15322),(336,0.15322),(337,0.15322),(338\\\\ ,0.15322),(339,0.15322),(340,0.15322),(341,0.15322),(342,0.15322),(343,0.15322),(344\\\\ ,0.15322),(345,0.15322),(346,0.15322),(347,0.15322),(348,0.15322),(349,0.15322),(350\\\\ ,0.15322),(351,0.15322),(352,0.15322),(353,0.15322),(354,0.15322),(355,0.15322),(356\\\\ ,0.15322),(357,0.15322),(358,0.15322),(359,0.15322),(360,0.15322),(361,0.15322),(362\\\\ ,0.15322),(363,0.15322),(364,0.15322),(365,0.15322))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], [
                                0.31354, 0.31354, 0.31354, 0.31354, 0.31354, 0.31354, 0.31354, 0.31354, 0.31354,
                                0.31354,
                                0.31354, 0.31354, 0.31354, 0.31354, 0.31354, 0.31354, 0.31354, 0.31354, 0.31354,
                                0.31354,
                                0.31354, 0.31354, 0.31354, 0.31354, 0.31354, 0.31354, 0.31354, 0.31354, 0.31354,
                                0.31354,
                                0.51477, 0.51477, 0.51477, 0.51477, 0.51477, 0.51477, 0.51477, 0.51477, 0.51477,
                                0.51477,
                                0.51477, 0.51477, 0.51477, 0.51477, 0.51477, 0.51477, 0.51477, 0.51477, 0.51477,
                                0.51477,
                                0.51477, 0.51477, 0.51477, 0.51477, 0.51477, 0.51477, 0.51477, 0.51477, 0.51477,
                                0.51477,
                                0.26542, 0.26542, 0.26542, 0.26542, 0.26542, 0.26542, 0.26542, 0.26542, 0.26542,
                                0.26542,
                                0.26542, 0.26542, 0.26542, 0.26542, 0.26542, 0.26542, 0.26542, 0.26542, 0.26542,
                                0.26542,
                                0.26542, 0.26542, 0.26542, 0.26542, 0.26542, 0.26542, 0.26542, 0.26542, 0.26542,
                                0.26542,
                                0.27026, 0.27026, 0.27026, 0.27026, 0.27026, 0.27026, 0.27026, 0.27026, 0.27026,
                                0.27026,
                                0.27026, 0.27026, 0.27026, 0.27026, 0.27026, 0.27026, 0.27026, 0.27026, 0.27026,
                                0.27026,
                                0.27026, 0.27026, 0.27026, 0.27026, 0.27026, 0.27026, 0.27026, 0.27026, 0.27026,
                                0.27026,
                                0.32409, 0.32409, 0.32409, 0.32409, 0.32409, 0.32409, 0.32409, 0.32409, 0.32409,
                                0.32409,
                                0.32409, 0.32409, 0.32409, 0.32409, 0.32409, 0.32409, 0.32409, 0.32409, 0.32409,
                                0.32409,
                                0.32409, 0.32409, 0.32409, 0.32409, 0.32409, 0.32409, 0.32409, 0.32409, 0.32409,
                                0.32409,
                                0.32722, 0.32722, 0.32722, 0.32722, 0.32722, 0.32722, 0.32722, 0.32722, 0.32722,
                                0.32722,
                                0.32722, 0.32722, 0.32722, 0.32722, 0.32722, 0.32722, 0.32722, 0.32722, 0.32722,
                                0.32722,
                                0.32722, 0.32722, 0.32722, 0.32722, 0.32722, 0.32722, 0.32722, 0.32722, 0.32722,
                                0.32722,
                                0.73235, 0.73235, 0.73235, 0.73235, 0.73235, 0.73235, 0.73235, 0.73235, 0.73235,
                                0.73235,
                                0.73235, 0.73235, 0.73235, 0.73235, 0.73235, 0.73235, 0.73235, 0.73235, 0.73235,
                                0.73235,
                                0.73235, 0.73235, 0.73235, 0.73235, 0.73235, 0.73235, 0.73235, 0.73235, 0.73235,
                                0.73235,
                                0.32645, 0.32645, 0.32645, 0.32645, 0.32645, 0.32645, 0.32645, 0.32645, 0.32645,
                                0.32645,
                                0.32645, 0.32645, 0.32645, 0.32645, 0.32645, 0.32645, 0.32645, 0.32645, 0.32645,
                                0.32645,
                                0.32645, 0.32645, 0.32645, 0.32645, 0.32645, 0.32645, 0.32645, 0.32645, 0.32645,
                                0.32645,
                                0.30768, 0.30768, 0.30768, 0.30768, 0.30768, 0.30768, 0.30768, 0.30768, 0.30768,
                                0.30768,
                                0.30768, 0.30768, 0.30768, 0.30768, 0.30768, 0.30768, 0.30768, 0.30768, 0.30768,
                                0.30768,
                                0.30768, 0.30768, 0.30768, 0.30768, 0.30768, 0.30768, 0.30768, 0.30768, 0.30768,
                                0.30768,
                                0.31673, 0.31673, 0.31673, 0.31673, 0.31673, 0.31673, 0.31673, 0.31673, 0.31673,
                                0.31673,
                                0.31673, 0.31673, 0.31673, 0.31673, 0.31673, 0.31673, 0.31673, 0.31673, 0.31673,
                                0.31673,
                                0.31673, 0.31673, 0.31673, 0.31673, 0.31673, 0.31673, 0.31673, 0.31673, 0.31673,
                                0.31673,
                                0.31243, 0.31243, 0.31243, 0.31243, 0.31243, 0.31243, 0.31243, 0.31243, 0.31243,
                                0.31243,
                                0.31243, 0.31243, 0.31243, 0.31243, 0.31243, 0.31243, 0.31243, 0.31243, 0.31243,
                                0.31243,
                                0.31243, 0.31243, 0.31243, 0.31243, 0.31243, 0.31243, 0.31243, 0.31243, 0.31243,
                                0.31243,
                                0.15322, 0.15322, 0.15322, 0.15322, 0.15322, 0.15322, 0.15322, 0.15322, 0.15322,
                                0.15322,
                                0.15322, 0.15322, 0.15322, 0.15322, 0.15322, 0.15322, 0.15322, 0.15322, 0.15322,
                                0.15322,
                                0.15322, 0.15322, 0.15322, 0.15322, 0.15322, 0.15322, 0.15322, 0.15322, 0.15322,
                                0.15322,
                                0.15322, 0.15322, 0.15322, 0.15322, 0.15322
                            ])


@cache('step')
def total_demand1finesk():
    """
    Real Name: b'"Total Demand-1Finesk"'
    Original Eqn: b'"Agricul-1Demand finesk" +"Domes-1 Demad finesk" (Time)+envi Demand Finesk (Time)'
    Units: b'MCM'
    Limits: (None, None)
    Type: component

    b''
    """
    return agricul1demand_finesk() + domes1_demad_finesk(time()) + envi_demand_finesk(time())


@cache('step')
def zr_ind_sup():
    """
    Real Name: b'zr Ind sup'
    Original Eqn: b'MIN(zr Ind (Time), (Zr outflow-zr Dim sup-zr Env sup))'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return np.minimum(zr_ind(time()), (zr_outflow() - zr_dim_sup() - zr_env_sup()))


@cache('step')
def zr_inflow():
    """
    Real Name: b'Zr inflow'
    Original Eqn: b'zr upstream (Time)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return zr_upstream(time())


@cache('step')
def dom_sup_after_finesk():
    """
    Real Name: b'Dom Sup after Finesk'
    Original Eqn: b'MIN(River aftr Finesk Dam, "Domes-1 Demad finesk" (Time))'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return np.minimum(river_aftr_finesk_dam(), domes1_demad_finesk(time()))


@cache('step')
def wr_def_bfr_div():
    """
    Real Name: b'wr def bfr div'
    Original Eqn: b'wr dem bfr div (Time)-wr sup bfr div'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return wr_dem_bfr_div(time()) - wr_sup_bfr_div()


@cache('step')
def env_tj_sup():
    """
    Real Name: b'Env Tj sup'
    Original Eqn: b'MIN("Tj Div aftr Ab-bn Spill", Env Tj Dem (Time))'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return np.minimum(tj_div_aftr_abbn_spill(), env_tj_dem(time()))


@cache('step')
def wr_dem_aftr_zr_dam():
    """
    Real Name: b'Wr Dem aftr Zr Dam'
    Original Eqn: b'Zr wr dem (Time)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return zr_wr_dem(time())


@cache('step')
def tj_aftr_div():
    """
    Real Name: b'Tj aftr Div'
    Original Eqn: b'Intrfl aftr Div (Time)+Tj Div'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return intrfl_aftr_div(time()) + tj_div()


def wr_dem_shirinrood(x):
    """
    Real Name: b'wr Dem Shirinrood'
    Original Eqn: b'( [(1,0)-(365,0.2)],(1,0.00878),(2,0.00878),(3,0.00878),(4,0.00878),(5,0.00878),(6,0.00878\\\\ ),(7,0.00878),(8,0.00878),(9,0.00878),(10,0.00878),(11,0.00878),(12,0.00878),(13,0.00878\\\\ ),(14,0.00878),(15,0.00878),(16,0.00878),(17,0.00878),(18,0.00878),(19,0.00878),(20\\\\ ,0.00878),(21,0.00878),(22,0.00878),(23,0.00878),(24,0.00878),(25,0.00878),(26,0.00878\\\\ ),(27,0.00878),(28,0.00878),(29,0.00878),(30,0.00878),(31,0),(32,0),(33,0),(34,0),(\\\\ 35,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),\\\\ (47,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0)\\\\ ,(59,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0\\\\ ),(71,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,\\\\ 0),(83,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94\\\\ ,0),(95,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105\\\\ ,0),(106,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0)\\\\ ,(116,0),(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126\\\\ ,0),(127,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0)\\\\ ,(137,0),(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147\\\\ ,0),(148,0),(149,0),(150,0),(151,0.00066),(152,0.00066),(153,0.00066),(154,0.00066)\\\\ ,(155,0.00066),(156,0.00066),(157,0.00066),(158,0.00066),(159,0.00066),(160,0.00066\\\\ ),(161,0.00066),(162,0.00066),(163,0.00066),(164,0.00066),(165,0.00066),(166,0.00066\\\\ ),(167,0.00066),(168,0.00066),(169,0.00066),(170,0.00066),(171,0.00066),(172,0.00066\\\\ ),(173,0.00066),(174,0.00066),(175,0.00066),(176,0.00066),(177,0.00066),(178,0.00066\\\\ ),(179,0.00066),(180,0.00066),(181,0.02452),(182,0.02452),(183,0.02452),(184,0.02452\\\\ ),(185,0.02452),(186,0.02452),(187,0.02452),(188,0.02452),(189,0.02452),(190,0.02452\\\\ ),(191,0.02452),(192,0.02452),(193,0.02452),(194,0.02452),(195,0.02452),(196,0.02452\\\\ ),(197,0.02452),(198,0.02452),(199,0.02452),(200,0.02452),(201,0.02452),(202,0.02452\\\\ ),(203,0.02452),(204,0.02452),(205,0.02452),(206,0.02452),(207,0.02452),(208,0.02452\\\\ ),(209,0.02452),(210,0.02452),(211,0.07626),(212,0.07626),(213,0.07626),(214,0.07626\\\\ ),(215,0.07626),(216,0.07626),(217,0.07626),(218,0.07626),(219,0.07626),(220,0.07626\\\\ ),(221,0.07626),(222,0.07626),(223,0.07626),(224,0.07626),(225,0.07626),(226,0.07626\\\\ ),(227,0.07626),(228,0.07626),(229,0.07626),(230,0.07626),(231,0.07626),(232,0.07626\\\\ ),(233,0.07626),(234,0.07626),(235,0.07626),(236,0.07626),(237,0.07626),(238,0.07626\\\\ ),(239,0.07626),(240,0.07626),(241,0.11028),(242,0.11028),(243,0.11028),(244,0.11028\\\\ ),(245,0.11028),(246,0.11028),(247,0.11028),(248,0.11028),(249,0.11028),(250,0.11028\\\\ ),(251,0.11028),(252,0.11028),(253,0.11028),(254,0.11028),(255,0.11028),(256,0.11028\\\\ ),(257,0.11028),(258,0.11028),(259,0.11028),(260,0.11028),(261,0.11028),(262,0.11028\\\\ ),(263,0.11028),(264,0.11028),(265,0.11028),(266,0.11028),(267,0.11028),(268,0.11028\\\\ ),(269,0.11028),(270,0.11028),(271,0.15799),(272,0.15799),(273,0.15799),(274,0.15799\\\\ ),(275,0.15799),(276,0.15799),(277,0.15799),(278,0.15799),(279,0.15799),(280,0.15799\\\\ ),(281,0.15799),(282,0.15799),(283,0.15799),(284,0.15799),(285,0.15799),(286,0.15799\\\\ ),(287,0.15799),(288,0.15799),(289,0.15799),(290,0.15799),(291,0.15799),(292,0.15799\\\\ ),(293,0.15799),(294,0.15799),(295,0.15799),(296,0.15799),(297,0.15799),(298,0.15799\\\\ ),(299,0.15799),(300,0.15799),(301,0.14253),(302,0.14253),(303,0.14253),(304,0.14253\\\\ ),(305,0.14253),(306,0.14253),(307,0.14253),(308,0.14253),(309,0.14253),(310,0.14253\\\\ ),(311,0.14253),(312,0.14253),(313,0.14253),(314,0.14253),(315,0.14253),(316,0.14253\\\\ ),(317,0.14253),(318,0.14253),(319,0.14253),(320,0.14253),(321,0.14253),(322,0.14253\\\\ ),(323,0.14253),(324,0.14253),(325,0.14253),(326,0.14253),(327,0.14253),(328,0.14253\\\\ ),(329,0.14253),(330,0.14253),(331,0.05832),(332,0.05832),(333,0.05832),(334,0.05832\\\\ ),(335,0.05832),(336,0.05832),(337,0.05832),(338,0.05832),(339,0.05832),(340,0.05832\\\\ ),(341,0.05832),(342,0.05832),(343,0.05832),(344,0.05832),(345,0.05832),(346,0.05832\\\\ ),(347,0.05832),(348,0.05832),(349,0.05832),(350,0.05832),(351,0.05832),(352,0.05832\\\\ ),(353,0.05832),(354,0.05832),(355,0.05832),(356,0.05832),(357,0.05832),(358,0.05832\\\\ ),(359,0.05832),(360,0.05832),(361,0.05832),(362,0.05832),(363,0.05832),(364,0.05832\\\\ ),(365,0.05832))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], [
                                0.00878, 0.00878, 0.00878, 0.00878, 0.00878, 0.00878, 0.00878, 0.00878, 0.00878,
                                0.00878,
                                0.00878, 0.00878, 0.00878, 0.00878, 0.00878, 0.00878, 0.00878, 0.00878, 0.00878,
                                0.00878,
                                0.00878, 0.00878, 0.00878, 0.00878, 0.00878, 0.00878, 0.00878, 0.00878, 0.00878,
                                0.00878,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0.00066, 0.00066, 0.00066, 0.00066, 0.00066, 0.00066, 0.00066, 0.00066, 0.00066,
                                0.00066,
                                0.00066, 0.00066, 0.00066, 0.00066, 0.00066, 0.00066, 0.00066, 0.00066, 0.00066,
                                0.00066,
                                0.00066, 0.00066, 0.00066, 0.00066, 0.00066, 0.00066, 0.00066, 0.00066, 0.00066,
                                0.00066,
                                0.02452, 0.02452, 0.02452, 0.02452, 0.02452, 0.02452, 0.02452, 0.02452, 0.02452,
                                0.02452,
                                0.02452, 0.02452, 0.02452, 0.02452, 0.02452, 0.02452, 0.02452, 0.02452, 0.02452,
                                0.02452,
                                0.02452, 0.02452, 0.02452, 0.02452, 0.02452, 0.02452, 0.02452, 0.02452, 0.02452,
                                0.02452,
                                0.07626, 0.07626, 0.07626, 0.07626, 0.07626, 0.07626, 0.07626, 0.07626, 0.07626,
                                0.07626,
                                0.07626, 0.07626, 0.07626, 0.07626, 0.07626, 0.07626, 0.07626, 0.07626, 0.07626,
                                0.07626,
                                0.07626, 0.07626, 0.07626, 0.07626, 0.07626, 0.07626, 0.07626, 0.07626, 0.07626,
                                0.07626,
                                0.11028, 0.11028, 0.11028, 0.11028, 0.11028, 0.11028, 0.11028, 0.11028, 0.11028,
                                0.11028,
                                0.11028, 0.11028, 0.11028, 0.11028, 0.11028, 0.11028, 0.11028, 0.11028, 0.11028,
                                0.11028,
                                0.11028, 0.11028, 0.11028, 0.11028, 0.11028, 0.11028, 0.11028, 0.11028, 0.11028,
                                0.11028,
                                0.15799, 0.15799, 0.15799, 0.15799, 0.15799, 0.15799, 0.15799, 0.15799, 0.15799,
                                0.15799,
                                0.15799, 0.15799, 0.15799, 0.15799, 0.15799, 0.15799, 0.15799, 0.15799, 0.15799,
                                0.15799,
                                0.15799, 0.15799, 0.15799, 0.15799, 0.15799, 0.15799, 0.15799, 0.15799, 0.15799,
                                0.15799,
                                0.14253, 0.14253, 0.14253, 0.14253, 0.14253, 0.14253, 0.14253, 0.14253, 0.14253,
                                0.14253,
                                0.14253, 0.14253, 0.14253, 0.14253, 0.14253, 0.14253, 0.14253, 0.14253, 0.14253,
                                0.14253,
                                0.14253, 0.14253, 0.14253, 0.14253, 0.14253, 0.14253, 0.14253, 0.14253, 0.14253,
                                0.14253,
                                0.05832, 0.05832, 0.05832, 0.05832, 0.05832, 0.05832, 0.05832, 0.05832, 0.05832,
                                0.05832,
                                0.05832, 0.05832, 0.05832, 0.05832, 0.05832, 0.05832, 0.05832, 0.05832, 0.05832,
                                0.05832,
                                0.05832, 0.05832, 0.05832, 0.05832, 0.05832, 0.05832, 0.05832, 0.05832, 0.05832,
                                0.05832,
                                0.05832, 0.05832, 0.05832, 0.05832, 0.05832
                            ])


def finesk_upstream(x):
    """
    Real Name: b'Finesk Upstream'
    Original Eqn: b'( [(1,0)-(365,0.3)],(1,0.03751),(2,0.03751),(3,0.03751),(4,0.03751),(5,0.03751),(6,0.03751\\\\ ),(7,0.03751),(8,0.03751),(9,0.03751),(10,0.03751),(11,0.03751),(12,0.03751),(13,0.03751\\\\ ),(14,0.03751),(15,0.03751),(16,0.03751),(17,0.03751),(18,0.03751),(19,0.03751),(20\\\\ ,0.03751),(21,0.03751),(22,0.03751),(23,0.03751),(24,0.03751),(25,0.03751),(26,0.03751\\\\ ),(27,0.03751),(28,0.03751),(29,0.03751),(30,0.03751),(31,0.03516),(32,0.03516),(33\\\\ ,0.03516),(34,0.03516),(35,0.03516),(36,0.03516),(37,0.03516),(38,0.03516),(39,0.03516\\\\ ),(40,0.03516),(41,0.03516),(42,0.03516),(43,0.03516),(44,0.03516),(45,0.03516),(46\\\\ ,0.03516),(47,0.03516),(48,0.03516),(49,0.03516),(50,0.03516),(51,0.03516),(52,0.03516\\\\ ),(53,0.03516),(54,0.03516),(55,0.03516),(56,0.03516),(57,0.03516),(58,0.03516),(59\\\\ ,0.03516),(60,0.03516),(61,0.03283),(62,0.03283),(63,0.03283),(64,0.03283),(65,0.03283\\\\ ),(66,0.03283),(67,0.03283),(68,0.03283),(69,0.03283),(70,0.03283),(71,0.03283),(72\\\\ ,0.03283),(73,0.03283),(74,0.03283),(75,0.03283),(76,0.03283),(77,0.03283),(78,0.03283\\\\ ),(79,0.03283),(80,0.03283),(81,0.03283),(82,0.03283),(83,0.03283),(84,0.03283),(85\\\\ ,0.03283),(86,0.03283),(87,0.03283),(88,0.03283),(89,0.03283),(90,0.03283),(91,0.0375\\\\ ),(92,0.0375),(93,0.0375),(94,0.0375),(95,0.0375),(96,0.0375),(97,0.0375),(98,0.0375\\\\ ),(99,0.0375),(100,0.0375),(101,0.0375),(102,0.0375),(103,0.0375),(104,0.0375),(105\\\\ ,0.0375),(106,0.0375),(107,0.0375),(108,0.0375),(109,0.0375),(110,0.0375),(111,0.0375\\\\ ),(112,0.0375),(113,0.0375),(114,0.0375),(115,0.0375),(116,0.0375),(117,0.0375),(118\\\\ ,0.0375),(119,0.0375),(120,0.0375),(121,0.03663),(122,0.03663),(123,0.03663),(124,0.03663\\\\ ),(125,0.03663),(126,0.03663),(127,0.03663),(128,0.03663),(129,0.03663),(130,0.03663\\\\ ),(131,0.03663),(132,0.03663),(133,0.03663),(134,0.03663),(135,0.03663),(136,0.03663\\\\ ),(137,0.03663),(138,0.03663),(139,0.03663),(140,0.03663),(141,0.03663),(142,0.03663\\\\ ),(143,0.03663),(144,0.03663),(145,0.03663),(146,0.03663),(147,0.03663),(148,0.03663\\\\ ),(149,0.03663),(150,0.03663),(151,0.05634),(152,0.05634),(153,0.05634),(154,0.05634\\\\ ),(155,0.05634),(156,0.05634),(157,0.05634),(158,0.05634),(159,0.05634),(160,0.05634\\\\ ),(161,0.05634),(162,0.05634),(163,0.05634),(164,0.05634),(165,0.05634),(166,0.05634\\\\ ),(167,0.05634),(168,0.05634),(169,0.05634),(170,0.05634),(171,0.05634),(172,0.05634\\\\ ),(173,0.05634),(174,0.05634),(175,0.05634),(176,0.05634),(177,0.05634),(178,0.05634\\\\ ),(179,0.05634),(180,0.05634),(181,0.17003),(182,0.17003),(183,0.17003),(184,0.17003\\\\ ),(185,0.17003),(186,0.17003),(187,0.17003),(188,0.17003),(189,0.17003),(190,0.17003\\\\ ),(191,0.17003),(192,0.17003),(193,0.17003),(194,0.17003),(195,0.17003),(196,0.17003\\\\ ),(197,0.17003),(198,0.17003),(199,0.17003),(200,0.17003),(201,0.17003),(202,0.17003\\\\ ),(203,0.17003),(204,0.17003),(205,0.17003),(206,0.17003),(207,0.17003),(208,0.17003\\\\ ),(209,0.17003),(210,0.17003),(211,0.22647),(212,0.22647),(213,0.22647),(214,0.22647\\\\ ),(215,0.22647),(216,0.22647),(217,0.22647),(218,0.22647),(219,0.22647),(220,0.22647\\\\ ),(221,0.22647),(222,0.22647),(223,0.22647),(224,0.22647),(225,0.22647),(226,0.22647\\\\ ),(227,0.22647),(228,0.22647),(229,0.22647),(230,0.22647),(231,0.22647),(232,0.22647\\\\ ),(233,0.22647),(234,0.22647),(235,0.22647),(236,0.22647),(237,0.22647),(238,0.22647\\\\ ),(239,0.22647),(240,0.22647),(241,0.20215),(242,0.20215),(243,0.20215),(244,0.20215\\\\ ),(245,0.20215),(246,0.20215),(247,0.20215),(248,0.20215),(249,0.20215),(250,0.20215\\\\ ),(251,0.20215),(252,0.20215),(253,0.20215),(254,0.20215),(255,0.20215),(256,0.20215\\\\ ),(257,0.20215),(258,0.20215),(259,0.20215),(260,0.20215),(261,0.20215),(262,0.20215\\\\ ),(263,0.20215),(264,0.20215),(265,0.20215),(266,0.20215),(267,0.20215),(268,0.20215\\\\ ),(269,0.20215),(270,0.20215),(271,0.17808),(272,0.17808),(273,0.17808),(274,0.17808\\\\ ),(275,0.17808),(276,0.17808),(277,0.17808),(278,0.17808),(279,0.17808),(280,0.17808\\\\ ),(281,0.17808),(282,0.17808),(283,0.17808),(284,0.17808),(285,0.17808),(286,0.17808\\\\ ),(287,0.17808),(288,0.17808),(289,0.17808),(290,0.17808),(291,0.17808),(292,0.17808\\\\ ),(293,0.17808),(294,0.17808),(295,0.17808),(296,0.17808),(297,0.17808),(298,0.17808\\\\ ),(299,0.17808),(300,0.17808),(301,0.15597),(302,0.15597),(303,0.15597),(304,0.15597\\\\ ),(305,0.15597),(306,0.15597),(307,0.15597),(308,0.15597),(309,0.15597),(310,0.15597\\\\ ),(311,0.15597),(312,0.15597),(313,0.15597),(314,0.15597),(315,0.15597),(316,0.15597\\\\ ),(317,0.15597),(318,0.15597),(319,0.15597),(320,0.15597),(321,0.15597),(322,0.15597\\\\ ),(323,0.15597),(324,0.15597),(325,0.15597),(326,0.15597),(327,0.15597),(328,0.15597\\\\ ),(329,0.15597),(330,0.15597),(331,0.08314),(332,0.08314),(333,0.08314),(334,0.08314\\\\ ),(335,0.08314),(336,0.08314),(337,0.08314),(338,0.08314),(339,0.08314),(340,0.08314\\\\ ),(341,0.08314),(342,0.08314),(343,0.08314),(344,0.08314),(345,0.08314),(346,0.08314\\\\ ),(347,0.08314),(348,0.08314),(349,0.08314),(350,0.08314),(351,0.08314),(352,0.08314\\\\ ),(353,0.08314),(354,0.08314),(355,0.08314),(356,0.08314),(357,0.08314),(358,0.08314\\\\ ),(359,0.08314),(360,0.08314),(361,0.08314),(362,0.08314),(363,0.08314),(364,0.08314\\\\ ),(365,0.08314))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], [
                                0.03751, 0.03751, 0.03751, 0.03751, 0.03751, 0.03751, 0.03751, 0.03751, 0.03751,
                                0.03751,
                                0.03751, 0.03751, 0.03751, 0.03751, 0.03751, 0.03751, 0.03751, 0.03751, 0.03751,
                                0.03751,
                                0.03751, 0.03751, 0.03751, 0.03751, 0.03751, 0.03751, 0.03751, 0.03751, 0.03751,
                                0.03751,
                                0.03516, 0.03516, 0.03516, 0.03516, 0.03516, 0.03516, 0.03516, 0.03516, 0.03516,
                                0.03516,
                                0.03516, 0.03516, 0.03516, 0.03516, 0.03516, 0.03516, 0.03516, 0.03516, 0.03516,
                                0.03516,
                                0.03516, 0.03516, 0.03516, 0.03516, 0.03516, 0.03516, 0.03516, 0.03516, 0.03516,
                                0.03516,
                                0.03283, 0.03283, 0.03283, 0.03283, 0.03283, 0.03283, 0.03283, 0.03283, 0.03283,
                                0.03283,
                                0.03283, 0.03283, 0.03283, 0.03283, 0.03283, 0.03283, 0.03283, 0.03283, 0.03283,
                                0.03283,
                                0.03283, 0.03283, 0.03283, 0.03283, 0.03283, 0.03283, 0.03283, 0.03283, 0.03283,
                                0.03283,
                                0.0375, 0.0375, 0.0375, 0.0375, 0.0375, 0.0375, 0.0375, 0.0375, 0.0375, 0.0375, 0.0375,
                                0.0375, 0.0375, 0.0375, 0.0375, 0.0375, 0.0375, 0.0375, 0.0375, 0.0375, 0.0375, 0.0375,
                                0.0375, 0.0375, 0.0375, 0.0375, 0.0375, 0.0375, 0.0375, 0.0375, 0.03663, 0.03663,
                                0.03663,
                                0.03663, 0.03663, 0.03663, 0.03663, 0.03663, 0.03663, 0.03663, 0.03663, 0.03663,
                                0.03663,
                                0.03663, 0.03663, 0.03663, 0.03663, 0.03663, 0.03663, 0.03663, 0.03663, 0.03663,
                                0.03663,
                                0.03663, 0.03663, 0.03663, 0.03663, 0.03663, 0.03663, 0.03663, 0.05634, 0.05634,
                                0.05634,
                                0.05634, 0.05634, 0.05634, 0.05634, 0.05634, 0.05634, 0.05634, 0.05634, 0.05634,
                                0.05634,
                                0.05634, 0.05634, 0.05634, 0.05634, 0.05634, 0.05634, 0.05634, 0.05634, 0.05634,
                                0.05634,
                                0.05634, 0.05634, 0.05634, 0.05634, 0.05634, 0.05634, 0.05634, 0.17003, 0.17003,
                                0.17003,
                                0.17003, 0.17003, 0.17003, 0.17003, 0.17003, 0.17003, 0.17003, 0.17003, 0.17003,
                                0.17003,
                                0.17003, 0.17003, 0.17003, 0.17003, 0.17003, 0.17003, 0.17003, 0.17003, 0.17003,
                                0.17003,
                                0.17003, 0.17003, 0.17003, 0.17003, 0.17003, 0.17003, 0.17003, 0.22647, 0.22647,
                                0.22647,
                                0.22647, 0.22647, 0.22647, 0.22647, 0.22647, 0.22647, 0.22647, 0.22647, 0.22647,
                                0.22647,
                                0.22647, 0.22647, 0.22647, 0.22647, 0.22647, 0.22647, 0.22647, 0.22647, 0.22647,
                                0.22647,
                                0.22647, 0.22647, 0.22647, 0.22647, 0.22647, 0.22647, 0.22647, 0.20215, 0.20215,
                                0.20215,
                                0.20215, 0.20215, 0.20215, 0.20215, 0.20215, 0.20215, 0.20215, 0.20215, 0.20215,
                                0.20215,
                                0.20215, 0.20215, 0.20215, 0.20215, 0.20215, 0.20215, 0.20215, 0.20215, 0.20215,
                                0.20215,
                                0.20215, 0.20215, 0.20215, 0.20215, 0.20215, 0.20215, 0.20215, 0.17808, 0.17808,
                                0.17808,
                                0.17808, 0.17808, 0.17808, 0.17808, 0.17808, 0.17808, 0.17808, 0.17808, 0.17808,
                                0.17808,
                                0.17808, 0.17808, 0.17808, 0.17808, 0.17808, 0.17808, 0.17808, 0.17808, 0.17808,
                                0.17808,
                                0.17808, 0.17808, 0.17808, 0.17808, 0.17808, 0.17808, 0.17808, 0.15597, 0.15597,
                                0.15597,
                                0.15597, 0.15597, 0.15597, 0.15597, 0.15597, 0.15597, 0.15597, 0.15597, 0.15597,
                                0.15597,
                                0.15597, 0.15597, 0.15597, 0.15597, 0.15597, 0.15597, 0.15597, 0.15597, 0.15597,
                                0.15597,
                                0.15597, 0.15597, 0.15597, 0.15597, 0.15597, 0.15597, 0.15597, 0.08314, 0.08314,
                                0.08314,
                                0.08314, 0.08314, 0.08314, 0.08314, 0.08314, 0.08314, 0.08314, 0.08314, 0.08314,
                                0.08314,
                                0.08314, 0.08314, 0.08314, 0.08314, 0.08314, 0.08314, 0.08314, 0.08314, 0.08314,
                                0.08314,
                                0.08314, 0.08314, 0.08314, 0.08314, 0.08314, 0.08314, 0.08314, 0.08314, 0.08314,
                                0.08314,
                                0.08314, 0.08314
                            ])


@cache('step')
def inflow_finesk():
    """
    Real Name: b'Inflow Finesk'
    Original Eqn: b'IF THEN ELSE( Finesk Upstream (Time)-Wr Sup befr Finesk<=0 , 0, Finesk Upstream (Time\\\\ )-Wr Sup befr Finesk )+(Wr Sup befr Finesk*0.2)'
    Units: b'MCM/Month'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.if_then_else(
        finesk_upstream(time()) - wr_sup_befr_finesk() <= 0, 0,
        finesk_upstream(time()) - wr_sup_befr_finesk()) + (wr_sup_befr_finesk() * 0.2)


@cache('step')
def wr_sup_shirinrood():
    """
    Real Name: b'wr Sup Shirinrood'
    Original Eqn: b'MIN(Shirinrood upstream (Time), wr Dem Shirinrood (Time))'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return np.minimum(shirinrood_upstream(time()), wr_dem_shirinrood(time()))


@cache('step')
def tajan_befr_zarem():
    """
    Real Name: b'Tajan Befr zarem'
    Original Eqn: b'Tajan Dam outflow+Tatal Inter Tajan Dam2zarem (Time)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return tajan_dam_outflow() + tatal_inter_tajan_dam2zarem(time())


@cache('step')
def tj_env_sup():
    """
    Real Name: b'Tj Env Sup'
    Original Eqn: b'MIN(Tj Env Dem (Time), (Tj Outflow-Tj Dom Sup))'
    Units: b''
    Limits: (None, None)
    Type: component

    b'MIN(zr upstream (Time), wr Dem bfr Zr dam (Time))'
    """
    return np.minimum(tj_env_dem(time()), (tj_outflow() - tj_dom_sup()))


@cache('step')
def tajan_dam_upstream():
    """
    Real Name: b'Tajan Dam upstream'
    Original Eqn: b'Parvarij station+Shirinrood upstream (Time)-wr Sup Shirinrood+(wr Sup Shirinrood*0.2\\\\ )'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return parvarij_station() + shirinrood_upstream(
        time()) - wr_sup_shirinrood() + (wr_sup_shirinrood() * 0.2)


@cache('step')
def supply_envi_finesk():
    """
    Real Name: b'Supply envi Finesk'
    Original Eqn: b'MIN(envi Demand Finesk (Time), (outflow Finesk-"Supply Domes-1Finesk") )'
    Units: b'MCM/Month'
    Limits: (None, None)
    Type: component

    b''
    """
    return np.minimum(envi_demand_finesk(time()), (outflow_finesk() - supply_domes1finesk()))


@cache('step')
def supply_domes1finesk():
    """
    Real Name: b'"Supply Domes-1Finesk"'
    Original Eqn: b'MIN("Domes-1 Demad finesk" (Time), (outflow Finesk) )'
    Units: b'MCM/Month'
    Limits: (None, None)
    Type: component

    b''
    """
    return np.minimum(domes1_demad_finesk(time()), (outflow_finesk()))


@cache('step')
def zr_evap():
    """
    Real Name: b'Zr evap'
    Original Eqn: b'Max(0,Zr onthly evap (Time)*"Zr area (km^2)"/1000)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return np.maximum(0, zr_onthly_evap(time()) * zr_area_km2() / 1000)


@cache('step')
def tj_bfr_div():
    """
    Real Name: b'Tj bfr Div'
    Original Eqn: b'Tj aftr Zr+Total Inter Zr2Div (Time)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return tj_aftr_zr() + total_inter_zr2div(time())


@cache('step')
def zr_wr_sup():
    """
    Real Name: b'zr wr sup'
    Original Eqn: b'MIN(Zr wr dem (Time) , Zr outflow - zr Dim sup - zr Env sup - zr Ind sup )'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return np.minimum(zr_wr_dem(time()), zr_outflow() - zr_dim_sup() - zr_env_sup() - zr_ind_sup())


@cache('step')
def zr_env_sup():
    """
    Real Name: b'zr Env sup'
    Original Eqn: b'MIN(zr Env dem (Time), (Zr outflow-zr Dim sup))'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return np.minimum(zr_env_dem(time()), (zr_outflow() - zr_dim_sup()))


@cache('step')
def wr_sup_bfr_div():
    """
    Real Name: b'wr sup bfr div'
    Original Eqn: b'MIN(Tj bfr Div, wr dem bfr div (Time))'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return np.minimum(tj_bfr_div(), wr_dem_bfr_div(time()))


@cache('run')
def abbn_max_vol():
    """
    Real Name: b'"Ab-bn max vol"'
    Original Eqn: b'102'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 102


@cache('run')
def abbn_min_vol():
    """
    Real Name: b'"Ab-bn min vol"'
    Original Eqn: b'25.6'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 25.6


@cache('step')
def abbn_spill():
    """
    Real Name: b'"Ab-bn Spill"'
    Original Eqn: b'IF THEN ELSE((("Ab-bn")+"Ab-bn inflow"-"Ab-bn outflow"-"Ab-bn Eva")>("Ab-bn max vol"\\\\ ), (("Ab-bn" )+"Ab-bn inflow"-"Ab-bn inflow"-"Ab-bn Eva"-("Ab-bn max vol")), 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.if_then_else(
        ((abbn()) + abbn_inflow() - abbn_outflow() - abbn_eva()) > (abbn_max_vol()),
        ((abbn()) + abbn_inflow() - abbn_inflow() - abbn_eva() - (abbn_max_vol())), 0)


@cache('step')
def abbn():
    """
    Real Name: b'"Ab-bn"'
    Original Eqn: b'INTEG ( "Ab-bn inflow"-"Ab-bn Eva"-"Ab-bn outflow"-"Ab-bn Spill", 19)'
    Units: b''
    Limits: (None, None)
    Type: component

    b'"AB-Bandan Inflow"-"AB-Bandan Evaporation"-"AB-Bandan Outflow"-"AB-Bandan \\n    \\t\\tSpil"'
    """
    return _integ_abbn()


@cache('run')
def gw_res():
    """
    Real Name: b'GW Res'
    Original Eqn: b'115*1.2/5'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 115 * 1.2 / 5


@cache('step')
def tj_div():
    """
    Real Name: b'Tj Div'
    Original Eqn: b'Tj bfr Div-wr sup bfr div+(wr sup bfr div*0.2)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return tj_bfr_div() - wr_sup_bfr_div() + (wr_sup_bfr_div() * 0.2)


def intrfl_aftr_div(x):
    """
    Real Name: b'Intrfl aftr Div'
    Original Eqn: b'( [(1,0)-(365,0.6)],(1,0.05275),(2,0.05275),(3,0.05275),(4,0.05275),(5,0.05275),(6,0.05275\\\\ ),(7,0.05275),(8,0.05275),(9,0.05275),(10,0.05275),(11,0.05275),(12,0.05275),(13,0.05275\\\\ ),(14,0.05275),(15,0.05275),(16,0.05275),(17,0.05275),(18,0.05275),(19,0.05275),(20\\\\ ,0.05275),(21,0.05275),(22,0.05275),(23,0.05275),(24,0.05275),(25,0.05275),(26,0.05275\\\\ ),(27,0.05275),(28,0.05275),(29,0.05275),(30,0.05275),(31,0.16696),(32,0.16696),(33\\\\ ,0.16696),(34,0.16696),(35,0.16696),(36,0.16696),(37,0.16696),(38,0.16696),(39,0.16696\\\\ ),(40,0.16696),(41,0.16696),(42,0.16696),(43,0.16696),(44,0.16696),(45,0.16696),(46\\\\ ,0.16696),(47,0.16696),(48,0.16696),(49,0.16696),(50,0.16696),(51,0.16696),(52,0.16696\\\\ ),(53,0.16696),(54,0.16696),(55,0.16696),(56,0.16696),(57,0.16696),(58,0.16696),(59\\\\ ,0.16696),(60,0.16696),(61,0.11057),(62,0.11057),(63,0.11057),(64,0.11057),(65,0.11057\\\\ ),(66,0.11057),(67,0.11057),(68,0.11057),(69,0.11057),(70,0.11057),(71,0.11057),(72\\\\ ,0.11057),(73,0.11057),(74,0.11057),(75,0.11057),(76,0.11057),(77,0.11057),(78,0.11057\\\\ ),(79,0.11057),(80,0.11057),(81,0.11057),(82,0.11057),(83,0.11057),(84,0.11057),(85\\\\ ,0.11057),(86,0.11057),(87,0.11057),(88,0.11057),(89,0.11057),(90,0.11057),(91,0.16922\\\\ ),(92,0.16922),(93,0.16922),(94,0.16922),(95,0.16922),(96,0.16922),(97,0.16922),(98\\\\ ,0.16922),(99,0.16922),(100,0.16922),(101,0.16922),(102,0.16922),(103,0.16922),(104\\\\ ,0.16922),(105,0.16922),(106,0.16922),(107,0.16922),(108,0.16922),(109,0.16922),(110\\\\ ,0.16922),(111,0.16922),(112,0.16922),(113,0.16922),(114,0.16922),(115,0.16922),(116\\\\ ,0.16922),(117,0.16922),(118,0.16922),(119,0.16922),(120,0.16922),(121,0.4248),(122\\\\ ,0.4248),(123,0.4248),(124,0.4248),(125,0.4248),(126,0.4248),(127,0.4248),(128,0.4248\\\\ ),(129,0.4248),(130,0.4248),(131,0.4248),(132,0.4248),(133,0.4248),(134,0.4248),(135\\\\ ,0.4248),(136,0.4248),(137,0.4248),(138,0.4248),(139,0.4248),(140,0.4248),(141,0.4248\\\\ ),(142,0.4248),(143,0.4248),(144,0.4248),(145,0.4248),(146,0.4248),(147,0.4248),(148\\\\ ,0.4248),(149,0.4248),(150,0.4248),(151,0.58497),(152,0.58497),(153,0.58497),(154,0.58497\\\\ ),(155,0.58497),(156,0.58497),(157,0.58497),(158,0.58497),(159,0.58497),(160,0.58497\\\\ ),(161,0.58497),(162,0.58497),(163,0.58497),(164,0.58497),(165,0.58497),(166,0.58497\\\\ ),(167,0.58497),(168,0.58497),(169,0.58497),(170,0.58497),(171,0.58497),(172,0.58497\\\\ ),(173,0.58497),(174,0.58497),(175,0.58497),(176,0.58497),(177,0.58497),(178,0.58497\\\\ ),(179,0.58497),(180,0.58497),(181,0.32873),(182,0.32873),(183,0.32873),(184,0.32873\\\\ ),(185,0.32873),(186,0.32873),(187,0.32873),(188,0.32873),(189,0.32873),(190,0.32873\\\\ ),(191,0.32873),(192,0.32873),(193,0.32873),(194,0.32873),(195,0.32873),(196,0.32873\\\\ ),(197,0.32873),(198,0.32873),(199,0.32873),(200,0.32873),(201,0.32873),(202,0.32873\\\\ ),(203,0.32873),(204,0.32873),(205,0.32873),(206,0.32873),(207,0.32873),(208,0.32873\\\\ ),(209,0.32873),(210,0.32873),(211,0.10324),(212,0.10324),(213,0.10324),(214,0.10324\\\\ ),(215,0.10324),(216,0.10324),(217,0.10324),(218,0.10324),(219,0.10324),(220,0.10324\\\\ ),(221,0.10324),(222,0.10324),(223,0.10324),(224,0.10324),(225,0.10324),(226,0.10324\\\\ ),(227,0.10324),(228,0.10324),(229,0.10324),(230,0.10324),(231,0.10324),(232,0.10324\\\\ ),(233,0.10324),(234,0.10324),(235,0.10324),(236,0.10324),(237,0.10324),(238,0.10324\\\\ ),(239,0.10324),(240,0.10324),(241,0.03038),(242,0.03038),(243,0.03038),(244,0.03038\\\\ ),(245,0.03038),(246,0.03038),(247,0.03038),(248,0.03038),(249,0.03038),(250,0.03038\\\\ ),(251,0.03038),(252,0.03038),(253,0.03038),(254,0.03038),(255,0.03038),(256,0.03038\\\\ ),(257,0.03038),(258,0.03038),(259,0.03038),(260,0.03038),(261,0.03038),(262,0.03038\\\\ ),(263,0.03038),(264,0.03038),(265,0.03038),(266,0.03038),(267,0.03038),(268,0.03038\\\\ ),(269,0.03038),(270,0.03038),(271,0.00313),(272,0.00313),(273,0.00313),(274,0.00313\\\\ ),(275,0.00313),(276,0.00313),(277,0.00313),(278,0.00313),(279,0.00313),(280,0.00313\\\\ ),(281,0.00313),(282,0.00313),(283,0.00313),(284,0.00313),(285,0.00313),(286,0.00313\\\\ ),(287,0.00313),(288,0.00313),(289,0.00313),(290,0.00313),(291,0.00313),(292,0.00313\\\\ ),(293,0.00313),(294,0.00313),(295,0.00313),(296,0.00313),(297,0.00313),(298,0.00313\\\\ ),(299,0.00313),(300,0.00313),(301,0),(302,0),(303,0),(304,0),(305,0),(306,0),(307,\\\\ 0),(308,0),(309,0),(310,0),(311,0),(312,0),(313,0),(314,0),(315,0),(316,0),(317,0),\\\\ (318,0),(319,0),(320,0),(321,0),(322,0),(323,0),(324,0),(325,0),(326,0),(327,0),(328\\\\ ,0),(329,0),(330,0),(331,0.00564),(332,0.00564),(333,0.00564),(334,0.00564),(335,0.00564\\\\ ),(336,0.00564),(337,0.00564),(338,0.00564),(339,0.00564),(340,0.00564),(341,0.00564\\\\ ),(342,0.00564),(343,0.00564),(344,0.00564),(345,0.00564),(346,0.00564),(347,0.00564\\\\ ),(348,0.00564),(349,0.00564),(350,0.00564),(351,0.00564),(352,0.00564),(353,0.00564\\\\ ),(354,0.00564),(355,0.00564),(356,0.00564),(357,0.00564),(358,0.00564),(359,0.00564\\\\ ),(360,0.00564),(361,0.00564),(362,0.00564),(363,0.00564),(364,0.00564),(365,0.00564\\\\ ))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b'\\u0645\\u0642\\u0627\\u062f\\u06cc\\u0631 \\u0622\\u0628\\u062f\\u0647\\u06cc \\u0637\\u0628\\u06cc\\u0639\\u06cc \\u0628\\u0639\\u062f \\u0627\\u0632 \\u0628\\u0646\\u062f \\u0627\\u0646\\u062d\\u0631\\u0627\\u0641\\u06cc \\n    \\t\\t\\u062a\\u062c\\u0646 \\u062a\\u0627 \\u067e\\u0627\\u06cc\\u0627\\u0628'
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], [
                                0.05275, 0.05275, 0.05275, 0.05275, 0.05275, 0.05275, 0.05275, 0.05275, 0.05275,
                                0.05275,
                                0.05275, 0.05275, 0.05275, 0.05275, 0.05275, 0.05275, 0.05275, 0.05275, 0.05275,
                                0.05275,
                                0.05275, 0.05275, 0.05275, 0.05275, 0.05275, 0.05275, 0.05275, 0.05275, 0.05275,
                                0.05275,
                                0.16696, 0.16696, 0.16696, 0.16696, 0.16696, 0.16696, 0.16696, 0.16696, 0.16696,
                                0.16696,
                                0.16696, 0.16696, 0.16696, 0.16696, 0.16696, 0.16696, 0.16696, 0.16696, 0.16696,
                                0.16696,
                                0.16696, 0.16696, 0.16696, 0.16696, 0.16696, 0.16696, 0.16696, 0.16696, 0.16696,
                                0.16696,
                                0.11057, 0.11057, 0.11057, 0.11057, 0.11057, 0.11057, 0.11057, 0.11057, 0.11057,
                                0.11057,
                                0.11057, 0.11057, 0.11057, 0.11057, 0.11057, 0.11057, 0.11057, 0.11057, 0.11057,
                                0.11057,
                                0.11057, 0.11057, 0.11057, 0.11057, 0.11057, 0.11057, 0.11057, 0.11057, 0.11057,
                                0.11057,
                                0.16922, 0.16922, 0.16922, 0.16922, 0.16922, 0.16922, 0.16922, 0.16922, 0.16922,
                                0.16922,
                                0.16922, 0.16922, 0.16922, 0.16922, 0.16922, 0.16922, 0.16922, 0.16922, 0.16922,
                                0.16922,
                                0.16922, 0.16922, 0.16922, 0.16922, 0.16922, 0.16922, 0.16922, 0.16922, 0.16922,
                                0.16922,
                                0.4248, 0.4248, 0.4248, 0.4248, 0.4248, 0.4248, 0.4248, 0.4248, 0.4248, 0.4248, 0.4248,
                                0.4248, 0.4248, 0.4248, 0.4248, 0.4248, 0.4248, 0.4248, 0.4248, 0.4248, 0.4248, 0.4248,
                                0.4248, 0.4248, 0.4248, 0.4248, 0.4248, 0.4248, 0.4248, 0.4248, 0.58497, 0.58497,
                                0.58497,
                                0.58497, 0.58497, 0.58497, 0.58497, 0.58497, 0.58497, 0.58497, 0.58497, 0.58497,
                                0.58497,
                                0.58497, 0.58497, 0.58497, 0.58497, 0.58497, 0.58497, 0.58497, 0.58497, 0.58497,
                                0.58497,
                                0.58497, 0.58497, 0.58497, 0.58497, 0.58497, 0.58497, 0.58497, 0.32873, 0.32873,
                                0.32873,
                                0.32873, 0.32873, 0.32873, 0.32873, 0.32873, 0.32873, 0.32873, 0.32873, 0.32873,
                                0.32873,
                                0.32873, 0.32873, 0.32873, 0.32873, 0.32873, 0.32873, 0.32873, 0.32873, 0.32873,
                                0.32873,
                                0.32873, 0.32873, 0.32873, 0.32873, 0.32873, 0.32873, 0.32873, 0.10324, 0.10324,
                                0.10324,
                                0.10324, 0.10324, 0.10324, 0.10324, 0.10324, 0.10324, 0.10324, 0.10324, 0.10324,
                                0.10324,
                                0.10324, 0.10324, 0.10324, 0.10324, 0.10324, 0.10324, 0.10324, 0.10324, 0.10324,
                                0.10324,
                                0.10324, 0.10324, 0.10324, 0.10324, 0.10324, 0.10324, 0.10324, 0.03038, 0.03038,
                                0.03038,
                                0.03038, 0.03038, 0.03038, 0.03038, 0.03038, 0.03038, 0.03038, 0.03038, 0.03038,
                                0.03038,
                                0.03038, 0.03038, 0.03038, 0.03038, 0.03038, 0.03038, 0.03038, 0.03038, 0.03038,
                                0.03038,
                                0.03038, 0.03038, 0.03038, 0.03038, 0.03038, 0.03038, 0.03038, 0.00313, 0.00313,
                                0.00313,
                                0.00313, 0.00313, 0.00313, 0.00313, 0.00313, 0.00313, 0.00313, 0.00313, 0.00313,
                                0.00313,
                                0.00313, 0.00313, 0.00313, 0.00313, 0.00313, 0.00313, 0.00313, 0.00313, 0.00313,
                                0.00313,
                                0.00313, 0.00313, 0.00313, 0.00313, 0.00313, 0.00313, 0.00313, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.00564, 0.00564,
                                0.00564,
                                0.00564, 0.00564, 0.00564, 0.00564, 0.00564, 0.00564, 0.00564, 0.00564, 0.00564,
                                0.00564,
                                0.00564, 0.00564, 0.00564, 0.00564, 0.00564, 0.00564, 0.00564, 0.00564, 0.00564,
                                0.00564,
                                0.00564, 0.00564, 0.00564, 0.00564, 0.00564, 0.00564, 0.00564, 0.00564, 0.00564,
                                0.00564,
                                0.00564, 0.00564
                            ])


@cache('run')
def area_abbn():
    """
    Real Name: b'"area ab-bn"'
    Original Eqn: b'49.9'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 49.9


def env_tj_dem(x):
    """
    Real Name: b'Env Tj Dem'
    Original Eqn: b'( [(1,0)-(365,0.5)],(1,0.23328),(2,0.23328),(3,0.23328),(4,0.23328),(5,0.23328),(6,0.23328\\\\ ),(7,0.23328),(8,0.23328),(9,0.23328),(10,0.23328),(11,0.23328),(12,0.23328),(13,0.23328\\\\ ),(14,0.23328),(15,0.23328),(16,0.23328),(17,0.23328),(18,0.23328),(19,0.23328),(20\\\\ ,0.23328),(21,0.23328),(22,0.23328),(23,0.23328),(24,0.23328),(25,0.23328),(26,0.23328\\\\ ),(27,0.23328),(28,0.23328),(29,0.23328),(30,0.23328),(31,0.25056),(32,0.25056),(33\\\\ ,0.25056),(34,0.25056),(35,0.25056),(36,0.25056),(37,0.25056),(38,0.25056),(39,0.25056\\\\ ),(40,0.25056),(41,0.25056),(42,0.25056),(43,0.25056),(44,0.25056),(45,0.25056),(46\\\\ ,0.25056),(47,0.25056),(48,0.25056),(49,0.25056),(50,0.25056),(51,0.25056),(52,0.25056\\\\ ),(53,0.25056),(54,0.25056),(55,0.25056),(56,0.25056),(57,0.25056),(58,0.25056),(59\\\\ ,0.25056),(60,0.25056),(61,0.32832),(62,0.32832),(63,0.32832),(64,0.32832),(65,0.32832\\\\ ),(66,0.32832),(67,0.32832),(68,0.32832),(69,0.32832),(70,0.32832),(71,0.32832),(72\\\\ ,0.32832),(73,0.32832),(74,0.32832),(75,0.32832),(76,0.32832),(77,0.32832),(78,0.32832\\\\ ),(79,0.32832),(80,0.32832),(81,0.32832),(82,0.32832),(83,0.32832),(84,0.32832),(85\\\\ ,0.32832),(86,0.32832),(87,0.32832),(88,0.32832),(89,0.32832),(90,0.32832),(91,0.19008\\\\ ),(92,0.19008),(93,0.19008),(94,0.19008),(95,0.19008),(96,0.19008),(97,0.19008),(98\\\\ ,0.19008),(99,0.19008),(100,0.19008),(101,0.19008),(102,0.19008),(103,0.19008),(104\\\\ ,0.19008),(105,0.19008),(106,0.19008),(107,0.19008),(108,0.19008),(109,0.19008),(110\\\\ ,0.19008),(111,0.19008),(112,0.19008),(113,0.19008),(114,0.19008),(115,0.19008),(116\\\\ ,0.19008),(117,0.19008),(118,0.19008),(119,0.19008),(120,0.19008),(121,0.23328),(122\\\\ ,0.23328),(123,0.23328),(124,0.23328),(125,0.23328),(126,0.23328),(127,0.23328),(128\\\\ ,0.23328),(129,0.23328),(130,0.23328),(131,0.23328),(132,0.23328),(133,0.23328),(134\\\\ ,0.23328),(135,0.23328),(136,0.23328),(137,0.23328),(138,0.23328),(139,0.23328),(140\\\\ ,0.23328),(141,0.23328),(142,0.23328),(143,0.23328),(144,0.23328),(145,0.23328),(146\\\\ ,0.23328),(147,0.23328),(148,0.23328),(149,0.23328),(150,0.23328),(151,0.37063),(152\\\\ ,0.37063),(153,0.37063),(154,0.37063),(155,0.37063),(156,0.37063),(157,0.37063),(158\\\\ ,0.37063),(159,0.37063),(160,0.37063),(161,0.37063),(162,0.37063),(163,0.37063),(164\\\\ ,0.37063),(165,0.37063),(166,0.37063),(167,0.37063),(168,0.37063),(169,0.37063),(170\\\\ ,0.37063),(171,0.37063),(172,0.37063),(173,0.37063),(174,0.37063),(175,0.37063),(176\\\\ ,0.37063),(177,0.37063),(178,0.37063),(179,0.37063),(180,0.37063),(181,0.41063),(182\\\\ ,0.41063),(183,0.41063),(184,0.41063),(185,0.41063),(186,0.41063),(187,0.41063),(188\\\\ ,0.41063),(189,0.41063),(190,0.41063),(191,0.41063),(192,0.41063),(193,0.41063),(194\\\\ ,0.41063),(195,0.41063),(196,0.41063),(197,0.41063),(198,0.41063),(199,0.41063),(200\\\\ ,0.41063),(201,0.41063),(202,0.41063),(203,0.41063),(204,0.41063),(205,0.41063),(206\\\\ ,0.41063),(207,0.41063),(208,0.41063),(209,0.41063),(210,0.41063),(211,0.32136),(212\\\\ ,0.32136),(213,0.32136),(214,0.32136),(215,0.32136),(216,0.32136),(217,0.32136),(218\\\\ ,0.32136),(219,0.32136),(220,0.32136),(221,0.32136),(222,0.32136),(223,0.32136),(224\\\\ ,0.32136),(225,0.32136),(226,0.32136),(227,0.32136),(228,0.32136),(229,0.32136),(230\\\\ ,0.32136),(231,0.32136),(232,0.32136),(233,0.32136),(234,0.32136),(235,0.32136),(236\\\\ ,0.32136),(237,0.32136),(238,0.32136),(239,0.32136),(240,0.32136),(241,0.2678),(242\\\\ ,0.2678),(243,0.2678),(244,0.2678),(245,0.2678),(246,0.2678),(247,0.2678),(248,0.2678\\\\ ),(249,0.2678),(250,0.2678),(251,0.2678),(252,0.2678),(253,0.2678),(254,0.2678),(255\\\\ ,0.2678),(256,0.2678),(257,0.2678),(258,0.2678),(259,0.2678),(260,0.2678),(261,0.2678\\\\ ),(262,0.2678),(263,0.2678),(264,0.2678),(265,0.2678),(266,0.2678),(267,0.2678),(268\\\\ ,0.2678),(269,0.2678),(270,0.2678),(271,0.24995),(272,0.24995),(273,0.24995),(274,0.24995\\\\ ),(275,0.24995),(276,0.24995),(277,0.24995),(278,0.24995),(279,0.24995),(280,0.24995\\\\ ),(281,0.24995),(282,0.24995),(283,0.24995),(284,0.24995),(285,0.24995),(286,0.24995\\\\ ),(287,0.24995),(288,0.24995),(289,0.24995),(290,0.24995),(291,0.24995),(292,0.24995\\\\ ),(293,0.24995),(294,0.24995),(295,0.24995),(296,0.24995),(297,0.24995),(298,0.24995\\\\ ),(299,0.24995),(300,0.24995),(301,0.21424),(302,0.21424),(303,0.21424),(304,0.21424\\\\ ),(305,0.21424),(306,0.21424),(307,0.21424),(308,0.21424),(309,0.21424),(310,0.21424\\\\ ),(311,0.21424),(312,0.21424),(313,0.21424),(314,0.21424),(315,0.21424),(316,0.21424\\\\ ),(317,0.21424),(318,0.21424),(319,0.21424),(320,0.21424),(321,0.21424),(322,0.21424\\\\ ),(323,0.21424),(324,0.21424),(325,0.21424),(326,0.21424),(327,0.21424),(328,0.21424\\\\ ),(329,0.21424),(330,0.21424),(331,0.20531),(332,0.20531),(333,0.20531),(334,0.20531\\\\ ),(335,0.20531),(336,0.20531),(337,0.20531),(338,0.20531),(339,0.20531),(340,0.20531\\\\ ),(341,0.20531),(342,0.20531),(343,0.20531),(344,0.20531),(345,0.20531),(346,0.20531\\\\ ),(347,0.20531),(348,0.20531),(349,0.20531),(350,0.20531),(351,0.20531),(352,0.20531\\\\ ),(353,0.20531),(354,0.20531),(355,0.20531),(356,0.20531),(357,0.20531),(358,0.20531\\\\ ),(359,0.20531),(360,0.20531),(361,0.20531),(362,0.20531),(363,0.20531),(364,0.20531\\\\ ),(365,0.20531))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], [
                                0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328,
                                0.23328,
                                0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328,
                                0.23328,
                                0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328,
                                0.23328,
                                0.25056, 0.25056, 0.25056, 0.25056, 0.25056, 0.25056, 0.25056, 0.25056, 0.25056,
                                0.25056,
                                0.25056, 0.25056, 0.25056, 0.25056, 0.25056, 0.25056, 0.25056, 0.25056, 0.25056,
                                0.25056,
                                0.25056, 0.25056, 0.25056, 0.25056, 0.25056, 0.25056, 0.25056, 0.25056, 0.25056,
                                0.25056,
                                0.32832, 0.32832, 0.32832, 0.32832, 0.32832, 0.32832, 0.32832, 0.32832, 0.32832,
                                0.32832,
                                0.32832, 0.32832, 0.32832, 0.32832, 0.32832, 0.32832, 0.32832, 0.32832, 0.32832,
                                0.32832,
                                0.32832, 0.32832, 0.32832, 0.32832, 0.32832, 0.32832, 0.32832, 0.32832, 0.32832,
                                0.32832,
                                0.19008, 0.19008, 0.19008, 0.19008, 0.19008, 0.19008, 0.19008, 0.19008, 0.19008,
                                0.19008,
                                0.19008, 0.19008, 0.19008, 0.19008, 0.19008, 0.19008, 0.19008, 0.19008, 0.19008,
                                0.19008,
                                0.19008, 0.19008, 0.19008, 0.19008, 0.19008, 0.19008, 0.19008, 0.19008, 0.19008,
                                0.19008,
                                0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328,
                                0.23328,
                                0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328,
                                0.23328,
                                0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328,
                                0.23328,
                                0.37063, 0.37063, 0.37063, 0.37063, 0.37063, 0.37063, 0.37063, 0.37063, 0.37063,
                                0.37063,
                                0.37063, 0.37063, 0.37063, 0.37063, 0.37063, 0.37063, 0.37063, 0.37063, 0.37063,
                                0.37063,
                                0.37063, 0.37063, 0.37063, 0.37063, 0.37063, 0.37063, 0.37063, 0.37063, 0.37063,
                                0.37063,
                                0.41063, 0.41063, 0.41063, 0.41063, 0.41063, 0.41063, 0.41063, 0.41063, 0.41063,
                                0.41063,
                                0.41063, 0.41063, 0.41063, 0.41063, 0.41063, 0.41063, 0.41063, 0.41063, 0.41063,
                                0.41063,
                                0.41063, 0.41063, 0.41063, 0.41063, 0.41063, 0.41063, 0.41063, 0.41063, 0.41063,
                                0.41063,
                                0.32136, 0.32136, 0.32136, 0.32136, 0.32136, 0.32136, 0.32136, 0.32136, 0.32136,
                                0.32136,
                                0.32136, 0.32136, 0.32136, 0.32136, 0.32136, 0.32136, 0.32136, 0.32136, 0.32136,
                                0.32136,
                                0.32136, 0.32136, 0.32136, 0.32136, 0.32136, 0.32136, 0.32136, 0.32136, 0.32136,
                                0.32136,
                                0.2678, 0.2678, 0.2678, 0.2678, 0.2678, 0.2678, 0.2678, 0.2678, 0.2678, 0.2678, 0.2678,
                                0.2678, 0.2678, 0.2678, 0.2678, 0.2678, 0.2678, 0.2678, 0.2678, 0.2678, 0.2678, 0.2678,
                                0.2678, 0.2678, 0.2678, 0.2678, 0.2678, 0.2678, 0.2678, 0.2678, 0.24995, 0.24995,
                                0.24995,
                                0.24995, 0.24995, 0.24995, 0.24995, 0.24995, 0.24995, 0.24995, 0.24995, 0.24995,
                                0.24995,
                                0.24995, 0.24995, 0.24995, 0.24995, 0.24995, 0.24995, 0.24995, 0.24995, 0.24995,
                                0.24995,
                                0.24995, 0.24995, 0.24995, 0.24995, 0.24995, 0.24995, 0.24995, 0.21424, 0.21424,
                                0.21424,
                                0.21424, 0.21424, 0.21424, 0.21424, 0.21424, 0.21424, 0.21424, 0.21424, 0.21424,
                                0.21424,
                                0.21424, 0.21424, 0.21424, 0.21424, 0.21424, 0.21424, 0.21424, 0.21424, 0.21424,
                                0.21424,
                                0.21424, 0.21424, 0.21424, 0.21424, 0.21424, 0.21424, 0.21424, 0.20531, 0.20531,
                                0.20531,
                                0.20531, 0.20531, 0.20531, 0.20531, 0.20531, 0.20531, 0.20531, 0.20531, 0.20531,
                                0.20531,
                                0.20531, 0.20531, 0.20531, 0.20531, 0.20531, 0.20531, 0.20531, 0.20531, 0.20531,
                                0.20531,
                                0.20531, 0.20531, 0.20531, 0.20531, 0.20531, 0.20531, 0.20531, 0.20531, 0.20531,
                                0.20531,
                                0.20531, 0.20531
                            ])


@cache('step')
def tj_bfr_sea():
    """
    Real Name: b'Tj bfr Sea'
    Original Eqn: b'"Tj Div aftr Ab-bn Spill"-Agri sup frm SW+(Agri sup frm SW*0.2)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return tj_div_aftr_abbn_spill() - agri_sup_frm_sw() + (agri_sup_frm_sw() * 0.2)


def wr_dem_bfr_div(x):
    """
    Real Name: b'wr dem bfr div'
    Original Eqn: b'( [(1,0)-(365,0.3)],(1,0.01341),(2,0.01341),(3,0.01341),(4,0.01341),(5,0.01341),(6,0.01341\\\\ ),(7,0.01341),(8,0.01341),(9,0.01341),(10,0.01341),(11,0.01341),(12,0.01341),(13,0.01341\\\\ ),(14,0.01341),(15,0.01341),(16,0.01341),(17,0.01341),(18,0.01341),(19,0.01341),(20\\\\ ,0.01341),(21,0.01341),(22,0.01341),(23,0.01341),(24,0.01341),(25,0.01341),(26,0.01341\\\\ ),(27,0.01341),(28,0.01341),(29,0.01341),(30,0.01341),(31,0),(32,0),(33,0),(34,0),(\\\\ 35,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),\\\\ (47,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0)\\\\ ,(59,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0\\\\ ),(71,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,\\\\ 0),(83,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94\\\\ ,0),(95,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105\\\\ ,0),(106,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0)\\\\ ,(116,0),(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126\\\\ ,0),(127,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0)\\\\ ,(137,0),(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147\\\\ ,0),(148,0),(149,0),(150,0),(151,0.00101),(152,0.00101),(153,0.00101),(154,0.00101)\\\\ ,(155,0.00101),(156,0.00101),(157,0.00101),(158,0.00101),(159,0.00101),(160,0.00101\\\\ ),(161,0.00101),(162,0.00101),(163,0.00101),(164,0.00101),(165,0.00101),(166,0.00101\\\\ ),(167,0.00101),(168,0.00101),(169,0.00101),(170,0.00101),(171,0.00101),(172,0.00101\\\\ ),(173,0.00101),(174,0.00101),(175,0.00101),(176,0.00101),(177,0.00101),(178,0.00101\\\\ ),(179,0.00101),(180,0.00101),(181,0.03745),(182,0.03745),(183,0.03745),(184,0.03745\\\\ ),(185,0.03745),(186,0.03745),(187,0.03745),(188,0.03745),(189,0.03745),(190,0.03745\\\\ ),(191,0.03745),(192,0.03745),(193,0.03745),(194,0.03745),(195,0.03745),(196,0.03745\\\\ ),(197,0.03745),(198,0.03745),(199,0.03745),(200,0.03745),(201,0.03745),(202,0.03745\\\\ ),(203,0.03745),(204,0.03745),(205,0.03745),(206,0.03745),(207,0.03745),(208,0.03745\\\\ ),(209,0.03745),(210,0.03745),(211,0.11647),(212,0.11647),(213,0.11647),(214,0.11647\\\\ ),(215,0.11647),(216,0.11647),(217,0.11647),(218,0.11647),(219,0.11647),(220,0.11647\\\\ ),(221,0.11647),(222,0.11647),(223,0.11647),(224,0.11647),(225,0.11647),(226,0.11647\\\\ ),(227,0.11647),(228,0.11647),(229,0.11647),(230,0.11647),(231,0.11647),(232,0.11647\\\\ ),(233,0.11647),(234,0.11647),(235,0.11647),(236,0.11647),(237,0.11647),(238,0.11647\\\\ ),(239,0.11647),(240,0.11647),(241,0.16842),(242,0.16842),(243,0.16842),(244,0.16842\\\\ ),(245,0.16842),(246,0.16842),(247,0.16842),(248,0.16842),(249,0.16842),(250,0.16842\\\\ ),(251,0.16842),(252,0.16842),(253,0.16842),(254,0.16842),(255,0.16842),(256,0.16842\\\\ ),(257,0.16842),(258,0.16842),(259,0.16842),(260,0.16842),(261,0.16842),(262,0.16842\\\\ ),(263,0.16842),(264,0.16842),(265,0.16842),(266,0.16842),(267,0.16842),(268,0.16842\\\\ ),(269,0.16842),(270,0.16842),(271,0.24129),(272,0.24129),(273,0.24129),(274,0.24129\\\\ ),(275,0.24129),(276,0.24129),(277,0.24129),(278,0.24129),(279,0.24129),(280,0.24129\\\\ ),(281,0.24129),(282,0.24129),(283,0.24129),(284,0.24129),(285,0.24129),(286,0.24129\\\\ ),(287,0.24129),(288,0.24129),(289,0.24129),(290,0.24129),(291,0.24129),(292,0.24129\\\\ ),(293,0.24129),(294,0.24129),(295,0.24129),(296,0.24129),(297,0.24129),(298,0.24129\\\\ ),(299,0.24129),(300,0.24129),(301,0.21767),(302,0.21767),(303,0.21767),(304,0.21767\\\\ ),(305,0.21767),(306,0.21767),(307,0.21767),(308,0.21767),(309,0.21767),(310,0.21767\\\\ ),(311,0.21767),(312,0.21767),(313,0.21767),(314,0.21767),(315,0.21767),(316,0.21767\\\\ ),(317,0.21767),(318,0.21767),(319,0.21767),(320,0.21767),(321,0.21767),(322,0.21767\\\\ ),(323,0.21767),(324,0.21767),(325,0.21767),(326,0.21767),(327,0.21767),(328,0.21767\\\\ ),(329,0.21767),(330,0.21767),(331,0.08906),(332,0.08906),(333,0.08906),(334,0.08906\\\\ ),(335,0.08906),(336,0.08906),(337,0.08906),(338,0.08906),(339,0.08906),(340,0.08906\\\\ ),(341,0.08906),(342,0.08906),(343,0.08906),(344,0.08906),(345,0.08906),(346,0.08906\\\\ ),(347,0.08906),(348,0.08906),(349,0.08906),(350,0.08906),(351,0.08906),(352,0.08906\\\\ ),(353,0.08906),(354,0.08906),(355,0.08906),(356,0.08906),(357,0.08906),(358,0.08906\\\\ ),(359,0.08906),(360,0.08906),(361,0.08906),(362,0.08906),(363,0.08906),(364,0.08906\\\\ ),(365,0.08906))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], [
                                0.01341, 0.01341, 0.01341, 0.01341, 0.01341, 0.01341, 0.01341, 0.01341, 0.01341,
                                0.01341,
                                0.01341, 0.01341, 0.01341, 0.01341, 0.01341, 0.01341, 0.01341, 0.01341, 0.01341,
                                0.01341,
                                0.01341, 0.01341, 0.01341, 0.01341, 0.01341, 0.01341, 0.01341, 0.01341, 0.01341,
                                0.01341,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0.00101, 0.00101, 0.00101, 0.00101, 0.00101, 0.00101, 0.00101, 0.00101, 0.00101,
                                0.00101,
                                0.00101, 0.00101, 0.00101, 0.00101, 0.00101, 0.00101, 0.00101, 0.00101, 0.00101,
                                0.00101,
                                0.00101, 0.00101, 0.00101, 0.00101, 0.00101, 0.00101, 0.00101, 0.00101, 0.00101,
                                0.00101,
                                0.03745, 0.03745, 0.03745, 0.03745, 0.03745, 0.03745, 0.03745, 0.03745, 0.03745,
                                0.03745,
                                0.03745, 0.03745, 0.03745, 0.03745, 0.03745, 0.03745, 0.03745, 0.03745, 0.03745,
                                0.03745,
                                0.03745, 0.03745, 0.03745, 0.03745, 0.03745, 0.03745, 0.03745, 0.03745, 0.03745,
                                0.03745,
                                0.11647, 0.11647, 0.11647, 0.11647, 0.11647, 0.11647, 0.11647, 0.11647, 0.11647,
                                0.11647,
                                0.11647, 0.11647, 0.11647, 0.11647, 0.11647, 0.11647, 0.11647, 0.11647, 0.11647,
                                0.11647,
                                0.11647, 0.11647, 0.11647, 0.11647, 0.11647, 0.11647, 0.11647, 0.11647, 0.11647,
                                0.11647,
                                0.16842, 0.16842, 0.16842, 0.16842, 0.16842, 0.16842, 0.16842, 0.16842, 0.16842,
                                0.16842,
                                0.16842, 0.16842, 0.16842, 0.16842, 0.16842, 0.16842, 0.16842, 0.16842, 0.16842,
                                0.16842,
                                0.16842, 0.16842, 0.16842, 0.16842, 0.16842, 0.16842, 0.16842, 0.16842, 0.16842,
                                0.16842,
                                0.24129, 0.24129, 0.24129, 0.24129, 0.24129, 0.24129, 0.24129, 0.24129, 0.24129,
                                0.24129,
                                0.24129, 0.24129, 0.24129, 0.24129, 0.24129, 0.24129, 0.24129, 0.24129, 0.24129,
                                0.24129,
                                0.24129, 0.24129, 0.24129, 0.24129, 0.24129, 0.24129, 0.24129, 0.24129, 0.24129,
                                0.24129,
                                0.21767, 0.21767, 0.21767, 0.21767, 0.21767, 0.21767, 0.21767, 0.21767, 0.21767,
                                0.21767,
                                0.21767, 0.21767, 0.21767, 0.21767, 0.21767, 0.21767, 0.21767, 0.21767, 0.21767,
                                0.21767,
                                0.21767, 0.21767, 0.21767, 0.21767, 0.21767, 0.21767, 0.21767, 0.21767, 0.21767,
                                0.21767,
                                0.08906, 0.08906, 0.08906, 0.08906, 0.08906, 0.08906, 0.08906, 0.08906, 0.08906,
                                0.08906,
                                0.08906, 0.08906, 0.08906, 0.08906, 0.08906, 0.08906, 0.08906, 0.08906, 0.08906,
                                0.08906,
                                0.08906, 0.08906, 0.08906, 0.08906, 0.08906, 0.08906, 0.08906, 0.08906, 0.08906,
                                0.08906,
                                0.08906, 0.08906, 0.08906, 0.08906, 0.08906
                            ])


def monthly_evp_abbn(x):
    """
    Real Name: b'"monthly evp ab-bn"'
    Original Eqn: b'( [(1,0)-(365,5)],(1,0.86667),(2,0.86667),(3,0.86667),(4,0.86667),(5,0.86667),(6,0.86667\\\\ ),(7,0.86667),(8,0.86667),(9,0.86667),(10,0.86667),(11,0.86667),(12,0.86667),(13,0.86667\\\\ ),(14,0.86667),(15,0.86667),(16,0.86667),(17,0.86667),(18,0.86667),(19,0.86667),(20\\\\ ,0.86667),(21,0.86667),(22,0.86667),(23,0.86667),(24,0.86667),(25,0.86667),(26,0.86667\\\\ ),(27,0.86667),(28,0.86667),(29,0.86667),(30,0.86667),(31,1.5),(32,1.5),(33,1.5),(34\\\\ ,1.5),(35,1.5),(36,1.5),(37,1.5),(38,1.5),(39,1.5),(40,1.5),(41,1.5),(42,1.5),(43,1.5\\\\ ),(44,1.5),(45,1.5),(46,1.5),(47,1.5),(48,1.5),(49,1.5),(50,1.5),(51,1.5),(52,1.5),\\\\ (53,1.5),(54,1.5),(55,1.5),(56,1.5),(57,1.5),(58,1.5),(59,1.5),(60,1.5),(61,0.96667\\\\ ),(62,0.96667),(63,0.96667),(64,0.96667),(65,0.96667),(66,0.96667),(67,0.96667),(68\\\\ ,0.96667),(69,0.96667),(70,0.96667),(71,0.96667),(72,0.96667),(73,0.96667),(74,0.96667\\\\ ),(75,0.96667),(76,0.96667),(77,0.96667),(78,0.96667),(79,0.96667),(80,0.96667),(81\\\\ ,0.96667),(82,0.96667),(83,0.96667),(84,0.96667),(85,0.96667),(86,0.96667),(87,0.96667\\\\ ),(88,0.96667),(89,0.96667),(90,0.96667),(91,0.83333),(92,0.83333),(93,0.83333),(94\\\\ ,0.83333),(95,0.83333),(96,0.83333),(97,0.83333),(98,0.83333),(99,0.83333),(100,0.83333\\\\ ),(101,0.83333),(102,0.83333),(103,0.83333),(104,0.83333),(105,0.83333),(106,0.83333\\\\ ),(107,0.83333),(108,0.83333),(109,0.83333),(110,0.83333),(111,0.83333),(112,0.83333\\\\ ),(113,0.83333),(114,0.83333),(115,0.83333),(116,0.83333),(117,0.83333),(118,0.83333\\\\ ),(119,0.83333),(120,0.83333),(121,1.03333),(122,1.03333),(123,1.03333),(124,1.03333\\\\ ),(125,1.03333),(126,1.03333),(127,1.03333),(128,1.03333),(129,1.03333),(130,1.03333\\\\ ),(131,1.03333),(132,1.03333),(133,1.03333),(134,1.03333),(135,1.03333),(136,1.03333\\\\ ),(137,1.03333),(138,1.03333),(139,1.03333),(140,1.03333),(141,1.03333),(142,1.03333\\\\ ),(143,1.03333),(144,1.03333),(145,1.03333),(146,1.03333),(147,1.03333),(148,1.03333\\\\ ),(149,1.03333),(150,1.03333),(151,1.56667),(152,1.56667),(153,1.56667),(154,1.56667\\\\ ),(155,1.56667),(156,1.56667),(157,1.56667),(158,1.56667),(159,1.56667),(160,1.56667\\\\ ),(161,1.56667),(162,1.56667),(163,1.56667),(164,1.56667),(165,1.56667),(166,1.56667\\\\ ),(167,1.56667),(168,1.56667),(169,1.56667),(170,1.56667),(171,1.56667),(172,1.56667\\\\ ),(173,1.56667),(174,1.56667),(175,1.56667),(176,1.56667),(177,1.56667),(178,1.56667\\\\ ),(179,1.56667),(180,1.56667),(181,2.5),(182,2.5),(183,2.5),(184,2.5),(185,2.5),(186\\\\ ,2.5),(187,2.5),(188,2.5),(189,2.5),(190,2.5),(191,2.5),(192,2.5),(193,2.5),(194,2.5\\\\ ),(195,2.5),(196,2.5),(197,2.5),(198,2.5),(199,2.5),(200,2.5),(201,2.5),(202,2.5),(\\\\ 203,2.5),(204,2.5),(205,2.5),(206,2.5),(207,2.5),(208,2.5),(209,2.5),(210,2.5),(211\\\\ ,3.6),(212,3.6),(213,3.6),(214,3.6),(215,3.6),(216,3.6),(217,3.6),(218,3.6),(219,3.6\\\\ ),(220,3.6),(221,3.6),(222,3.6),(223,3.6),(224,3.6),(225,3.6),(226,3.6),(227,3.6),(\\\\ 228,3.6),(229,3.6),(230,3.6),(231,3.6),(232,3.6),(233,3.6),(234,3.6),(235,3.6),(236\\\\ ,3.6),(237,3.6),(238,3.6),(239,3.6),(240,3.6),(241,4.46667),(242,4.46667),(243,4.46667\\\\ ),(244,4.46667),(245,4.46667),(246,4.46667),(247,4.46667),(248,4.46667),(249,4.46667\\\\ ),(250,4.46667),(251,4.46667),(252,4.46667),(253,4.46667),(254,4.46667),(255,4.46667\\\\ ),(256,4.46667),(257,4.46667),(258,4.46667),(259,4.46667),(260,4.46667),(261,4.46667\\\\ ),(262,4.46667),(263,4.46667),(264,4.46667),(265,4.46667),(266,4.46667),(267,4.46667\\\\ ),(268,4.46667),(269,4.46667),(270,4.46667),(271,4.93333),(272,4.93333),(273,4.93333\\\\ ),(274,4.93333),(275,4.93333),(276,4.93333),(277,4.93333),(278,4.93333),(279,4.93333\\\\ ),(280,4.93333),(281,4.93333),(282,4.93333),(283,4.93333),(284,4.93333),(285,4.93333\\\\ ),(286,4.93333),(287,4.93333),(288,4.93333),(289,4.93333),(290,4.93333),(291,4.93333\\\\ ),(292,4.93333),(293,4.93333),(294,4.93333),(295,4.93333),(296,4.93333),(297,4.93333\\\\ ),(298,4.93333),(299,4.93333),(300,4.93333),(301,4.8),(302,4.8),(303,4.8),(304,4.8)\\\\ ,(305,4.8),(306,4.8),(307,4.8),(308,4.8),(309,4.8),(310,4.8),(311,4.8),(312,4.8),(313\\\\ ,4.8),(314,4.8),(315,4.8),(316,4.8),(317,4.8),(318,4.8),(319,4.8),(320,4.8),(321,4.8\\\\ ),(322,4.8),(323,4.8),(324,4.8),(325,4.8),(326,4.8),(327,4.8),(328,4.8),(329,4.8),(\\\\ 330,4.8),(331,3.7),(332,3.7),(333,3.7),(334,3.7),(335,3.7),(336,3.7),(337,3.7),(338\\\\ ,3.7),(339,3.7),(340,3.7),(341,3.7),(342,3.7),(343,3.7),(344,3.7),(345,3.7),(346,3.7\\\\ ),(347,3.7),(348,3.7),(349,3.7),(350,3.7),(351,3.7),(352,3.7),(353,3.7),(354,3.7),(\\\\ 355,3.7),(356,3.7),(357,3.7),(358,3.7),(359,3.7),(360,3.7),(361,3.7),(362,3.7),(363\\\\ ,3.7),(364,3.7),(365,3.7))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], [
                                0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667,
                                0.86667,
                                0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667,
                                0.86667,
                                0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667,
                                0.86667,
                                1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5,
                                1.5,
                                1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 0.96667, 0.96667, 0.96667,
                                0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667,
                                0.96667,
                                0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667,
                                0.96667,
                                0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.83333, 0.83333,
                                0.83333,
                                0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333,
                                0.83333,
                                0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333,
                                0.83333,
                                0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 1.03333, 1.03333,
                                1.03333,
                                1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333,
                                1.03333,
                                1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333,
                                1.03333,
                                1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.56667, 1.56667,
                                1.56667,
                                1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667,
                                1.56667,
                                1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667,
                                1.56667,
                                1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 2.5, 2.5, 2.5, 2.5, 2.5,
                                2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5,
                                2.5,
                                2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6,
                                3.6,
                                3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6,
                                3.6,
                                3.6, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667,
                                4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667,
                                4.46667,
                                4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667,
                                4.46667,
                                4.46667, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333,
                                4.93333,
                                4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333,
                                4.93333,
                                4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333,
                                4.93333,
                                4.93333, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8,
                                4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 3.7, 3.7, 3.7,
                                3.7,
                                3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7,
                                3.7,
                                3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7
                            ])


@cache('step')
def tj_div_aftr_abbn_spill():
    """
    Real Name: b'"Tj Div aftr Ab-bn Spill"'
    Original Eqn: b'Tj aftr Div+"Ab-bn Spill"'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return tj_aftr_div() + abbn_spill()


@cache('step')
def over_reso_bfr_div():
    """
    Real Name: b'over Reso bfr Div'
    Original Eqn: b'IF THEN ELSE(Tj aftr Div<ovr Reso in out system, 0, ovr Reso in out system)'
    Units: b''
    Limits: (None, None)
    Type: component

    b'\\u0645\\u0642\\u0627\\u062f\\u06cc\\u0631 \\u0622\\u0628\\u062f\\u0647\\u06cc \\u0645\\u0627\\u0632\\u0627\\u062f \\u0631\\u0648\\u062f\\u062e\\u0627\\u0646\\u0647 \\u062a\\u062d\\u0646 \\u0642\\u0627\\u0628\\u0644 \\n    \\t\\t\\u0627\\u0646\\u062a\\u0642\\u0627\\u0644 \\u0628\\u0647 \\u062d\\u0648\\u0636\\u0647 \\u0645\\u062c\\u0627\\u0648\\u0631 \\u0627\\u0632 \\u0645\\u0642\\u0637\\u0639 \\u0628\\u0639\\u062f \\u0627\\u0632 \\u0628\\u0646\\u062f \\n    \\t\\t\\u0627\\u0646\\u062d\\u0631\\u0627\\u0641\\u06cc \\u062a\\u062c\\u0646'
    """
    return functions.if_then_else(tj_aftr_div() < ovr_reso_in_out_system(), 0,
                                  ovr_reso_in_out_system())


def zr_env_dem(x):
    """
    Real Name: b'zr Env dem'
    Original Eqn: b'( [(1,0)-(365,0.03)],(1,0.03),(2,0.03),(3,0.03),(4,0.03),(5,0.03),(6,0.03),(7,0.03),(8\\\\ ,0.03),(9,0.03),(10,0.03),(11,0.03),(12,0.03),(13,0.03),(14,0.03),(15,0.03),(16,0.03\\\\ ),(17,0.03),(18,0.03),(19,0.03),(20,0.03),(21,0.03),(22,0.03),(23,0.03),(24,0.03),(\\\\ 25,0.03),(26,0.03),(27,0.03),(28,0.03),(29,0.03),(30,0.03),(31,0),(32,0),(33,0),(34\\\\ ,0),(35,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46\\\\ ,0),(47,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58\\\\ ,0),(59,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70\\\\ ,0),(71,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82\\\\ ,0),(83,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94\\\\ ,0),(95,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105\\\\ ,0),(106,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0)\\\\ ,(116,0),(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126\\\\ ,0),(127,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0)\\\\ ,(137,0),(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147\\\\ ,0),(148,0),(149,0),(150,0),(151,0),(152,0),(153,0),(154,0),(155,0),(156,0),(157,0)\\\\ ,(158,0),(159,0),(160,0),(161,0),(162,0),(163,0),(164,0),(165,0),(166,0),(167,0),(168\\\\ ,0),(169,0),(170,0),(171,0),(172,0),(173,0),(174,0),(175,0),(176,0),(177,0),(178,0)\\\\ ,(179,0),(180,0),(181,0),(182,0),(183,0),(184,0),(185,0),(186,0),(187,0),(188,0),(189\\\\ ,0),(190,0),(191,0),(192,0),(193,0),(194,0),(195,0),(196,0),(197,0),(198,0),(199,0)\\\\ ,(200,0),(201,0),(202,0),(203,0),(204,0),(205,0),(206,0),(207,0),(208,0),(209,0),(210\\\\ ,0),(211,0),(212,0),(213,0),(214,0),(215,0),(216,0),(217,0),(218,0),(219,0),(220,0)\\\\ ,(221,0),(222,0),(223,0),(224,0),(225,0),(226,0),(227,0),(228,0),(229,0),(230,0),(231\\\\ ,0),(232,0),(233,0),(234,0),(235,0),(236,0),(237,0),(238,0),(239,0),(240,0),(241,0)\\\\ ,(242,0),(243,0),(244,0),(245,0),(246,0),(247,0),(248,0),(249,0),(250,0),(251,0),(252\\\\ ,0),(253,0),(254,0),(255,0),(256,0),(257,0),(258,0),(259,0),(260,0),(261,0),(262,0)\\\\ ,(263,0),(264,0),(265,0),(266,0),(267,0),(268,0),(269,0),(270,0),(271,0),(272,0),(273\\\\ ,0),(274,0),(275,0),(276,0),(277,0),(278,0),(279,0),(280,0),(281,0),(282,0),(283,0)\\\\ ,(284,0),(285,0),(286,0),(287,0),(288,0),(289,0),(290,0),(291,0),(292,0),(293,0),(294\\\\ ,0),(295,0),(296,0),(297,0),(298,0),(299,0),(300,0),(301,0),(302,0),(303,0),(304,0)\\\\ ,(305,0),(306,0),(307,0),(308,0),(309,0),(310,0),(311,0),(312,0),(313,0),(314,0),(315\\\\ ,0),(316,0),(317,0),(318,0),(319,0),(320,0),(321,0),(322,0),(323,0),(324,0),(325,0)\\\\ ,(326,0),(327,0),(328,0),(329,0),(330,0),(331,0),(332,0),(333,0),(334,0),(335,0),(336\\\\ ,0),(337,0),(338,0),(339,0),(340,0),(341,0),(342,0),(343,0),(344,0),(345,0),(346,0)\\\\ ,(347,0),(348,0),(349,0),(350,0),(351,0),(352,0),(353,0),(354,0),(355,0),(356,0),(357\\\\ ,0),(358,0),(359,0),(360,0),(361,0),(362,0),(363,0),(364,0),(365,0))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], [
                                0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
                                0.03,
                                0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
                                0.03,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0
                            ])


@cache('run')
def agri_zr_dam_coef():
    """
    Real Name: b'agri zr dam coef'
    Original Eqn: b'1'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1


@cache('run')
def agri_zr_dev_coef():
    """
    Real Name: b'agri zr dev coef'
    Original Eqn: b'1e-012'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1e-012


def zr_ind(x):
    """
    Real Name: b'zr Ind'
    Original Eqn: b'( [(1,0.02)-(365,0.03)],(1,0.03),(2,0.03),(3,0.03),(4,0.03),(5,0.03),(6,0.03),(7,0.03)\\\\ ,(8,0.03),(9,0.03),(10,0.03),(11,0.03),(12,0.03),(13,0.03),(14,0.03),(15,0.03),(16,\\\\ 0.03),(17,0.03),(18,0.03),(19,0.03),(20,0.03),(21,0.03),(22,0.03),(23,0.03),(24,0.03\\\\ ),(25,0.03),(26,0.03),(27,0.03),(28,0.03),(29,0.03),(30,0.03),(31,0.03),(32,0.03),(\\\\ 33,0.03),(34,0.03),(35,0.03),(36,0.03),(37,0.03),(38,0.03),(39,0.03),(40,0.03),(41,\\\\ 0.03),(42,0.03),(43,0.03),(44,0.03),(45,0.03),(46,0.03),(47,0.03),(48,0.03),(49,0.03\\\\ ),(50,0.03),(51,0.03),(52,0.03),(53,0.03),(54,0.03),(55,0.03),(56,0.03),(57,0.03),(\\\\ 58,0.03),(59,0.03),(60,0.03),(61,0.03),(62,0.03),(63,0.03),(64,0.03),(65,0.03),(66,\\\\ 0.03),(67,0.03),(68,0.03),(69,0.03),(70,0.03),(71,0.03),(72,0.03),(73,0.03),(74,0.03\\\\ ),(75,0.03),(76,0.03),(77,0.03),(78,0.03),(79,0.03),(80,0.03),(81,0.03),(82,0.03),(\\\\ 83,0.03),(84,0.03),(85,0.03),(86,0.03),(87,0.03),(88,0.03),(89,0.03),(90,0.03),(91,\\\\ 0.03),(92,0.03),(93,0.03),(94,0.03),(95,0.03),(96,0.03),(97,0.03),(98,0.03),(99,0.03\\\\ ),(100,0.03),(101,0.03),(102,0.03),(103,0.03),(104,0.03),(105,0.03),(106,0.03),(107\\\\ ,0.03),(108,0.03),(109,0.03),(110,0.03),(111,0.03),(112,0.03),(113,0.03),(114,0.03)\\\\ ,(115,0.03),(116,0.03),(117,0.03),(118,0.03),(119,0.03),(120,0.03),(121,0.03),(122,\\\\ 0.03),(123,0.03),(124,0.03),(125,0.03),(126,0.03),(127,0.03),(128,0.03),(129,0.03),\\\\ (130,0.03),(131,0.03),(132,0.03),(133,0.03),(134,0.03),(135,0.03),(136,0.03),(137,0.03\\\\ ),(138,0.03),(139,0.03),(140,0.03),(141,0.03),(142,0.03),(143,0.03),(144,0.03),(145\\\\ ,0.03),(146,0.03),(147,0.03),(148,0.03),(149,0.03),(150,0.03),(151,0.03),(152,0.03)\\\\ ,(153,0.03),(154,0.03),(155,0.03),(156,0.03),(157,0.03),(158,0.03),(159,0.03),(160,\\\\ 0.03),(161,0.03),(162,0.03),(163,0.03),(164,0.03),(165,0.03),(166,0.03),(167,0.03),\\\\ (168,0.03),(169,0.03),(170,0.03),(171,0.03),(172,0.03),(173,0.03),(174,0.03),(175,0.03\\\\ ),(176,0.03),(177,0.03),(178,0.03),(179,0.03),(180,0.03),(181,0.03),(182,0.03),(183\\\\ ,0.03),(184,0.03),(185,0.03),(186,0.03),(187,0.03),(188,0.03),(189,0.03),(190,0.03)\\\\ ,(191,0.03),(192,0.03),(193,0.03),(194,0.03),(195,0.03),(196,0.03),(197,0.03),(198,\\\\ 0.03),(199,0.03),(200,0.03),(201,0.03),(202,0.03),(203,0.03),(204,0.03),(205,0.03),\\\\ (206,0.03),(207,0.03),(208,0.03),(209,0.03),(210,0.03),(211,0.03),(212,0.03),(213,0.03\\\\ ),(214,0.03),(215,0.03),(216,0.03),(217,0.03),(218,0.03),(219,0.03),(220,0.03),(221\\\\ ,0.03),(222,0.03),(223,0.03),(224,0.03),(225,0.03),(226,0.03),(227,0.03),(228,0.03)\\\\ ,(229,0.03),(230,0.03),(231,0.03),(232,0.03),(233,0.03),(234,0.03),(235,0.03),(236,\\\\ 0.03),(237,0.03),(238,0.03),(239,0.03),(240,0.03),(241,0.03),(242,0.03),(243,0.03),\\\\ (244,0.03),(245,0.03),(246,0.03),(247,0.03),(248,0.03),(249,0.03),(250,0.03),(251,0.03\\\\ ),(252,0.03),(253,0.03),(254,0.03),(255,0.03),(256,0.03),(257,0.03),(258,0.03),(259\\\\ ,0.03),(260,0.03),(261,0.03),(262,0.03),(263,0.03),(264,0.03),(265,0.03),(266,0.03)\\\\ ,(267,0.03),(268,0.03),(269,0.03),(270,0.03),(271,0.03),(272,0.03),(273,0.03),(274,\\\\ 0.03),(275,0.03),(276,0.03),(277,0.03),(278,0.03),(279,0.03),(280,0.03),(281,0.03),\\\\ (282,0.03),(283,0.03),(284,0.03),(285,0.03),(286,0.03),(287,0.03),(288,0.03),(289,0.03\\\\ ),(290,0.03),(291,0.03),(292,0.03),(293,0.03),(294,0.03),(295,0.03),(296,0.03),(297\\\\ ,0.03),(298,0.03),(299,0.03),(300,0.03),(301,0.03),(302,0.03),(303,0.03),(304,0.03)\\\\ ,(305,0.03),(306,0.03),(307,0.03),(308,0.03),(309,0.03),(310,0.03),(311,0.03),(312,\\\\ 0.03),(313,0.03),(314,0.03),(315,0.03),(316,0.03),(317,0.03),(318,0.03),(319,0.03),\\\\ (320,0.03),(321,0.03),(322,0.03),(323,0.03),(324,0.03),(325,0.03),(326,0.03),(327,0.03\\\\ ),(328,0.03),(329,0.03),(330,0.03),(331,0.03),(332,0.03),(333,0.03),(334,0.03),(335\\\\ ,0.03),(336,0.03),(337,0.03),(338,0.03),(339,0.03),(340,0.03),(341,0.03),(342,0.03)\\\\ ,(343,0.03),(344,0.03),(345,0.03),(346,0.03),(347,0.03),(348,0.03),(349,0.03),(350,\\\\ 0.03),(351,0.03),(352,0.03),(353,0.03),(354,0.03),(355,0.03),(356,0.03),(357,0.03),\\\\ (358,0.03),(359,0.03),(360,0.03),(361,0.03),(362,0.03),(363,0.03),(364,0.03),(365,0.03\\\\ ))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], [
                                0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
                                0.03,
                                0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
                                0.03,
                                0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
                                0.03,
                                0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
                                0.03,
                                0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
                                0.03,
                                0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
                                0.03,
                                0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
                                0.03,
                                0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
                                0.03,
                                0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
                                0.03,
                                0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
                                0.03,
                                0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
                                0.03,
                                0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
                                0.03,
                                0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
                                0.03,
                                0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
                                0.03,
                                0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
                                0.03,
                                0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
                                0.03,
                                0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
                                0.03,
                                0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
                                0.03,
                                0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
                                0.03,
                                0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
                                0.03,
                                0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
                                0.03,
                                0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
                                0.03,
                                0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
                                0.03,
                                0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
                                0.03,
                                0.03, 0.03, 0.03, 0.03, 0.03
                            ])


@cache('run')
def zr_max_vol():
    """
    Real Name: b'zr max vol'
    Original Eqn: b'82.73'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 82.73


@cache('run')
def zr_min_vol():
    """
    Real Name: b'zr min vol'
    Original Eqn: b'13'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 13


@cache('step')
def zr_spill():
    """
    Real Name: b'Zr Spill'
    Original Eqn: b'IF THEN ELSE(((Zr reservoir)+Zr inflow-Zr outflow-Zr evap)>(zr max vol), ((Zr reservoir )+Zr inflow-Zr outflow-Zr evap-(zr max vol)), 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.if_then_else(
        ((zr_reservoir()) + zr_inflow() - zr_outflow() - zr_evap()) > (zr_max_vol()),
        ((zr_reservoir()) + zr_inflow() - zr_outflow() - zr_evap() - (zr_max_vol())), 0)


def wr_dem_bfr_zr_dam(x):
    """
    Real Name: b'wr Dem bfr Zr dam'
    Original Eqn: b'( [(1,0)-(365,0.06)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,\\\\ 0),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23\\\\ ,0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35\\\\ ,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47\\\\ ,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94,0),(95\\\\ ,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105,0),(106\\\\ ,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0),(116,0)\\\\ ,(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126,0),(127\\\\ ,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0),(137,0)\\\\ ,(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147,0),(148\\\\ ,0),(149,0),(150,0),(151,0),(152,0),(153,0),(154,0),(155,0),(156,0),(157,0),(158,0)\\\\ ,(159,0),(160,0),(161,0),(162,0),(163,0),(164,0),(165,0),(166,0),(167,0),(168,0),(169\\\\ ,0),(170,0),(171,0),(172,0),(173,0),(174,0),(175,0),(176,0),(177,0),(178,0),(179,0)\\\\ ,(180,0),(181,0.03),(182,0.03),(183,0.03),(184,0.03),(185,0.03),(186,0.03),(187,0.03\\\\ ),(188,0.03),(189,0.03),(190,0.03),(191,0.03),(192,0.03),(193,0.03),(194,0.03),(195\\\\ ,0.03),(196,0.03),(197,0.03),(198,0.03),(199,0.03),(200,0.03),(201,0.03),(202,0.03)\\\\ ,(203,0.03),(204,0.03),(205,0.03),(206,0.03),(207,0.03),(208,0.03),(209,0.03),(210,\\\\ 0.03),(211,0.06),(212,0.06),(213,0.06),(214,0.06),(215,0.06),(216,0.06),(217,0.06),\\\\ (218,0.06),(219,0.06),(220,0.06),(221,0.06),(222,0.06),(223,0.06),(224,0.06),(225,0.06\\\\ ),(226,0.06),(227,0.06),(228,0.06),(229,0.06),(230,0.06),(231,0.06),(232,0.06),(233\\\\ ,0.06),(234,0.06),(235,0.06),(236,0.06),(237,0.06),(238,0.06),(239,0.06),(240,0.06)\\\\ ,(241,0.05),(242,0.05),(243,0.05),(244,0.05),(245,0.05),(246,0.05),(247,0.05),(248,\\\\ 0.05),(249,0.05),(250,0.05),(251,0.05),(252,0.05),(253,0.05),(254,0.05),(255,0.05),\\\\ (256,0.05),(257,0.05),(258,0.05),(259,0.05),(260,0.05),(261,0.05),(262,0.05),(263,0.05\\\\ ),(264,0.05),(265,0.05),(266,0.05),(267,0.05),(268,0.05),(269,0.05),(270,0.05),(271\\\\ ,0.06),(272,0.06),(273,0.06),(274,0.06),(275,0.06),(276,0.06),(277,0.06),(278,0.06)\\\\ ,(279,0.06),(280,0.06),(281,0.06),(282,0.06),(283,0.06),(284,0.06),(285,0.06),(286,\\\\ 0.06),(287,0.06),(288,0.06),(289,0.06),(290,0.06),(291,0.06),(292,0.06),(293,0.06),\\\\ (294,0.06),(295,0.06),(296,0.06),(297,0.06),(298,0.06),(299,0.06),(300,0.06),(301,0.05\\\\ ),(302,0.05),(303,0.05),(304,0.05),(305,0.05),(306,0.05),(307,0.05),(308,0.05),(309\\\\ ,0.05),(310,0.05),(311,0.05),(312,0.05),(313,0.05),(314,0.05),(315,0.05),(316,0.05)\\\\ ,(317,0.05),(318,0.05),(319,0.05),(320,0.05),(321,0.05),(322,0.05),(323,0.05),(324,\\\\ 0.05),(325,0.05),(326,0.05),(327,0.05),(328,0.05),(329,0.05),(330,0.05),(331,0.02),\\\\ (332,0.02),(333,0.02),(334,0.02),(335,0.02),(336,0.02),(337,0.02),(338,0.02),(339,0.02\\\\ ),(340,0.02),(341,0.02),(342,0.02),(343,0.02),(344,0.02),(345,0.02),(346,0.02),(347\\\\ ,0.02),(348,0.02),(349,0.02),(350,0.02),(351,0.02),(352,0.02),(353,0.02),(354,0.02)\\\\ ,(355,0.02),(356,0.02),(357,0.02),(358,0.02),(359,0.02),(360,0.02),(361,0.02),(362,\\\\ 0.02),(363,0.02),(364,0.02),(365,0.02))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], [
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
                                0.03,
                                0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
                                0.03,
                                0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06,
                                0.06,
                                0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06,
                                0.06,
                                0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05,
                                0.05,
                                0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05,
                                0.05,
                                0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06,
                                0.06,
                                0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06,
                                0.06,
                                0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05,
                                0.05,
                                0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05,
                                0.05,
                                0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02,
                                0.02,
                                0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02,
                                0.02,
                                0.02, 0.02, 0.02, 0.02, 0.02
                            ])


@cache('step')
def tj_aftr_zr():
    """
    Real Name: b'Tj aftr Zr'
    Original Eqn: b'Tajan Befr zarem+Zr bfr Tj-wr sup Tj bfr Zr+(wr sup Tj bfr Zr*0.2)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return tajan_befr_zarem() + zr_bfr_tj() - wr_sup_tj_bfr_zr() + (wr_sup_tj_bfr_zr() * 0.2)


@cache('step')
def wr_sup_aftr_zr_dam():
    """
    Real Name: b'Wr sup aftr Zr Dam'
    Original Eqn: b'MIN(Zr aftr Dam, Wr Dem aftr Zr Dam)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return np.minimum(zr_aftr_dam(), wr_dem_aftr_zr_dam())


def inter_aftr_zr_dam(x):
    """
    Real Name: b'inter aftr Zr Dam'
    Original Eqn: b'( [(1,0)-(365,1)],(1,0.06439),(2,0.06439),(3,0.06439),(4,0.06439),(5,0.06439),(6,0.06439\\\\ ),(7,0.06439),(8,0.06439),(9,0.06439),(10,0.06439),(11,0.06439),(12,0.06439),(13,0.06439\\\\ ),(14,0.06439),(15,0.06439),(16,0.06439),(17,0.06439),(18,0.06439),(19,0.06439),(20\\\\ ,0.06439),(21,0.06439),(22,0.06439),(23,0.06439),(24,0.06439),(25,0.06439),(26,0.06439\\\\ ),(27,0.06439),(28,0.06439),(29,0.06439),(30,0.06439),(31,0.11676),(32,0.11676),(33\\\\ ,0.11676),(34,0.11676),(35,0.11676),(36,0.11676),(37,0.11676),(38,0.11676),(39,0.11676\\\\ ),(40,0.11676),(41,0.11676),(42,0.11676),(43,0.11676),(44,0.11676),(45,0.11676),(46\\\\ ,0.11676),(47,0.11676),(48,0.11676),(49,0.11676),(50,0.11676),(51,0.11676),(52,0.11676\\\\ ),(53,0.11676),(54,0.11676),(55,0.11676),(56,0.11676),(57,0.11676),(58,0.11676),(59\\\\ ,0.11676),(60,0.11676),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,\\\\ 0),(70,0),(71,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81\\\\ ,0),(82,0),(83,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0.16065),(92\\\\ ,0.16065),(93,0.16065),(94,0.16065),(95,0.16065),(96,0.16065),(97,0.16065),(98,0.16065\\\\ ),(99,0.16065),(100,0.16065),(101,0.16065),(102,0.16065),(103,0.16065),(104,0.16065\\\\ ),(105,0.16065),(106,0.16065),(107,0.16065),(108,0.16065),(109,0.16065),(110,0.16065\\\\ ),(111,0.16065),(112,0.16065),(113,0.16065),(114,0.16065),(115,0.16065),(116,0.16065\\\\ ),(117,0.16065),(118,0.16065),(119,0.16065),(120,0.16065),(121,0.63944),(122,0.63944\\\\ ),(123,0.63944),(124,0.63944),(125,0.63944),(126,0.63944),(127,0.63944),(128,0.63944\\\\ ),(129,0.63944),(130,0.63944),(131,0.63944),(132,0.63944),(133,0.63944),(134,0.63944\\\\ ),(135,0.63944),(136,0.63944),(137,0.63944),(138,0.63944),(139,0.63944),(140,0.63944\\\\ ),(141,0.63944),(142,0.63944),(143,0.63944),(144,0.63944),(145,0.63944),(146,0.63944\\\\ ),(147,0.63944),(148,0.63944),(149,0.63944),(150,0.63944),(151,0.98094),(152,0.98094\\\\ ),(153,0.98094),(154,0.98094),(155,0.98094),(156,0.98094),(157,0.98094),(158,0.98094\\\\ ),(159,0.98094),(160,0.98094),(161,0.98094),(162,0.98094),(163,0.98094),(164,0.98094\\\\ ),(165,0.98094),(166,0.98094),(167,0.98094),(168,0.98094),(169,0.98094),(170,0.98094\\\\ ),(171,0.98094),(172,0.98094),(173,0.98094),(174,0.98094),(175,0.98094),(176,0.98094\\\\ ),(177,0.98094),(178,0.98094),(179,0.98094),(180,0.98094),(181,0.01199),(182,0.01199\\\\ ),(183,0.01199),(184,0.01199),(185,0.01199),(186,0.01199),(187,0.01199),(188,0.01199\\\\ ),(189,0.01199),(190,0.01199),(191,0.01199),(192,0.01199),(193,0.01199),(194,0.01199\\\\ ),(195,0.01199),(196,0.01199),(197,0.01199),(198,0.01199),(199,0.01199),(200,0.01199\\\\ ),(201,0.01199),(202,0.01199),(203,0.01199),(204,0.01199),(205,0.01199),(206,0.01199\\\\ ),(207,0.01199),(208,0.01199),(209,0.01199),(210,0.01199),(211,0),(212,0),(213,0),(\\\\ 214,0),(215,0),(216,0),(217,0),(218,0),(219,0),(220,0),(221,0),(222,0),(223,0),(224\\\\ ,0),(225,0),(226,0),(227,0),(228,0),(229,0),(230,0),(231,0),(232,0),(233,0),(234,0)\\\\ ,(235,0),(236,0),(237,0),(238,0),(239,0),(240,0),(241,0),(242,0),(243,0),(244,0),(245\\\\ ,0),(246,0),(247,0),(248,0),(249,0),(250,0),(251,0),(252,0),(253,0),(254,0),(255,0)\\\\ ,(256,0),(257,0),(258,0),(259,0),(260,0),(261,0),(262,0),(263,0),(264,0),(265,0),(266\\\\ ,0),(267,0),(268,0),(269,0),(270,0),(271,0.02971),(272,0.02971),(273,0.02971),(274,\\\\ 0.02971),(275,0.02971),(276,0.02971),(277,0.02971),(278,0.02971),(279,0.02971),(280\\\\ ,0.02971),(281,0.02971),(282,0.02971),(283,0.02971),(284,0.02971),(285,0.02971),(286\\\\ ,0.02971),(287,0.02971),(288,0.02971),(289,0.02971),(290,0.02971),(291,0.02971),(292\\\\ ,0.02971),(293,0.02971),(294,0.02971),(295,0.02971),(296,0.02971),(297,0.02971),(298\\\\ ,0.02971),(299,0.02971),(300,0.02971),(301,0),(302,0),(303,0),(304,0),(305,0),(306,\\\\ 0),(307,0),(308,0),(309,0),(310,0),(311,0),(312,0),(313,0),(314,0),(315,0),(316,0),\\\\ (317,0),(318,0),(319,0),(320,0),(321,0),(322,0),(323,0),(324,0),(325,0),(326,0),(327\\\\ ,0),(328,0),(329,0),(330,0),(331,0.00536),(332,0.00536),(333,0.00536),(334,0.00536)\\\\ ,(335,0.00536),(336,0.00536),(337,0.00536),(338,0.00536),(339,0.00536),(340,0.00536\\\\ ),(341,0.00536),(342,0.00536),(343,0.00536),(344,0.00536),(345,0.00536),(346,0.00536\\\\ ),(347,0.00536),(348,0.00536),(349,0.00536),(350,0.00536),(351,0.00536),(352,0.00536\\\\ ),(353,0.00536),(354,0.00536),(355,0.00536),(356,0.00536),(357,0.00536),(358,0.00536\\\\ ),(359,0.00536),(360,0.00536),(361,0.00536),(362,0.00536),(363,0.00536),(364,0.00536\\\\ ),(365,0.00536))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], [
                                0.06439, 0.06439, 0.06439, 0.06439, 0.06439, 0.06439, 0.06439, 0.06439, 0.06439,
                                0.06439,
                                0.06439, 0.06439, 0.06439, 0.06439, 0.06439, 0.06439, 0.06439, 0.06439, 0.06439,
                                0.06439,
                                0.06439, 0.06439, 0.06439, 0.06439, 0.06439, 0.06439, 0.06439, 0.06439, 0.06439,
                                0.06439,
                                0.11676, 0.11676, 0.11676, 0.11676, 0.11676, 0.11676, 0.11676, 0.11676, 0.11676,
                                0.11676,
                                0.11676, 0.11676, 0.11676, 0.11676, 0.11676, 0.11676, 0.11676, 0.11676, 0.11676,
                                0.11676,
                                0.11676, 0.11676, 0.11676, 0.11676, 0.11676, 0.11676, 0.11676, 0.11676, 0.11676,
                                0.11676,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0.16065, 0.16065, 0.16065, 0.16065, 0.16065, 0.16065, 0.16065, 0.16065, 0.16065,
                                0.16065,
                                0.16065, 0.16065, 0.16065, 0.16065, 0.16065, 0.16065, 0.16065, 0.16065, 0.16065,
                                0.16065,
                                0.16065, 0.16065, 0.16065, 0.16065, 0.16065, 0.16065, 0.16065, 0.16065, 0.16065,
                                0.16065,
                                0.63944, 0.63944, 0.63944, 0.63944, 0.63944, 0.63944, 0.63944, 0.63944, 0.63944,
                                0.63944,
                                0.63944, 0.63944, 0.63944, 0.63944, 0.63944, 0.63944, 0.63944, 0.63944, 0.63944,
                                0.63944,
                                0.63944, 0.63944, 0.63944, 0.63944, 0.63944, 0.63944, 0.63944, 0.63944, 0.63944,
                                0.63944,
                                0.98094, 0.98094, 0.98094, 0.98094, 0.98094, 0.98094, 0.98094, 0.98094, 0.98094,
                                0.98094,
                                0.98094, 0.98094, 0.98094, 0.98094, 0.98094, 0.98094, 0.98094, 0.98094, 0.98094,
                                0.98094,
                                0.98094, 0.98094, 0.98094, 0.98094, 0.98094, 0.98094, 0.98094, 0.98094, 0.98094,
                                0.98094,
                                0.01199, 0.01199, 0.01199, 0.01199, 0.01199, 0.01199, 0.01199, 0.01199, 0.01199,
                                0.01199,
                                0.01199, 0.01199, 0.01199, 0.01199, 0.01199, 0.01199, 0.01199, 0.01199, 0.01199,
                                0.01199,
                                0.01199, 0.01199, 0.01199, 0.01199, 0.01199, 0.01199, 0.01199, 0.01199, 0.01199,
                                0.01199,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0.02971, 0.02971, 0.02971, 0.02971, 0.02971, 0.02971, 0.02971, 0.02971, 0.02971,
                                0.02971,
                                0.02971, 0.02971, 0.02971, 0.02971, 0.02971, 0.02971, 0.02971, 0.02971, 0.02971,
                                0.02971,
                                0.02971, 0.02971, 0.02971, 0.02971, 0.02971, 0.02971, 0.02971, 0.02971, 0.02971,
                                0.02971,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0.00536, 0.00536, 0.00536, 0.00536, 0.00536, 0.00536, 0.00536, 0.00536, 0.00536,
                                0.00536,
                                0.00536, 0.00536, 0.00536, 0.00536, 0.00536, 0.00536, 0.00536, 0.00536, 0.00536,
                                0.00536,
                                0.00536, 0.00536, 0.00536, 0.00536, 0.00536, 0.00536, 0.00536, 0.00536, 0.00536,
                                0.00536,
                                0.00536, 0.00536, 0.00536, 0.00536, 0.00536
                            ])


def zr_agri_dev_dem(x):
    """
    Real Name: b'zr agri dev dem'
    Original Eqn: b'( [(1,0)-(636,10)],(1,5.21),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0.44),(8,7.51),(9,9.81),(\\\\ 10,9.98),(11,7.86),(12,5.48),(13,5.21),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0.44)\\\\ ,(20,7.51),(21,9.81),(22,9.98),(23,7.86),(24,5.48),(25,5.21),(26,0),(27,0),(28,0),(\\\\ 29,0),(30,0),(31,0.44),(32,7.51),(33,9.81),(34,9.98),(35,7.86),(36,5.48),(37,5.21),\\\\ (38,0),(39,0),(40,0),(41,0),(42,0),(43,0.44),(44,7.51),(45,9.81),(46,9.98),(47,7.86\\\\ ),(48,5.48),(49,5.21),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0.44),(56,7.51),(57,9.81\\\\ ),(58,9.98),(59,7.86),(60,5.48),(61,5.21),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0.44\\\\ ),(68,7.51),(69,9.81),(70,9.98),(71,7.86),(72,5.48),(73,5.21),(74,0),(75,0),(76,0),\\\\ (77,0),(78,0),(79,0.44),(80,7.51),(81,9.81),(82,9.98),(83,7.86),(84,5.48),(85,5.21)\\\\ ,(86,0),(87,0),(88,0),(89,0),(90,0),(91,0.44),(92,7.51),(93,9.81),(94,9.98),(95,7.86\\\\ ),(96,5.48),(97,5.21),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0.44),(104,7.51),(\\\\ 105,9.81),(106,9.98),(107,7.86),(108,5.48),(109,5.21),(110,0),(111,0),(112,0),(113,\\\\ 0),(114,0),(115,0.44),(116,7.51),(117,9.81),(118,9.98),(119,7.86),(120,5.48),(121,5.21\\\\ ),(122,0),(123,0),(124,0),(125,0),(126,0),(127,0.44),(128,7.51),(129,9.81),(130,9.98\\\\ ),(131,7.86),(132,5.48),(133,5.21),(134,0),(135,0),(136,0),(137,0),(138,0),(139,0.44\\\\ ),(140,7.51),(141,9.81),(142,9.98),(143,7.86),(144,5.48),(145,5.21),(146,0),(147,0)\\\\ ,(148,0),(149,0),(150,0),(151,0.44),(152,7.51),(153,9.81),(154,9.98),(155,7.86),(156\\\\ ,5.48),(157,5.21),(158,0),(159,0),(160,0),(161,0),(162,0),(163,0.44),(164,7.51),(165\\\\ ,9.81),(166,9.98),(167,7.86),(168,5.48),(169,5.21),(170,0),(171,0),(172,0),(173,0),\\\\ (174,0),(175,0.44),(176,7.51),(177,9.81),(178,9.98),(179,7.86),(180,5.48),(181,5.21\\\\ ),(182,0),(183,0),(184,0),(185,0),(186,0),(187,0.44),(188,7.51),(189,9.81),(190,9.98\\\\ ),(191,7.86),(192,5.48),(193,5.21),(194,0),(195,0),(196,0),(197,0),(198,0),(199,0.44\\\\ ),(200,7.51),(201,9.81),(202,9.98),(203,7.86),(204,5.48),(205,5.21),(206,0),(207,0)\\\\ ,(208,0),(209,0),(210,0),(211,0.44),(212,7.51),(213,9.81),(214,9.98),(215,7.86),(216\\\\ ,5.48),(217,5.21),(218,0),(219,0),(220,0),(221,0),(222,0),(223,0.44),(224,7.51),(225\\\\ ,9.81),(226,9.98),(227,7.86),(228,5.48),(229,5.21),(230,0),(231,0),(232,0),(233,0),\\\\ (234,0),(235,0.44),(236,7.51),(237,9.81),(238,9.98),(239,7.86),(240,5.48),(241,5.21\\\\ ),(242,0),(243,0),(244,0),(245,0),(246,0),(247,0.44),(248,7.51),(249,9.81),(250,9.98\\\\ ),(251,7.86),(252,5.48),(253,5.21),(254,0),(255,0),(256,0),(257,0),(258,0),(259,0.44\\\\ ),(260,7.51),(261,9.81),(262,9.98),(263,7.86),(264,5.48),(265,5.21),(266,0),(267,0)\\\\ ,(268,0),(269,0),(270,0),(271,0.44),(272,7.51),(273,9.81),(274,9.98),(275,7.86),(276\\\\ ,5.48),(277,5.21),(278,0),(279,0),(280,0),(281,0),(282,0),(283,0.44),(284,7.51),(285\\\\ ,9.81),(286,9.98),(287,7.86),(288,5.48),(289,5.21),(290,0),(291,0),(292,0),(293,0),\\\\ (294,0),(295,0.44),(296,7.51),(297,9.81),(298,9.98),(299,7.86),(300,5.48),(301,5.21\\\\ ),(302,0),(303,0),(304,0),(305,0),(306,0),(307,0.44),(308,7.51),(309,9.81),(310,9.98\\\\ ),(311,7.86),(312,5.48),(313,5.21),(314,0),(315,0),(316,0),(317,0),(318,0),(319,0.44\\\\ ),(320,7.51),(321,9.81),(322,9.98),(323,7.86),(324,5.48),(325,5.21),(326,0),(327,0)\\\\ ,(328,0),(329,0),(330,0),(331,0.44),(332,7.51),(333,9.81),(334,9.98),(335,7.86),(336\\\\ ,5.48),(337,5.21),(338,0),(339,0),(340,0),(341,0),(342,0),(343,0.44),(344,7.51),(345\\\\ ,9.81),(346,9.98),(347,7.86),(348,5.48),(349,5.21),(350,0),(351,0),(352,0),(353,0),\\\\ (354,0),(355,0.44),(356,7.51),(357,9.81),(358,9.98),(359,7.86),(360,5.48),(361,5.21\\\\ ),(362,0),(363,0),(364,0),(365,0),(366,0),(367,0.44),(368,7.51),(369,9.81),(370,9.98\\\\ ),(371,7.86),(372,5.48),(373,5.21),(374,0),(375,0),(376,0),(377,0),(378,0),(379,0.44\\\\ ),(380,7.51),(381,9.81),(382,9.98),(383,7.86),(384,5.48),(385,5.21),(386,0),(387,0)\\\\ ,(388,0),(389,0),(390,0),(391,0.44),(392,7.51),(393,9.81),(394,9.98),(395,7.86),(396\\\\ ,5.48),(397,5.21),(398,0),(399,0),(400,0),(401,0),(402,0),(403,0.44),(404,7.51),(405\\\\ ,9.81),(406,9.98),(407,7.86),(408,5.48),(409,5.21),(410,0),(411,0),(412,0),(413,0),\\\\ (414,0),(415,0.44),(416,7.51),(417,9.81),(418,9.98),(419,7.86),(420,5.48),(421,5.21\\\\ ),(422,0),(423,0),(424,0),(425,0),(426,0),(427,0.44),(428,7.51),(429,9.81),(430,9.98\\\\ ),(431,7.86),(432,5.48),(433,5.21),(434,0),(435,0),(436,0),(437,0),(438,0),(439,0.44\\\\ ),(440,7.51),(441,9.81),(442,9.98),(443,7.86),(444,5.48),(445,5.21),(446,0),(447,0)\\\\ ,(448,0),(449,0),(450,0),(451,0.44),(452,7.51),(453,9.81),(454,9.98),(455,7.86),(456\\\\ ,5.48),(457,5.21),(458,0),(459,0),(460,0),(461,0),(462,0),(463,0.44),(464,7.51),(465\\\\ ,9.81),(466,9.98),(467,7.86),(468,5.48),(469,5.21),(470,0),(471,0),(472,0),(473,0),\\\\ (474,0),(475,0.44),(476,7.51),(477,9.81),(478,9.98),(479,7.86),(480,5.48),(481,5.21\\\\ ),(482,0),(483,0),(484,0),(485,0),(486,0),(487,0.44),(488,7.51),(489,9.81),(490,9.98\\\\ ),(491,7.86),(492,5.48),(493,5.21),(494,0),(495,0),(496,0),(497,0),(498,0),(499,0.44\\\\ ),(500,7.51),(501,9.81),(502,9.98),(503,7.86),(504,5.48),(505,5.21),(506,0),(507,0)\\\\ ,(508,0),(509,0),(510,0),(511,0.44),(512,7.51),(513,9.81),(514,9.98),(515,7.86),(516\\\\ ,5.48),(517,5.21),(518,0),(519,0),(520,0),(521,0),(522,0),(523,0.44),(524,7.51),(525\\\\ ,9.81),(526,9.98),(527,7.86),(528,5.48),(529,5.21),(530,0),(531,0),(532,0),(533,0),\\\\ (534,0),(535,0.44),(536,7.51),(537,9.81),(538,9.98),(539,7.86),(540,5.48),(541,5.21\\\\ ),(542,0),(543,0),(544,0),(545,0),(546,0),(547,0.44),(548,7.51),(549,9.81),(550,9.98\\\\ ),(551,7.86),(552,5.48),(553,5.21),(554,0),(555,0),(556,0),(557,0),(558,0),(559,0.44\\\\ ),(560,7.51),(561,9.81),(562,9.98),(563,7.86),(564,5.48),(565,5.21),(566,0),(567,0)\\\\ ,(568,0),(569,0),(570,0),(571,0.44),(572,7.51),(573,9.81),(574,9.98),(575,7.86),(576\\\\ ,5.48),(577,5.21),(578,0),(579,0),(580,0),(581,0),(582,0),(583,0.44),(584,7.51),(585\\\\ ,9.81),(586,9.98),(587,7.86),(588,5.48),(589,5.21),(590,0),(591,0),(592,0),(593,0),\\\\ (594,0),(595,0.44),(596,7.51),(597,9.81),(598,9.98),(599,7.86),(600,5.48),(601,5.21\\\\ ),(602,0),(603,0),(604,0),(605,0),(606,0),(607,0.44),(608,7.51),(609,9.81),(610,9.98\\\\ ),(611,7.86),(612,5.48),(613,5.21),(614,0),(615,0),(616,0),(617,0),(618,0),(619,0.44\\\\ ),(620,7.51),(621,9.81),(622,9.98),(623,7.86),(624,5.48),(625,5.21),(626,0),(627,0)\\\\ ,(628,0),(629,0),(630,0),(631,0.44),(632,7.51),(633,9.81),(634,9.98),(635,7.86),(636\\\\ ,5.48))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365,
        366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383,
        384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401,
        402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419,
        420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437,
        438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455,
        456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473,
        474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491,
        492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509,
        510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527,
        528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545,
        546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563,
        564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581,
        582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599,
        600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617,
        618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635,
        636
    ], [
                                5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44,
                                7.51,
                                9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21,
                                0,
                                0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81,
                                9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0,
                                0,
                                0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98,
                                7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0,
                                0,
                                0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86,
                                5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0,
                                0.44,
                                7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48,
                                5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44,
                                7.51,
                                9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21,
                                0,
                                0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81,
                                9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0,
                                0,
                                0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98,
                                7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0,
                                0,
                                0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86,
                                5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0,
                                0.44,
                                7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48,
                                5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44,
                                7.51,
                                9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21,
                                0,
                                0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81,
                                9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0,
                                0,
                                0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98,
                                7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0,
                                0,
                                0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86,
                                5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0,
                                0.44,
                                7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48,
                                5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44,
                                7.51,
                                9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21,
                                0,
                                0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81,
                                9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0,
                                0,
                                0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98,
                                7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0,
                                0,
                                0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86,
                                5.48
                            ])


@cache('step')
def zr_area_km2():
    """
    Real Name: b'"Zr area (km^2)"'
    Original Eqn: b'zr vol area curve(Zr reservoir)'
    Units: b'km*km'
    Limits: (None, None)
    Type: component

    b''
    """
    return zr_vol_area_curve(zr_reservoir())


@cache('step')
def zr_bfr_tj():
    """
    Real Name: b'Zr bfr Tj'
    Original Eqn: b'Zr aftr Dam-Wr sup aftr Zr Dam+(Wr sup aftr Zr Dam*0.2)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return zr_aftr_dam() - wr_sup_aftr_zr_dam() + (wr_sup_aftr_zr_dam() * 0.2)


def zr_dom_dem(x):
    """
    Real Name: b'zr dom dem'
    Original Eqn: b'( [(1,0.1)-(365,0.2)],(1,0.13),(2,0.13),(3,0.13),(4,0.13),(5,0.13),(6,0.13),(7,0.13),(\\\\ 8,0.13),(9,0.13),(10,0.13),(11,0.13),(12,0.13),(13,0.13),(14,0.13),(15,0.13),(16,0.13\\\\ ),(17,0.13),(18,0.13),(19,0.13),(20,0.13),(21,0.13),(22,0.13),(23,0.13),(24,0.13),(\\\\ 25,0.13),(26,0.13),(27,0.13),(28,0.13),(29,0.13),(30,0.13),(31,0.13),(32,0.13),(33,\\\\ 0.13),(34,0.13),(35,0.13),(36,0.13),(37,0.13),(38,0.13),(39,0.13),(40,0.13),(41,0.13\\\\ ),(42,0.13),(43,0.13),(44,0.13),(45,0.13),(46,0.13),(47,0.13),(48,0.13),(49,0.13),(\\\\ 50,0.13),(51,0.13),(52,0.13),(53,0.13),(54,0.13),(55,0.13),(56,0.13),(57,0.13),(58,\\\\ 0.13),(59,0.13),(60,0.13),(61,0.13),(62,0.13),(63,0.13),(64,0.13),(65,0.13),(66,0.13\\\\ ),(67,0.13),(68,0.13),(69,0.13),(70,0.13),(71,0.13),(72,0.13),(73,0.13),(74,0.13),(\\\\ 75,0.13),(76,0.13),(77,0.13),(78,0.13),(79,0.13),(80,0.13),(81,0.13),(82,0.13),(83,\\\\ 0.13),(84,0.13),(85,0.13),(86,0.13),(87,0.13),(88,0.13),(89,0.13),(90,0.13),(91,0.13\\\\ ),(92,0.13),(93,0.13),(94,0.13),(95,0.13),(96,0.13),(97,0.13),(98,0.13),(99,0.13),(\\\\ 100,0.13),(101,0.13),(102,0.13),(103,0.13),(104,0.13),(105,0.13),(106,0.13),(107,0.13\\\\ ),(108,0.13),(109,0.13),(110,0.13),(111,0.13),(112,0.13),(113,0.13),(114,0.13),(115\\\\ ,0.13),(116,0.13),(117,0.13),(118,0.13),(119,0.13),(120,0.13),(121,0.13),(122,0.13)\\\\ ,(123,0.13),(124,0.13),(125,0.13),(126,0.13),(127,0.13),(128,0.13),(129,0.13),(130,\\\\ 0.13),(131,0.13),(132,0.13),(133,0.13),(134,0.13),(135,0.13),(136,0.13),(137,0.13),\\\\ (138,0.13),(139,0.13),(140,0.13),(141,0.13),(142,0.13),(143,0.13),(144,0.13),(145,0.13\\\\ ),(146,0.13),(147,0.13),(148,0.13),(149,0.13),(150,0.13),(151,0.13),(152,0.13),(153\\\\ ,0.13),(154,0.13),(155,0.13),(156,0.13),(157,0.13),(158,0.13),(159,0.13),(160,0.13)\\\\ ,(161,0.13),(162,0.13),(163,0.13),(164,0.13),(165,0.13),(166,0.13),(167,0.13),(168,\\\\ 0.13),(169,0.13),(170,0.13),(171,0.13),(172,0.13),(173,0.13),(174,0.13),(175,0.13),\\\\ (176,0.13),(177,0.13),(178,0.13),(179,0.13),(180,0.13),(181,0.13),(182,0.13),(183,0.13\\\\ ),(184,0.13),(185,0.13),(186,0.13),(187,0.13),(188,0.13),(189,0.13),(190,0.13),(191\\\\ ,0.13),(192,0.13),(193,0.13),(194,0.13),(195,0.13),(196,0.13),(197,0.13),(198,0.13)\\\\ ,(199,0.13),(200,0.13),(201,0.13),(202,0.13),(203,0.13),(204,0.13),(205,0.13),(206,\\\\ 0.13),(207,0.13),(208,0.13),(209,0.13),(210,0.13),(211,0.13),(212,0.13),(213,0.13),\\\\ (214,0.13),(215,0.13),(216,0.13),(217,0.13),(218,0.13),(219,0.13),(220,0.13),(221,0.13\\\\ ),(222,0.13),(223,0.13),(224,0.13),(225,0.13),(226,0.13),(227,0.13),(228,0.13),(229\\\\ ,0.13),(230,0.13),(231,0.13),(232,0.13),(233,0.13),(234,0.13),(235,0.13),(236,0.13)\\\\ ,(237,0.13),(238,0.13),(239,0.13),(240,0.13),(241,0.13),(242,0.13),(243,0.13),(244,\\\\ 0.13),(245,0.13),(246,0.13),(247,0.13),(248,0.13),(249,0.13),(250,0.13),(251,0.13),\\\\ (252,0.13),(253,0.13),(254,0.13),(255,0.13),(256,0.13),(257,0.13),(258,0.13),(259,0.13\\\\ ),(260,0.13),(261,0.13),(262,0.13),(263,0.13),(264,0.13),(265,0.13),(266,0.13),(267\\\\ ,0.13),(268,0.13),(269,0.13),(270,0.13),(271,0.13),(272,0.13),(273,0.13),(274,0.13)\\\\ ,(275,0.13),(276,0.13),(277,0.13),(278,0.13),(279,0.13),(280,0.13),(281,0.13),(282,\\\\ 0.13),(283,0.13),(284,0.13),(285,0.13),(286,0.13),(287,0.13),(288,0.13),(289,0.13),\\\\ (290,0.13),(291,0.13),(292,0.13),(293,0.13),(294,0.13),(295,0.13),(296,0.13),(297,0.13\\\\ ),(298,0.13),(299,0.13),(300,0.13),(301,0.13),(302,0.13),(303,0.13),(304,0.13),(305\\\\ ,0.13),(306,0.13),(307,0.13),(308,0.13),(309,0.13),(310,0.13),(311,0.13),(312,0.13)\\\\ ,(313,0.13),(314,0.13),(315,0.13),(316,0.13),(317,0.13),(318,0.13),(319,0.13),(320,\\\\ 0.13),(321,0.13),(322,0.13),(323,0.13),(324,0.13),(325,0.13),(326,0.13),(327,0.13),\\\\ (328,0.13),(329,0.13),(330,0.13),(331,0.13),(332,0.13),(333,0.13),(334,0.13),(335,0.13\\\\ ),(336,0.13),(337,0.13),(338,0.13),(339,0.13),(340,0.13),(341,0.13),(342,0.13),(343\\\\ ,0.13),(344,0.13),(345,0.13),(346,0.13),(347,0.13),(348,0.13),(349,0.13),(350,0.13)\\\\ ,(351,0.13),(352,0.13),(353,0.13),(354,0.13),(355,0.13),(356,0.13),(357,0.13),(358,\\\\ 0.13),(359,0.13),(360,0.13),(361,0.13),(362,0.13),(363,0.13),(364,0.13),(365,0.13))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], [
                                0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
                                0.13,
                                0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
                                0.13,
                                0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
                                0.13,
                                0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
                                0.13,
                                0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
                                0.13,
                                0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
                                0.13,
                                0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
                                0.13,
                                0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
                                0.13,
                                0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
                                0.13,
                                0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
                                0.13,
                                0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
                                0.13,
                                0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
                                0.13,
                                0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
                                0.13,
                                0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
                                0.13,
                                0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
                                0.13,
                                0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
                                0.13,
                                0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
                                0.13,
                                0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
                                0.13,
                                0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
                                0.13,
                                0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
                                0.13,
                                0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
                                0.13,
                                0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
                                0.13,
                                0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
                                0.13,
                                0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
                                0.13,
                                0.13, 0.13, 0.13, 0.13, 0.13
                            ])


@cache('step')
def zr_ele():
    """
    Real Name: b'zr ele'
    Original Eqn: b'zr vol ele curve(Zr reservoir)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return zr_vol_ele_curve(zr_reservoir())


def zr_vol_area_curve(x):
    """
    Real Name: b'zr vol area curve'
    Original Eqn: b'( [(0,0)-(239.71,6.0476)],(0,0),(0.05,0.051),(0.5,0.1383),(1.57,0.285),(3.32,0.457),(6.18\\\\ ,0.663),(9.66,0.829),(14.45,1.0026),(19.84,1.2202),(26.86,1.4963),(34.82,1.794),(44.66\\\\ ,2.0798),(55.67,2.3895),(68.56,2.7136),(82.73,3.0343),(99.18,3.4241),(116.91,3.8179\\\\ ),(137.3,4.2143),(159.18,4.6487),(183.91,5.1236),(239.71,6.0476))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b'[(0,0)-(239.71,6.0476)],(0,0),(0.05,0.051),(0.5,0.1383),(1.57,0.285),(3.32,\\n    \\t\\t0.457),(6.18,0.663),(9.66,0.829),(14.45,1.0026),(19.84,1.2202),(26.86,1.496\\n    \\t\\t3),(34.82,1.794),(44.66,2.0798),(55.67,2.3895),(68.56,2.7136),(82.73,3.0343\\n    \\t\\t),(99.18,3.4241),(116.91,3.8179),(137.3,4.2143),(159.18,4.6487),(183.91,5.1\\n    \\t\\t236),(239.71,6.0476)'
    """
    return functions.lookup(x, [
        0, 0.05, 0.5, 1.57, 3.32, 6.18, 9.66, 14.45, 19.84, 26.86, 34.82, 44.66, 55.67, 68.56,
        82.73, 99.18, 116.91, 137.3, 159.18, 183.91, 239.71
    ], [
                                0, 0.051, 0.1383, 0.285, 0.457, 0.663, 0.829, 1.0026, 1.2202, 1.4963, 1.794, 2.0798,
                                2.3895, 2.7136, 3.0343, 3.4241, 3.8179, 4.2143, 4.6487, 5.1236, 6.0476
                            ])


def total_inter_zr2div(x):
    """
    Real Name: b'Total Inter Zr2Div'
    Original Eqn: b'( [(1,0)-(365,1)],(1,0.06439),(2,0.06439),(3,0.06439),(4,0.06439),(5,0.06439),(6,0.06439\\\\ ),(7,0.06439),(8,0.06439),(9,0.06439),(10,0.06439),(11,0.06439),(12,0.06439),(13,0.06439\\\\ ),(14,0.06439),(15,0.06439),(16,0.06439),(17,0.06439),(18,0.06439),(19,0.06439),(20\\\\ ,0.06439),(21,0.06439),(22,0.06439),(23,0.06439),(24,0.06439),(25,0.06439),(26,0.06439\\\\ ),(27,0.06439),(28,0.06439),(29,0.06439),(30,0.06439),(31,0.11676),(32,0.11676),(33\\\\ ,0.11676),(34,0.11676),(35,0.11676),(36,0.11676),(37,0.11676),(38,0.11676),(39,0.11676\\\\ ),(40,0.11676),(41,0.11676),(42,0.11676),(43,0.11676),(44,0.11676),(45,0.11676),(46\\\\ ,0.11676),(47,0.11676),(48,0.11676),(49,0.11676),(50,0.11676),(51,0.11676),(52,0.11676\\\\ ),(53,0.11676),(54,0.11676),(55,0.11676),(56,0.11676),(57,0.11676),(58,0.11676),(59\\\\ ,0.11676),(60,0.11676),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,\\\\ 0),(70,0),(71,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81\\\\ ,0),(82,0),(83,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0.16065),(92\\\\ ,0.16065),(93,0.16065),(94,0.16065),(95,0.16065),(96,0.16065),(97,0.16065),(98,0.16065\\\\ ),(99,0.16065),(100,0.16065),(101,0.16065),(102,0.16065),(103,0.16065),(104,0.16065\\\\ ),(105,0.16065),(106,0.16065),(107,0.16065),(108,0.16065),(109,0.16065),(110,0.16065\\\\ ),(111,0.16065),(112,0.16065),(113,0.16065),(114,0.16065),(115,0.16065),(116,0.16065\\\\ ),(117,0.16065),(118,0.16065),(119,0.16065),(120,0.16065),(121,0.63944),(122,0.63944\\\\ ),(123,0.63944),(124,0.63944),(125,0.63944),(126,0.63944),(127,0.63944),(128,0.63944\\\\ ),(129,0.63944),(130,0.63944),(131,0.63944),(132,0.63944),(133,0.63944),(134,0.63944\\\\ ),(135,0.63944),(136,0.63944),(137,0.63944),(138,0.63944),(139,0.63944),(140,0.63944\\\\ ),(141,0.63944),(142,0.63944),(143,0.63944),(144,0.63944),(145,0.63944),(146,0.63944\\\\ ),(147,0.63944),(148,0.63944),(149,0.63944),(150,0.63944),(151,0.98094),(152,0.98094\\\\ ),(153,0.98094),(154,0.98094),(155,0.98094),(156,0.98094),(157,0.98094),(158,0.98094\\\\ ),(159,0.98094),(160,0.98094),(161,0.98094),(162,0.98094),(163,0.98094),(164,0.98094\\\\ ),(165,0.98094),(166,0.98094),(167,0.98094),(168,0.98094),(169,0.98094),(170,0.98094\\\\ ),(171,0.98094),(172,0.98094),(173,0.98094),(174,0.98094),(175,0.98094),(176,0.98094\\\\ ),(177,0.98094),(178,0.98094),(179,0.98094),(180,0.98094),(181,0.01199),(182,0.01199\\\\ ),(183,0.01199),(184,0.01199),(185,0.01199),(186,0.01199),(187,0.01199),(188,0.01199\\\\ ),(189,0.01199),(190,0.01199),(191,0.01199),(192,0.01199),(193,0.01199),(194,0.01199\\\\ ),(195,0.01199),(196,0.01199),(197,0.01199),(198,0.01199),(199,0.01199),(200,0.01199\\\\ ),(201,0.01199),(202,0.01199),(203,0.01199),(204,0.01199),(205,0.01199),(206,0.01199\\\\ ),(207,0.01199),(208,0.01199),(209,0.01199),(210,0.01199),(211,0),(212,0),(213,0),(\\\\ 214,0),(215,0),(216,0),(217,0),(218,0),(219,0),(220,0),(221,0),(222,0),(223,0),(224\\\\ ,0),(225,0),(226,0),(227,0),(228,0),(229,0),(230,0),(231,0),(232,0),(233,0),(234,0)\\\\ ,(235,0),(236,0),(237,0),(238,0),(239,0),(240,0),(241,0),(242,0),(243,0),(244,0),(245\\\\ ,0),(246,0),(247,0),(248,0),(249,0),(250,0),(251,0),(252,0),(253,0),(254,0),(255,0)\\\\ ,(256,0),(257,0),(258,0),(259,0),(260,0),(261,0),(262,0),(263,0),(264,0),(265,0),(266\\\\ ,0),(267,0),(268,0),(269,0),(270,0),(271,0.02971),(272,0.02971),(273,0.02971),(274,\\\\ 0.02971),(275,0.02971),(276,0.02971),(277,0.02971),(278,0.02971),(279,0.02971),(280\\\\ ,0.02971),(281,0.02971),(282,0.02971),(283,0.02971),(284,0.02971),(285,0.02971),(286\\\\ ,0.02971),(287,0.02971),(288,0.02971),(289,0.02971),(290,0.02971),(291,0.02971),(292\\\\ ,0.02971),(293,0.02971),(294,0.02971),(295,0.02971),(296,0.02971),(297,0.02971),(298\\\\ ,0.02971),(299,0.02971),(300,0.02971),(301,0),(302,0),(303,0),(304,0),(305,0),(306,\\\\ 0),(307,0),(308,0),(309,0),(310,0),(311,0),(312,0),(313,0),(314,0),(315,0),(316,0),\\\\ (317,0),(318,0),(319,0),(320,0),(321,0),(322,0),(323,0),(324,0),(325,0),(326,0),(327\\\\ ,0),(328,0),(329,0),(330,0),(331,0.00536),(332,0.00536),(333,0.00536),(334,0.00536)\\\\ ,(335,0.00536),(336,0.00536),(337,0.00536),(338,0.00536),(339,0.00536),(340,0.00536\\\\ ),(341,0.00536),(342,0.00536),(343,0.00536),(344,0.00536),(345,0.00536),(346,0.00536\\\\ ),(347,0.00536),(348,0.00536),(349,0.00536),(350,0.00536),(351,0.00536),(352,0.00536\\\\ ),(353,0.00536),(354,0.00536),(355,0.00536),(356,0.00536),(357,0.00536),(358,0.00536\\\\ ),(359,0.00536),(360,0.00536),(361,0.00536),(362,0.00536),(363,0.00536),(364,0.00536\\\\ ),(365,0.00536))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], [
                                0.06439, 0.06439, 0.06439, 0.06439, 0.06439, 0.06439, 0.06439, 0.06439, 0.06439,
                                0.06439,
                                0.06439, 0.06439, 0.06439, 0.06439, 0.06439, 0.06439, 0.06439, 0.06439, 0.06439,
                                0.06439,
                                0.06439, 0.06439, 0.06439, 0.06439, 0.06439, 0.06439, 0.06439, 0.06439, 0.06439,
                                0.06439,
                                0.11676, 0.11676, 0.11676, 0.11676, 0.11676, 0.11676, 0.11676, 0.11676, 0.11676,
                                0.11676,
                                0.11676, 0.11676, 0.11676, 0.11676, 0.11676, 0.11676, 0.11676, 0.11676, 0.11676,
                                0.11676,
                                0.11676, 0.11676, 0.11676, 0.11676, 0.11676, 0.11676, 0.11676, 0.11676, 0.11676,
                                0.11676,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0.16065, 0.16065, 0.16065, 0.16065, 0.16065, 0.16065, 0.16065, 0.16065, 0.16065,
                                0.16065,
                                0.16065, 0.16065, 0.16065, 0.16065, 0.16065, 0.16065, 0.16065, 0.16065, 0.16065,
                                0.16065,
                                0.16065, 0.16065, 0.16065, 0.16065, 0.16065, 0.16065, 0.16065, 0.16065, 0.16065,
                                0.16065,
                                0.63944, 0.63944, 0.63944, 0.63944, 0.63944, 0.63944, 0.63944, 0.63944, 0.63944,
                                0.63944,
                                0.63944, 0.63944, 0.63944, 0.63944, 0.63944, 0.63944, 0.63944, 0.63944, 0.63944,
                                0.63944,
                                0.63944, 0.63944, 0.63944, 0.63944, 0.63944, 0.63944, 0.63944, 0.63944, 0.63944,
                                0.63944,
                                0.98094, 0.98094, 0.98094, 0.98094, 0.98094, 0.98094, 0.98094, 0.98094, 0.98094,
                                0.98094,
                                0.98094, 0.98094, 0.98094, 0.98094, 0.98094, 0.98094, 0.98094, 0.98094, 0.98094,
                                0.98094,
                                0.98094, 0.98094, 0.98094, 0.98094, 0.98094, 0.98094, 0.98094, 0.98094, 0.98094,
                                0.98094,
                                0.01199, 0.01199, 0.01199, 0.01199, 0.01199, 0.01199, 0.01199, 0.01199, 0.01199,
                                0.01199,
                                0.01199, 0.01199, 0.01199, 0.01199, 0.01199, 0.01199, 0.01199, 0.01199, 0.01199,
                                0.01199,
                                0.01199, 0.01199, 0.01199, 0.01199, 0.01199, 0.01199, 0.01199, 0.01199, 0.01199,
                                0.01199,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0.02971, 0.02971, 0.02971, 0.02971, 0.02971, 0.02971, 0.02971, 0.02971, 0.02971,
                                0.02971,
                                0.02971, 0.02971, 0.02971, 0.02971, 0.02971, 0.02971, 0.02971, 0.02971, 0.02971,
                                0.02971,
                                0.02971, 0.02971, 0.02971, 0.02971, 0.02971, 0.02971, 0.02971, 0.02971, 0.02971,
                                0.02971,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0.00536, 0.00536, 0.00536, 0.00536, 0.00536, 0.00536, 0.00536, 0.00536, 0.00536,
                                0.00536,
                                0.00536, 0.00536, 0.00536, 0.00536, 0.00536, 0.00536, 0.00536, 0.00536, 0.00536,
                                0.00536,
                                0.00536, 0.00536, 0.00536, 0.00536, 0.00536, 0.00536, 0.00536, 0.00536, 0.00536,
                                0.00536,
                                0.00536, 0.00536, 0.00536, 0.00536, 0.00536
                            ])


def zr_upstream(x):
    """
    Real Name: b'zr upstream'
    Original Eqn: b'( [(1,0)-(365,2)],(1,0.78),(2,0.78),(3,0.78),(4,0.78),(5,0.78),(6,0.78),(7,0.78),(8,0.78\\\\ ),(9,0.78),(10,0.78),(11,0.78),(12,0.78),(13,0.78),(14,0.78),(15,0.78),(16,0.78),(17\\\\ ,0.78),(18,0.78),(19,0.78),(20,0.78),(21,0.78),(22,0.78),(23,0.78),(24,0.78),(25,0.78\\\\ ),(26,0.78),(27,0.78),(28,0.78),(29,0.78),(30,0.78),(31,0.59),(32,0.59),(33,0.59),(\\\\ 34,0.59),(35,0.59),(36,0.59),(37,0.59),(38,0.59),(39,0.59),(40,0.59),(41,0.59),(42,\\\\ 0.59),(43,0.59),(44,0.59),(45,0.59),(46,0.59),(47,0.59),(48,0.59),(49,0.59),(50,0.59\\\\ ),(51,0.59),(52,0.59),(53,0.59),(54,0.59),(55,0.59),(56,0.59),(57,0.59),(58,0.59),(\\\\ 59,0.59),(60,0.59),(61,0.41),(62,0.41),(63,0.41),(64,0.41),(65,0.41),(66,0.41),(67,\\\\ 0.41),(68,0.41),(69,0.41),(70,0.41),(71,0.41),(72,0.41),(73,0.41),(74,0.41),(75,0.41\\\\ ),(76,0.41),(77,0.41),(78,0.41),(79,0.41),(80,0.41),(81,0.41),(82,0.41),(83,0.41),(\\\\ 84,0.41),(85,0.41),(86,0.41),(87,0.41),(88,0.41),(89,0.41),(90,0.41),(91,0.39),(92,\\\\ 0.39),(93,0.39),(94,0.39),(95,0.39),(96,0.39),(97,0.39),(98,0.39),(99,0.39),(100,0.39\\\\ ),(101,0.39),(102,0.39),(103,0.39),(104,0.39),(105,0.39),(106,0.39),(107,0.39),(108\\\\ ,0.39),(109,0.39),(110,0.39),(111,0.39),(112,0.39),(113,0.39),(114,0.39),(115,0.39)\\\\ ,(116,0.39),(117,0.39),(118,0.39),(119,0.39),(120,0.39),(121,0.99),(122,0.99),(123,\\\\ 0.99),(124,0.99),(125,0.99),(126,0.99),(127,0.99),(128,0.99),(129,0.99),(130,0.99),\\\\ (131,0.99),(132,0.99),(133,0.99),(134,0.99),(135,0.99),(136,0.99),(137,0.99),(138,0.99\\\\ ),(139,0.99),(140,0.99),(141,0.99),(142,0.99),(143,0.99),(144,0.99),(145,0.99),(146\\\\ ,0.99),(147,0.99),(148,0.99),(149,0.99),(150,0.99),(151,1.79),(152,1.79),(153,1.79)\\\\ ,(154,1.79),(155,1.79),(156,1.79),(157,1.79),(158,1.79),(159,1.79),(160,1.79),(161,\\\\ 1.79),(162,1.79),(163,1.79),(164,1.79),(165,1.79),(166,1.79),(167,1.79),(168,1.79),\\\\ (169,1.79),(170,1.79),(171,1.79),(172,1.79),(173,1.79),(174,1.79),(175,1.79),(176,1.79\\\\ ),(177,1.79),(178,1.79),(179,1.79),(180,1.79),(181,1.53),(182,1.53),(183,1.53),(184\\\\ ,1.53),(185,1.53),(186,1.53),(187,1.53),(188,1.53),(189,1.53),(190,1.53),(191,1.53)\\\\ ,(192,1.53),(193,1.53),(194,1.53),(195,1.53),(196,1.53),(197,1.53),(198,1.53),(199,\\\\ 1.53),(200,1.53),(201,1.53),(202,1.53),(203,1.53),(204,1.53),(205,1.53),(206,1.53),\\\\ (207,1.53),(208,1.53),(209,1.53),(210,1.53),(211,0.35),(212,0.35),(213,0.35),(214,0.35\\\\ ),(215,0.35),(216,0.35),(217,0.35),(218,0.35),(219,0.35),(220,0.35),(221,0.35),(222\\\\ ,0.35),(223,0.35),(224,0.35),(225,0.35),(226,0.35),(227,0.35),(228,0.35),(229,0.35)\\\\ ,(230,0.35),(231,0.35),(232,0.35),(233,0.35),(234,0.35),(235,0.35),(236,0.35),(237,\\\\ 0.35),(238,0.35),(239,0.35),(240,0.35),(241,0.21),(242,0.21),(243,0.21),(244,0.21),\\\\ (245,0.21),(246,0.21),(247,0.21),(248,0.21),(249,0.21),(250,0.21),(251,0.21),(252,0.21\\\\ ),(253,0.21),(254,0.21),(255,0.21),(256,0.21),(257,0.21),(258,0.21),(259,0.21),(260\\\\ ,0.21),(261,0.21),(262,0.21),(263,0.21),(264,0.21),(265,0.21),(266,0.21),(267,0.21)\\\\ ,(268,0.21),(269,0.21),(270,0.21),(271,0.21),(272,0.21),(273,0.21),(274,0.21),(275,\\\\ 0.21),(276,0.21),(277,0.21),(278,0.21),(279,0.21),(280,0.21),(281,0.21),(282,0.21),\\\\ (283,0.21),(284,0.21),(285,0.21),(286,0.21),(287,0.21),(288,0.21),(289,0.21),(290,0.21\\\\ ),(291,0.21),(292,0.21),(293,0.21),(294,0.21),(295,0.21),(296,0.21),(297,0.21),(298\\\\ ,0.21),(299,0.21),(300,0.21),(301,0.21),(302,0.21),(303,0.21),(304,0.21),(305,0.21)\\\\ ,(306,0.21),(307,0.21),(308,0.21),(309,0.21),(310,0.21),(311,0.21),(312,0.21),(313,\\\\ 0.21),(314,0.21),(315,0.21),(316,0.21),(317,0.21),(318,0.21),(319,0.21),(320,0.21),\\\\ (321,0.21),(322,0.21),(323,0.21),(324,0.21),(325,0.21),(326,0.21),(327,0.21),(328,0.21\\\\ ),(329,0.21),(330,0.21),(331,0.31),(332,0.31),(333,0.31),(334,0.31),(335,0.31),(336\\\\ ,0.31),(337,0.31),(338,0.31),(339,0.31),(340,0.31),(341,0.31),(342,0.31),(343,0.31)\\\\ ,(344,0.31),(345,0.31),(346,0.31),(347,0.31),(348,0.31),(349,0.31),(350,0.31),(351,\\\\ 0.31),(352,0.31),(353,0.31),(354,0.31),(355,0.31),(356,0.31),(357,0.31),(358,0.31),\\\\ (359,0.31),(360,0.31),(361,0.31),(362,0.31),(363,0.31),(364,0.31),(365,0.31))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b"GET XLS DATA( 'Zalemroud.xls', 'Inputs', 'A', 'B2')"
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], [
                                0.78, 0.78, 0.78, 0.78, 0.78, 0.78, 0.78, 0.78, 0.78, 0.78, 0.78, 0.78, 0.78, 0.78,
                                0.78,
                                0.78, 0.78, 0.78, 0.78, 0.78, 0.78, 0.78, 0.78, 0.78, 0.78, 0.78, 0.78, 0.78, 0.78,
                                0.78,
                                0.59, 0.59, 0.59, 0.59, 0.59, 0.59, 0.59, 0.59, 0.59, 0.59, 0.59, 0.59, 0.59, 0.59,
                                0.59,
                                0.59, 0.59, 0.59, 0.59, 0.59, 0.59, 0.59, 0.59, 0.59, 0.59, 0.59, 0.59, 0.59, 0.59,
                                0.59,
                                0.41, 0.41, 0.41, 0.41, 0.41, 0.41, 0.41, 0.41, 0.41, 0.41, 0.41, 0.41, 0.41, 0.41,
                                0.41,
                                0.41, 0.41, 0.41, 0.41, 0.41, 0.41, 0.41, 0.41, 0.41, 0.41, 0.41, 0.41, 0.41, 0.41,
                                0.41,
                                0.39, 0.39, 0.39, 0.39, 0.39, 0.39, 0.39, 0.39, 0.39, 0.39, 0.39, 0.39, 0.39, 0.39,
                                0.39,
                                0.39, 0.39, 0.39, 0.39, 0.39, 0.39, 0.39, 0.39, 0.39, 0.39, 0.39, 0.39, 0.39, 0.39,
                                0.39,
                                0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99,
                                0.99,
                                0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99,
                                0.99,
                                1.79, 1.79, 1.79, 1.79, 1.79, 1.79, 1.79, 1.79, 1.79, 1.79, 1.79, 1.79, 1.79, 1.79,
                                1.79,
                                1.79, 1.79, 1.79, 1.79, 1.79, 1.79, 1.79, 1.79, 1.79, 1.79, 1.79, 1.79, 1.79, 1.79,
                                1.79,
                                1.53, 1.53, 1.53, 1.53, 1.53, 1.53, 1.53, 1.53, 1.53, 1.53, 1.53, 1.53, 1.53, 1.53,
                                1.53,
                                1.53, 1.53, 1.53, 1.53, 1.53, 1.53, 1.53, 1.53, 1.53, 1.53, 1.53, 1.53, 1.53, 1.53,
                                1.53,
                                0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35,
                                0.35,
                                0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35,
                                0.35,
                                0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21,
                                0.21,
                                0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21,
                                0.21,
                                0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21,
                                0.21,
                                0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21,
                                0.21,
                                0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21,
                                0.21,
                                0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21,
                                0.21,
                                0.31, 0.31, 0.31, 0.31, 0.31, 0.31, 0.31, 0.31, 0.31, 0.31, 0.31, 0.31, 0.31, 0.31,
                                0.31,
                                0.31, 0.31, 0.31, 0.31, 0.31, 0.31, 0.31, 0.31, 0.31, 0.31, 0.31, 0.31, 0.31, 0.31,
                                0.31,
                                0.31, 0.31, 0.31, 0.31, 0.31
                            ])


def zr_onthly_evap(x):
    """
    Real Name: b'Zr onthly evap'
    Original Eqn: b'( [(1,0)-(365,7)],(1,1.87),(2,1.87),(3,1.87),(4,1.87),(5,1.87),(6,1.87),(7,1.87),(8,1.87\\\\ ),(9,1.87),(10,1.87),(11,1.87),(12,1.87),(13,1.87),(14,1.87),(15,1.87),(16,1.87),(17\\\\ ,1.87),(18,1.87),(19,1.87),(20,1.87),(21,1.87),(22,1.87),(23,1.87),(24,1.87),(25,1.87\\\\ ),(26,1.87),(27,1.87),(28,1.87),(29,1.87),(30,1.87),(31,1),(32,1),(33,1),(34,1),(35\\\\ ,1),(36,1),(37,1),(38,1),(39,1),(40,1),(41,1),(42,1),(43,1),(44,1),(45,1),(46,1),(47\\\\ ,1),(48,1),(49,1),(50,1),(51,1),(52,1),(53,1),(54,1),(55,1),(56,1),(57,1),(58,1),(59\\\\ ,1),(60,1),(61,0.47),(62,0.47),(63,0.47),(64,0.47),(65,0.47),(66,0.47),(67,0.47),(68\\\\ ,0.47),(69,0.47),(70,0.47),(71,0.47),(72,0.47),(73,0.47),(74,0.47),(75,0.47),(76,0.47\\\\ ),(77,0.47),(78,0.47),(79,0.47),(80,0.47),(81,0.47),(82,0.47),(83,0.47),(84,0.47),(\\\\ 85,0.47),(86,0.47),(87,0.47),(88,0.47),(89,0.47),(90,0.47),(91,0.27),(92,0.27),(93,\\\\ 0.27),(94,0.27),(95,0.27),(96,0.27),(97,0.27),(98,0.27),(99,0.27),(100,0.27),(101,0.27\\\\ ),(102,0.27),(103,0.27),(104,0.27),(105,0.27),(106,0.27),(107,0.27),(108,0.27),(109\\\\ ,0.27),(110,0.27),(111,0.27),(112,0.27),(113,0.27),(114,0.27),(115,0.27),(116,0.27)\\\\ ,(117,0.27),(118,0.27),(119,0.27),(120,0.27),(121,0.3),(122,0.3),(123,0.3),(124,0.3\\\\ ),(125,0.3),(126,0.3),(127,0.3),(128,0.3),(129,0.3),(130,0.3),(131,0.3),(132,0.3),(\\\\ 133,0.3),(134,0.3),(135,0.3),(136,0.3),(137,0.3),(138,0.3),(139,0.3),(140,0.3),(141\\\\ ,0.3),(142,0.3),(143,0.3),(144,0.3),(145,0.3),(146,0.3),(147,0.3),(148,0.3),(149,0.3\\\\ ),(150,0.3),(151,0.53),(152,0.53),(153,0.53),(154,0.53),(155,0.53),(156,0.53),(157,\\\\ 0.53),(158,0.53),(159,0.53),(160,0.53),(161,0.53),(162,0.53),(163,0.53),(164,0.53),\\\\ (165,0.53),(166,0.53),(167,0.53),(168,0.53),(169,0.53),(170,0.53),(171,0.53),(172,0.53\\\\ ),(173,0.53),(174,0.53),(175,0.53),(176,0.53),(177,0.53),(178,0.53),(179,0.53),(180\\\\ ,0.53),(181,1.97),(182,1.97),(183,1.97),(184,1.97),(185,1.97),(186,1.97),(187,1.97)\\\\ ,(188,1.97),(189,1.97),(190,1.97),(191,1.97),(192,1.97),(193,1.97),(194,1.97),(195,\\\\ 1.97),(196,1.97),(197,1.97),(198,1.97),(199,1.97),(200,1.97),(201,1.97),(202,1.97),\\\\ (203,1.97),(204,1.97),(205,1.97),(206,1.97),(207,1.97),(208,1.97),(209,1.97),(210,1.97\\\\ ),(211,3.5),(212,3.5),(213,3.5),(214,3.5),(215,3.5),(216,3.5),(217,3.5),(218,3.5),(\\\\ 219,3.5),(220,3.5),(221,3.5),(222,3.5),(223,3.5),(224,3.5),(225,3.5),(226,3.5),(227\\\\ ,3.5),(228,3.5),(229,3.5),(230,3.5),(231,3.5),(232,3.5),(233,3.5),(234,3.5),(235,3.5\\\\ ),(236,3.5),(237,3.5),(238,3.5),(239,3.5),(240,3.5),(241,5.13),(242,5.13),(243,5.13\\\\ ),(244,5.13),(245,5.13),(246,5.13),(247,5.13),(248,5.13),(249,5.13),(250,5.13),(251\\\\ ,5.13),(252,5.13),(253,5.13),(254,5.13),(255,5.13),(256,5.13),(257,5.13),(258,5.13)\\\\ ,(259,5.13),(260,5.13),(261,5.13),(262,5.13),(263,5.13),(264,5.13),(265,5.13),(266,\\\\ 5.13),(267,5.13),(268,5.13),(269,5.13),(270,5.13),(271,6.37),(272,6.37),(273,6.37),\\\\ (274,6.37),(275,6.37),(276,6.37),(277,6.37),(278,6.37),(279,6.37),(280,6.37),(281,6.37\\\\ ),(282,6.37),(283,6.37),(284,6.37),(285,6.37),(286,6.37),(287,6.37),(288,6.37),(289\\\\ ,6.37),(290,6.37),(291,6.37),(292,6.37),(293,6.37),(294,6.37),(295,6.37),(296,6.37)\\\\ ,(297,6.37),(298,6.37),(299,6.37),(300,6.37),(301,6.37),(302,6.37),(303,6.37),(304,\\\\ 6.37),(305,6.37),(306,6.37),(307,6.37),(308,6.37),(309,6.37),(310,6.37),(311,6.37),\\\\ (312,6.37),(313,6.37),(314,6.37),(315,6.37),(316,6.37),(317,6.37),(318,6.37),(319,6.37\\\\ ),(320,6.37),(321,6.37),(322,6.37),(323,6.37),(324,6.37),(325,6.37),(326,6.37),(327\\\\ ,6.37),(328,6.37),(329,6.37),(330,6.37),(331,4.83),(332,4.83),(333,4.83),(334,4.83)\\\\ ,(335,4.83),(336,4.83),(337,4.83),(338,4.83),(339,4.83),(340,4.83),(341,4.83),(342,\\\\ 4.83),(343,4.83),(344,4.83),(345,4.83),(346,4.83),(347,4.83),(348,4.83),(349,4.83),\\\\ (350,4.83),(351,4.83),(352,4.83),(353,4.83),(354,4.83),(355,4.83),(356,4.83),(357,4.83\\\\ ),(358,4.83),(359,4.83),(360,4.83),(361,4.83),(362,4.83),(363,4.83),(364,4.83),(365\\\\ ,4.83))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], [
                                1.87, 1.87, 1.87, 1.87, 1.87, 1.87, 1.87, 1.87, 1.87, 1.87, 1.87, 1.87, 1.87, 1.87,
                                1.87,
                                1.87, 1.87, 1.87, 1.87, 1.87, 1.87, 1.87, 1.87, 1.87, 1.87, 1.87, 1.87, 1.87, 1.87,
                                1.87,
                                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                1,
                                0.47, 0.47, 0.47, 0.47, 0.47, 0.47, 0.47, 0.47, 0.47, 0.47, 0.47, 0.47, 0.47, 0.47,
                                0.47,
                                0.47, 0.47, 0.47, 0.47, 0.47, 0.47, 0.47, 0.47, 0.47, 0.47, 0.47, 0.47, 0.47, 0.47,
                                0.47,
                                0.27, 0.27, 0.27, 0.27, 0.27, 0.27, 0.27, 0.27, 0.27, 0.27, 0.27, 0.27, 0.27, 0.27,
                                0.27,
                                0.27, 0.27, 0.27, 0.27, 0.27, 0.27, 0.27, 0.27, 0.27, 0.27, 0.27, 0.27, 0.27, 0.27,
                                0.27,
                                0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
                                0.3,
                                0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.53, 0.53, 0.53, 0.53,
                                0.53,
                                0.53, 0.53, 0.53, 0.53, 0.53, 0.53, 0.53, 0.53, 0.53, 0.53, 0.53, 0.53, 0.53, 0.53,
                                0.53,
                                0.53, 0.53, 0.53, 0.53, 0.53, 0.53, 0.53, 0.53, 0.53, 0.53, 1.97, 1.97, 1.97, 1.97,
                                1.97,
                                1.97, 1.97, 1.97, 1.97, 1.97, 1.97, 1.97, 1.97, 1.97, 1.97, 1.97, 1.97, 1.97, 1.97,
                                1.97,
                                1.97, 1.97, 1.97, 1.97, 1.97, 1.97, 1.97, 1.97, 1.97, 1.97, 3.5, 3.5, 3.5, 3.5, 3.5,
                                3.5,
                                3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5,
                                3.5,
                                3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 5.13, 5.13, 5.13, 5.13, 5.13, 5.13, 5.13, 5.13, 5.13,
                                5.13,
                                5.13, 5.13, 5.13, 5.13, 5.13, 5.13, 5.13, 5.13, 5.13, 5.13, 5.13, 5.13, 5.13, 5.13,
                                5.13,
                                5.13, 5.13, 5.13, 5.13, 5.13, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37,
                                6.37,
                                6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37,
                                6.37,
                                6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37,
                                6.37,
                                6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37,
                                6.37,
                                6.37, 6.37, 6.37, 6.37, 6.37, 4.83, 4.83, 4.83, 4.83, 4.83, 4.83, 4.83, 4.83, 4.83,
                                4.83,
                                4.83, 4.83, 4.83, 4.83, 4.83, 4.83, 4.83, 4.83, 4.83, 4.83, 4.83, 4.83, 4.83, 4.83,
                                4.83,
                                4.83, 4.83, 4.83, 4.83, 4.83, 4.83, 4.83, 4.83, 4.83, 4.83
                            ])


@cache('step')
def zr_outflow():
    """
    Real Name: b'Zr outflow'
    Original Eqn: b'IF THEN ELSE((((Zr reservoir-zr min vol))+Zr inflow-Zr evap)>=zr total dem , zr total dem\\\\ ,Max(0, (((Zr reservoir-zr min vol))+Zr inflow-Zr evap )))'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.if_then_else(
        (((zr_reservoir() - zr_min_vol())) + zr_inflow() - zr_evap()) >= zr_total_dem(),
        zr_total_dem(), np.maximum(0,
                                   (((zr_reservoir() - zr_min_vol())) + zr_inflow() - zr_evap())))


@cache('step')
def zr_reservoir():
    """
    Real Name: b'Zr reservoir'
    Original Eqn: b'INTEG ( Zr inflow-Zr evap-Zr outflow-Zr Spill, 31)'
    Units: b'MCM'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_zr_reservoir()


def zr_vol_ele_curve(x):
    """
    Real Name: b'zr vol ele curve'
    Original Eqn: b'( [(0,307.3)-(239.71,410)],(0,307.3),(0.05,310),(0.5,315),(1.57,320),(3.32,325),(6.18,\\\\ 330),(9.66,335),(14.45,340),(19.84,345),(26.86,350),(34.82,355),(44.66,360),(55.67,\\\\ 365),(68.56,370),(82.73,375),(99.18,380),(116.91,385),(137.3,390),(159.18,395),(183.91\\\\ ,400),(239.71,410))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, [
        0, 0.05, 0.5, 1.57, 3.32, 6.18, 9.66, 14.45, 19.84, 26.86, 34.82, 44.66, 55.67, 68.56,
        82.73, 99.18, 116.91, 137.3, 159.18, 183.91, 239.71
    ], [
                                307.3, 310, 315, 320, 325, 330, 335, 340, 345, 350, 355, 360, 365, 370, 375, 380, 385,
                                390,
                                395, 400, 410
                            ])


@cache('step')
def wr_def_aftr_zr_dam():
    """
    Real Name: b'wr def aftr Zr Dam'
    Original Eqn: b'Wr Dem aftr Zr Dam-Wr sup aftr Zr Dam'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return wr_dem_aftr_zr_dam() - wr_sup_aftr_zr_dam()


def zr_wr_dem(x):
    """
    Real Name: b'Zr wr dem'
    Original Eqn: b'( [(1,0)-(365,0.04)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,\\\\ 0),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23\\\\ ,0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35\\\\ ,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47\\\\ ,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94,0),(95\\\\ ,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105,0),(106\\\\ ,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0),(116,0)\\\\ ,(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126,0),(127\\\\ ,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0),(137,0)\\\\ ,(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147,0),(148\\\\ ,0),(149,0),(150,0),(151,0),(152,0),(153,0),(154,0),(155,0),(156,0),(157,0),(158,0)\\\\ ,(159,0),(160,0),(161,0),(162,0),(163,0),(164,0),(165,0),(166,0),(167,0),(168,0),(169\\\\ ,0),(170,0),(171,0),(172,0),(173,0),(174,0),(175,0),(176,0),(177,0),(178,0),(179,0)\\\\ ,(180,0),(181,0.02),(182,0.02),(183,0.02),(184,0.02),(185,0.02),(186,0.02),(187,0.02\\\\ ),(188,0.02),(189,0.02),(190,0.02),(191,0.02),(192,0.02),(193,0.02),(194,0.02),(195\\\\ ,0.02),(196,0.02),(197,0.02),(198,0.02),(199,0.02),(200,0.02),(201,0.02),(202,0.02)\\\\ ,(203,0.02),(204,0.02),(205,0.02),(206,0.02),(207,0.02),(208,0.02),(209,0.02),(210,\\\\ 0.02),(211,0.04),(212,0.04),(213,0.04),(214,0.04),(215,0.04),(216,0.04),(217,0.04),\\\\ (218,0.04),(219,0.04),(220,0.04),(221,0.04),(222,0.04),(223,0.04),(224,0.04),(225,0.04\\\\ ),(226,0.04),(227,0.04),(228,0.04),(229,0.04),(230,0.04),(231,0.04),(232,0.04),(233\\\\ ,0.04),(234,0.04),(235,0.04),(236,0.04),(237,0.04),(238,0.04),(239,0.04),(240,0.04)\\\\ ,(241,0.03),(242,0.03),(243,0.03),(244,0.03),(245,0.03),(246,0.03),(247,0.03),(248,\\\\ 0.03),(249,0.03),(250,0.03),(251,0.03),(252,0.03),(253,0.03),(254,0.03),(255,0.03),\\\\ (256,0.03),(257,0.03),(258,0.03),(259,0.03),(260,0.03),(261,0.03),(262,0.03),(263,0.03\\\\ ),(264,0.03),(265,0.03),(266,0.03),(267,0.03),(268,0.03),(269,0.03),(270,0.03),(271\\\\ ,0.04),(272,0.04),(273,0.04),(274,0.04),(275,0.04),(276,0.04),(277,0.04),(278,0.04)\\\\ ,(279,0.04),(280,0.04),(281,0.04),(282,0.04),(283,0.04),(284,0.04),(285,0.04),(286,\\\\ 0.04),(287,0.04),(288,0.04),(289,0.04),(290,0.04),(291,0.04),(292,0.04),(293,0.04),\\\\ (294,0.04),(295,0.04),(296,0.04),(297,0.04),(298,0.04),(299,0.04),(300,0.04),(301,0.03\\\\ ),(302,0.03),(303,0.03),(304,0.03),(305,0.03),(306,0.03),(307,0.03),(308,0.03),(309\\\\ ,0.03),(310,0.03),(311,0.03),(312,0.03),(313,0.03),(314,0.03),(315,0.03),(316,0.03)\\\\ ,(317,0.03),(318,0.03),(319,0.03),(320,0.03),(321,0.03),(322,0.03),(323,0.03),(324,\\\\ 0.03),(325,0.03),(326,0.03),(327,0.03),(328,0.03),(329,0.03),(330,0.03),(331,0.01),\\\\ (332,0.01),(333,0.01),(334,0.01),(335,0.01),(336,0.01),(337,0.01),(338,0.01),(339,0.01\\\\ ),(340,0.01),(341,0.01),(342,0.01),(343,0.01),(344,0.01),(345,0.01),(346,0.01),(347\\\\ ,0.01),(348,0.01),(349,0.01),(350,0.01),(351,0.01),(352,0.01),(353,0.01),(354,0.01)\\\\ ,(355,0.01),(356,0.01),(357,0.01),(358,0.01),(359,0.01),(360,0.01),(361,0.01),(362,\\\\ 0.01),(363,0.01),(364,0.01),(365,0.01))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], [
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02,
                                0.02,
                                0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02,
                                0.02,
                                0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04,
                                0.04,
                                0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04,
                                0.04,
                                0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
                                0.03,
                                0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
                                0.03,
                                0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04,
                                0.04,
                                0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04,
                                0.04,
                                0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
                                0.03,
                                0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
                                0.03,
                                0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,
                                0.01,
                                0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,
                                0.01,
                                0.01, 0.01, 0.01, 0.01, 0.01
                            ])


@cache('step')
def zr_dam_outflow():
    """
    Real Name: b'Zr Dam outflow'
    Original Eqn: b'zr agri sup+zr Env sup+Zr Spill+zr wr sup'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return zr_agri_sup() + zr_env_sup() + zr_spill() + zr_wr_sup()


@cache('step')
def tajan_dam_outflow():
    """
    Real Name: b'Tajan Dam outflow'
    Original Eqn: b'Tj Agri Sup+Tj Env Sup+Tj Spill'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return tj_agri_sup() + tj_env_sup() + tj_spill()


@cache('step')
def tajan_res_mcm():
    """
    Real Name: b'"Tajan Res (MCM)"'
    Original Eqn: b'INTEG ( Tj inflow-Tj Evaporation-Tj Outflow-Tj Spill, 37.9)'
    Units: b'MCM'
    Limits: (None, None)
    Type: component

    b'Tj Inflow-Tj Outflow-Tj Spill-Tj Evaporation'
    """
    return _integ_tajan_res_mcm()


def tatal_inter_tajan_dam2zarem(x):
    """
    Real Name: b'Tatal Inter Tajan Dam2zarem'
    Original Eqn: b'( [(1,0)-(365,2)],(1,0.41978),(2,0.41978),(3,0.41978),(4,0.41978),(5,0.41978),(6,0.41978\\\\ ),(7,0.41978),(8,0.41978),(9,0.41978),(10,0.41978),(11,0.41978),(12,0.41978),(13,0.41978\\\\ ),(14,0.41978),(15,0.41978),(16,0.41978),(17,0.41978),(18,0.41978),(19,0.41978),(20\\\\ ,0.41978),(21,0.41978),(22,0.41978),(23,0.41978),(24,0.41978),(25,0.41978),(26,0.41978\\\\ ),(27,0.41978),(28,0.41978),(29,0.41978),(30,0.41978),(31,0.68134),(32,0.68134),(33\\\\ ,0.68134),(34,0.68134),(35,0.68134),(36,0.68134),(37,0.68134),(38,0.68134),(39,0.68134\\\\ ),(40,0.68134),(41,0.68134),(42,0.68134),(43,0.68134),(44,0.68134),(45,0.68134),(46\\\\ ,0.68134),(47,0.68134),(48,0.68134),(49,0.68134),(50,0.68134),(51,0.68134),(52,0.68134\\\\ ),(53,0.68134),(54,0.68134),(55,0.68134),(56,0.68134),(57,0.68134),(58,0.68134),(59\\\\ ,0.68134),(60,0.68134),(61,0.43987),(62,0.43987),(63,0.43987),(64,0.43987),(65,0.43987\\\\ ),(66,0.43987),(67,0.43987),(68,0.43987),(69,0.43987),(70,0.43987),(71,0.43987),(72\\\\ ,0.43987),(73,0.43987),(74,0.43987),(75,0.43987),(76,0.43987),(77,0.43987),(78,0.43987\\\\ ),(79,0.43987),(80,0.43987),(81,0.43987),(82,0.43987),(83,0.43987),(84,0.43987),(85\\\\ ,0.43987),(86,0.43987),(87,0.43987),(88,0.43987),(89,0.43987),(90,0.43987),(91,0.4058\\\\ ),(92,0.4058),(93,0.4058),(94,0.4058),(95,0.4058),(96,0.4058),(97,0.4058),(98,0.4058\\\\ ),(99,0.4058),(100,0.4058),(101,0.4058),(102,0.4058),(103,0.4058),(104,0.4058),(105\\\\ ,0.4058),(106,0.4058),(107,0.4058),(108,0.4058),(109,0.4058),(110,0.4058),(111,0.4058\\\\ ),(112,0.4058),(113,0.4058),(114,0.4058),(115,0.4058),(116,0.4058),(117,0.4058),(118\\\\ ,0.4058),(119,0.4058),(120,0.4058),(121,0.51498),(122,0.51498),(123,0.51498),(124,0.51498\\\\ ),(125,0.51498),(126,0.51498),(127,0.51498),(128,0.51498),(129,0.51498),(130,0.51498\\\\ ),(131,0.51498),(132,0.51498),(133,0.51498),(134,0.51498),(135,0.51498),(136,0.51498\\\\ ),(137,0.51498),(138,0.51498),(139,0.51498),(140,0.51498),(141,0.51498),(142,0.51498\\\\ ),(143,0.51498),(144,0.51498),(145,0.51498),(146,0.51498),(147,0.51498),(148,0.51498\\\\ ),(149,0.51498),(150,0.51498),(151,0.87034),(152,0.87034),(153,0.87034),(154,0.87034\\\\ ),(155,0.87034),(156,0.87034),(157,0.87034),(158,0.87034),(159,0.87034),(160,0.87034\\\\ ),(161,0.87034),(162,0.87034),(163,0.87034),(164,0.87034),(165,0.87034),(166,0.87034\\\\ ),(167,0.87034),(168,0.87034),(169,0.87034),(170,0.87034),(171,0.87034),(172,0.87034\\\\ ),(173,0.87034),(174,0.87034),(175,0.87034),(176,0.87034),(177,0.87034),(178,0.87034\\\\ ),(179,0.87034),(180,0.87034),(181,1.65382),(182,1.65382),(183,1.65382),(184,1.65382\\\\ ),(185,1.65382),(186,1.65382),(187,1.65382),(188,1.65382),(189,1.65382),(190,1.65382\\\\ ),(191,1.65382),(192,1.65382),(193,1.65382),(194,1.65382),(195,1.65382),(196,1.65382\\\\ ),(197,1.65382),(198,1.65382),(199,1.65382),(200,1.65382),(201,1.65382),(202,1.65382\\\\ ),(203,1.65382),(204,1.65382),(205,1.65382),(206,1.65382),(207,1.65382),(208,1.65382\\\\ ),(209,1.65382),(210,1.65382),(211,0.94696),(212,0.94696),(213,0.94696),(214,0.94696\\\\ ),(215,0.94696),(216,0.94696),(217,0.94696),(218,0.94696),(219,0.94696),(220,0.94696\\\\ ),(221,0.94696),(222,0.94696),(223,0.94696),(224,0.94696),(225,0.94696),(226,0.94696\\\\ ),(227,0.94696),(228,0.94696),(229,0.94696),(230,0.94696),(231,0.94696),(232,0.94696\\\\ ),(233,0.94696),(234,0.94696),(235,0.94696),(236,0.94696),(237,0.94696),(238,0.94696\\\\ ),(239,0.94696),(240,0.94696),(241,0.66318),(242,0.66318),(243,0.66318),(244,0.66318\\\\ ),(245,0.66318),(246,0.66318),(247,0.66318),(248,0.66318),(249,0.66318),(250,0.66318\\\\ ),(251,0.66318),(252,0.66318),(253,0.66318),(254,0.66318),(255,0.66318),(256,0.66318\\\\ ),(257,0.66318),(258,0.66318),(259,0.66318),(260,0.66318),(261,0.66318),(262,0.66318\\\\ ),(263,0.66318),(264,0.66318),(265,0.66318),(266,0.66318),(267,0.66318),(268,0.66318\\\\ ),(269,0.66318),(270,0.66318),(271,0.56752),(272,0.56752),(273,0.56752),(274,0.56752\\\\ ),(275,0.56752),(276,0.56752),(277,0.56752),(278,0.56752),(279,0.56752),(280,0.56752\\\\ ),(281,0.56752),(282,0.56752),(283,0.56752),(284,0.56752),(285,0.56752),(286,0.56752\\\\ ),(287,0.56752),(288,0.56752),(289,0.56752),(290,0.56752),(291,0.56752),(292,0.56752\\\\ ),(293,0.56752),(294,0.56752),(295,0.56752),(296,0.56752),(297,0.56752),(298,0.56752\\\\ ),(299,0.56752),(300,0.56752),(301,0.41015),(302,0.41015),(303,0.41015),(304,0.41015\\\\ ),(305,0.41015),(306,0.41015),(307,0.41015),(308,0.41015),(309,0.41015),(310,0.41015\\\\ ),(311,0.41015),(312,0.41015),(313,0.41015),(314,0.41015),(315,0.41015),(316,0.41015\\\\ ),(317,0.41015),(318,0.41015),(319,0.41015),(320,0.41015),(321,0.41015),(322,0.41015\\\\ ),(323,0.41015),(324,0.41015),(325,0.41015),(326,0.41015),(327,0.41015),(328,0.41015\\\\ ),(329,0.41015),(330,0.41015),(331,0.38256),(332,0.38256),(333,0.38256),(334,0.38256\\\\ ),(335,0.38256),(336,0.38256),(337,0.38256),(338,0.38256),(339,0.38256),(340,0.38256\\\\ ),(341,0.38256),(342,0.38256),(343,0.38256),(344,0.38256),(345,0.38256),(346,0.38256\\\\ ),(347,0.38256),(348,0.38256),(349,0.38256),(350,0.38256),(351,0.38256),(352,0.38256\\\\ ),(353,0.38256),(354,0.38256),(355,0.38256),(356,0.38256),(357,0.38256),(358,0.38256\\\\ ),(359,0.38256),(360,0.38256),(361,0.38256),(362,0.38256),(363,0.38256),(364,0.38256\\\\ ),(365,0.38256))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], [
                                0.41978, 0.41978, 0.41978, 0.41978, 0.41978, 0.41978, 0.41978, 0.41978, 0.41978,
                                0.41978,
                                0.41978, 0.41978, 0.41978, 0.41978, 0.41978, 0.41978, 0.41978, 0.41978, 0.41978,
                                0.41978,
                                0.41978, 0.41978, 0.41978, 0.41978, 0.41978, 0.41978, 0.41978, 0.41978, 0.41978,
                                0.41978,
                                0.68134, 0.68134, 0.68134, 0.68134, 0.68134, 0.68134, 0.68134, 0.68134, 0.68134,
                                0.68134,
                                0.68134, 0.68134, 0.68134, 0.68134, 0.68134, 0.68134, 0.68134, 0.68134, 0.68134,
                                0.68134,
                                0.68134, 0.68134, 0.68134, 0.68134, 0.68134, 0.68134, 0.68134, 0.68134, 0.68134,
                                0.68134,
                                0.43987, 0.43987, 0.43987, 0.43987, 0.43987, 0.43987, 0.43987, 0.43987, 0.43987,
                                0.43987,
                                0.43987, 0.43987, 0.43987, 0.43987, 0.43987, 0.43987, 0.43987, 0.43987, 0.43987,
                                0.43987,
                                0.43987, 0.43987, 0.43987, 0.43987, 0.43987, 0.43987, 0.43987, 0.43987, 0.43987,
                                0.43987,
                                0.4058, 0.4058, 0.4058, 0.4058, 0.4058, 0.4058, 0.4058, 0.4058, 0.4058, 0.4058, 0.4058,
                                0.4058, 0.4058, 0.4058, 0.4058, 0.4058, 0.4058, 0.4058, 0.4058, 0.4058, 0.4058, 0.4058,
                                0.4058, 0.4058, 0.4058, 0.4058, 0.4058, 0.4058, 0.4058, 0.4058, 0.51498, 0.51498,
                                0.51498,
                                0.51498, 0.51498, 0.51498, 0.51498, 0.51498, 0.51498, 0.51498, 0.51498, 0.51498,
                                0.51498,
                                0.51498, 0.51498, 0.51498, 0.51498, 0.51498, 0.51498, 0.51498, 0.51498, 0.51498,
                                0.51498,
                                0.51498, 0.51498, 0.51498, 0.51498, 0.51498, 0.51498, 0.51498, 0.87034, 0.87034,
                                0.87034,
                                0.87034, 0.87034, 0.87034, 0.87034, 0.87034, 0.87034, 0.87034, 0.87034, 0.87034,
                                0.87034,
                                0.87034, 0.87034, 0.87034, 0.87034, 0.87034, 0.87034, 0.87034, 0.87034, 0.87034,
                                0.87034,
                                0.87034, 0.87034, 0.87034, 0.87034, 0.87034, 0.87034, 0.87034, 1.65382, 1.65382,
                                1.65382,
                                1.65382, 1.65382, 1.65382, 1.65382, 1.65382, 1.65382, 1.65382, 1.65382, 1.65382,
                                1.65382,
                                1.65382, 1.65382, 1.65382, 1.65382, 1.65382, 1.65382, 1.65382, 1.65382, 1.65382,
                                1.65382,
                                1.65382, 1.65382, 1.65382, 1.65382, 1.65382, 1.65382, 1.65382, 0.94696, 0.94696,
                                0.94696,
                                0.94696, 0.94696, 0.94696, 0.94696, 0.94696, 0.94696, 0.94696, 0.94696, 0.94696,
                                0.94696,
                                0.94696, 0.94696, 0.94696, 0.94696, 0.94696, 0.94696, 0.94696, 0.94696, 0.94696,
                                0.94696,
                                0.94696, 0.94696, 0.94696, 0.94696, 0.94696, 0.94696, 0.94696, 0.66318, 0.66318,
                                0.66318,
                                0.66318, 0.66318, 0.66318, 0.66318, 0.66318, 0.66318, 0.66318, 0.66318, 0.66318,
                                0.66318,
                                0.66318, 0.66318, 0.66318, 0.66318, 0.66318, 0.66318, 0.66318, 0.66318, 0.66318,
                                0.66318,
                                0.66318, 0.66318, 0.66318, 0.66318, 0.66318, 0.66318, 0.66318, 0.56752, 0.56752,
                                0.56752,
                                0.56752, 0.56752, 0.56752, 0.56752, 0.56752, 0.56752, 0.56752, 0.56752, 0.56752,
                                0.56752,
                                0.56752, 0.56752, 0.56752, 0.56752, 0.56752, 0.56752, 0.56752, 0.56752, 0.56752,
                                0.56752,
                                0.56752, 0.56752, 0.56752, 0.56752, 0.56752, 0.56752, 0.56752, 0.41015, 0.41015,
                                0.41015,
                                0.41015, 0.41015, 0.41015, 0.41015, 0.41015, 0.41015, 0.41015, 0.41015, 0.41015,
                                0.41015,
                                0.41015, 0.41015, 0.41015, 0.41015, 0.41015, 0.41015, 0.41015, 0.41015, 0.41015,
                                0.41015,
                                0.41015, 0.41015, 0.41015, 0.41015, 0.41015, 0.41015, 0.41015, 0.38256, 0.38256,
                                0.38256,
                                0.38256, 0.38256, 0.38256, 0.38256, 0.38256, 0.38256, 0.38256, 0.38256, 0.38256,
                                0.38256,
                                0.38256, 0.38256, 0.38256, 0.38256, 0.38256, 0.38256, 0.38256, 0.38256, 0.38256,
                                0.38256,
                                0.38256, 0.38256, 0.38256, 0.38256, 0.38256, 0.38256, 0.38256, 0.38256, 0.38256,
                                0.38256,
                                0.38256, 0.38256
                            ])


def tj_volume_area_curve(x):
    """
    Real Name: b'Tj Volume area curve'
    Original Eqn: b'( [(0,0)-(167,4.13)],(3.6,0.4),(3.92,0.419531),(5.29,0.497656),(6.03,0.55),(6.82,0.576674\\\\ ),(8.51,0.657506),(9.86,0.738337),(10.92,0.819169),(12.17,0.9),(13.62,0.964),(15.27\\\\ ,1.028),(17.12,1.092),(19.17,1.156),(21.42,1.22),(23.87,1.284),(25.5,1.3),(26.52,1.372\\\\ ),(29.37,1.468),(32.41,1.564),(35.228,1.66649),(39.1,1.756),(42.75,1.852),(46.59,1.948\\\\ ),(50.63,2.044),(54.87,2.14),(59.31,2.236),(63.95,2.332),(68.79,2.428),(71.6,2.5),(\\\\ 73.87,2.528),(79.07,2.64),(84.51,2.752),(90.14,2.864),(95.98,2.976),(102.01,3.088),\\\\ (108.24,3.2),(114.68,3.344),(121.3,3.488),(128.14,3.632),(135.17,3.776),(142.4,3.92\\\\ ),(151.23,4.064),(153.1,4.1),(160.14,4.115),(162.5,4.12),(167,4.13))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b'\\u0645\\u0646\\u062d\\u06cc \\u062d\\u062c\\u0645 \\u0633\\u0637\\u062d \\u0627\\u0631\\u062a\\u0641\\u0627\\u0639'
    """
    return functions.lookup(x, [
        3.6, 3.92, 5.29, 6.03, 6.82, 8.51, 9.86, 10.92, 12.17, 13.62, 15.27, 17.12, 19.17, 21.42,
        23.87, 25.5, 26.52, 29.37, 32.41, 35.228, 39.1, 42.75, 46.59, 50.63, 54.87, 59.31, 63.95,
        68.79, 71.6, 73.87, 79.07, 84.51, 90.14, 95.98, 102.01, 108.24, 114.68, 121.3, 128.14,
        135.17, 142.4, 151.23, 153.1, 160.14, 162.5, 167
    ], [
                                0.4, 0.419531, 0.497656, 0.55, 0.576674, 0.657506, 0.738337, 0.819169, 0.9, 0.964,
                                1.028,
                                1.092, 1.156, 1.22, 1.284, 1.3, 1.372, 1.468, 1.564, 1.66649, 1.756, 1.852, 1.948,
                                2.044,
                                2.14, 2.236, 2.332, 2.428, 2.5, 2.528, 2.64, 2.752, 2.864, 2.976, 3.088, 3.2, 3.344,
                                3.488,
                                3.632, 3.776, 3.92, 4.064, 4.1, 4.115, 4.12, 4.13
                            ])


def tj_env_dem(x):
    """
    Real Name: b'Tj Env Dem'
    Original Eqn: b'( [(1,0)-(365,0.4)],(1,0.04638),(2,0.04638),(3,0.04638),(4,0.04638),(5,0.04638),(6,0.04638\\\\ ),(7,0.04638),(8,0.04638),(9,0.04638),(10,0.04638),(11,0.04638),(12,0.04638),(13,0.04638\\\\ ),(14,0.04638),(15,0.04638),(16,0.04638),(17,0.04638),(18,0.04638),(19,0.04638),(20\\\\ ,0.04638),(21,0.04638),(22,0.04638),(23,0.04638),(24,0.04638),(25,0.04638),(26,0.04638\\\\ ),(27,0.04638),(28,0.04638),(29,0.04638),(30,0.04638),(31,0.04352),(32,0.04352),(33\\\\ ,0.04352),(34,0.04352),(35,0.04352),(36,0.04352),(37,0.04352),(38,0.04352),(39,0.04352\\\\ ),(40,0.04352),(41,0.04352),(42,0.04352),(43,0.04352),(44,0.04352),(45,0.04352),(46\\\\ ,0.04352),(47,0.04352),(48,0.04352),(49,0.04352),(50,0.04352),(51,0.04352),(52,0.04352\\\\ ),(53,0.04352),(54,0.04352),(55,0.04352),(56,0.04352),(57,0.04352),(58,0.04352),(59\\\\ ,0.04352),(60,0.04352),(61,0.04487),(62,0.04487),(63,0.04487),(64,0.04487),(65,0.04487\\\\ ),(66,0.04487),(67,0.04487),(68,0.04487),(69,0.04487),(70,0.04487),(71,0.04487),(72\\\\ ,0.04487),(73,0.04487),(74,0.04487),(75,0.04487),(76,0.04487),(77,0.04487),(78,0.04487\\\\ ),(79,0.04487),(80,0.04487),(81,0.04487),(82,0.04487),(83,0.04487),(84,0.04487),(85\\\\ ,0.04487),(86,0.04487),(87,0.04487),(88,0.04487),(89,0.04487),(90,0.04487),(91,0.0458\\\\ ),(92,0.0458),(93,0.0458),(94,0.0458),(95,0.0458),(96,0.0458),(97,0.0458),(98,0.0458\\\\ ),(99,0.0458),(100,0.0458),(101,0.0458),(102,0.0458),(103,0.0458),(104,0.0458),(105\\\\ ,0.0458),(106,0.0458),(107,0.0458),(108,0.0458),(109,0.0458),(110,0.0458),(111,0.0458\\\\ ),(112,0.0458),(113,0.0458),(114,0.0458),(115,0.0458),(116,0.0458),(117,0.0458),(118\\\\ ,0.0458),(119,0.0458),(120,0.0458),(121,0.04956),(122,0.04956),(123,0.04956),(124,0.04956\\\\ ),(125,0.04956),(126,0.04956),(127,0.04956),(128,0.04956),(129,0.04956),(130,0.04956\\\\ ),(131,0.04956),(132,0.04956),(133,0.04956),(134,0.04956),(135,0.04956),(136,0.04956\\\\ ),(137,0.04956),(138,0.04956),(139,0.04956),(140,0.04956),(141,0.04956),(142,0.04956\\\\ ),(143,0.04956),(144,0.04956),(145,0.04956),(146,0.04956),(147,0.04956),(148,0.04956\\\\ ),(149,0.04956),(150,0.04956),(151,0.06719),(152,0.06719),(153,0.06719),(154,0.06719\\\\ ),(155,0.06719),(156,0.06719),(157,0.06719),(158,0.06719),(159,0.06719),(160,0.06719\\\\ ),(161,0.06719),(162,0.06719),(163,0.06719),(164,0.06719),(165,0.06719),(166,0.06719\\\\ ),(167,0.06719),(168,0.06719),(169,0.06719),(170,0.06719),(171,0.06719),(172,0.06719\\\\ ),(173,0.06719),(174,0.06719),(175,0.06719),(176,0.06719),(177,0.06719),(178,0.06719\\\\ ),(179,0.06719),(180,0.06719),(181,0.31762),(182,0.31762),(183,0.31762),(184,0.31762\\\\ ),(185,0.31762),(186,0.31762),(187,0.31762),(188,0.31762),(189,0.31762),(190,0.31762\\\\ ),(191,0.31762),(192,0.31762),(193,0.31762),(194,0.31762),(195,0.31762),(196,0.31762\\\\ ),(197,0.31762),(198,0.31762),(199,0.31762),(200,0.31762),(201,0.31762),(202,0.31762\\\\ ),(203,0.31762),(204,0.31762),(205,0.31762),(206,0.31762),(207,0.31762),(208,0.31762\\\\ ),(209,0.31762),(210,0.31762),(211,0.26985),(212,0.26985),(213,0.26985),(214,0.26985\\\\ ),(215,0.26985),(216,0.26985),(217,0.26985),(218,0.26985),(219,0.26985),(220,0.26985\\\\ ),(221,0.26985),(222,0.26985),(223,0.26985),(224,0.26985),(225,0.26985),(226,0.26985\\\\ ),(227,0.26985),(228,0.26985),(229,0.26985),(230,0.26985),(231,0.26985),(232,0.26985\\\\ ),(233,0.26985),(234,0.26985),(235,0.26985),(236,0.26985),(237,0.26985),(238,0.26985\\\\ ),(239,0.26985),(240,0.26985),(241,0.23489),(242,0.23489),(243,0.23489),(244,0.23489\\\\ ),(245,0.23489),(246,0.23489),(247,0.23489),(248,0.23489),(249,0.23489),(250,0.23489\\\\ ),(251,0.23489),(252,0.23489),(253,0.23489),(254,0.23489),(255,0.23489),(256,0.23489\\\\ ),(257,0.23489),(258,0.23489),(259,0.23489),(260,0.23489),(261,0.23489),(262,0.23489\\\\ ),(263,0.23489),(264,0.23489),(265,0.23489),(266,0.23489),(267,0.23489),(268,0.23489\\\\ ),(269,0.23489),(270,0.23489),(271,0.23456),(272,0.23456),(273,0.23456),(274,0.23456\\\\ ),(275,0.23456),(276,0.23456),(277,0.23456),(278,0.23456),(279,0.23456),(280,0.23456\\\\ ),(281,0.23456),(282,0.23456),(283,0.23456),(284,0.23456),(285,0.23456),(286,0.23456\\\\ ),(287,0.23456),(288,0.23456),(289,0.23456),(290,0.23456),(291,0.23456),(292,0.23456\\\\ ),(293,0.23456),(294,0.23456),(295,0.23456),(296,0.23456),(297,0.23456),(298,0.23456\\\\ ),(299,0.23456),(300,0.23456),(301,0.19464),(302,0.19464),(303,0.19464),(304,0.19464\\\\ ),(305,0.19464),(306,0.19464),(307,0.19464),(308,0.19464),(309,0.19464),(310,0.19464\\\\ ),(311,0.19464),(312,0.19464),(313,0.19464),(314,0.19464),(315,0.19464),(316,0.19464\\\\ ),(317,0.19464),(318,0.19464),(319,0.19464),(320,0.19464),(321,0.19464),(322,0.19464\\\\ ),(323,0.19464),(324,0.19464),(325,0.19464),(326,0.19464),(327,0.19464),(328,0.19464\\\\ ),(329,0.19464),(330,0.19464),(331,0.00153),(332,0.00153),(333,0.00153),(334,0.00153\\\\ ),(335,0.00153),(336,0.00153),(337,0.00153),(338,0.00153),(339,0.00153),(340,0.00153\\\\ ),(341,0.00153),(342,0.00153),(343,0.00153),(344,0.00153),(345,0.00153),(346,0.00153\\\\ ),(347,0.00153),(348,0.00153),(349,0.00153),(350,0.00153),(351,0.00153),(352,0.00153\\\\ ),(353,0.00153),(354,0.00153),(355,0.00153),(356,0.00153),(357,0.00153),(358,0.00153\\\\ ),(359,0.00153),(360,0.00153),(361,0.00153),(362,0.00153),(363,0.00153),(364,0.00153\\\\ ),(365,0.00153))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], [
                                0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
                                0.04638,
                                0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
                                0.04638,
                                0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
                                0.04638,
                                0.04352, 0.04352, 0.04352, 0.04352, 0.04352, 0.04352, 0.04352, 0.04352, 0.04352,
                                0.04352,
                                0.04352, 0.04352, 0.04352, 0.04352, 0.04352, 0.04352, 0.04352, 0.04352, 0.04352,
                                0.04352,
                                0.04352, 0.04352, 0.04352, 0.04352, 0.04352, 0.04352, 0.04352, 0.04352, 0.04352,
                                0.04352,
                                0.04487, 0.04487, 0.04487, 0.04487, 0.04487, 0.04487, 0.04487, 0.04487, 0.04487,
                                0.04487,
                                0.04487, 0.04487, 0.04487, 0.04487, 0.04487, 0.04487, 0.04487, 0.04487, 0.04487,
                                0.04487,
                                0.04487, 0.04487, 0.04487, 0.04487, 0.04487, 0.04487, 0.04487, 0.04487, 0.04487,
                                0.04487,
                                0.0458, 0.0458, 0.0458, 0.0458, 0.0458, 0.0458, 0.0458, 0.0458, 0.0458, 0.0458, 0.0458,
                                0.0458, 0.0458, 0.0458, 0.0458, 0.0458, 0.0458, 0.0458, 0.0458, 0.0458, 0.0458, 0.0458,
                                0.0458, 0.0458, 0.0458, 0.0458, 0.0458, 0.0458, 0.0458, 0.0458, 0.04956, 0.04956,
                                0.04956,
                                0.04956, 0.04956, 0.04956, 0.04956, 0.04956, 0.04956, 0.04956, 0.04956, 0.04956,
                                0.04956,
                                0.04956, 0.04956, 0.04956, 0.04956, 0.04956, 0.04956, 0.04956, 0.04956, 0.04956,
                                0.04956,
                                0.04956, 0.04956, 0.04956, 0.04956, 0.04956, 0.04956, 0.04956, 0.06719, 0.06719,
                                0.06719,
                                0.06719, 0.06719, 0.06719, 0.06719, 0.06719, 0.06719, 0.06719, 0.06719, 0.06719,
                                0.06719,
                                0.06719, 0.06719, 0.06719, 0.06719, 0.06719, 0.06719, 0.06719, 0.06719, 0.06719,
                                0.06719,
                                0.06719, 0.06719, 0.06719, 0.06719, 0.06719, 0.06719, 0.06719, 0.31762, 0.31762,
                                0.31762,
                                0.31762, 0.31762, 0.31762, 0.31762, 0.31762, 0.31762, 0.31762, 0.31762, 0.31762,
                                0.31762,
                                0.31762, 0.31762, 0.31762, 0.31762, 0.31762, 0.31762, 0.31762, 0.31762, 0.31762,
                                0.31762,
                                0.31762, 0.31762, 0.31762, 0.31762, 0.31762, 0.31762, 0.31762, 0.26985, 0.26985,
                                0.26985,
                                0.26985, 0.26985, 0.26985, 0.26985, 0.26985, 0.26985, 0.26985, 0.26985, 0.26985,
                                0.26985,
                                0.26985, 0.26985, 0.26985, 0.26985, 0.26985, 0.26985, 0.26985, 0.26985, 0.26985,
                                0.26985,
                                0.26985, 0.26985, 0.26985, 0.26985, 0.26985, 0.26985, 0.26985, 0.23489, 0.23489,
                                0.23489,
                                0.23489, 0.23489, 0.23489, 0.23489, 0.23489, 0.23489, 0.23489, 0.23489, 0.23489,
                                0.23489,
                                0.23489, 0.23489, 0.23489, 0.23489, 0.23489, 0.23489, 0.23489, 0.23489, 0.23489,
                                0.23489,
                                0.23489, 0.23489, 0.23489, 0.23489, 0.23489, 0.23489, 0.23489, 0.23456, 0.23456,
                                0.23456,
                                0.23456, 0.23456, 0.23456, 0.23456, 0.23456, 0.23456, 0.23456, 0.23456, 0.23456,
                                0.23456,
                                0.23456, 0.23456, 0.23456, 0.23456, 0.23456, 0.23456, 0.23456, 0.23456, 0.23456,
                                0.23456,
                                0.23456, 0.23456, 0.23456, 0.23456, 0.23456, 0.23456, 0.23456, 0.19464, 0.19464,
                                0.19464,
                                0.19464, 0.19464, 0.19464, 0.19464, 0.19464, 0.19464, 0.19464, 0.19464, 0.19464,
                                0.19464,
                                0.19464, 0.19464, 0.19464, 0.19464, 0.19464, 0.19464, 0.19464, 0.19464, 0.19464,
                                0.19464,
                                0.19464, 0.19464, 0.19464, 0.19464, 0.19464, 0.19464, 0.19464, 0.00153, 0.00153,
                                0.00153,
                                0.00153, 0.00153, 0.00153, 0.00153, 0.00153, 0.00153, 0.00153, 0.00153, 0.00153,
                                0.00153,
                                0.00153, 0.00153, 0.00153, 0.00153, 0.00153, 0.00153, 0.00153, 0.00153, 0.00153,
                                0.00153,
                                0.00153, 0.00153, 0.00153, 0.00153, 0.00153, 0.00153, 0.00153, 0.00153, 0.00153,
                                0.00153,
                                0.00153, 0.00153
                            ])


@cache('step')
def tj_outflow():
    """
    Real Name: b'Tj Outflow'
    Original Eqn: b'IF THEN ELSE("Tajan Res (MCM)"-Tj Min Volume+Tj inflow-Tj Evaporation>=Tj Total Demand\\\\ , Tj Total Demand, Max(0, "Tajan Res (MCM)"- Tj Min Volume+Tj inflow-Tj Evaporation ) )'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.if_then_else(
        tajan_res_mcm() - tj_min_volume() + tj_inflow() - tj_evaporation() >= tj_total_demand(),
        tj_total_demand(),
        np.maximum(0,
                   tajan_res_mcm() - tj_min_volume() + tj_inflow() - tj_evaporation()))


def tj_ind_dem(x):
    """
    Real Name: b'Tj Ind Dem'
    Original Eqn: b'( [(1,0.04)-(365,0.05)],(1,0.04638),(2,0.04638),(3,0.04638),(4,0.04638),(5,0.04638),(6\\\\ ,0.04638),(7,0.04638),(8,0.04638),(9,0.04638),(10,0.04638),(11,0.04638),(12,0.04638\\\\ ),(13,0.04638),(14,0.04638),(15,0.04638),(16,0.04638),(17,0.04638),(18,0.04638),(19\\\\ ,0.04638),(20,0.04638),(21,0.04638),(22,0.04638),(23,0.04638),(24,0.04638),(25,0.04638\\\\ ),(26,0.04638),(27,0.04638),(28,0.04638),(29,0.04638),(30,0.04638),(31,0.04638),(32\\\\ ,0.04638),(33,0.04638),(34,0.04638),(35,0.04638),(36,0.04638),(37,0.04638),(38,0.04638\\\\ ),(39,0.04638),(40,0.04638),(41,0.04638),(42,0.04638),(43,0.04638),(44,0.04638),(45\\\\ ,0.04638),(46,0.04638),(47,0.04638),(48,0.04638),(49,0.04638),(50,0.04638),(51,0.04638\\\\ ),(52,0.04638),(53,0.04638),(54,0.04638),(55,0.04638),(56,0.04638),(57,0.04638),(58\\\\ ,0.04638),(59,0.04638),(60,0.04638),(61,0.04638),(62,0.04638),(63,0.04638),(64,0.04638\\\\ ),(65,0.04638),(66,0.04638),(67,0.04638),(68,0.04638),(69,0.04638),(70,0.04638),(71\\\\ ,0.04638),(72,0.04638),(73,0.04638),(74,0.04638),(75,0.04638),(76,0.04638),(77,0.04638\\\\ ),(78,0.04638),(79,0.04638),(80,0.04638),(81,0.04638),(82,0.04638),(83,0.04638),(84\\\\ ,0.04638),(85,0.04638),(86,0.04638),(87,0.04638),(88,0.04638),(89,0.04638),(90,0.04638\\\\ ),(91,0.04638),(92,0.04638),(93,0.04638),(94,0.04638),(95,0.04638),(96,0.04638),(97\\\\ ,0.04638),(98,0.04638),(99,0.04638),(100,0.04638),(101,0.04638),(102,0.04638),(103,\\\\ 0.04638),(104,0.04638),(105,0.04638),(106,0.04638),(107,0.04638),(108,0.04638),(109\\\\ ,0.04638),(110,0.04638),(111,0.04638),(112,0.04638),(113,0.04638),(114,0.04638),(115\\\\ ,0.04638),(116,0.04638),(117,0.04638),(118,0.04638),(119,0.04638),(120,0.04638),(121\\\\ ,0.04638),(122,0.04638),(123,0.04638),(124,0.04638),(125,0.04638),(126,0.04638),(127\\\\ ,0.04638),(128,0.04638),(129,0.04638),(130,0.04638),(131,0.04638),(132,0.04638),(133\\\\ ,0.04638),(134,0.04638),(135,0.04638),(136,0.04638),(137,0.04638),(138,0.04638),(139\\\\ ,0.04638),(140,0.04638),(141,0.04638),(142,0.04638),(143,0.04638),(144,0.04638),(145\\\\ ,0.04638),(146,0.04638),(147,0.04638),(148,0.04638),(149,0.04638),(150,0.04638),(151\\\\ ,0.04638),(152,0.04638),(153,0.04638),(154,0.04638),(155,0.04638),(156,0.04638),(157\\\\ ,0.04638),(158,0.04638),(159,0.04638),(160,0.04638),(161,0.04638),(162,0.04638),(163\\\\ ,0.04638),(164,0.04638),(165,0.04638),(166,0.04638),(167,0.04638),(168,0.04638),(169\\\\ ,0.04638),(170,0.04638),(171,0.04638),(172,0.04638),(173,0.04638),(174,0.04638),(175\\\\ ,0.04638),(176,0.04638),(177,0.04638),(178,0.04638),(179,0.04638),(180,0.04638),(181\\\\ ,0.04638),(182,0.04638),(183,0.04638),(184,0.04638),(185,0.04638),(186,0.04638),(187\\\\ ,0.04638),(188,0.04638),(189,0.04638),(190,0.04638),(191,0.04638),(192,0.04638),(193\\\\ ,0.04638),(194,0.04638),(195,0.04638),(196,0.04638),(197,0.04638),(198,0.04638),(199\\\\ ,0.04638),(200,0.04638),(201,0.04638),(202,0.04638),(203,0.04638),(204,0.04638),(205\\\\ ,0.04638),(206,0.04638),(207,0.04638),(208,0.04638),(209,0.04638),(210,0.04638),(211\\\\ ,0.04638),(212,0.04638),(213,0.04638),(214,0.04638),(215,0.04638),(216,0.04638),(217\\\\ ,0.04638),(218,0.04638),(219,0.04638),(220,0.04638),(221,0.04638),(222,0.04638),(223\\\\ ,0.04638),(224,0.04638),(225,0.04638),(226,0.04638),(227,0.04638),(228,0.04638),(229\\\\ ,0.04638),(230,0.04638),(231,0.04638),(232,0.04638),(233,0.04638),(234,0.04638),(235\\\\ ,0.04638),(236,0.04638),(237,0.04638),(238,0.04638),(239,0.04638),(240,0.04638),(241\\\\ ,0.04638),(242,0.04638),(243,0.04638),(244,0.04638),(245,0.04638),(246,0.04638),(247\\\\ ,0.04638),(248,0.04638),(249,0.04638),(250,0.04638),(251,0.04638),(252,0.04638),(253\\\\ ,0.04638),(254,0.04638),(255,0.04638),(256,0.04638),(257,0.04638),(258,0.04638),(259\\\\ ,0.04638),(260,0.04638),(261,0.04638),(262,0.04638),(263,0.04638),(264,0.04638),(265\\\\ ,0.04638),(266,0.04638),(267,0.04638),(268,0.04638),(269,0.04638),(270,0.04638),(271\\\\ ,0.04638),(272,0.04638),(273,0.04638),(274,0.04638),(275,0.04638),(276,0.04638),(277\\\\ ,0.04638),(278,0.04638),(279,0.04638),(280,0.04638),(281,0.04638),(282,0.04638),(283\\\\ ,0.04638),(284,0.04638),(285,0.04638),(286,0.04638),(287,0.04638),(288,0.04638),(289\\\\ ,0.04638),(290,0.04638),(291,0.04638),(292,0.04638),(293,0.04638),(294,0.04638),(295\\\\ ,0.04638),(296,0.04638),(297,0.04638),(298,0.04638),(299,0.04638),(300,0.04638),(301\\\\ ,0.04638),(302,0.04638),(303,0.04638),(304,0.04638),(305,0.04638),(306,0.04638),(307\\\\ ,0.04638),(308,0.04638),(309,0.04638),(310,0.04638),(311,0.04638),(312,0.04638),(313\\\\ ,0.04638),(314,0.04638),(315,0.04638),(316,0.04638),(317,0.04638),(318,0.04638),(319\\\\ ,0.04638),(320,0.04638),(321,0.04638),(322,0.04638),(323,0.04638),(324,0.04638),(325\\\\ ,0.04638),(326,0.04638),(327,0.04638),(328,0.04638),(329,0.04638),(330,0.04638),(331\\\\ ,0.04638),(332,0.04638),(333,0.04638),(334,0.04638),(335,0.04638),(336,0.04638),(337\\\\ ,0.04638),(338,0.04638),(339,0.04638),(340,0.04638),(341,0.04638),(342,0.04638),(343\\\\ ,0.04638),(344,0.04638),(345,0.04638),(346,0.04638),(347,0.04638),(348,0.04638),(349\\\\ ,0.04638),(350,0.04638),(351,0.04638),(352,0.04638),(353,0.04638),(354,0.04638),(355\\\\ ,0.04638),(356,0.04638),(357,0.04638),(358,0.04638),(359,0.04638),(360,0.04638),(361\\\\ ,0.04638),(362,0.04638),(363,0.04638),(364,0.04638),(365,0.04638))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], [
                                0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
                                0.04638,
                                0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
                                0.04638,
                                0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
                                0.04638,
                                0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
                                0.04638,
                                0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
                                0.04638,
                                0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
                                0.04638,
                                0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
                                0.04638,
                                0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
                                0.04638,
                                0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
                                0.04638,
                                0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
                                0.04638,
                                0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
                                0.04638,
                                0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
                                0.04638,
                                0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
                                0.04638,
                                0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
                                0.04638,
                                0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
                                0.04638,
                                0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
                                0.04638,
                                0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
                                0.04638,
                                0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
                                0.04638,
                                0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
                                0.04638,
                                0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
                                0.04638,
                                0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
                                0.04638,
                                0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
                                0.04638,
                                0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
                                0.04638,
                                0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
                                0.04638,
                                0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
                                0.04638,
                                0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
                                0.04638,
                                0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
                                0.04638,
                                0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
                                0.04638,
                                0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
                                0.04638,
                                0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
                                0.04638,
                                0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
                                0.04638,
                                0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
                                0.04638,
                                0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
                                0.04638,
                                0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
                                0.04638,
                                0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
                                0.04638,
                                0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
                                0.04638,
                                0.04638, 0.04638, 0.04638, 0.04638, 0.04638
                            ])


@cache('step')
def tj_inflow():
    """
    Real Name: b'Tj inflow'
    Original Eqn: b'Tajan Dam upstream'
    Units: b'MCM/Month'
    Limits: (None, None)
    Type: component

    b''
    """
    return tajan_dam_upstream()


@cache('run')
def tj_max_volume():
    """
    Real Name: b'Tj max Volume'
    Original Eqn: b'162.4'
    Units: b'MCM'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 162.4


@cache('run')
def tj_min_volume():
    """
    Real Name: b'Tj Min Volume'
    Original Eqn: b'17.12'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 17.12


def tj_monthly_evaporation(x):
    """
    Real Name: b'Tj Monthly Evaporation'
    Original Eqn: b'( [(1,0)-(365,5)],(1,0.86667),(2,0.86667),(3,0.86667),(4,0.86667),(5,0.86667),(6,0.86667\\\\ ),(7,0.86667),(8,0.86667),(9,0.86667),(10,0.86667),(11,0.86667),(12,0.86667),(13,0.86667\\\\ ),(14,0.86667),(15,0.86667),(16,0.86667),(17,0.86667),(18,0.86667),(19,0.86667),(20\\\\ ,0.86667),(21,0.86667),(22,0.86667),(23,0.86667),(24,0.86667),(25,0.86667),(26,0.86667\\\\ ),(27,0.86667),(28,0.86667),(29,0.86667),(30,0.86667),(31,1.5),(32,1.5),(33,1.5),(34\\\\ ,1.5),(35,1.5),(36,1.5),(37,1.5),(38,1.5),(39,1.5),(40,1.5),(41,1.5),(42,1.5),(43,1.5\\\\ ),(44,1.5),(45,1.5),(46,1.5),(47,1.5),(48,1.5),(49,1.5),(50,1.5),(51,1.5),(52,1.5),\\\\ (53,1.5),(54,1.5),(55,1.5),(56,1.5),(57,1.5),(58,1.5),(59,1.5),(60,1.5),(61,0.96667\\\\ ),(62,0.96667),(63,0.96667),(64,0.96667),(65,0.96667),(66,0.96667),(67,0.96667),(68\\\\ ,0.96667),(69,0.96667),(70,0.96667),(71,0.96667),(72,0.96667),(73,0.96667),(74,0.96667\\\\ ),(75,0.96667),(76,0.96667),(77,0.96667),(78,0.96667),(79,0.96667),(80,0.96667),(81\\\\ ,0.96667),(82,0.96667),(83,0.96667),(84,0.96667),(85,0.96667),(86,0.96667),(87,0.96667\\\\ ),(88,0.96667),(89,0.96667),(90,0.96667),(91,0.83333),(92,0.83333),(93,0.83333),(94\\\\ ,0.83333),(95,0.83333),(96,0.83333),(97,0.83333),(98,0.83333),(99,0.83333),(100,0.83333\\\\ ),(101,0.83333),(102,0.83333),(103,0.83333),(104,0.83333),(105,0.83333),(106,0.83333\\\\ ),(107,0.83333),(108,0.83333),(109,0.83333),(110,0.83333),(111,0.83333),(112,0.83333\\\\ ),(113,0.83333),(114,0.83333),(115,0.83333),(116,0.83333),(117,0.83333),(118,0.83333\\\\ ),(119,0.83333),(120,0.83333),(121,1.03333),(122,1.03333),(123,1.03333),(124,1.03333\\\\ ),(125,1.03333),(126,1.03333),(127,1.03333),(128,1.03333),(129,1.03333),(130,1.03333\\\\ ),(131,1.03333),(132,1.03333),(133,1.03333),(134,1.03333),(135,1.03333),(136,1.03333\\\\ ),(137,1.03333),(138,1.03333),(139,1.03333),(140,1.03333),(141,1.03333),(142,1.03333\\\\ ),(143,1.03333),(144,1.03333),(145,1.03333),(146,1.03333),(147,1.03333),(148,1.03333\\\\ ),(149,1.03333),(150,1.03333),(151,1.56667),(152,1.56667),(153,1.56667),(154,1.56667\\\\ ),(155,1.56667),(156,1.56667),(157,1.56667),(158,1.56667),(159,1.56667),(160,1.56667\\\\ ),(161,1.56667),(162,1.56667),(163,1.56667),(164,1.56667),(165,1.56667),(166,1.56667\\\\ ),(167,1.56667),(168,1.56667),(169,1.56667),(170,1.56667),(171,1.56667),(172,1.56667\\\\ ),(173,1.56667),(174,1.56667),(175,1.56667),(176,1.56667),(177,1.56667),(178,1.56667\\\\ ),(179,1.56667),(180,1.56667),(181,2.5),(182,2.5),(183,2.5),(184,2.5),(185,2.5),(186\\\\ ,2.5),(187,2.5),(188,2.5),(189,2.5),(190,2.5),(191,2.5),(192,2.5),(193,2.5),(194,2.5\\\\ ),(195,2.5),(196,2.5),(197,2.5),(198,2.5),(199,2.5),(200,2.5),(201,2.5),(202,2.5),(\\\\ 203,2.5),(204,2.5),(205,2.5),(206,2.5),(207,2.5),(208,2.5),(209,2.5),(210,2.5),(211\\\\ ,3.6),(212,3.6),(213,3.6),(214,3.6),(215,3.6),(216,3.6),(217,3.6),(218,3.6),(219,3.6\\\\ ),(220,3.6),(221,3.6),(222,3.6),(223,3.6),(224,3.6),(225,3.6),(226,3.6),(227,3.6),(\\\\ 228,3.6),(229,3.6),(230,3.6),(231,3.6),(232,3.6),(233,3.6),(234,3.6),(235,3.6),(236\\\\ ,3.6),(237,3.6),(238,3.6),(239,3.6),(240,3.6),(241,4.46667),(242,4.46667),(243,4.46667\\\\ ),(244,4.46667),(245,4.46667),(246,4.46667),(247,4.46667),(248,4.46667),(249,4.46667\\\\ ),(250,4.46667),(251,4.46667),(252,4.46667),(253,4.46667),(254,4.46667),(255,4.46667\\\\ ),(256,4.46667),(257,4.46667),(258,4.46667),(259,4.46667),(260,4.46667),(261,4.46667\\\\ ),(262,4.46667),(263,4.46667),(264,4.46667),(265,4.46667),(266,4.46667),(267,4.46667\\\\ ),(268,4.46667),(269,4.46667),(270,4.46667),(271,4.93333),(272,4.93333),(273,4.93333\\\\ ),(274,4.93333),(275,4.93333),(276,4.93333),(277,4.93333),(278,4.93333),(279,4.93333\\\\ ),(280,4.93333),(281,4.93333),(282,4.93333),(283,4.93333),(284,4.93333),(285,4.93333\\\\ ),(286,4.93333),(287,4.93333),(288,4.93333),(289,4.93333),(290,4.93333),(291,4.93333\\\\ ),(292,4.93333),(293,4.93333),(294,4.93333),(295,4.93333),(296,4.93333),(297,4.93333\\\\ ),(298,4.93333),(299,4.93333),(300,4.93333),(301,4.8),(302,4.8),(303,4.8),(304,4.8)\\\\ ,(305,4.8),(306,4.8),(307,4.8),(308,4.8),(309,4.8),(310,4.8),(311,4.8),(312,4.8),(313\\\\ ,4.8),(314,4.8),(315,4.8),(316,4.8),(317,4.8),(318,4.8),(319,4.8),(320,4.8),(321,4.8\\\\ ),(322,4.8),(323,4.8),(324,4.8),(325,4.8),(326,4.8),(327,4.8),(328,4.8),(329,4.8),(\\\\ 330,4.8),(331,3.7),(332,3.7),(333,3.7),(334,3.7),(335,3.7),(336,3.7),(337,3.7),(338\\\\ ,3.7),(339,3.7),(340,3.7),(341,3.7),(342,3.7),(343,3.7),(344,3.7),(345,3.7),(346,3.7\\\\ ),(347,3.7),(348,3.7),(349,3.7),(350,3.7),(351,3.7),(352,3.7),(353,3.7),(354,3.7),(\\\\ 355,3.7),(356,3.7),(357,3.7),(358,3.7),(359,3.7),(360,3.7),(361,3.7),(362,3.7),(363\\\\ ,3.7),(364,3.7),(365,3.7))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], [
                                0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667,
                                0.86667,
                                0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667,
                                0.86667,
                                0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667,
                                0.86667,
                                1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5,
                                1.5,
                                1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 0.96667, 0.96667, 0.96667,
                                0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667,
                                0.96667,
                                0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667,
                                0.96667,
                                0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.83333, 0.83333,
                                0.83333,
                                0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333,
                                0.83333,
                                0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333,
                                0.83333,
                                0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 1.03333, 1.03333,
                                1.03333,
                                1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333,
                                1.03333,
                                1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333,
                                1.03333,
                                1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.56667, 1.56667,
                                1.56667,
                                1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667,
                                1.56667,
                                1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667,
                                1.56667,
                                1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 2.5, 2.5, 2.5, 2.5, 2.5,
                                2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5,
                                2.5,
                                2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6,
                                3.6,
                                3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6,
                                3.6,
                                3.6, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667,
                                4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667,
                                4.46667,
                                4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667,
                                4.46667,
                                4.46667, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333,
                                4.93333,
                                4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333,
                                4.93333,
                                4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333,
                                4.93333,
                                4.93333, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8,
                                4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 3.7, 3.7, 3.7,
                                3.7,
                                3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7,
                                3.7,
                                3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7
                            ])


@cache('step')
def tj_spill():
    """
    Real Name: b'Tj Spill'
    Original Eqn: b'IF THEN ELSE((("Tajan Res (MCM)")+Tj inflow-Tj Outflow-Tj Evaporation)>(Tj max Volume\\\\ ), (("Tajan Res (MCM)" )+Tj inflow-Tj Outflow-Tj Evaporation-(Tj max Volume)), 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.if_then_else(
        ((tajan_res_mcm()) + tj_inflow() - tj_outflow() - tj_evaporation()) > (tj_max_volume()),
        ((tajan_res_mcm()) + tj_inflow() - tj_outflow() - tj_evaporation() - (tj_max_volume())), 0)


@cache('step')
def total_sup():
    """
    Real Name: b'Total Sup'
    Original Eqn: b'Tj Agri Sup+Tj Dom Sup+Tj Env Sup+Tj Ind Sup'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return tj_agri_sup() + tj_dom_sup() + tj_env_sup() + tj_ind_sup()


@cache('step')
def tj_areakm2():
    """
    Real Name: b'"Tj Area(km^2)"'
    Original Eqn: b'Tj Volume area curve("Tajan Res (MCM)")'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return tj_volume_area_curve(tajan_res_mcm())


def tj_dom_dem(x):
    """
    Real Name: b'Tj Dom Dem'
    Original Eqn: b'( [(1,0.08)-(365,0.09)],(1,0.08333),(2,0.08333),(3,0.08333),(4,0.08333),(5,0.08333),(6\\\\ ,0.08333),(7,0.08333),(8,0.08333),(9,0.08333),(10,0.08333),(11,0.08333),(12,0.08333\\\\ ),(13,0.08333),(14,0.08333),(15,0.08333),(16,0.08333),(17,0.08333),(18,0.08333),(19\\\\ ,0.08333),(20,0.08333),(21,0.08333),(22,0.08333),(23,0.08333),(24,0.08333),(25,0.08333\\\\ ),(26,0.08333),(27,0.08333),(28,0.08333),(29,0.08333),(30,0.08333),(31,0.08333),(32\\\\ ,0.08333),(33,0.08333),(34,0.08333),(35,0.08333),(36,0.08333),(37,0.08333),(38,0.08333\\\\ ),(39,0.08333),(40,0.08333),(41,0.08333),(42,0.08333),(43,0.08333),(44,0.08333),(45\\\\ ,0.08333),(46,0.08333),(47,0.08333),(48,0.08333),(49,0.08333),(50,0.08333),(51,0.08333\\\\ ),(52,0.08333),(53,0.08333),(54,0.08333),(55,0.08333),(56,0.08333),(57,0.08333),(58\\\\ ,0.08333),(59,0.08333),(60,0.08333),(61,0.08333),(62,0.08333),(63,0.08333),(64,0.08333\\\\ ),(65,0.08333),(66,0.08333),(67,0.08333),(68,0.08333),(69,0.08333),(70,0.08333),(71\\\\ ,0.08333),(72,0.08333),(73,0.08333),(74,0.08333),(75,0.08333),(76,0.08333),(77,0.08333\\\\ ),(78,0.08333),(79,0.08333),(80,0.08333),(81,0.08333),(82,0.08333),(83,0.08333),(84\\\\ ,0.08333),(85,0.08333),(86,0.08333),(87,0.08333),(88,0.08333),(89,0.08333),(90,0.08333\\\\ ),(91,0.08333),(92,0.08333),(93,0.08333),(94,0.08333),(95,0.08333),(96,0.08333),(97\\\\ ,0.08333),(98,0.08333),(99,0.08333),(100,0.08333),(101,0.08333),(102,0.08333),(103,\\\\ 0.08333),(104,0.08333),(105,0.08333),(106,0.08333),(107,0.08333),(108,0.08333),(109\\\\ ,0.08333),(110,0.08333),(111,0.08333),(112,0.08333),(113,0.08333),(114,0.08333),(115\\\\ ,0.08333),(116,0.08333),(117,0.08333),(118,0.08333),(119,0.08333),(120,0.08333),(121\\\\ ,0.08333),(122,0.08333),(123,0.08333),(124,0.08333),(125,0.08333),(126,0.08333),(127\\\\ ,0.08333),(128,0.08333),(129,0.08333),(130,0.08333),(131,0.08333),(132,0.08333),(133\\\\ ,0.08333),(134,0.08333),(135,0.08333),(136,0.08333),(137,0.08333),(138,0.08333),(139\\\\ ,0.08333),(140,0.08333),(141,0.08333),(142,0.08333),(143,0.08333),(144,0.08333),(145\\\\ ,0.08333),(146,0.08333),(147,0.08333),(148,0.08333),(149,0.08333),(150,0.08333),(151\\\\ ,0.08333),(152,0.08333),(153,0.08333),(154,0.08333),(155,0.08333),(156,0.08333),(157\\\\ ,0.08333),(158,0.08333),(159,0.08333),(160,0.08333),(161,0.08333),(162,0.08333),(163\\\\ ,0.08333),(164,0.08333),(165,0.08333),(166,0.08333),(167,0.08333),(168,0.08333),(169\\\\ ,0.08333),(170,0.08333),(171,0.08333),(172,0.08333),(173,0.08333),(174,0.08333),(175\\\\ ,0.08333),(176,0.08333),(177,0.08333),(178,0.08333),(179,0.08333),(180,0.08333),(181\\\\ ,0.08333),(182,0.08333),(183,0.08333),(184,0.08333),(185,0.08333),(186,0.08333),(187\\\\ ,0.08333),(188,0.08333),(189,0.08333),(190,0.08333),(191,0.08333),(192,0.08333),(193\\\\ ,0.08333),(194,0.08333),(195,0.08333),(196,0.08333),(197,0.08333),(198,0.08333),(199\\\\ ,0.08333),(200,0.08333),(201,0.08333),(202,0.08333),(203,0.08333),(204,0.08333),(205\\\\ ,0.08333),(206,0.08333),(207,0.08333),(208,0.08333),(209,0.08333),(210,0.08333),(211\\\\ ,0.08333),(212,0.08333),(213,0.08333),(214,0.08333),(215,0.08333),(216,0.08333),(217\\\\ ,0.08333),(218,0.08333),(219,0.08333),(220,0.08333),(221,0.08333),(222,0.08333),(223\\\\ ,0.08333),(224,0.08333),(225,0.08333),(226,0.08333),(227,0.08333),(228,0.08333),(229\\\\ ,0.08333),(230,0.08333),(231,0.08333),(232,0.08333),(233,0.08333),(234,0.08333),(235\\\\ ,0.08333),(236,0.08333),(237,0.08333),(238,0.08333),(239,0.08333),(240,0.08333),(241\\\\ ,0.08333),(242,0.08333),(243,0.08333),(244,0.08333),(245,0.08333),(246,0.08333),(247\\\\ ,0.08333),(248,0.08333),(249,0.08333),(250,0.08333),(251,0.08333),(252,0.08333),(253\\\\ ,0.08333),(254,0.08333),(255,0.08333),(256,0.08333),(257,0.08333),(258,0.08333),(259\\\\ ,0.08333),(260,0.08333),(261,0.08333),(262,0.08333),(263,0.08333),(264,0.08333),(265\\\\ ,0.08333),(266,0.08333),(267,0.08333),(268,0.08333),(269,0.08333),(270,0.08333),(271\\\\ ,0.08333),(272,0.08333),(273,0.08333),(274,0.08333),(275,0.08333),(276,0.08333),(277\\\\ ,0.08333),(278,0.08333),(279,0.08333),(280,0.08333),(281,0.08333),(282,0.08333),(283\\\\ ,0.08333),(284,0.08333),(285,0.08333),(286,0.08333),(287,0.08333),(288,0.08333),(289\\\\ ,0.08333),(290,0.08333),(291,0.08333),(292,0.08333),(293,0.08333),(294,0.08333),(295\\\\ ,0.08333),(296,0.08333),(297,0.08333),(298,0.08333),(299,0.08333),(300,0.08333),(301\\\\ ,0.08333),(302,0.08333),(303,0.08333),(304,0.08333),(305,0.08333),(306,0.08333),(307\\\\ ,0.08333),(308,0.08333),(309,0.08333),(310,0.08333),(311,0.08333),(312,0.08333),(313\\\\ ,0.08333),(314,0.08333),(315,0.08333),(316,0.08333),(317,0.08333),(318,0.08333),(319\\\\ ,0.08333),(320,0.08333),(321,0.08333),(322,0.08333),(323,0.08333),(324,0.08333),(325\\\\ ,0.08333),(326,0.08333),(327,0.08333),(328,0.08333),(329,0.08333),(330,0.08333),(331\\\\ ,0.08333),(332,0.08333),(333,0.08333),(334,0.08333),(335,0.08333),(336,0.08333),(337\\\\ ,0.08333),(338,0.08333),(339,0.08333),(340,0.08333),(341,0.08333),(342,0.08333),(343\\\\ ,0.08333),(344,0.08333),(345,0.08333),(346,0.08333),(347,0.08333),(348,0.08333),(349\\\\ ,0.08333),(350,0.08333),(351,0.08333),(352,0.08333),(353,0.08333),(354,0.08333),(355\\\\ ,0.08333),(356,0.08333),(357,0.08333),(358,0.08333),(359,0.08333),(360,0.08333),(361\\\\ ,0.08333),(362,0.08333),(363,0.08333),(364,0.08333),(365,0.08333))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], [
                                0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
                                0.08333,
                                0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
                                0.08333,
                                0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
                                0.08333,
                                0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
                                0.08333,
                                0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
                                0.08333,
                                0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
                                0.08333,
                                0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
                                0.08333,
                                0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
                                0.08333,
                                0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
                                0.08333,
                                0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
                                0.08333,
                                0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
                                0.08333,
                                0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
                                0.08333,
                                0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
                                0.08333,
                                0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
                                0.08333,
                                0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
                                0.08333,
                                0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
                                0.08333,
                                0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
                                0.08333,
                                0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
                                0.08333,
                                0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
                                0.08333,
                                0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
                                0.08333,
                                0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
                                0.08333,
                                0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
                                0.08333,
                                0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
                                0.08333,
                                0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
                                0.08333,
                                0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
                                0.08333,
                                0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
                                0.08333,
                                0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
                                0.08333,
                                0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
                                0.08333,
                                0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
                                0.08333,
                                0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
                                0.08333,
                                0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
                                0.08333,
                                0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
                                0.08333,
                                0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
                                0.08333,
                                0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
                                0.08333,
                                0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
                                0.08333,
                                0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
                                0.08333,
                                0.08333, 0.08333, 0.08333, 0.08333, 0.08333
                            ])


def after_finesk_interflow(x):
    """
    Real Name: b'After Finesk Interflow'
    Original Eqn: b'( [(1,0)-(365,2)],(1,0.19653),(2,0.19653),(3,0.19653),(4,0.19653),(5,0.19653),(6,0.19653\\\\ ),(7,0.19653),(8,0.19653),(9,0.19653),(10,0.19653),(11,0.19653),(12,0.19653),(13,0.19653\\\\ ),(14,0.19653),(15,0.19653),(16,0.19653),(17,0.19653),(18,0.19653),(19,0.19653),(20\\\\ ,0.19653),(21,0.19653),(22,0.19653),(23,0.19653),(24,0.19653),(25,0.19653),(26,0.19653\\\\ ),(27,0.19653),(28,0.19653),(29,0.19653),(30,0.19653),(31,0.30084),(32,0.30084),(33\\\\ ,0.30084),(34,0.30084),(35,0.30084),(36,0.30084),(37,0.30084),(38,0.30084),(39,0.30084\\\\ ),(40,0.30084),(41,0.30084),(42,0.30084),(43,0.30084),(44,0.30084),(45,0.30084),(46\\\\ ,0.30084),(47,0.30084),(48,0.30084),(49,0.30084),(50,0.30084),(51,0.30084),(52,0.30084\\\\ ),(53,0.30084),(54,0.30084),(55,0.30084),(56,0.30084),(57,0.30084),(58,0.30084),(59\\\\ ,0.30084),(60,0.30084),(61,0.25039),(62,0.25039),(63,0.25039),(64,0.25039),(65,0.25039\\\\ ),(66,0.25039),(67,0.25039),(68,0.25039),(69,0.25039),(70,0.25039),(71,0.25039),(72\\\\ ,0.25039),(73,0.25039),(74,0.25039),(75,0.25039),(76,0.25039),(77,0.25039),(78,0.25039\\\\ ),(79,0.25039),(80,0.25039),(81,0.25039),(82,0.25039),(83,0.25039),(84,0.25039),(85\\\\ ,0.25039),(86,0.25039),(87,0.25039),(88,0.25039),(89,0.25039),(90,0.25039),(91,0.18343\\\\ ),(92,0.18343),(93,0.18343),(94,0.18343),(95,0.18343),(96,0.18343),(97,0.18343),(98\\\\ ,0.18343),(99,0.18343),(100,0.18343),(101,0.18343),(102,0.18343),(103,0.18343),(104\\\\ ,0.18343),(105,0.18343),(106,0.18343),(107,0.18343),(108,0.18343),(109,0.18343),(110\\\\ ,0.18343),(111,0.18343),(112,0.18343),(113,0.18343),(114,0.18343),(115,0.18343),(116\\\\ ,0.18343),(117,0.18343),(118,0.18343),(119,0.18343),(120,0.18343),(121,0.21583),(122\\\\ ,0.21583),(123,0.21583),(124,0.21583),(125,0.21583),(126,0.21583),(127,0.21583),(128\\\\ ,0.21583),(129,0.21583),(130,0.21583),(131,0.21583),(132,0.21583),(133,0.21583),(134\\\\ ,0.21583),(135,0.21583),(136,0.21583),(137,0.21583),(138,0.21583),(139,0.21583),(140\\\\ ,0.21583),(141,0.21583),(142,0.21583),(143,0.21583),(144,0.21583),(145,0.21583),(146\\\\ ,0.21583),(147,0.21583),(148,0.21583),(149,0.21583),(150,0.21583),(151,0.62171),(152\\\\ ,0.62171),(153,0.62171),(154,0.62171),(155,0.62171),(156,0.62171),(157,0.62171),(158\\\\ ,0.62171),(159,0.62171),(160,0.62171),(161,0.62171),(162,0.62171),(163,0.62171),(164\\\\ ,0.62171),(165,0.62171),(166,0.62171),(167,0.62171),(168,0.62171),(169,0.62171),(170\\\\ ,0.62171),(171,0.62171),(172,0.62171),(173,0.62171),(174,0.62171),(175,0.62171),(176\\\\ ,0.62171),(177,0.62171),(178,0.62171),(179,0.62171),(180,0.62171),(181,1.10257),(182\\\\ ,1.10257),(183,1.10257),(184,1.10257),(185,1.10257),(186,1.10257),(187,1.10257),(188\\\\ ,1.10257),(189,1.10257),(190,1.10257),(191,1.10257),(192,1.10257),(193,1.10257),(194\\\\ ,1.10257),(195,1.10257),(196,1.10257),(197,1.10257),(198,1.10257),(199,1.10257),(200\\\\ ,1.10257),(201,1.10257),(202,1.10257),(203,1.10257),(204,1.10257),(205,1.10257),(206\\\\ ,1.10257),(207,1.10257),(208,1.10257),(209,1.10257),(210,1.10257),(211,0.55757),(212\\\\ ,0.55757),(213,0.55757),(214,0.55757),(215,0.55757),(216,0.55757),(217,0.55757),(218\\\\ ,0.55757),(219,0.55757),(220,0.55757),(221,0.55757),(222,0.55757),(223,0.55757),(224\\\\ ,0.55757),(225,0.55757),(226,0.55757),(227,0.55757),(228,0.55757),(229,0.55757),(230\\\\ ,0.55757),(231,0.55757),(232,0.55757),(233,0.55757),(234,0.55757),(235,0.55757),(236\\\\ ,0.55757),(237,0.55757),(238,0.55757),(239,0.55757),(240,0.55757),(241,0.29591),(242\\\\ ,0.29591),(243,0.29591),(244,0.29591),(245,0.29591),(246,0.29591),(247,0.29591),(248\\\\ ,0.29591),(249,0.29591),(250,0.29591),(251,0.29591),(252,0.29591),(253,0.29591),(254\\\\ ,0.29591),(255,0.29591),(256,0.29591),(257,0.29591),(258,0.29591),(259,0.29591),(260\\\\ ,0.29591),(261,0.29591),(262,0.29591),(263,0.29591),(264,0.29591),(265,0.29591),(266\\\\ ,0.29591),(267,0.29591),(268,0.29591),(269,0.29591),(270,0.29591),(271,0.29107),(272\\\\ ,0.29107),(273,0.29107),(274,0.29107),(275,0.29107),(276,0.29107),(277,0.29107),(278\\\\ ,0.29107),(279,0.29107),(280,0.29107),(281,0.29107),(282,0.29107),(283,0.29107),(284\\\\ ,0.29107),(285,0.29107),(286,0.29107),(287,0.29107),(288,0.29107),(289,0.29107),(290\\\\ ,0.29107),(291,0.29107),(292,0.29107),(293,0.29107),(294,0.29107),(295,0.29107),(296\\\\ ,0.29107),(297,0.29107),(298,0.29107),(299,0.29107),(300,0.29107),(301,0.12915),(302\\\\ ,0.12915),(303,0.12915),(304,0.12915),(305,0.12915),(306,0.12915),(307,0.12915),(308\\\\ ,0.12915),(309,0.12915),(310,0.12915),(311,0.12915),(312,0.12915),(313,0.12915),(314\\\\ ,0.12915),(315,0.12915),(316,0.12915),(317,0.12915),(318,0.12915),(319,0.12915),(320\\\\ ,0.12915),(321,0.12915),(322,0.12915),(323,0.12915),(324,0.12915),(325,0.12915),(326\\\\ ,0.12915),(327,0.12915),(328,0.12915),(329,0.12915),(330,0.12915),(331,0.30265),(332\\\\ ,0.30265),(333,0.30265),(334,0.30265),(335,0.30265),(336,0.30265),(337,0.30265),(338\\\\ ,0.30265),(339,0.30265),(340,0.30265),(341,0.30265),(342,0.30265),(343,0.30265),(344\\\\ ,0.30265),(345,0.30265),(346,0.30265),(347,0.30265),(348,0.30265),(349,0.30265),(350\\\\ ,0.30265),(351,0.30265),(352,0.30265),(353,0.30265),(354,0.30265),(355,0.30265),(356\\\\ ,0.30265),(357,0.30265),(358,0.30265),(359,0.30265),(360,0.30265),(361,0.30265),(362\\\\ ,0.30265),(363,0.30265),(364,0.30265),(365,0.30265))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], [
                                0.19653, 0.19653, 0.19653, 0.19653, 0.19653, 0.19653, 0.19653, 0.19653, 0.19653,
                                0.19653,
                                0.19653, 0.19653, 0.19653, 0.19653, 0.19653, 0.19653, 0.19653, 0.19653, 0.19653,
                                0.19653,
                                0.19653, 0.19653, 0.19653, 0.19653, 0.19653, 0.19653, 0.19653, 0.19653, 0.19653,
                                0.19653,
                                0.30084, 0.30084, 0.30084, 0.30084, 0.30084, 0.30084, 0.30084, 0.30084, 0.30084,
                                0.30084,
                                0.30084, 0.30084, 0.30084, 0.30084, 0.30084, 0.30084, 0.30084, 0.30084, 0.30084,
                                0.30084,
                                0.30084, 0.30084, 0.30084, 0.30084, 0.30084, 0.30084, 0.30084, 0.30084, 0.30084,
                                0.30084,
                                0.25039, 0.25039, 0.25039, 0.25039, 0.25039, 0.25039, 0.25039, 0.25039, 0.25039,
                                0.25039,
                                0.25039, 0.25039, 0.25039, 0.25039, 0.25039, 0.25039, 0.25039, 0.25039, 0.25039,
                                0.25039,
                                0.25039, 0.25039, 0.25039, 0.25039, 0.25039, 0.25039, 0.25039, 0.25039, 0.25039,
                                0.25039,
                                0.18343, 0.18343, 0.18343, 0.18343, 0.18343, 0.18343, 0.18343, 0.18343, 0.18343,
                                0.18343,
                                0.18343, 0.18343, 0.18343, 0.18343, 0.18343, 0.18343, 0.18343, 0.18343, 0.18343,
                                0.18343,
                                0.18343, 0.18343, 0.18343, 0.18343, 0.18343, 0.18343, 0.18343, 0.18343, 0.18343,
                                0.18343,
                                0.21583, 0.21583, 0.21583, 0.21583, 0.21583, 0.21583, 0.21583, 0.21583, 0.21583,
                                0.21583,
                                0.21583, 0.21583, 0.21583, 0.21583, 0.21583, 0.21583, 0.21583, 0.21583, 0.21583,
                                0.21583,
                                0.21583, 0.21583, 0.21583, 0.21583, 0.21583, 0.21583, 0.21583, 0.21583, 0.21583,
                                0.21583,
                                0.62171, 0.62171, 0.62171, 0.62171, 0.62171, 0.62171, 0.62171, 0.62171, 0.62171,
                                0.62171,
                                0.62171, 0.62171, 0.62171, 0.62171, 0.62171, 0.62171, 0.62171, 0.62171, 0.62171,
                                0.62171,
                                0.62171, 0.62171, 0.62171, 0.62171, 0.62171, 0.62171, 0.62171, 0.62171, 0.62171,
                                0.62171,
                                1.10257, 1.10257, 1.10257, 1.10257, 1.10257, 1.10257, 1.10257, 1.10257, 1.10257,
                                1.10257,
                                1.10257, 1.10257, 1.10257, 1.10257, 1.10257, 1.10257, 1.10257, 1.10257, 1.10257,
                                1.10257,
                                1.10257, 1.10257, 1.10257, 1.10257, 1.10257, 1.10257, 1.10257, 1.10257, 1.10257,
                                1.10257,
                                0.55757, 0.55757, 0.55757, 0.55757, 0.55757, 0.55757, 0.55757, 0.55757, 0.55757,
                                0.55757,
                                0.55757, 0.55757, 0.55757, 0.55757, 0.55757, 0.55757, 0.55757, 0.55757, 0.55757,
                                0.55757,
                                0.55757, 0.55757, 0.55757, 0.55757, 0.55757, 0.55757, 0.55757, 0.55757, 0.55757,
                                0.55757,
                                0.29591, 0.29591, 0.29591, 0.29591, 0.29591, 0.29591, 0.29591, 0.29591, 0.29591,
                                0.29591,
                                0.29591, 0.29591, 0.29591, 0.29591, 0.29591, 0.29591, 0.29591, 0.29591, 0.29591,
                                0.29591,
                                0.29591, 0.29591, 0.29591, 0.29591, 0.29591, 0.29591, 0.29591, 0.29591, 0.29591,
                                0.29591,
                                0.29107, 0.29107, 0.29107, 0.29107, 0.29107, 0.29107, 0.29107, 0.29107, 0.29107,
                                0.29107,
                                0.29107, 0.29107, 0.29107, 0.29107, 0.29107, 0.29107, 0.29107, 0.29107, 0.29107,
                                0.29107,
                                0.29107, 0.29107, 0.29107, 0.29107, 0.29107, 0.29107, 0.29107, 0.29107, 0.29107,
                                0.29107,
                                0.12915, 0.12915, 0.12915, 0.12915, 0.12915, 0.12915, 0.12915, 0.12915, 0.12915,
                                0.12915,
                                0.12915, 0.12915, 0.12915, 0.12915, 0.12915, 0.12915, 0.12915, 0.12915, 0.12915,
                                0.12915,
                                0.12915, 0.12915, 0.12915, 0.12915, 0.12915, 0.12915, 0.12915, 0.12915, 0.12915,
                                0.12915,
                                0.30265, 0.30265, 0.30265, 0.30265, 0.30265, 0.30265, 0.30265, 0.30265, 0.30265,
                                0.30265,
                                0.30265, 0.30265, 0.30265, 0.30265, 0.30265, 0.30265, 0.30265, 0.30265, 0.30265,
                                0.30265,
                                0.30265, 0.30265, 0.30265, 0.30265, 0.30265, 0.30265, 0.30265, 0.30265, 0.30265,
                                0.30265,
                                0.30265, 0.30265, 0.30265, 0.30265, 0.30265
                            ])


def domes1_demad_finesk(x):
    """
    Real Name: b'"Domes-1 Demad finesk"'
    Original Eqn: b'( [(1,0.6)-(12,0.9)],(1,0.6),(2,0.6),(3,0.6),(4,0.6),(5,0.6),(6,0.6),(7,0.85),(8,0.85)\\\\ ,(9,0.85),(10,0.85),(11,0.85),(11,0.85))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11],
                            [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85])


def envi_demand_finesk(x):
    """
    Real Name: b'envi Demand Finesk'
    Original Eqn: b'( [(1,0)-(12,2)],(1,0.14),(2,0.13),(3,0.12),(4,0.13),(5,0.14),(6,0.18),(7,1.06),(8,1.23\\\\ ),(9,1.25),(10,1.5),(11,1.36),(12,0.83))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(
        x, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        [0.14, 0.13, 0.12, 0.13, 0.14, 0.18, 1.06, 1.23, 1.25, 1.5, 1.36, 0.83])


@cache('run')
def finesk_0():
    """
    Real Name: b'Finesk 0'
    Original Eqn: b'1'
    Units: b'MCM'
    Limits: (None, None)
    Type: constant

    b'I dont know yet'
    """
    return 1


@cache('step')
def finesk_dam():
    """
    Real Name: b'Finesk Dam'
    Original Eqn: b'INTEG ( +Inflow Finesk-outflow Finesk-Spill Finesk-Evaporation, 2.53)'
    Units: b'MCM'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_finesk_dam()


@cache('run')
def maxvolume_finesk():
    """
    Real Name: b'"Max-volume Finesk"'
    Original Eqn: b'11.8'
    Units: b'MCM'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 11.8


def monthly_evaporation_1_finesk(x):
    """
    Real Name: b'"monthly evaporation -1 Finesk"'
    Original Eqn: b'( [(1,0)-(365,7)],(1,3.25),(2,3.25),(3,3.25),(4,3.25),(5,3.25),(6,3.25),(7,3.25),(8,3.25\\\\ ),(9,3.25),(10,3.25),(11,3.25),(12,3.25),(13,3.25),(14,3.25),(15,3.25),(16,3.25),(17\\\\ ,3.25),(18,3.25),(19,3.25),(20,3.25),(21,3.25),(22,3.25),(23,3.25),(24,3.25),(25,3.25\\\\ ),(26,3.25),(27,3.25),(28,3.25),(29,3.25),(30,3.25),(31,1.25667),(32,1.25667),(33,1.25667\\\\ ),(34,1.25667),(35,1.25667),(36,1.25667),(37,1.25667),(38,1.25667),(39,1.25667),(40\\\\ ,1.25667),(41,1.25667),(42,1.25667),(43,1.25667),(44,1.25667),(45,1.25667),(46,1.25667\\\\ ),(47,1.25667),(48,1.25667),(49,1.25667),(50,1.25667),(51,1.25667),(52,1.25667),(53\\\\ ,1.25667),(54,1.25667),(55,1.25667),(56,1.25667),(57,1.25667),(58,1.25667),(59,1.25667\\\\ ),(60,1.25667),(61,0.12),(62,0.12),(63,0.12),(64,0.12),(65,0.12),(66,0.12),(67,0.12\\\\ ),(68,0.12),(69,0.12),(70,0.12),(71,0.12),(72,0.12),(73,0.12),(74,0.12),(75,0.12),(\\\\ 76,0.12),(77,0.12),(78,0.12),(79,0.12),(80,0.12),(81,0.12),(82,0.12),(83,0.12),(84,\\\\ 0.12),(85,0.12),(86,0.12),(87,0.12),(88,0.12),(89,0.12),(90,0.12),(91,0.05333),(92,\\\\ 0.05333),(93,0.05333),(94,0.05333),(95,0.05333),(96,0.05333),(97,0.05333),(98,0.05333\\\\ ),(99,0.05333),(100,0.05333),(101,0.05333),(102,0.05333),(103,0.05333),(104,0.05333\\\\ ),(105,0.05333),(106,0.05333),(107,0.05333),(108,0.05333),(109,0.05333),(110,0.05333\\\\ ),(111,0.05333),(112,0.05333),(113,0.05333),(114,0.05333),(115,0.05333),(116,0.05333\\\\ ),(117,0.05333),(118,0.05333),(119,0.05333),(120,0.05333),(121,0.04333),(122,0.04333\\\\ ),(123,0.04333),(124,0.04333),(125,0.04333),(126,0.04333),(127,0.04333),(128,0.04333\\\\ ),(129,0.04333),(130,0.04333),(131,0.04333),(132,0.04333),(133,0.04333),(134,0.04333\\\\ ),(135,0.04333),(136,0.04333),(137,0.04333),(138,0.04333),(139,0.04333),(140,0.04333\\\\ ),(141,0.04333),(142,0.04333),(143,0.04333),(144,0.04333),(145,0.04333),(146,0.04333\\\\ ),(147,0.04333),(148,0.04333),(149,0.04333),(150,0.04333),(151,0.04),(152,0.04),(153\\\\ ,0.04),(154,0.04),(155,0.04),(156,0.04),(157,0.04),(158,0.04),(159,0.04),(160,0.04)\\\\ ,(161,0.04),(162,0.04),(163,0.04),(164,0.04),(165,0.04),(166,0.04),(167,0.04),(168,\\\\ 0.04),(169,0.04),(170,0.04),(171,0.04),(172,0.04),(173,0.04),(174,0.04),(175,0.04),\\\\ (176,0.04),(177,0.04),(178,0.04),(179,0.04),(180,0.04),(181,0.92667),(182,0.92667),\\\\ (183,0.92667),(184,0.92667),(185,0.92667),(186,0.92667),(187,0.92667),(188,0.92667)\\\\ ,(189,0.92667),(190,0.92667),(191,0.92667),(192,0.92667),(193,0.92667),(194,0.92667\\\\ ),(195,0.92667),(196,0.92667),(197,0.92667),(198,0.92667),(199,0.92667),(200,0.92667\\\\ ),(201,0.92667),(202,0.92667),(203,0.92667),(204,0.92667),(205,0.92667),(206,0.92667\\\\ ),(207,0.92667),(208,0.92667),(209,0.92667),(210,0.92667),(211,4.12),(212,4.12),(213\\\\ ,4.12),(214,4.12),(215,4.12),(216,4.12),(217,4.12),(218,4.12),(219,4.12),(220,4.12)\\\\ ,(221,4.12),(222,4.12),(223,4.12),(224,4.12),(225,4.12),(226,4.12),(227,4.12),(228,\\\\ 4.12),(229,4.12),(230,4.12),(231,4.12),(232,4.12),(233,4.12),(234,4.12),(235,4.12),\\\\ (236,4.12),(237,4.12),(238,4.12),(239,4.12),(240,4.12),(241,4.68667),(242,4.68667),\\\\ (243,4.68667),(244,4.68667),(245,4.68667),(246,4.68667),(247,4.68667),(248,4.68667)\\\\ ,(249,4.68667),(250,4.68667),(251,4.68667),(252,4.68667),(253,4.68667),(254,4.68667\\\\ ),(255,4.68667),(256,4.68667),(257,4.68667),(258,4.68667),(259,4.68667),(260,4.68667\\\\ ),(261,4.68667),(262,4.68667),(263,4.68667),(264,4.68667),(265,4.68667),(266,4.68667\\\\ ),(267,4.68667),(268,4.68667),(269,4.68667),(270,4.68667),(271,5.71),(272,5.71),(273\\\\ ,5.71),(274,5.71),(275,5.71),(276,5.71),(277,5.71),(278,5.71),(279,5.71),(280,5.71)\\\\ ,(281,5.71),(282,5.71),(283,5.71),(284,5.71),(285,5.71),(286,5.71),(287,5.71),(288,\\\\ 5.71),(289,5.71),(290,5.71),(291,5.71),(292,5.71),(293,5.71),(294,5.71),(295,5.71),\\\\ (296,5.71),(297,5.71),(298,5.71),(299,5.71),(300,5.71),(301,6.48667),(302,6.48667),\\\\ (303,6.48667),(304,6.48667),(305,6.48667),(306,6.48667),(307,6.48667),(308,6.48667)\\\\ ,(309,6.48667),(310,6.48667),(311,6.48667),(312,6.48667),(313,6.48667),(314,6.48667\\\\ ),(315,6.48667),(316,6.48667),(317,6.48667),(318,6.48667),(319,6.48667),(320,6.48667\\\\ ),(321,6.48667),(322,6.48667),(323,6.48667),(324,6.48667),(325,6.48667),(326,6.48667\\\\ ),(327,6.48667),(328,6.48667),(329,6.48667),(330,6.48667),(331,5.38667),(332,5.38667\\\\ ),(333,5.38667),(334,5.38667),(335,5.38667),(336,5.38667),(337,5.38667),(338,5.38667\\\\ ),(339,5.38667),(340,5.38667),(341,5.38667),(342,5.38667),(343,5.38667),(344,5.38667\\\\ ),(345,5.38667),(346,5.38667),(347,5.38667),(348,5.38667),(349,5.38667),(350,5.38667\\\\ ),(351,5.38667),(352,5.38667),(353,5.38667),(354,5.38667),(355,5.38667),(356,5.38667\\\\ ),(357,5.38667),(358,5.38667),(359,5.38667),(360,5.38667),(361,5.38667),(362,5.38667\\\\ ),(363,5.38667),(364,5.38667),(365,5.38667))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], [
                                3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25,
                                3.25,
                                3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25,
                                3.25,
                                1.25667, 1.25667, 1.25667, 1.25667, 1.25667, 1.25667, 1.25667, 1.25667, 1.25667,
                                1.25667,
                                1.25667, 1.25667, 1.25667, 1.25667, 1.25667, 1.25667, 1.25667, 1.25667, 1.25667,
                                1.25667,
                                1.25667, 1.25667, 1.25667, 1.25667, 1.25667, 1.25667, 1.25667, 1.25667, 1.25667,
                                1.25667,
                                0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12,
                                0.12,
                                0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12,
                                0.12,
                                0.05333, 0.05333, 0.05333, 0.05333, 0.05333, 0.05333, 0.05333, 0.05333, 0.05333,
                                0.05333,
                                0.05333, 0.05333, 0.05333, 0.05333, 0.05333, 0.05333, 0.05333, 0.05333, 0.05333,
                                0.05333,
                                0.05333, 0.05333, 0.05333, 0.05333, 0.05333, 0.05333, 0.05333, 0.05333, 0.05333,
                                0.05333,
                                0.04333, 0.04333, 0.04333, 0.04333, 0.04333, 0.04333, 0.04333, 0.04333, 0.04333,
                                0.04333,
                                0.04333, 0.04333, 0.04333, 0.04333, 0.04333, 0.04333, 0.04333, 0.04333, 0.04333,
                                0.04333,
                                0.04333, 0.04333, 0.04333, 0.04333, 0.04333, 0.04333, 0.04333, 0.04333, 0.04333,
                                0.04333,
                                0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04,
                                0.04,
                                0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04,
                                0.04,
                                0.92667, 0.92667, 0.92667, 0.92667, 0.92667, 0.92667, 0.92667, 0.92667, 0.92667,
                                0.92667,
                                0.92667, 0.92667, 0.92667, 0.92667, 0.92667, 0.92667, 0.92667, 0.92667, 0.92667,
                                0.92667,
                                0.92667, 0.92667, 0.92667, 0.92667, 0.92667, 0.92667, 0.92667, 0.92667, 0.92667,
                                0.92667,
                                4.12, 4.12, 4.12, 4.12, 4.12, 4.12, 4.12, 4.12, 4.12, 4.12, 4.12, 4.12, 4.12, 4.12,
                                4.12,
                                4.12, 4.12, 4.12, 4.12, 4.12, 4.12, 4.12, 4.12, 4.12, 4.12, 4.12, 4.12, 4.12, 4.12,
                                4.12,
                                4.68667, 4.68667, 4.68667, 4.68667, 4.68667, 4.68667, 4.68667, 4.68667, 4.68667,
                                4.68667,
                                4.68667, 4.68667, 4.68667, 4.68667, 4.68667, 4.68667, 4.68667, 4.68667, 4.68667,
                                4.68667,
                                4.68667, 4.68667, 4.68667, 4.68667, 4.68667, 4.68667, 4.68667, 4.68667, 4.68667,
                                4.68667,
                                5.71, 5.71, 5.71, 5.71, 5.71, 5.71, 5.71, 5.71, 5.71, 5.71, 5.71, 5.71, 5.71, 5.71,
                                5.71,
                                5.71, 5.71, 5.71, 5.71, 5.71, 5.71, 5.71, 5.71, 5.71, 5.71, 5.71, 5.71, 5.71, 5.71,
                                5.71,
                                6.48667, 6.48667, 6.48667, 6.48667, 6.48667, 6.48667, 6.48667, 6.48667, 6.48667,
                                6.48667,
                                6.48667, 6.48667, 6.48667, 6.48667, 6.48667, 6.48667, 6.48667, 6.48667, 6.48667,
                                6.48667,
                                6.48667, 6.48667, 6.48667, 6.48667, 6.48667, 6.48667, 6.48667, 6.48667, 6.48667,
                                6.48667,
                                5.38667, 5.38667, 5.38667, 5.38667, 5.38667, 5.38667, 5.38667, 5.38667, 5.38667,
                                5.38667,
                                5.38667, 5.38667, 5.38667, 5.38667, 5.38667, 5.38667, 5.38667, 5.38667, 5.38667,
                                5.38667,
                                5.38667, 5.38667, 5.38667, 5.38667, 5.38667, 5.38667, 5.38667, 5.38667, 5.38667,
                                5.38667,
                                5.38667, 5.38667, 5.38667, 5.38667, 5.38667
                            ])


@cache('run')
def normal_evaporation_1_finesk():
    """
    Real Name: b'"normal evaporation -1 Finesk"'
    Original Eqn: b'1/1000'
    Units: b'MCM/(km*km*mm*Month)'
    Limits: (None, None)
    Type: constant

    b'\\u062a\\u0628\\u062f\\u06cc\\u0644 \\u0645\\u06cc\\u0644\\u06cc\\u0645\\u062a\\u0631 \\u0628\\u0647 \\u0645\\u062a\\u0631'
    """
    return 1 / 1000


@cache('run')
def normal_period_1_finesk():
    """
    Real Name: b'"normal period -1 Finesk"'
    Original Eqn: b'1'
    Units: b'Month'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1


@cache('step')
def outflow_finesk():
    """
    Real Name: b'outflow Finesk'
    Original Eqn: b'IF THEN ELSE((((Finesk Dam-"mini-Sfinesk")/"normal period -1 Finesk")+Inflow Finesk-\\\\ Evaporation)>="Total Demand-1Finesk" , "Total Demand-1Finesk" ,Max(0, (((Finesk Dam-"mini-Sfinesk")/"normal period -1 Finesk")+Inflow Finesk-Evaporation )))'
    Units: b'MCM/Month'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.if_then_else(
        (((finesk_dam() - minisfinesk()) / normal_period_1_finesk()) + inflow_finesk() -
         evaporation()) >= total_demand1finesk(), total_demand1finesk(),
        np.maximum(0, (((finesk_dam() - minisfinesk()) / normal_period_1_finesk()) +
                       inflow_finesk() - evaporation())))


@cache('step')
def parvarij_station():
    """
    Real Name: b'Parvarij station'
    Original Eqn: b'River aftr Finesk Dam-Dom Sup after Finesk-Agric supply after Finesk+(Agric supply after Finesk\\\\ *0.2)'
    Units: b'MCM/Month'
    Limits: (None, None)
    Type: component

    b''
    """
    return river_aftr_finesk_dam() - dom_sup_after_finesk() - agric_supply_after_finesk() + (
            agric_supply_after_finesk() * 0.2)


@cache('step')
def spill_finesk():
    """
    Real Name: b'Spill Finesk'
    Original Eqn: b'IF THEN ELSE(((Finesk Dam/"normal period -1 Finesk")+Inflow Finesk-outflow Finesk-Evaporation\\\\ )>("Max-volume Finesk"/"normal period -1 Finesk"),((Finesk Dam /"normal period -1 Finesk")+Inflow Finesk-outflow Finesk-Evaporation-("Max-volume Finesk"\\\\ /"normal period -1 Finesk" )), 0)'
    Units: b'MCM/Month'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.if_then_else(
        ((finesk_dam() / normal_period_1_finesk()) + inflow_finesk() - outflow_finesk() -
         evaporation()) > (maxvolume_finesk() / normal_period_1_finesk()),
        ((finesk_dam() / normal_period_1_finesk()) + inflow_finesk() - outflow_finesk() -
         evaporation() - (maxvolume_finesk() / normal_period_1_finesk())), 0)


@cache('step')
def surface_1_finesk():
    """
    Real Name: b'"surface -1 Finesk"'
    Original Eqn: b'"volume -1 surface Look up Finesk"(Finesk Dam/Finesk 0)*"surface 0-1 Finesk"'
    Units: b'km*km'
    Limits: (None, None)
    Type: component

    b'\\u0645\\u0641\\u0627\\u0647\\u06cc\\u0645 \\u062a\\u0639\\u0631\\u06cc\\u0641 \\u0636\\u0631\\u06cc\\u0628 \\u0645\\u062e\\u0632\\u0646'
    """
    return volume_1_surface_look_up_finesk(finesk_dam() / finesk_0()) * surface_01_finesk()


@cache('run')
def surface_01_finesk():
    """
    Real Name: b'"surface 0-1 Finesk"'
    Original Eqn: b'1'
    Units: b'km*km'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1


def volume_1_surface_look_up_finesk(x):
    """
    Real Name: b'"volume -1 surface Look up Finesk"'
    Original Eqn: b'( [(0,0)-(40,1)],(0,0),(0.001,0.001),(0.004,0.004),(0.01,0.01),(0.03,0.01),(0.06,0.02)\\\\ ,(0.1,0.03),(0.18,0.04),(0.27,0.06),(0.4,0.07),(0.56,0.09),(0.75,0.11),(0.98,0.13),\\\\ (1.26,0.15),(1.58,0.17),(1.95,0.2),(2.37,0.23),(2.87,0.26),(3.43,0.3),(4.05,0.32),(\\\\ 4.73,0.36),(5.48,0.4),(6.32,0.44),(7.24,0.48),(8.24,0.52),(9.34,0.57),(10.52,0.61),\\\\ (11.78,0.65),(13.13,0.7),(14.58,0.75),(16.12,0.8),(17.77,0.85),(19.52,0.9),(21.38,0.96\\\\ ),(23.36,1.02),(25.44,1.07),(27.65,1.13),(29.98,1.19))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, [
        0, 0.001, 0.004, 0.01, 0.03, 0.06, 0.1, 0.18, 0.27, 0.4, 0.56, 0.75, 0.98, 1.26, 1.58,
        1.95, 2.37, 2.87, 3.43, 4.05, 4.73, 5.48, 6.32, 7.24, 8.24, 9.34, 10.52, 11.78, 13.13,
        14.58, 16.12, 17.77, 19.52, 21.38, 23.36, 25.44, 27.65, 29.98
    ], [
                                0, 0.001, 0.004, 0.01, 0.01, 0.02, 0.03, 0.04, 0.06, 0.07, 0.09, 0.11, 0.13, 0.15, 0.17,
                                0.2, 0.23, 0.26, 0.3, 0.32, 0.36, 0.4, 0.44, 0.48, 0.52, 0.57, 0.61, 0.65, 0.7, 0.75,
                                0.8,
                                0.85, 0.9, 0.96, 1.02, 1.07, 1.13, 1.19
                            ])


def wr_dem_befr_finesk(x):
    """
    Real Name: b'Wr Dem befr Finesk'
    Original Eqn: b'( [(1,0)-(365,0.3)],(1,0.01115),(2,0.01115),(3,0.01115),(4,0.01115),(5,0.01115),(6,0.01115\\\\ ),(7,0.01115),(8,0.01115),(9,0.01115),(10,0.01115),(11,0.01115),(12,0.01115),(13,0.01115\\\\ ),(14,0.01115),(15,0.01115),(16,0.01115),(17,0.01115),(18,0.01115),(19,0.01115),(20\\\\ ,0.01115),(21,0.01115),(22,0.01115),(23,0.01115),(24,0.01115),(25,0.01115),(26,0.01115\\\\ ),(27,0.01115),(28,0.01115),(29,0.01115),(30,0.01115),(31,0),(32,0),(33,0),(34,0),(\\\\ 35,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),\\\\ (47,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0)\\\\ ,(59,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0\\\\ ),(71,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,\\\\ 0),(83,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94\\\\ ,0),(95,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105\\\\ ,0),(106,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0)\\\\ ,(116,0),(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126\\\\ ,0),(127,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0)\\\\ ,(137,0),(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147\\\\ ,0),(148,0),(149,0),(150,0),(151,0.00084),(152,0.00084),(153,0.00084),(154,0.00084)\\\\ ,(155,0.00084),(156,0.00084),(157,0.00084),(158,0.00084),(159,0.00084),(160,0.00084\\\\ ),(161,0.00084),(162,0.00084),(163,0.00084),(164,0.00084),(165,0.00084),(166,0.00084\\\\ ),(167,0.00084),(168,0.00084),(169,0.00084),(170,0.00084),(171,0.00084),(172,0.00084\\\\ ),(173,0.00084),(174,0.00084),(175,0.00084),(176,0.00084),(177,0.00084),(178,0.00084\\\\ ),(179,0.00084),(180,0.00084),(181,0.03114),(182,0.03114),(183,0.03114),(184,0.03114\\\\ ),(185,0.03114),(186,0.03114),(187,0.03114),(188,0.03114),(189,0.03114),(190,0.03114\\\\ ),(191,0.03114),(192,0.03114),(193,0.03114),(194,0.03114),(195,0.03114),(196,0.03114\\\\ ),(197,0.03114),(198,0.03114),(199,0.03114),(200,0.03114),(201,0.03114),(202,0.03114\\\\ ),(203,0.03114),(204,0.03114),(205,0.03114),(206,0.03114),(207,0.03114),(208,0.03114\\\\ ),(209,0.03114),(210,0.03114),(211,0.09685),(212,0.09685),(213,0.09685),(214,0.09685\\\\ ),(215,0.09685),(216,0.09685),(217,0.09685),(218,0.09685),(219,0.09685),(220,0.09685\\\\ ),(221,0.09685),(222,0.09685),(223,0.09685),(224,0.09685),(225,0.09685),(226,0.09685\\\\ ),(227,0.09685),(228,0.09685),(229,0.09685),(230,0.09685),(231,0.09685),(232,0.09685\\\\ ),(233,0.09685),(234,0.09685),(235,0.09685),(236,0.09685),(237,0.09685),(238,0.09685\\\\ ),(239,0.09685),(240,0.09685),(241,0.14005),(242,0.14005),(243,0.14005),(244,0.14005\\\\ ),(245,0.14005),(246,0.14005),(247,0.14005),(248,0.14005),(249,0.14005),(250,0.14005\\\\ ),(251,0.14005),(252,0.14005),(253,0.14005),(254,0.14005),(255,0.14005),(256,0.14005\\\\ ),(257,0.14005),(258,0.14005),(259,0.14005),(260,0.14005),(261,0.14005),(262,0.14005\\\\ ),(263,0.14005),(264,0.14005),(265,0.14005),(266,0.14005),(267,0.14005),(268,0.14005\\\\ ),(269,0.14005),(270,0.14005),(271,0.20065),(272,0.20065),(273,0.20065),(274,0.20065\\\\ ),(275,0.20065),(276,0.20065),(277,0.20065),(278,0.20065),(279,0.20065),(280,0.20065\\\\ ),(281,0.20065),(282,0.20065),(283,0.20065),(284,0.20065),(285,0.20065),(286,0.20065\\\\ ),(287,0.20065),(288,0.20065),(289,0.20065),(290,0.20065),(291,0.20065),(292,0.20065\\\\ ),(293,0.20065),(294,0.20065),(295,0.20065),(296,0.20065),(297,0.20065),(298,0.20065\\\\ ),(299,0.20065),(300,0.20065),(301,0.18101),(302,0.18101),(303,0.18101),(304,0.18101\\\\ ),(305,0.18101),(306,0.18101),(307,0.18101),(308,0.18101),(309,0.18101),(310,0.18101\\\\ ),(311,0.18101),(312,0.18101),(313,0.18101),(314,0.18101),(315,0.18101),(316,0.18101\\\\ ),(317,0.18101),(318,0.18101),(319,0.18101),(320,0.18101),(321,0.18101),(322,0.18101\\\\ ),(323,0.18101),(324,0.18101),(325,0.18101),(326,0.18101),(327,0.18101),(328,0.18101\\\\ ),(329,0.18101),(330,0.18101),(331,0.07406),(332,0.07406),(333,0.07406),(334,0.07406\\\\ ),(335,0.07406),(336,0.07406),(337,0.07406),(338,0.07406),(339,0.07406),(340,0.07406\\\\ ),(341,0.07406),(342,0.07406),(343,0.07406),(344,0.07406),(345,0.07406),(346,0.07406\\\\ ),(347,0.07406),(348,0.07406),(349,0.07406),(350,0.07406),(351,0.07406),(352,0.07406\\\\ ),(353,0.07406),(354,0.07406),(355,0.07406),(356,0.07406),(357,0.07406),(358,0.07406\\\\ ),(359,0.07406),(360,0.07406),(361,0.07406),(362,0.07406),(363,0.07406),(364,0.07406\\\\ ),(365,0.07406))'
    Units: b'MCM/Month'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
        132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
        168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
        204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
        276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
        294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
        312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,
        348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365
    ], [
                                0.01115, 0.01115, 0.01115, 0.01115, 0.01115, 0.01115, 0.01115, 0.01115, 0.01115,
                                0.01115,
                                0.01115, 0.01115, 0.01115, 0.01115, 0.01115, 0.01115, 0.01115, 0.01115, 0.01115,
                                0.01115,
                                0.01115, 0.01115, 0.01115, 0.01115, 0.01115, 0.01115, 0.01115, 0.01115, 0.01115,
                                0.01115,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0.00084, 0.00084, 0.00084, 0.00084, 0.00084, 0.00084, 0.00084, 0.00084, 0.00084,
                                0.00084,
                                0.00084, 0.00084, 0.00084, 0.00084, 0.00084, 0.00084, 0.00084, 0.00084, 0.00084,
                                0.00084,
                                0.00084, 0.00084, 0.00084, 0.00084, 0.00084, 0.00084, 0.00084, 0.00084, 0.00084,
                                0.00084,
                                0.03114, 0.03114, 0.03114, 0.03114, 0.03114, 0.03114, 0.03114, 0.03114, 0.03114,
                                0.03114,
                                0.03114, 0.03114, 0.03114, 0.03114, 0.03114, 0.03114, 0.03114, 0.03114, 0.03114,
                                0.03114,
                                0.03114, 0.03114, 0.03114, 0.03114, 0.03114, 0.03114, 0.03114, 0.03114, 0.03114,
                                0.03114,
                                0.09685, 0.09685, 0.09685, 0.09685, 0.09685, 0.09685, 0.09685, 0.09685, 0.09685,
                                0.09685,
                                0.09685, 0.09685, 0.09685, 0.09685, 0.09685, 0.09685, 0.09685, 0.09685, 0.09685,
                                0.09685,
                                0.09685, 0.09685, 0.09685, 0.09685, 0.09685, 0.09685, 0.09685, 0.09685, 0.09685,
                                0.09685,
                                0.14005, 0.14005, 0.14005, 0.14005, 0.14005, 0.14005, 0.14005, 0.14005, 0.14005,
                                0.14005,
                                0.14005, 0.14005, 0.14005, 0.14005, 0.14005, 0.14005, 0.14005, 0.14005, 0.14005,
                                0.14005,
                                0.14005, 0.14005, 0.14005, 0.14005, 0.14005, 0.14005, 0.14005, 0.14005, 0.14005,
                                0.14005,
                                0.20065, 0.20065, 0.20065, 0.20065, 0.20065, 0.20065, 0.20065, 0.20065, 0.20065,
                                0.20065,
                                0.20065, 0.20065, 0.20065, 0.20065, 0.20065, 0.20065, 0.20065, 0.20065, 0.20065,
                                0.20065,
                                0.20065, 0.20065, 0.20065, 0.20065, 0.20065, 0.20065, 0.20065, 0.20065, 0.20065,
                                0.20065,
                                0.18101, 0.18101, 0.18101, 0.18101, 0.18101, 0.18101, 0.18101, 0.18101, 0.18101,
                                0.18101,
                                0.18101, 0.18101, 0.18101, 0.18101, 0.18101, 0.18101, 0.18101, 0.18101, 0.18101,
                                0.18101,
                                0.18101, 0.18101, 0.18101, 0.18101, 0.18101, 0.18101, 0.18101, 0.18101, 0.18101,
                                0.18101,
                                0.07406, 0.07406, 0.07406, 0.07406, 0.07406, 0.07406, 0.07406, 0.07406, 0.07406,
                                0.07406,
                                0.07406, 0.07406, 0.07406, 0.07406, 0.07406, 0.07406, 0.07406, 0.07406, 0.07406,
                                0.07406,
                                0.07406, 0.07406, 0.07406, 0.07406, 0.07406, 0.07406, 0.07406, 0.07406, 0.07406,
                                0.07406,
                                0.07406, 0.07406, 0.07406, 0.07406, 0.07406
                            ])


@cache('run')
def final_time():
    """
    Real Name: b'FINAL TIME'
    Original Eqn: b'365'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b'The final time for the simulation.'
    """
    return 365


@cache('run')
def initial_time():
    """
    Real Name: b'INITIAL TIME'
    Original Eqn: b'0'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b'The initial time for the simulation.'
    """
    return 0


@cache('step')
def saveper():
    """
    Real Name: b'SAVEPER'
    Original Eqn: b'TIME STEP'
    Units: b'Day'
    Limits: (0.0, None)
    Type: component

    b'The frequency with which output is stored.'
    """
    return time_step()


@cache('run')
def time_step():
    """
    Real Name: b'TIME STEP'
    Original Eqn: b'1'
    Units: b'Day'
    Limits: (0.0, None)
    Type: constant

    b'The time step for the simulation.'
    """
    return 1


_integ_abbn = functions.Integ(lambda: abbn_inflow() - abbn_eva() - abbn_outflow() - abbn_spill(),
                              lambda: 19)

_integ_zr_reservoir = functions.Integ(lambda: zr_inflow() - zr_evap() - zr_outflow() - zr_spill(),
                                      lambda: 31)

_integ_tajan_res_mcm = functions.Integ(
    lambda: tj_inflow() - tj_evaporation() - tj_outflow() - tj_spill(), lambda: 37.9)

_integ_finesk_dam = functions.Integ(
    lambda: inflow_finesk() - outflow_finesk() - spill_finesk() - evaporation(), lambda: 2.53)
