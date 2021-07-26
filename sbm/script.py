import graph_tool.all as gt
from sbm import sbm

experimentName = "test"

model = sbm()
patient_num = 115
# patient_num = 56115
model.make_graph(patient_num=patient_num, age=False,gender=False,ethnicity=False)
experimentName = "56115nested_noDegCorr_noDem" 
model.setOuputLoc(experimentName)
model.fit(multilayer=False,deg_corr=False)

model = sbm()
patient_num = 115
# patient_num = 56115
model.make_graph(patient_num=patient_num, age=False,gender=False,ethnicity=False)
experimentName = "56115nested_DegCorr_noDem" 
model.setOuputLoc(experimentName)
model.fit(multilayer=False,deg_corr=True)

model = sbm()
patient_num = 115
# patient_num = 56115
model.make_graph(patient_num=patient_num, age=True,gender=True,ethnicity=True)
experimentName = "56115nested_DegCorr_Dem" 
model.setOuputLoc(experimentName)
model.fit(multilayer=False,deg_corr=True)

model = sbm()
patient_num = 115
# patient_num = 56115
model.make_graph(patient_num=patient_num, age=True,gender=True,ethnicity=True)
experimentName = "56115multi_noDegCorr_Dem" 
model.setOuputLoc(experimentName)
model.fit(multilayer=True,deg_corr=False)

model = sbm()
patient_num = 115
# patient_num = 56115
model.make_graph(patient_num=patient_num, age=True,gender=True,ethnicity=True)
experimentName = "56115mult_DegCorr_Dem" 
model.setOuputLoc(experimentName)
model.fit(multilayer=True,deg_corr=True)