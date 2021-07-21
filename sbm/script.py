import graph_tool.all as gt
from sbm import sbm

experimentName = "patientIcd1000"

model = sbm()

# graph_title = "multi1000PatientDiseases.gt.gz"
admin_num = 1000
model.make_graph(admin_num=admin_num, age=True,ethnicity=True)

model.save_graph(filename=experimentName+".gt.gz")

model.fit(multilayer=False)
print(model.mdl)

# gt.draw_hierarchy(model.state, subsample_edges=1000, layout = "bipartite",output=experimentName+"Hierarchy.pdf")
gt.draw_hierarchy(model.state, subsample_edges=1000,output=experimentName+"Hierarchy.pdf")