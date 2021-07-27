


Multimorbidity is defined by the coexistence of multiple health conditions in an individual. 


patient with multiple diseases

relationship between the patients and their diagnoised diseases can be represented in a network

nodes for each patients
and for diseases

patients node being linked to diseases they have.

the number of connection from diseases to patients and the type of patients they are linked to should be fairly different given their nature 

other diseases connected to same patients

but also the demographic characteristics of the patients, should lead to range of different connection patterns from the diseases

grouping the diseases by the similarity of their relation 


classification 

bring surprising groups of diseases, different from usual classification, 
different factors

task regroup nodes more densely connected together 

community: locally dense connected subgraph 

community finding



https://academic.oup.com/eurpub/article/29/1/182/5033670

maybe this https://www.researchgate.net/profile/Marzouki-Faouzi/publication/341400450_Multi-morbidity_Analysis_using_Community_Detection_Approach_a_Comparative_study/links/5ec854fda6fdcc90d68fa7a1/Multi-morbidity-Analysis-using-Community-Detection-Approach-a-Comparative-study.pdf





community detection

http://www.princeton.edu/~eabbe/publications/abbe_FNT_2.pdf 
intro this paper 
https://appliednetsci.springeropen.com/track/pdf/10.1007/s41109-019-0232-2.pdf

talk on community


https://arxiv.org/pdf/1610.02703v4.pdf

Nonparametric Bayesian inference microcano SBM

many methods for community detection, SBM based on bayesian inference is robust  

generative model inferring the parameters of the modular structure of a network from the data itself.
probabilistic technique distinguishes communities from statistical noise 

microcanonical 




other applications stochatib block model for classifications

talk on sbm 

inference 

bayes 

flat sbm 

nested sbm 

layered 
https://arxiv.org/pdf/1310.4377.pdf
https://topsbm.github.io




multimorbidity: not studied enough, could use progress in network analysis 



community detection in medical perspective

find cluster of diseases 

what is a community 
clique ? too strict 


definition SBM

group membership 
block matrix 

generate graph given two
infer from real data


infer partition


minimum description length

description length amount of info to describe data, the likelihood of found partition giving rise to the given data
minimising this value equivalent to opting for the simplest model, one that will 
completely randomly generated graphs should not give rise to communities 

from bayes
want to find the most likely distribution of the parameters of the models explaining the data. 

MCMC to sample values from the posterior 
https://towardsdatascience.com/from-scratch-bayesian-inference-markov-chain-monte-carlo-and-metropolis-hastings-in-python-ef21a29e25a

https://twiecki.io/blog/2015/11/10/mcmc-sampling/

https://towardsdatascience.com/mcmc-intuition-for-everyone-5ae79fff22b1

MCMC
monte carlo 
relies on generation of random numbers
based on a given distribution

markov chains 
where newly drawn values depend on the previous ones. 

metropolis hastings
which proposed value of teta to accept or reject


nested SBM

layered SBM


MIMIC 
data 
bipartite 

SBM accomodate 

layers: info from demographics ? 


EXPLAIN WHAT IVE DONE AS WELL TOO 


research papers
try understand them
research community finding
get used to library
discover dataset
work on dice 



ICD9 disease classification

data set

admissions 
patients
demographic informations:
age that i grouped 
7 ethnic categories
gender

turned into multilayer graph

bipartite graph simply patients and diseases


add layer for demographics
tripartite graph

different types of connections between patients and diseases along with the demographic categories are taken into account 
weight given to 