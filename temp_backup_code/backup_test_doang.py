import pandas as pd

#import hitung_impurity
import nodeSearch
#from hitung_impurity import AttrSearch
from nodeSearch import evaluationSearch
from nodeSearch import CariSafety, CariLugage, CariPerson
from nodeTotal import TotalSafety, TotalLugage, TotalPerson

df = pd.read_csv('dataset.csv')

eval = df["Evaluation"].tolist()
evaluationSearch(eval)
total_eval = len(df['Evaluation'])
total_GiniP = labelSearch.total
#

# ~ ITERASI 1 ~
print("\n")
print("#"*34)
print("           Iterasi 1")
print("#"*34)

# # Data Gini Parent
# unacc, acc, good, vgood = labelSearch.q, labelSearch.w, labelSearch.e, labelSearch.r
# #labelCount()
# GinID_parent = 1-(unacc/(total_eval))**2-(acc/(total_eval))**2-(good/(total_eval))**2-(vgood/(total_eval))**2
# print("\n         Data Gini Parent")
# print("="*34)
# print("Total Data   :", total_eval)
# print("Unacceptance :", unacc)
# print("Acceptance   :", acc)
# print("Good         :", good)
# print("Very Good    :", vgood)
# print("="*34)
# print("Gini Parent :", float(GinID_parent))
#
# # Data Safety Low
# gini_SafetyLow = CariSafety('low')
# totalSafety_Low = TotalSafety('low')
# unacc, acc, good, vgood = labelSearch.q, labelSearch.w, labelSearch.e, labelSearch.r
# print("\n         Data Safety Low")
#
#
# #labelCount()
# unacc, acc, good, vgood = labelSearch.q, labelSearch.w, labelSearch.e, labelSearch.r
# print("\n     Data Safety Med || High")
# print("="*34)
# print("Total Data   :", totalSafety_MedHigh)
# print("Unacceptance :", unacc)
# print("Acceptance   :", acc)
# print("Good         :", good)
# print("Very Good    :", vgood)
# print("="*34)
# print("Gini (D2) : {:.9f}".format(gini_MedHigh))
#
# # Iterasi 1 Delta Gini A & ΔGini
# print("")
# print("~"*34)
# bobotRata = (((totalSafety_Low/total_GiniP)*gini_SafetyLow)+((totalSafety_MedHigh/total_GiniP)*gini_MedHigh))
# gain = float(GinID_parent) - bobotRata
# print("Gini A = {:.9f}".format(bobotRata))
# print("ΔGini = {:.9f}".format(gain))
# print("~"*34)


# ITERASI 2
print("")
print("#"*34)
print("           Iterasi 2")
print("#"*34)

# Data Safety Low [unacc]
filter = df['Safety']=='low'
total_safetyLow = len(df.loc[filter, 'Evaluation'])
giniTotalSafetyLow = labelSearch.label_search('Safety', 'low')
unacc, acc, good, vgood = labelSearch.data_unacc, labelSearch.data_acc, labelSearch.data_good, labelSearch.data_vgood
print("\n      Data Safety Low [unacc]")
print("="*34)
print("Total Data   :", total_safetyLow)
print("Unacceptance :", unacc)
print("Acceptance   :", acc)
print("Good         :", good)
print("Very Good    :", vgood)
print("="*34)
print("Gini (D) :", giniTotalSafetyLow)

