import nodeCartFunc
from nodeCartFunc import cetakNode, hitungGiniA_Gain
from nodeSearch import CariImpurity, CariLugage, CariPerson, TotalImpurity, TotalLugage, TotalPerson

#                                               ~ ITERASI 1 ~
print("\n")
print("#"*34)
print("           Iterasi 1")
print("#"*34)
import nodeCountImpurity
safety = nodeCountImpurity.safety
nodeCartFunc.iterasiRoot()

# NODE KIRI
print("Node Kiri ------------------------")
print("----------------------------------")
# Data Safety Low
print("Data Safety Low")
gini_SafetyLow = CariImpurity(safety,'low')
totalSafety_Low = TotalImpurity(safety,'low')
cetakNode(totalSafety_Low,gini_SafetyLow,'D1')

# NODE KANAN
print("\nNode Kanan -----------------------")
print("----------------------------------")
# Data Safety Med || High
print("Data Safety Med || High")
gini_MedHigh = CariImpurity(safety,'MedHigh')
totalSafety_MedHigh = TotalImpurity(safety,'MedHigh')
cetakNode(totalSafety_MedHigh,gini_MedHigh,'D2')

# Iterasi 1 ~ Delta Gini A & ΔGini ~
print("\n----------------------------------")
print("\nIterasi 1  ~  GiniA & ΔGini ~")
hitungGiniA_Gain(totalSafety_Low,gini_SafetyLow,totalSafety_MedHigh,gini_MedHigh,nodeCountImpurity.total_eval,nodeCountImpurity.GinID_parent)
nodeCartFunc.iterasi1()
print("----------------------------------")

#                                               ~ ITERASI 2 ~
print("")
print("#"*34)
print("           Iterasi 2")
print("#"*34)

# NODE Label
print("\nNode Label ------------------------")
print("----------------------------------")
# Data Safety Low
print("Data Safety Low [unacc]")
gini_SafetyLow = CariImpurity(safety,'low')
totalSafety_Low = TotalImpurity(safety,'low')
cetakNode(totalSafety_Low,gini_SafetyLow,'D')

# Iterasi 2 ~ Delta Gini A & ΔGini ~
print("\n----------------------------------")
print("\n   Iterasi 2  ~ GiniA & ΔGini ~")
print("~" * 35)
nodeCartFunc.iterasi2()
print("----------------------------------")

#                                               ~ ITERASI 3 ~
print("")
print("#"*34)
print("           Iterasi 3")
print("#"*34)

# NODE PARENT
print("\nNode Parent -----------------------")
print("----------------------------------")
# Data Safety Med || High
print("Data Safety Med || High")
gini_MedHigh = CariImpurity(safety,'MedHigh')
totalSafety_MedHigh = TotalImpurity(safety,'MedHigh')
cetakNode(totalSafety_MedHigh,gini_MedHigh,'D')

# NODE KIRI
print("\nNode Kiri ------------------------")
print("----------------------------------")
# Data Safety Med
print("Data Safety Med")
gini_SafetyMed = CariImpurity(safety,'med')
totalSafety_Med = TotalImpurity(safety,'med')
cetakNode(totalSafety_Med,gini_SafetyMed,'D1')

# NODE KANAN
print("\nNode Kanan -----------------------")
print("----------------------------------")
# Data Safety High
print("Data Safety High")
gini_SafetyHigh = CariImpurity(safety,'high')
totalSafety_High = TotalImpurity(safety,'high')
cetakNode(totalSafety_High,gini_SafetyHigh,'D2')

# Iterasi 3 ~ Delta Gini A & ΔGini ~
print("\n----------------------------------")
print("\n   Iterasi 3 ~ GiniA & ΔGini ~")
hitungGiniA_Gain(totalSafety_Med,gini_SafetyMed,totalSafety_High,gini_SafetyHigh,totalSafety_MedHigh,gini_MedHigh)
nodeCartFunc.iterasi3()
print("----------------------------------")

#                                               ~ ITERASI 4 ~
print("")
print("#"*34)
print("           Iterasi 4")
print("#"*34)

