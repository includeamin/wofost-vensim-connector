RegionsVariablesMap = {
    "Zarem": {
        "Apple": {
            "Wofost": "Supply of apple zr",
            "Vensim": "apple zr",
            "KeyInVensimModel": "apple_zr"
        },
        "Rice": {
            "Wofost": "supply of rice zr",
            "Vensim": "rice zr",
            "KeyInVensimModel": "rice_zr"
        },
        "Citrus": {
            "Wofost": "Supply of citrus zr",
            "Vensim": "citrus zr",
            "KeyInVensimModel": "citrus_zr"
        },
        "Rapeseed": {
            "Wofost": "Supply of rapeseed zr",
            "Vensim": "rapeseed zr",
            "KeyInVensimModel": "rapeseed_zr"
        }
    },
    "Finesk": {
        "Tomato": {
            "Wofost": "supply of tomato",
            "Vensim": "tomato",
            "KeyInVensimModel": "tomato"
        },
        "Rapeseed": {
            "Wofost": "Supply of rapeseed",
            "Vensim": "rapeseed",
            "KeyInVensimModel": "rapeseed"
        },
        "Apple": {
            "Wofost": "Supply of apple",
            "Vensim": "apple",
            "KeyInVensimModel": "apple"
        },
        "Citrus": {
            "Wofost": "Supply of citrus",
            "Vensim": "citrus",
            "KeyInVensimModel": "citrus"
        },
        "Grainmaize": {
            "Wofost": "Supply grainmaize",
            "Vensim": "grainmaize",
            "KeyInVensimModel": "grainmaize"
        },
        "Wheat": {
            "Wofost": "Supply of wheat",
            "Vensim": "wheat",
            "KeyInVensimModel": "wheat"
        },
        "Chickpea": {
            "Wofost": "Supply of chickpea",
            "Vensim": "chickpea",
            "KeyInVensimModel": "chickpea"
        },
        "Rice": {
            "Wofost": "Supply of rice",
            "Vensim": "rice",
            "KeyInVensimModel": "rice"
        }

    },
    "shah R D": {
        "Rice": {
            "Wofost": "Supply of Rice Tj",
            "Vensim": "Rice Tj",
            "KeyInVensimModel": "Rice_Tj"
        },
        "Apple": {
            "Wofost": "Supply of apple Tj",
            "Vensim": "apple Tj",
            "KeyInVensimModel": "apple_Tj"
        },
        "Citrus": {
            "Wofost": "Supply of Citrus Tj",
            "Vensim": "Citrus Tj",
            "KeyInVensimModel": "Citrs_Tj"
        },
        "Tomato": {
            "Wofost": "Supply of tomato tj",
            "Vensim": "tomato tj",
            "KeyInVensimModel": "tomato_Tj"
        },
        "Wheat": {
            "Wofost": "Supply of wheat Tj",
            "Vensim": "wheat Tj",
            "KeyInVensimModel": "wheat_Tj"
        },
        "Rapeseed": {
            "Wofost": "Supply of rapeseed Tj",
            "Vensim": "Rapeseed Tj",
            "KeyInVensimModel": "Rapeseed_Tj"
        }
    },
    "Tj dd":
        {
            "Rice": {
                "Wofost": "Sup- Rice tjj dd",
                "Vensim": "rice tjj dd",
                "KeyInVensimModel": "rice_tjj_dd"
            },
            "Citrus": {
                "Wofost": "sup-Citrus tjj dd",
                "Vensim": "citrud tjj dd",
                "KeyInVensimModel": "citrud_tjj_dd"
            },
            "Apple": {
                "Wofost": "sup-Apple tjj dd",
                "Vensim": "apple tjj dd",
                "KeyInVensimModel": "apple_tjj_dd"
            },
            "Sorgum": {
                "Wofost": "sup-Sorgum tjdd",
                "Vensim": "sorgum tjj dd",
                "KeyInVensimModel": "sorgum_tjj_dd"
            },
            "Wheat": {
                "Wofost": "sup-Wheat tjj dd",
                "Vensim": "wheat tjj dd",
                "KeyInVensimModel": "wheat_tjj_dd"
            },
            "Rapeseed": {
                "Wofost": "sup-Rapeseed tjdd",
                "Vensim": "rapeseed tjj dd",
                "KeyInVensimModel": "rapeseed_tjj_dd"
            },
            "Grainmaize": {
                "Wofost": "Sup-grainmaize Tjdd",
                "Vensim": "grain maiz tjj dd",
                "KeyInVensimModel": "grain_maiz_tjj_dd"
            },
            "Tomato": {
                "Wofost": "Sup-tomato tjdd",
                "Vensim": "tomato tjj dd",
                "KeyInVensimModel": "tomato_tjj_dd"
            }
        }

}

CropNameMaps = {
    "Apple": "APP301 - TJ.CAB",
    "Chickpea": "CHICKPEA - TJ.W41",
    "Citrus": "CIT301 - TJ.CAB",
    "Grainmaize": "MAIZ - TJ.W41",
    "Tomato": "POT701-TJ.CAB",
    "Rice": "RIC501 - TJ.CAB",
    "Rapeseed": "SOYBEAN - TJ.W41",
    "Wheat": "WWH101 - TJ.CAB",
    "Sorgum":"MAIZ - TJ.W41"

}

MeteoNameMaps = {
    "Apple": "SAP2",
    "Chickpea": "SCK2",
    "Citrus": "SCT2",
    "Grainmaize": "SMZ2",
    "Tomato": "SPT2",
    "Rice": "SRC2",
    "Rapeseed": "SRP2",
    "Wheat": "SWT2",
    "Sorgum":"SMZ2"
}

Coefficient:dict = {
    "Tomato": {
        "Finesk": 0.02782949291,
        "Zarem": 0,
        "Tj dd": 0,
        "shah R D": 0.0000351
    },
    "Chickpea": {
        "Finesk": 0.000061,
        "Zarem": 0,
        "Tj dd": 0,
        "shah R D": 0
    },
    "Rapeseed": {
        "Finesk": 0.00013,
        "Zarem": 0.000017,
        "Tj dd": 0.004354075,
        "shah R D": 0
    },
    "Grainmaize": {
        "Finesk": 0.00001,
        "Zarem": 0,
        "Tj dd": 0.003685,
        "shah R D": 0
    },
    "Apple": {
        "Finesk": 0.02752754991,
        "Zarem": 0.041570141,
        "Tj dd": 0.03405931491,
        "shah R D": 0.005011631
    },
    "Rice": {
        "Finesk": 0.019067016,
        "Zarem": 0.0097329009,
        "Tj dd": 0.2196073774,
        "shah R D": 0.0105982088
    },
    "Wheat": {
        "Finesk": 0.009012,
        "Zarem": 0,
        "Tj dd": 0.017090164,
        "shah R D": 0.000008
    },
    "Citrus": {
        "Finesk": 0.0009526,
        "Zarem": 0.001605887,
        "Tj dd": 0.1293910401,
        "shah R D": 0.00038915
    },
    "Sorgum": {
        "Finesk": 0,
        "Zarem": 0,
        "Tj dd": 0.01708,
        "shah R D": 0
    }

}

Regions = {
    "Finesk",
    "Zarem",
    "Tj dd",
    "shah R D"

}
