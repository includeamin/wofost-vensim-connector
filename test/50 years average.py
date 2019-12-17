"""
Python model "50 years average.py"
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
    "citrus_zr": [],
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
    Original Eqn: b'( [(1,0)-(365,0.02)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,\\\\ 0),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23\\\\ ,0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35\\\\ ,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47\\\\ ,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94,0),(95\\\\ ,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105,0),(106\\\\ ,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0),(116,0)\\\\ ,(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126,0),(127\\\\ ,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0),(137,0)\\\\ ,(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147,0),(148\\\\ ,0),(149,0),(150,0),(151,0),(152,0),(153,0),(154,0),(155,0),(156,0),(157,0),(158,0)\\\\ ,(159,0),(160,0),(161,0),(162,0),(163,0),(164,0),(165,0),(166,0),(167,0),(168,0),(169\\\\ ,0),(170,0),(171,0),(172,0),(173,0),(174,0),(175,0),(176,0),(177,0),(178,0),(179,0)\\\\ ,(180,0),(181,0),(182,0),(183,0),(184,0),(185,0),(186,0),(187,0),(188,0),(189,0),(190\\\\ ,0),(191,0),(192,0),(193,0),(194,0),(195,0.0111086),(196,0.0111086),(197,0.0111086)\\\\ ,(198,0.0111086),(199,0.0111086),(200,0.0111086),(201,0.0111086),(202,0.0111086),(203\\\\ ,0.0111086),(204,0.0111086),(205,0.0133303),(206,0.0133303),(207,0.0133303),(208,0.0133303\\\\ ),(209,0.0133303),(210,0.0133303),(211,0.0133303),(212,0.0133303),(213,0.0133303),(\\\\ 214,0.0133303),(215,0.0140139),(216,0.0140139),(217,0.0140139),(218,0.0140139),(219\\\\ ,0.0140139),(220,0.0140139),(221,0.0140139),(222,0.0140139),(223,0.0140139),(224,0.0140139\\\\ ),(225,0.0146975),(226,0.0146975),(227,0.0146975),(228,0.0146975),(229,0.0146975),(\\\\ 230,0.0146975),(231,0.0146975),(232,0.0146975),(233,0.0146975),(234,0.0146975),(235\\\\ ,0.0162357),(236,0.0162357),(237,0.0162357),(238,0.0162357),(239,0.0162357),(240,0.0162357\\\\ ),(241,0.0162357),(242,0.0162357),(243,0.0162357),(244,0.0162357),(245,0.0148684),(\\\\ 246,0.0148684),(247,0.0148684),(248,0.0148684),(249,0.0148684),(250,0.0148684),(251\\\\ ,0.0148684),(252,0.0148684),(253,0.0148684),(254,0.0148684),(255,0.0116213),(256,0.0116213\\\\ ),(257,0.0116213),(258,0.0116213),(259,0.0116213),(260,0.0116213),(261,0.0116213),(\\\\ 262,0.0116213),(263,0.0116213),(264,0.0116213),(265,0.00854508),(266,0.00854508),(267\\\\ ,0.00854508),(268,0.00854508),(269,0.00854508),(270,0.00854508),(271,0.00854508),(272\\\\ ,0.00854508),(273,0.00854508),(274,0.00854508),(275,0.00854508),(276,0.00683607),(277\\\\ ,0.00683607),(278,0.00683607),(279,0.00683607),(280,0.00683607),(281,0.00683607),(282\\\\ ,0.00683607),(283,0.00683607),(284,0.00683607),(285,0.00683607),(286,0),(287,0),(288\\\\ ,0),(289,0),(290,0),(291,0),(292,0),(293,0),(294,0),(295,0),(296,0),(297,0),(298,0)\\\\ ,(299,0),(300,0),(301,0),(302,0),(303,0),(304,0),(305,0),(306,0),(307,0),(308,0),(309\\\\ ,0),(310,0),(311,0),(312,0),(313,0),(314,0),(315,0),(316,0),(317,0),(318,0),(319,0)\\\\ ,(320,0),(321,0),(322,0),(323,0),(324,0),(325,0),(326,0),(327,0),(328,0),(329,0),(330\\\\ ,0),(331,0),(332,0),(333,0),(334,0),(335,0),(336,0),(337,0),(338,0),(339,0),(340,0)\\\\ ,(341,0),(342,0),(343,0),(344,0),(345,0),(346,0),(347,0),(348,0),(349,0),(350,0),(351\\\\ ,0),(352,0),(353,0),(354,0),(355,0),(356,0),(357,0),(358,0),(359,0),(360,0),(361,0)\\\\ ,(362,0),(363,0),(364,0),(365,0))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b'forth priority'
    """
    return functions.lookup(x, time_in_lookup_data,lookups_data["wheat_tjj_dd"])


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
    Original Eqn: b'( [(1,0)-(365,0.4)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0\\\\ ),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23,\\\\ 0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35\\\\ ,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47\\\\ ,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0.128097),(92,0.128097),(93\\\\ ,0.128097),(94,0.128097),(95,0.128097),(96,0.128097),(97,0.128097),(98,0.128097),(99\\\\ ,0.128097),(100,0.128097),(101,0.143624),(102,0.143624),(103,0.143624),(104,0.143624\\\\ ),(105,0.143624),(106,0.143624),(107,0.143624),(108,0.143624),(109,0.143624),(110,0.143624\\\\ ),(111,0.165621),(112,0.165621),(113,0.165621),(114,0.165621),(115,0.165621),(116,0.165621\\\\ ),(117,0.165621),(118,0.165621),(119,0.165621),(120,0.165621),(121,0.187617),(122,0.187617\\\\ ),(123,0.187617),(124,0.187617),(125,0.187617),(126,0.187617),(127,0.187617),(128,0.187617\\\\ ),(129,0.187617),(130,0.187617),(131,0.209613),(132,0.209613),(133,0.209613),(134,0.209613\\\\ ),(135,0.209613),(136,0.209613),(137,0.209613),(138,0.209613),(139,0.209613),(140,0.209613\\\\ ),(141,0.256194),(142,0.256194),(143,0.256194),(144,0.256194),(145,0.256194),(146,0.256194\\\\ ),(147,0.256194),(148,0.256194),(149,0.256194),(150,0.256194),(151,0.260076),(152,0.260076\\\\ ),(153,0.260076),(154,0.260076),(155,0.260076),(156,0.260076),(157,0.260076),(158,0.260076\\\\ ),(159,0.260076),(160,0.260076),(161,0.285954),(162,0.285954),(163,0.285954),(164,0.285954\\\\ ),(165,0.285954),(166,0.285954),(167,0.285954),(168,0.285954),(169,0.285954),(170,0.285954\\\\ ),(171,0.285954),(172,0.285954),(173,0.285954),(174,0.285954),(175,0.285954),(176,0.285954\\\\ ),(177,0.285954),(178,0.285954),(179,0.285954),(180,0.285954),(181,0.125509),(182,0.125509\\\\ ),(183,0.125509),(184,0.125509),(185,0.125509),(186,0.125509),(187,0.125509),(188,0.125509\\\\ ),(189,0.125509),(190,0.125509),(191,0.0517564),(192,0.0517564),(193,0.0517564),(194\\\\ ,0.0517564),(195,0.0517564),(196,0.0517564),(197,0.0517564),(198,0.0517564),(199,0.0517564\\\\ ),(200,0.0517564),(201,0.197968),(202,0.197968),(203,0.197968),(204,0.197968),(205,\\\\ 0.197968),(206,0.197968),(207,0.197968),(208,0.197968),(209,0.197968),(210,0.197968\\\\ ),(211,0.34418),(212,0.34418),(213,0.34418),(214,0.34418),(215,0.34418),(216,0.34418\\\\ ),(217,0.34418),(218,0.34418),(219,0.34418),(220,0.34418),(221,0.361001),(222,0.361001\\\\ ),(223,0.361001),(224,0.361001),(225,0.361001),(226,0.361001),(227,0.361001),(228,0.361001\\\\ ),(229,0.361001),(230,0.361001),(231,0.346768),(232,0.346768),(233,0.346768),(234,0.346768\\\\ ),(235,0.346768),(236,0.346768),(237,0.346768),(238,0.346768),(239,0.346768),(240,0.346768\\\\ ),(241,0.128097),(242,0.128097),(243,0.128097),(244,0.128097),(245,0.128097),(246,0.128097\\\\ ),(247,0.128097),(248,0.128097),(249,0.128097),(250,0.128097),(251,0.0181147),(252,\\\\ 0.0181147),(253,0.0181147),(254,0.0181147),(255,0.0181147),(256,0.0181147),(257,0.0181147\\\\ ),(258,0.0181147),(259,0.0181147),(260,0.0181147),(261,0.0375234),(262,0.0375234),(\\\\ 263,0.0375234),(264,0.0375234),(265,0.0375234),(266,0.0375234),(267,0.0375234),(268\\\\ ,0.0375234),(269,0.0375234),(270,0.0375234),(271,0.0918676),(272,0.0918676),(273,0.0918676\\\\ ),(274,0.0918676),(275,0.0918676),(276,0.0918676),(277,0.0918676),(278,0.0918676),(\\\\ 279,0.0918676),(280,0.0918676),(281,0.111276),(282,0.111276),(283,0.111276),(284,0.111276\\\\ ),(285,0.111276),(286,0.111276),(287,0.111276),(288,0.111276),(289,0.111276),(290,0.111276\\\\ ),(291,0.0271721),(292,0.0271721),(293,0.0271721),(294,0.0271721),(295,0.0271721),(\\\\ 296,0.0271721),(297,0.0271721),(298,0.0271721),(299,0.0271721),(300,0.0271721),(301\\\\ ,0.0271721),(302,0),(303,0),(304,0),(305,0),(306,0),(307,0),(308,0),(309,0),(310,0)\\\\ ,(311,0),(312,0),(313,0),(314,0),(315,0),(316,0),(317,0),(318,0),(319,0),(320,0),(321\\\\ ,0),(322,0),(323,0),(324,0),(325,0),(326,0),(327,0),(328,0),(329,0),(330,0),(331,0)\\\\ ,(332,0),(333,0),(334,0),(335,0),(336,0),(337,0),(338,0),(339,0),(340,0),(341,0),(342\\\\ ,0),(343,0),(344,0),(345,0),(346,0),(347,0),(348,0),(349,0),(350,0),(351,0),(352,0)\\\\ ,(353,0),(354,0),(355,0),(356,0),(357,0),(358,0),(359,0),(360,0),(361,0),(362,0),(363\\\\ ,0),(364,0),(365,0))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b'second priority'
    """
    return functions.lookup(x,time_in_lookup_data,lookups_data["citrud_tjj_dd"])


def tomato_tjj_dd(x):
    """
    Real Name: b'tomato tjj dd'
    Original Eqn: b'( [(1,0)-(365,0.0003)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11\\\\ ,0),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23\\\\ ,0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35\\\\ ,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47\\\\ ,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94,0),(95\\\\ ,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105,0),(106\\\\ ,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0),(116,0)\\\\ ,(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126,0),(127\\\\ ,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0),(137,0)\\\\ ,(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147,0),(148\\\\ ,0),(149,0),(150,0),(151,0),(152,0),(153,0),(154,0),(155,0),(156,0),(157,0),(158,0)\\\\ ,(159,0),(160,0),(161,0),(162,0),(163,0),(164,0),(165,0),(166,0),(167,0),(168,0),(169\\\\ ,0),(170,0),(171,0),(172,0),(173,0),(174,0),(175,0),(176,0),(177,0),(178,0),(179,0)\\\\ ,(180,0),(181,0),(182,0),(183,0),(184,0),(185,0),(186,0),(187,0),(188,0),(189,0),(190\\\\ ,0),(191,0),(192,0),(193,0),(194,0),(195,0),(196,0),(197,0),(198,0),(199,0),(200,0)\\\\ ,(201,0),(202,0),(203,0),(204,0),(205,0.000173858),(206,0.000173858),(207,0.000173858\\\\ ),(208,0.000173858),(209,0.000173858),(210,0.000173858),(211,0.000173858),(212,0.000173858\\\\ ),(213,0.000173858),(214,0.000173858),(215,0.000195003),(216,0.000195003),(217,0.000195003\\\\ ),(218,0.000195003),(219,0.000195003),(220,0.000195003),(221,0.000195003),(222,0.000195003\\\\ ),(223,0.000195003),(224,0.000195003),(225,0.000202051),(226,0.000202051),(227,0.000202051\\\\ ),(228,0.000202051),(229,0.000202051),(230,0.000202051),(231,0.000202051),(232,0.000202051\\\\ ),(233,0.000202051),(234,0.000202051),(235,0.000223196),(236,0.000223196),(237,0.000223196\\\\ ),(238,0.000223196),(239,0.000223196),(240,0.000223196),(241,0.000223196),(242,0.000223196\\\\ ),(243,0.000223196),(244,0.000223196),(245,0.000244341),(246,0.000244341),(247,0.000244341\\\\ ),(248,0.000244341),(249,0.000244341),(250,0.000244341),(251,0.000244341),(252,0.000244341\\\\ ),(253,0.000244341),(254,0.000244341),(255,0.000260787),(256,0.000260787),(257,0.000260787\\\\ ),(258,0.000260787),(259,0.000260787),(260,0.000260787),(261,0.000260787),(262,0.000260787\\\\ ),(263,0.000260787),(264,0.000260787),(265,0.000270184),(266,0.000270184),(267,0.000270184\\\\ ),(268,0.000270184),(269,0.000270184),(270,0.000270184),(271,0.000270184),(272,0.000270184\\\\ ),(273,0.000270184),(274,0.000270184),(275,0.000270184),(276,0),(277,0),(278,0),(279\\\\ ,0),(280,0),(281,0),(282,0),(283,0),(284,0),(285,0),(286,0),(287,0),(288,0),(289,0)\\\\ ,(290,0),(291,0),(292,0),(293,0),(294,0),(295,0),(296,0),(297,0),(298,0),(299,0),(300\\\\ ,0),(301,0),(302,0),(303,0),(304,0),(305,0),(306,0),(307,0),(308,0),(309,0),(310,0)\\\\ ,(311,0),(312,0),(313,0),(314,0),(315,0),(316,0),(317,0),(318,0),(319,0),(320,0),(321\\\\ ,0),(322,0),(323,0),(324,0),(325,0),(326,0),(327,0),(328,0),(329,0),(330,0),(331,0)\\\\ ,(332,0),(333,0),(334,0),(335,0),(336,0),(337,0),(338,0),(339,0),(340,0),(341,0),(342\\\\ ,0),(343,0),(344,0),(345,0),(346,0),(347,0),(348,0),(349,0),(350,0),(351,0),(352,0)\\\\ ,(353,0),(354,0),(355,0),(356,0),(357,0),(358,0),(359,0),(360,0),(361,0),(362,0),(363\\\\ ,0),(364,0),(365,0))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, time_in_lookup_data,lookups_data["tomato_tjj_dd"])


def grain_maiz_tjj_dd(x):
    """
    Real Name: b'grain maiz tjj dd'
    Original Eqn: b'( [(1,0)-(365,0.02)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,\\\\ 0),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23\\\\ ,0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35\\\\ ,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47\\\\ ,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94,0),(95\\\\ ,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105,0),(106\\\\ ,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0),(116,0)\\\\ ,(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126,0),(127\\\\ ,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0),(137,0)\\\\ ,(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147,0),(148\\\\ ,0),(149,0),(150,0),(151,0),(152,0),(153,0),(154,0),(155,0),(156,0),(157,0),(158,0)\\\\ ,(159,0),(160,0),(161,0),(162,0),(163,0),(164,0),(165,0),(166,0),(167,0),(168,0),(169\\\\ ,0),(170,0),(171,0),(172,0),(173,0),(174,0),(175,0),(176,0),(177,0),(178,0),(179,0)\\\\ ,(180,0),(181,0),(182,0),(183,0),(184,0),(185,0),(186,0),(187,0),(188,0),(189,0),(190\\\\ ,0),(191,0),(192,0),(193,0),(194,0),(195,0),(196,0),(197,0),(198,0),(199,0),(200,0)\\\\ ,(201,0),(202,0),(203,0),(204,0.0040535),(205,0.0040535),(206,0.0040535),(207,0.0040535\\\\ ),(208,0.0040535),(209,0.0040535),(210,0.0040535),(211,0.0040535),(212,0.0040535),(\\\\ 213,0.0040535),(214,0.0040535),(215,0.0025795),(216,0.0025795),(217,0.0025795),(218\\\\ ,0.0025795),(219,0.0025795),(220,0.0025795),(221,0.0025795),(222,0.0025795),(223,0.0025795\\\\ ),(224,0.0025795),(225,0.006633),(226,0.006633),(227,0.006633),(228,0.006633),(229,\\\\ 0.006633),(230,0.006633),(231,0.006633),(232,0.006633),(233,0.006633),(234,0.006633\\\\ ),(235,0.002211),(236,0.002211),(237,0.002211),(238,0.002211),(239,0.002211),(240,0.002211\\\\ ),(241,0.002211),(242,0.002211),(243,0.002211),(244,0.002211),(245,0.0011055),(246,\\\\ 0.0011055),(247,0.0011055),(248,0.0011055),(249,0.0011055),(250,0.0011055),(251,0.0011055\\\\ ),(252,0.0011055),(253,0.0011055),(254,0.0011055),(255,0.005159),(256,0.005159),(257\\\\ ,0.005159),(258,0.005159),(259,0.005159),(260,0.005159),(261,0.005159),(262,0.005159\\\\ ),(263,0.005159),(264,0.005159),(265,0.0062645),(266,0.0062645),(267,0.0062645),(268\\\\ ,0.0062645),(269,0.0062645),(270,0.0062645),(271,0.0062645),(272,0.0062645),(273,0.0062645\\\\ ),(274,0.0062645),(275,0.0062645),(276,0.011792),(277,0.011792),(278,0.011792),(279\\\\ ,0.011792),(280,0.011792),(281,0.011792),(282,0.011792),(283,0.011792),(284,0.011792\\\\ ),(285,0.011792),(286,0.004422),(287,0.004422),(288,0.004422),(289,0.004422),(290,0.004422\\\\ ),(291,0.004422),(292,0.004422),(293,0.004422),(294,0.004422),(295,0.004422),(296,0.005159\\\\ ),(297,0.005159),(298,0.005159),(299,0.005159),(300,0.005159),(301,0.005159),(302,0.005159\\\\ ),(303,0.005159),(304,0.005159),(305,0.001474),(306,0.001474),(307,0.001474),(308,0.001474\\\\ ),(309,0.001474),(310,0.001474),(311,0.001474),(312,0.001474),(313,0.001474),(314,0.001474\\\\ ),(315,0),(316,0),(317,0),(318,0),(319,0),(320,0),(321,0),(322,0),(323,0),(324,0),(\\\\ 325,0),(326,0),(327,0),(328,0),(329,0),(330,0),(331,0),(332,0),(333,0),(334,0),(335\\\\ ,0),(336,0),(337,0),(338,0),(339,0),(340,0),(341,0),(342,0),(343,0),(344,0),(345,0)\\\\ ,(346,0),(347,0),(348,0),(349,0),(350,0),(351,0),(352,0),(353,0),(354,0),(355,0),(356\\\\ ,0),(357,0),(358,0),(359,0),(360,0),(361,0),(362,0),(363,0),(364,0),(365,0))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, time_in_lookup_data,lookups_data["grain_maiz_tjj_dd"])


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
    Original Eqn: b'( [(1,0)-(365,0.02)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,\\\\ 0),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23\\\\ ,0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35\\\\ ,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47\\\\ ,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94,0),(95\\\\ ,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105,0),(106\\\\ ,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0),(116,0)\\\\ ,(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126,0),(127\\\\ ,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0),(137,0)\\\\ ,(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147,0),(148\\\\ ,0),(149,0),(150,0),(151,0),(152,0),(153,0),(154,0.00130622),(155,0.00130622),(156,\\\\ 0.00130622),(157,0.00130622),(158,0.00130622),(159,0.00130622),(160,0.00130622),(161\\\\ ,0.00130622),(162,0.00130622),(163,0.00130622),(164,0.00261245),(165,0.00261245),(166\\\\ ,0.00261245),(167,0.00261245),(168,0.00261245),(169,0.00261245),(170,0.00261245),(171\\\\ ,0.00261245),(172,0.00261245),(173,0.00261245),(174,0.00478948),(175,0.00478948),(176\\\\ ,0.00478948),(177,0.00478948),(178,0.00478948),(179,0.00478948),(180,0.00478948),(181\\\\ ,0.00478948),(182,0.00478948),(183,0.00478948),(184,0.0113206),(185,0.0113206),(186\\\\ ,0.0113206),(187,0.0113206),(188,0.0113206),(189,0.0113206),(190,0.0113206),(191,0.0113206\\\\ ),(192,0.0113206),(193,0.0113206),(194,0.0165455),(195,0.0165455),(196,0.0165455),(\\\\ 197,0.0165455),(198,0.0165455),(199,0.0165455),(200,0.0165455),(201,0.0165455),(202\\\\ ,0.0165455),(203,0.0165455),(204,0.0165455),(205,0.0130622),(206,0.0130622),(207,0.0130622\\\\ ),(208,0.0130622),(209,0.0130622),(210,0.0130622),(211,0.0130622),(212,0.0130622),(\\\\ 213,0.0130622),(214,0.0130622),(215,0.0174163),(216,0.0174163),(217,0.0174163),(218\\\\ ,0.0174163),(219,0.0174163),(220,0.0174163),(221,0.0174163),(222,0.0174163),(223,0.0174163\\\\ ),(224,0.0174163),(225,0.0178517),(226,0.0178517),(227,0.0178517),(228,0.0178517),(\\\\ 229,0.0178517),(230,0.0178517),(231,0.0178517),(232,0.0178517),(233,0.0178517),(234\\\\ ,0.0178517),(235,0.0156747),(236,0.0156747),(237,0.0156747),(238,0.0156747),(239,0.0156747\\\\ ),(240,0.0156747),(241,0.0156747),(242,0.0156747),(243,0.0156747),(244,0.0156747),(\\\\ 245,0.0100144),(246,0.0100144),(247,0.0100144),(248,0.0100144),(249,0.0100144),(250\\\\ ,0.0100144),(251,0.0100144),(252,0.0100144),(253,0.0100144),(254,0.0100144),(255,0.0121914\\\\ ),(256,0.0121914),(257,0.0121914),(258,0.0121914),(259,0.0121914),(260,0.0121914),(\\\\ 261,0.0121914),(262,0.0121914),(263,0.0121914),(264,0.0121914),(265,0.00783733),(266\\\\ ,0.00783733),(267,0.00783733),(268,0.00783733),(269,0.00783733),(270,0.00783733),(271\\\\ ,0.00783733),(272,0.00783733),(273,0.00783733),(274,0.00783733),(275,0.00783733),(276\\\\ ,0.00870815),(277,0.00870815),(278,0.00870815),(279,0.00870815),(280,0.00870815),(281\\\\ ,0.00870815),(282,0.00870815),(283,0.00870815),(284,0.00870815),(285,0.00870815),(286\\\\ ,0),(287,0),(288,0),(289,0),(290,0),(291,0),(292,0),(293,0),(294,0),(295,0),(296,0)\\\\ ,(297,0),(298,0),(299,0),(300,0),(301,0),(302,0),(303,0),(304,0),(305,0),(306,0),(307\\\\ ,0),(308,0),(309,0),(310,0),(311,0),(312,0),(313,0),(314,0),(315,0),(316,0),(317,0)\\\\ ,(318,0),(319,0),(320,0),(321,0),(322,0),(323,0),(324,0),(325,0),(326,0),(327,0),(328\\\\ ,0),(329,0),(330,0),(331,0),(332,0),(333,0),(334,0),(335,0),(336,0),(337,0),(338,0)\\\\ ,(339,0),(340,0),(341,0),(342,0),(343,0),(344,0),(345,0),(346,0),(347,0),(348,0),(349\\\\ ,0),(350,0),(351,0),(352,0),(353,0),(354,0),(355,0),(356,0),(357,0),(358,0),(359,0)\\\\ ,(360,0),(361,0),(362,0),(363,0),(364,0),(365,0))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b'sixth priority'
    """
    return functions.lookup(x,time_in_lookup_data,lookups_data["rapeseed_tjj_dd"])


def rice_tjj_dd(x):
    """
    Real Name: b'rice tjj dd'
    Original Eqn: b'( [(1,0)-(365,5)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0),\\\\ (12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23,0)\\\\ ,(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35,0\\\\ ),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47,\\\\ 0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94,0),(95\\\\ ,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105,0),(106\\\\ ,0),(107,0),(108,0),(109,0),(110,0),(111,0.0527058),(112,0.0527058),(113,0.0527058)\\\\ ,(114,0.0527058),(115,0.0527058),(116,0.0527058),(117,0.0527058),(118,0.0527058),(119\\\\ ,0.0527058),(120,0.0527058),(121,1.60533),(122,1.60533),(123,1.60533),(124,1.60533)\\\\ ,(125,1.60533),(126,1.60533),(127,1.60533),(128,1.60533),(129,1.60533),(130,1.60533\\\\ ),(131,4.11105),(132,4.11105),(133,4.11105),(134,4.11105),(135,4.11105),(136,4.11105\\\\ ),(137,4.11105),(138,4.11105),(139,4.11105),(140,4.11105),(141,0.915763),(142,0.915763\\\\ ),(143,0.915763),(144,0.915763),(145,0.915763),(146,0.915763),(147,0.915763),(148,0.915763\\\\ ),(149,0.915763),(150,0.915763),(151,0.937724),(152,0.937724),(153,0.937724),(154,0.937724\\\\ ),(155,0.937724),(156,0.937724),(157,0.937724),(158,0.937724),(159,0.937724),(160,0.937724\\\\ ),(161,1.03215),(162,1.03215),(163,1.03215),(164,1.03215),(165,1.03215),(166,1.03215\\\\ ),(167,1.03215),(168,1.03215),(169,1.03215),(170,1.03215),(171,1.03435),(172,1.03435\\\\ ),(173,1.03435),(174,1.03435),(175,1.03435),(176,1.03435),(177,1.03435),(178,1.03435\\\\ ),(179,1.03435),(180,1.03435),(181,0.764234),(182,0.764234),(183,0.764234),(184,0.764234\\\\ ),(185,0.764234),(186,0.764234),(187,0.764234),(188,0.764234),(189,0.764234),(190,0.764234\\\\ ),(191,0.641254),(192,0.641254),(193,0.641254),(194,0.641254),(195,0.641254),(196,0.641254\\\\ ),(197,0.641254),(198,0.641254),(199,0.641254),(200,0.641254),(201,0.920155),(202,0.920155\\\\ ),(203,0.920155),(204,0.920155),(205,0.920155),(206,0.920155),(207,0.920155),(208,0.920155\\\\ ),(209,0.920155),(210,0.920155),(211,1.14855),(212,1.14855),(213,1.14855),(214,1.14855\\\\ ),(215,1.14855),(216,1.14855),(217,1.14855),(218,1.14855),(219,1.14855),(220,1.14855\\\\ ),(221,1.20125),(222,1.20125),(223,1.20125),(224,1.20125),(225,1.20125),(226,1.20125\\\\ ),(227,1.20125),(228,1.20125),(229,1.20125),(230,1.20125),(231,1.12659),(232,1.12659\\\\ ),(233,1.12659),(234,1.12659),(235,1.12659),(236,1.12659),(237,1.12659),(238,1.12659\\\\ ),(239,1.12659),(240,1.12659),(241,0.586352),(242,0.586352),(243,0.586352),(244,0.586352\\\\ ),(245,0.586352),(246,0.586352),(247,0.586352),(248,0.586352),(249,0.586352),(250,0.586352\\\\ ),(251,0.24596),(252,0.24596),(253,0.24596),(254,0.24596),(255,0.24596),(256,0.24596\\\\ ),(257,0.24596),(258,0.24596),(259,0.24596),(260,0.24596),(261,0),(262,0),(263,0),(\\\\ 264,0),(265,0),(266,0),(267,0),(268,0),(269,0),(270,0),(271,0),(272,0),(273,0),(274\\\\ ,0),(275,0),(276,0),(277,0),(278,0),(279,0),(280,0),(281,0),(282,0),(283,0),(284,0)\\\\ ,(285,0),(286,0),(287,0),(288,0),(289,0),(290,0),(291,0),(292,0),(293,0),(294,0),(295\\\\ ,0),(296,0),(297,0),(298,0),(299,0),(300,0),(301,0),(302,0),(303,0),(304,0),(305,0)\\\\ ,(306,0),(307,0),(308,0),(309,0),(310,0),(311,0),(312,0),(313,0),(314,0),(315,0),(316\\\\ ,0),(317,0),(318,0),(319,0),(320,0),(321,0),(322,0),(323,0),(324,0),(325,0),(326,0)\\\\ ,(327,0),(328,0),(329,0),(330,0),(331,0),(332,0),(333,0),(334,0),(335,0),(336,0),(337\\\\ ,0),(338,0),(339,0),(340,0),(341,0),(342,0),(343,0),(344,0),(345,0),(346,0),(347,0)\\\\ ,(348,0),(349,0),(350,0),(351,0),(352,0),(353,0),(354,0),(355,0),(356,0),(357,0),(358\\\\ ,0),(359,0),(360,0),(361,0),(362,0),(363,0),(364,0),(365,0))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b'first priority'
    """
    return functions.lookup(x, time_in_lookup_data,lookups_data["rice_tjj_dd"])


