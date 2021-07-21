import graph_tool.all as gt
import matplotlib.pyplot as plt
import numpy as np
import sys
import os
import logging
import pathlib
from datetime import datetime
from scipy.special import gammaln



def main():

    now = datetime.now()
    date_time = now.strftime("%H_%M")

    graph_name = "karate"

    expName = graph_name + date_time

    g = getGraph(graph_name)


    # logging.basicConfig(filename=expName+".log",level=logging.INFO)

    
    # logging.info(isinstance(g,gt.Graph))

    state = gt.minimize_blockmodel_dl(g)

    dS, nattempts, nmoves = state.multiflip_mcmc_sweep(niter=1000)

    print("Change in description length:", dS)
    # print("Number of accepted vertex moves:", nmoves)
    print(state.entropy())


    # collecting partitions


    bs = []
    dls = []

    def collect_partitions(s):
        bs.append(s.get_state().a.copy())

        dls.append(s.entropy())

    # We will collect only partitions 1000 partitions. For more accurate
    # results, this number should be increased.
    gt.mcmc_equilibrate(state, force_niter=1000, mcmc_args=dict(niter=10),
                        callback=collect_partitions)


    # Marginals 


    pmode = gt.PartitionModeState(bs, converge=True)
    pv = pmode.get_marginal(g)

    # Now the node marginals are stored in property map pv. We can
    # visualize them as pie charts on the nodes:
    state.draw(pos=g.vp.pos, vertex_shape="pie", vertex_pie_fractions=pv,
            output=expName+"-sbm-marginals.svg")

    # Partition modes 

    # Infer partition modes
    pmode = gt.ModeClusterState(bs, nested=False)

    # Minimize the mode state itself
    gt.mcmc_equilibrate(pmode, wait=1, mcmc_args=dict(niter=1, beta=np.inf))

    # Get inferred modes
    modes = pmode.get_modes()

    for i, mode in enumerate(modes):
        b = mode.get_max_nested()
        pv = mode.get_marginal(g)

        print(f"Mode {i} with size {mode.get_M()/len(bs)}")
        state = state.copy(bs=b)
        # state.draw(vertex_shape="pie", vertex_pie_fractions=pv,
        #         output=expName+"-partition-mode-%i.svg" % i)

    #Log evidence calculation
    
    # Posterior entropy
    H = pmode.posterior_entropy()

    # log(B!) term
    logB = np.mean(gammaln(np.array([len(np.unique(b)) for b in bs]) + 1))

    # Evidence
    L = -np.mean(dls) + logB + H

    print(f"Model log-evidence = {L}")





def getGraph(name):
    graph_name = name

    try:
        g = gt.collection.data[graph_name]
    except:
        print("Graph not found")
        raise

    return g

# def createResultFolder(expName):

#     if not os.path.exists(expName):
#         os.mkdir(expName)
#         print("Directory " , expName ,  " Created ")
#     else:    
#         print("Directory " , expName ,  " already exists")

#     return os.path.abspath(os.getcwd()+'/'+expName)


if __name__ == "__main__":
    main()
