import graph_tool.all as gt
import numpy as np

g = gt.collection.data["lesmis"]

# clabel = g.vp['kind']

# state_args = {'clabel': clabel, 'pclabel': clabel}
# if "count" in g.ep:
#     state_args["eweight"] = g.ep.count

## the inference
mdl = np.inf ##

base_type = gt.BlockState
state_tmp = gt.minimize_nested_blockmodel_dl(g,
                                                             state_args=dict(
                                                                 base_type=base_type))
L = 0
for s in state_tmp.levels:
    L += 1
    if s.get_nonempty_B() == 2:
        break
state_tmp = state_tmp.copy(bs=state_tmp.get_bs()[:L] + [np.zeros(1)])
                # state_tmp = state_tmp.copy(sampling=True)
                # delta = 1 + epsilon
                # while abs(delta) > epsilon:
                #     delta = state_tmp.multiflip_mcmc_sweep(niter=10, beta=np.inf)[0]
                #     print(delta)
print(state_tmp)

mdl_tmp = state_tmp.entropy()
print(mdl_tmp)
if mdl_tmp < mdl:
    mdl = 1.0*mdl_tmp
    state = state_tmp.copy()
state.draw(subsample_edges=1000, hshortcuts=1, hide=0)