def sorgum_tjj_dd(x):
    """
    Real Name: b'sorgum tjj dd'
    Original Eqn: b'( [(1,0)-(365,0.06)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,\\\\ 0),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23\\\\ ,0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35\\\\ ,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47\\\\ ,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94,0),(95\\\\ ,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105,0),(106\\\\ ,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0),(116,0)\\\\ ,(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126,0),(127\\\\ ,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0),(137,0)\\\\ ,(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147,0),(148\\\\ ,0),(149,0),(150,0),(151,0),(152,0),(153,0),(154,0),(155,0),(156,0),(157,0),(158,0)\\\\ ,(159,0),(160,0),(161,0),(162,0),(163,0),(164,0),(165,0),(166,0),(167,0),(168,0),(169\\\\ ,0),(170,0),(171,0),(172,0),(173,0),(174,0),(175,0),(176,0),(177,0),(178,0),(179,0)\\\\ ,(180,0),(181,0),(182,0),(183,0),(184,0),(185,0),(186,0),(187,0),(188,0),(189,0),(190\\\\ ,0),(191,0),(192,0),(193,0),(194,0),(195,0),(196,0),(197,0),(198,0),(199,0),(200,0)\\\\ ,(201,0),(202,0),(203,0),(204,0.01879),(205,0.01879),(206,0.01879),(207,0.01879),(208\\\\ ,0.01879),(209,0.01879),(210,0.01879),(211,0.01879),(212,0.01879),(213,0.01879),(214\\\\ ,0.01879),(215,0.01196),(216,0.01196),(217,0.01196),(218,0.01196),(219,0.01196),(220\\\\ ,0.01196),(221,0.01196),(222,0.01196),(223,0.01196),(224,0.01196),(225,0.03074),(226\\\\ ,0.03074),(227,0.03074),(228,0.03074),(229,0.03074),(230,0.03074),(231,0.03074),(232\\\\ ,0.03074),(233,0.03074),(234,0.03074),(235,0.01025),(236,0.01025),(237,0.01025),(238\\\\ ,0.01025),(239,0.01025),(240,0.01025),(241,0.01025),(242,0.01025),(243,0.01025),(244\\\\ ,0.01025),(245,0.00512),(246,0.00512),(247,0.00512),(248,0.00512),(249,0.00512),(250\\\\ ,0.00512),(251,0.00512),(252,0.00512),(253,0.00512),(254,0.00512),(255,0.02391),(256\\\\ ,0.02391),(257,0.02391),(258,0.02391),(259,0.02391),(260,0.02391),(261,0.02391),(262\\\\ ,0.02391),(263,0.02391),(264,0.02391),(265,0.02904),(266,0.02904),(267,0.02904),(268\\\\ ,0.02904),(269,0.02904),(270,0.02904),(271,0.02904),(272,0.02904),(273,0.02904),(274\\\\ ,0.02904),(275,0.02904),(276,0.05466),(277,0.05466),(278,0.05466),(279,0.05466),(280\\\\ ,0.05466),(281,0.05466),(282,0.05466),(283,0.05466),(284,0.05466),(285,0.05466),(286\\\\ ,0.0205),(287,0.0205),(288,0.0205),(289,0.0205),(290,0.0205),(291,0.0205),(292,0.0205\\\\ ),(293,0.0205),(294,0.0205),(295,0.0205),(296,0.02391),(297,0.02391),(298,0.02391),\\\\ (299,0.02391),(300,0.02391),(301,0.02391),(302,0.02391),(303,0.02391),(304,0.02391)\\\\ ,(305,0.00683),(306,0.00683),(307,0.00683),(308,0.00683),(309,0.00683),(310,0.00683\\\\ ),(311,0.00683),(312,0.00683),(313,0.00683),(314,0.00683),(315,0),(316,0),(317,0),(\\\\ 318,0),(319,0),(320,0),(321,0),(322,0),(323,0),(324,0),(325,0),(326,0),(327,0),(328\\\\ ,0),(329,0),(330,0),(331,0),(332,0),(333,0),(334,0),(335,0),(336,0),(337,0),(338,0)\\\\ ,(339,0),(340,0),(341,0),(342,0),(343,0),(344,0),(345,0),(346,0),(347,0),(348,0),(349\\\\ ,0),(350,0),(351,0),(352,0),(353,0),(354,0),(355,0),(356,0),(357,0),(358,0),(359,0)\\\\ ,(360,0),(361,0),(362,0),(363,0),(364,0),(365,0))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x,time_in_lookup_data,lookups_data["sorgum_tjj_dd"])


def apple_tjj_dd(x):
    """
    Real Name: b'apple tjj dd'
    Original Eqn: b'( [(1,0)-(365,0.1)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0\\\\ ),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23,\\\\ 0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35\\\\ ,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47\\\\ ,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94,0),(95\\\\ ,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105,0),(106\\\\ ,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0),(116,0)\\\\ ,(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126,0),(127\\\\ ,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0),(137,0)\\\\ ,(138,0),(139,0),(140,0.0132831),(141,0.0132831),(142,0.0132831),(143,0.0132831),(144\\\\ ,0.0132831),(145,0.0132831),(146,0.0132831),(147,0.0132831),(148,0.0132831),(149,0.0132831\\\\ ),(150,0.0596038),(151,0.0596038),(152,0.0596038),(153,0.0596038),(154,0.0596038),(\\\\ 155,0.0596038),(156,0.0596038),(157,0.0596038),(158,0.0596038),(159,0.0596038),(160\\\\ ,0.0653939),(161,0.0653939),(162,0.0653939),(163,0.0653939),(164,0.0653939),(165,0.0653939\\\\ ),(166,0.0653939),(167,0.0653939),(168,0.0653939),(169,0.0653939),(170,0.0650533),(\\\\ 171,0.0650533),(172,0.0650533),(173,0.0650533),(174,0.0650533),(175,0.0650533),(176\\\\ ,0.0650533),(177,0.0650533),(178,0.0650533),(179,0.0650533),(180,0.0231603),(181,0.0231603\\\\ ),(182,0.0231603),(183,0.0231603),(184,0.0231603),(185,0.0231603),(186,0.0231603),(\\\\ 187,0.0231603),(188,0.0231603),(189,0.0231603),(190,0.00272475),(191,0.00272475),(192\\\\ ,0.00272475),(193,0.00272475),(194,0.00272475),(195,0.00272475),(196,0.00272475),(197\\\\ ,0.00272475),(198,0.00272475),(199,0.00272475),(200,0.0364435),(201,0.0364435),(202\\\\ ,0.0364435),(203,0.0364435),(204,0.0364435),(205,0.0364435),(206,0.0364435),(207,0.0364435\\\\ ),(208,0.0364435),(209,0.0364435),(210,0.0827641),(211,0.0827641),(212,0.0827641),(\\\\ 213,0.0827641),(214,0.0827641),(215,0.0827641),(216,0.0827641),(217,0.0827641),(218\\\\ ,0.0827641),(219,0.0827641),(220,0.0940037),(221,0.0940037),(222,0.0940037),(223,0.0940037\\\\ ),(224,0.0940037),(225,0.0940037),(226,0.0940037),(227,0.0940037),(228,0.0940037),(\\\\ 229,0.0940037),(230,0.0974096),(231,0.0974096),(232,0.0974096),(233,0.0974096),(234\\\\ ,0.0974096),(235,0.0974096),(236,0.0974096),(237,0.0974096),(238,0.0974096),(239,0.0974096\\\\ ),(240,0.0439365),(241,0.0439365),(242,0.0439365),(243,0.0439365),(244,0.0439365),(\\\\ 245,0.0439365),(246,0.0439365),(247,0.0439365),(248,0.0439365),(249,0.0439365),(250\\\\ ,0.0180514),(251,0.0180514),(252,0.0180514),(253,0.0180514),(254,0.0180514),(255,0.0180514\\\\ ),(256,0.0180514),(257,0.0180514),(258,0.0180514),(259,0.0180514),(260,0.0262257),(\\\\ 261,0.0262257),(262,0.0262257),(263,0.0262257),(264,0.0262257),(265,0.0262257),(266\\\\ ,0.0262257),(267,0.0262257),(268,0.0262257),(269,0.0262257),(270,0.0425741),(271,0.0425741\\\\ ),(272,0.0425741),(273,0.0425741),(274,0.0425741),(275,0.0425741),(276,0.0425741),(\\\\ 277,0.0425741),(278,0.0425741),(279,0.0425741),(280,0.0487048),(281,0.0487048),(282\\\\ ,0.0487048),(283,0.0487048),(284,0.0487048),(285,0.0487048),(286,0.0487048),(287,0.0487048\\\\ ),(288,0.0487048),(289,0.0487048),(290,0.0286098),(291,0.0286098),(292,0.0286098),(\\\\ 293,0.0286098),(294,0.0286098),(295,0.0286098),(296,0.0286098),(297,0.0286098),(298\\\\ ,0.0286098),(299,0.0286098),(300,0),(301,0),(302,0),(303,0),(304,0),(305,0),(306,0)\\\\ ,(307,0),(308,0),(309,0),(310,0),(311,0),(312,0),(313,0),(314,0),(315,0),(316,0),(317\\\\ ,0),(318,0),(319,0),(320,0),(321,0),(322,0),(323,0),(324,0),(325,0),(326,0),(327,0)\\\\ ,(328,0),(329,0),(330,0),(331,0),(332,0),(333,0),(334,0),(335,0),(336,0),(337,0),(338\\\\ ,0),(339,0),(340,0),(341,0),(342,0),(343,0),(344,0),(345,0),(346,0),(347,0),(348,0)\\\\ ,(349,0),(350,0),(351,0),(352,0),(353,0),(354,0),(355,0),(356,0),(357,0),(358,0),(359\\\\ ,0),(360,0),(361,0),(362,0),(363,0),(364,0),(365,0))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b'third priority'
    """
    return functions.lookup(x, time_in_lookup_data,lookups_data["apple_tjj_dd"])


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
    return functions.lookup(x, time_in_lookup_data,lookups_data["citrud_tjj_dd"])


def apple_zr(x):
    """
    Real Name: b'apple zr'
    Original Eqn: b'( [(1,0)-(365,0.2)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0\\\\ ),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23,\\\\ 0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35\\\\ ,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47\\\\ ,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94,0),(95\\\\ ,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105,0),(106\\\\ ,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0),(116,0)\\\\ ,(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126,0),(127\\\\ ,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0),(137,0)\\\\ ,(138,0),(139,0),(140,0.0162124),(141,0.0162124),(142,0.0162124),(143,0.0162124),(144\\\\ ,0.0162124),(145,0.0162124),(146,0.0162124),(147,0.0162124),(148,0.0162124),(149,0.0162124\\\\ ),(150,0.0727477),(151,0.0727477),(152,0.0727477),(153,0.0727477),(154,0.0727477),(\\\\ 155,0.0727477),(156,0.0727477),(157,0.0727477),(158,0.0727477),(159,0.0727477),(160\\\\ ,0.0798147),(161,0.0798147),(162,0.0798147),(163,0.0798147),(164,0.0798147),(165,0.0798147\\\\ ),(166,0.0798147),(167,0.0798147),(168,0.0798147),(169,0.0798147),(170,0.079399),(171\\\\ ,0.079399),(172,0.079399),(173,0.079399),(174,0.079399),(175,0.079399),(176,0.079399\\\\ ),(177,0.079399),(178,0.079399),(179,0.079399),(180,0.0282677),(181,0.0282677),(182\\\\ ,0.0282677),(183,0.0282677),(184,0.0282677),(185,0.0282677),(186,0.0282677),(187,0.0282677\\\\ ),(188,0.0282677),(189,0.0282677),(190,0.00332561),(191,0.00332561),(192,0.00332561\\\\ ),(193,0.00332561),(194,0.00332561),(195,0.00332561),(196,0.00332561),(197,0.00332561\\\\ ),(198,0.00332561),(199,0.00332561),(200,0.0444801),(201,0.0444801),(202,0.0444801)\\\\ ,(203,0.0444801),(204,0.0444801),(205,0.0444801),(206,0.0444801),(207,0.0444801),(208\\\\ ,0.0444801),(209,0.0444801),(210,0.101015),(211,0.101015),(212,0.101015),(213,0.101015\\\\ ),(214,0.101015),(215,0.101015),(216,0.101015),(217,0.101015),(218,0.101015),(219,0.101015\\\\ ),(220,0.114734),(221,0.114734),(222,0.114734),(223,0.114734),(224,0.114734),(225,0.114734\\\\ ),(226,0.114734),(227,0.114734),(228,0.114734),(229,0.114734),(230,0.118891),(231,0.118891\\\\ ),(232,0.118891),(233,0.118891),(234,0.118891),(235,0.118891),(236,0.118891),(237,0.118891\\\\ ),(238,0.118891),(239,0.118891),(240,0.0536255),(241,0.0536255),(242,0.0536255),(243\\\\ ,0.0536255),(244,0.0536255),(245,0.0536255),(246,0.0536255),(247,0.0536255),(248,0.0536255\\\\ ),(249,0.0536255),(250,0.0220322),(251,0.0220322),(252,0.0220322),(253,0.0220322),(\\\\ 254,0.0220322),(255,0.0220322),(256,0.0220322),(257,0.0220322),(258,0.0220322),(259\\\\ ,0.0220322),(260,0.032009),(261,0.032009),(262,0.032009),(263,0.032009),(264,0.032009\\\\ ),(265,0.032009),(266,0.032009),(267,0.032009),(268,0.032009),(269,0.032009),(270,0.0519627\\\\ ),(271,0.0519627),(272,0.0519627),(273,0.0519627),(274,0.0519627),(275,0.0519627),(\\\\ 276,0.0519627),(277,0.0519627),(278,0.0519627),(279,0.0519627),(280,0.0594453),(281\\\\ ,0.0594453),(282,0.0594453),(283,0.0594453),(284,0.0594453),(285,0.0594453),(286,0.0594453\\\\ ),(287,0.0594453),(288,0.0594453),(289,0.0594453),(290,0.0349189),(291,0.0349189),(\\\\ 292,0.0349189),(293,0.0349189),(294,0.0349189),(295,0.0349189),(296,0.0349189),(297\\\\ ,0.0349189),(298,0.0349189),(299,0.0349189),(300,0),(301,0),(302,0),(303,0),(304,0)\\\\ ,(305,0),(306,0),(307,0),(308,0),(309,0),(310,0),(311,0),(312,0),(313,0),(314,0),(315\\\\ ,0),(316,0),(317,0),(318,0),(319,0),(320,0),(321,0),(322,0),(323,0),(324,0),(325,0)\\\\ ,(326,0),(327,0),(328,0),(329,0),(330,0),(331,0),(332,0),(333,0),(334,0),(335,0),(336\\\\ ,0),(337,0),(338,0),(339,0),(340,0),(341,0),(342,0),(343,0),(344,0),(345,0),(346,0)\\\\ ,(347,0),(348,0),(349,0),(350,0),(351,0),(352,0),(353,0),(354,0),(355,0),(356,0),(357\\\\ ,0),(358,0),(359,0),(360,0),(361,0),(362,0),(363,0),(364,0),(365,0))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b'first priority'
    """
    return functions.lookup(x, time_in_lookup_data,lookups_data["apple_zr"])


def rapeseed_zr(x):
    """
    Real Name: b'rapeseed zr'
    Original Eqn: b'( [(1,0)-(365,7e-005)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11\\\\ ,0),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23\\\\ ,0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35\\\\ ,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47\\\\ ,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94,0),(95\\\\ ,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105,0),(106\\\\ ,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0),(116,0)\\\\ ,(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126,0),(127\\\\ ,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0),(137,0)\\\\ ,(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147,0),(148\\\\ ,0),(149,0),(150,0),(151,0),(152,0),(153,0),(154,5.1e-006),(155,5.1e-006),(156,5.1e-006\\\\ ),(157,5.1e-006),(158,5.1e-006),(159,5.1e-006),(160,5.1e-006),(161,5.1e-006),(162,5.1e-006\\\\ ),(163,5.1e-006),(164,1.02e-005),(165,1.02e-005),(166,1.02e-005),(167,1.02e-005),(168\\\\ ,1.02e-005),(169,1.02e-005),(170,1.02e-005),(171,1.02e-005),(172,1.02e-005),(173,1.02e-005\\\\ ),(174,1.87e-005),(175,1.87e-005),(176,1.87e-005),(177,1.87e-005),(178,1.87e-005),(\\\\ 179,1.87e-005),(180,1.87e-005),(181,1.87e-005),(182,1.87e-005),(183,1.87e-005),(184\\\\ ,4.42e-005),(185,4.42e-005),(186,4.42e-005),(187,4.42e-005),(188,4.42e-005),(189,4.42e-005\\\\ ),(190,4.42e-005),(191,4.42e-005),(192,4.42e-005),(193,4.42e-005),(194,6.46e-005),(\\\\ 195,6.46e-005),(196,6.46e-005),(197,6.46e-005),(198,6.46e-005),(199,6.46e-005),(200\\\\ ,6.46e-005),(201,6.46e-005),(202,6.46e-005),(203,6.46e-005),(204,6.46e-005),(205,5.1e-005\\\\ ),(206,5.1e-005),(207,5.1e-005),(208,5.1e-005),(209,5.1e-005),(210,5.1e-005),(211,5.1e-005\\\\ ),(212,5.1e-005),(213,5.1e-005),(214,5.1e-005),(215,6.8e-005),(216,6.8e-005),(217,6.8e-005\\\\ ),(218,6.8e-005),(219,6.8e-005),(220,6.8e-005),(221,6.8e-005),(222,6.8e-005),(223,6.8e-005\\\\ ),(224,6.8e-005),(225,6.97e-005),(226,6.97e-005),(227,6.97e-005),(228,6.97e-005),(229\\\\ ,6.97e-005),(230,6.97e-005),(231,6.97e-005),(232,6.97e-005),(233,6.97e-005),(234,6.97e-005\\\\ ),(235,6.12e-005),(236,6.12e-005),(237,6.12e-005),(238,6.12e-005),(239,6.12e-005),(\\\\ 240,6.12e-005),(241,6.12e-005),(242,6.12e-005),(243,6.12e-005),(244,6.12e-005),(245\\\\ ,3.91e-005),(246,3.91e-005),(247,3.91e-005),(248,3.91e-005),(249,3.91e-005),(250,3.91e-005\\\\ ),(251,3.91e-005),(252,3.91e-005),(253,3.91e-005),(254,3.91e-005),(255,4.76e-005),(\\\\ 256,4.76e-005),(257,4.76e-005),(258,4.76e-005),(259,4.76e-005),(260,4.76e-005),(261\\\\ ,4.76e-005),(262,4.76e-005),(263,4.76e-005),(264,4.76e-005),(265,3.06e-005),(266,3.06e-005\\\\ ),(267,3.06e-005),(268,3.06e-005),(269,3.06e-005),(270,3.06e-005),(271,3.06e-005),(\\\\ 272,3.06e-005),(273,3.06e-005),(274,3.06e-005),(275,3.06e-005),(276,3.4e-005),(277,\\\\ 3.4e-005),(278,3.4e-005),(279,3.4e-005),(280,3.4e-005),(281,3.4e-005),(282,3.4e-005\\\\ ),(283,3.4e-005),(284,3.4e-005),(285,3.4e-005),(286,0),(287,0),(288,0),(289,0),(290\\\\ ,0),(291,0),(292,0),(293,0),(294,0),(295,0),(296,0),(297,0),(298,0),(299,0),(300,0)\\\\ ,(301,0),(302,0),(303,0),(304,0),(305,0),(306,0),(307,0),(308,0),(309,0),(310,0),(311\\\\ ,0),(312,0),(313,0),(314,0),(315,0),(316,0),(317,0),(318,0),(319,0),(320,0),(321,0)\\\\ ,(322,0),(323,0),(324,0),(325,0),(326,0),(327,0),(328,0),(329,0),(330,0),(331,0),(332\\\\ ,0),(333,0),(334,0),(335,0),(336,0),(337,0),(338,0),(339,0),(340,0),(341,0),(342,0)\\\\ ,(343,0),(344,0),(345,0),(346,0),(347,0),(348,0),(349,0),(350,0),(351,0),(352,0),(353\\\\ ,0),(354,0),(355,0),(356,0),(357,0),(358,0),(359,0),(360,0),(361,0),(362,0),(363,0)\\\\ ,(364,0),(365,0))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, time_in_lookup_data,lookups_data["rapeseed_zr"])


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
    Original Eqn: b'( [(1,0)-(365,0.005)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11\\\\ ,0),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23\\\\ ,0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35\\\\ ,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47\\\\ ,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0.00158983),(92,0.00158983\\\\ ),(93,0.00158983),(94,0.00158983),(95,0.00158983),(96,0.00158983),(97,0.00158983),(\\\\ 98,0.00158983),(99,0.00158983),(100,0.00158983),(101,0.00178253),(102,0.00178253),(\\\\ 103,0.00178253),(104,0.00178253),(105,0.00178253),(106,0.00178253),(107,0.00178253)\\\\ ,(108,0.00178253),(109,0.00178253),(110,0.00178253),(111,0.00205554),(112,0.00205554\\\\ ),(113,0.00205554),(114,0.00205554),(115,0.00205554),(116,0.00205554),(117,0.00205554\\\\ ),(118,0.00205554),(119,0.00205554),(120,0.00205554),(121,0.00232854),(122,0.00232854\\\\ ),(123,0.00232854),(124,0.00232854),(125,0.00232854),(126,0.00232854),(127,0.00232854\\\\ ),(128,0.00232854),(129,0.00232854),(130,0.00232854),(131,0.00260154),(132,0.00260154\\\\ ),(133,0.00260154),(134,0.00260154),(135,0.00260154),(136,0.00260154),(137,0.00260154\\\\ ),(138,0.00260154),(139,0.00260154),(140,0.00260154),(141,0.00317966),(142,0.00317966\\\\ ),(143,0.00317966),(144,0.00317966),(145,0.00317966),(146,0.00317966),(147,0.00317966\\\\ ),(148,0.00317966),(149,0.00317966),(150,0.00317966),(151,0.00322783),(152,0.00322783\\\\ ),(153,0.00322783),(154,0.00322783),(155,0.00322783),(156,0.00322783),(157,0.00322783\\\\ ),(158,0.00322783),(159,0.00322783),(160,0.00322783),(161,0.00354901),(162,0.00354901\\\\ ),(163,0.00354901),(164,0.00354901),(165,0.00354901),(166,0.00354901),(167,0.00354901\\\\ ),(168,0.00354901),(169,0.00354901),(170,0.00354901),(171,0.00354901),(172,0.00354901\\\\ ),(173,0.00354901),(174,0.00354901),(175,0.00354901),(176,0.00354901),(177,0.00354901\\\\ ),(178,0.00354901),(179,0.00354901),(180,0.00354901),(181,0.00155771),(182,0.00155771\\\\ ),(183,0.00155771),(184,0.00155771),(185,0.00155771),(186,0.00155771),(187,0.00155771\\\\ ),(188,0.00155771),(189,0.00155771),(190,0.00155771),(191,0.000642355),(192,0.000642355\\\\ ),(193,0.000642355),(194,0.000642355),(195,0.000642355),(196,0.000642355),(197,0.000642355\\\\ ),(198,0.000642355),(199,0.000642355),(200,0.000642355),(201,0.00245701),(202,0.00245701\\\\ ),(203,0.00245701),(204,0.00245701),(205,0.00245701),(206,0.00245701),(207,0.00245701\\\\ ),(208,0.00245701),(209,0.00245701),(210,0.00245701),(211,0.00427166),(212,0.00427166\\\\ ),(213,0.00427166),(214,0.00427166),(215,0.00427166),(216,0.00427166),(217,0.00427166\\\\ ),(218,0.00427166),(219,0.00427166),(220,0.00427166),(221,0.00448042),(222,0.00448042\\\\ ),(223,0.00448042),(224,0.00448042),(225,0.00448042),(226,0.00448042),(227,0.00448042\\\\ ),(228,0.00448042),(229,0.00448042),(230,0.00448042),(231,0.00430378),(232,0.00430378\\\\ ),(233,0.00430378),(234,0.00430378),(235,0.00430378),(236,0.00430378),(237,0.00430378\\\\ ),(238,0.00430378),(239,0.00430378),(240,0.00430378),(241,0.00158983),(242,0.00158983\\\\ ),(243,0.00158983),(244,0.00158983),(245,0.00158983),(246,0.00158983),(247,0.00158983\\\\ ),(248,0.00158983),(249,0.00158983),(250,0.00158983),(251,0.000224824),(252,0.000224824\\\\ ),(253,0.000224824),(254,0.000224824),(255,0.000224824),(256,0.000224824),(257,0.000224824\\\\ ),(258,0.000224824),(259,0.000224824),(260,0.000224824),(261,0.000465707),(262,0.000465707\\\\ ),(263,0.000465707),(264,0.000465707),(265,0.000465707),(266,0.000465707),(267,0.000465707\\\\ ),(268,0.000465707),(269,0.000465707),(270,0.000465707),(271,0.00114018),(272,0.00114018\\\\ ),(273,0.00114018),(274,0.00114018),(275,0.00114018),(276,0.00114018),(277,0.00114018\\\\ ),(278,0.00114018),(279,0.00114018),(280,0.00114018),(281,0.00138106),(282,0.00138106\\\\ ),(283,0.00138106),(284,0.00138106),(285,0.00138106),(286,0.00138106),(287,0.00138106\\\\ ),(288,0.00138106),(289,0.00138106),(290,0.00138106),(291,0.000337236),(292,0.000337236\\\\ ),(293,0.000337236),(294,0.000337236),(295,0.000337236),(296,0.000337236),(297,0.000337236\\\\ ),(298,0.000337236),(299,0.000337236),(300,0.000337236),(301,0.000337236),(302,0),(\\\\ 303,0),(304,0),(305,0),(306,0),(307,0),(308,0),(309,0),(310,0),(311,0),(312,0),(313\\\\ ,0),(314,0),(315,0),(316,0),(317,0),(318,0),(319,0),(320,0),(321,0),(322,0),(323,0)\\\\ ,(324,0),(325,0),(326,0),(327,0),(328,0),(329,0),(330,0),(331,0),(332,0),(333,0),(334\\\\ ,0),(335,0),(336,0),(337,0),(338,0),(339,0),(340,0),(341,0),(342,0),(343,0),(344,0)\\\\ ,(345,0),(346,0),(347,0),(348,0),(349,0),(350,0),(351,0),(352,0),(353,0),(354,0),(355\\\\ ,0),(356,0),(357,0),(358,0),(359,0),(360,0),(361,0),(362,0),(363,0),(364,0),(365,0)\\\\ )'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x,time_in_lookup_data,lookups_data["citrus_zr"])


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
    Original Eqn: b'( [(1,0)-(365,0.2)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0\\\\ ),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23,\\\\ 0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35\\\\ ,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47\\\\ ,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94,0),(95\\\\ ,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105,0),(106\\\\ ,0),(107,0),(108,0),(109,0),(110,0),(111,0.0023359),(112,0.0023359),(113,0.0023359)\\\\ ,(114,0.0023359),(115,0.0023359),(116,0.0023359),(117,0.0023359),(118,0.0023359),(119\\\\ ,0.0023359),(120,0.0023359),(121,0.0711475),(122,0.0711475),(123,0.0711475),(124,0.0711475\\\\ ),(125,0.0711475),(126,0.0711475),(127,0.0711475),(128,0.0711475),(129,0.0711475),(\\\\ 130,0.0711475),(131,0.1822),(132,0.1822),(133,0.1822),(134,0.1822),(135,0.1822),(136\\\\ ,0.1822),(137,0.1822),(138,0.1822),(139,0.1822),(140,0.1822),(141,0.0405862),(142,0.0405862\\\\ ),(143,0.0405862),(144,0.0405862),(145,0.0405862),(146,0.0405862),(147,0.0405862),(\\\\ 148,0.0405862),(149,0.0405862),(150,0.0405862),(151,0.0415595),(152,0.0415595),(153\\\\ ,0.0415595),(154,0.0415595),(155,0.0415595),(156,0.0415595),(157,0.0415595),(158,0.0415595\\\\ ),(159,0.0415595),(160,0.0415595),(161,0.0457446),(162,0.0457446),(163,0.0457446),(\\\\ 164,0.0457446),(165,0.0457446),(166,0.0457446),(167,0.0457446),(168,0.0457446),(169\\\\ ,0.0457446),(170,0.0457446),(171,0.045842),(172,0.045842),(173,0.045842),(174,0.045842\\\\ ),(175,0.045842),(176,0.045842),(177,0.045842),(178,0.045842),(179,0.045842),(180,0.045842\\\\ ),(181,0.0338705),(182,0.0338705),(183,0.0338705),(184,0.0338705),(185,0.0338705),(\\\\ 186,0.0338705),(187,0.0338705),(188,0.0338705),(189,0.0338705),(190,0.0338705),(191\\\\ ,0.0284201),(192,0.0284201),(193,0.0284201),(194,0.0284201),(195,0.0284201),(196,0.0284201\\\\ ),(197,0.0284201),(198,0.0284201),(199,0.0284201),(200,0.0284201),(201,0.0407809),(\\\\ 202,0.0407809),(203,0.0407809),(204,0.0407809),(205,0.0407809),(206,0.0407809),(207\\\\ ,0.0407809),(208,0.0407809),(209,0.0407809),(210,0.0407809),(211,0.0509031),(212,0.0509031\\\\ ),(213,0.0509031),(214,0.0509031),(215,0.0509031),(216,0.0509031),(217,0.0509031),(\\\\ 218,0.0509031),(219,0.0509031),(220,0.0509031),(221,0.053239),(222,0.053239),(223,0.053239\\\\ ),(224,0.053239),(225,0.053239),(226,0.053239),(227,0.053239),(228,0.053239),(229,0.053239\\\\ ),(230,0.053239),(231,0.0499298),(232,0.0499298),(233,0.0499298),(234,0.0499298),(235\\\\ ,0.0499298),(236,0.0499298),(237,0.0499298),(238,0.0499298),(239,0.0499298),(240,0.0499298\\\\ ),(241,0.0259868),(242,0.0259868),(243,0.0259868),(244,0.0259868),(245,0.0259868),(\\\\ 246,0.0259868),(247,0.0259868),(248,0.0259868),(249,0.0259868),(250,0.0259868),(251\\\\ ,0.0109008),(252,0.0109008),(253,0.0109008),(254,0.0109008),(255,0.0109008),(256,0.0109008\\\\ ),(257,0.0109008),(258,0.0109008),(259,0.0109008),(260,0.0109008),(261,0),(262,0),(\\\\ 263,0),(264,0),(265,0),(266,0),(267,0),(268,0),(269,0),(270,0),(271,0),(272,0),(273\\\\ ,0),(274,0),(275,0),(276,0),(277,0),(278,0),(279,0),(280,0),(281,0),(282,0),(283,0)\\\\ ,(284,0),(285,0),(286,0),(287,0),(288,0),(289,0),(290,0),(291,0),(292,0),(293,0),(294\\\\ ,0),(295,0),(296,0),(297,0),(298,0),(299,0),(300,0),(301,0),(302,0),(303,0),(304,0)\\\\ ,(305,0),(306,0),(307,0),(308,0),(309,0),(310,0),(311,0),(312,0),(313,0),(314,0),(315\\\\ ,0),(316,0),(317,0),(318,0),(319,0),(320,0),(321,0),(322,0),(323,0),(324,0),(325,0)\\\\ ,(326,0),(327,0),(328,0),(329,0),(330,0),(331,0),(332,0),(333,0),(334,0),(335,0),(336\\\\ ,0),(337,0),(338,0),(339,0),(340,0),(341,0),(342,0),(343,0),(344,0),(345,0),(346,0)\\\\ ,(347,0),(348,0),(349,0),(350,0),(351,0),(352,0),(353,0),(354,0),(355,0),(356,0),(357\\\\ ,0),(358,0),(359,0),(360,0),(361,0),(362,0),(363,0),(364,0),(365,0))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, time_in_lookup_data,lookups_data["rice_zr"])


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
    Original Eqn: b'( [(1,0)-(365,0.02)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,\\\\ 0),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23\\\\ ,0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35\\\\ ,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47\\\\ ,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94,0),(95\\\\ ,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105,0),(106\\\\ ,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0),(116,0)\\\\ ,(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126,0),(127\\\\ ,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0),(137,0)\\\\ ,(138,0),(139,0),(140,0.00195454),(141,0.00195454),(142,0.00195454),(143,0.00195454\\\\ ),(144,0.00195454),(145,0.00195454),(146,0.00195454),(147,0.00195454),(148,0.00195454\\\\ ),(149,0.00195454),(150,0.00877035),(151,0.00877035),(152,0.00877035),(153,0.00877035\\\\ ),(154,0.00877035),(155,0.00877035),(156,0.00877035),(157,0.00877035),(158,0.00877035\\\\ ),(159,0.00877035),(160,0.00962233),(161,0.00962233),(162,0.00962233),(163,0.00962233\\\\ ),(164,0.00962233),(165,0.00962233),(166,0.00962233),(167,0.00962233),(168,0.00962233\\\\ ),(169,0.00962233),(170,0.00957222),(171,0.00957222),(172,0.00957222),(173,0.00957222\\\\ ),(174,0.00957222),(175,0.00957222),(176,0.00957222),(177,0.00957222),(178,0.00957222\\\\ ),(179,0.00957222),(180,0.00340791),(181,0.00340791),(182,0.00340791),(183,0.00340791\\\\ ),(184,0.00340791),(185,0.00340791),(186,0.00340791),(187,0.00340791),(188,0.00340791\\\\ ),(189,0.00340791),(190,0.00040093),(191,0.00040093),(192,0.00040093),(193,0.00040093\\\\ ),(194,0.00040093),(195,0.00040093),(196,0.00040093),(197,0.00040093),(198,0.00040093\\\\ ),(199,0.00040093),(200,0.00536245),(201,0.00536245),(202,0.00536245),(203,0.00536245\\\\ ),(204,0.00536245),(205,0.00536245),(206,0.00536245),(207,0.00536245),(208,0.00536245\\\\ ),(209,0.00536245),(210,0.0121783),(211,0.0121783),(212,0.0121783),(213,0.0121783),\\\\ (214,0.0121783),(215,0.0121783),(216,0.0121783),(217,0.0121783),(218,0.0121783),(219\\\\ ,0.0121783),(220,0.0138321),(221,0.0138321),(222,0.0138321),(223,0.0138321),(224,0.0138321\\\\ ),(225,0.0138321),(226,0.0138321),(227,0.0138321),(228,0.0138321),(229,0.0138321),(\\\\ 230,0.0143333),(231,0.0143333),(232,0.0143333),(233,0.0143333),(234,0.0143333),(235\\\\ ,0.0143333),(236,0.0143333),(237,0.0143333),(238,0.0143333),(239,0.0143333),(240,0.006465\\\\ ),(241,0.006465),(242,0.006465),(243,0.006465),(244,0.006465),(245,0.006465),(246,0.006465\\\\ ),(247,0.006465),(248,0.006465),(249,0.006465),(250,0.00265616),(251,0.00265616),(252\\\\ ,0.00265616),(253,0.00265616),(254,0.00265616),(255,0.00265616),(256,0.00265616),(257\\\\ ,0.00265616),(258,0.00265616),(259,0.00265616),(260,0.00385896),(261,0.00385896),(262\\\\ ,0.00385896),(263,0.00385896),(264,0.00385896),(265,0.00385896),(266,0.00385896),(267\\\\ ,0.00385896),(268,0.00385896),(269,0.00385896),(270,0.00626454),(271,0.00626454),(272\\\\ ,0.00626454),(273,0.00626454),(274,0.00626454),(275,0.00626454),(276,0.00626454),(277\\\\ ,0.00626454),(278,0.00626454),(279,0.00626454),(280,0.00716663),(281,0.00716663),(282\\\\ ,0.00716663),(283,0.00716663),(284,0.00716663),(285,0.00716663),(286,0.00716663),(287\\\\ ,0.00716663),(288,0.00716663),(289,0.00716663),(290,0.00420977),(291,0.00420977),(292\\\\ ,0.00420977),(293,0.00420977),(294,0.00420977),(295,0.00420977),(296,0.00420977),(297\\\\ ,0.00420977),(298,0.00420977),(299,0.00420977),(300,0),(301,0),(302,0),(303,0),(304\\\\ ,0),(305,0),(306,0),(307,0),(308,0),(309,0),(310,0),(311,0),(312,0),(313,0),(314,0)\\\\ ,(315,0),(316,0),(317,0),(318,0),(319,0),(320,0),(321,0),(322,0),(323,0),(324,0),(325\\\\ ,0),(326,0),(327,0),(328,0),(329,0),(330,0),(331,0),(332,0),(333,0),(334,0),(335,0)\\\\ ,(336,0),(337,0),(338,0),(339,0),(340,0),(341,0),(342,0),(343,0),(344,0),(345,0),(346\\\\ ,0),(347,0),(348,0),(349,0),(350,0),(351,0),(352,0),(353,0),(354,0),(355,0),(356,0)\\\\ ,(357,0),(358,0),(359,0),(360,0),(361,0),(362,0),(363,0),(364,0),(365,0))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b'second priority'
    """
    return functions.lookup(x, time_in_lookup_data,lookups_data["apple_tj"])


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
    Original Eqn: b'( [(1,0)-(365,5e-005)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11\\\\ ,0),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23\\\\ ,0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35\\\\ ,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47\\\\ ,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94,0),(95\\\\ ,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105,0),(106\\\\ ,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0),(116,0)\\\\ ,(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126,0),(127\\\\ ,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0),(137,0)\\\\ ,(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147,0),(148\\\\ ,0),(149,0),(150,0),(151,0),(152,0),(153,0),(154,0),(155,0),(156,0),(157,0),(158,0)\\\\ ,(159,0),(160,0),(161,0),(162,0),(163,0),(164,0),(165,0),(166,0),(167,0),(168,0),(169\\\\ ,0),(170,0),(171,0),(172,0),(173,0),(174,0),(175,0),(176,0),(177,0),(178,0),(179,0)\\\\ ,(180,0),(181,0),(182,0),(183,0),(184,0),(185,0),(186,0),(187,0),(188,0),(189,0),(190\\\\ ,0),(191,0),(192,0),(193,0),(194,0),(195,0),(196,0),(197,0),(198,0),(199,0),(200,0)\\\\ ,(201,0),(202,0),(203,0),(204,0),(205,2.5974e-005),(206,2.5974e-005),(207,2.5974e-005\\\\ ),(208,2.5974e-005),(209,2.5974e-005),(210,2.5974e-005),(211,2.5974e-005),(212,2.5974e-005\\\\ ),(213,2.5974e-005),(214,2.5974e-005),(215,2.9133e-005),(216,2.9133e-005),(217,2.9133e-005\\\\ ),(218,2.9133e-005),(219,2.9133e-005),(220,2.9133e-005),(221,2.9133e-005),(222,2.9133e-005\\\\ ),(223,2.9133e-005),(224,2.9133e-005),(225,3.0186e-005),(226,3.0186e-005),(227,3.0186e-005\\\\ ),(228,3.0186e-005),(229,3.0186e-005),(230,3.0186e-005),(231,3.0186e-005),(232,3.0186e-005\\\\ ),(233,3.0186e-005),(234,3.0186e-005),(235,3.3345e-005),(236,3.3345e-005),(237,3.3345e-005\\\\ ),(238,3.3345e-005),(239,3.3345e-005),(240,3.3345e-005),(241,3.3345e-005),(242,3.3345e-005\\\\ ),(243,3.3345e-005),(244,3.3345e-005),(245,3.6504e-005),(246,3.6504e-005),(247,3.6504e-005\\\\ ),(248,3.6504e-005),(249,3.6504e-005),(250,3.6504e-005),(251,3.6504e-005),(252,3.6504e-005\\\\ ),(253,3.6504e-005),(254,3.6504e-005),(255,3.8961e-005),(256,3.8961e-005),(257,3.8961e-005\\\\ ),(258,3.8961e-005),(259,3.8961e-005),(260,3.8961e-005),(261,3.8961e-005),(262,3.8961e-005\\\\ ),(263,3.8961e-005),(264,3.8961e-005),(265,4.0365e-005),(266,4.0365e-005),(267,4.0365e-005\\\\ ),(268,4.0365e-005),(269,4.0365e-005),(270,4.0365e-005),(271,4.0365e-005),(272,4.0365e-005\\\\ ),(273,4.0365e-005),(274,4.0365e-005),(275,4.0365e-005),(276,0),(277,0),(278,0),(279\\\\ ,0),(280,0),(281,0),(282,0),(283,0),(284,0),(285,0),(286,0),(287,0),(288,0),(289,0)\\\\ ,(290,0),(291,0),(292,0),(293,0),(294,0),(295,0),(296,0),(297,0),(298,0),(299,0),(300\\\\ ,0),(301,0),(302,0),(303,0),(304,0),(305,0),(306,0),(307,0),(308,0),(309,0),(310,0)\\\\ ,(311,0),(312,0),(313,0),(314,0),(315,0),(316,0),(317,0),(318,0),(319,0),(320,0),(321\\\\ ,0),(322,0),(323,0),(324,0),(325,0),(326,0),(327,0),(328,0),(329,0),(330,0),(331,0)\\\\ ,(332,0),(333,0),(334,0),(335,0),(336,0),(337,0),(338,0),(339,0),(340,0),(341,0),(342\\\\ ,0),(343,0),(344,0),(345,0),(346,0),(347,0),(348,0),(349,0),(350,0),(351,0),(352,0)\\\\ ,(353,0),(354,0),(355,0),(356,0),(357,0),(358,0),(359,0),(360,0),(361,0),(362,0),(363\\\\ ,0),(364,0),(365,0))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b'forth priority'
    """
    return functions.lookup(x, time_in_lookup_data,lookups_data["tomato_tj"])


