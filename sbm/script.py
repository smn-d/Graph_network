import graph_tool.all as gt
from sbm import sbm



folder = "data/"


def runModel(outputFolder,patient_num,multi,deg_corr,age,gender,ethnicity):
    model = sbm()
    model.make_graph(patient_num, age,gender,ethnicity)
    experimentName = outputFolder + str(patient_num)
    if(multi):
        experimentName += "multi"
    else:
        experimentName += "nested"
    if(deg_corr):
        experimentName += "Deg_corr"
    if(age):
        experimentName += "A"
    if(gender):
        experimentName += "G"
    if(ethnicity):
        experimentName += "E"
    model.setOuputLoc(experimentName)
    model.save_graph()
    model.fit(multi,deg_corr)
    print("experiment "+ experimentName+ " done")

runModel(folder,56115,True,True,True,True,True)
runModel(folder,56115,True,False,True,True,True)
# runModel(folder,56115,False,False,True,True,True)
# runModel(folder,10,False,True,True,True,True)


# model = sbm()
# # patient_num = 115
# patient_num = 56115
# # patient_num = 100
# model.make_graph(patient_num=patient_num, age=True,gender=True,ethnicity=True)

# experimentName = folder + str(patient_num)+"nested_noDegCorr_Dem" 
# experimentName += "NoEq"

# model.setOuputLoc(experimentName)
# model.save_graph()

# model.fit(multilayer=False,deg_corr=False)
# print("experiment "+ experimentName+ " done")

# model = sbm()
# # patient_num = 100
# patient_num = 56115
# # patient_num = 10000
# model.make_graph(patient_num=patient_num, age=True,gender=True,ethnicity=True)

# experimentName = folder + str(patient_num)+"nested_DegCorr_Dem" 
# experimentName += "NoEq"

# model.setOuputLoc(experimentName)
# model.save_graph()

# model.fit(multilayer=False,deg_corr=True)
# print("experiment "+ experimentName+ " done")



# model = sbm()
# # patient_num = 115
# patient_num = 56115
# # patient_num = 10000
# model.make_graph(patient_num=patient_num, age=True,gender=True,ethnicity=True)

# experimentName = folder + str(patient_num)+"multi_noDegCorr_Dem" 
# experimentName += "NoEq"

# model.setOuputLoc(experimentName)
# model.save_graph()

# model.fit(multilayer=True,deg_corr=False)
# print("experiment "+ experimentName+ " done")

# model = sbm()
# # patient_num = 115
# patient_num = 56115
# # patient_num = 10000

# model.make_graph(patient_num=patient_num, age=True,gender=True,ethnicity=True)

# experimentName = folder + str(patient_num)+"mult_DegCorr_Dem" 
# experimentName += "noEq"

# model.setOuputLoc(experimentName)
# model.save_graph()

# model.fit(multilayer=True,deg_corr=True)
# print("experiment "+ experimentName+ " done")
