class Recipe:
    tricks = []             # mistaken use of a class variable

    def __init__(self, name, ingredientList, description):
        self.name = name
        self.ingredientList = ingredientList 
        self.description = description

    def selfPrint(self):
        print(self.name)
        print(self.ingredientList)
        print(self.description)

realName = "Tomatensuppe"
realList = ["z1","z2"]
realDescription = "descriptionTomatensuppe"

realName2 = "Hamburger"
realList2 = ["z3","z4"]
realDescription2 = "descriptionHamburger"

myRecipe = Recipe(realName, realList, realDescription)
myRecipe2 = Recipe(realName2, realList2, realDescription2)

myRecipe.selfPrint()
myRecipe2.selfPrint()