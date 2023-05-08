import pandas as pd

df = pd.read_csv('dataset.csv')

read_dataRecord = {
    "safety": df['Safety'],
    "lugage": df['Lugage_boot'],
    "evaluation": df['Evaluation']
}

def TotalSafety_MedHigh(attr):
    safety_medHigh = 0

    for i in range(len(attr)):
        if (attr[i] == "med" or attr[i] == "high"):
            safety_medHigh += 1

    return safety_medHigh

def TotalLugage_small(Attribut, attr2, attr3):
    lugage = Attribut['lugage']
    safety = Attribut['safety']
    lugage_small = 0

    Lugage = ('small', 'med', 'big')

    search_lugage = []
    if (attr2=='small'):
        search_lugage.append(attr2)
    elif (attr2 == 'med'):
        search_lugage.append(attr2)
    elif (attr2 == 'big'):
        search_lugage.append(attr2)
    else:
        search_lugage.extend(Lugage)

    search_safety = []
    search_safety.append(attr3)

    for i in range(len(lugage)):
        if (lugage[i] in search_lugage and safety[i] in search_safety):
            lugage_small += 1
    return lugage_small

def TotalLugage_MedBig(Attribut, attr2, attr3, attr4):
    lugage = Attribut['lugage']
    safety = Attribut['safety']

    search_attr = []
    search_attr.append(attr2)
    search_attr.append(attr3)

    search_attr_high = []
    search_attr_high.append(attr4)

    lugage_medBig = 0
    for i in range(len(lugage)):
        if (lugage[i] in search_attr and safety[i] in search_attr_high):
            lugage_medBig += 1
    return lugage_medBig

def TotalPerson(Attribut, attr2):
    lugage = Attribut['lugage']
    safety = Attribut['safety']
    person = Attribut['person']
    total_person = 0
    search = []
    if (attr2 == '2'):
        search.append(attr2)
    else:
        search2 = ('3', '4', 'More')
        search.extend(search2)

    for i in range(len(person)):
        if (person[i] in search and lugage[i] == "small" and safety[i] == "med"):
            total_person += 1

    return total_person

# def TotalLugage_MedBig(Attribut, attr2, attr3):
#     x = Attribut
#     y = attr3
#     z = attr2
#
#     total = x+y+z
#     return total

# print(TotalLugage_MedBig(read_dataRecord, 'med', 'big'))