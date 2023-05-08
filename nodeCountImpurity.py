import pandas as pd

import nodeSearch
from nodeCartFunc import hitungGiniA_Gain
from nodeSearch import evaluationSearch, AttrSearch, CariImpurity, TotalImpurity

df = pd.read_csv('dataset.csv')
eval = df["Evaluation"].tolist()
evaluationSearch(eval)
total_eval = len(df['Evaluation'])
total_GiniP = nodeSearch.t

AttrSearch()
buying, maintenance, safety, doors, lugage, person = \
    nodeSearch.buying, nodeSearch.maintenance, \
    nodeSearch.safety, nodeSearch.doors, \
    nodeSearch.lugage, nodeSearch.person

def labelCount2():
    global unacc, acc, good, vgood
    unacc, acc, good, vgood = nodeSearch.q, nodeSearch.w, nodeSearch.e, nodeSearch.r

    return unacc, acc, good, vgood

# Data Gini Parent
labelCount2()
GinID_parent = 1-(unacc/(total_eval))**2-(acc/(total_eval))**2-(good/(total_eval))**2-(vgood/(total_eval))**2
print("\n         Data Gini Parent")
print("="*34)
print("Total Data   :", total_eval)
print("Unacceptance :", unacc)
print("Acceptance   :", acc)
print("Good         :", good)
print("Very Good    :", vgood)
print("="*34)
print("Gini Parent :", float(GinID_parent))

# Impurity Buying Low
giniBuying_Low = CariImpurity(buying, 'Low')
total_BuyingLow = TotalImpurity(buying,'Low')
labelCount2()
print("\n         Data Buying Low")
print("="*34)
print("Total Data   :", total_BuyingLow)
print("Unacceptance :", unacc)
print("Acceptance   :", acc)
print("Good         :", good)
print("Very Good    :", vgood)
print("="*34)
print("Gini (D1) :", giniBuying_Low)

# Impurity Buying Med || High
giniBuying_MedHigh = CariImpurity(buying, 'MedHigh')
total_BuyingMedHigh = TotalImpurity(buying,'MedHigh')
labelCount2()
print("\n      Data Buying Med || High")
print("="*34)
print("Total Data   :", total_BuyingMedHigh)
print("Unacceptance :", unacc)
print("Acceptance   :", acc)
print("Good         :", good)
print("Very Good    :", vgood)
print("="*34)
print("Gini (D2) :", giniBuying_MedHigh)
#parm1-2 = node1, parm 3-4 = node2, parm 5 = total, parm 6 = gini parent
hitungGiniA_Gain(total_BuyingLow,giniBuying_Low,total_BuyingMedHigh,giniBuying_MedHigh,total_eval,GinID_parent)

# Impurity Maintenance Low
giniMaintenance_Low = CariImpurity(maintenance, 'Low')
total_MaintenanceLow = TotalImpurity(maintenance,'Low')
labelCount2()
print("\n      Data Maintenance Low")
print("="*34)
print("Total Data   :", total_MaintenanceLow)
print("Unacceptance :", unacc)
print("Acceptance   :", acc)
print("Good         :", good)
print("Very Good    :", vgood)
print("="*34)
print("Gini (D) :", giniMaintenance_Low)

# Impurity Maintenance Med
giniMaintenance_MedHigh = CariImpurity(maintenance, 'med')
total_MaintenanceMedHigh = TotalImpurity(maintenance,'med')
labelCount2()
print("\n      Data Maintenance Med")
print("="*34)
print("Total Data   :", total_MaintenanceMedHigh)
print("Unacceptance :", unacc)
print("Acceptance   :", acc)
print("Good         :", good)
print("Very Good    :", vgood)
print("="*34)
print("Gini (D) :", giniMaintenance_MedHigh)
#parm1-2 = node1, parm 3-4 = node2, parm 5 = total, parm 6 = gini parent
hitungGiniA_Gain(total_MaintenanceLow,giniMaintenance_Low,total_MaintenanceMedHigh,giniMaintenance_MedHigh,total_eval,GinID_parent)


# Impurity Doors 3
giniDoors_Low = CariImpurity(doors, '3')
total_DoorsLow = TotalImpurity(doors,'3')
labelCount2()
print("\n         Data Doors 3")
print("="*34)
print("Total Data   :", total_DoorsLow)
print("Unacceptance :", unacc)
print("Acceptance   :", acc)
print("Good         :", good)
print("Very Good    :", vgood)
print("="*34)
print("Gini (D) :", giniDoors_Low)

