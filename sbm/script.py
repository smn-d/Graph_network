import graph_tool.all as gt
from sbm import sbm

experimentName = "test"


model = sbm()
# patient_num = 115
# patient_num = 56115
patient_num = 10000
model.make_graph(patient_num=patient_num, age=False,gender=False,ethnicity=False)
experimentName = str(patient_num)+"nested_noDegCorr_noDem" 
# experimentName += "NoEq"
model.setOuputLoc(experimentName)
model.fit(multilayer=False,deg_corr=False)
print("experiment "+ experimentName+ " done")

model = sbm()
# patient_num = 115
# patient_num = 56115
patient_num = 10000
model.make_graph(patient_num=patient_num, age=False,gender=False,ethnicity=False)
experimentName = str(patient_num)+"nested_DegCorr_noDem" 
# experimentName += "NoEq"
model.setOuputLoc(experimentName)
model.fit(multilayer=False,deg_corr=True)
print("experiment "+ experimentName+ " done")

model = sbm()
# patient_num = 115
# patient_num = 56115
patient_num = 10000
model.make_graph(patient_num=patient_num, age=True,gender=True,ethnicity=True)
experimentName = str(patient_num)+"nested_DegCorr_Dem" 
# experimentName += "NoEq"

model.setOuputLoc(experimentName)
model.fit(multilayer=False,deg_corr=True)
print("experiment "+ experimentName+ " done")

model = sbm()
# patient_num = 115
# patient_num = 56115
patient_num = 10000
model.make_graph(patient_num=patient_num, age=True,gender=True,ethnicity=True)
experimentName = str(patient_num)+"multi_noDegCorr_Dem" 
# experimentName += "NoEq"

model.setOuputLoc(experimentName)
model.fit(multilayer=True,deg_corr=False)
print("experiment "+ experimentName+ " done")

model = sbm()
# patient_num = 115
# patient_num = 56115
patient_num = 10000

model.make_graph(patient_num=patient_num, age=True,gender=True,ethnicity=True)
experimentName = str(patient_num)+"mult_DegCorr_Dem" 
# experimentName += "NoEq"

model.setOuputLoc(experimentName)
model.fit(multilayer=True,deg_corr=True)
print("experiment "+ experimentName+ " done")