# NODE PARENT
print("\nNode Parent ------------------------")
print("----------------------------------")
# Data Safety Med
print("Data Safety Med")
gini_SafetyMed = CariImpurity(safety,'med')
totalSafety_Med = TotalImpurity(safety,'med')
cetakNode(totalSafety_Med,gini_SafetyMed,'D')

# NODE KIRI
print("\nNode Kiri ------------------------")
print("----------------------------------")
# Data  Data Lugage Small
print("Data Lugage Small")
giniLugage_Small = CariLugage('small','med')
totalLugage_Small = TotalLugage('small','med')
cetakNode(totalLugage_Small,giniLugage_Small,'D1')

# NODE KANAN
print("\nNode Kanan -----------------------")
print("----------------------------------")
# Data Data Lugage Med || Big
print("Data Lugage Med || Big")
giniLugage_MedBig = CariLugage('MedBig','med')
totalLugage_MedBig = TotalLugage('MedBig','med')
cetakNode(totalLugage_MedBig,giniLugage_MedBig,'D2')

# Iterasi 4 ~ Delta Gini A & ΔGini ~
print("\n----------------------------------")
print("\nIterasi 4  ~  GiniA & ΔGini ~")
hitungGiniA_Gain(totalLugage_Small,giniLugage_Small,
    totalLugage_MedBig,giniLugage_MedBig,
    totalSafety_Med,gini_SafetyMed)
nodeCartFunc.iterasi4()
print("----------------------------------")

#                                               ~ ITERASI 5 ~
print("")
print("#"*34)
print("           Iterasi 5")
print("#"*34)

# NODE PARENT
print("\nNode Parent ------------------------")
print("----------------------------------")
# Data Lugage Small
print("Data Lugage Small")
giniLugage_Small = CariLugage('small','med')
totalLugage_Small = TotalLugage('small','med')
cetakNode(totalLugage_Small,giniLugage_Small,'D')

# NODE KIRI
print("\nNode Kiri ------------------------")
print("----------------------------------")
# Data Data Person 2
print("Data Person 2")
giniPerson_2 = CariPerson('2')
totalPerson_2 = TotalPerson('2')
cetakNode(totalPerson_2,giniPerson_2,'D1')

# NODE KANAN
print("\nNode Kanan -----------------------")
print("----------------------------------")
# Data Data Person 4 || More
print("Data Person 4 || More")
giniPerson_More = CariPerson('More')
totalPerson_More = TotalPerson('More')
cetakNode(totalPerson_More,giniPerson_More,'D2')

# Iterasi 5 ~ Delta Gini A & ΔGini ~
print("\n----------------------------------")
print("\nIterasi 5  ~  GiniA & ΔGini ~")
hitungGiniA_Gain(totalPerson_2,giniPerson_2,totalPerson_More,giniPerson_More,totalLugage_Small,giniLugage_Small)
nodeCartFunc.iterasi5()
print("----------------------------------")

#                                               ~ ITERASI 6 ~
print("")
print("#"*34)
print("           Iterasi 6")
print("#"*34)

# NODE LABEL
print("\nNode LABEL ------------------------")
print("----------------------------------")
# Data Data Person 2
print("Data Person 2 [unacc]")
giniPerson_2 = CariPerson('2')
totalPerson_2 = TotalPerson('2')
cetakNode(totalPerson_2,giniPerson_2,'D')

# Iterasi 6 ~ Delta Gini A & ΔGini ~
print("\n----------------------------------")
print("\n   Iterasi 6  ~ GiniA & ΔGini ~")
print("~" * 35)
nodeCartFunc.iterasi6()
print("----------------------------------")

#                                               ~ ITERASI 7 ~
print("")
print("#"*34)
print("           Iterasi 7")
print("#"*34)

# NODE LABEL
print("\nNode LABEL -----------------------")
print("----------------------------------")
# Data Data Person 4 || More
print("Data Person 4 || More [acc]")
giniPerson_More = CariPerson('More')
totalPerson_More = TotalPerson('More')
cetakNode(totalPerson_More,giniPerson_More,'D')