def rapeseed_tj(x):
    """
    Real Name: b'Rapeseed Tj'
    Original Eqn: b'( [(1,0)-(365,2e-005)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11\\\\ ,0),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23\\\\ ,0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35\\\\ ,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47\\\\ ,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94,0),(95\\\\ ,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105,0),(106\\\\ ,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0),(116,0)\\\\ ,(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126,0),(127\\\\ ,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0),(137,0)\\\\ ,(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147,0),(148\\\\ ,0),(149,0),(150,0),(151,0),(152,0),(153,0),(154,9e-007),(155,9e-007),(156,9e-007),\\\\ (157,9e-007),(158,9e-007),(159,9e-007),(160,9e-007),(161,9e-007),(162,9e-007),(163,\\\\ 9e-007),(164,1.8e-006),(165,1.8e-006),(166,1.8e-006),(167,1.8e-006),(168,1.8e-006),\\\\ (169,1.8e-006),(170,1.8e-006),(171,1.8e-006),(172,1.8e-006),(173,1.8e-006),(174,3.3e-006\\\\ ),(175,3.3e-006),(176,3.3e-006),(177,3.3e-006),(178,3.3e-006),(179,3.3e-006),(180,3.3e-006\\\\ ),(181,3.3e-006),(182,3.3e-006),(183,3.3e-006),(184,7.8e-006),(185,7.8e-006),(186,7.8e-006\\\\ ),(187,7.8e-006),(188,7.8e-006),(189,7.8e-006),(190,7.8e-006),(191,7.8e-006),(192,7.8e-006\\\\ ),(193,7.8e-006),(194,1.14e-005),(195,1.14e-005),(196,1.14e-005),(197,1.14e-005),(198\\\\ ,1.14e-005),(199,1.14e-005),(200,1.14e-005),(201,1.14e-005),(202,1.14e-005),(203,1.14e-005\\\\ ),(204,1.14e-005),(205,9e-006),(206,9e-006),(207,9e-006),(208,9e-006),(209,9e-006),\\\\ (210,9e-006),(211,9e-006),(212,9e-006),(213,9e-006),(214,9e-006),(215,1.2e-005),(216\\\\ ,1.2e-005),(217,1.2e-005),(218,1.2e-005),(219,1.2e-005),(220,1.2e-005),(221,1.2e-005\\\\ ),(222,1.2e-005),(223,1.2e-005),(224,1.2e-005),(225,1.23e-005),(226,1.23e-005),(227\\\\ ,1.23e-005),(228,1.23e-005),(229,1.23e-005),(230,1.23e-005),(231,1.23e-005),(232,1.23e-005\\\\ ),(233,1.23e-005),(234,1.23e-005),(235,1.08e-005),(236,1.08e-005),(237,1.08e-005),(\\\\ 238,1.08e-005),(239,1.08e-005),(240,1.08e-005),(241,1.08e-005),(242,1.08e-005),(243\\\\ ,1.08e-005),(244,1.08e-005),(245,6.9e-006),(246,6.9e-006),(247,6.9e-006),(248,6.9e-006\\\\ ),(249,6.9e-006),(250,6.9e-006),(251,6.9e-006),(252,6.9e-006),(253,6.9e-006),(254,6.9e-006\\\\ ),(255,8.4e-006),(256,8.4e-006),(257,8.4e-006),(258,8.4e-006),(259,8.4e-006),(260,8.4e-006\\\\ ),(261,8.4e-006),(262,8.4e-006),(263,8.4e-006),(264,8.4e-006),(265,5.4e-006),(266,5.4e-006\\\\ ),(267,5.4e-006),(268,5.4e-006),(269,5.4e-006),(270,5.4e-006),(271,5.4e-006),(272,5.4e-006\\\\ ),(273,5.4e-006),(274,5.4e-006),(275,5.4e-006),(276,6e-006),(277,6e-006),(278,6e-006\\\\ ),(279,6e-006),(280,6e-006),(281,6e-006),(282,6e-006),(283,6e-006),(284,6e-006),(285\\\\ ,6e-006),(286,0),(287,0),(288,0),(289,0),(290,0),(291,0),(292,0),(293,0),(294,0),(295\\\\ ,0),(296,0),(297,0),(298,0),(299,0),(300,0),(301,0),(302,0),(303,0),(304,0),(305,0)\\\\ ,(306,0),(307,0),(308,0),(309,0),(310,0),(311,0),(312,0),(313,0),(314,0),(315,0),(316\\\\ ,0),(317,0),(318,0),(319,0),(320,0),(321,0),(322,0),(323,0),(324,0),(325,0),(326,0)\\\\ ,(327,0),(328,0),(329,0),(330,0),(331,0),(332,0),(333,0),(334,0),(335,0),(336,0),(337\\\\ ,0),(338,0),(339,0),(340,0),(341,0),(342,0),(343,0),(344,0),(345,0),(346,0),(347,0)\\\\ ,(348,0),(349,0),(350,0),(351,0),(352,0),(353,0),(354,0),(355,0),(356,0),(357,0),(358\\\\ ,0),(359,0),(360,0),(361,0),(362,0),(363,0),(364,0),(365,0))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b'sixth priority'
    """
    return functions.lookup(x, time_in_lookup_data,lookups_data["rapeseed_tj"])


def rice_tj(x):
    """
    Real Name: b'Rice Tj'
    Original Eqn: b'( [(1,0)-(365,0.2)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0\\\\ ),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23,\\\\ 0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35\\\\ ,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47\\\\ ,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94,0),(95\\\\ ,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105,0),(106\\\\ ,0),(107,0),(108,0),(109,0),(110,0),(111,0.00254357),(112,0.00254357),(113,0.00254357\\\\ ),(114,0.00254357),(115,0.00254357),(116,0.00254357),(117,0.00254357),(118,0.00254357\\\\ ),(119,0.00254357),(120,0.00254357),(121,0.0774729),(122,0.0774729),(123,0.0774729)\\\\ ,(124,0.0774729),(125,0.0774729),(126,0.0774729),(127,0.0774729),(128,0.0774729),(129\\\\ ,0.0774729),(130,0.0774729),(131,0.198398),(132,0.198398),(133,0.198398),(134,0.198398\\\\ ),(135,0.198398),(136,0.198398),(137,0.198398),(138,0.198398),(139,0.198398),(140,0.198398\\\\ ),(141,0.0441945),(142,0.0441945),(143,0.0441945),(144,0.0441945),(145,0.0441945),(\\\\ 146,0.0441945),(147,0.0441945),(148,0.0441945),(149,0.0441945),(150,0.0441945),(151\\\\ ,0.0452544),(152,0.0452544),(153,0.0452544),(154,0.0452544),(155,0.0452544),(156,0.0452544\\\\ ),(157,0.0452544),(158,0.0452544),(159,0.0452544),(160,0.0452544),(161,0.0498116),(\\\\ 162,0.0498116),(163,0.0498116),(164,0.0498116),(165,0.0498116),(166,0.0498116),(167\\\\ ,0.0498116),(168,0.0498116),(169,0.0498116),(170,0.0498116),(171,0.0499176),(172,0.0499176\\\\ ),(173,0.0499176),(174,0.0499176),(175,0.0499176),(176,0.0499176),(177,0.0499176),(\\\\ 178,0.0499176),(179,0.0499176),(180,0.0499176),(181,0.0368818),(182,0.0368818),(183\\\\ ,0.0368818),(184,0.0368818),(185,0.0368818),(186,0.0368818),(187,0.0368818),(188,0.0368818\\\\ ),(189,0.0368818),(190,0.0368818),(191,0.0309468),(192,0.0309468),(193,0.0309468),(\\\\ 194,0.0309468),(195,0.0309468),(196,0.0309468),(197,0.0309468),(198,0.0309468),(199\\\\ ,0.0309468),(200,0.0309468),(201,0.0444065),(202,0.0444065),(203,0.0444065),(204,0.0444065\\\\ ),(205,0.0444065),(206,0.0444065),(207,0.0444065),(208,0.0444065),(209,0.0444065),(\\\\ 210,0.0444065),(211,0.0554286),(212,0.0554286),(213,0.0554286),(214,0.0554286),(215\\\\ ,0.0554286),(216,0.0554286),(217,0.0554286),(218,0.0554286),(219,0.0554286),(220,0.0554286\\\\ ),(221,0.0579722),(222,0.0579722),(223,0.0579722),(224,0.0579722),(225,0.0579722),(\\\\ 226,0.0579722),(227,0.0579722),(228,0.0579722),(229,0.0579722),(230,0.0579722),(231\\\\ ,0.0543688),(232,0.0543688),(233,0.0543688),(234,0.0543688),(235,0.0543688),(236,0.0543688\\\\ ),(237,0.0543688),(238,0.0543688),(239,0.0543688),(240,0.0543688),(241,0.0282972),(\\\\ 242,0.0282972),(243,0.0282972),(244,0.0282972),(245,0.0282972),(246,0.0282972),(247\\\\ ,0.0282972),(248,0.0282972),(249,0.0282972),(250,0.0282972),(251,0.01187),(252,0.01187\\\\ ),(253,0.01187),(254,0.01187),(255,0.01187),(256,0.01187),(257,0.01187),(258,0.01187\\\\ ),(259,0.01187),(260,0.01187),(261,0),(262,0),(263,0),(264,0),(265,0),(266,0),(267,\\\\ 0),(268,0),(269,0),(270,0),(271,0),(272,0),(273,0),(274,0),(275,0),(276,0),(277,0),\\\\ (278,0),(279,0),(280,0),(281,0),(282,0),(283,0),(284,0),(285,0),(286,0),(287,0),(288\\\\ ,0),(289,0),(290,0),(291,0),(292,0),(293,0),(294,0),(295,0),(296,0),(297,0),(298,0)\\\\ ,(299,0),(300,0),(301,0),(302,0),(303,0),(304,0),(305,0),(306,0),(307,0),(308,0),(309\\\\ ,0),(310,0),(311,0),(312,0),(313,0),(314,0),(315,0),(316,0),(317,0),(318,0),(319,0)\\\\ ,(320,0),(321,0),(322,0),(323,0),(324,0),(325,0),(326,0),(327,0),(328,0),(329,0),(330\\\\ ,0),(331,0),(332,0),(333,0),(334,0),(335,0),(336,0),(337,0),(338,0),(339,0),(340,0)\\\\ ,(341,0),(342,0),(343,0),(344,0),(345,0),(346,0),(347,0),(348,0),(349,0),(350,0),(351\\\\ ,0),(352,0),(353,0),(354,0),(355,0),(356,0),(357,0),(358,0),(359,0),(360,0),(361,0)\\\\ ,(362,0),(363,0),(364,0),(365,0))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b'first priority'
    """
    return functions.lookup(x, time_in_lookup_data,lookups_data["rice_tj"])


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
    Original Eqn: b'( [(1,0)-(365,0.002)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11\\\\ ,0),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23\\\\ ,0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35\\\\ ,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47\\\\ ,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0.000385259),(92,0.000385259\\\\ ),(93,0.000385259),(94,0.000385259),(95,0.000385259),(96,0.000385259),(97,0.000385259\\\\ ),(98,0.000385259),(99,0.000385259),(100,0.000385259),(101,0.000431957),(102,0.000431957\\\\ ),(103,0.000431957),(104,0.000431957),(105,0.000431957),(106,0.000431957),(107,0.000431957\\\\ ),(108,0.000431957),(109,0.000431957),(110,0.000431957),(111,0.000498112),(112,0.000498112\\\\ ),(113,0.000498112),(114,0.000498112),(115,0.000498112),(116,0.000498112),(117,0.000498112\\\\ ),(118,0.000498112),(119,0.000498112),(120,0.000498112),(121,0.000564268),(122,0.000564268\\\\ ),(123,0.000564268),(124,0.000564268),(125,0.000564268),(126,0.000564268),(127,0.000564268\\\\ ),(128,0.000564268),(129,0.000564268),(130,0.000564268),(131,0.000630423),(132,0.000630423\\\\ ),(133,0.000630423),(134,0.000630423),(135,0.000630423),(136,0.000630423),(137,0.000630423\\\\ ),(138,0.000630423),(139,0.000630423),(140,0.000630423),(141,0.000770517),(142,0.000770517\\\\ ),(143,0.000770517),(144,0.000770517),(145,0.000770517),(146,0.000770517),(147,0.000770517\\\\ ),(148,0.000770517),(149,0.000770517),(150,0.000770517),(151,0.000782192),(152,0.000782192\\\\ ),(153,0.000782192),(154,0.000782192),(155,0.000782192),(156,0.000782192),(157,0.000782192\\\\ ),(158,0.000782192),(159,0.000782192),(160,0.000782192),(161,0.000860022),(162,0.000860022\\\\ ),(163,0.000860022),(164,0.000860022),(165,0.000860022),(166,0.000860022),(167,0.000860022\\\\ ),(168,0.000860022),(169,0.000860022),(170,0.000860022),(171,0.000860022),(172,0.000860022\\\\ ),(173,0.000860022),(174,0.000860022),(175,0.000860022),(176,0.000860022),(177,0.000860022\\\\ ),(178,0.000860022),(179,0.000860022),(180,0.000860022),(181,0.000377476),(182,0.000377476\\\\ ),(183,0.000377476),(184,0.000377476),(185,0.000377476),(186,0.000377476),(187,0.000377476\\\\ ),(188,0.000377476),(189,0.000377476),(190,0.000377476),(191,0.00015566),(192,0.00015566\\\\ ),(193,0.00015566),(194,0.00015566),(195,0.00015566),(196,0.00015566),(197,0.00015566\\\\ ),(198,0.00015566),(199,0.00015566),(200,0.00015566),(201,0.0005954),(202,0.0005954\\\\ ),(203,0.0005954),(204,0.0005954),(205,0.0005954),(206,0.0005954),(207,0.0005954),(\\\\ 208,0.0005954),(209,0.0005954),(210,0.0005954),(211,0.00103514),(212,0.00103514),(213\\\\ ,0.00103514),(214,0.00103514),(215,0.00103514),(216,0.00103514),(217,0.00103514),(218\\\\ ,0.00103514),(219,0.00103514),(220,0.00103514),(221,0.00108573),(222,0.00108573),(223\\\\ ,0.00108573),(224,0.00108573),(225,0.00108573),(226,0.00108573),(227,0.00108573),(228\\\\ ,0.00108573),(229,0.00108573),(230,0.00108573),(231,0.00104292),(232,0.00104292),(233\\\\ ,0.00104292),(234,0.00104292),(235,0.00104292),(236,0.00104292),(237,0.00104292),(238\\\\ ,0.00104292),(239,0.00104292),(240,0.00104292),(241,0.000385259),(242,0.000385259),\\\\ (243,0.000385259),(244,0.000385259),(245,0.000385259),(246,0.000385259),(247,0.000385259\\\\ ),(248,0.000385259),(249,0.000385259),(250,0.000385259),(251,5.4481e-005),(252,5.4481e-005\\\\ ),(253,5.4481e-005),(254,5.4481e-005),(255,5.4481e-005),(256,5.4481e-005),(257,5.4481e-005\\\\ ),(258,5.4481e-005),(259,5.4481e-005),(260,5.4481e-005),(261,0.000112854),(262,0.000112854\\\\ ),(263,0.000112854),(264,0.000112854),(265,0.000112854),(266,0.000112854),(267,0.000112854\\\\ ),(268,0.000112854),(269,0.000112854),(270,0.000112854),(271,0.000276297),(272,0.000276297\\\\ ),(273,0.000276297),(274,0.000276297),(275,0.000276297),(276,0.000276297),(277,0.000276297\\\\ ),(278,0.000276297),(279,0.000276297),(280,0.000276297),(281,0.000334669),(282,0.000334669\\\\ ),(283,0.000334669),(284,0.000334669),(285,0.000334669),(286,0.000334669),(287,0.000334669\\\\ ),(288,0.000334669),(289,0.000334669),(290,0.000334669),(291,8.1722e-005),(292,8.1722e-005\\\\ ),(293,8.1722e-005),(294,8.1722e-005),(295,8.1722e-005),(296,8.1722e-005),(297,8.1722e-005\\\\ ),(298,8.1722e-005),(299,8.1722e-005),(300,8.1722e-005),(301,8.1722e-005),(302,0),(\\\\ 303,0),(304,0),(305,0),(306,0),(307,0),(308,0),(309,0),(310,0),(311,0),(312,0),(313\\\\ ,0),(314,0),(315,0),(316,0),(317,0),(318,0),(319,0),(320,0),(321,0),(322,0),(323,0)\\\\ ,(324,0),(325,0),(326,0),(327,0),(328,0),(329,0),(330,0),(331,0),(332,0),(333,0),(334\\\\ ,0),(335,0),(336,0),(337,0),(338,0),(339,0),(340,0),(341,0),(342,0),(343,0),(344,0)\\\\ ,(345,0),(346,0),(347,0),(348,0),(349,0),(350,0),(351,0),(352,0),(353,0),(354,0),(355\\\\ ,0),(356,0),(357,0),(358,0),(359,0),(360,0),(361,0),(362,0),(363,0),(364,0),(365,0)\\\\ )'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b'third priority'
    """
    return functions.lookup(x, time_in_lookup_data,lookups_data["citrs_tj"])


def wheat_tj(x):
    """
    Real Name: b'wheat Tj'
    Original Eqn: b'( [(1,0)-(365,8e-006)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11\\\\ ,0),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23\\\\ ,0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35\\\\ ,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47\\\\ ,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94,0),(95\\\\ ,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105,0),(106\\\\ ,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0),(116,0)\\\\ ,(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126,0),(127\\\\ ,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0),(137,0)\\\\ ,(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147,0),(148\\\\ ,0),(149,0),(150,0),(151,0),(152,0),(153,0),(154,0),(155,0),(156,0),(157,0),(158,0)\\\\ ,(159,0),(160,0),(161,0),(162,0),(163,0),(164,0),(165,0),(166,0),(167,0),(168,0),(169\\\\ ,0),(170,0),(171,0),(172,0),(173,0),(174,0),(175,0),(176,0),(177,0),(178,0),(179,0)\\\\ ,(180,0),(181,0),(182,0),(183,0),(184,0),(185,0),(186,0),(187,0),(188,0),(189,0),(190\\\\ ,0),(191,0),(192,0),(193,0),(194,0),(195,5.2e-006),(196,5.2e-006),(197,5.2e-006),(198\\\\ ,5.2e-006),(199,5.2e-006),(200,5.2e-006),(201,5.2e-006),(202,5.2e-006),(203,5.2e-006\\\\ ),(204,5.2e-006),(205,6.24e-006),(206,6.24e-006),(207,6.24e-006),(208,6.24e-006),(209\\\\ ,6.24e-006),(210,6.24e-006),(211,6.24e-006),(212,6.24e-006),(213,6.24e-006),(214,6.24e-006\\\\ ),(215,6.56e-006),(216,6.56e-006),(217,6.56e-006),(218,6.56e-006),(219,6.56e-006),(\\\\ 220,6.56e-006),(221,6.56e-006),(222,6.56e-006),(223,6.56e-006),(224,6.56e-006),(225\\\\ ,6.88e-006),(226,6.88e-006),(227,6.88e-006),(228,6.88e-006),(229,6.88e-006),(230,6.88e-006\\\\ ),(231,6.88e-006),(232,6.88e-006),(233,6.88e-006),(234,6.88e-006),(235,7.6e-006),(236\\\\ ,7.6e-006),(237,7.6e-006),(238,7.6e-006),(239,7.6e-006),(240,7.6e-006),(241,7.6e-006\\\\ ),(242,7.6e-006),(243,7.6e-006),(244,7.6e-006),(245,6.96e-006),(246,6.96e-006),(247\\\\ ,6.96e-006),(248,6.96e-006),(249,6.96e-006),(250,6.96e-006),(251,6.96e-006),(252,6.96e-006\\\\ ),(253,6.96e-006),(254,6.96e-006),(255,5.44e-006),(256,5.44e-006),(257,5.44e-006),(\\\\ 258,5.44e-006),(259,5.44e-006),(260,5.44e-006),(261,5.44e-006),(262,5.44e-006),(263\\\\ ,5.44e-006),(264,5.44e-006),(265,4e-006),(266,4e-006),(267,4e-006),(268,4e-006),(269\\\\ ,4e-006),(270,4e-006),(271,4e-006),(272,4e-006),(273,4e-006),(274,4e-006),(275,4e-006\\\\ ),(276,3.2e-006),(277,3.2e-006),(278,3.2e-006),(279,3.2e-006),(280,3.2e-006),(281,3.2e-006\\\\ ),(282,3.2e-006),(283,3.2e-006),(284,3.2e-006),(285,3.2e-006),(286,0),(287,0),(288,\\\\ 0),(289,0),(290,0),(291,0),(292,0),(293,0),(294,0),(295,0),(296,0),(297,0),(298,0),\\\\ (299,0),(300,0),(301,0),(302,0),(303,0),(304,0),(305,0),(306,0),(307,0),(308,0),(309\\\\ ,0),(310,0),(311,0),(312,0),(313,0),(314,0),(315,0),(316,0),(317,0),(318,0),(319,0)\\\\ ,(320,0),(321,0),(322,0),(323,0),(324,0),(325,0),(326,0),(327,0),(328,0),(329,0),(330\\\\ ,0),(331,0),(332,0),(333,0),(334,0),(335,0),(336,0),(337,0),(338,0),(339,0),(340,0)\\\\ ,(341,0),(342,0),(343,0),(344,0),(345,0),(346,0),(347,0),(348,0),(349,0),(350,0),(351\\\\ ,0),(352,0),(353,0),(354,0),(355,0),(356,0),(357,0),(358,0),(359,0),(360,0),(361,0)\\\\ ,(362,0),(363,0),(364,0),(365,0))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b'fifth priority'
    """
    return functions.lookup(x, time_in_lookup_data,lookups_data["wheat_tj"])


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
    Original Eqn: b'( [(1,0)-(365,0.08)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,\\\\ 0),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23\\\\ ,0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35\\\\ ,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47\\\\ ,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94,0),(95\\\\ ,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105,0),(106\\\\ ,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0),(116,0)\\\\ ,(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126,0),(127\\\\ ,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0),(137,0)\\\\ ,(138,0),(139,0),(140,0.0107357),(141,0.0107357),(142,0.0107357),(143,0.0107357),(144\\\\ ,0.0107357),(145,0.0107357),(146,0.0107357),(147,0.0107357),(148,0.0107357),(149,0.0107357\\\\ ),(150,0.0481732),(151,0.0481732),(152,0.0481732),(153,0.0481732),(154,0.0481732),(\\\\ 155,0.0481732),(156,0.0481732),(157,0.0481732),(158,0.0481732),(159,0.0481732),(160\\\\ ,0.0528529),(161,0.0528529),(162,0.0528529),(163,0.0528529),(164,0.0528529),(165,0.0528529\\\\ ),(166,0.0528529),(167,0.0528529),(168,0.0528529),(169,0.0528529),(170,0.0525776),(\\\\ 171,0.0525776),(172,0.0525776),(173,0.0525776),(174,0.0525776),(175,0.0525776),(176\\\\ ,0.0525776),(177,0.0525776),(178,0.0525776),(179,0.0525776),(180,0.0187187),(181,0.0187187\\\\ ),(182,0.0187187),(183,0.0187187),(184,0.0187187),(185,0.0187187),(186,0.0187187),(\\\\ 187,0.0187187),(188,0.0187187),(189,0.0187187),(190,0.0022022),(191,0.0022022),(192\\\\ ,0.0022022),(193,0.0022022),(194,0.0022022),(195,0.0022022),(196,0.0022022),(197,0.0022022\\\\ ),(198,0.0022022),(199,0.0022022),(200,0.0294545),(201,0.0294545),(202,0.0294545),(\\\\ 203,0.0294545),(204,0.0294545),(205,0.0294545),(206,0.0294545),(207,0.0294545),(208\\\\ ,0.0294545),(209,0.0294545),(210,0.0668919),(211,0.0668919),(212,0.0668919),(213,0.0668919\\\\ ),(214,0.0668919),(215,0.0668919),(216,0.0668919),(217,0.0668919),(218,0.0668919),(\\\\ 219,0.0668919),(220,0.075976),(221,0.075976),(222,0.075976),(223,0.075976),(224,0.075976\\\\ ),(225,0.075976),(226,0.075976),(227,0.075976),(228,0.075976),(229,0.075976),(230,0.0787288\\\\ ),(231,0.0787288),(232,0.0787288),(233,0.0787288),(234,0.0787288),(235,0.0787288),(\\\\ 236,0.0787288),(237,0.0787288),(238,0.0787288),(239,0.0787288),(240,0.0355105),(241\\\\ ,0.0355105),(242,0.0355105),(243,0.0355105),(244,0.0355105),(245,0.0355105),(246,0.0355105\\\\ ),(247,0.0355105),(248,0.0355105),(249,0.0355105),(250,0.0145896),(251,0.0145896),(\\\\ 252,0.0145896),(253,0.0145896),(254,0.0145896),(255,0.0145896),(256,0.0145896),(257\\\\ ,0.0145896),(258,0.0145896),(259,0.0145896),(260,0.0211962),(261,0.0211962),(262,0.0211962\\\\ ),(263,0.0211962),(264,0.0211962),(265,0.0211962),(266,0.0211962),(267,0.0211962),(\\\\ 268,0.0211962),(269,0.0211962),(270,0.0344094),(271,0.0344094),(272,0.0344094),(273\\\\ ,0.0344094),(274,0.0344094),(275,0.0344094),(276,0.0344094),(277,0.0344094),(278,0.0344094\\\\ ),(279,0.0344094),(280,0.0393644),(281,0.0393644),(282,0.0393644),(283,0.0393644),(\\\\ 284,0.0393644),(285,0.0393644),(286,0.0393644),(287,0.0393644),(288,0.0393644),(289\\\\ ,0.0393644),(290,0.0231231),(291,0.0231231),(292,0.0231231),(293,0.0231231),(294,0.0231231\\\\ ),(295,0.0231231),(296,0.0231231),(297,0.0231231),(298,0.0231231),(299,0.0231231),(\\\\ 300,0),(301,0),(302,0),(303,0),(304,0),(305,0),(306,0),(307,0),(308,0),(309,0),(310\\\\ ,0),(311,0),(312,0),(313,0),(314,0),(315,0),(316,0),(317,0),(318,0),(319,0),(320,0)\\\\ ,(321,0),(322,0),(323,0),(324,0),(325,0),(326,0),(327,0),(328,0),(329,0),(330,0),(331\\\\ ,0),(332,0),(333,0),(334,0),(335,0),(336,0),(337,0),(338,0),(339,0),(340,0),(341,0)\\\\ ,(342,0),(343,0),(344,0),(345,0),(346,0),(347,0),(348,0),(349,0),(350,0),(351,0),(352\\\\ ,0),(353,0),(354,0),(355,0),(356,0),(357,0),(358,0),(359,0),(360,0),(361,0),(362,0)\\\\ ,(363,0),(364,0),(365,0))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, time_in_lookup_data,lookups_data["apple"])


def rice(x):
    """
    Real Name: b'rice'
    Original Eqn: b'( [(1,0)-(365,0.4)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0\\\\ ),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23,\\\\ 0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35\\\\ ,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47\\\\ ,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94,0),(95\\\\ ,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105,0),(106\\\\ ,0),(107,0),(108,0),(109,0),(110,0),(111,0.00457608),(112,0.00457608),(113,0.00457608\\\\ ),(114,0.00457608),(115,0.00457608),(116,0.00457608),(117,0.00457608),(118,0.00457608\\\\ ),(119,0.00457608),(120,0.00457608),(121,0.13938),(122,0.13938),(123,0.13938),(124,\\\\ 0.13938),(125,0.13938),(126,0.13938),(127,0.13938),(128,0.13938),(129,0.13938),(130\\\\ ,0.13938),(131,0.356935),(132,0.356935),(133,0.356935),(134,0.356935),(135,0.356935\\\\ ),(136,0.356935),(137,0.356935),(138,0.356935),(139,0.356935),(140,0.356935),(141,0.0795095\\\\ ),(142,0.0795095),(143,0.0795095),(144,0.0795095),(145,0.0795095),(146,0.0795095),(\\\\ 147,0.0795095),(148,0.0795095),(149,0.0795095),(150,0.0795095),(151,0.0814162),(152\\\\ ,0.0814162),(153,0.0814162),(154,0.0814162),(155,0.0814162),(156,0.0814162),(157,0.0814162\\\\ ),(158,0.0814162),(159,0.0814162),(160,0.0814162),(161,0.089615),(162,0.089615),(163\\\\ ,0.089615),(164,0.089615),(165,0.089615),(166,0.089615),(167,0.089615),(168,0.089615\\\\ ),(169,0.089615),(170,0.089615),(171,0.0898056),(172,0.0898056),(173,0.0898056),(174\\\\ ,0.0898056),(175,0.0898056),(176,0.0898056),(177,0.0898056),(178,0.0898056),(179,0.0898056\\\\ ),(180,0.0898056),(181,0.0663532),(182,0.0663532),(183,0.0663532),(184,0.0663532),(\\\\ 185,0.0663532),(186,0.0663532),(187,0.0663532),(188,0.0663532),(189,0.0663532),(190\\\\ ,0.0663532),(191,0.0556757),(192,0.0556757),(193,0.0556757),(194,0.0556757),(195,0.0556757\\\\ ),(196,0.0556757),(197,0.0556757),(198,0.0556757),(199,0.0556757),(200,0.0556757),(\\\\ 201,0.0798908),(202,0.0798908),(203,0.0798908),(204,0.0798908),(205,0.0798908),(206\\\\ ,0.0798908),(207,0.0798908),(208,0.0798908),(209,0.0798908),(210,0.0798908),(211,0.0997205\\\\ ),(212,0.0997205),(213,0.0997205),(214,0.0997205),(215,0.0997205),(216,0.0997205),(\\\\ 217,0.0997205),(218,0.0997205),(219,0.0997205),(220,0.0997205),(221,0.104297),(222,\\\\ 0.104297),(223,0.104297),(224,0.104297),(225,0.104297),(226,0.104297),(227,0.104297\\\\ ),(228,0.104297),(229,0.104297),(230,0.104297),(231,0.0978138),(232,0.0978138),(233\\\\ ,0.0978138),(234,0.0978138),(235,0.0978138),(236,0.0978138),(237,0.0978138),(238,0.0978138\\\\ ),(239,0.0978138),(240,0.0978138),(241,0.0509089),(242,0.0509089),(243,0.0509089),(\\\\ 244,0.0509089),(245,0.0509089),(246,0.0509089),(247,0.0509089),(248,0.0509089),(249\\\\ ,0.0509089),(250,0.0509089),(251,0.0213551),(252,0.0213551),(253,0.0213551),(254,0.0213551\\\\ ),(255,0.0213551),(256,0.0213551),(257,0.0213551),(258,0.0213551),(259,0.0213551),(\\\\ 260,0.0213551),(261,0),(262,0),(263,0),(264,0),(265,0),(266,0),(267,0),(268,0),(269\\\\ ,0),(270,0),(271,0),(272,0),(273,0),(274,0),(275,0),(276,0),(277,0),(278,0),(279,0)\\\\ ,(280,0),(281,0),(282,0),(283,0),(284,0),(285,0),(286,0),(287,0),(288,0),(289,0),(290\\\\ ,0),(291,0),(292,0),(293,0),(294,0),(295,0),(296,0),(297,0),(298,0),(299,0),(300,0)\\\\ ,(301,0),(302,0),(303,0),(304,0),(305,0),(306,0),(307,0),(308,0),(309,0),(310,0),(311\\\\ ,0),(312,0),(313,0),(314,0),(315,0),(316,0),(317,0),(318,0),(319,0),(320,0),(321,0)\\\\ ,(322,0),(323,0),(324,0),(325,0),(326,0),(327,0),(328,0),(329,0),(330,0),(331,0),(332\\\\ ,0),(333,0),(334,0),(335,0),(336,0),(337,0),(338,0),(339,0),(340,0),(341,0),(342,0)\\\\ ,(343,0),(344,0),(345,0),(346,0),(347,0),(348,0),(349,0),(350,0),(351,0),(352,0),(353\\\\ ,0),(354,0),(355,0),(356,0),(357,0),(358,0),(359,0),(360,0),(361,0),(362,0),(363,0)\\\\ ,(364,0),(365,0))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x,time_in_lookup_data,lookups_data["rice"])