# # ITERASI 3
# print("")
# print("#"*34)
# print("           Iterasi 3")
# print("#"*34)
#
# filter = df['Safety']=='med'
# total_safetyMed = len(df.loc[filter, 'Evaluation'])
# giniTotalSafetyMed = labelSearch.label_search('Safety', 'med')
# unacc, acc, good, vgood = labelSearch.data_unacc, labelSearch.data_acc, labelSearch.data_good, labelSearch.data_vgood
# print("\n         Data Safety Med")
# print("="*34)
# print("Total Data   :", total_safetyMed)
# print("Unacceptance :", unacc)
# print("Acceptance   :", acc)
# print("Good         :", good)
# print("Very Good    :", vgood)
# print("="*34)
# print("Gini (D1) : {:.8f}".format(giniTotalSafetyMed))
#
# filter = df['Safety']=='high'
# total_safetyHigh = len(df.loc[filter, 'Evaluation'])
# giniTotalSafetyHigh = labelSearch.label_search('Safety', 'high')
# unacc, acc, good, vgood = labelSearch.data_unacc, labelSearch.data_acc, labelSearch.data_good, labelSearch.data_vgood
# print("\n         Data Safety High")
# print("="*34)
# print("Total Data   :", total_safetyHigh)
# print("Unacceptance :", unacc)
# print("Acceptance   :", acc)
# print("Good         :", good)
# print("Very Good    :", vgood)
# print("="*34)
# print("Gini (D2) : {:.2f}".format(giniTotalSafetyHigh))
#
# # Iterasi 3 Delta Gini A & ΔGini
# print("")
# print("~"*34)
# bobotRata = (((total_safetyMed / totalSafety_MedHigh) * giniTotalSafetyMed) + ((total_safetyHigh / totalSafety_MedHigh) * giniTotalSafetyHigh))
# gain = gini_MedHigh - bobotRata
# print("GiniA (D) = {:.9f}".format(bobotRata))
# print("ΔGini (D) = {:.9f}".format(gain))
# print("~"*34)
#
# # ITERASI 4
# print("")
# print("#"*34)
# print("           Iterasi 4")
# print("#"*34)
#
# filter = df['Safety']=='med'
# total_safetyMed = len(df.loc[filter, 'Evaluation'])
# giniTotalSafetyMed = labelSearch.label_search('Safety', 'med')
# unacc, acc, good, vgood = labelSearch.data_unacc, labelSearch.data_acc, labelSearch.data_good, labelSearch.data_vgood
# print("\n         Data Safety Med")
# print("="*34)
# print("Total Data   :", total_safetyMed)
# print("Unacceptance :", unacc)
# print("Acceptance   :", acc)
# print("Good         :", good)
# print("Very Good    :", vgood)
# print("="*34)
# print("Gini (D) : {:.8f}".format(giniTotalSafetyMed))
#
# giniLugage_small = CariLugage('small', 'med')
# unacc, acc, good, vgood = labelSearch.data_unacc, labelSearch.data_acc, labelSearch.data_good, labelSearch.data_vgood
# total_lugageSmall = TotalLugage('small', 'med')
# print("\n        Data Lugage Small")
# print("="*34)
# print("Total Data   :", total_lugageSmall)
# print("Unacceptance :", unacc)
# print("Acceptance   :", acc)
# print("Good         :", good)
# print("Very Good    :", vgood)
# print("="*34)
# print("Gini (D1) : {:.8f}".format(giniLugage_small))
#
# # Data Safety Lugage Med || Big
# giniLugage_MedBig = CariLugage('','med')
# total_lugageMedBig = TotalLugage('MedBig','med')
# unacc, acc, good, vgood = labelSearch.data_unacc, labelSearch.data_acc, labelSearch.data_good, labelSearch.data_vgood
# print("\n     Data Lugage Med || Big")
# print("="*34)
# print("Total Data   :", total_lugageMedBig)
# print("Unacceptance :", unacc)
# print("Acceptance   :", acc)
# print("Good         :", good)
# print("Very Good    :", vgood)
# print("="*34)
# print("Gini (D2) :", giniLugage_MedBig)
#
# # Iterasi 4 Delta Gini A & ΔGini
# print("")
# print("~"*34)
# bobotRata = (((total_lugageSmall/total_safetyMed)*giniLugage_small)+((total_lugageMedBig/total_safetyMed)*giniLugage_MedBig))
# gain = giniTotalSafetyMed - bobotRata
# print("GiniA (D) = {:.9f}".format(bobotRata))
# print("ΔGini (D) = {:.9f}".format(gain))
# print("~"*34)
#
# # ITERASI 5
# print("")
# print("#"*34)
# print("           Iterasi 5")
# print("#"*34)
#
# giniLugage_small = CariLugage('small', 'med')
# unacc, acc, good, vgood = labelSearch.data_unacc, labelSearch.data_acc, labelSearch.data_good, labelSearch.data_vgood
# total_lugageSmall = TotalLugage('small', 'med')
# print("\n        Data Lugage Small")
# print("="*34)
# print("Total Data   :", total_lugageSmall)
# print("Unacceptance :", unacc)
# print("Acceptance   :", acc)
# print("Good         :", good)
# print("Very Good    :", vgood)
# print("="*34)
# print("Gini (D1) : {:.8f}".format(giniLugage_small))
#
# giniPerson = CariPerson('2')
# unacc, acc, good, vgood = labelSearch.data_unacc, labelSearch.data_acc, labelSearch.data_good, labelSearch.data_vgood
# total_PersonDua = TotalPerson('2','small','med')
# print("\n         Data Person 2")
# print("="*34)
# print("Total Data   :", total_PersonDua)
# print("Unacceptance :", unacc)
# print("Acceptance   :", acc)
# print("Good         :", good)
# print("Very Good    :", vgood)
# print("="*34)
# print("Gini (D1) : {:.8f}".format(giniPerson))
#
# giniPerson = CariPerson('more')
# unacc, acc, good, vgood = labelSearch.data_unacc, labelSearch.data_acc, labelSearch.data_good, labelSearch.data_vgood
# total_PersonMore = TotalPerson('more','small','med')
# print("\n      Data Person 4 || More")
# print("="*34)
# print("Total Data   :", total_PersonMore)
# print("Unacceptance :", unacc)
# print("Acceptance   :", acc)
# print("Good         :", good)
# print("Very Good    :", vgood)
# print("="*34)
# print("Gini (D2) : {:.8f}".format(giniPerson))
#
# print("")
# print("~"*34)
# bobotRata = (((total_lugageSmall/total_safetyMed)*giniLugage_small)+((total_lugageMedBig/total_safetyMed)*giniLugage_MedBig))
# gain = giniTotalSafetyMed - bobotRata
# print("GiniA (D) = {:.9f}".format(bobotRata))
# print("ΔGini (D) = {:.9f}".format(gain))
# print("~"*34)
#
#
#
# # ITERASI 6
# print("")
# print("#"*34)
# print("           Iterasi 6")
# print("#"*34)
#
# giniPerson = CariPerson('2')
# unacc, acc, good, vgood = labelSearch.data_unacc, labelSearch.data_acc, labelSearch.data_good, labelSearch.data_vgood
# total_lugageSmall = TotalPerson('2','small','med')
# print("\n      Data Person 2 [unacc]")
# print("="*34)
# print("Total Data   :", total_lugageSmall)
# print("Unacceptance :", unacc)
# print("Acceptance   :", acc)
# print("Good         :", good)
# print("Very Good    :", vgood)
# print("="*34)
# print("Gini (D) : {:.8f}".format(giniPerson))
#
# # ITERASI 7
# print("")
# print("#"*34)
# print("           Iterasi 7")
# print("#"*34)
#
# giniPerson = CariPerson('more')
# unacc, acc, good, vgood = labelSearch.data_unacc, labelSearch.data_acc, labelSearch.data_good, labelSearch.data_vgood
# total_PersonMore = TotalPerson('more','small','med')
# print("\n    Data Person 4 || More [acc]")
# print("="*34)
# print("Total Data   :", total_PersonMore)
# print("Unacceptance :", unacc)
# print("Acceptance   :", acc)
# print("Good         :", good)
# print("Very Good    :", vgood)
# print("="*34)
# print("Gini (D) : {:.8f}".format(giniPerson))
#
# # ITERASI 8
# print("")
# print("#"*34)
# print("           Iterasi 8")
# print("#"*34)
#
# giniLugage_MedBig = CariLugage('MedBig','med')
# total_lugageMedBig = TotalLugage('MedBig','med')
# unacc, acc, good, vgood = labelSearch.data_unacc, labelSearch.data_acc, labelSearch.data_good, labelSearch.data_vgood
# print("\n  Data Lugage Med || Big [Good]")
# print("="*34)
# print("Total Data   :", total_lugageMedBig)
# print("Unacceptance :", unacc)
# print("Acceptance   :", acc)
# print("Good         :", good)
# print("Very Good    :", vgood)
# print("="*34)
# print("Gini (D) :", giniLugage_MedBig)
#
# # ITERASI 9
# print("")
# print("#"*34)
# print("           Iterasi 9")
# print("#"*34)
#
# filter = df['Safety']=='high'
# total_safetyHigh = len(df.loc[filter, 'Evaluation'])
# giniTotalSafetyHigh = labelSearch.label_search('Safety', 'high')
# unacc, acc, good, vgood = labelSearch.data_unacc, labelSearch.data_acc, labelSearch.data_good, labelSearch.data_vgood
# print("\n         Data Safety High")
# print("="*34)
# print("Total Data   :", total_safetyHigh)
# print("Unacceptance :", unacc)
# print("Acceptance   :", acc)
# print("Good         :", good)
# print("Very Good    :", vgood)
# print("="*34)
# print("Gini (D) : {:.2f}".format(giniTotalSafetyHigh))
#
# giniSafetyHigh_Lugagesmall = CariLugage('small','high')
# totalSafetyHigh_lugageSmall = TotalLugage('small', 'high')
# unacc, acc, good, vgood = labelSearch.data_unacc, labelSearch.data_acc, labelSearch.data_good, labelSearch.data_vgood
# print("\n        Data Safety High ")
# print("          Lugage Small ")
# print("="*34)
# print("Total Data   :", totalSafetyHigh_lugageSmall)
# print("Unacceptance :", unacc)
# print("Acceptance   :", acc)
# print("Good         :", good)
# print("Very Good    :", vgood)
# print("="*34)
# print("Gini (D1) : {:.8f}".format(giniSafetyHigh_Lugagesmall))
#
# giniSafetyHigh_LugageMedBig = CariLugage('MedBig','high')
# totalSafetyHigh_lugageMedBig = TotalLugage('MedBig', 'high')
# unacc, acc, good, vgood = labelSearch.data_unacc, labelSearch.data_acc, labelSearch.data_good, labelSearch.data_vgood
# print("\n       Data Safety High ")
# print("      Lugage Med || Big ")
# print("="*34)
# print("Total Data   :", totalSafetyHigh_lugageMedBig)
# print("Unacceptance :", unacc)
# print("Acceptance   :", acc)
# print("Good         :", good)
# print("Very Good    :", vgood)
# print("="*34)
# print("Gini (D2) :", giniSafetyHigh_LugageMedBig)
#
# print("")
# print("~"*34)
# bobotRata = (((totalSafetyHigh_lugageSmall/total_safetyHigh)*giniSafetyHigh_Lugagesmall)+((totalSafetyHigh_lugageMedBig/total_safetyHigh)*giniSafetyHigh_LugageMedBig))
# gain = giniTotalSafetyHigh - bobotRata
# print("GiniA (D) = {:.1f}".format(bobotRata))
# print("ΔGini (D) = {:.2f}".format(gain))
# print("~"*34)
#
# # ITERASI 10
# print("")
# print("#"*34)
# print("           Iterasi 10")
# print("#"*34)
#
# giniSafetyHigh_Lugagesmall = CariLugage('small','high')
# totalSafetyHigh_lugageSmall = TotalLugage('small', 'high')
# unacc, acc, good, vgood = labelSearch.data_unacc, labelSearch.data_acc, labelSearch.data_good, labelSearch.data_vgood
# print("\n     Data Safety High [Good] ")
# print("          Lugage Small ")
# print("="*34)
# print("Total Data   :", totalSafetyHigh_lugageSmall)
# print("Unacceptance :", labelSearch.data_unacc)
# print("Acceptance   :", acc)
# print("Good         :", good)
# print("Very Good    :", vgood)
# print("="*34)
# print("Gini (D) : {:.8f}".format(giniSafetyHigh_Lugagesmall))
#
# # ITERASI 11
# print("")
# print("#"*34)
# print("           Iterasi 11")
# print("#"*34)
#
# giniSafetyHigh_LugageMedBig = CariLugage('MedBig','high')
# totalSafetyHigh_lugageMedBig = TotalLugage('MedBig','high')
# unacc, acc, good, vgood = labelSearch.data_unacc, labelSearch.data_acc, labelSearch.data_good, labelSearch.data_vgood
# print("\n   Data Safety High [vGood] ")
# print("       Lugage Med || Big ")
# print("="*34)
# print("Total Data   :", totalSafetyHigh_lugageMedBig)
# print("Unacceptance :", unacc)
# print("Acceptance   :", acc)
# print("Good         :", good)
# print("Very Good    :", vgood)
# print("="*34)
# print("Gini (D) :", giniSafetyHigh_LugageMedBig)
