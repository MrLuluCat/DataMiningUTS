import pandas as pd
df = pd.read_csv('dataset.csv')

read_dataset = {
    'safety'      : df['Safety'],
    'evaluation'  : df['Evaluation'],
    'lugage'      : df['Lugage_boot'],
    'person'      : df['Person'],
    'doors'       : df['Doors'],
    'maintenance' : df['Maintenance'],
    'buying'      : df['Buying']
}

#----------------------------------------------------------------------------------------------------------------------#

def AttrSearch():
    global buying, maintenance, safety, doors, lugage, person, evaluation

    Attribut    = read_dataset
    buying      = Attribut['buying']
    maintenance = Attribut['maintenance']
    safety      = Attribut['safety']
    doors       = Attribut['doors']
    lugage      = Attribut['lugage']
    person      = Attribut['person']
    evaluation  = Attribut['evaluation']

#----------------------------------------------------------------------------------------------------------------------#

def evaluationSearch(attr):
    global q, w, e, r, total
    data_unacc, data_acc, data_good, data_vgood, total = 0, 0, 0, 0, 0

    for i in range(len(attr)):
        if (attr[i] == "unacc"):
            data_unacc += 1
        elif (attr[i] == "acc"):
            data_acc += 1
        elif (attr[i] == "good"):
            data_good += 1
        elif (attr[i] == "vgood"):
            data_vgood += 1

    total = data_unacc + data_acc + data_good + data_vgood
    q, w, e, r = data_unacc, data_acc, data_good, data_vgood

    return q, w, e, r, total

#----------------------------------------------------------------------------------------------------------------------#

def CariSafety(attr2):
    global q, w, e, r, total
    data_unacc, data_acc, data_good, data_vgood, total, hitung_gini = 0, 0, 0, 0, 0, 0

    Attribut = read_dataset
    safety     = Attribut['safety']
    evaluation = Attribut['evaluation']

    SafetyMedHigh = ('med', 'high')

    search_safety = []
    if (attr2 == 'low'):
        search_safety.append(attr2)
    elif (attr2 == 'med'):
        search_safety.append(attr2)
    elif (attr2 == 'high'):
        search_safety.append(attr2)
    else:
        search_safety.extend(SafetyMedHigh)

    for i in range(len(safety)):
        if (safety[i] in search_safety and evaluation[i] == "unacc"):
            data_unacc += 1
        elif (safety[i] in search_safety and evaluation[i] == "acc"):
            data_acc += 1
        elif (safety[i] in search_safety and evaluation[i] == "good"):
            data_good += 1
        elif (safety[i] in search_safety and evaluation[i] == "vgood"):
            data_vgood += 1

    total = data_unacc + data_acc + data_good + data_vgood

    if (total == 0):
        hitung_gini = 0
    else:
        hitung_gini = 1 - (data_unacc / (total)) ** 2 - (data_acc / (total)) ** 2 - \
                      (data_good / (total)) ** 2 - (data_vgood / (total)) ** 2

    q, w, e, r = data_unacc, data_acc, data_good, data_vgood

    return hitung_gini

#----------------------------------------------------------------------------------------------------------------------#

def CariLugage(attr2, attr3):
    global q, w, e, r, total
    data_unacc, data_acc, data_good, data_vgood, total, hitung_gini = 0, 0, 0, 0, 0, 0

    Attribut = read_dataset
    safety     = Attribut['safety']
    lugage     = Attribut['lugage']
    evaluation = Attribut['evaluation']

    Lugage = ('small', 'med', 'big')
    LugageMedBig = ('med', 'big')

    search_lugage = []
    if (attr2 == 'small'):
        search_lugage.append(attr2)
    elif (attr2 == 'med'):
        search_lugage.append(attr2)
    elif (attr2 == 'big'):
        search_lugage.append(attr2)
    elif (attr2 == 'MedBig'):
        search_lugage.extend(LugageMedBig)
    else:
        search_lugage.extend(Lugage)

    search_safety = []
    search_safety.append(attr3)

    for i in range(len(lugage)):
        if (lugage[i] in search_lugage and safety[i] in search_safety and evaluation[i] == "unacc"):
            data_unacc += 1
        elif (lugage[i] in search_lugage and safety[i] in search_safety and evaluation[i] == "acc"):
            data_acc += 1
        elif (lugage[i] in search_lugage and safety[i] in search_safety and evaluation[i] == "good"):
            data_good += 1
        elif (lugage[i] in search_lugage and safety[i] in search_safety and evaluation[i] == "vgood"):
            data_vgood += 1

    total = data_unacc + data_acc + data_good + data_vgood

    if (total == 0):
        hitung_gini = 0
    else:
        hitung_gini = 1 - (data_unacc / (total)) ** 2 - (data_acc / (total)) ** 2 - \
                      (data_good / (total)) ** 2 - (data_vgood / (total)) ** 2

    q, w, e, r = data_unacc, data_acc, data_good, data_vgood

    return hitung_gini