def chickpea(x):
    """
    Real Name: b'chickpea'
    Original Eqn: b'( [(1,0)-(365,0.0003)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11\\\\ ,0),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23\\\\ ,0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35\\\\ ,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47\\\\ ,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94,0),(95\\\\ ,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105,0),(106\\\\ ,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0),(116,0)\\\\ ,(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126,0),(127\\\\ ,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0),(137,0)\\\\ ,(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,1.83e-005),(145,1.83e-005),(146\\\\ ,1.83e-005),(147,1.83e-005),(148,1.83e-005),(149,1.83e-005),(150,1.83e-005),(151,1.83e-005\\\\ ),(152,1.83e-005),(153,1.83e-005),(154,1.83e-005),(155,1.83e-005),(156,1.83e-005),(\\\\ 157,1.83e-005),(158,1.83e-005),(159,1.83e-005),(160,1.83e-005),(161,1.83e-005),(162\\\\ ,1.83e-005),(163,1.83e-005),(164,6.1e-005),(165,6.1e-005),(166,6.1e-005),(167,6.1e-005\\\\ ),(168,6.1e-005),(169,6.1e-005),(170,6.1e-005),(171,6.1e-005),(172,6.1e-005),(173,6.1e-005\\\\ ),(174,0.0001281),(175,0.0001281),(176,0.0001281),(177,0.0001281),(178,0.0001281),(\\\\ 179,0.0001281),(180,0.0001281),(181,0.0001281),(182,0.0001281),(183,0.0001281),(184\\\\ ,0.0002318),(185,0.0002318),(186,0.0002318),(187,0.0002318),(188,0.0002318),(189,0.0002318\\\\ ),(190,0.0002318),(191,0.0002318),(192,0.0002318),(193,0.0002318),(194,0.0002928),(\\\\ 195,0.0002928),(196,0.0002928),(197,0.0002928),(198,0.0002928),(199,0.0002928),(200\\\\ ,0.0002928),(201,0.0002928),(202,0.0002928),(203,0.0002928),(204,0.0001098),(205,0.0001098\\\\ ),(206,0.0001098),(207,0.0001098),(208,0.0001098),(209,0.0001098),(210,0.0001098),(\\\\ 211,0.0001098),(212,0.0001098),(213,0.0001098),(214,0),(215,0),(216,0),(217,0),(218\\\\ ,0),(219,0),(220,0),(221,0),(222,0),(223,0),(224,0),(225,0),(226,0),(227,0),(228,0)\\\\ ,(229,0),(230,0),(231,0),(232,0),(233,0),(234,0),(235,0),(236,0),(237,0),(238,0),(239\\\\ ,0),(240,0),(241,0),(242,0),(243,0),(244,0),(245,0),(246,0),(247,0),(248,0),(249,0)\\\\ ,(250,0),(251,0),(252,0),(253,0),(254,0),(255,0),(256,0),(257,0),(258,0),(259,0),(260\\\\ ,0),(261,0),(262,0),(263,0),(264,0),(265,0),(266,0),(267,0),(268,0),(269,0),(270,0)\\\\ ,(271,0),(272,0),(273,0),(274,0),(275,0),(276,0),(277,0),(278,0),(279,0),(280,0),(281\\\\ ,0),(282,0),(283,0),(284,0),(285,0),(286,0),(287,0),(288,0),(289,0),(290,0),(291,0)\\\\ ,(292,0),(293,0),(294,0),(295,0),(296,0),(297,0),(298,0),(299,0),(300,0),(301,0),(302\\\\ ,0),(303,0),(304,0),(305,0),(306,0),(307,0),(308,0),(309,0),(310,0),(311,0),(312,0)\\\\ ,(313,0),(314,0),(315,0),(316,0),(317,0),(318,0),(319,0),(320,0),(321,0),(322,0),(323\\\\ ,0),(324,0),(325,0),(326,0),(327,0),(328,0),(329,0),(330,0),(331,0),(332,0),(333,0)\\\\ ,(334,0),(335,0),(336,0),(337,0),(338,0),(339,0),(340,0),(341,0),(342,0),(343,0),(344\\\\ ,0),(345,0),(346,0),(347,0),(348,0),(349,0),(350,0),(351,0),(352,0),(353,0),(354,0)\\\\ ,(355,0),(356,0),(357,0),(358,0),(359,0),(360,0),(361,0),(362,0),(363,0),(364,0),(365\\\\ ,0))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x,time_in_lookup_data,lookups_data["chickpea"])


def citrus(x):
    """
    Real Name: b'citrus'
    Original Eqn: b'( [(1,0)-(365,0.003)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11\\\\ ,0),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23\\\\ ,0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35\\\\ ,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47\\\\ ,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0.000943074),(92,0.000943074\\\\ ),(93,0.000943074),(94,0.000943074),(95,0.000943074),(96,0.000943074),(97,0.000943074\\\\ ),(98,0.000943074),(99,0.000943074),(100,0.000943074),(101,0.00105739),(102,0.00105739\\\\ ),(103,0.00105739),(104,0.00105739),(105,0.00105739),(106,0.00105739),(107,0.00105739\\\\ ),(108,0.00105739),(109,0.00105739),(110,0.00105739),(111,0.00121933),(112,0.00121933\\\\ ),(113,0.00121933),(114,0.00121933),(115,0.00121933),(116,0.00121933),(117,0.00121933\\\\ ),(118,0.00121933),(119,0.00121933),(120,0.00121933),(121,0.00138127),(122,0.00138127\\\\ ),(123,0.00138127),(124,0.00138127),(125,0.00138127),(126,0.00138127),(127,0.00138127\\\\ ),(128,0.00138127),(129,0.00138127),(130,0.00138127),(131,0.00154321),(132,0.00154321\\\\ ),(133,0.00154321),(134,0.00154321),(135,0.00154321),(136,0.00154321),(137,0.00154321\\\\ ),(138,0.00154321),(139,0.00154321),(140,0.00154321),(141,0.00188615),(142,0.00188615\\\\ ),(143,0.00188615),(144,0.00188615),(145,0.00188615),(146,0.00188615),(147,0.00188615\\\\ ),(148,0.00188615),(149,0.00188615),(150,0.00188615),(151,0.00191473),(152,0.00191473\\\\ ),(153,0.00191473),(154,0.00191473),(155,0.00191473),(156,0.00191473),(157,0.00191473\\\\ ),(158,0.00191473),(159,0.00191473),(160,0.00191473),(161,0.00210525),(162,0.00210525\\\\ ),(163,0.00210525),(164,0.00210525),(165,0.00210525),(166,0.00210525),(167,0.00210525\\\\ ),(168,0.00210525),(169,0.00210525),(170,0.00210525),(171,0.00210525),(172,0.00210525\\\\ ),(173,0.00210525),(174,0.00210525),(175,0.00210525),(176,0.00210525),(177,0.00210525\\\\ ),(178,0.00210525),(179,0.00210525),(180,0.00210525),(181,0.000924022),(182,0.000924022\\\\ ),(183,0.000924022),(184,0.000924022),(185,0.000924022),(186,0.000924022),(187,0.000924022\\\\ ),(188,0.000924022),(189,0.000924022),(190,0.000924022),(191,0.00038104),(192,0.00038104\\\\ ),(193,0.00038104),(194,0.00038104),(195,0.00038104),(196,0.00038104),(197,0.00038104\\\\ ),(198,0.00038104),(199,0.00038104),(200,0.00038104),(201,0.00145748),(202,0.00145748\\\\ ),(203,0.00145748),(204,0.00145748),(205,0.00145748),(206,0.00145748),(207,0.00145748\\\\ ),(208,0.00145748),(209,0.00145748),(210,0.00145748),(211,0.00253392),(212,0.00253392\\\\ ),(213,0.00253392),(214,0.00253392),(215,0.00253392),(216,0.00253392),(217,0.00253392\\\\ ),(218,0.00253392),(219,0.00253392),(220,0.00253392),(221,0.00265775),(222,0.00265775\\\\ ),(223,0.00265775),(224,0.00265775),(225,0.00265775),(226,0.00265775),(227,0.00265775\\\\ ),(228,0.00265775),(229,0.00265775),(230,0.00265775),(231,0.00255297),(232,0.00255297\\\\ ),(233,0.00255297),(234,0.00255297),(235,0.00255297),(236,0.00255297),(237,0.00255297\\\\ ),(238,0.00255297),(239,0.00255297),(240,0.00255297),(241,0.000943074),(242,0.000943074\\\\ ),(243,0.000943074),(244,0.000943074),(245,0.000943074),(246,0.000943074),(247,0.000943074\\\\ ),(248,0.000943074),(249,0.000943074),(250,0.000943074),(251,0.000133364),(252,0.000133364\\\\ ),(253,0.000133364),(254,0.000133364),(255,0.000133364),(256,0.000133364),(257,0.000133364\\\\ ),(258,0.000133364),(259,0.000133364),(260,0.000133364),(261,0.000276254),(262,0.000276254\\\\ ),(263,0.000276254),(264,0.000276254),(265,0.000276254),(266,0.000276254),(267,0.000276254\\\\ ),(268,0.000276254),(269,0.000276254),(270,0.000276254),(271,0.000676346),(272,0.000676346\\\\ ),(273,0.000676346),(274,0.000676346),(275,0.000676346),(276,0.000676346),(277,0.000676346\\\\ ),(278,0.000676346),(279,0.000676346),(280,0.000676346),(281,0.000819236),(282,0.000819236\\\\ ),(283,0.000819236),(284,0.000819236),(285,0.000819236),(286,0.000819236),(287,0.000819236\\\\ ),(288,0.000819236),(289,0.000819236),(290,0.000819236),(291,0.000200046),(292,0.000200046\\\\ ),(293,0.000200046),(294,0.000200046),(295,0.000200046),(296,0.000200046),(297,0.000200046\\\\ ),(298,0.000200046),(299,0.000200046),(300,0.000200046),(301,0.000200046),(302,0),(\\\\ 303,0),(304,0),(305,0),(306,0),(307,0),(308,0),(309,0),(310,0),(311,0),(312,0),(313\\\\ ,0),(314,0),(315,0),(316,0),(317,0),(318,0),(319,0),(320,0),(321,0),(322,0),(323,0)\\\\ ,(324,0),(325,0),(326,0),(327,0),(328,0),(329,0),(330,0),(331,0),(332,0),(333,0),(334\\\\ ,0),(335,0),(336,0),(337,0),(338,0),(339,0),(340,0),(341,0),(342,0),(343,0),(344,0)\\\\ ,(345,0),(346,0),(347,0),(348,0),(349,0),(350,0),(351,0),(352,0),(353,0),(354,0),(355\\\\ ,0),(356,0),(357,0),(358,0),(359,0),(360,0),(361,0),(362,0),(363,0),(364,0),(365,0)\\\\ )'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, time_in_lookup_data,lookups_data["citrus"])


def rapeseed(x):
    """
    Real Name: b'rapeseed'
    Original Eqn: b'( [(1,0)-(365,0.0006)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11\\\\ ,0),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23\\\\ ,0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35\\\\ ,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47\\\\ ,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94,0),(95\\\\ ,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105,0),(106\\\\ ,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0),(116,0)\\\\ ,(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126,0),(127\\\\ ,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0),(137,0)\\\\ ,(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147,0),(148\\\\ ,0),(149,0),(150,0),(151,0),(152,0),(153,0),(154,3.9e-005),(155,3.9e-005),(156,3.9e-005\\\\ ),(157,3.9e-005),(158,3.9e-005),(159,3.9e-005),(160,3.9e-005),(161,3.9e-005),(162,3.9e-005\\\\ ),(163,3.9e-005),(164,7.8e-005),(165,7.8e-005),(166,7.8e-005),(167,7.8e-005),(168,7.8e-005\\\\ ),(169,7.8e-005),(170,7.8e-005),(171,7.8e-005),(172,7.8e-005),(173,7.8e-005),(174,0.000143\\\\ ),(175,0.000143),(176,0.000143),(177,0.000143),(178,0.000143),(179,0.000143),(180,0.000143\\\\ ),(181,0.000143),(182,0.000143),(183,0.000143),(184,0.000338),(185,0.000338),(186,0.000338\\\\ ),(187,0.000338),(188,0.000338),(189,0.000338),(190,0.000338),(191,0.000338),(192,0.000338\\\\ ),(193,0.000338),(194,0.000494),(195,0.000494),(196,0.000494),(197,0.000494),(198,0.000494\\\\ ),(199,0.000494),(200,0.000494),(201,0.000494),(202,0.000494),(203,0.000494),(204,0.000494\\\\ ),(205,0.00039),(206,0.00039),(207,0.00039),(208,0.00039),(209,0.00039),(210,0.00039\\\\ ),(211,0.00039),(212,0.00039),(213,0.00039),(214,0.00039),(215,0.00052),(216,0.00052\\\\ ),(217,0.00052),(218,0.00052),(219,0.00052),(220,0.00052),(221,0.00052),(222,0.00052\\\\ ),(223,0.00052),(224,0.00052),(225,0.000533),(226,0.000533),(227,0.000533),(228,0.000533\\\\ ),(229,0.000533),(230,0.000533),(231,0.000533),(232,0.000533),(233,0.000533),(234,0.000533\\\\ ),(235,0.000468),(236,0.000468),(237,0.000468),(238,0.000468),(239,0.000468),(240,0.000468\\\\ ),(241,0.000468),(242,0.000468),(243,0.000468),(244,0.000468),(245,0.000299),(246,0.000299\\\\ ),(247,0.000299),(248,0.000299),(249,0.000299),(250,0.000299),(251,0.000299),(252,0.000299\\\\ ),(253,0.000299),(254,0.000299),(255,0.000364),(256,0.000364),(257,0.000364),(258,0.000364\\\\ ),(259,0.000364),(260,0.000364),(261,0.000364),(262,0.000364),(263,0.000364),(264,0.000364\\\\ ),(265,0.000234),(266,0.000234),(267,0.000234),(268,0.000234),(269,0.000234),(270,0.000234\\\\ ),(271,0.000234),(272,0.000234),(273,0.000234),(274,0.000234),(275,0.000234),(276,0.00026\\\\ ),(277,0.00026),(278,0.00026),(279,0.00026),(280,0.00026),(281,0.00026),(282,0.00026\\\\ ),(283,0.00026),(284,0.00026),(285,0.00026),(286,0),(287,0),(288,0),(289,0),(290,0)\\\\ ,(291,0),(292,0),(293,0),(294,0),(295,0),(296,0),(297,0),(298,0),(299,0),(300,0),(301\\\\ ,0),(302,0),(303,0),(304,0),(305,0),(306,0),(307,0),(308,0),(309,0),(310,0),(311,0)\\\\ ,(312,0),(313,0),(314,0),(315,0),(316,0),(317,0),(318,0),(319,0),(320,0),(321,0),(322\\\\ ,0),(323,0),(324,0),(325,0),(326,0),(327,0),(328,0),(329,0),(330,0),(331,0),(332,0)\\\\ ,(333,0),(334,0),(335,0),(336,0),(337,0),(338,0),(339,0),(340,0),(341,0),(342,0),(343\\\\ ,0),(344,0),(345,0),(346,0),(347,0),(348,0),(349,0),(350,0),(351,0),(352,0),(353,0)\\\\ ,(354,0),(355,0),(356,0),(357,0),(358,0),(359,0),(360,0),(361,0),(362,0),(363,0),(364\\\\ ,0),(365,0))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, time_in_lookup_data,lookups_data["rapeseed"])


def grainmaize(x):
    """
    Real Name: b'grainmaize'
    Original Eqn: b'( [(1,0)-(365,4e-005)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11\\\\ ,0),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23\\\\ ,0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35\\\\ ,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47\\\\ ,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94,0),(95\\\\ ,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105,0),(106\\\\ ,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0),(116,0)\\\\ ,(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126,0),(127\\\\ ,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0),(137,0)\\\\ ,(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147,0),(148\\\\ ,0),(149,0),(150,0),(151,0),(152,0),(153,0),(154,0),(155,0),(156,0),(157,0),(158,0)\\\\ ,(159,0),(160,0),(161,0),(162,0),(163,0),(164,0),(165,0),(166,0),(167,0),(168,0),(169\\\\ ,0),(170,0),(171,0),(172,0),(173,0),(174,0),(175,0),(176,0),(177,0),(178,0),(179,0)\\\\ ,(180,0),(181,0),(182,0),(183,0),(184,0),(185,0),(186,0),(187,0),(188,0),(189,0),(190\\\\ ,0),(191,0),(192,0),(193,0),(194,0),(195,0),(196,0),(197,0),(198,0),(199,0),(200,0)\\\\ ,(201,0),(202,0),(203,0),(204,1.1e-005),(205,1.1e-005),(206,1.1e-005),(207,1.1e-005\\\\ ),(208,1.1e-005),(209,1.1e-005),(210,1.1e-005),(211,1.1e-005),(212,1.1e-005),(213,1.1e-005\\\\ ),(214,1.1e-005),(215,7e-006),(216,7e-006),(217,7e-006),(218,7e-006),(219,7e-006),(\\\\ 220,7e-006),(221,7e-006),(222,7e-006),(223,7e-006),(224,7e-006),(225,1.8e-005),(226\\\\ ,1.8e-005),(227,1.8e-005),(228,1.8e-005),(229,1.8e-005),(230,1.8e-005),(231,1.8e-005\\\\ ),(232,1.8e-005),(233,1.8e-005),(234,1.8e-005),(235,6e-006),(236,6e-006),(237,6e-006\\\\ ),(238,6e-006),(239,6e-006),(240,6e-006),(241,6e-006),(242,6e-006),(243,6e-006),(244\\\\ ,6e-006),(245,3e-006),(246,3e-006),(247,3e-006),(248,3e-006),(249,3e-006),(250,3e-006\\\\ ),(251,3e-006),(252,3e-006),(253,3e-006),(254,3e-006),(255,1.4e-005),(256,1.4e-005)\\\\ ,(257,1.4e-005),(258,1.4e-005),(259,1.4e-005),(260,1.4e-005),(261,1.4e-005),(262,1.4e-005\\\\ ),(263,1.4e-005),(264,1.4e-005),(265,1.7e-005),(266,1.7e-005),(267,1.7e-005),(268,1.7e-005\\\\ ),(269,1.7e-005),(270,1.7e-005),(271,1.7e-005),(272,1.7e-005),(273,1.7e-005),(274,1.7e-005\\\\ ),(275,1.7e-005),(276,3.2e-005),(277,3.2e-005),(278,3.2e-005),(279,3.2e-005),(280,3.2e-005\\\\ ),(281,3.2e-005),(282,3.2e-005),(283,3.2e-005),(284,3.2e-005),(285,3.2e-005),(286,1.2e-005\\\\ ),(287,1.2e-005),(288,1.2e-005),(289,1.2e-005),(290,1.2e-005),(291,1.2e-005),(292,1.2e-005\\\\ ),(293,1.2e-005),(294,1.2e-005),(295,1.2e-005),(296,1.4e-005),(297,1.4e-005),(298,1.4e-005\\\\ ),(299,1.4e-005),(300,1.4e-005),(301,1.4e-005),(302,1.4e-005),(303,1.4e-005),(304,1.4e-005\\\\ ),(305,4e-006),(306,4e-006),(307,4e-006),(308,4e-006),(309,4e-006),(310,4e-006),(311\\\\ ,4e-006),(312,4e-006),(313,4e-006),(314,4e-006),(315,0),(316,0),(317,0),(318,0),(319\\\\ ,0),(320,0),(321,0),(322,0),(323,0),(324,0),(325,0),(326,0),(327,0),(328,0),(329,0)\\\\ ,(330,0),(331,0),(332,0),(333,0),(334,0),(335,0),(336,0),(337,0),(338,0),(339,0),(340\\\\ ,0),(341,0),(342,0),(343,0),(344,0),(345,0),(346,0),(347,0),(348,0),(349,0),(350,0)\\\\ ,(351,0),(352,0),(353,0),(354,0),(355,0),(356,0),(357,0),(358,0),(359,0),(360,0),(361\\\\ ,0),(362,0),(363,0),(364,0),(365,0))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x,time_in_lookup_data,lookups_data["grainmaize"])


