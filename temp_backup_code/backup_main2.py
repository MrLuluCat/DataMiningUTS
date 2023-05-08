import nodeCartFunc
import nodeSearch
import backup_CartTree
from nodeCartFunc import cetakNode, hitungGiniA_Gain
from nodeSearch import CariSafety
from nodeTotal import TotalSafety

# ~ ITERASI 1 ~
print("\n")
print("#"*34)
print("           Iterasi 1")
print("#"*34)
import nodeCountImpurity
CartTree.iterasi0()

# NODE KIRI
print("Node Kiri ------------------------")
print("----------------------------------")
# Data Safety Low
print("         Data Safety Low")
gini_SafetyLow = CariSafety('low')
totalSafety_Low = TotalSafety('low')
cetakNode(totalSafety_Low,gini_SafetyLow)

# NODE KANAN
print("\nNode Kanan -----------------------")
print("----------------------------------")
# Data Safety Med || High
print("     Data Safety Med || High")
gini_MedHigh = CariSafety('MedHigh')
totalSafety_MedHigh = TotalSafety('MedHigh')
cetakNode(totalSafety_MedHigh,gini_MedHigh)

print("\n----------------------------------")
# Iterasi 1 ~ Delta Gini A & ΔGini ~
print("\n   Iterasi 1  ~  GiniA & ΔGini ~")
hitungGiniA_Gain(totalSafety_Low,gini_SafetyLow,totalSafety_MedHigh,gini_MedHigh,hitung_impurity.total_eval,hitung_impurity.GinID_parent)
CartTree.iterasi1()
print("----------------------------------")
