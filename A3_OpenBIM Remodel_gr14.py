import ifcopenshell
import ifcopenshell.api
import ifcopenshell.util
import ifcopenshell.util.element
import pandas as pd
import openpyxl

#Loads the file (REMEMBER TO CHANGE THE PATH TO MAKE THE SCRIPT WORK)
model = ifcopenshell.open(r'C:/Users/Bruger/OneDrive/Dokumenter/Advanced Building Information Modelling/Skylab4_medQuantities.ifc')

WallNameList = []
walltypes = model.by_type('IfcWallType')

#Creates list with all walltypenames
for walltype in walltypes:
    WallNameList.append(walltype.Name)

#Defines excelpath and columnnames (REMEMBER TO CHANGE THE PATH TO MAKE THE SCRIPT WORK)
ExcelPath = r"C:/Users/Bruger/OneDrive/Dokumenter/Advanced Building Information Modelling/Excel_Input.xlsx"
ColumnNames= ["Wall_Name", "Material_1", "Thickness_1 [mm]","Material_2", "Thickness_2 [mm]","Material_3","Thickness_3 [mm]","Material_4","Thickness_4 [mm]","Material_5","Thickness_5 [mm]"]

#Writes to excelfile and creates table with walltype names and empty materials and thicknesses
Excel_Input = pd.DataFrame({"Wall_Name": WallNameList},columns=ColumnNames)
#Creates a new excel-file located at the specified filepath
Excel_Input.to_excel(ExcelPath, index=False)

#Informs user that an excel-file has been created in the filepath
print("An excel-file has now been created and you can now start to fill in information about the walltypes materials and thicknesses.")

#Makes sure user has modified excel, saved it and closed it
Check = input("\nTo continue, you must fill in the information in the excelfile, save it, close it and write 'DONE': ")

