def detect(name: str):
    name = name.lower()
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


region, crop = detect('supply of rice zr')
print(region, crop)