def tomato(x):
    """
    Real Name: b'tomato'
    Original Eqn: b'( [(1,0)-(365,0.04)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,\\\\ 0),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23\\\\ ,0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35\\\\ ,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47\\\\ ,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94,0),(95\\\\ ,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105,0),(106\\\\ ,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0),(116,0)\\\\ ,(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126,0),(127\\\\ ,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0),(137,0)\\\\ ,(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147,0),(148\\\\ ,0),(149,0),(150,0),(151,0),(152,0),(153,0),(154,0),(155,0),(156,0),(157,0),(158,0)\\\\ ,(159,0),(160,0),(161,0),(162,0),(163,0),(164,0),(165,0),(166,0),(167,0),(168,0),(169\\\\ ,0),(170,0),(171,0),(172,0),(173,0),(174,0),(175,0),(176,0),(177,0),(178,0),(179,0)\\\\ ,(180,0),(181,0),(182,0),(183,0),(184,0),(185,0),(186,0),(187,0),(188,0),(189,0),(190\\\\ ,0),(191,0),(192,0),(193,0),(194,0),(195,0),(196,0),(197,0),(198,0),(199,0),(200,0)\\\\ ,(201,0),(202,0),(203,0),(204,0),(205,0.0205938),(206,0.0205938),(207,0.0205938),(208\\\\ ,0.0205938),(209,0.0205938),(210,0.0205938),(211,0.0205938),(212,0.0205938),(213,0.0205938\\\\ ),(214,0.0205938),(215,0.0230985),(216,0.0230985),(217,0.0230985),(218,0.0230985),(\\\\ 219,0.0230985),(220,0.0230985),(221,0.0230985),(222,0.0230985),(223,0.0230985),(224\\\\ ,0.0230985),(225,0.0239334),(226,0.0239334),(227,0.0239334),(228,0.0239334),(229,0.0239334\\\\ ),(230,0.0239334),(231,0.0239334),(232,0.0239334),(233,0.0239334),(234,0.0239334),(\\\\ 235,0.026438),(236,0.026438),(237,0.026438),(238,0.026438),(239,0.026438),(240,0.026438\\\\ ),(241,0.026438),(242,0.026438),(243,0.026438),(244,0.026438),(245,0.0289427),(246,\\\\ 0.0289427),(247,0.0289427),(248,0.0289427),(249,0.0289427),(250,0.0289427),(251,0.0289427\\\\ ),(252,0.0289427),(253,0.0289427),(254,0.0289427),(255,0.0308907),(256,0.0308907),(\\\\ 257,0.0308907),(258,0.0308907),(259,0.0308907),(260,0.0308907),(261,0.0308907),(262\\\\ ,0.0308907),(263,0.0308907),(264,0.0308907),(265,0.0320039),(266,0.0320039),(267,0.0320039\\\\ ),(268,0.0320039),(269,0.0320039),(270,0.0320039),(271,0.0320039),(272,0.0320039),(\\\\ 273,0.0320039),(274,0.0320039),(275,0.0320039),(276,0),(277,0),(278,0),(279,0),(280\\\\ ,0),(281,0),(282,0),(283,0),(284,0),(285,0),(286,0),(287,0),(288,0),(289,0),(290,0)\\\\ ,(291,0),(292,0),(293,0),(294,0),(295,0),(296,0),(297,0),(298,0),(299,0),(300,0),(301\\\\ ,0),(302,0),(303,0),(304,0),(305,0),(306,0),(307,0),(308,0),(309,0),(310,0),(311,0)\\\\ ,(312,0),(313,0),(314,0),(315,0),(316,0),(317,0),(318,0),(319,0),(320,0),(321,0),(322\\\\ ,0),(323,0),(324,0),(325,0),(326,0),(327,0),(328,0),(329,0),(330,0),(331,0),(332,0)\\\\ ,(333,0),(334,0),(335,0),(336,0),(337,0),(338,0),(339,0),(340,0),(341,0),(342,0),(343\\\\ ,0),(344,0),(345,0),(346,0),(347,0),(348,0),(349,0),(350,0),(351,0),(352,0),(353,0)\\\\ ,(354,0),(355,0),(356,0),(357,0),(358,0),(359,0),(360,0),(361,0),(362,0),(363,0),(364\\\\ ,0),(365,0))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x,time_in_lookup_data,lookups_data["tomato"])


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
    Original Eqn: b'( [(1,0)-(365,0.009)],(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11\\\\ ,0),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23\\\\ ,0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35\\\\ ,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47\\\\ ,0),(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),(54,0),(55,0),(56,0),(57,0),(58,0),(59\\\\ ,0),(60,0),(61,0),(62,0),(63,0),(64,0),(65,0),(66,0),(67,0),(68,0),(69,0),(70,0),(71\\\\ ,0),(72,0),(73,0),(74,0),(75,0),(76,0),(77,0),(78,0),(79,0),(80,0),(81,0),(82,0),(83\\\\ ,0),(84,0),(85,0),(86,0),(87,0),(88,0),(89,0),(90,0),(91,0),(92,0),(93,0),(94,0),(95\\\\ ,0),(96,0),(97,0),(98,0),(99,0),(100,0),(101,0),(102,0),(103,0),(104,0),(105,0),(106\\\\ ,0),(107,0),(108,0),(109,0),(110,0),(111,0),(112,0),(113,0),(114,0),(115,0),(116,0)\\\\ ,(117,0),(118,0),(119,0),(120,0),(121,0),(122,0),(123,0),(124,0),(125,0),(126,0),(127\\\\ ,0),(128,0),(129,0),(130,0),(131,0),(132,0),(133,0),(134,0),(135,0),(136,0),(137,0)\\\\ ,(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),(144,0),(145,0),(146,0),(147,0),(148\\\\ ,0),(149,0),(150,0),(151,0),(152,0),(153,0),(154,0),(155,0),(156,0),(157,0),(158,0)\\\\ ,(159,0),(160,0),(161,0),(162,0),(163,0),(164,0),(165,0),(166,0),(167,0),(168,0),(169\\\\ ,0),(170,0),(171,0),(172,0),(173,0),(174,0),(175,0),(176,0),(177,0),(178,0),(179,0)\\\\ ,(180,0),(181,0),(182,0),(183,0),(184,0),(185,0),(186,0),(187,0),(188,0),(189,0),(190\\\\ ,0),(191,0),(192,0),(193,0),(194,0),(195,0.0058578),(196,0.0058578),(197,0.0058578)\\\\ ,(198,0.0058578),(199,0.0058578),(200,0.0058578),(201,0.0058578),(202,0.0058578),(203\\\\ ,0.0058578),(204,0.0058578),(205,0.00702936),(206,0.00702936),(207,0.00702936),(208\\\\ ,0.00702936),(209,0.00702936),(210,0.00702936),(211,0.00702936),(212,0.00702936),(213\\\\ ,0.00702936),(214,0.00702936),(215,0.00738984),(216,0.00738984),(217,0.00738984),(218\\\\ ,0.00738984),(219,0.00738984),(220,0.00738984),(221,0.00738984),(222,0.00738984),(223\\\\ ,0.00738984),(224,0.00738984),(225,0.00775032),(226,0.00775032),(227,0.00775032),(228\\\\ ,0.00775032),(229,0.00775032),(230,0.00775032),(231,0.00775032),(232,0.00775032),(233\\\\ ,0.00775032),(234,0.00775032),(235,0.0085614),(236,0.0085614),(237,0.0085614),(238,\\\\ 0.0085614),(239,0.0085614),(240,0.0085614),(241,0.0085614),(242,0.0085614),(243,0.0085614\\\\ ),(244,0.0085614),(245,0.00784044),(246,0.00784044),(247,0.00784044),(248,0.00784044\\\\ ),(249,0.00784044),(250,0.00784044),(251,0.00784044),(252,0.00784044),(253,0.00784044\\\\ ),(254,0.00784044),(255,0.00612816),(256,0.00612816),(257,0.00612816),(258,0.00612816\\\\ ),(259,0.00612816),(260,0.00612816),(261,0.00612816),(262,0.00612816),(263,0.00612816\\\\ ),(264,0.00612816),(265,0.004506),(266,0.004506),(267,0.004506),(268,0.004506),(269\\\\ ,0.004506),(270,0.004506),(271,0.004506),(272,0.004506),(273,0.004506),(274,0.004506\\\\ ),(275,0.004506),(276,0.0036048),(277,0.0036048),(278,0.0036048),(279,0.0036048),(280\\\\ ,0.0036048),(281,0.0036048),(282,0.0036048),(283,0.0036048),(284,0.0036048),(285,0.0036048\\\\ ),(286,0),(287,0),(288,0),(289,0),(290,0),(291,0),(292,0),(293,0),(294,0),(295,0),(\\\\ 296,0),(297,0),(298,0),(299,0),(300,0),(301,0),(302,0),(303,0),(304,0),(305,0),(306\\\\ ,0),(307,0),(308,0),(309,0),(310,0),(311,0),(312,0),(313,0),(314,0),(315,0),(316,0)\\\\ ,(317,0),(318,0),(319,0),(320,0),(321,0),(322,0),(323,0),(324,0),(325,0),(326,0),(327\\\\ ,0),(328,0),(329,0),(330,0),(331,0),(332,0),(333,0),(334,0),(335,0),(336,0),(337,0)\\\\ ,(338,0),(339,0),(340,0),(341,0),(342,0),(343,0),(344,0),(345,0),(346,0),(347,0),(348\\\\ ,0),(349,0),(350,0),(351,0),(352,0),(353,0),(354,0),(355,0),(356,0),(357,0),(358,0)\\\\ ,(359,0),(360,0),(361,0),(362,0),(363,0),(364,0),(365,0))'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x,time_in_lookup_data,lookups_data["wheat"])


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
    Original Eqn: b'( [(1,0)-(365,0.7)],(1,0.210334),(2,0.210334),(3,0.210334),(4,0.210334),(5,0.210334),(\\\\ 6,0.210334),(7,0.210334),(8,0.210334),(9,0.210334),(10,0.210334),(11,0.210334),(12,\\\\ 0.210334),(13,0.210334),(14,0.210334),(15,0.210334),(16,0.210334),(17,0.210334),(18\\\\ ,0.210334),(19,0.210334),(20,0.210334),(21,0.210334),(22,0.210334),(23,0.210334),(24\\\\ ,0.210334),(25,0.210334),(26,0.210334),(27,0.210334),(28,0.210334),(29,0.210334),(30\\\\ ,0.210334),(31,0.225111),(32,0.225111),(33,0.225111),(34,0.225111),(35,0.225111),(36\\\\ ,0.225111),(37,0.225111),(38,0.225111),(39,0.225111),(40,0.225111),(41,0.225111),(42\\\\ ,0.225111),(43,0.225111),(44,0.225111),(45,0.225111),(46,0.225111),(47,0.225111),(48\\\\ ,0.225111),(49,0.225111),(50,0.225111),(51,0.225111),(52,0.225111),(53,0.225111),(54\\\\ ,0.225111),(55,0.225111),(56,0.225111),(57,0.225111),(58,0.225111),(59,0.225111),(60\\\\ ,0.225111),(61,0.247338),(62,0.247338),(63,0.247338),(64,0.247338),(65,0.247338),(66\\\\ ,0.247338),(67,0.247338),(68,0.247338),(69,0.247338),(70,0.247338),(71,0.247338),(72\\\\ ,0.247338),(73,0.247338),(74,0.247338),(75,0.247338),(76,0.247338),(77,0.247338),(78\\\\ ,0.247338),(79,0.247338),(80,0.247338),(81,0.247338),(82,0.247338),(83,0.247338),(84\\\\ ,0.247338),(85,0.247338),(86,0.247338),(87,0.247338),(88,0.247338),(89,0.247338),(90\\\\ ,0.247338),(91,0.323928),(92,0.323928),(93,0.323928),(94,0.323928),(95,0.323928),(96\\\\ ,0.323928),(97,0.323928),(98,0.323928),(99,0.323928),(100,0.323928),(101,0.323928),\\\\ (102,0.323928),(103,0.323928),(104,0.323928),(105,0.323928),(106,0.323928),(107,0.323928\\\\ ),(108,0.323928),(109,0.323928),(110,0.323928),(111,0.323928),(112,0.323928),(113,0.323928\\\\ ),(114,0.323928),(115,0.323928),(116,0.323928),(117,0.323928),(118,0.323928),(119,0.323928\\\\ ),(120,0.323928),(121,0.498409),(122,0.498409),(123,0.498409),(124,0.498409),(125,0.498409\\\\ ),(126,0.498409),(127,0.498409),(128,0.498409),(129,0.498409),(130,0.498409),(131,0.498409\\\\ ),(132,0.498409),(133,0.498409),(134,0.498409),(135,0.498409),(136,0.498409),(137,0.498409\\\\ ),(138,0.498409),(139,0.498409),(140,0.498409),(141,0.498409),(142,0.498409),(143,0.498409\\\\ ),(144,0.498409),(145,0.498409),(146,0.498409),(147,0.498409),(148,0.498409),(149,0.498409\\\\ ),(150,0.498409),(151,0.412189),(152,0.412189),(153,0.412189),(154,0.412189),(155,0.412189\\\\ ),(156,0.412189),(157,0.412189),(158,0.412189),(159,0.412189),(160,0.412189),(161,0.412189\\\\ ),(162,0.412189),(163,0.412189),(164,0.412189),(165,0.412189),(166,0.412189),(167,0.412189\\\\ ),(168,0.412189),(169,0.412189),(170,0.412189),(171,0.412189),(172,0.412189),(173,0.412189\\\\ ),(174,0.412189),(175,0.412189),(176,0.412189),(177,0.412189),(178,0.412189),(179,0.412189\\\\ ),(180,0.412189),(181,0.3615),(182,0.3615),(183,0.3615),(184,0.3615),(185,0.3615),(\\\\ 186,0.3615),(187,0.3615),(188,0.3615),(189,0.3615),(190,0.3615),(191,0.3615),(192,0.3615\\\\ ),(193,0.3615),(194,0.3615),(195,0.3615),(196,0.3615),(197,0.3615),(198,0.3615),(199\\\\ ,0.3615),(200,0.3615),(201,0.3615),(202,0.3615),(203,0.3615),(204,0.3615),(205,0.3615\\\\ ),(206,0.3615),(207,0.3615),(208,0.3615),(209,0.3615),(210,0.3615),(211,0.351684),(\\\\ 212,0.351684),(213,0.351684),(214,0.351684),(215,0.351684),(216,0.351684),(217,0.351684\\\\ ),(218,0.351684),(219,0.351684),(220,0.351684),(221,0.351684),(222,0.351684),(223,0.351684\\\\ ),(224,0.351684),(225,0.351684),(226,0.351684),(227,0.351684),(228,0.351684),(229,0.351684\\\\ ),(230,0.351684),(231,0.351684),(232,0.351684),(233,0.351684),(234,0.351684),(235,0.351684\\\\ ),(236,0.351684),(237,0.351684),(238,0.351684),(239,0.351684),(240,0.351684),(241,0.283267\\\\ ),(242,0.283267),(243,0.283267),(244,0.283267),(245,0.283267),(246,0.283267),(247,0.283267\\\\ ),(248,0.283267),(249,0.283267),(250,0.283267),(251,0.283267),(252,0.283267),(253,0.283267\\\\ ),(254,0.283267),(255,0.283267),(256,0.283267),(257,0.283267),(258,0.283267),(259,0.283267\\\\ ),(260,0.283267),(261,0.283267),(262,0.283267),(263,0.283267),(264,0.283267),(265,0.283267\\\\ ),(266,0.283267),(267,0.283267),(268,0.283267),(269,0.283267),(270,0.283267),(271,0.253135\\\\ ),(272,0.253135),(273,0.253135),(274,0.253135),(275,0.253135),(276,0.253135),(277,0.253135\\\\ ),(278,0.253135),(279,0.253135),(280,0.253135),(281,0.253135),(282,0.253135),(283,0.253135\\\\ ),(284,0.253135),(285,0.253135),(286,0.253135),(287,0.253135),(288,0.253135),(289,0.253135\\\\ ),(290,0.253135),(291,0.253135),(292,0.253135),(293,0.253135),(294,0.253135),(295,0.253135\\\\ ),(296,0.253135),(297,0.253135),(298,0.253135),(299,0.253135),(300,0.253135),(301,0.604811\\\\ ),(302,0.604811),(303,0.604811),(304,0.604811),(305,0.604811),(306,0.604811),(307,0.604811\\\\ ),(308,0.604811),(309,0.604811),(310,0.604811),(311,0.604811),(312,0.604811),(313,0.604811\\\\ ),(314,0.604811),(315,0.604811),(316,0.604811),(317,0.604811),(318,0.604811),(319,0.604811\\\\ ),(320,0.604811),(321,0.604811),(322,0.604811),(323,0.604811),(324,0.604811),(325,0.604811\\\\ ),(326,0.604811),(327,0.604811),(328,0.604811),(329,0.604811),(330,0.604811),(331,0.205543\\\\ ),(332,0.205543),(333,0.205543),(334,0.205543),(335,0.205543),(336,0.205543),(337,0.205543\\\\ ),(338,0.205543),(339,0.205543),(340,0.205543),(341,0.205543),(342,0.205543),(343,0.205543\\\\ ),(344,0.205543),(345,0.205543),(346,0.205543),(347,0.205543),(348,0.205543),(349,0.205543\\\\ ),(350,0.205543),(351,0.205543),(352,0.205543),(353,0.205543),(354,0.205543),(355,0.205543\\\\ ),(356,0.205543),(357,0.205543),(358,0.205543),(359,0.205543),(360,0.205543),(361,0.205543\\\\ ),(362,0.205543),(363,0.205543),(364,0.205543),(365,0.205543))'
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
        0.210334, 0.210334, 0.210334, 0.210334, 0.210334, 0.210334, 0.210334, 0.210334, 0.210334,
        0.210334, 0.210334, 0.210334, 0.210334, 0.210334, 0.210334, 0.210334, 0.210334, 0.210334,
        0.210334, 0.210334, 0.210334, 0.210334, 0.210334, 0.210334, 0.210334, 0.210334, 0.210334,
        0.210334, 0.210334, 0.210334, 0.225111, 0.225111, 0.225111, 0.225111, 0.225111, 0.225111,
        0.225111, 0.225111, 0.225111, 0.225111, 0.225111, 0.225111, 0.225111, 0.225111, 0.225111,
        0.225111, 0.225111, 0.225111, 0.225111, 0.225111, 0.225111, 0.225111, 0.225111, 0.225111,
        0.225111, 0.225111, 0.225111, 0.225111, 0.225111, 0.225111, 0.247338, 0.247338, 0.247338,
        0.247338, 0.247338, 0.247338, 0.247338, 0.247338, 0.247338, 0.247338, 0.247338, 0.247338,
        0.247338, 0.247338, 0.247338, 0.247338, 0.247338, 0.247338, 0.247338, 0.247338, 0.247338,
        0.247338, 0.247338, 0.247338, 0.247338, 0.247338, 0.247338, 0.247338, 0.247338, 0.247338,
        0.323928, 0.323928, 0.323928, 0.323928, 0.323928, 0.323928, 0.323928, 0.323928, 0.323928,
        0.323928, 0.323928, 0.323928, 0.323928, 0.323928, 0.323928, 0.323928, 0.323928, 0.323928,
        0.323928, 0.323928, 0.323928, 0.323928, 0.323928, 0.323928, 0.323928, 0.323928, 0.323928,
        0.323928, 0.323928, 0.323928, 0.498409, 0.498409, 0.498409, 0.498409, 0.498409, 0.498409,
        0.498409, 0.498409, 0.498409, 0.498409, 0.498409, 0.498409, 0.498409, 0.498409, 0.498409,
        0.498409, 0.498409, 0.498409, 0.498409, 0.498409, 0.498409, 0.498409, 0.498409, 0.498409,
        0.498409, 0.498409, 0.498409, 0.498409, 0.498409, 0.498409, 0.412189, 0.412189, 0.412189,
        0.412189, 0.412189, 0.412189, 0.412189, 0.412189, 0.412189, 0.412189, 0.412189, 0.412189,
        0.412189, 0.412189, 0.412189, 0.412189, 0.412189, 0.412189, 0.412189, 0.412189, 0.412189,
        0.412189, 0.412189, 0.412189, 0.412189, 0.412189, 0.412189, 0.412189, 0.412189, 0.412189,
        0.3615, 0.3615, 0.3615, 0.3615, 0.3615, 0.3615, 0.3615, 0.3615, 0.3615, 0.3615, 0.3615,
        0.3615, 0.3615, 0.3615, 0.3615, 0.3615, 0.3615, 0.3615, 0.3615, 0.3615, 0.3615, 0.3615,
        0.3615, 0.3615, 0.3615, 0.3615, 0.3615, 0.3615, 0.3615, 0.3615, 0.351684, 0.351684,
        0.351684, 0.351684, 0.351684, 0.351684, 0.351684, 0.351684, 0.351684, 0.351684, 0.351684,
        0.351684, 0.351684, 0.351684, 0.351684, 0.351684, 0.351684, 0.351684, 0.351684, 0.351684,
        0.351684, 0.351684, 0.351684, 0.351684, 0.351684, 0.351684, 0.351684, 0.351684, 0.351684,
        0.351684, 0.283267, 0.283267, 0.283267, 0.283267, 0.283267, 0.283267, 0.283267, 0.283267,
        0.283267, 0.283267, 0.283267, 0.283267, 0.283267, 0.283267, 0.283267, 0.283267, 0.283267,
        0.283267, 0.283267, 0.283267, 0.283267, 0.283267, 0.283267, 0.283267, 0.283267, 0.283267,
        0.283267, 0.283267, 0.283267, 0.283267, 0.253135, 0.253135, 0.253135, 0.253135, 0.253135,
        0.253135, 0.253135, 0.253135, 0.253135, 0.253135, 0.253135, 0.253135, 0.253135, 0.253135,
        0.253135, 0.253135, 0.253135, 0.253135, 0.253135, 0.253135, 0.253135, 0.253135, 0.253135,
        0.253135, 0.253135, 0.253135, 0.253135, 0.253135, 0.253135, 0.253135, 0.604811, 0.604811,
        0.604811, 0.604811, 0.604811, 0.604811, 0.604811, 0.604811, 0.604811, 0.604811, 0.604811,
        0.604811, 0.604811, 0.604811, 0.604811, 0.604811, 0.604811, 0.604811, 0.604811, 0.604811,
        0.604811, 0.604811, 0.604811, 0.604811, 0.604811, 0.604811, 0.604811, 0.604811, 0.604811,
        0.604811, 0.205543, 0.205543, 0.205543, 0.205543, 0.205543, 0.205543, 0.205543, 0.205543,
        0.205543, 0.205543, 0.205543, 0.205543, 0.205543, 0.205543, 0.205543, 0.205543, 0.205543,
        0.205543, 0.205543, 0.205543, 0.205543, 0.205543, 0.205543, 0.205543, 0.205543, 0.205543,
        0.205543, 0.205543, 0.205543, 0.205543, 0.205543, 0.205543, 0.205543, 0.205543, 0.205543
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
        0.00878, 0.00878, 0.00878, 0.00878, 0.00878, 0.00878, 0.00878, 0.00878, 0.00878, 0.00878,
        0.00878, 0.00878, 0.00878, 0.00878, 0.00878, 0.00878, 0.00878, 0.00878, 0.00878, 0.00878,
        0.00878, 0.00878, 0.00878, 0.00878, 0.00878, 0.00878, 0.00878, 0.00878, 0.00878, 0.00878,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0.00066, 0.00066, 0.00066, 0.00066, 0.00066, 0.00066, 0.00066, 0.00066, 0.00066, 0.00066,
        0.00066, 0.00066, 0.00066, 0.00066, 0.00066, 0.00066, 0.00066, 0.00066, 0.00066, 0.00066,
        0.00066, 0.00066, 0.00066, 0.00066, 0.00066, 0.00066, 0.00066, 0.00066, 0.00066, 0.00066,
        0.02452, 0.02452, 0.02452, 0.02452, 0.02452, 0.02452, 0.02452, 0.02452, 0.02452, 0.02452,
        0.02452, 0.02452, 0.02452, 0.02452, 0.02452, 0.02452, 0.02452, 0.02452, 0.02452, 0.02452,
        0.02452, 0.02452, 0.02452, 0.02452, 0.02452, 0.02452, 0.02452, 0.02452, 0.02452, 0.02452,
        0.07626, 0.07626, 0.07626, 0.07626, 0.07626, 0.07626, 0.07626, 0.07626, 0.07626, 0.07626,
        0.07626, 0.07626, 0.07626, 0.07626, 0.07626, 0.07626, 0.07626, 0.07626, 0.07626, 0.07626,
        0.07626, 0.07626, 0.07626, 0.07626, 0.07626, 0.07626, 0.07626, 0.07626, 0.07626, 0.07626,
        0.11028, 0.11028, 0.11028, 0.11028, 0.11028, 0.11028, 0.11028, 0.11028, 0.11028, 0.11028,
        0.11028, 0.11028, 0.11028, 0.11028, 0.11028, 0.11028, 0.11028, 0.11028, 0.11028, 0.11028,
        0.11028, 0.11028, 0.11028, 0.11028, 0.11028, 0.11028, 0.11028, 0.11028, 0.11028, 0.11028,
        0.15799, 0.15799, 0.15799, 0.15799, 0.15799, 0.15799, 0.15799, 0.15799, 0.15799, 0.15799,
        0.15799, 0.15799, 0.15799, 0.15799, 0.15799, 0.15799, 0.15799, 0.15799, 0.15799, 0.15799,
        0.15799, 0.15799, 0.15799, 0.15799, 0.15799, 0.15799, 0.15799, 0.15799, 0.15799, 0.15799,
        0.14253, 0.14253, 0.14253, 0.14253, 0.14253, 0.14253, 0.14253, 0.14253, 0.14253, 0.14253,
        0.14253, 0.14253, 0.14253, 0.14253, 0.14253, 0.14253, 0.14253, 0.14253, 0.14253, 0.14253,
        0.14253, 0.14253, 0.14253, 0.14253, 0.14253, 0.14253, 0.14253, 0.14253, 0.14253, 0.14253,
        0.05832, 0.05832, 0.05832, 0.05832, 0.05832, 0.05832, 0.05832, 0.05832, 0.05832, 0.05832,
        0.05832, 0.05832, 0.05832, 0.05832, 0.05832, 0.05832, 0.05832, 0.05832, 0.05832, 0.05832,
        0.05832, 0.05832, 0.05832, 0.05832, 0.05832, 0.05832, 0.05832, 0.05832, 0.05832, 0.05832,
        0.05832, 0.05832, 0.05832, 0.05832, 0.05832
    ])


def finesk_upstream(x):
    """
    Real Name: b'Finesk Upstream'
    Original Eqn: b'( [(1,0)-(365,0.2)],(1,0.0470926),(2,0.0470926),(3,0.0470926),(4,0.0470926),(5,0.0470926\\\\ ),(6,0.0470926),(7,0.0470926),(8,0.0470926),(9,0.0470926),(10,0.0470926),(11,0.0470926\\\\ ),(12,0.0470926),(13,0.0470926),(14,0.0470926),(15,0.0470926),(16,0.0470926),(17,0.0470926\\\\ ),(18,0.0470926),(19,0.0470926),(20,0.0470926),(21,0.0470926),(22,0.0470926),(23,0.0470926\\\\ ),(24,0.0470926),(25,0.0470926),(26,0.0470926),(27,0.0470926),(28,0.0470926),(29,0.0470926\\\\ ),(30,0.0470926),(31,0.0415),(32,0.0415),(33,0.0415),(34,0.0415),(35,0.0415),(36,0.0415\\\\ ),(37,0.0415),(38,0.0415),(39,0.0415),(40,0.0415),(41,0.0415),(42,0.0415),(43,0.0415\\\\ ),(44,0.0415),(45,0.0415),(46,0.0415),(47,0.0415),(48,0.0415),(49,0.0415),(50,0.0415\\\\ ),(51,0.0415),(52,0.0415),(53,0.0415),(54,0.0415),(55,0.0415),(56,0.0415),(57,0.0415\\\\ ),(58,0.0415),(59,0.0415),(60,0.0415),(61,0.0407901),(62,0.0407901),(63,0.0407901),\\\\ (64,0.0407901),(65,0.0407901),(66,0.0407901),(67,0.0407901),(68,0.0407901),(69,0.0407901\\\\ ),(70,0.0407901),(71,0.0407901),(72,0.0407901),(73,0.0407901),(74,0.0407901),(75,0.0407901\\\\ ),(76,0.0407901),(77,0.0407901),(78,0.0407901),(79,0.0407901),(80,0.0407901),(81,0.0407901\\\\ ),(82,0.0407901),(83,0.0407901),(84,0.0407901),(85,0.0407901),(86,0.0407901),(87,0.0407901\\\\ ),(88,0.0407901),(89,0.0407901),(90,0.0407901),(91,0.0410926),(92,0.0410926),(93,0.0410926\\\\ ),(94,0.0410926),(95,0.0410926),(96,0.0410926),(97,0.0410926),(98,0.0410926),(99,0.0410926\\\\ ),(100,0.0410926),(101,0.0410926),(102,0.0410926),(103,0.0410926),(104,0.0410926),(\\\\ 105,0.0410926),(106,0.0410926),(107,0.0410926),(108,0.0410926),(109,0.0410926),(110\\\\ ,0.0410926),(111,0.0410926),(112,0.0410926),(113,0.0410926),(114,0.0410926),(115,0.0410926\\\\ ),(116,0.0410926),(117,0.0410926),(118,0.0410926),(119,0.0410926),(120,0.0410926),(\\\\ 121,0.0451296),(122,0.0451296),(123,0.0451296),(124,0.0451296),(125,0.0451296),(126\\\\ ,0.0451296),(127,0.0451296),(128,0.0451296),(129,0.0451296),(130,0.0451296),(131,0.0451296\\\\ ),(132,0.0451296),(133,0.0451296),(134,0.0451296),(135,0.0451296),(136,0.0451296),(\\\\ 137,0.0451296),(138,0.0451296),(139,0.0451296),(140,0.0451296),(141,0.0451296),(142\\\\ ,0.0451296),(143,0.0451296),(144,0.0451296),(145,0.0451296),(146,0.0451296),(147,0.0451296\\\\ ),(148,0.0451296),(149,0.0451296),(150,0.0451296),(151,0.0593086),(152,0.0593086),(\\\\ 153,0.0593086),(154,0.0593086),(155,0.0593086),(156,0.0593086),(157,0.0593086),(158\\\\ ,0.0593086),(159,0.0593086),(160,0.0593086),(161,0.0593086),(162,0.0593086),(163,0.0593086\\\\ ),(164,0.0593086),(165,0.0593086),(166,0.0593086),(167,0.0593086),(168,0.0593086),(\\\\ 169,0.0593086),(170,0.0593086),(171,0.0593086),(172,0.0593086),(173,0.0593086),(174\\\\ ,0.0593086),(175,0.0593086),(176,0.0593086),(177,0.0593086),(178,0.0593086),(179,0.0593086\\\\ ),(180,0.0593086),(181,0.115852),(182,0.115852),(183,0.115852),(184,0.115852),(185,\\\\ 0.115852),(186,0.115852),(187,0.115852),(188,0.115852),(189,0.115852),(190,0.115852\\\\ ),(191,0.115852),(192,0.115852),(193,0.115852),(194,0.115852),(195,0.115852),(196,0.115852\\\\ ),(197,0.115852),(198,0.115852),(199,0.115852),(200,0.115852),(201,0.115852),(202,0.115852\\\\ ),(203,0.115852),(204,0.115852),(205,0.115852),(206,0.115852),(207,0.115852),(208,0.115852\\\\ ),(209,0.115852),(210,0.115852),(211,0.134432),(212,0.134432),(213,0.134432),(214,0.134432\\\\ ),(215,0.134432),(216,0.134432),(217,0.134432),(218,0.134432),(219,0.134432),(220,0.134432\\\\ ),(221,0.134432),(222,0.134432),(223,0.134432),(224,0.134432),(225,0.134432),(226,0.134432\\\\ ),(227,0.134432),(228,0.134432),(229,0.134432),(230,0.134432),(231,0.134432),(232,0.134432\\\\ ),(233,0.134432),(234,0.134432),(235,0.134432),(236,0.134432),(237,0.134432),(238,0.134432\\\\ ),(239,0.134432),(240,0.134432),(241,0.136407),(242,0.136407),(243,0.136407),(244,0.136407\\\\ ),(245,0.136407),(246,0.136407),(247,0.136407),(248,0.136407),(249,0.136407),(250,0.136407\\\\ ),(251,0.136407),(252,0.136407),(253,0.136407),(254,0.136407),(255,0.136407),(256,0.136407\\\\ ),(257,0.136407),(258,0.136407),(259,0.136407),(260,0.136407),(261,0.136407),(262,0.136407\\\\ ),(263,0.136407),(264,0.136407),(265,0.136407),(266,0.136407),(267,0.136407),(268,0.136407\\\\ ),(269,0.136407),(270,0.136407),(271,0.163352),(272,0.163352),(273,0.163352),(274,0.163352\\\\ ),(275,0.163352),(276,0.163352),(277,0.163352),(278,0.163352),(279,0.163352),(280,0.163352\\\\ ),(281,0.163352),(282,0.163352),(283,0.163352),(284,0.163352),(285,0.163352),(286,0.163352\\\\ ),(287,0.163352),(288,0.163352),(289,0.163352),(290,0.163352),(291,0.163352),(292,0.163352\\\\ ),(293,0.163352),(294,0.163352),(295,0.163352),(296,0.163352),(297,0.163352),(298,0.163352\\\\ ),(299,0.163352),(300,0.163352),(301,0.148302),(302,0.148302),(303,0.148302),(304,0.148302\\\\ ),(305,0.148302),(306,0.148302),(307,0.148302),(308,0.148302),(309,0.148302),(310,0.148302\\\\ ),(311,0.148302),(312,0.148302),(313,0.148302),(314,0.148302),(315,0.148302),(316,0.148302\\\\ ),(317,0.148302),(318,0.148302),(319,0.148302),(320,0.148302),(321,0.148302),(322,0.148302\\\\ ),(323,0.148302),(324,0.148302),(325,0.148302),(326,0.148302),(327,0.148302),(328,0.148302\\\\ ),(329,0.148302),(330,0.148302),(331,0.0901296),(332,0.0901296),(333,0.0901296),(334\\\\ ,0.0901296),(335,0.0901296),(336,0.0901296),(337,0.0901296),(338,0.0901296),(339,0.0901296\\\\ ),(340,0.0901296),(341,0.0901296),(342,0.0901296),(343,0.0901296),(344,0.0901296),(\\\\ 345,0.0901296),(346,0.0901296),(347,0.0901296),(348,0.0901296),(349,0.0901296),(350\\\\ ,0.0901296),(351,0.0901296),(352,0.0901296),(353,0.0901296),(354,0.0901296),(355,0.0901296\\\\ ),(356,0.0901296),(357,0.0901296),(358,0.0901296),(359,0.0901296),(360,0.0901296),(\\\\ 361,0.0901296),(362,0.0901296),(363,0.0901296),(364,0.0901296),(365,0.0901296))'
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
        0.0470926, 0.0470926, 0.0470926, 0.0470926, 0.0470926, 0.0470926, 0.0470926, 0.0470926,
        0.0470926, 0.0470926, 0.0470926, 0.0470926, 0.0470926, 0.0470926, 0.0470926, 0.0470926,
        0.0470926, 0.0470926, 0.0470926, 0.0470926, 0.0470926, 0.0470926, 0.0470926, 0.0470926,
        0.0470926, 0.0470926, 0.0470926, 0.0470926, 0.0470926, 0.0470926, 0.0415, 0.0415, 0.0415,
        0.0415, 0.0415, 0.0415, 0.0415, 0.0415, 0.0415, 0.0415, 0.0415, 0.0415, 0.0415, 0.0415,
        0.0415, 0.0415, 0.0415, 0.0415, 0.0415, 0.0415, 0.0415, 0.0415, 0.0415, 0.0415, 0.0415,
        0.0415, 0.0415, 0.0415, 0.0415, 0.0415, 0.0407901, 0.0407901, 0.0407901, 0.0407901,
        0.0407901, 0.0407901, 0.0407901, 0.0407901, 0.0407901, 0.0407901, 0.0407901, 0.0407901,
        0.0407901, 0.0407901, 0.0407901, 0.0407901, 0.0407901, 0.0407901, 0.0407901, 0.0407901,
        0.0407901, 0.0407901, 0.0407901, 0.0407901, 0.0407901, 0.0407901, 0.0407901, 0.0407901,
        0.0407901, 0.0407901, 0.0410926, 0.0410926, 0.0410926, 0.0410926, 0.0410926, 0.0410926,
        0.0410926, 0.0410926, 0.0410926, 0.0410926, 0.0410926, 0.0410926, 0.0410926, 0.0410926,
        0.0410926, 0.0410926, 0.0410926, 0.0410926, 0.0410926, 0.0410926, 0.0410926, 0.0410926,
        0.0410926, 0.0410926, 0.0410926, 0.0410926, 0.0410926, 0.0410926, 0.0410926, 0.0410926,
        0.0451296, 0.0451296, 0.0451296, 0.0451296, 0.0451296, 0.0451296, 0.0451296, 0.0451296,
        0.0451296, 0.0451296, 0.0451296, 0.0451296, 0.0451296, 0.0451296, 0.0451296, 0.0451296,
        0.0451296, 0.0451296, 0.0451296, 0.0451296, 0.0451296, 0.0451296, 0.0451296, 0.0451296,
        0.0451296, 0.0451296, 0.0451296, 0.0451296, 0.0451296, 0.0451296, 0.0593086, 0.0593086,
        0.0593086, 0.0593086, 0.0593086, 0.0593086, 0.0593086, 0.0593086, 0.0593086, 0.0593086,
        0.0593086, 0.0593086, 0.0593086, 0.0593086, 0.0593086, 0.0593086, 0.0593086, 0.0593086,
        0.0593086, 0.0593086, 0.0593086, 0.0593086, 0.0593086, 0.0593086, 0.0593086, 0.0593086,
        0.0593086, 0.0593086, 0.0593086, 0.0593086, 0.115852, 0.115852, 0.115852, 0.115852,
        0.115852, 0.115852, 0.115852, 0.115852, 0.115852, 0.115852, 0.115852, 0.115852, 0.115852,
        0.115852, 0.115852, 0.115852, 0.115852, 0.115852, 0.115852, 0.115852, 0.115852, 0.115852,
        0.115852, 0.115852, 0.115852, 0.115852, 0.115852, 0.115852, 0.115852, 0.115852, 0.134432,
        0.134432, 0.134432, 0.134432, 0.134432, 0.134432, 0.134432, 0.134432, 0.134432, 0.134432,
        0.134432, 0.134432, 0.134432, 0.134432, 0.134432, 0.134432, 0.134432, 0.134432, 0.134432,
        0.134432, 0.134432, 0.134432, 0.134432, 0.134432, 0.134432, 0.134432, 0.134432, 0.134432,
        0.134432, 0.134432, 0.136407, 0.136407, 0.136407, 0.136407, 0.136407, 0.136407, 0.136407,
        0.136407, 0.136407, 0.136407, 0.136407, 0.136407, 0.136407, 0.136407, 0.136407, 0.136407,
        0.136407, 0.136407, 0.136407, 0.136407, 0.136407, 0.136407, 0.136407, 0.136407, 0.136407,
        0.136407, 0.136407, 0.136407, 0.136407, 0.136407, 0.163352, 0.163352, 0.163352, 0.163352,
        0.163352, 0.163352, 0.163352, 0.163352, 0.163352, 0.163352, 0.163352, 0.163352, 0.163352,
        0.163352, 0.163352, 0.163352, 0.163352, 0.163352, 0.163352, 0.163352, 0.163352, 0.163352,
        0.163352, 0.163352, 0.163352, 0.163352, 0.163352, 0.163352, 0.163352, 0.163352, 0.148302,
        0.148302, 0.148302, 0.148302, 0.148302, 0.148302, 0.148302, 0.148302, 0.148302, 0.148302,
        0.148302, 0.148302, 0.148302, 0.148302, 0.148302, 0.148302, 0.148302, 0.148302, 0.148302,
        0.148302, 0.148302, 0.148302, 0.148302, 0.148302, 0.148302, 0.148302, 0.148302, 0.148302,
        0.148302, 0.148302, 0.0901296, 0.0901296, 0.0901296, 0.0901296, 0.0901296, 0.0901296,
        0.0901296, 0.0901296, 0.0901296, 0.0901296, 0.0901296, 0.0901296, 0.0901296, 0.0901296,
        0.0901296, 0.0901296, 0.0901296, 0.0901296, 0.0901296, 0.0901296, 0.0901296, 0.0901296,
        0.0901296, 0.0901296, 0.0901296, 0.0901296, 0.0901296, 0.0901296, 0.0901296, 0.0901296,
        0.0901296, 0.0901296, 0.0901296, 0.0901296, 0.0901296
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
    Original Eqn: b'( [(1,0)-(365,0.4)],(1,0.0500382),(2,0.0500382),(3,0.0500382),(4,0.0500382),(5,0.0500382\\\\ ),(6,0.0500382),(7,0.0500382),(8,0.0500382),(9,0.0500382),(10,0.0500382),(11,0.0500382\\\\ ),(12,0.0500382),(13,0.0500382),(14,0.0500382),(15,0.0500382),(16,0.0500382),(17,0.0500382\\\\ ),(18,0.0500382),(19,0.0500382),(20,0.0500382),(21,0.0500382),(22,0.0500382),(23,0.0500382\\\\ ),(24,0.0500382),(25,0.0500382),(26,0.0500382),(27,0.0500382),(28,0.0500382),(29,0.0500382\\\\ ),(30,0.0500382),(31,0.134835),(32,0.134835),(33,0.134835),(34,0.134835),(35,0.134835\\\\ ),(36,0.134835),(37,0.134835),(38,0.134835),(39,0.134835),(40,0.134835),(41,0.134835\\\\ ),(42,0.134835),(43,0.134835),(44,0.134835),(45,0.134835),(46,0.134835),(47,0.134835\\\\ ),(48,0.134835),(49,0.134835),(50,0.134835),(51,0.134835),(52,0.134835),(53,0.134835\\\\ ),(54,0.134835),(55,0.134835),(56,0.134835),(57,0.134835),(58,0.134835),(59,0.134835\\\\ ),(60,0.134835),(61,0.166877),(62,0.166877),(63,0.166877),(64,0.166877),(65,0.166877\\\\ ),(66,0.166877),(67,0.166877),(68,0.166877),(69,0.166877),(70,0.166877),(71,0.166877\\\\ ),(72,0.166877),(73,0.166877),(74,0.166877),(75,0.166877),(76,0.166877),(77,0.166877\\\\ ),(78,0.166877),(79,0.166877),(80,0.166877),(81,0.166877),(82,0.166877),(83,0.166877\\\\ ),(84,0.166877),(85,0.166877),(86,0.166877),(87,0.166877),(88,0.166877),(89,0.166877\\\\ ),(90,0.166877),(91,0.196866),(92,0.196866),(93,0.196866),(94,0.196866),(95,0.196866\\\\ ),(96,0.196866),(97,0.196866),(98,0.196866),(99,0.196866),(100,0.196866),(101,0.196866\\\\ ),(102,0.196866),(103,0.196866),(104,0.196866),(105,0.196866),(106,0.196866),(107,0.196866\\\\ ),(108,0.196866),(109,0.196866),(110,0.196866),(111,0.196866),(112,0.196866),(113,0.196866\\\\ ),(114,0.196866),(115,0.196866),(116,0.196866),(117,0.196866),(118,0.196866),(119,0.196866\\\\ ),(120,0.196866),(121,0.224476),(122,0.224476),(123,0.224476),(124,0.224476),(125,0.224476\\\\ ),(126,0.224476),(127,0.224476),(128,0.224476),(129,0.224476),(130,0.224476),(131,0.224476\\\\ ),(132,0.224476),(133,0.224476),(134,0.224476),(135,0.224476),(136,0.224476),(137,0.224476\\\\ ),(138,0.224476),(139,0.224476),(140,0.224476),(141,0.224476),(142,0.224476),(143,0.224476\\\\ ),(144,0.224476),(145,0.224476),(146,0.224476),(147,0.224476),(148,0.224476),(149,0.224476\\\\ ),(150,0.224476),(151,0.289559),(152,0.289559),(153,0.289559),(154,0.289559),(155,0.289559\\\\ ),(156,0.289559),(157,0.289559),(158,0.289559),(159,0.289559),(160,0.289559),(161,0.289559\\\\ ),(162,0.289559),(163,0.289559),(164,0.289559),(165,0.289559),(166,0.289559),(167,0.289559\\\\ ),(168,0.289559),(169,0.289559),(170,0.289559),(171,0.289559),(172,0.289559),(173,0.289559\\\\ ),(174,0.289559),(175,0.289559),(176,0.289559),(177,0.289559),(178,0.289559),(179,0.289559\\\\ ),(180,0.289559),(181,0.361086),(182,0.361086),(183,0.361086),(184,0.361086),(185,0.361086\\\\ ),(186,0.361086),(187,0.361086),(188,0.361086),(189,0.361086),(190,0.361086),(191,0.361086\\\\ ),(192,0.361086),(193,0.361086),(194,0.361086),(195,0.361086),(196,0.361086),(197,0.361086\\\\ ),(198,0.361086),(199,0.361086),(200,0.361086),(201,0.361086),(202,0.361086),(203,0.361086\\\\ ),(204,0.361086),(205,0.361086),(206,0.361086),(207,0.361086),(208,0.361086),(209,0.361086\\\\ ),(210,0.361086),(211,0.272473),(212,0.272473),(213,0.272473),(214,0.272473),(215,0.272473\\\\ ),(216,0.272473),(217,0.272473),(218,0.272473),(219,0.272473),(220,0.272473),(221,0.272473\\\\ ),(222,0.272473),(223,0.272473),(224,0.272473),(225,0.272473),(226,0.272473),(227,0.272473\\\\ ),(228,0.272473),(229,0.272473),(230,0.272473),(231,0.272473),(232,0.272473),(233,0.272473\\\\ ),(234,0.272473),(235,0.272473),(236,0.272473),(237,0.272473),(238,0.272473),(239,0.272473\\\\ ),(240,0.272473),(241,0.0996614),(242,0.0996614),(243,0.0996614),(244,0.0996614),(245\\\\ ,0.0996614),(246,0.0996614),(247,0.0996614),(248,0.0996614),(249,0.0996614),(250,0.0996614\\\\ ),(251,0.0996614),(252,0.0996614),(253,0.0996614),(254,0.0996614),(255,0.0996614),(\\\\ 256,0.0996614),(257,0.0996614),(258,0.0996614),(259,0.0996614),(260,0.0996614),(261\\\\ ,0.0996614),(262,0.0996614),(263,0.0996614),(264,0.0996614),(265,0.0996614),(266,0.0996614\\\\ ),(267,0.0996614),(268,0.0996614),(269,0.0996614),(270,0.0996614),(271,0.0085943),(\\\\ 272,0.0085943),(273,0.0085943),(274,0.0085943),(275,0.0085943),(276,0.0085943),(277\\\\ ,0.0085943),(278,0.0085943),(279,0.0085943),(280,0.0085943),(281,0.0085943),(282,0.0085943\\\\ ),(283,0.0085943),(284,0.0085943),(285,0.0085943),(286,0.0085943),(287,0.0085943),(\\\\ 288,0.0085943),(289,0.0085943),(290,0.0085943),(291,0.0085943),(292,0.0085943),(293\\\\ ,0.0085943),(294,0.0085943),(295,0.0085943),(296,0.0085943),(297,0.0085943),(298,0.0085943\\\\ ),(299,0.0085943),(300,0.0085943),(301,0),(302,0),(303,0),(304,0),(305,0),(306,0),(\\\\ 307,0),(308,0),(309,0),(310,0),(311,0),(312,0),(313,0),(314,0),(315,0),(316,0),(317\\\\ ,0),(318,0),(319,0),(320,0),(321,0),(322,0),(323,0),(324,0),(325,0),(326,0),(327,0)\\\\ ,(328,0),(329,0),(330,0),(331,0),(332,0),(333,0),(334,0),(335,0),(336,0),(337,0),(338\\\\ ,0),(339,0),(340,0),(341,0),(342,0),(343,0),(344,0),(345,0),(346,0),(347,0),(348,0)\\\\ ,(349,0),(350,0),(351,0),(352,0),(353,0),(354,0),(355,0),(356,0),(357,0),(358,0),(359\\\\ ,0),(360,0),(361,0),(362,0),(363,0),(364,0),(365,0))'
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
        0.0500382, 0.0500382, 0.0500382, 0.0500382, 0.0500382, 0.0500382, 0.0500382, 0.0500382,
        0.0500382, 0.0500382, 0.0500382, 0.0500382, 0.0500382, 0.0500382, 0.0500382, 0.0500382,
        0.0500382, 0.0500382, 0.0500382, 0.0500382, 0.0500382, 0.0500382, 0.0500382, 0.0500382,
        0.0500382, 0.0500382, 0.0500382, 0.0500382, 0.0500382, 0.0500382, 0.134835, 0.134835,
        0.134835, 0.134835, 0.134835, 0.134835, 0.134835, 0.134835, 0.134835, 0.134835, 0.134835,
        0.134835, 0.134835, 0.134835, 0.134835, 0.134835, 0.134835, 0.134835, 0.134835, 0.134835,
        0.134835, 0.134835, 0.134835, 0.134835, 0.134835, 0.134835, 0.134835, 0.134835, 0.134835,
        0.134835, 0.166877, 0.166877, 0.166877, 0.166877, 0.166877, 0.166877, 0.166877, 0.166877,
        0.166877, 0.166877, 0.166877, 0.166877, 0.166877, 0.166877, 0.166877, 0.166877, 0.166877,
        0.166877, 0.166877, 0.166877, 0.166877, 0.166877, 0.166877, 0.166877, 0.166877, 0.166877,
        0.166877, 0.166877, 0.166877, 0.166877, 0.196866, 0.196866, 0.196866, 0.196866, 0.196866,
        0.196866, 0.196866, 0.196866, 0.196866, 0.196866, 0.196866, 0.196866, 0.196866, 0.196866,
        0.196866, 0.196866, 0.196866, 0.196866, 0.196866, 0.196866, 0.196866, 0.196866, 0.196866,
        0.196866, 0.196866, 0.196866, 0.196866, 0.196866, 0.196866, 0.196866, 0.224476, 0.224476,
        0.224476, 0.224476, 0.224476, 0.224476, 0.224476, 0.224476, 0.224476, 0.224476, 0.224476,
        0.224476, 0.224476, 0.224476, 0.224476, 0.224476, 0.224476, 0.224476, 0.224476, 0.224476,
        0.224476, 0.224476, 0.224476, 0.224476, 0.224476, 0.224476, 0.224476, 0.224476, 0.224476,
        0.224476, 0.289559, 0.289559, 0.289559, 0.289559, 0.289559, 0.289559, 0.289559, 0.289559,
        0.289559, 0.289559, 0.289559, 0.289559, 0.289559, 0.289559, 0.289559, 0.289559, 0.289559,
        0.289559, 0.289559, 0.289559, 0.289559, 0.289559, 0.289559, 0.289559, 0.289559, 0.289559,
        0.289559, 0.289559, 0.289559, 0.289559, 0.361086, 0.361086, 0.361086, 0.361086, 0.361086,
        0.361086, 0.361086, 0.361086, 0.361086, 0.361086, 0.361086, 0.361086, 0.361086, 0.361086,
        0.361086, 0.361086, 0.361086, 0.361086, 0.361086, 0.361086, 0.361086, 0.361086, 0.361086,
        0.361086, 0.361086, 0.361086, 0.361086, 0.361086, 0.361086, 0.361086, 0.272473, 0.272473,
        0.272473, 0.272473, 0.272473, 0.272473, 0.272473, 0.272473, 0.272473, 0.272473, 0.272473,
        0.272473, 0.272473, 0.272473, 0.272473, 0.272473, 0.272473, 0.272473, 0.272473, 0.272473,
        0.272473, 0.272473, 0.272473, 0.272473, 0.272473, 0.272473, 0.272473, 0.272473, 0.272473,
        0.272473, 0.0996614, 0.0996614, 0.0996614, 0.0996614, 0.0996614, 0.0996614, 0.0996614,
        0.0996614, 0.0996614, 0.0996614, 0.0996614, 0.0996614, 0.0996614, 0.0996614, 0.0996614,
        0.0996614, 0.0996614, 0.0996614, 0.0996614, 0.0996614, 0.0996614, 0.0996614, 0.0996614,
        0.0996614, 0.0996614, 0.0996614, 0.0996614, 0.0996614, 0.0996614, 0.0996614, 0.0085943,
        0.0085943, 0.0085943, 0.0085943, 0.0085943, 0.0085943, 0.0085943, 0.0085943, 0.0085943,
        0.0085943, 0.0085943, 0.0085943, 0.0085943, 0.0085943, 0.0085943, 0.0085943, 0.0085943,
        0.0085943, 0.0085943, 0.0085943, 0.0085943, 0.0085943, 0.0085943, 0.0085943, 0.0085943,
        0.0085943, 0.0085943, 0.0085943, 0.0085943, 0.0085943, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
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
        0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328,
        0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328,
        0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328,
        0.25056, 0.25056, 0.25056, 0.25056, 0.25056, 0.25056, 0.25056, 0.25056, 0.25056, 0.25056,
        0.25056, 0.25056, 0.25056, 0.25056, 0.25056, 0.25056, 0.25056, 0.25056, 0.25056, 0.25056,
        0.25056, 0.25056, 0.25056, 0.25056, 0.25056, 0.25056, 0.25056, 0.25056, 0.25056, 0.25056,
        0.32832, 0.32832, 0.32832, 0.32832, 0.32832, 0.32832, 0.32832, 0.32832, 0.32832, 0.32832,
        0.32832, 0.32832, 0.32832, 0.32832, 0.32832, 0.32832, 0.32832, 0.32832, 0.32832, 0.32832,
        0.32832, 0.32832, 0.32832, 0.32832, 0.32832, 0.32832, 0.32832, 0.32832, 0.32832, 0.32832,
        0.19008, 0.19008, 0.19008, 0.19008, 0.19008, 0.19008, 0.19008, 0.19008, 0.19008, 0.19008,
        0.19008, 0.19008, 0.19008, 0.19008, 0.19008, 0.19008, 0.19008, 0.19008, 0.19008, 0.19008,
        0.19008, 0.19008, 0.19008, 0.19008, 0.19008, 0.19008, 0.19008, 0.19008, 0.19008, 0.19008,
        0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328,
        0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328,
        0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328, 0.23328,
        0.37063, 0.37063, 0.37063, 0.37063, 0.37063, 0.37063, 0.37063, 0.37063, 0.37063, 0.37063,
        0.37063, 0.37063, 0.37063, 0.37063, 0.37063, 0.37063, 0.37063, 0.37063, 0.37063, 0.37063,
        0.37063, 0.37063, 0.37063, 0.37063, 0.37063, 0.37063, 0.37063, 0.37063, 0.37063, 0.37063,
        0.41063, 0.41063, 0.41063, 0.41063, 0.41063, 0.41063, 0.41063, 0.41063, 0.41063, 0.41063,
        0.41063, 0.41063, 0.41063, 0.41063, 0.41063, 0.41063, 0.41063, 0.41063, 0.41063, 0.41063,
        0.41063, 0.41063, 0.41063, 0.41063, 0.41063, 0.41063, 0.41063, 0.41063, 0.41063, 0.41063,
        0.32136, 0.32136, 0.32136, 0.32136, 0.32136, 0.32136, 0.32136, 0.32136, 0.32136, 0.32136,
        0.32136, 0.32136, 0.32136, 0.32136, 0.32136, 0.32136, 0.32136, 0.32136, 0.32136, 0.32136,
        0.32136, 0.32136, 0.32136, 0.32136, 0.32136, 0.32136, 0.32136, 0.32136, 0.32136, 0.32136,
        0.2678, 0.2678, 0.2678, 0.2678, 0.2678, 0.2678, 0.2678, 0.2678, 0.2678, 0.2678, 0.2678,
        0.2678, 0.2678, 0.2678, 0.2678, 0.2678, 0.2678, 0.2678, 0.2678, 0.2678, 0.2678, 0.2678,
        0.2678, 0.2678, 0.2678, 0.2678, 0.2678, 0.2678, 0.2678, 0.2678, 0.24995, 0.24995, 0.24995,
        0.24995, 0.24995, 0.24995, 0.24995, 0.24995, 0.24995, 0.24995, 0.24995, 0.24995, 0.24995,
        0.24995, 0.24995, 0.24995, 0.24995, 0.24995, 0.24995, 0.24995, 0.24995, 0.24995, 0.24995,
        0.24995, 0.24995, 0.24995, 0.24995, 0.24995, 0.24995, 0.24995, 0.21424, 0.21424, 0.21424,
        0.21424, 0.21424, 0.21424, 0.21424, 0.21424, 0.21424, 0.21424, 0.21424, 0.21424, 0.21424,
        0.21424, 0.21424, 0.21424, 0.21424, 0.21424, 0.21424, 0.21424, 0.21424, 0.21424, 0.21424,
        0.21424, 0.21424, 0.21424, 0.21424, 0.21424, 0.21424, 0.21424, 0.20531, 0.20531, 0.20531,
        0.20531, 0.20531, 0.20531, 0.20531, 0.20531, 0.20531, 0.20531, 0.20531, 0.20531, 0.20531,
        0.20531, 0.20531, 0.20531, 0.20531, 0.20531, 0.20531, 0.20531, 0.20531, 0.20531, 0.20531,
        0.20531, 0.20531, 0.20531, 0.20531, 0.20531, 0.20531, 0.20531, 0.20531, 0.20531, 0.20531,
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
        0.01341, 0.01341, 0.01341, 0.01341, 0.01341, 0.01341, 0.01341, 0.01341, 0.01341, 0.01341,
        0.01341, 0.01341, 0.01341, 0.01341, 0.01341, 0.01341, 0.01341, 0.01341, 0.01341, 0.01341,
        0.01341, 0.01341, 0.01341, 0.01341, 0.01341, 0.01341, 0.01341, 0.01341, 0.01341, 0.01341,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0.00101, 0.00101, 0.00101, 0.00101, 0.00101, 0.00101, 0.00101, 0.00101, 0.00101, 0.00101,
        0.00101, 0.00101, 0.00101, 0.00101, 0.00101, 0.00101, 0.00101, 0.00101, 0.00101, 0.00101,
        0.00101, 0.00101, 0.00101, 0.00101, 0.00101, 0.00101, 0.00101, 0.00101, 0.00101, 0.00101,
        0.03745, 0.03745, 0.03745, 0.03745, 0.03745, 0.03745, 0.03745, 0.03745, 0.03745, 0.03745,
        0.03745, 0.03745, 0.03745, 0.03745, 0.03745, 0.03745, 0.03745, 0.03745, 0.03745, 0.03745,
        0.03745, 0.03745, 0.03745, 0.03745, 0.03745, 0.03745, 0.03745, 0.03745, 0.03745, 0.03745,
        0.11647, 0.11647, 0.11647, 0.11647, 0.11647, 0.11647, 0.11647, 0.11647, 0.11647, 0.11647,
        0.11647, 0.11647, 0.11647, 0.11647, 0.11647, 0.11647, 0.11647, 0.11647, 0.11647, 0.11647,
        0.11647, 0.11647, 0.11647, 0.11647, 0.11647, 0.11647, 0.11647, 0.11647, 0.11647, 0.11647,
        0.16842, 0.16842, 0.16842, 0.16842, 0.16842, 0.16842, 0.16842, 0.16842, 0.16842, 0.16842,
        0.16842, 0.16842, 0.16842, 0.16842, 0.16842, 0.16842, 0.16842, 0.16842, 0.16842, 0.16842,
        0.16842, 0.16842, 0.16842, 0.16842, 0.16842, 0.16842, 0.16842, 0.16842, 0.16842, 0.16842,
        0.24129, 0.24129, 0.24129, 0.24129, 0.24129, 0.24129, 0.24129, 0.24129, 0.24129, 0.24129,
        0.24129, 0.24129, 0.24129, 0.24129, 0.24129, 0.24129, 0.24129, 0.24129, 0.24129, 0.24129,
        0.24129, 0.24129, 0.24129, 0.24129, 0.24129, 0.24129, 0.24129, 0.24129, 0.24129, 0.24129,
        0.21767, 0.21767, 0.21767, 0.21767, 0.21767, 0.21767, 0.21767, 0.21767, 0.21767, 0.21767,
        0.21767, 0.21767, 0.21767, 0.21767, 0.21767, 0.21767, 0.21767, 0.21767, 0.21767, 0.21767,
        0.21767, 0.21767, 0.21767, 0.21767, 0.21767, 0.21767, 0.21767, 0.21767, 0.21767, 0.21767,
        0.08906, 0.08906, 0.08906, 0.08906, 0.08906, 0.08906, 0.08906, 0.08906, 0.08906, 0.08906,
        0.08906, 0.08906, 0.08906, 0.08906, 0.08906, 0.08906, 0.08906, 0.08906, 0.08906, 0.08906,
        0.08906, 0.08906, 0.08906, 0.08906, 0.08906, 0.08906, 0.08906, 0.08906, 0.08906, 0.08906,
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
        0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667,
        0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667,
        0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667,
        1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5,
        1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 0.96667, 0.96667, 0.96667,
        0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667,
        0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667,
        0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.83333, 0.83333, 0.83333,
        0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333,
        0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333,
        0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 1.03333, 1.03333, 1.03333,
        1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333,
        1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333,
        1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.56667, 1.56667, 1.56667,
        1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667,
        1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667,
        1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 2.5, 2.5, 2.5, 2.5, 2.5,
        2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5,
        2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6,
        3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6,
        3.6, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667,
        4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667,
        4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667,
        4.46667, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333,
        4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333,
        4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333,
        4.93333, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8,
        4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 3.7, 3.7, 3.7, 3.7,
        3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7,
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
        0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
        0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
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
        0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
        0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
        0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
        0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
        0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
        0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
        0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
        0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
        0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
        0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
        0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
        0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
        0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
        0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
        0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
        0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
        0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
        0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
        0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
        0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
        0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
        0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
        0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
        0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
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
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
        0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
        0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06,
        0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06,
        0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05,
        0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05,
        0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06,
        0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06,
        0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05,
        0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05,
        0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02,
        0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02,
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
    Original Eqn: b'( [(1,0)-(365,0.2)],(1,0.0412677),(2,0.0412677),(3,0.0412677),(4,0.0412677),(5,0.0412677\\\\ ),(6,0.0412677),(7,0.0412677),(8,0.0412677),(9,0.0412677),(10,0.0412677),(11,0.0412677\\\\ ),(12,0.0412677),(13,0.0412677),(14,0.0412677),(15,0.0412677),(16,0.0412677),(17,0.0412677\\\\ ),(18,0.0412677),(19,0.0412677),(20,0.0412677),(21,0.0412677),(22,0.0412677),(23,0.0412677\\\\ ),(24,0.0412677),(25,0.0412677),(26,0.0412677),(27,0.0412677),(28,0.0412677),(29,0.0412677\\\\ ),(30,0.0412677),(31,0.0455649),(32,0.0455649),(33,0.0455649),(34,0.0455649),(35,0.0455649\\\\ ),(36,0.0455649),(37,0.0455649),(38,0.0455649),(39,0.0455649),(40,0.0455649),(41,0.0455649\\\\ ),(42,0.0455649),(43,0.0455649),(44,0.0455649),(45,0.0455649),(46,0.0455649),(47,0.0455649\\\\ ),(48,0.0455649),(49,0.0455649),(50,0.0455649),(51,0.0455649),(52,0.0455649),(53,0.0455649\\\\ ),(54,0.0455649),(55,0.0455649),(56,0.0455649),(57,0.0455649),(58,0.0455649),(59,0.0455649\\\\ ),(60,0.0455649),(61,0.05162),(62,0.05162),(63,0.05162),(64,0.05162),(65,0.05162),(\\\\ 66,0.05162),(67,0.05162),(68,0.05162),(69,0.05162),(70,0.05162),(71,0.05162),(72,0.05162\\\\ ),(73,0.05162),(74,0.05162),(75,0.05162),(76,0.05162),(77,0.05162),(78,0.05162),(79\\\\ ,0.05162),(80,0.05162),(81,0.05162),(82,0.05162),(83,0.05162),(84,0.05162),(85,0.05162\\\\ ),(86,0.05162),(87,0.05162),(88,0.05162),(89,0.05162),(90,0.05162),(91,0.0515981),(\\\\ 92,0.0515981),(93,0.0515981),(94,0.0515981),(95,0.0515981),(96,0.0515981),(97,0.0515981\\\\ ),(98,0.0515981),(99,0.0515981),(100,0.0515981),(101,0.0515981),(102,0.0515981),(103\\\\ ,0.0515981),(104,0.0515981),(105,0.0515981),(106,0.0515981),(107,0.0515981),(108,0.0515981\\\\ ),(109,0.0515981),(110,0.0515981),(111,0.0515981),(112,0.0515981),(113,0.0515981),(\\\\ 114,0.0515981),(115,0.0515981),(116,0.0515981),(117,0.0515981),(118,0.0515981),(119\\\\ ,0.0515981),(120,0.0515981),(121,0.0635695),(122,0.0635695),(123,0.0635695),(124,0.0635695\\\\ ),(125,0.0635695),(126,0.0635695),(127,0.0635695),(128,0.0635695),(129,0.0635695),(\\\\ 130,0.0635695),(131,0.0635695),(132,0.0635695),(133,0.0635695),(134,0.0635695),(135\\\\ ,0.0635695),(136,0.0635695),(137,0.0635695),(138,0.0635695),(139,0.0635695),(140,0.0635695\\\\ ),(141,0.0635695),(142,0.0635695),(143,0.0635695),(144,0.0635695),(145,0.0635695),(\\\\ 146,0.0635695),(147,0.0635695),(148,0.0635695),(149,0.0635695),(150,0.0635695),(151\\\\ ,0.0873189),(152,0.0873189),(153,0.0873189),(154,0.0873189),(155,0.0873189),(156,0.0873189\\\\ ),(157,0.0873189),(158,0.0873189),(159,0.0873189),(160,0.0873189),(161,0.0873189),(\\\\ 162,0.0873189),(163,0.0873189),(164,0.0873189),(165,0.0873189),(166,0.0873189),(167\\\\ ,0.0873189),(168,0.0873189),(169,0.0873189),(170,0.0873189),(171,0.0873189),(172,0.0873189\\\\ ),(173,0.0873189),(174,0.0873189),(175,0.0873189),(176,0.0873189),(177,0.0873189),(\\\\ 178,0.0873189),(179,0.0873189),(180,0.0873189),(181,0.108824),(182,0.108824),(183,0.108824\\\\ ),(184,0.108824),(185,0.108824),(186,0.108824),(187,0.108824),(188,0.108824),(189,0.108824\\\\ ),(190,0.108824),(191,0.108824),(192,0.108824),(193,0.108824),(194,0.108824),(195,0.108824\\\\ ),(196,0.108824),(197,0.108824),(198,0.108824),(199,0.108824),(200,0.108824),(201,0.108824\\\\ ),(202,0.108824),(203,0.108824),(204,0.108824),(205,0.108824),(206,0.108824),(207,0.108824\\\\ ),(208,0.108824),(209,0.108824),(210,0.108824),(211,0.0754385),(212,0.0754385),(213\\\\ ,0.0754385),(214,0.0754385),(215,0.0754385),(216,0.0754385),(217,0.0754385),(218,0.0754385\\\\ ),(219,0.0754385),(220,0.0754385),(221,0.0754385),(222,0.0754385),(223,0.0754385),(\\\\ 224,0.0754385),(225,0.0754385),(226,0.0754385),(227,0.0754385),(228,0.0754385),(229\\\\ ,0.0754385),(230,0.0754385),(231,0.0754385),(232,0.0754385),(233,0.0754385),(234,0.0754385\\\\ ),(235,0.0754385),(236,0.0754385),(237,0.0754385),(238,0.0754385),(239,0.0754385),(\\\\ 240,0.0754385),(241,0.0514541),(242,0.0514541),(243,0.0514541),(244,0.0514541),(245\\\\ ,0.0514541),(246,0.0514541),(247,0.0514541),(248,0.0514541),(249,0.0514541),(250,0.0514541\\\\ ),(251,0.0514541),(252,0.0514541),(253,0.0514541),(254,0.0514541),(255,0.0514541),(\\\\ 256,0.0514541),(257,0.0514541),(258,0.0514541),(259,0.0514541),(260,0.0514541),(261\\\\ ,0.0514541),(262,0.0514541),(263,0.0514541),(264,0.0514541),(265,0.0514541),(266,0.0514541\\\\ ),(267,0.0514541),(268,0.0514541),(269,0.0514541),(270,0.0514541),(271,0.043286),(272\\\\ ,0.043286),(273,0.043286),(274,0.043286),(275,0.043286),(276,0.043286),(277,0.043286\\\\ ),(278,0.043286),(279,0.043286),(280,0.043286),(281,0.043286),(282,0.043286),(283,0.043286\\\\ ),(284,0.043286),(285,0.043286),(286,0.043286),(287,0.043286),(288,0.043286),(289,0.043286\\\\ ),(290,0.043286),(291,0.043286),(292,0.043286),(293,0.043286),(294,0.043286),(295,0.043286\\\\ ),(296,0.043286),(297,0.043286),(298,0.043286),(299,0.043286),(300,0.043286),(301,0.040713\\\\ ),(302,0.040713),(303,0.040713),(304,0.040713),(305,0.040713),(306,0.040713),(307,0.040713\\\\ ),(308,0.040713),(309,0.040713),(310,0.040713),(311,0.040713),(312,0.040713),(313,0.040713\\\\ ),(314,0.040713),(315,0.040713),(316,0.040713),(317,0.040713),(318,0.040713),(319,0.040713\\\\ ),(320,0.040713),(321,0.040713),(322,0.040713),(323,0.040713),(324,0.040713),(325,0.040713\\\\ ),(326,0.040713),(327,0.040713),(328,0.040713),(329,0.040713),(330,0.040713),(331,0.0389759\\\\ ),(332,0.0389759),(333,0.0389759),(334,0.0389759),(335,0.0389759),(336,0.0389759),(\\\\ 337,0.0389759),(338,0.0389759),(339,0.0389759),(340,0.0389759),(341,0.0389759),(342\\\\ ,0.0389759),(343,0.0389759),(344,0.0389759),(345,0.0389759),(346,0.0389759),(347,0.0389759\\\\ ),(348,0.0389759),(349,0.0389759),(350,0.0389759),(351,0.0389759),(352,0.0389759),(\\\\ 353,0.0389759),(354,0.0389759),(355,0.0389759),(356,0.0389759),(357,0.0389759),(358\\\\ ,0.0389759),(359,0.0389759),(360,0.0389759),(361,0.0389759),(362,0.0389759),(363,0.0389759\\\\ ),(364,0.0389759),(365,0.0389759))'
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
        0.0412677, 0.0412677, 0.0412677, 0.0412677, 0.0412677, 0.0412677, 0.0412677, 0.0412677,
        0.0412677, 0.0412677, 0.0412677, 0.0412677, 0.0412677, 0.0412677, 0.0412677, 0.0412677,
        0.0412677, 0.0412677, 0.0412677, 0.0412677, 0.0412677, 0.0412677, 0.0412677, 0.0412677,
        0.0412677, 0.0412677, 0.0412677, 0.0412677, 0.0412677, 0.0412677, 0.0455649, 0.0455649,
        0.0455649, 0.0455649, 0.0455649, 0.0455649, 0.0455649, 0.0455649, 0.0455649, 0.0455649,
        0.0455649, 0.0455649, 0.0455649, 0.0455649, 0.0455649, 0.0455649, 0.0455649, 0.0455649,
        0.0455649, 0.0455649, 0.0455649, 0.0455649, 0.0455649, 0.0455649, 0.0455649, 0.0455649,
        0.0455649, 0.0455649, 0.0455649, 0.0455649, 0.05162, 0.05162, 0.05162, 0.05162, 0.05162,
        0.05162, 0.05162, 0.05162, 0.05162, 0.05162, 0.05162, 0.05162, 0.05162, 0.05162, 0.05162,
        0.05162, 0.05162, 0.05162, 0.05162, 0.05162, 0.05162, 0.05162, 0.05162, 0.05162, 0.05162,
        0.05162, 0.05162, 0.05162, 0.05162, 0.05162, 0.0515981, 0.0515981, 0.0515981, 0.0515981,
        0.0515981, 0.0515981, 0.0515981, 0.0515981, 0.0515981, 0.0515981, 0.0515981, 0.0515981,
        0.0515981, 0.0515981, 0.0515981, 0.0515981, 0.0515981, 0.0515981, 0.0515981, 0.0515981,
        0.0515981, 0.0515981, 0.0515981, 0.0515981, 0.0515981, 0.0515981, 0.0515981, 0.0515981,
        0.0515981, 0.0515981, 0.0635695, 0.0635695, 0.0635695, 0.0635695, 0.0635695, 0.0635695,
        0.0635695, 0.0635695, 0.0635695, 0.0635695, 0.0635695, 0.0635695, 0.0635695, 0.0635695,
        0.0635695, 0.0635695, 0.0635695, 0.0635695, 0.0635695, 0.0635695, 0.0635695, 0.0635695,
        0.0635695, 0.0635695, 0.0635695, 0.0635695, 0.0635695, 0.0635695, 0.0635695, 0.0635695,
        0.0873189, 0.0873189, 0.0873189, 0.0873189, 0.0873189, 0.0873189, 0.0873189, 0.0873189,
        0.0873189, 0.0873189, 0.0873189, 0.0873189, 0.0873189, 0.0873189, 0.0873189, 0.0873189,
        0.0873189, 0.0873189, 0.0873189, 0.0873189, 0.0873189, 0.0873189, 0.0873189, 0.0873189,
        0.0873189, 0.0873189, 0.0873189, 0.0873189, 0.0873189, 0.0873189, 0.108824, 0.108824,
        0.108824, 0.108824, 0.108824, 0.108824, 0.108824, 0.108824, 0.108824, 0.108824, 0.108824,
        0.108824, 0.108824, 0.108824, 0.108824, 0.108824, 0.108824, 0.108824, 0.108824, 0.108824,
        0.108824, 0.108824, 0.108824, 0.108824, 0.108824, 0.108824, 0.108824, 0.108824, 0.108824,
        0.108824, 0.0754385, 0.0754385, 0.0754385, 0.0754385, 0.0754385, 0.0754385, 0.0754385,
        0.0754385, 0.0754385, 0.0754385, 0.0754385, 0.0754385, 0.0754385, 0.0754385, 0.0754385,
        0.0754385, 0.0754385, 0.0754385, 0.0754385, 0.0754385, 0.0754385, 0.0754385, 0.0754385,
        0.0754385, 0.0754385, 0.0754385, 0.0754385, 0.0754385, 0.0754385, 0.0754385, 0.0514541,
        0.0514541, 0.0514541, 0.0514541, 0.0514541, 0.0514541, 0.0514541, 0.0514541, 0.0514541,
        0.0514541, 0.0514541, 0.0514541, 0.0514541, 0.0514541, 0.0514541, 0.0514541, 0.0514541,
        0.0514541, 0.0514541, 0.0514541, 0.0514541, 0.0514541, 0.0514541, 0.0514541, 0.0514541,
        0.0514541, 0.0514541, 0.0514541, 0.0514541, 0.0514541, 0.043286, 0.043286, 0.043286,
        0.043286, 0.043286, 0.043286, 0.043286, 0.043286, 0.043286, 0.043286, 0.043286, 0.043286,
        0.043286, 0.043286, 0.043286, 0.043286, 0.043286, 0.043286, 0.043286, 0.043286, 0.043286,
        0.043286, 0.043286, 0.043286, 0.043286, 0.043286, 0.043286, 0.043286, 0.043286, 0.043286,
        0.040713, 0.040713, 0.040713, 0.040713, 0.040713, 0.040713, 0.040713, 0.040713, 0.040713,
        0.040713, 0.040713, 0.040713, 0.040713, 0.040713, 0.040713, 0.040713, 0.040713, 0.040713,
        0.040713, 0.040713, 0.040713, 0.040713, 0.040713, 0.040713, 0.040713, 0.040713, 0.040713,
        0.040713, 0.040713, 0.040713, 0.0389759, 0.0389759, 0.0389759, 0.0389759, 0.0389759,
        0.0389759, 0.0389759, 0.0389759, 0.0389759, 0.0389759, 0.0389759, 0.0389759, 0.0389759,
        0.0389759, 0.0389759, 0.0389759, 0.0389759, 0.0389759, 0.0389759, 0.0389759, 0.0389759,
        0.0389759, 0.0389759, 0.0389759, 0.0389759, 0.0389759, 0.0389759, 0.0389759, 0.0389759,
        0.0389759, 0.0389759, 0.0389759, 0.0389759, 0.0389759, 0.0389759
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
        5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51,
        9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0,
        0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81,
        9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0,
        0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98,
        7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0,
        0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86,
        5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44,
        7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48,
        5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51,
        9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0,
        0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81,
        9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0,
        0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98,
        7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0,
        0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86,
        5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44,
        7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48,
        5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51,
        9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0,
        0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81,
        9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0,
        0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98,
        7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0,
        0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86,
        5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44,
        7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48,
        5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51,
        9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0,
        0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81,
        9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0,
        0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98,
        7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0,
        0.44, 7.51, 9.81, 9.98, 7.86, 5.48, 5.21, 0, 0, 0, 0, 0, 0.44, 7.51, 9.81, 9.98, 7.86, 5.48
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
        0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
        0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
        0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
        0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
        0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
        0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
        0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
        0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
        0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
        0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
        0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
        0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
        0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
        0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
        0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
        0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
        0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
        0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
        0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
        0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
        0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
        0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
        0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
        0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13,
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
    Original Eqn: b'( [(1,0)-(365,0.2)],(1,0.0835446),(2,0.0835446),(3,0.0835446),(4,0.0835446),(5,0.0835446\\\\ ),(6,0.0835446),(7,0.0835446),(8,0.0835446),(9,0.0835446),(10,0.0835446),(11,0.0835446\\\\ ),(12,0.0835446),(13,0.0835446),(14,0.0835446),(15,0.0835446),(16,0.0835446),(17,0.0835446\\\\ ),(18,0.0835446),(19,0.0835446),(20,0.0835446),(21,0.0835446),(22,0.0835446),(23,0.0835446\\\\ ),(24,0.0835446),(25,0.0835446),(26,0.0835446),(27,0.0835446),(28,0.0835446),(29,0.0835446\\\\ ),(30,0.0835446),(31,0.0911704),(32,0.0911704),(33,0.0911704),(34,0.0911704),(35,0.0911704\\\\ ),(36,0.0911704),(37,0.0911704),(38,0.0911704),(39,0.0911704),(40,0.0911704),(41,0.0911704\\\\ ),(42,0.0911704),(43,0.0911704),(44,0.0911704),(45,0.0911704),(46,0.0911704),(47,0.0911704\\\\ ),(48,0.0911704),(49,0.0911704),(50,0.0911704),(51,0.0911704),(52,0.0911704),(53,0.0911704\\\\ ),(54,0.0911704),(55,0.0911704),(56,0.0911704),(57,0.0911704),(58,0.0911704),(59,0.0911704\\\\ ),(60,0.0911704),(61,0.075059),(62,0.075059),(63,0.075059),(64,0.075059),(65,0.075059\\\\ ),(66,0.075059),(67,0.075059),(68,0.075059),(69,0.075059),(70,0.075059),(71,0.075059\\\\ ),(72,0.075059),(73,0.075059),(74,0.075059),(75,0.075059),(76,0.075059),(77,0.075059\\\\ ),(78,0.075059),(79,0.075059),(80,0.075059),(81,0.075059),(82,0.075059),(83,0.075059\\\\ ),(84,0.075059),(85,0.075059),(86,0.075059),(87,0.075059),(88,0.075059),(89,0.075059\\\\ ),(90,0.075059),(91,0.089665),(92,0.089665),(93,0.089665),(94,0.089665),(95,0.089665\\\\ ),(96,0.089665),(97,0.089665),(98,0.089665),(99,0.089665),(100,0.089665),(101,0.089665\\\\ ),(102,0.089665),(103,0.089665),(104,0.089665),(105,0.089665),(106,0.089665),(107,0.089665\\\\ ),(108,0.089665),(109,0.089665),(110,0.089665),(111,0.089665),(112,0.089665),(113,0.089665\\\\ ),(114,0.089665),(115,0.089665),(116,0.089665),(117,0.089665),(118,0.089665),(119,0.089665\\\\ ),(120,0.089665),(121,0.118193),(122,0.118193),(123,0.118193),(124,0.118193),(125,0.118193\\\\ ),(126,0.118193),(127,0.118193),(128,0.118193),(129,0.118193),(130,0.118193),(131,0.118193\\\\ ),(132,0.118193),(133,0.118193),(134,0.118193),(135,0.118193),(136,0.118193),(137,0.118193\\\\ ),(138,0.118193),(139,0.118193),(140,0.118193),(141,0.118193),(142,0.118193),(143,0.118193\\\\ ),(144,0.118193),(145,0.118193),(146,0.118193),(147,0.118193),(148,0.118193),(149,0.118193\\\\ ),(150,0.118193),(151,0.14769),(152,0.14769),(153,0.14769),(154,0.14769),(155,0.14769\\\\ ),(156,0.14769),(157,0.14769),(158,0.14769),(159,0.14769),(160,0.14769),(161,0.14769\\\\ ),(162,0.14769),(163,0.14769),(164,0.14769),(165,0.14769),(166,0.14769),(167,0.14769\\\\ ),(168,0.14769),(169,0.14769),(170,0.14769),(171,0.14769),(172,0.14769),(173,0.14769\\\\ ),(174,0.14769),(175,0.14769),(176,0.14769),(177,0.14769),(178,0.14769),(179,0.14769\\\\ ),(180,0.14769),(181,0.172278),(182,0.172278),(183,0.172278),(184,0.172278),(185,0.172278\\\\ ),(186,0.172278),(187,0.172278),(188,0.172278),(189,0.172278),(190,0.172278),(191,0.172278\\\\ ),(192,0.172278),(193,0.172278),(194,0.172278),(195,0.172278),(196,0.172278),(197,0.172278\\\\ ),(198,0.172278),(199,0.172278),(200,0.172278),(201,0.172278),(202,0.172278),(203,0.172278\\\\ ),(204,0.172278),(205,0.172278),(206,0.172278),(207,0.172278),(208,0.172278),(209,0.172278\\\\ ),(210,0.172278),(211,0.161028),(212,0.161028),(213,0.161028),(214,0.161028),(215,0.161028\\\\ ),(216,0.161028),(217,0.161028),(218,0.161028),(219,0.161028),(220,0.161028),(221,0.161028\\\\ ),(222,0.161028),(223,0.161028),(224,0.161028),(225,0.161028),(226,0.161028),(227,0.161028\\\\ ),(228,0.161028),(229,0.161028),(230,0.161028),(231,0.161028),(232,0.161028),(233,0.161028\\\\ ),(234,0.161028),(235,0.161028),(236,0.161028),(237,0.161028),(238,0.161028),(239,0.161028\\\\ ),(240,0.161028),(241,0.108693),(242,0.108693),(243,0.108693),(244,0.108693),(245,0.108693\\\\ ),(246,0.108693),(247,0.108693),(248,0.108693),(249,0.108693),(250,0.108693),(251,0.108693\\\\ ),(252,0.108693),(253,0.108693),(254,0.108693),(255,0.108693),(256,0.108693),(257,0.108693\\\\ ),(258,0.108693),(259,0.108693),(260,0.108693),(261,0.108693),(262,0.108693),(263,0.108693\\\\ ),(264,0.108693),(265,0.108693),(266,0.108693),(267,0.108693),(268,0.108693),(269,0.108693\\\\ ),(270,0.108693),(271,0.0867655),(272,0.0867655),(273,0.0867655),(274,0.0867655),(275\\\\ ,0.0867655),(276,0.0867655),(277,0.0867655),(278,0.0867655),(279,0.0867655),(280,0.0867655\\\\ ),(281,0.0867655),(282,0.0867655),(283,0.0867655),(284,0.0867655),(285,0.0867655),(\\\\ 286,0.0867655),(287,0.0867655),(288,0.0867655),(289,0.0867655),(290,0.0867655),(291\\\\ ,0.0867655),(292,0.0867655),(293,0.0867655),(294,0.0867655),(295,0.0867655),(296,0.0867655\\\\ ),(297,0.0867655),(298,0.0867655),(299,0.0867655),(300,0.0867655),(301,0.0532128),(\\\\ 302,0.0532128),(303,0.0532128),(304,0.0532128),(305,0.0532128),(306,0.0532128),(307\\\\ ,0.0532128),(308,0.0532128),(309,0.0532128),(310,0.0532128),(311,0.0532128),(312,0.0532128\\\\ ),(313,0.0532128),(314,0.0532128),(315,0.0532128),(316,0.0532128),(317,0.0532128),(\\\\ 318,0.0532128),(319,0.0532128),(320,0.0532128),(321,0.0532128),(322,0.0532128),(323\\\\ ,0.0532128),(324,0.0532128),(325,0.0532128),(326,0.0532128),(327,0.0532128),(328,0.0532128\\\\ ),(329,0.0532128),(330,0.0532128),(331,0.0901026),(332,0.0901026),(333,0.0901026),(\\\\ 334,0.0901026),(335,0.0901026),(336,0.0901026),(337,0.0901026),(338,0.0901026),(339\\\\ ,0.0901026),(340,0.0901026),(341,0.0901026),(342,0.0901026),(343,0.0901026),(344,0.0901026\\\\ ),(345,0.0901026),(346,0.0901026),(347,0.0901026),(348,0.0901026),(349,0.0901026),(\\\\ 350,0.0901026),(351,0.0901026),(352,0.0901026),(353,0.0901026),(354,0.0901026),(355\\\\ ,0.0901026),(356,0.0901026),(357,0.0901026),(358,0.0901026),(359,0.0901026),(360,0.0901026\\\\ ),(361,0.0901026),(362,0.0901026),(363,0.0901026),(364,0.0901026),(365,0.0901026))'
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
        0.0835446, 0.0835446, 0.0835446, 0.0835446, 0.0835446, 0.0835446, 0.0835446, 0.0835446,
        0.0835446, 0.0835446, 0.0835446, 0.0835446, 0.0835446, 0.0835446, 0.0835446, 0.0835446,
        0.0835446, 0.0835446, 0.0835446, 0.0835446, 0.0835446, 0.0835446, 0.0835446, 0.0835446,
        0.0835446, 0.0835446, 0.0835446, 0.0835446, 0.0835446, 0.0835446, 0.0911704, 0.0911704,
        0.0911704, 0.0911704, 0.0911704, 0.0911704, 0.0911704, 0.0911704, 0.0911704, 0.0911704,
        0.0911704, 0.0911704, 0.0911704, 0.0911704, 0.0911704, 0.0911704, 0.0911704, 0.0911704,
        0.0911704, 0.0911704, 0.0911704, 0.0911704, 0.0911704, 0.0911704, 0.0911704, 0.0911704,
        0.0911704, 0.0911704, 0.0911704, 0.0911704, 0.075059, 0.075059, 0.075059, 0.075059,
        0.075059, 0.075059, 0.075059, 0.075059, 0.075059, 0.075059, 0.075059, 0.075059, 0.075059,
        0.075059, 0.075059, 0.075059, 0.075059, 0.075059, 0.075059, 0.075059, 0.075059, 0.075059,
        0.075059, 0.075059, 0.075059, 0.075059, 0.075059, 0.075059, 0.075059, 0.075059, 0.089665,
        0.089665, 0.089665, 0.089665, 0.089665, 0.089665, 0.089665, 0.089665, 0.089665, 0.089665,
        0.089665, 0.089665, 0.089665, 0.089665, 0.089665, 0.089665, 0.089665, 0.089665, 0.089665,
        0.089665, 0.089665, 0.089665, 0.089665, 0.089665, 0.089665, 0.089665, 0.089665, 0.089665,
        0.089665, 0.089665, 0.118193, 0.118193, 0.118193, 0.118193, 0.118193, 0.118193, 0.118193,
        0.118193, 0.118193, 0.118193, 0.118193, 0.118193, 0.118193, 0.118193, 0.118193, 0.118193,
        0.118193, 0.118193, 0.118193, 0.118193, 0.118193, 0.118193, 0.118193, 0.118193, 0.118193,
        0.118193, 0.118193, 0.118193, 0.118193, 0.118193, 0.14769, 0.14769, 0.14769, 0.14769,
        0.14769, 0.14769, 0.14769, 0.14769, 0.14769, 0.14769, 0.14769, 0.14769, 0.14769, 0.14769,
        0.14769, 0.14769, 0.14769, 0.14769, 0.14769, 0.14769, 0.14769, 0.14769, 0.14769, 0.14769,
        0.14769, 0.14769, 0.14769, 0.14769, 0.14769, 0.14769, 0.172278, 0.172278, 0.172278,
        0.172278, 0.172278, 0.172278, 0.172278, 0.172278, 0.172278, 0.172278, 0.172278, 0.172278,
        0.172278, 0.172278, 0.172278, 0.172278, 0.172278, 0.172278, 0.172278, 0.172278, 0.172278,
        0.172278, 0.172278, 0.172278, 0.172278, 0.172278, 0.172278, 0.172278, 0.172278, 0.172278,
        0.161028, 0.161028, 0.161028, 0.161028, 0.161028, 0.161028, 0.161028, 0.161028, 0.161028,
        0.161028, 0.161028, 0.161028, 0.161028, 0.161028, 0.161028, 0.161028, 0.161028, 0.161028,
        0.161028, 0.161028, 0.161028, 0.161028, 0.161028, 0.161028, 0.161028, 0.161028, 0.161028,
        0.161028, 0.161028, 0.161028, 0.108693, 0.108693, 0.108693, 0.108693, 0.108693, 0.108693,
        0.108693, 0.108693, 0.108693, 0.108693, 0.108693, 0.108693, 0.108693, 0.108693, 0.108693,
        0.108693, 0.108693, 0.108693, 0.108693, 0.108693, 0.108693, 0.108693, 0.108693, 0.108693,
        0.108693, 0.108693, 0.108693, 0.108693, 0.108693, 0.108693, 0.0867655, 0.0867655,
        0.0867655, 0.0867655, 0.0867655, 0.0867655, 0.0867655, 0.0867655, 0.0867655, 0.0867655,
        0.0867655, 0.0867655, 0.0867655, 0.0867655, 0.0867655, 0.0867655, 0.0867655, 0.0867655,
        0.0867655, 0.0867655, 0.0867655, 0.0867655, 0.0867655, 0.0867655, 0.0867655, 0.0867655,
        0.0867655, 0.0867655, 0.0867655, 0.0867655, 0.0532128, 0.0532128, 0.0532128, 0.0532128,
        0.0532128, 0.0532128, 0.0532128, 0.0532128, 0.0532128, 0.0532128, 0.0532128, 0.0532128,
        0.0532128, 0.0532128, 0.0532128, 0.0532128, 0.0532128, 0.0532128, 0.0532128, 0.0532128,
        0.0532128, 0.0532128, 0.0532128, 0.0532128, 0.0532128, 0.0532128, 0.0532128, 0.0532128,
        0.0532128, 0.0532128, 0.0901026, 0.0901026, 0.0901026, 0.0901026, 0.0901026, 0.0901026,
        0.0901026, 0.0901026, 0.0901026, 0.0901026, 0.0901026, 0.0901026, 0.0901026, 0.0901026,
        0.0901026, 0.0901026, 0.0901026, 0.0901026, 0.0901026, 0.0901026, 0.0901026, 0.0901026,
        0.0901026, 0.0901026, 0.0901026, 0.0901026, 0.0901026, 0.0901026, 0.0901026, 0.0901026,
        0.0901026, 0.0901026, 0.0901026, 0.0901026, 0.0901026
    ])