def CariPerson(attr2):
    global q, w, e, r, total
    data_unacc, data_acc, data_good, data_vgood, total, hitung_gini = 0, 0, 0, 0, 0, 0

    Attribut = read_dataset
    safety = Attribut['safety']
    lugage = Attribut['lugage']
    person = Attribut['person']
    evaluation = Attribut['evaluation']

    Person = ('3', '4', 'More')

    search = []

    if (attr2 == '2'):
        search.append(attr2)
    else:
        search.extend(Person)

    for i in range(len(person)):
        if (person[i] in search and lugage[i] == "small" and safety[i] == "med"  and evaluation[i] == "unacc"):
            data_unacc += 1
        elif (person[i] in search and lugage[i] == "small" and safety[i] == "med" and evaluation[i] == "acc"):
            data_acc += 1
        elif (person[i] in search and lugage[i] == "small" and safety[i] == "med" and evaluation[i] == "good"):
            data_good += 1
        elif (person[i] in search and lugage[i] == "small" and safety[i] == "med" and evaluation[i] == "vgood"):
            data_vgood += 1

    total = data_unacc + data_acc + data_good + data_vgood

    if (total == 0):
        hitung_gini = 0
    else:
        hitung_gini = 1 - (data_unacc / (total)) ** 2 - (data_acc / (total)) ** 2 - \
                      (data_good / (total)) ** 2 - (data_vgood / (total)) ** 2

    q, w, e, r = data_unacc, data_acc, data_good, data_vgood

    return hitung_gini

#----------------------------------------------------------------------------------------------------------------------#

def CariImpurity(parm, parm2):
    global q, w, e, r, total
    data_unacc, data_acc, data_good, data_vgood, total, hitung_gini = 0, 0, 0, 0, 0, 0

    Attribut = read_dataset
    evaluation = Attribut['evaluation']

    Doors4More = ('4', 'more')
    Person4More = ('4', 'More')
    LugageMedBig = ('med', 'big')
    SafetyMedHigh = ('med', 'high')

    search = []
    if (parm2 == '2'): #Persons
        search.append(parm2)
    elif (parm2 == '3'): #Doors
        search.append(parm2)
    elif (parm2 == 'Low'): #Buying
        search.append(parm2)
    elif (parm2 == 'low'): #Safety
        search.append(parm2)
    elif (parm2 == 'small'): #Lugage_Boot
        search.append(parm2)
    elif (parm2 == 'med'): #Maintenance
        search.append(parm2)

    elif (parm2 == 'MedHigh'): #Safety
        search.extend(SafetyMedHigh)
    elif (parm2 == 'more'):
        search.extend(Doors4More)
    elif (parm2 == 'MedBig'): #Lugage_Boot
        search.extend(LugageMedBig)
    elif (parm2 == '4more'):
        search.extend(Person4More)

    for i in range(len(parm)):
        if (parm[i] in search and evaluation[i] == "unacc"):
            data_unacc += 1
        elif (parm[i] in search and evaluation[i] == "acc"):
            data_acc += 1
        elif (parm[i] in search and evaluation[i] == "good"):
            data_good += 1
        elif (parm[i] in search and evaluation[i] == "vgood"):
            data_vgood += 1

    total = data_unacc + data_acc + data_good + data_vgood

    if (total == 0):
        hitung_gini = 0
    else:
        hitung_gini = 1 - (data_unacc / (total)) ** 2 - (data_acc / (total)) ** 2 - \
                      (data_good / (total)) ** 2 - (data_vgood / (total)) ** 2

    q, w, e, r = data_unacc, data_acc, data_good, data_vgood

    return hitung_gini



