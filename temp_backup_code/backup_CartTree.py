from treelib import Tree

def iterasiRoot():
    tree = Tree()
    node = tree.create_node
    node("Root", "root")
    node("|", "center", parent="root")
    tree.show()

def iterasi1():
    tree = Tree()
    node = tree.create_node
    node("Root", "root")
    node("{L} Safety [Low]", "left", parent = "root")
    node("{R} Safety [Med,High]", "right", parent = "root")
    tree.show()

def iterasi2():
    tree = Tree()
    node = tree.create_node
    node("Root", "root")
    node("{L} Safety [Low] unacc", "left", parent = "root")
    node("{R} Safety [Med,High]", "right", parent = "root")
    tree.show()

def iterasi3():
    tree = Tree()
    node = tree.create_node
    node("Root", "root")
    node("{L} Safety [Low] unacc", "left", parent = "root")
    node("{R} Safety [Med,High]", "right", parent = "root")
    node("{L} Safety [Med]", "left2", parent ="right")
    node("{R} Safety [High]", "right2", parent="right")
    tree.show()

def iterasi4():
    tree = Tree()
    node = tree.create_node
    node("Root", "root")
    node("{L} Safety [Low] unacc", "left", parent = "root")
    node("{R} Safety [Med,High]", "right", parent = "root")
    node("{L} Safety [Med]", "left2", parent ="right")
    node("{R} Safety [High]", "right2", parent="right")
    node("{L} Lugage [Small]", "left3", parent="left2")
    node("{R} Lugage [Med, Big]", "right3", parent="left2")
    tree.show()

def iterasi5():
    tree = Tree()
    node = tree.create_node
    node("Root", "root")
    node("{L} Safety [Low] unacc", "left", parent = "root")
    node("{R} Safety [Med,High]", "right", parent = "root")
    node("{L} Safety [Med]", "left2", parent ="right")
    node("{R} Safety [High]", "right2", parent="right")
    node("{L} Lugage [Small]", "left3", parent="left2")
    node("{R} Lugage [Med, Big]", "right3", parent="left2")
    node("{L} Persons [2]", "left4", parent="left3")
    node("{R} Persons [4,More]", "right4", parent="left3")
    tree.show()

def iterasi6():
    tree = Tree()
    node = tree.create_node
    node("Root", "root")
    node("{L} Safety [Low] unacc", "left", parent = "root")
    node("{R} Safety [Med,High]", "right", parent = "root")
    node("{L} Safety [Med]", "left2", parent ="right")
    node("{R} Safety [High]", "right2", parent="right")
    node("{L} Lugage [Small]", "left3", parent="left2")
    node("{R} Lugage [Med, Big]", "right3", parent="left2")
    node("{L} Persons [2] unacc", "left4", parent="left3")
    node("{R} Persons [4,More]", "right4", parent="left3")
    tree.show()

def iterasi7():
    tree = Tree()
    node = tree.create_node
    node("Root", "root")
    node("{L} Safety [Low] unacc", "left", parent = "root")
    node("{R} Safety [Med,High]", "right", parent = "root")
    node("{L} Safety [Med]", "left2", parent ="right")
    node("{R} Safety [High]", "right2", parent="right")
    node("{L} Lugage [Small]", "left3", parent="left2")
    node("{R} Lugage [Med, Big]", "right3", parent="left2")
    node("{L} Persons [2] unacc", "left4", parent="left3")
    node("{R} Persons [4,More] acc", "right4", parent="left3")
    tree.show()

def iterasi8():
    tree = Tree()
    node = tree.create_node
    node("Root", "root")
    node("{L} Safety [Low] unacc", "left", parent = "root")
    node("{R} Safety [Med,High]", "right", parent = "root")
    node("{L} Safety [Med]", "left2", parent ="right")
    node("{R} Safety [High]", "right2", parent="right")
    node("{L} Lugage [Small]", "left3", parent="left2")
    node("{R} Lugage [Med, Big] good", "right3", parent="left2")
    node("{L} Persons [2] unacc", "left4", parent="left3")
    node("{R} Persons [4,More] acc", "right4", parent="left3")
    tree.show()

def iterasi9():
    tree = Tree()
    node = tree.create_node
    node("Root", "root")
    node("{L} Safety [Low] unacc", "left", parent = "root")
    node("{R} Safety [Med,High]", "right", parent = "root")
    node("{L} Safety [Med]", "left2", parent ="right")
    node("{R} Safety [High]", "right2", parent="right")
    node("{L} Lugage [Small]", "left3", parent="left2")
    node("{R} Lugage [Med, Big] good", "right3", parent="left2")
    node("{L} Persons [2] unacc", "left4", parent="left3")
    node("{R} Persons [4,More] acc", "right4", parent="left3")
    node("{L} Lugage [Small]", "left5", parent="right2")
    node("{R} Lugage [Med, Big]", "right5", parent="right2")
    tree.show()

def iterasi10():
    tree = Tree()
    node = tree.create_node
    node("Root", "root")
    node("{L} Safety [Low] unacc", "left", parent = "root")
    node("{R} Safety [Med,High]", "right", parent = "root")
    node("{L} Safety [Med]", "left2", parent ="right")
    node("{R} Safety [High]", "right2", parent="right")
    node("{L} Lugage [Small]", "left3", parent="left2")
    node("{R} Lugage [Med, Big] good", "right3", parent="left2")
    node("{L} Persons [2] unacc", "left4", parent="left3")
    node("{R} Persons [4,More] acc", "right4", parent="left3")
    node("{L} Lugage [Small] good", "left5", parent="right2")
    node("{R} Lugage [Med, Big]", "right5", parent="right2")
    tree.show()

def iterasi11():
    tree = Tree()
    node = tree.create_node
    node("Root", "root")
    node("{L} Safety [Low] unacc", "left", parent = "root")
    node("{R} Safety [Med,High]", "right", parent = "root")
    node("{L} Safety [Med]", "left2", parent ="right")
    node("{R} Safety [High]", "right2", parent="right")
    node("{L} Lugage [Small]", "left3", parent="left2")
    node("{R} Lugage [Med, Big] good", "right3", parent="left2")
    node("{L} Persons [2] unacc", "left4", parent="left3")
    node("{R} Persons [4,More] acc", "right4", parent="left3")
    node("{L} Lugage [Small] good", "left5", parent="right2")
    node("{R} Lugage [Med, Big] vgood", "right5", parent="right2")
    tree.show()

# print("Root")
# print(" |---Safety[low]")
# print(" |---Safety[med,high]")
# print("        |------------Safety [med]")
# print("                        |---------Luggage [small]")
# print("                        |            |-------------Persons [4] unacc")
# print("                        |            |-------------Persons [2,3,more] acc")
# print("                        |---------Luggage [med,big]")
# print("        |------------Safety [high]")
# print("                        |---------Luggage [small] good")
# print("                        |---------Luggage [med,big]")