# Iterasi 7 ~ Delta Gini A & ΔGini ~
print("\n----------------------------------")
print("\n   Iterasi 7  ~ GiniA & ΔGini ~")
print("~" * 35)
nodeCartFunc.iterasi7()
print("----------------------------------")

#                                               ~ ITERASI 8 ~
print("")
print("#"*34)
print("           Iterasi 8 **")
print("#"*34)

# NODE LABEL
print("\nNode LABEL -----------------------")
print("----------------------------------")
# Data Data Lugage Med || Big
print("Data Lugage Med || Big [good]")
giniLugage_MedBig = CariLugage('MedBig','med')
totalLugage_MedBig = TotalLugage('MedBig','med')
cetakNode(totalLugage_MedBig,giniLugage_MedBig,'D2')

# Iterasi 8 ~ Delta Gini A & ΔGini ~
print("\n----------------------------------")
print("\n   Iterasi 8  ~ GiniA & ΔGini ~")
print("~" * 35)
nodeCartFunc.iterasi8()
print("----------------------------------")

#                                               ~ ITERASI 9 ~
print("")
print("#"*34)
print("           Iterasi 9")
print("#"*34)

# NODE PARENT
print("\nNode Parent -----------------------")
print("----------------------------------")
# Data Safety High
print("Data Safety High")
gini_SafetyHigh = CariImpurity(safety,'high')
totalSafety_High = TotalImpurity(safety,'high')
cetakNode(totalSafety_High,gini_SafetyHigh,'D')

# NODE KIRI
print("\nNode Kiri ------------------------")
print("----------------------------------")
# Data  Data Lugage Small
print("Data Lugage Small")
giniLugage_Small = CariLugage('small','high')
totalLugage_Small = TotalLugage('small','high')
cetakNode(totalLugage_Small,giniLugage_Small,'D1')

# NODE KANAN
print("\nNode Kanan -----------------------")
print("----------------------------------")
# Data Data Lugage Med || Big
print("Data Lugage Med || Big")
giniLugage_MedBig = CariLugage('MedBig','high')
totalLugage_MedBig = TotalLugage('MedBig','high')
cetakNode(totalLugage_MedBig,giniLugage_MedBig,'D2')

# Iterasi 8 ~ Delta Gini A & ΔGini ~
print("\n----------------------------------")
print("\nIterasi 8  ~  GiniA & ΔGini ~")
hitungGiniA_Gain(totalLugage_Small,giniLugage_Small,totalLugage_MedBig,giniLugage_MedBig,totalSafety_Med,gini_SafetyMed)
nodeCartFunc.iterasi9()
print("----------------------------------")

#                                               ~ ITERASI 10 ~
print("")
print("#"*34)
print("           Iterasi 10")
print("#"*34)

# NODE LABEL
print("\nNode LABEL -----------------------")
print("----------------------------------")
# Data Data Lugage Med
print("Data Lugage Med ")
giniLugage_MedBig = CariLugage('small','high')
totalLugage_MedBig = TotalLugage('small','high')
cetakNode(totalLugage_MedBig,giniLugage_MedBig,'D')

# Iterasi 8 ~ Delta Gini A & ΔGini ~
print("\n----------------------------------")
print("\n   Iterasi 10  ~ GiniA & ΔGini ~")
print("~" * 35)
nodeCartFunc.iterasi10()
print("----------------------------------")

#                                               ~ ITERASI 11 ~
print("")
print("#"*34)
print("           Iterasi 11")
print("#"*34)

# NODE LABEL
print("\nNode LABEL -----------------------")
print("----------------------------------")
# Data Data Lugage Med || Big
print("Data Lugage Med || Big")
giniLugage_MedBig = CariLugage('MedBig','high')
totalLugage_MedBig = TotalLugage('MedBig','high')
cetakNode(totalLugage_MedBig,giniLugage_MedBig,'D')

# Iterasi 8 ~ Delta Gini A & ΔGini ~
print("\n----------------------------------")
print("\n   Iterasi 11  ~ GiniA & ΔGini ~")
print("~" * 35)
nodeCartFunc.iterasi11()
print("----------------------------------")