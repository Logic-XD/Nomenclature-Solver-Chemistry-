cations = [["Li", "lithium", 1, 1], ["Be", "berylium", 1, 2],
["Na", "sodium", 1, 1], ["Mg", "magnesium", 1, 2], 
["K", "potassium", 1, 1], ["Ca", "calcium", 1, 2], 
["Rb", "rubidium", 1, 1], ["Sr", "strontium", 1, 2], 
["Cs", "cesium", 1, 1], ["Ba", "barium", 1, 2], 
["Fr", "francium", 1, 1], ["Ra", "radium", 1, 2], 
["Sc", "scandium", 1, 3], ["Y", "yttrium", 1, 3], 
["Ru", "ruthenium", 1, 3], ["Rh", "rhodium", 1, 2], 
["Ag", "silver", 1, 1], ["Cd", "cadmium", 1, 2], 
["Cd", "cadmium", 1, 2], ["In", "indium", 1, 3], 
["Zn", "zinc", 1, 2], ["Ga", "gallium", 1, 3],
["Al", "aluminum", 1, 3], ["Ge", "germanium", 1, 4],
["Ti", "titanium", 2, 3, 4], ["V", "vanadium", 2, 4, 5],
["Mn", "manganese", 5, 1, 2, 3, 4, 5], ["Fe", "iron", 2, 2, 3],
["Co", "cobalt", 2, 2, 3], ["Ni", "nickle", 3, 2, 3], 
["Cu", "copper", 2, 1, 2], ["Pd", "palladium", 2, 2, 4],
["Sn", "tin", 2, 2, 4], ["Sb", "antimony", 2, 3, 5],
["Pt", "platinum", 2, 2, 4], ["Au", "gold", 2, 1, 3],
["Hg", "mercury", 2, 1, 2], ["Tl", "thallium", 2, 1, 3], ["Pb", "lead", 2, 2, 4]]

anions = [["N", "nitride", 3], ["O", "oxide", 2], ["F", "fluoride", 1], 
["P", "phosphide", 3], ["S", "sulfide", 2], ["Cl", "chloride", 1], 
["As", "arsenide", 3], ["Se", "selenide", 2], ["Br", "bromide", 1],
["Te", "telluride", 2], ["I", "iodide", 1], ["As", "asstatide", 1]]

numeros = ["0", "I", "II", "III", "IV", "V", "VI", "VII"]

#-------------------------------------------------------------------------

print("Welcome to Logic's Nomenclature solver! If there is an error, please re-run the program and provide the correct input.")
query = input("Press 1 for formula to name and 2 for name to formula: ")

if(query == "1"):
    formula = input("Please enter the formula in the following format without special characters: Fe2O3 or MgS\n")
    
    element1 = formula[0]
    if(formula[1].isnumeric() == False):
        element1 += formula[1]
    #if(element1 not in cations):
    #    print("Please enter an ionic compound!")
    #    quit()
    for i in range(len(cations)):
        if(cations[i][0] == element1):
            idx1 = i; break
    name1 = cations[idx1][1]
    
    if(len(element1) == 1):
        if(formula[1].isnumeric()):
            subscript1 = formula[1]
            element2 = formula[2:]
        else:
            subscript1 = 1 
            element2 = formula[1:]
    else:
        if(formula[2].isnumeric()):
            subscript1 = formula[2]
            element2 = formula[3:]
        else:
            subscript1 = 1 
            element2 = formula[2:]
    if(element2[-1].isnumeric()):
        subscript2 = element2[-1]
        element2 = element2[:-1]
    else:
        subscript2 = 1
    #if(element2 not in anions):
    #    print("Please enter an ionic compound!")
    #    quit()
    for i in range(len(anions)):
        if(anions[i][0] == element2):
            idx2 = i; break
    name2 = anions[idx2][1]
    
    if(cations[idx1][2] == 1):
        print(name1, name2)
    else:
        charge = anions[idx2][2]*int(subscript2)/int(subscript1)
        exist = False
        for x in cations[idx1]:
            if(x == charge):
                exist = True
        if(exist == False):
            print("Impossible formula!")
        else:
            print(name1+"("+numeros[int(charge)]+") "+name2)
    
elif(query == "2"):
    name = input("Please enter the name in the following format without special characters: iron(III) oxide or magnesium sulfide\n")
    try:
        name1, name2 = name.split()
    except:
        print("Please provide a valid input.")
        quit()
    charge1 = ""
    if("(" in name1):
        idx = name1.index('(')
        for i in range(idx+1, name1.index(')')):
            charge1 += name1[i]
        name1 = (name1[:idx]).lower()
    name2 = name2.lower()
    
    for i in range(len(cations)):
        if(cations[i][1] == name1):
            idx1 = i; break
    element1 = cations[idx1][0]
    
    for i in range(len(anions)):
        if(anions[i][1] == name2):
            idx2 = i; break
    element2 = anions[idx2][0]
    
    if(charge1 == "" and cations[idx1][2] != 1):
        print("Please specify the charge of the metal.")
        quit()
    if(len(charge1)):
        charge1 = numeros.index(charge1.upper())
    else:
        charge1 = cations[idx1][3]
    charge2 = anions[idx2][2]
    if(charge1 % 2 == 0 and charge2 % 2 == 0):
        charge1 //= 2; charge2 //= 2;
    if(charge1 % 3 == 0 and charge2 % 3 == 0):
        charge1 //= 3; charge2 //= 3;
    if(charge1 == 1):
        charge1 = ""
    if(charge2 == 1):
        charge2 = ""
    print(element1+str(charge2)+element2+str(charge1))
    
else:
    print("Please enter 1 or 2.")

