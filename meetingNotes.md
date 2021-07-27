layered networks later


09 july

best model: 
minimize entropy: explain simplest way
different processes/angles to approach it but ultimately goal is to minimize entropy

graph tool essential
community detection

(disease classification)

12 july

community for diseases
patients with demographic values(ethnic age etc)
ICD9 codes: insurance: identify specific diseases

thousands of codes

end up with bipartite network 
with differnet layers

layer diseases and demographics and patients
(layer is like a line)

could project bipartite into single layer
hard to optimise parameters
cant use entropy since parameters lead up to networks with different number of vertises and edges
bipartite 



network with different types of connections
different grouping of diseases


take data and make wrapper to conveniently experiment with sbm on data 
see which ones gives the best community 



NOTEBOOK ON DICE

have data with various connection types
need to find way that gives us minimum entropy 
(for community finding ? )

want to connect the diseases
group them 



need to try different types of block models 

setup framework to compare different sbm on same data

try more SBM

start on small network 

only use ethnicity groups, gender, icd9 codes and age groups

find model with smallest entropy
data should be described that way

investigate different types of SBM:

latent poisson multigraph
nested
multilayer
single
degree corrected or not 

compare in term of entropy
and mutual info: how much they overlap

(could fix partitions: paper by tiago)

libraries make use of graphtool with framework that could be useful 
 

 build small script uses SBM in proper way

 does everything to minimize entropy

 for all models that does it to compute fast


 also something on modes and posterior could be good 



 16 july 


smbm: data manipulation + graphtool 
also on bipartite 

topic modelisation 

copy data manipulation functions

fit function: initialise blockstate and minimize nested BM 

use minimized nested + run some mcmc equilibrate
best way to do it : tries to get stuck local minima of entropy (find ref ?)

what want to do: compare basic partition from medical category to SBM ones
if can get better entropy with sbm

what well have
block states in which partitions are the ones given by doctors/classifications 
-> in 13 categories: can be seen as blocks 
and compare them to ones obtained by SBM

want to find entropy of doctor classification

and evaluate diverse partitions obtained by SBM

and perhaps see if we can directly improve partition we give

planted block model: give partition to start from and can then improve it 

then see if it makes any medical sense

simple: applying many stochastic models types and run experiments

tricky: have bipartite network 
network has patients and will be tricky to understand planted with patients cuz dont have exact communities for patient
have classes for doctors, in our network also have patients 


could project bipartite into network of diseases, using the number of common patients that diseases have, rescaling the contribution of each neighbourgh(patient) on their connections


first: try to do different instances of SBM and see which one is best

important ones:
- nested
- multilayer ? means that edges represent different types of connections: patient to demographic; patient to disease; age to patient; gender to patient


patients connected to diseases and demographic:
try to find multilayer structure with nested and multilayer 

see if it improves classification: reduces entropy 


next step: include medical classification to compare with 
could end up with at last 8 models 



look at layered network paper
also include peixoto papers understanding 

dont need to be too detailed; could increase level of detail later 


21 july 

do on patients and not admission 

DIFFERENCE DEGREE CORRECTED VS NOT 

(not from valerio: pick a group of diseases from each group and check if it makes sense
to  compare multilayer to non-multilayer ? 
)

DO AGE TOO

remove all same block: remove 


reduced mutual information
https://graph-tool.skewed.de/static/doc/inference.html#graph_tool.inference.partition_centroid.reduced_mutual_information


