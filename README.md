Group 14

# A3 OpenBIM Change

## A3 Goal and Scope

The goal of the tool is to be able to add materials and layers to wall types in an
IFC4 file. The scope of this tool is that the tool only relates to walls and is
limited to the thickness given beforehand. It is also limited in regard to the
materiels you add, ideally we would like to make a material catalog with
respective EPD data the user would be able to choose the materials from.

## A3A BIM Execution plan - BEP

##### Model use

The use of the model is to assign materials and layerthicknesses to a simple model – which is especially important in the early stages of an LCA when wanting to have an indicator of how the CO2 emissions of the building will/ can look like.

##### Process

The process is to be able to connect specific materials and thicknesses to a simple
model where the materials are not modeled yet. This could be very relevant in
early stages where the architects might only have the rough dimensions. Then
we, as a LCA specialist, will need to make some assumptions to be able to
indicate the CO2 emissions of the building. This feature is therefore relevant
in the early stages where we get a rough BIM model. This step is important for
the sustainability agenda, because it is in the early stages we can make the
biggest impact on lowering the environmental impacts of the building.

##### Information exchange

The information exchange happens between the LCA-specialt and all the different
engineering parties. Here the LCA specialist will require the BIM models of the
architects, the construction model, the VVS model ect.

There will also be an information exchange between the LCA specialist and the appointing party. They are the ones in charge of the sustainability goals and the budget and the one who can take decisions to e.g. choose a different product of insulation to lower the CO2 emissions. They are also the ones who set the goal
and can ‘approve’.

## A3B Remodel

For the remodel assignment the skylab IFC 4 has been used. We noticed that it didn’t contain any material layers and thereby no layer thickness. This information is crucial when making a LCA and that is why we chose to make a tool where the user can add that to an IFC file. To make it user friendly and to make the tool work for all IFC files, the first step in the code is to create a list with all different wall types. This is then used to make an excel sheet, where the user can add materials and thicknesses. Next step is for the user to save the file and write DONE, and then the tool will add all the information provided by the user to the IFC file. Lastly, the tool makes sure to save the now remodeled IFC file under a new name. The workflow, the tool provides, is marked with a green color in the BPMN-diagram for the workflow after the tool.

What we would like to work on as the next step is to include a material database, so
that the user can choose a material from a database included in the excel sheet the code creates. The database should then have different specific materials that has an EPD. It should also include the ‘industry EPD’s’ that relates to the average environmental effect of e.g. concreate used in Denmark, which often is used in the early stages before decisions are made. When this is done the user could directly connect all the EPD data of a given material to the IFC file.

![BPMN -before tool](https://github.com/s203726/test/assets/145358059/c0a11b25-463d-4568-9c81-ad1102f26ff5)
![BPMN - after tool](https://github.com/s203726/test/assets/145358059/24b81628-e096-4db3-a729-de418fd247bf)



## 3D Value what is the potential improvement offered by this tool?

The business value in this tool is to quickly implement materials and their thicknesses to all walls of same type. The tool also helps to extract the total area of each wall type ( from A2). These quantities is what you need from the IFC to create an LCA. When the next step is implementet and it is possible only to choose among materials that has an EPD attached, it would be possible to extract even more information about the environmental impact right away.

The social value of this tool is that it encourages to implement LCA calculations in early
stages – and it is shown that the impact of LCA consulting is greater in the earlier stages because you then can consult the client to make changes e.g. in regards to material choices based on different variant studies. This shoudl all result in lower environmeltal impact from new construction in the build industry.