def zr_upstream(x):
    """
    Real Name: b'zr upstream'
    Original Eqn: b'( [(1,0)-(365,0.8)],(1,0.273879),(2,0.273879),(3,0.273879),(4,0.273879),(5,0.273879),(\\\\ 6,0.273879),(7,0.273879),(8,0.273879),(9,0.273879),(10,0.273879),(11,0.273879),(12,\\\\ 0.273879),(13,0.273879),(14,0.273879),(15,0.273879),(16,0.273879),(17,0.273879),(18\\\\ ,0.273879),(19,0.273879),(20,0.273879),(21,0.273879),(22,0.273879),(23,0.273879),(24\\\\ ,0.273879),(25,0.273879),(26,0.273879),(27,0.273879),(28,0.273879),(29,0.273879),(30\\\\ ,0.273879),(31,0.302397),(32,0.302397),(33,0.302397),(34,0.302397),(35,0.302397),(36\\\\ ,0.302397),(37,0.302397),(38,0.302397),(39,0.302397),(40,0.302397),(41,0.302397),(42\\\\ ,0.302397),(43,0.302397),(44,0.302397),(45,0.302397),(46,0.302397),(47,0.302397),(48\\\\ ,0.302397),(49,0.302397),(50,0.302397),(51,0.302397),(52,0.302397),(53,0.302397),(54\\\\ ,0.302397),(55,0.302397),(56,0.302397),(57,0.302397),(58,0.302397),(59,0.302397),(60\\\\ ,0.302397),(61,0.342583),(62,0.342583),(63,0.342583),(64,0.342583),(65,0.342583),(66\\\\ ,0.342583),(67,0.342583),(68,0.342583),(69,0.342583),(70,0.342583),(71,0.342583),(72\\\\ ,0.342583),(73,0.342583),(74,0.342583),(75,0.342583),(76,0.342583),(77,0.342583),(78\\\\ ,0.342583),(79,0.342583),(80,0.342583),(81,0.342583),(82,0.342583),(83,0.342583),(84\\\\ ,0.342583),(85,0.342583),(86,0.342583),(87,0.342583),(88,0.342583),(89,0.342583),(90\\\\ ,0.342583),(91,0.342437),(92,0.342437),(93,0.342437),(94,0.342437),(95,0.342437),(96\\\\ ,0.342437),(97,0.342437),(98,0.342437),(99,0.342437),(100,0.342437),(101,0.342437),\\\\ (102,0.342437),(103,0.342437),(104,0.342437),(105,0.342437),(106,0.342437),(107,0.342437\\\\ ),(108,0.342437),(109,0.342437),(110,0.342437),(111,0.342437),(112,0.342437),(113,0.342437\\\\ ),(114,0.342437),(115,0.342437),(116,0.342437),(117,0.342437),(118,0.342437),(119,0.342437\\\\ ),(120,0.342437),(121,0.421888),(122,0.421888),(123,0.421888),(124,0.421888),(125,0.421888\\\\ ),(126,0.421888),(127,0.421888),(128,0.421888),(129,0.421888),(130,0.421888),(131,0.421888\\\\ ),(132,0.421888),(133,0.421888),(134,0.421888),(135,0.421888),(136,0.421888),(137,0.421888\\\\ ),(138,0.421888),(139,0.421888),(140,0.421888),(141,0.421888),(142,0.421888),(143,0.421888\\\\ ),(144,0.421888),(145,0.421888),(146,0.421888),(147,0.421888),(148,0.421888),(149,0.421888\\\\ ),(150,0.421888),(151,0.579503),(152,0.579503),(153,0.579503),(154,0.579503),(155,0.579503\\\\ ),(156,0.579503),(157,0.579503),(158,0.579503),(159,0.579503),(160,0.579503),(161,0.579503\\\\ ),(162,0.579503),(163,0.579503),(164,0.579503),(165,0.579503),(166,0.579503),(167,0.579503\\\\ ),(168,0.579503),(169,0.579503),(170,0.579503),(171,0.579503),(172,0.579503),(173,0.579503\\\\ ),(174,0.579503),(175,0.579503),(176,0.579503),(177,0.579503),(178,0.579503),(179,0.579503\\\\ ),(180,0.579503),(181,0.722223),(182,0.722223),(183,0.722223),(184,0.722223),(185,0.722223\\\\ ),(186,0.722223),(187,0.722223),(188,0.722223),(189,0.722223),(190,0.722223),(191,0.722223\\\\ ),(192,0.722223),(193,0.722223),(194,0.722223),(195,0.722223),(196,0.722223),(197,0.722223\\\\ ),(198,0.722223),(199,0.722223),(200,0.722223),(201,0.722223),(202,0.722223),(203,0.722223\\\\ ),(204,0.722223),(205,0.722223),(206,0.722223),(207,0.722223),(208,0.722223),(209,0.722223\\\\ ),(210,0.722223),(211,0.494075),(212,0.494075),(213,0.494075),(214,0.494075),(215,0.494075\\\\ ),(216,0.494075),(217,0.494075),(218,0.494075),(219,0.494075),(220,0.494075),(221,0.494075\\\\ ),(222,0.494075),(223,0.494075),(224,0.494075),(225,0.494075),(226,0.494075),(227,0.494075\\\\ ),(228,0.494075),(229,0.494075),(230,0.494075),(231,0.494075),(232,0.494075),(233,0.494075\\\\ ),(234,0.494075),(235,0.494075),(236,0.494075),(237,0.494075),(238,0.494075),(239,0.494075\\\\ ),(240,0.494075),(241,0.334899),(242,0.334899),(243,0.334899),(244,0.334899),(245,0.334899\\\\ ),(246,0.334899),(247,0.334899),(248,0.334899),(249,0.334899),(250,0.334899),(251,0.334899\\\\ ),(252,0.334899),(253,0.334899),(254,0.334899),(255,0.334899),(256,0.334899),(257,0.334899\\\\ ),(258,0.334899),(259,0.334899),(260,0.334899),(261,0.334899),(262,0.334899),(263,0.334899\\\\ ),(264,0.334899),(265,0.334899),(266,0.334899),(267,0.334899),(268,0.334899),(269,0.334899\\\\ ),(270,0.334899),(271,0.276105),(272,0.276105),(273,0.276105),(274,0.276105),(275,0.276105\\\\ ),(276,0.276105),(277,0.276105),(278,0.276105),(279,0.276105),(280,0.276105),(281,0.276105\\\\ ),(282,0.276105),(283,0.276105),(284,0.276105),(285,0.276105),(286,0.276105),(287,0.276105\\\\ ),(288,0.276105),(289,0.276105),(290,0.276105),(291,0.276105),(292,0.276105),(293,0.276105\\\\ ),(294,0.276105),(295,0.276105),(296,0.276105),(297,0.276105),(298,0.276105),(299,0.276105\\\\ ),(300,0.276105),(301,0.253477),(302,0.253477),(303,0.253477),(304,0.253477),(305,0.253477\\\\ ),(306,0.253477),(307,0.253477),(308,0.253477),(309,0.253477),(310,0.253477),(311,0.253477\\\\ ),(312,0.253477),(313,0.253477),(314,0.253477),(315,0.253477),(316,0.253477),(317,0.253477\\\\ ),(318,0.253477),(319,0.253477),(320,0.253477),(321,0.253477),(322,0.253477),(323,0.253477\\\\ ),(324,0.253477),(325,0.253477),(326,0.253477),(327,0.253477),(328,0.253477),(329,0.253477\\\\ ),(330,0.253477),(331,0.258668),(332,0.258668),(333,0.258668),(334,0.258668),(335,0.258668\\\\ ),(336,0.258668),(337,0.258668),(338,0.258668),(339,0.258668),(340,0.258668),(341,0.258668\\\\ ),(342,0.258668),(343,0.258668),(344,0.258668),(345,0.258668),(346,0.258668),(347,0.258668\\\\ ),(348,0.258668),(349,0.258668),(350,0.258668),(351,0.258668),(352,0.258668),(353,0.258668\\\\ ),(354,0.258668),(355,0.258668),(356,0.258668),(357,0.258668),(358,0.258668),(359,0.258668\\\\ ),(360,0.258668),(361,0.258668),(362,0.258668),(363,0.258668),(364,0.258668),(365,0.258668\\\\ ))'
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
        0.273879, 0.273879, 0.273879, 0.273879, 0.273879, 0.273879, 0.273879, 0.273879, 0.273879,
        0.273879, 0.273879, 0.273879, 0.273879, 0.273879, 0.273879, 0.273879, 0.273879, 0.273879,
        0.273879, 0.273879, 0.273879, 0.273879, 0.273879, 0.273879, 0.273879, 0.273879, 0.273879,
        0.273879, 0.273879, 0.273879, 0.302397, 0.302397, 0.302397, 0.302397, 0.302397, 0.302397,
        0.302397, 0.302397, 0.302397, 0.302397, 0.302397, 0.302397, 0.302397, 0.302397, 0.302397,
        0.302397, 0.302397, 0.302397, 0.302397, 0.302397, 0.302397, 0.302397, 0.302397, 0.302397,
        0.302397, 0.302397, 0.302397, 0.302397, 0.302397, 0.302397, 0.342583, 0.342583, 0.342583,
        0.342583, 0.342583, 0.342583, 0.342583, 0.342583, 0.342583, 0.342583, 0.342583, 0.342583,
        0.342583, 0.342583, 0.342583, 0.342583, 0.342583, 0.342583, 0.342583, 0.342583, 0.342583,
        0.342583, 0.342583, 0.342583, 0.342583, 0.342583, 0.342583, 0.342583, 0.342583, 0.342583,
        0.342437, 0.342437, 0.342437, 0.342437, 0.342437, 0.342437, 0.342437, 0.342437, 0.342437,
        0.342437, 0.342437, 0.342437, 0.342437, 0.342437, 0.342437, 0.342437, 0.342437, 0.342437,
        0.342437, 0.342437, 0.342437, 0.342437, 0.342437, 0.342437, 0.342437, 0.342437, 0.342437,
        0.342437, 0.342437, 0.342437, 0.421888, 0.421888, 0.421888, 0.421888, 0.421888, 0.421888,
        0.421888, 0.421888, 0.421888, 0.421888, 0.421888, 0.421888, 0.421888, 0.421888, 0.421888,
        0.421888, 0.421888, 0.421888, 0.421888, 0.421888, 0.421888, 0.421888, 0.421888, 0.421888,
        0.421888, 0.421888, 0.421888, 0.421888, 0.421888, 0.421888, 0.579503, 0.579503, 0.579503,
        0.579503, 0.579503, 0.579503, 0.579503, 0.579503, 0.579503, 0.579503, 0.579503, 0.579503,
        0.579503, 0.579503, 0.579503, 0.579503, 0.579503, 0.579503, 0.579503, 0.579503, 0.579503,
        0.579503, 0.579503, 0.579503, 0.579503, 0.579503, 0.579503, 0.579503, 0.579503, 0.579503,
        0.722223, 0.722223, 0.722223, 0.722223, 0.722223, 0.722223, 0.722223, 0.722223, 0.722223,
        0.722223, 0.722223, 0.722223, 0.722223, 0.722223, 0.722223, 0.722223, 0.722223, 0.722223,
        0.722223, 0.722223, 0.722223, 0.722223, 0.722223, 0.722223, 0.722223, 0.722223, 0.722223,
        0.722223, 0.722223, 0.722223, 0.494075, 0.494075, 0.494075, 0.494075, 0.494075, 0.494075,
        0.494075, 0.494075, 0.494075, 0.494075, 0.494075, 0.494075, 0.494075, 0.494075, 0.494075,
        0.494075, 0.494075, 0.494075, 0.494075, 0.494075, 0.494075, 0.494075, 0.494075, 0.494075,
        0.494075, 0.494075, 0.494075, 0.494075, 0.494075, 0.494075, 0.334899, 0.334899, 0.334899,
        0.334899, 0.334899, 0.334899, 0.334899, 0.334899, 0.334899, 0.334899, 0.334899, 0.334899,
        0.334899, 0.334899, 0.334899, 0.334899, 0.334899, 0.334899, 0.334899, 0.334899, 0.334899,
        0.334899, 0.334899, 0.334899, 0.334899, 0.334899, 0.334899, 0.334899, 0.334899, 0.334899,
        0.276105, 0.276105, 0.276105, 0.276105, 0.276105, 0.276105, 0.276105, 0.276105, 0.276105,
        0.276105, 0.276105, 0.276105, 0.276105, 0.276105, 0.276105, 0.276105, 0.276105, 0.276105,
        0.276105, 0.276105, 0.276105, 0.276105, 0.276105, 0.276105, 0.276105, 0.276105, 0.276105,
        0.276105, 0.276105, 0.276105, 0.253477, 0.253477, 0.253477, 0.253477, 0.253477, 0.253477,
        0.253477, 0.253477, 0.253477, 0.253477, 0.253477, 0.253477, 0.253477, 0.253477, 0.253477,
        0.253477, 0.253477, 0.253477, 0.253477, 0.253477, 0.253477, 0.253477, 0.253477, 0.253477,
        0.253477, 0.253477, 0.253477, 0.253477, 0.253477, 0.253477, 0.258668, 0.258668, 0.258668,
        0.258668, 0.258668, 0.258668, 0.258668, 0.258668, 0.258668, 0.258668, 0.258668, 0.258668,
        0.258668, 0.258668, 0.258668, 0.258668, 0.258668, 0.258668, 0.258668, 0.258668, 0.258668,
        0.258668, 0.258668, 0.258668, 0.258668, 0.258668, 0.258668, 0.258668, 0.258668, 0.258668,
        0.258668, 0.258668, 0.258668, 0.258668, 0.258668
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
        1.87, 1.87, 1.87, 1.87, 1.87, 1.87, 1.87, 1.87, 1.87, 1.87, 1.87, 1.87, 1.87, 1.87, 1.87,
        1.87, 1.87, 1.87, 1.87, 1.87, 1.87, 1.87, 1.87, 1.87, 1.87, 1.87, 1.87, 1.87, 1.87, 1.87,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        0.47, 0.47, 0.47, 0.47, 0.47, 0.47, 0.47, 0.47, 0.47, 0.47, 0.47, 0.47, 0.47, 0.47, 0.47,
        0.47, 0.47, 0.47, 0.47, 0.47, 0.47, 0.47, 0.47, 0.47, 0.47, 0.47, 0.47, 0.47, 0.47, 0.47,
        0.27, 0.27, 0.27, 0.27, 0.27, 0.27, 0.27, 0.27, 0.27, 0.27, 0.27, 0.27, 0.27, 0.27, 0.27,
        0.27, 0.27, 0.27, 0.27, 0.27, 0.27, 0.27, 0.27, 0.27, 0.27, 0.27, 0.27, 0.27, 0.27, 0.27,
        0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
        0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.53, 0.53, 0.53, 0.53, 0.53,
        0.53, 0.53, 0.53, 0.53, 0.53, 0.53, 0.53, 0.53, 0.53, 0.53, 0.53, 0.53, 0.53, 0.53, 0.53,
        0.53, 0.53, 0.53, 0.53, 0.53, 0.53, 0.53, 0.53, 0.53, 0.53, 1.97, 1.97, 1.97, 1.97, 1.97,
        1.97, 1.97, 1.97, 1.97, 1.97, 1.97, 1.97, 1.97, 1.97, 1.97, 1.97, 1.97, 1.97, 1.97, 1.97,
        1.97, 1.97, 1.97, 1.97, 1.97, 1.97, 1.97, 1.97, 1.97, 1.97, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5,
        3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5,
        3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 5.13, 5.13, 5.13, 5.13, 5.13, 5.13, 5.13, 5.13, 5.13, 5.13,
        5.13, 5.13, 5.13, 5.13, 5.13, 5.13, 5.13, 5.13, 5.13, 5.13, 5.13, 5.13, 5.13, 5.13, 5.13,
        5.13, 5.13, 5.13, 5.13, 5.13, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37,
        6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37,
        6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37,
        6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37, 6.37,
        6.37, 6.37, 6.37, 6.37, 6.37, 4.83, 4.83, 4.83, 4.83, 4.83, 4.83, 4.83, 4.83, 4.83, 4.83,
        4.83, 4.83, 4.83, 4.83, 4.83, 4.83, 4.83, 4.83, 4.83, 4.83, 4.83, 4.83, 4.83, 4.83, 4.83,
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
        307.3, 310, 315, 320, 325, 330, 335, 340, 345, 350, 355, 360, 365, 370, 375, 380, 385, 390,
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
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02,
        0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02,
        0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04,
        0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04,
        0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
        0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
        0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04,
        0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04,
        0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
        0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
        0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,
        0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,
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
    Original Eqn: b'( [(1,0)-(365,0.9)],(1,0.332774),(2,0.332774),(3,0.332774),(4,0.332774),(5,0.332774),(\\\\ 6,0.332774),(7,0.332774),(8,0.332774),(9,0.332774),(10,0.332774),(11,0.332774),(12,\\\\ 0.332774),(13,0.332774),(14,0.332774),(15,0.332774),(16,0.332774),(17,0.332774),(18\\\\ ,0.332774),(19,0.332774),(20,0.332774),(21,0.332774),(22,0.332774),(23,0.332774),(24\\\\ ,0.332774),(25,0.332774),(26,0.332774),(27,0.332774),(28,0.332774),(29,0.332774),(30\\\\ ,0.332774),(31,0.368075),(32,0.368075),(33,0.368075),(34,0.368075),(35,0.368075),(36\\\\ ,0.368075),(37,0.368075),(38,0.368075),(39,0.368075),(40,0.368075),(41,0.368075),(42\\\\ ,0.368075),(43,0.368075),(44,0.368075),(45,0.368075),(46,0.368075),(47,0.368075),(48\\\\ ,0.368075),(49,0.368075),(50,0.368075),(51,0.368075),(52,0.368075),(53,0.368075),(54\\\\ ,0.368075),(55,0.368075),(56,0.368075),(57,0.368075),(58,0.368075),(59,0.368075),(60\\\\ ,0.368075),(61,0.403649),(62,0.403649),(63,0.403649),(64,0.403649),(65,0.403649),(66\\\\ ,0.403649),(67,0.403649),(68,0.403649),(69,0.403649),(70,0.403649),(71,0.403649),(72\\\\ ,0.403649),(73,0.403649),(74,0.403649),(75,0.403649),(76,0.403649),(77,0.403649),(78\\\\ ,0.403649),(79,0.403649),(80,0.403649),(81,0.403649),(82,0.403649),(83,0.403649),(84\\\\ ,0.403649),(85,0.403649),(86,0.403649),(87,0.403649),(88,0.403649),(89,0.403649),(90\\\\ ,0.403649),(91,0.400335),(92,0.400335),(93,0.400335),(94,0.400335),(95,0.400335),(96\\\\ ,0.400335),(97,0.400335),(98,0.400335),(99,0.400335),(100,0.400335),(101,0.400335),\\\\ (102,0.400335),(103,0.400335),(104,0.400335),(105,0.400335),(106,0.400335),(107,0.400335\\\\ ),(108,0.400335),(109,0.400335),(110,0.400335),(111,0.400335),(112,0.400335),(113,0.400335\\\\ ),(114,0.400335),(115,0.400335),(116,0.400335),(117,0.400335),(118,0.400335),(119,0.400335\\\\ ),(120,0.400335),(121,0.484778),(122,0.484778),(123,0.484778),(124,0.484778),(125,0.484778\\\\ ),(126,0.484778),(127,0.484778),(128,0.484778),(129,0.484778),(130,0.484778),(131,0.484778\\\\ ),(132,0.484778),(133,0.484778),(134,0.484778),(135,0.484778),(136,0.484778),(137,0.484778\\\\ ),(138,0.484778),(139,0.484778),(140,0.484778),(141,0.484778),(142,0.484778),(143,0.484778\\\\ ),(144,0.484778),(145,0.484778),(146,0.484778),(147,0.484778),(148,0.484778),(149,0.484778\\\\ ),(150,0.484778),(151,0.630134),(152,0.630134),(153,0.630134),(154,0.630134),(155,0.630134\\\\ ),(156,0.630134),(157,0.630134),(158,0.630134),(159,0.630134),(160,0.630134),(161,0.630134\\\\ ),(162,0.630134),(163,0.630134),(164,0.630134),(165,0.630134),(166,0.630134),(167,0.630134\\\\ ),(168,0.630134),(169,0.630134),(170,0.630134),(171,0.630134),(172,0.630134),(173,0.630134\\\\ ),(174,0.630134),(175,0.630134),(176,0.630134),(177,0.630134),(178,0.630134),(179,0.630134\\\\ ),(180,0.630134),(181,0.850056),(182,0.850056),(183,0.850056),(184,0.850056),(185,0.850056\\\\ ),(186,0.850056),(187,0.850056),(188,0.850056),(189,0.850056),(190,0.850056),(191,0.850056\\\\ ),(192,0.850056),(193,0.850056),(194,0.850056),(195,0.850056),(196,0.850056),(197,0.850056\\\\ ),(198,0.850056),(199,0.850056),(200,0.850056),(201,0.850056),(202,0.850056),(203,0.850056\\\\ ),(204,0.850056),(205,0.850056),(206,0.850056),(207,0.850056),(208,0.850056),(209,0.850056\\\\ ),(210,0.850056),(211,0.655255),(212,0.655255),(213,0.655255),(214,0.655255),(215,0.655255\\\\ ),(216,0.655255),(217,0.655255),(218,0.655255),(219,0.655255),(220,0.655255),(221,0.655255\\\\ ),(222,0.655255),(223,0.655255),(224,0.655255),(225,0.655255),(226,0.655255),(227,0.655255\\\\ ),(228,0.655255),(229,0.655255),(230,0.655255),(231,0.655255),(232,0.655255),(233,0.655255\\\\ ),(234,0.655255),(235,0.655255),(236,0.655255),(237,0.655255),(238,0.655255),(239,0.655255\\\\ ),(240,0.655255),(241,0.530371),(242,0.530371),(243,0.530371),(244,0.530371),(245,0.530371\\\\ ),(246,0.530371),(247,0.530371),(248,0.530371),(249,0.530371),(250,0.530371),(251,0.530371\\\\ ),(252,0.530371),(253,0.530371),(254,0.530371),(255,0.530371),(256,0.530371),(257,0.530371\\\\ ),(258,0.530371),(259,0.530371),(260,0.530371),(261,0.530371),(262,0.530371),(263,0.530371\\\\ ),(264,0.530371),(265,0.530371),(266,0.530371),(267,0.530371),(268,0.530371),(269,0.530371\\\\ ),(270,0.530371),(271,0.470681),(272,0.470681),(273,0.470681),(274,0.470681),(275,0.470681\\\\ ),(276,0.470681),(277,0.470681),(278,0.470681),(279,0.470681),(280,0.470681),(281,0.470681\\\\ ),(282,0.470681),(283,0.470681),(284,0.470681),(285,0.470681),(286,0.470681),(287,0.470681\\\\ ),(288,0.470681),(289,0.470681),(290,0.470681),(291,0.470681),(292,0.470681),(293,0.470681\\\\ ),(294,0.470681),(295,0.470681),(296,0.470681),(297,0.470681),(298,0.470681),(299,0.470681\\\\ ),(300,0.470681),(301,0.417966),(302,0.417966),(303,0.417966),(304,0.417966),(305,0.417966\\\\ ),(306,0.417966),(307,0.417966),(308,0.417966),(309,0.417966),(310,0.417966),(311,0.417966\\\\ ),(312,0.417966),(313,0.417966),(314,0.417966),(315,0.417966),(316,0.417966),(317,0.417966\\\\ ),(318,0.417966),(319,0.417966),(320,0.417966),(321,0.417966),(322,0.417966),(323,0.417966\\\\ ),(324,0.417966),(325,0.417966),(326,0.417966),(327,0.417966),(328,0.417966),(329,0.417966\\\\ ),(330,0.417966),(331,0.0133445),(332,0.0133445),(333,0.0133445),(334,0.0133445),(335\\\\ ,0.0133445),(336,0.0133445),(337,0.0133445),(338,0.0133445),(339,0.0133445),(340,0.0133445\\\\ ),(341,0.0133445),(342,0.0133445),(343,0.0133445),(344,0.0133445),(345,0.0133445),(\\\\ 346,0.0133445),(347,0.0133445),(348,0.0133445),(349,0.0133445),(350,0.0133445),(351\\\\ ,0.0133445),(352,0.0133445),(353,0.0133445),(354,0.0133445),(355,0.0133445),(356,0.0133445\\\\ ),(357,0.0133445),(358,0.0133445),(359,0.0133445),(360,0.0133445),(361,0.0133445),(\\\\ 362,0.0133445),(363,0.0133445),(364,0.0133445),(365,0.0133445))'
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
        0.332774, 0.332774, 0.332774, 0.332774, 0.332774, 0.332774, 0.332774, 0.332774, 0.332774,
        0.332774, 0.332774, 0.332774, 0.332774, 0.332774, 0.332774, 0.332774, 0.332774, 0.332774,
        0.332774, 0.332774, 0.332774, 0.332774, 0.332774, 0.332774, 0.332774, 0.332774, 0.332774,
        0.332774, 0.332774, 0.332774, 0.368075, 0.368075, 0.368075, 0.368075, 0.368075, 0.368075,
        0.368075, 0.368075, 0.368075, 0.368075, 0.368075, 0.368075, 0.368075, 0.368075, 0.368075,
        0.368075, 0.368075, 0.368075, 0.368075, 0.368075, 0.368075, 0.368075, 0.368075, 0.368075,
        0.368075, 0.368075, 0.368075, 0.368075, 0.368075, 0.368075, 0.403649, 0.403649, 0.403649,
        0.403649, 0.403649, 0.403649, 0.403649, 0.403649, 0.403649, 0.403649, 0.403649, 0.403649,
        0.403649, 0.403649, 0.403649, 0.403649, 0.403649, 0.403649, 0.403649, 0.403649, 0.403649,
        0.403649, 0.403649, 0.403649, 0.403649, 0.403649, 0.403649, 0.403649, 0.403649, 0.403649,
        0.400335, 0.400335, 0.400335, 0.400335, 0.400335, 0.400335, 0.400335, 0.400335, 0.400335,
        0.400335, 0.400335, 0.400335, 0.400335, 0.400335, 0.400335, 0.400335, 0.400335, 0.400335,
        0.400335, 0.400335, 0.400335, 0.400335, 0.400335, 0.400335, 0.400335, 0.400335, 0.400335,
        0.400335, 0.400335, 0.400335, 0.484778, 0.484778, 0.484778, 0.484778, 0.484778, 0.484778,
        0.484778, 0.484778, 0.484778, 0.484778, 0.484778, 0.484778, 0.484778, 0.484778, 0.484778,
        0.484778, 0.484778, 0.484778, 0.484778, 0.484778, 0.484778, 0.484778, 0.484778, 0.484778,
        0.484778, 0.484778, 0.484778, 0.484778, 0.484778, 0.484778, 0.630134, 0.630134, 0.630134,
        0.630134, 0.630134, 0.630134, 0.630134, 0.630134, 0.630134, 0.630134, 0.630134, 0.630134,
        0.630134, 0.630134, 0.630134, 0.630134, 0.630134, 0.630134, 0.630134, 0.630134, 0.630134,
        0.630134, 0.630134, 0.630134, 0.630134, 0.630134, 0.630134, 0.630134, 0.630134, 0.630134,
        0.850056, 0.850056, 0.850056, 0.850056, 0.850056, 0.850056, 0.850056, 0.850056, 0.850056,
        0.850056, 0.850056, 0.850056, 0.850056, 0.850056, 0.850056, 0.850056, 0.850056, 0.850056,
        0.850056, 0.850056, 0.850056, 0.850056, 0.850056, 0.850056, 0.850056, 0.850056, 0.850056,
        0.850056, 0.850056, 0.850056, 0.655255, 0.655255, 0.655255, 0.655255, 0.655255, 0.655255,
        0.655255, 0.655255, 0.655255, 0.655255, 0.655255, 0.655255, 0.655255, 0.655255, 0.655255,
        0.655255, 0.655255, 0.655255, 0.655255, 0.655255, 0.655255, 0.655255, 0.655255, 0.655255,
        0.655255, 0.655255, 0.655255, 0.655255, 0.655255, 0.655255, 0.530371, 0.530371, 0.530371,
        0.530371, 0.530371, 0.530371, 0.530371, 0.530371, 0.530371, 0.530371, 0.530371, 0.530371,
        0.530371, 0.530371, 0.530371, 0.530371, 0.530371, 0.530371, 0.530371, 0.530371, 0.530371,
        0.530371, 0.530371, 0.530371, 0.530371, 0.530371, 0.530371, 0.530371, 0.530371, 0.530371,
        0.470681, 0.470681, 0.470681, 0.470681, 0.470681, 0.470681, 0.470681, 0.470681, 0.470681,
        0.470681, 0.470681, 0.470681, 0.470681, 0.470681, 0.470681, 0.470681, 0.470681, 0.470681,
        0.470681, 0.470681, 0.470681, 0.470681, 0.470681, 0.470681, 0.470681, 0.470681, 0.470681,
        0.470681, 0.470681, 0.470681, 0.417966, 0.417966, 0.417966, 0.417966, 0.417966, 0.417966,
        0.417966, 0.417966, 0.417966, 0.417966, 0.417966, 0.417966, 0.417966, 0.417966, 0.417966,
        0.417966, 0.417966, 0.417966, 0.417966, 0.417966, 0.417966, 0.417966, 0.417966, 0.417966,
        0.417966, 0.417966, 0.417966, 0.417966, 0.417966, 0.417966, 0.0133445, 0.0133445,
        0.0133445, 0.0133445, 0.0133445, 0.0133445, 0.0133445, 0.0133445, 0.0133445, 0.0133445,
        0.0133445, 0.0133445, 0.0133445, 0.0133445, 0.0133445, 0.0133445, 0.0133445, 0.0133445,
        0.0133445, 0.0133445, 0.0133445, 0.0133445, 0.0133445, 0.0133445, 0.0133445, 0.0133445,
        0.0133445, 0.0133445, 0.0133445, 0.0133445, 0.0133445, 0.0133445, 0.0133445, 0.0133445,
        0.0133445
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
        0.4, 0.419531, 0.497656, 0.55, 0.576674, 0.657506, 0.738337, 0.819169, 0.9, 0.964, 1.028,
        1.092, 1.156, 1.22, 1.284, 1.3, 1.372, 1.468, 1.564, 1.66649, 1.756, 1.852, 1.948, 2.044,
        2.14, 2.236, 2.332, 2.428, 2.5, 2.528, 2.64, 2.752, 2.864, 2.976, 3.088, 3.2, 3.344, 3.488,
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
        0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
        0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
        0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
        0.04352, 0.04352, 0.04352, 0.04352, 0.04352, 0.04352, 0.04352, 0.04352, 0.04352, 0.04352,
        0.04352, 0.04352, 0.04352, 0.04352, 0.04352, 0.04352, 0.04352, 0.04352, 0.04352, 0.04352,
        0.04352, 0.04352, 0.04352, 0.04352, 0.04352, 0.04352, 0.04352, 0.04352, 0.04352, 0.04352,
        0.04487, 0.04487, 0.04487, 0.04487, 0.04487, 0.04487, 0.04487, 0.04487, 0.04487, 0.04487,
        0.04487, 0.04487, 0.04487, 0.04487, 0.04487, 0.04487, 0.04487, 0.04487, 0.04487, 0.04487,
        0.04487, 0.04487, 0.04487, 0.04487, 0.04487, 0.04487, 0.04487, 0.04487, 0.04487, 0.04487,
        0.0458, 0.0458, 0.0458, 0.0458, 0.0458, 0.0458, 0.0458, 0.0458, 0.0458, 0.0458, 0.0458,
        0.0458, 0.0458, 0.0458, 0.0458, 0.0458, 0.0458, 0.0458, 0.0458, 0.0458, 0.0458, 0.0458,
        0.0458, 0.0458, 0.0458, 0.0458, 0.0458, 0.0458, 0.0458, 0.0458, 0.04956, 0.04956, 0.04956,
        0.04956, 0.04956, 0.04956, 0.04956, 0.04956, 0.04956, 0.04956, 0.04956, 0.04956, 0.04956,
        0.04956, 0.04956, 0.04956, 0.04956, 0.04956, 0.04956, 0.04956, 0.04956, 0.04956, 0.04956,
        0.04956, 0.04956, 0.04956, 0.04956, 0.04956, 0.04956, 0.04956, 0.06719, 0.06719, 0.06719,
        0.06719, 0.06719, 0.06719, 0.06719, 0.06719, 0.06719, 0.06719, 0.06719, 0.06719, 0.06719,
        0.06719, 0.06719, 0.06719, 0.06719, 0.06719, 0.06719, 0.06719, 0.06719, 0.06719, 0.06719,
        0.06719, 0.06719, 0.06719, 0.06719, 0.06719, 0.06719, 0.06719, 0.31762, 0.31762, 0.31762,
        0.31762, 0.31762, 0.31762, 0.31762, 0.31762, 0.31762, 0.31762, 0.31762, 0.31762, 0.31762,
        0.31762, 0.31762, 0.31762, 0.31762, 0.31762, 0.31762, 0.31762, 0.31762, 0.31762, 0.31762,
        0.31762, 0.31762, 0.31762, 0.31762, 0.31762, 0.31762, 0.31762, 0.26985, 0.26985, 0.26985,
        0.26985, 0.26985, 0.26985, 0.26985, 0.26985, 0.26985, 0.26985, 0.26985, 0.26985, 0.26985,
        0.26985, 0.26985, 0.26985, 0.26985, 0.26985, 0.26985, 0.26985, 0.26985, 0.26985, 0.26985,
        0.26985, 0.26985, 0.26985, 0.26985, 0.26985, 0.26985, 0.26985, 0.23489, 0.23489, 0.23489,
        0.23489, 0.23489, 0.23489, 0.23489, 0.23489, 0.23489, 0.23489, 0.23489, 0.23489, 0.23489,
        0.23489, 0.23489, 0.23489, 0.23489, 0.23489, 0.23489, 0.23489, 0.23489, 0.23489, 0.23489,
        0.23489, 0.23489, 0.23489, 0.23489, 0.23489, 0.23489, 0.23489, 0.23456, 0.23456, 0.23456,
        0.23456, 0.23456, 0.23456, 0.23456, 0.23456, 0.23456, 0.23456, 0.23456, 0.23456, 0.23456,
        0.23456, 0.23456, 0.23456, 0.23456, 0.23456, 0.23456, 0.23456, 0.23456, 0.23456, 0.23456,
        0.23456, 0.23456, 0.23456, 0.23456, 0.23456, 0.23456, 0.23456, 0.19464, 0.19464, 0.19464,
        0.19464, 0.19464, 0.19464, 0.19464, 0.19464, 0.19464, 0.19464, 0.19464, 0.19464, 0.19464,
        0.19464, 0.19464, 0.19464, 0.19464, 0.19464, 0.19464, 0.19464, 0.19464, 0.19464, 0.19464,
        0.19464, 0.19464, 0.19464, 0.19464, 0.19464, 0.19464, 0.19464, 0.00153, 0.00153, 0.00153,
        0.00153, 0.00153, 0.00153, 0.00153, 0.00153, 0.00153, 0.00153, 0.00153, 0.00153, 0.00153,
        0.00153, 0.00153, 0.00153, 0.00153, 0.00153, 0.00153, 0.00153, 0.00153, 0.00153, 0.00153,
        0.00153, 0.00153, 0.00153, 0.00153, 0.00153, 0.00153, 0.00153, 0.00153, 0.00153, 0.00153,
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
        0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
        0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
        0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
        0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
        0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
        0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
        0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
        0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
        0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
        0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
        0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
        0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
        0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
        0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
        0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
        0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
        0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
        0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
        0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
        0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
        0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
        0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
        0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
        0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
        0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
        0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
        0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
        0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
        0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
        0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
        0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
        0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
        0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
        0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
        0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
        0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638, 0.04638,
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
        0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667,
        0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667,
        0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667, 0.86667,
        1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5,
        1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 0.96667, 0.96667, 0.96667,
        0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667,
        0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667,
        0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.96667, 0.83333, 0.83333, 0.83333,
        0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333,
        0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333,
        0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 0.83333, 1.03333, 1.03333, 1.03333,
        1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333,
        1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333,
        1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.03333, 1.56667, 1.56667, 1.56667,
        1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667,
        1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667,
        1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 1.56667, 2.5, 2.5, 2.5, 2.5, 2.5,
        2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5,
        2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6,
        3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6,
        3.6, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667,
        4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667,
        4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667, 4.46667,
        4.46667, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333,
        4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333,
        4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333, 4.93333,
        4.93333, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8,
        4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 3.7, 3.7, 3.7, 3.7,
        3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7,
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
        0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
        0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
        0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
        0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
        0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
        0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
        0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
        0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
        0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
        0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
        0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
        0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
        0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
        0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
        0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
        0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
        0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
        0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
        0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
        0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
        0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
        0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
        0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
        0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
        0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
        0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
        0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
        0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
        0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
        0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
        0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
        0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
        0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
        0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
        0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
        0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333,
        0.08333, 0.08333, 0.08333, 0.08333, 0.08333
    ])


def after_finesk_interflow(x):
    """
    Real Name: b'After Finesk Interflow'
    Original Eqn: b'( [(1,0)-(365,1)],(1,0.198805),(2,0.198805),(3,0.198805),(4,0.198805),(5,0.198805),(6,\\\\ 0.198805),(7,0.198805),(8,0.198805),(9,0.198805),(10,0.198805),(11,0.198805),(12,0.198805\\\\ ),(13,0.198805),(14,0.198805),(15,0.198805),(16,0.198805),(17,0.198805),(18,0.198805\\\\ ),(19,0.198805),(20,0.198805),(21,0.198805),(22,0.198805),(23,0.198805),(24,0.198805\\\\ ),(25,0.198805),(26,0.198805),(27,0.198805),(28,0.198805),(29,0.198805),(30,0.198805\\\\ ),(31,0.183866),(32,0.183866),(33,0.183866),(34,0.183866),(35,0.183866),(36,0.183866\\\\ ),(37,0.183866),(38,0.183866),(39,0.183866),(40,0.183866),(41,0.183866),(42,0.183866\\\\ ),(43,0.183866),(44,0.183866),(45,0.183866),(46,0.183866),(47,0.183866),(48,0.183866\\\\ ),(49,0.183866),(50,0.183866),(51,0.183866),(52,0.183866),(53,0.183866),(54,0.183866\\\\ ),(55,0.183866),(56,0.183866),(57,0.183866),(58,0.183866),(59,0.183866),(60,0.183866\\\\ ),(61,0.183866),(62,0.183866),(63,0.183866),(64,0.183866),(65,0.183866),(66,0.183866\\\\ ),(67,0.183866),(68,0.183866),(69,0.183866),(70,0.183866),(71,0.183866),(72,0.183866\\\\ ),(73,0.183866),(74,0.183866),(75,0.183866),(76,0.183866),(77,0.183866),(78,0.183866\\\\ ),(79,0.183866),(80,0.183866),(81,0.183866),(82,0.183866),(83,0.183866),(84,0.183866\\\\ ),(85,0.183866),(86,0.183866),(87,0.183866),(88,0.183866),(89,0.183866),(90,0.183866\\\\ ),(91,0.183866),(92,0.183866),(93,0.183866),(94,0.183866),(95,0.183866),(96,0.183866\\\\ ),(97,0.183866),(98,0.183866),(99,0.183866),(100,0.183866),(101,0.183866),(102,0.183866\\\\ ),(103,0.183866),(104,0.183866),(105,0.183866),(106,0.183866),(107,0.183866),(108,0.183866\\\\ ),(109,0.183866),(110,0.183866),(111,0.183866),(112,0.183866),(113,0.183866),(114,0.183866\\\\ ),(115,0.183866),(116,0.183866),(117,0.183866),(118,0.183866),(119,0.183866),(120,0.183866\\\\ ),(121,0.183866),(122,0.183866),(123,0.183866),(124,0.183866),(125,0.183866),(126,0.183866\\\\ ),(127,0.183866),(128,0.183866),(129,0.183866),(130,0.183866),(131,0.183866),(132,0.183866\\\\ ),(133,0.183866),(134,0.183866),(135,0.183866),(136,0.183866),(137,0.183866),(138,0.183866\\\\ ),(139,0.183866),(140,0.183866),(141,0.183866),(142,0.183866),(143,0.183866),(144,0.183866\\\\ ),(145,0.183866),(146,0.183866),(147,0.183866),(148,0.183866),(149,0.183866),(150,0.183866\\\\ ),(151,0.183866),(152,0.183866),(153,0.183866),(154,0.183866),(155,0.183866),(156,0.183866\\\\ ),(157,0.183866),(158,0.183866),(159,0.183866),(160,0.183866),(161,0.183866),(162,0.183866\\\\ ),(163,0.183866),(164,0.183866),(165,0.183866),(166,0.183866),(167,0.183866),(168,0.183866\\\\ ),(169,0.183866),(170,0.183866),(171,0.183866),(172,0.183866),(173,0.183866),(174,0.183866\\\\ ),(175,0.183866),(176,0.183866),(177,0.183866),(178,0.183866),(179,0.183866),(180,0.183866\\\\ ),(181,0.183866),(182,0.183866),(183,0.183866),(184,0.183866),(185,0.183866),(186,0.183866\\\\ ),(187,0.183866),(188,0.183866),(189,0.183866),(190,0.183866),(191,0.183866),(192,0.183866\\\\ ),(193,0.183866),(194,0.183866),(195,0.183866),(196,0.183866),(197,0.183866),(198,0.183866\\\\ ),(199,0.183866),(200,0.183866),(201,0.183866),(202,0.183866),(203,0.183866),(204,0.183866\\\\ ),(205,0.183866),(206,0.183866),(207,0.183866),(208,0.183866),(209,0.183866),(210,0.183866\\\\ ),(211,0.183866),(212,0.183866),(213,0.183866),(214,0.183866),(215,0.183866),(216,0.183866\\\\ ),(217,0.183866),(218,0.183866),(219,0.183866),(220,0.183866),(221,0.183866),(222,0.183866\\\\ ),(223,0.183866),(224,0.183866),(225,0.183866),(226,0.183866),(227,0.183866),(228,0.183866\\\\ ),(229,0.183866),(230,0.183866),(231,0.183866),(232,0.183866),(233,0.183866),(234,0.183866\\\\ ),(235,0.183866),(236,0.183866),(237,0.183866),(238,0.183866),(239,0.183866),(240,0.183866\\\\ ),(241,0.183866),(242,0.183866),(243,0.183866),(244,0.183866),(245,0.183866),(246,0.183866\\\\ ),(247,0.183866),(248,0.183866),(249,0.183866),(250,0.183866),(251,0.183866),(252,0.183866\\\\ ),(253,0.183866),(254,0.183866),(255,0.183866),(256,0.183866),(257,0.183866),(258,0.183866\\\\ ),(259,0.183866),(260,0.183866),(261,0.183866),(262,0.183866),(263,0.183866),(264,0.183866\\\\ ),(265,0.183866),(266,0.183866),(267,0.183866),(268,0.183866),(269,0.183866),(270,0.183866\\\\ ),(271,0.183866),(272,0.183866),(273,0.183866),(274,0.183866),(275,0.183866),(276,0.183866\\\\ ),(277,0.183866),(278,0.183866),(279,0.183866),(280,0.183866),(281,0.183866),(282,0.183866\\\\ ),(283,0.183866),(284,0.183866),(285,0.183866),(286,0.183866),(287,0.183866),(288,0.183866\\\\ ),(289,0.183866),(290,0.183866),(291,0.183866),(292,0.183866),(293,0.183866),(294,0.183866\\\\ ),(295,0.183866),(296,0.183866),(297,0.183866),(298,0.183866),(299,0.183866),(300,0.183866\\\\ ),(301,0.183866),(302,0.183866),(303,0.183866),(304,0.183866),(305,0.183866),(306,0.183866\\\\ ),(307,0.183866),(308,0.183866),(309,0.183866),(310,0.183866),(311,0.183866),(312,0.183866\\\\ ),(313,0.183866),(314,0.183866),(315,0.183866),(316,0.183866),(317,0.183866),(318,0.183866\\\\ ),(319,0.183866),(320,0.183866),(321,0.183866),(322,0.183866),(323,0.183866),(324,0.183866\\\\ ),(325,0.183866),(326,0.183866),(327,0.183866),(328,0.183866),(329,0.183866),(330,0.183866\\\\ ),(331,0.183866),(332,0.183866),(333,0.183866),(334,0.183866),(335,0.183866),(336,0.183866\\\\ ),(337,0.183866),(338,0.183866),(339,0.183866),(340,0.183866),(341,0.183866),(342,0.183866\\\\ ),(343,0.183866),(344,0.183866),(345,0.183866),(346,0.183866),(347,0.183866),(348,0.183866\\\\ ),(349,0.183866),(350,0.183866),(351,0.183866),(352,0.183866),(353,0.183866),(354,0.183866\\\\ ),(355,0.183866),(356,0.183866),(357,0.183866),(358,0.183866),(359,0.183866),(360,0.183866\\\\ ),(361,0.183866),(362,0.183866),(363,0.183866),(364,0.183866),(365,0.183866))'
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
        0.198805, 0.198805, 0.198805, 0.198805, 0.198805, 0.198805, 0.198805, 0.198805, 0.198805,
        0.198805, 0.198805, 0.198805, 0.198805, 0.198805, 0.198805, 0.198805, 0.198805, 0.198805,
        0.198805, 0.198805, 0.198805, 0.198805, 0.198805, 0.198805, 0.198805, 0.198805, 0.198805,
        0.198805, 0.198805, 0.198805, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866,
        0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866,
        0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866,
        0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866,
        0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866,
        0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866,
        0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866,
        0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866,
        0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866,
        0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866,
        0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866,
        0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866,
        0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866,
        0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866,
        0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866,
        0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866,
        0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866,
        0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866,
        0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866,
        0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866,
        0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866,
        0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866,
        0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866,
        0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866,
        0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866,
        0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866,
        0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866,
        0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866,
        0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866,
        0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866,
        0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866,
        0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866,
        0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866,
        0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866,
        0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866,
        0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866,
        0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866, 0.183866,
        0.183866, 0.183866, 0.183866, 0.183866, 0.183866
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
        3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25,
        3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25,
        1.25667, 1.25667, 1.25667, 1.25667, 1.25667, 1.25667, 1.25667, 1.25667, 1.25667, 1.25667,
        1.25667, 1.25667, 1.25667, 1.25667, 1.25667, 1.25667, 1.25667, 1.25667, 1.25667, 1.25667,
        1.25667, 1.25667, 1.25667, 1.25667, 1.25667, 1.25667, 1.25667, 1.25667, 1.25667, 1.25667,
        0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12,
        0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12,
        0.05333, 0.05333, 0.05333, 0.05333, 0.05333, 0.05333, 0.05333, 0.05333, 0.05333, 0.05333,
        0.05333, 0.05333, 0.05333, 0.05333, 0.05333, 0.05333, 0.05333, 0.05333, 0.05333, 0.05333,
        0.05333, 0.05333, 0.05333, 0.05333, 0.05333, 0.05333, 0.05333, 0.05333, 0.05333, 0.05333,
        0.04333, 0.04333, 0.04333, 0.04333, 0.04333, 0.04333, 0.04333, 0.04333, 0.04333, 0.04333,
        0.04333, 0.04333, 0.04333, 0.04333, 0.04333, 0.04333, 0.04333, 0.04333, 0.04333, 0.04333,
        0.04333, 0.04333, 0.04333, 0.04333, 0.04333, 0.04333, 0.04333, 0.04333, 0.04333, 0.04333,
        0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04,
        0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04,
        0.92667, 0.92667, 0.92667, 0.92667, 0.92667, 0.92667, 0.92667, 0.92667, 0.92667, 0.92667,
        0.92667, 0.92667, 0.92667, 0.92667, 0.92667, 0.92667, 0.92667, 0.92667, 0.92667, 0.92667,
        0.92667, 0.92667, 0.92667, 0.92667, 0.92667, 0.92667, 0.92667, 0.92667, 0.92667, 0.92667,
        4.12, 4.12, 4.12, 4.12, 4.12, 4.12, 4.12, 4.12, 4.12, 4.12, 4.12, 4.12, 4.12, 4.12, 4.12,
        4.12, 4.12, 4.12, 4.12, 4.12, 4.12, 4.12, 4.12, 4.12, 4.12, 4.12, 4.12, 4.12, 4.12, 4.12,
        4.68667, 4.68667, 4.68667, 4.68667, 4.68667, 4.68667, 4.68667, 4.68667, 4.68667, 4.68667,
        4.68667, 4.68667, 4.68667, 4.68667, 4.68667, 4.68667, 4.68667, 4.68667, 4.68667, 4.68667,
        4.68667, 4.68667, 4.68667, 4.68667, 4.68667, 4.68667, 4.68667, 4.68667, 4.68667, 4.68667,
        5.71, 5.71, 5.71, 5.71, 5.71, 5.71, 5.71, 5.71, 5.71, 5.71, 5.71, 5.71, 5.71, 5.71, 5.71,
        5.71, 5.71, 5.71, 5.71, 5.71, 5.71, 5.71, 5.71, 5.71, 5.71, 5.71, 5.71, 5.71, 5.71, 5.71,
        6.48667, 6.48667, 6.48667, 6.48667, 6.48667, 6.48667, 6.48667, 6.48667, 6.48667, 6.48667,
        6.48667, 6.48667, 6.48667, 6.48667, 6.48667, 6.48667, 6.48667, 6.48667, 6.48667, 6.48667,
        6.48667, 6.48667, 6.48667, 6.48667, 6.48667, 6.48667, 6.48667, 6.48667, 6.48667, 6.48667,
        5.38667, 5.38667, 5.38667, 5.38667, 5.38667, 5.38667, 5.38667, 5.38667, 5.38667, 5.38667,
        5.38667, 5.38667, 5.38667, 5.38667, 5.38667, 5.38667, 5.38667, 5.38667, 5.38667, 5.38667,
        5.38667, 5.38667, 5.38667, 5.38667, 5.38667, 5.38667, 5.38667, 5.38667, 5.38667, 5.38667,
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
        0.2, 0.23, 0.26, 0.3, 0.32, 0.36, 0.4, 0.44, 0.48, 0.52, 0.57, 0.61, 0.65, 0.7, 0.75, 0.8,
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
        0.01115, 0.01115, 0.01115, 0.01115, 0.01115, 0.01115, 0.01115, 0.01115, 0.01115, 0.01115,
        0.01115, 0.01115, 0.01115, 0.01115, 0.01115, 0.01115, 0.01115, 0.01115, 0.01115, 0.01115,
        0.01115, 0.01115, 0.01115, 0.01115, 0.01115, 0.01115, 0.01115, 0.01115, 0.01115, 0.01115,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0.00084, 0.00084, 0.00084, 0.00084, 0.00084, 0.00084, 0.00084, 0.00084, 0.00084, 0.00084,
        0.00084, 0.00084, 0.00084, 0.00084, 0.00084, 0.00084, 0.00084, 0.00084, 0.00084, 0.00084,
        0.00084, 0.00084, 0.00084, 0.00084, 0.00084, 0.00084, 0.00084, 0.00084, 0.00084, 0.00084,
        0.03114, 0.03114, 0.03114, 0.03114, 0.03114, 0.03114, 0.03114, 0.03114, 0.03114, 0.03114,
        0.03114, 0.03114, 0.03114, 0.03114, 0.03114, 0.03114, 0.03114, 0.03114, 0.03114, 0.03114,
        0.03114, 0.03114, 0.03114, 0.03114, 0.03114, 0.03114, 0.03114, 0.03114, 0.03114, 0.03114,
        0.09685, 0.09685, 0.09685, 0.09685, 0.09685, 0.09685, 0.09685, 0.09685, 0.09685, 0.09685,
        0.09685, 0.09685, 0.09685, 0.09685, 0.09685, 0.09685, 0.09685, 0.09685, 0.09685, 0.09685,
        0.09685, 0.09685, 0.09685, 0.09685, 0.09685, 0.09685, 0.09685, 0.09685, 0.09685, 0.09685,
        0.14005, 0.14005, 0.14005, 0.14005, 0.14005, 0.14005, 0.14005, 0.14005, 0.14005, 0.14005,
        0.14005, 0.14005, 0.14005, 0.14005, 0.14005, 0.14005, 0.14005, 0.14005, 0.14005, 0.14005,
        0.14005, 0.14005, 0.14005, 0.14005, 0.14005, 0.14005, 0.14005, 0.14005, 0.14005, 0.14005,
        0.20065, 0.20065, 0.20065, 0.20065, 0.20065, 0.20065, 0.20065, 0.20065, 0.20065, 0.20065,
        0.20065, 0.20065, 0.20065, 0.20065, 0.20065, 0.20065, 0.20065, 0.20065, 0.20065, 0.20065,
        0.20065, 0.20065, 0.20065, 0.20065, 0.20065, 0.20065, 0.20065, 0.20065, 0.20065, 0.20065,
        0.18101, 0.18101, 0.18101, 0.18101, 0.18101, 0.18101, 0.18101, 0.18101, 0.18101, 0.18101,
        0.18101, 0.18101, 0.18101, 0.18101, 0.18101, 0.18101, 0.18101, 0.18101, 0.18101, 0.18101,
        0.18101, 0.18101, 0.18101, 0.18101, 0.18101, 0.18101, 0.18101, 0.18101, 0.18101, 0.18101,
        0.07406, 0.07406, 0.07406, 0.07406, 0.07406, 0.07406, 0.07406, 0.07406, 0.07406, 0.07406,
        0.07406, 0.07406, 0.07406, 0.07406, 0.07406, 0.07406, 0.07406, 0.07406, 0.07406, 0.07406,
        0.07406, 0.07406, 0.07406, 0.07406, 0.07406, 0.07406, 0.07406, 0.07406, 0.07406, 0.07406,
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