# Impurity Doors 4 || More
giniDoors_More = CariImpurity(doors, 'more')
total_DoorsMore = TotalImpurity(doors,'more')
labelCount2()
print("\n       Data Doors 4 || More")
print("="*34)
print("Total Data   :", total_DoorsMore)
print("Unacceptance :", unacc)
print("Acceptance   :", acc)
print("Good         :", good)
print("Very Good    :", vgood)
print("="*34)
print("Gini (D) :", giniDoors_More)
#parm1-2 = node1, parm 3-4 = node2, parm 5 = total, parm 6 = gini parent
hitungGiniA_Gain(total_DoorsLow,giniDoors_Low,total_DoorsMore,giniDoors_More,total_eval,GinID_parent)

# Impurity Person 2
giniPerson_dua = CariImpurity(person,'2')
total_PersonDua = TotalImpurity(person,'2')
labelCount2()
print("\n         Data Person 2")
print("="*34)
print("Total Data   :", total_PersonDua)
print("Unacceptance :", unacc)
print("Acceptance   :", acc)
print("Good         :", good)
print("Very Good    :", vgood)
print("="*34)
print("Gini (D) :", giniPerson_dua)

# Impurity Person 4 || More
giniPerson_More = CariImpurity(person,'4more')
total_PersonMore = TotalImpurity(person,'4more')
labelCount2()
print("\n      Data Person 4 || More")
print("="*34)
print("Total Data   :", total_PersonMore)
print("Unacceptance :", unacc)
print("Acceptance   :", acc)
print("Good         :", good)
print("Very Good    :", vgood)
print("="*34)
print("Gini (D) {:.9f}".format(giniPerson_More))
#parm1-2 = node1, parm 3-4 = node2, parm 5 = total, parm 6 = gini parent
hitungGiniA_Gain(total_PersonDua,giniPerson_dua,total_PersonMore,giniPerson_More,total_eval,GinID_parent)


# Impurity Lugage_boot Small
giniLugage_Small = CariImpurity(lugage,'small')
total_lugageSmall = TotalImpurity(lugage,'small')
labelCount2()
print("\n        Data Lugage Small")
print("="*34)
print("Total Data   :", total_lugageSmall)
print("Unacceptance :", unacc)
print("Acceptance   :", acc)
print("Good         :", good)
print("Very Good    :", vgood)
print("="*34)
print("Gini (D) :", giniLugage_Small)

# Impurity Lugage_boot Med || Big
giniLugage_MedBig = CariImpurity(lugage, 'MedBig')
total_lugageMedBig = TotalImpurity(lugage,'MedBig')
labelCount2()
print("\n     Data Lugage Med || Big")
print("="*34)
print("Total Data   :", total_lugageMedBig)
print("Unacceptance :", unacc)
print("Acceptance   :", acc)
print("Good         :", good)
print("Very Good    :", vgood)
print("="*34)
print("Gini (D) :", giniLugage_MedBig)
#parm1-2 = node1, parm 3-4 = node2, parm 5 = total, parm 6 = gini parent
hitungGiniA_Gain(total_lugageSmall,giniLugage_Small,total_lugageMedBig,giniLugage_MedBig,total_eval,GinID_parent)


# Impurity Safety Low
giniSafety_low = CariImpurity(safety, 'low')
total_SafetyLow = TotalImpurity(safety, 'low')
labelCount2()
print("\n        Data Safety Low")
print("="*34)
print("Total Data   :", total_SafetyLow)
print("Unacceptance :", unacc)
print("Acceptance   :", acc)
print("Good         :", good)
print("Very Good    :", vgood)
print("="*34)
print("Gini (D) :", giniSafety_low)

# Impurity Safety Med || High
giniSafety_MedHigh = CariImpurity(safety,'MedHigh')
total_SafetyMedHighMedHigh = TotalImpurity(safety,'MedHigh')
labelCount2()
print("\n     Data Safety Med || High")
print("="*34)
print("Total Data   :", total_SafetyMedHighMedHigh)
print("Unacceptance :", unacc)
print("Acceptance   :", acc)
print("Good         :", good)
print("Very Good    :", vgood)
print("="*34)
print("Gini (D) :", giniSafety_MedHigh)
hitungGiniA_Gain(total_SafetyLow,
                 giniSafety_low,total_SafetyMedHighMedHigh,
                 giniSafety_MedHigh,total_eval,
                 GinID_parent)

print("\n----------------------------------")
print("           Root Node : ")
print(" ΔGini (D) Terbesar Adalah Safety")
hitungGiniA_Gain(
    total_SafetyLow,
    giniSafety_low,
    total_SafetyMedHighMedHigh,
    giniSafety_MedHigh,
    total_eval,
    GinID_parent)