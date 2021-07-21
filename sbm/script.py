import graph_tool.all as gt
from sbm import sbm

experimentName = "patientIcd100"

model = sbm()

# graph_title = "multi1000PatientDiseases.gt.gz"
admin_num = 100
model.make_graph(admin_num=admin_num, age=False,ethnicity=False)

model.save_graph(filename=experimentName+".gt.gz")

model.fit()
print(model.mdl)

gt.draw_hierarchy(model.state, subsample_edges=1000, layout = "bipartite",output=experimentName+"Hierarchy.pdf")