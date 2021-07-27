import csv
import graph_tool.all as gt
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as mticker
import os
import scipy.special as sc



class sbm():

    def __init__(self):
        self.g = None ## network
        self.output = None

        self.patients = [] ## list of  patients
        self.icd9 = [] ## list of disease icd9 codes

        self.state = None ## inference state from graphtool
        self.groups = {} ## results of group membership from inference
        self.mdl = np.nan ## minimum description length of inferred state
        self.L = np.nan ## number of levels in hierarchy

    def setOuputLoc(self,experimentName="exp"):
        if not os.path.exists(experimentName):
            os.makedirs(experimentName)
        self.output = experimentName+"/"

    def make_graph(self,patient_num = 0, gender=False, ethnicity=False, age=False):
        '''
        optional argument:
        - patient_num: only consider the given number of patients
        '''


        ## make a graph
        ## create a graph
        g = gt.Graph(directed=False)
        ## define node properties
        ## name: docs - title, words - 'word'
        ## kind: docs - 0, words - 1
        name = g.vp["name"] = g.new_vp("string")
        kind = g.vp["kind"] = g.new_vp("int")

        if(gender or ethnicity or age):
            weight = g.ep["weight"] = g.new_ep("int")
        if(gender):
            m = g.add_vertex()
            f = g.add_vertex()
            name[m] = "M"
            kind[m] = 2
            name[f] = "F"
            kind[f] = 2
        if(ethnicity):
            # ethnicities = ['hispanic', 'white', 'black', 'asian', 'native', 'unknown', 'other']
            h = g.add_vertex()
            name[h] = "hispanic"
            kind[h] = 3
            w = g.add_vertex()
            name[w] = "white"
            kind[w] = 3
            b = g.add_vertex()
            name[b] = "black"
            kind[b] = 3
            a = g.add_vertex()
            name[a] = "asian"
            kind[a] = 3
            n = g.add_vertex()
            name[n] = "native"
            kind[n] = 3
            u = g.add_vertex()
            name[u] = "unknown"
            kind[u] = 3
            o = g.add_vertex()
            name[o] = "other"
            kind[o] = 3

        if(age):
            a1 = g.add_vertex()
            name[a1] = "0-19"
            kind[a1] = 4
            a2 = g.add_vertex()
            name[a2] = "20-39"
            kind[a2] = 4
            a3 = g.add_vertex()
            name[a3] = "40-59"
            kind[a3] = 4
            a4 = g.add_vertex()
            name[a4] = "60-79"
            kind[a4] = 4
            a5 = g.add_vertex()
            name[a5] = "80+"
            kind[a5] = 4
 


    


        subject_add = defaultdict(lambda: g.add_vertex())
        icd9_add = defaultdict(lambda: g.add_vertex())

        with open('admission_patients_demograhics_morbidities.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            count = 0
            for row in csv_reader:

                # p = admin_add[row['hadm_id']]
                p = subject_add[row['subject_id']]
                
                name[p] = row['hadm_id']
                kind[p] = 0

                icdList = row['icd9_4_digits'].split(',')
                for icd9 in icdList:
                    d=icd9_add[icd9]
                    name[d] = icd9
                    kind[d] = 1
                    e = g.add_edge(p,d)
                    if(gender or ethnicity or age):
                        g.ep.weight[e]=0

                if(gender):
                    
                    if(row['gender']=="M"):
                        e = g.add_edge(p,m)
                        g.ep.weight[e]=-1
                    else:
                        e = g.add_edge(p,f)
                        g.ep.weight[e]=-1

                if(ethnicity):

                    if(row['ethnicity_grouped']=="hispanic"):
                        e = g.add_edge(p,h)
                        g.ep.weight[e]=1
                    elif(row['ethnicity_grouped']=="white"):
                        e = g.add_edge(p,w)
                        g.ep.weight[e]=1
                    elif(row['ethnicity_grouped']=="black"):
                        e = g.add_edge(p,b)
                        g.ep.weight[e]=1
                    elif(row['ethnicity_grouped']=="asian"):
                        e = g.add_edge(p,a)
                        g.ep.weight[e]=1
                    elif(row['ethnicity_grouped']=="native"):
                        e = g.add_edge(p,n)
                        g.ep.weight[e]=1
                    elif(row['ethnicity_grouped']=="unknown"):
                        e = g.add_edge(p,u)
                        g.ep.weight[e]=1
                    elif(row['ethnicity_grouped']=="other"):
                        e = g.add_edge(p,o)
                        g.ep.weight[e]=1

                if(age):
                    if(0<=int(row['age'])<=19):
                        e = g.add_edge(p,a1)
                        g.ep.weight[e]=2
                    elif(20<=int(row['age'])<=39):
                        e = g.add_edge(p,a2)
                        g.ep.weight[e]=2
                    elif(40<=int(row['age'])<=59):
                        e = g.add_edge(p,a3)
                        g.ep.weight[e]=2
                    elif(60<=int(row['age'])<=79):
                        e = g.add_edge(p,a4)
                        g.ep.weight[e]=2
                    elif(80<=int(row['age'])):
                        e = g.add_edge(p,a5)
                        g.ep.weight[e]=2
                    
                        


                count+=1
                if(count==patient_num):
                    break

        # g.save(graph_title+'.gt.gz')

        self.g = g
        self.icd9 = [g.vp['name'][v] for v in g.vertices() if g.vp['kind'][v] == 1]
        self.patients = [g.vp['name'][v] for v in g.vertices() if g.vp['kind'][v] == 0]

        return self

    def save_graph(self):
        '''
        Save the word-document network generated by make_graph() as filename.
        Allows for loading the graph without calling make_graph().
        '''

        self.g.save(self.output+"graph.gt.gz")

    def load_graph(self,experimentName = None):
        '''
        Load a word-document network generated by make_graph() and saved with save_graph().
        '''
        self.g = gt.load_graph(experimentName+"/graph.gt.gz")
        self.icd9 = [ self.g.vp['name'][v] for v in  self.g.vertices() if self.g.vp['kind'][v]==1   ]
        self.admissions = [ self.g.vp['name'][v] for v in  self.g.vertices() if self.g.vp['kind'][v]==0   ]


    def fit(self,multilayer=False,deg_corr=True):
            '''
            Fit the sbm to the patient-icd9-demographic network.
            '''


            g = self.g
            if g is None:
                print('No data to fit the SBM. Load some data first (make_graph)')
            else:

                with open(self.output+"info.txt", "a") as f:
                    f.truncate(0)

                #cluster different kind of nodes together
                clabel = g.vp['kind']

                state_args = {}

                # state_args = {'clabel': clabel, 'pclabel': clabel}
                state_args["clabel"] = clabel
                state_args["pclabel"] = clabel

                if not(deg_corr):
                    state_args["deg_corr"] = False

                if(multilayer):
                    state_args["ec"] = g.ep.weight
                    state_args["layers"] = True
                    # state_args["clabel"] = clabel
                    # state_args["pclabel"] = clabel
                    state = gt.minimize_nested_blockmodel_dl(g,state_args=dict(base_type=gt.LayeredBlockState,**state_args))
                    # state = gt.minimize_nested_blockmodel_dl(g,state_args=dict(base_type=gt.LayeredBlockState))

                else:
                    # base_type = gt.BlockState
                    state = gt.minimize_nested_blockmodel_dl(g,state_args=dict(base_type=gt.BlockState,**state_args))
                    # state = gt.minimize_nested_blockmodel_dl(g,state_args=dict(base_type=gt.BlockState))


                print("model minimized")

                L = 0
                for s in state.levels:
                    L += 1
                    if s.get_nonempty_B() == 2:
                        break
                state = state.copy(bs=state.get_bs()[:L] + [np.zeros(1)])

                b = state.get_bs()[0]

                nKind = {}
                for bNum in np.unique(b):
                    nKind[bNum]=set()

                for v,group in enumerate(b):
                    nKind[group].add(self.g.vp.kind[v])

                self.state = state

                gt.draw_hierarchy(state, subsample_edges=1000,output=self.output+"noSwapHierarchy.pdf")
                self.plotEdgeMatrix()

                with open(self.output+"info.txt", "a") as f:

                    print("no swap: ", file=f)
                    print(nKind,file=f)
                    print("entropy: ",state.entropy(),file=f)
                    print(state, file=f)




                # if(multilayer):
                #     state = state.copy(state_args=dict(clabel=None,pclabel=None,ec=g.ep.weight,layers=True))
                # else:
                #     state = state.copy(state_args=dict(clabel=None,pclabel=None))


                # hist = gt.mcmc_equilibrate(state, wait=100,mcmc_args=dict(niter=10),history=True)
                # print("equilibration done")





                



                self.state = state

                ## minimum description length
                self.mdl = state.entropy()


                # gt.draw_hierarchy(self.state, subsample_edges=1000,output=self.output+"Hierarchy.pdf")
                

                # if(multilayer):
                #     self.state.draw(edge_color=g.ep.weight, edge_gradient=[],
                #             ecmap=(plt.cm.coolwarm_r, .6), edge_pen_width=5,
                #             output=self.output+"edge-layer.pdf")
                # self.plotEntropyEvolution(hist)
                self.plotEdgeMatrix()
                # self.modelSelection()
                # self.plotGroupNum()

                for l in range(0,L):
                    if not os.path.exists(self.output+"groups"):
                        os.makedirs(self.output+"groups")
                    np.savetxt(self.output+"groups/level"+str(l)+".csv",self.state.get_bs()[l])


                # nKind = {}
                # for bNum in np.unique(b):
                #     nKind[bNum]=set()

                # for v,group in enumerate(b):
                #     nKind[group].add(self.g.vp.kind[v])




                # with open(self.output+"info.txt", "a") as f:
            
                #     print("final model entropy: ",self.mdl, file=f)
                #     print(nKind,file=f)

                #     print(self.state, file=f)
                
                    # print(self.state.get_bs()[0].tolist(),file=f)


      

                

    def plotEdgeMatrix(self):
        state = self.state.get_levels()[0]
        b = gt.contiguous_map(state.get_blocks())
        state = state.copy(b=b)

        e = state.get_matrix()

        B = state.get_nonempty_B()
        plt.matshow(e.todense()[:B, :B])
        plt.savefig(self.output+"matrix-edge-counts.pdf")

        plt.show()



    def plotEntropyEvolution(self,hist):

        width = .35 # width of a bar

        nattempts = [tup[0] for tup in hist]
        nmoves = [tup[1] for tup in hist]
        entropy = [tup[2] for tup in hist]

        m1_t = pd.DataFrame({
        'entropy' : entropy,
        'attemps' : nattempts,
        'moves' :  nmoves})

        m1_t[['attemps','moves']].plot(kind='bar', width = width)
        m1_t['entropy'].plot(secondary_y=True,label="entropy",color='red')
        plt.legend(loc='upper left')



        ax = plt.gca()


        myLocator = mticker.MultipleLocator(1000)
        ax.xaxis.set_major_locator(myLocator)

        # plt.xlim([-width, len(m1_t['attemps'])-width])
        # ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10'))
        plt.savefig(self.output+'entropyHistory.pdf')
        plt.show()

    def modelSelection(self):
        # collect nested partitions
        bs = []
        dls = [] 

        def collect_partitions(s):
            bs.append(s.get_bs())
            dls.append(s.entropy())

        # Now we collect the marginals for exactly 1,000 sweeps
        gt.mcmc_equilibrate(self.state, force_niter=100, mcmc_args=dict(niter=10),
                            callback=collect_partitions)

        # Disambiguate partitions and obtain marginals
        pmode = gt.PartitionModeState(bs, nested=True, converge=True)
        pv = pmode.get_marginal(self.g)

        # Get consensus estimate
        bs = pmode.get_max_nested()

        state = self.state.copy(bs=bs)

        # We can visualize the marginals as pie charts on the nodes:
        # state.draw(vertex_shape="pie", vertex_pie_fractions=pv,
        #            output="lesmis-nested-sbm-marginals.svg")
        state.draw(vertex_shape="pie", vertex_pie_fractions=pv,output=self.output+"marginals.pdf")



        # Infer partition modes
        pmode = gt.ModeClusterState(bs)

        # Minimize the mode state itself
        gt.mcmc_equilibrate(pmode, wait=1, mcmc_args=dict(niter=1, beta=np.inf))

        # Posterior entropy
        H = pmode.posterior_entropy()

        # log(B!) term

        logB = np.mean(sc.gammaln(np.array([len(np.unique(b)) for b in bs]) + 1))

        # Evidence
        L = -np.mean(dls) + logB + H

        with open(self.output+"info.txt", "a") as f:
            print(f"Model log-evidence = {L}",file=f)

        
    def plotGroupNum(self):
        h = [np.zeros(self.g.num_vertices() + 1) for s in self.state.get_levels()]

        def collect_num_groups(s):
            for l, sl in enumerate(s.get_levels()):
                B = sl.get_nonempty_B()
                h[l][B] += 1

        # Now we collect the marginal distribution for exactly 1,000 sweeps
        gt.mcmc_equilibrate(self.state, force_niter=100, mcmc_args=dict(niter=10),
                            callback=collect_num_groups)
        
        if not os.path.exists(self.output+"/groupNumber"):
            os.makedirs(self.output+"/groupNumber")

        for l,level in enumerate(self.state.get_levels()):
            mat = np.divide(h[l],np.sum(h[l]))
            ind = np.nonzero(mat)[0]
            marginals = mat[ind[0]:ind[len(ind)-1]+1]
            
            plt.xticks(range(ind[0],ind[len(ind)-1]+1))
            plt.bar(ind, marginals, align='center', alpha=0.5)

            plt.xlabel(f"Number of groups, Level {l}", fontsize=16)
            plt.ylabel("Marginal posterior probability", fontsize=16)

            
            plt.savefig(self.output+'groupNumber/groupNumlevel'+str(l)+'.pdf')
            plt.show()


    # def stuff(self):
    #     gt.graph_draw(self.g,output="g.pdf")

    #     print(gt.is_bipartite(g))
    #     # for v in g.iter_vertices():
    #     #     print(v)
    #     #     print(g.vp.name[v])
    #     #     print(g.vp.kind[v])

    #     for e in self.g.iter_edges():
    #         print(e)
    #         print(self.g.vp.name[e[0]],g.vp.name[e[1]])
    #         # print(e,e.source(), e.target())
    #         # print(g.vp.name[e.source()],g.vp.name[e.target()])

    #     state = gt.minimize_nested_blockmodel_dl(g)
    #     gt.mcmc_equilibrate(state, wait=100, mcmc_args=dict(niter=10))

    #     state.print_summary()
    #     print(state.entropy())
    #     gt.draw_hierarchy(state, subsample_edges=1000, layout = "bipartite",output="min.pdf")
