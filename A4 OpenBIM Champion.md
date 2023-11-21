A4 OpenBim Champion

## Identification of the target audience

We are targeting R1, the modeler, and R2, the analyst. When targeting these groups we need to think of the least we can expect from each group and the knowledge they have.  

For the modeller the lowest level includes being able to model in BlenderBIM focusing on the mapping structure and to export to an IFC.  

For the lowest level of the analyst role, you can analyze an IFC file in excel, which was what our peers did in assignment A1. 

To sum up we conclude that our target role doesn’t have any knowledge about python and programming using IfcOpenshell, which is why we have tried to make our script understandable and user friendly.

## Goal and scope

The goal of the tool is to be able to add materials and layers to wall types in an IFC4 file. The scope of this tool is that the tool only relates to walls and is limited to the thickness given beforehand. It is also limited regarding the materials you add, ideally, we would like to make a material catalog with respective EPD data the user would be able to choose the materials from.

## BIM use

#### Introduction 

The use of the model is to assign materials and layer thicknesses to a simple model – which is especially important in the early stages of an LCA when wanting to have an indicator of how the CO2 emissions of the building will/can look like. It involves user input through an Excel file to define material properties for each wall type, streamlining the process of updating the IFC file. The script is designed to simplify the task of updating early stage IFC files. It targets wall types and utilizes an Excel file for user input, allowing for the specification of material properties for the different walltypes (names and thicknesses).

#### Step-by-step instructions 

1. Loading the IFC File:

The script uses the `ifcopenshell` library to open an IFC file specified by the user.

2. Creating a List of Wall Type Names:

Wall types are extracted from the IFC file, and their names are stored in a list.

3. Setting Up Excel File for User Input:

An Excel file is generated with columns for wall names, material names, and thicknesses using the Pandas library.

4. Prompting User Interaction:

The user is informed about the creation of the Excel file and prompted to fill in the material information.

5. User Confirmation:

The script waits for the user to confirm completion by typing 'DONE' after modifying and saving the Excel file.

6. Reading User-Inputted Data:

If confirmed, the script reads the modified Excel file and organizes the data for further processing.

7. Modifying IFC File Based on User Input:

Wall types in the IFC file are iterated, and materials with corresponding thicknesses are added based on user-inputted data.

8. Verifying Modifications:

A function is included to print out the materials and thicknesses of wall types for user verification.

9. Writing Modified Data to a New IFC File:

The modified data is written to a new IFC file, leaving the original file unchanged.