# Can only continue if user writes 'DONE'
if Check == "DONE":

    print("\nYour walltypes in the IFC-file have now been modified to match the information in the excel!")

    #To test if it works, you can remove comment and use the attached testfile with allready added data
    #ExcelPath = r"C:/Users/Bruger/OneDrive/Dokumenter/Advanced Building Information Modelling/Excel_Input_with_Input.xlsx"

    # Reads excel file and removes "nan" elements
    Excel_Output = pd.read_excel(ExcelPath)
    Excel_Output = Excel_Output.stack()

    #Creates empty list to put in the name of the walltypes and its corresponding materials and thickness from modifyed excel-file
    WallTypeMaterials = []

    #Loop that adds materialsets to the walltypes from the modified excel-file
    for i in range(len(WallNameList)):
        WallTypeMaterials.append(Excel_Output.loc[i].tolist())
        
        #If there is one material added to the walltype
        if len(WallTypeMaterials[i]) == 3:
            #Finds wallname
            Wall_Name = str(WallTypeMaterials[i][0])
            #Finds materialname
            Material_1 = str(WallTypeMaterials[i][1])
            #Finds materialthickness
            Thickness_1 = int(WallTypeMaterials[i][2])
            #Makes materialset from wallname
            material_set = ifcopenshell.api.run("material.add_material_set", model, name=Wall_Name, set_type="IfcMaterialLayerSet")
            #Makes a new material
            material = ifcopenshell.api.run("material.add_material", model, name=Material_1, category=Material_1)
            #Adds layer with material to materialset
            layer = ifcopenshell.api.run("material.add_layer", model, layer_set=material_set, material=material)
            #Edits the layerthickness of material
            ifcopenshell.api.run("material.edit_layer", model, layer=layer, attributes={"LayerThickness": Thickness_1})
            #Assigns materialset to walltype
            ifcopenshell.api.run("material.assign_material", model, product=walltypes[i], material=material_set)
        
        #If there are two material added to the walltype
        elif len(WallTypeMaterials[i]) == 5:
            Wall_Name = str(WallTypeMaterials[i][0])
            Material_1 = str(WallTypeMaterials[i][1])
            Thickness_1 = int(WallTypeMaterials[i][2])
            Material_2 = str(WallTypeMaterials[i][3])
            Thickness_2 = int(WallTypeMaterials[i][4])
            
            material_set = ifcopenshell.api.run("material.add_material_set", model, name=Wall_Name, set_type="IfcMaterialLayerSet")
            
            material1 = ifcopenshell.api.run("material.add_material", model, name=Material_1, category=Material_1)
            material2 = ifcopenshell.api.run("material.add_material", model, name=Material_2, category=Material_2)
            
            layer = ifcopenshell.api.run("material.add_layer", model, layer_set=material_set, material=material1)
            ifcopenshell.api.run("material.edit_layer", model, layer=layer, attributes={"LayerThickness": Thickness_1})
            layer = ifcopenshell.api.run("material.add_layer", model, layer_set=material_set, material=material2)
            ifcopenshell.api.run("material.edit_layer", model, layer=layer, attributes={"LayerThickness": Thickness_2})

            ifcopenshell.api.run("material.assign_material", model, product=walltypes[i], material=material_set)

        #If there are three material added to the walltype    
        elif len(WallTypeMaterials[i]) == 7:
            Wall_Name = str(WallTypeMaterials[i][0])
            Material_1 = str(WallTypeMaterials[i][1])
            Thickness_1 = int(WallTypeMaterials[i][2])
            Material_2 = str(WallTypeMaterials[i][3])
            Thickness_2 = int(WallTypeMaterials[i][4])
            Material_3 = str(WallTypeMaterials[i][5])
            Thickness_3 = int(WallTypeMaterials[i][6])
            
            material_set = ifcopenshell.api.run("material.add_material_set", model, name=Wall_Name, set_type="IfcMaterialLayerSet")
            
            material1 = ifcopenshell.api.run("material.add_material", model, name=Material_1, category=Material_1)
            material2 = ifcopenshell.api.run("material.add_material", model, name=Material_2, category=Material_2)
            material3 = ifcopenshell.api.run("material.add_material", model, name=Material_3, category=Material_3)
            
            layer = ifcopenshell.api.run("material.add_layer", model, layer_set=material_set, material=material1)
            ifcopenshell.api.run("material.edit_layer", model, layer=layer, attributes={"LayerThickness": Thickness_1})
            layer = ifcopenshell.api.run("material.add_layer", model, layer_set=material_set, material=material2)
            ifcopenshell.api.run("material.edit_layer", model, layer=layer, attributes={"LayerThickness": Thickness_2})
            layer = ifcopenshell.api.run("material.add_layer", model, layer_set=material_set, material=material3)
            ifcopenshell.api.run("material.edit_layer", model, layer=layer, attributes={"LayerThickness": Thickness_3})
            
            ifcopenshell.api.run("material.assign_material", model, product=walltypes[i], material=material_set)
        
    #Function from A2 that finds materials and thicknesses of elements
    def MaterialThickness(elements):
        
        for elm in elements:
            material_name = []
            material_thickness = []
            
            if elm.HasAssociations:
                for i in elm.HasAssociations:
                    if i.is_a('IfcRelAssociatesMaterial'):
            
                        if i.RelatingMaterial.is_a('IfcMaterial'):
                            material_name.append(i.RelatingMaterial.Name)
            
                        elif i.RelatingMaterial.is_a('IfcMaterialList'):
                            for materials in i.RelatingMaterial.Materials:
                                material_name.append(materials.Name)
            
                        elif i.RelatingMaterial.is_a('IfcMaterialLayerSetUsage'):
                            for materials in i.RelatingMaterial.ForLayerSet.MaterialLayers:
                                material_name.append(materials.Material.Name)
                                material_thickness.append(materials.LayerThickness)
                                
                        if i.RelatingMaterial.is_a('IfcMaterialLayerSet'):
                            for materials in i.RelatingMaterial.MaterialLayers:
                                material_name.append(materials.Material.Name)
                                material_thickness.append(materials.LayerThickness)
            
            print(f"\nMaterials and LayerThickness of {elm.Name}:")
            
            if len(material_name) == 0 and len(material_thickness) == 0:
                print("Element has no materials or thickness.")
                
            elif len(material_name) >= 0 and len(material_thickness) == 0:
                for i in range(len(material_name)):
                    print(material_name[i])
                
            else:
                for i in range(len(material_name)):
                    print(f"{material_name[i]}: {material_thickness[i]} mm")
            
        return

    #Tests if materials and thicknesses was added successfully
    MaterialThickness(walltypes)
    
    #Creates new ifc-file with modified data (REMEMBER TO CHANGE THE PATH TO MAKE THE SCRIPT WORK)
    model.write(r'C:/Users/Bruger/OneDrive/Dokumenter/Advanced Building Information Modelling/Skylab4_medQuantities_modified.ifc')