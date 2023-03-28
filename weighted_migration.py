from pyflagsercount import flagser_count
import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from pyflagser import flagser_unweighted
from pyflagser import flagser_weighted
import scipy


# PREPROCESSING
state_codes = {}
state_codes[1]='Alabama'
state_codes[2]='Alaska'
#3?
state_codes[4]='Arizona'
state_codes[5]='Arkansas'
state_codes[6]='California'
#7?
state_codes[8]='Colorado'
state_codes[9]='Connecticut'
state_codes[10]='Delaware'
state_codes[11]='District of Columbia'
state_codes[12]='Florida'
state_codes[13]='Georgia'
#14?
state_codes[15]='Hawaii'
state_codes[16]='Idaho'
state_codes[17]='Illinois'
state_codes[18]='Indiana'
state_codes[19]='Iowa'
state_codes[20]='Kansas'
state_codes[21]='Kentucky'
state_codes[22]='Louisiana'
state_codes[23]='Maine'
state_codes[24]='Maryland'
state_codes[25]='Massachusetts'
state_codes[26]='Michigan'
state_codes[27]='Minnesota'
state_codes[28]='Mississippi'
state_codes[29]='Missouri'
state_codes[30]='Montana'
state_codes[31]='Nebraska'
state_codes[32]='Nevada'
state_codes[33]='New Hampshire'
state_codes[34]='New Jersey'
state_codes[35]='New Mexico'
state_codes[36]='New York'
state_codes[37]='North Carolina'
state_codes[38]='North Dakota'
state_codes[39]='Ohio'
state_codes[40]='Oklahoma'
state_codes[41]='Oregon'
state_codes[42]='Pennsylvania'
#43?
state_codes[44]='Rhode Island'
state_codes[45]='South Carolina'
state_codes[46]='South Dakota'
state_codes[47]='Tennessee'
state_codes[48]='Texas'
state_codes[49]='Utah'
state_codes[50]='Vermont'
state_codes[51]='Virginia'
state_codes[53]='Washington'
#52?
state_codes[54]='West Virginia'
state_codes[55]='Wisconsin'
state_codes[56]='Wyoming'


df = pd.read_csv('usa_00003.csv')
df2 = df.loc[df['MIGRATE1'] == 3]
df2 = df2.loc[df2['MIGPLAC1']<=56]
df2 = df2.loc[df2['STATEFIP']<=56]
df2 = df2[['YEAR','MIGPLAC1', 'STATEFIP','METRO', 'SEX', 'AGE', 'RACE', 'HISPAN', 'POVERTY']]


# DEFINE FUNCTIONS
def edge_counts(df):
    edges = {}
    for i in range(len(df)):
        node1 = df.iloc[i,1]
        node2 = df.iloc[i,2]
        edge = (node1, node2)
        if edge not in edges:
            edges[edge] = 1
        else:     
            edges[edge] += 1            
    return edges

def make_df(edges):
    sources = []
    sinks = []
    weights = []
    for edge in edges:
        sources.append(edge[0])
        sinks.append(edge[1])
        weights.append(edges[edge])
    return pd.DataFrame({'From': sources, 'To': sinks, 'Weight': weights})


def normalize(df):
    # compute total out weight
    out_weights = {}
    for i in set(df["From"]):
        out_weights[i] = df[df["From"] == i]["Weight"].sum()
    
    norm = df.apply(lambda s: [s["From"], s["To"], 1.0 - s["Weight"] / out_weights[s["From"]]], axis = 1)
    new_df = pd.DataFrame.from_dict(dict(zip(norm.index, norm.values))).T
    return new_df.rename(columns={0: "From", 1: "To", 2: "Weight"})


def simplify(df):
    ordering = {}
    for (i, state) in enumerate(set(df["To"]).union(set(df["From"]))):
        ordering[state] = i
    new_from = df["From"].apply(lambda r: ordering[r])
    new_to = df["To"].apply(lambda r: ordering[r])
    new_df = pd.DataFrame({"From": new_from, "To": new_to, "Weight": df["Weight"]})
    return new_df.sort_values(["From", "To"]), ordering


def make_matrix(df, threshold):
    # filter too-high weights
    nodeList = []
    for i in range(51):
        nodeList.append(i)
    
    for row in range(len(df)):
        if df.iloc[row,2] > threshold:
            df.iloc[row,2] = 0 
    graph = nx.from_pandas_edgelist(df, 'From', 'To', create_using=nx.DiGraph())

    attr = {}
    for i in range(len(df)):#
        node1 = df.iloc[i,0]
        node2 = df.iloc[i,1]
        attr[(node1,node2)]={'weight': df.iloc[i,2]}
    nx.set_edge_attributes(graph, attr)
    mat = nx.adjacency_matrix(graph, nodelist=nodeList).todense()
    return scipy.sparse.csr_matrix(mat)


def pipeline(year, threshold):
    df = df2.loc[df2['YEAR']==year]
    processed, ordering = simplify(normalize(make_df(edge_counts(df))))
    return make_matrix(processed,threshold), ordering

def intersection_of_size(x1, x2, n):
    x1_n = x1["simplices"][n - 1]
    x2_n = x2["simplices"][n - 1]
    return [v for v in x1_n if v in x2_n]




# NEW STATE CODES
new_state_codes={}
new_state_codes[0] = 'Alabama'
new_state_codes[1] = 'Alaska'
new_state_codes[2] = 'Arizona'
new_state_codes[3] = 'Arkansas'
new_state_codes[4] = 'California'
new_state_codes[5] = 'Colorado'
new_state_codes[6] = 'Connecticut'
new_state_codes[7] = 'Delaware'
new_state_codes[8] = 'District of Columbia'
new_state_codes[9] = 'Florida'
new_state_codes[10]='Georgia'
new_state_codes[11]='Hawaii'
new_state_codes[12]='Idaho'
new_state_codes[13]='Illinois'
new_state_codes[14]='Indiana'
new_state_codes[15]='Iowa'
new_state_codes[16]='Kansas'
new_state_codes[17]='Kentucky'
new_state_codes[18]='Louisiana'
new_state_codes[19]='Maine'
new_state_codes[20]='Maryland'
new_state_codes[21]='Massachusetts'
new_state_codes[22]='Michigan'
new_state_codes[23]='Minnesota'
new_state_codes[24]='Mississippi'
new_state_codes[25]='Missouri'
new_state_codes[26]='Montana'
new_state_codes[27]='Nebraska'
new_state_codes[28]='Nevada'
new_state_codes[29]='New Hampshire'
new_state_codes[30]='New Jersey'
new_state_codes[31]='New Mexico'
new_state_codes[32]='New York'
new_state_codes[33]='North Carolina'
new_state_codes[34]='North Dakota'
new_state_codes[35]='Ohio'
new_state_codes[36]='Oklahoma'
new_state_codes[37]='Oregon'
new_state_codes[38]='Pennsylvania'
new_state_codes[39]='Rhode Island'
new_state_codes[40]='South Carolina'
new_state_codes[41]='South Dakota'
new_state_codes[42]='Tennessee'
new_state_codes[43]='Texas'
new_state_codes[44]='Utah'
new_state_codes[45]='Vermont'
new_state_codes[46]='Virginia'
new_state_codes[47]='Washington'
new_state_codes[48]='West Virginia'
new_state_codes[49]='Wisconsin'
new_state_codes[50]='Wyoming'



#######################   THIS IS ALL FOR 0.95 THRESHOLD   ######################################################

m2000_95, ordering2000 = pipeline(2000, .95)
m2010_95, ordering2010 = pipeline(2010, .95)
m2011_95, ordering2011 = pipeline(2016, .95)
m2016_95, ordering2016 = pipeline(2016, .95)
m2017_95, ordering2017 = pipeline(2017, .95)
m2018_95, ordering2018 = pipeline(2018, .95)
m2019_95, ordering2019 = pipeline(2019, .95)
m2021_95, ordering2021 = pipeline(2021, .95)

if ordering2000 != ordering2019:
    print("uh oh")




X2000_95 = flagser_count(m2000_95, return_simplices=True)
X2010_95 = flagser_count(m2010_95, return_simplices=True)
X2011_95 = flagser_count(m2011_95, return_simplices=True)
X2016_95 = flagser_count(m2016_95, return_simplices=True)
X2017_95 = flagser_count(m2017_95, return_simplices=True)
X2018_95 = flagser_count(m2018_95, return_simplices=True)
X2019_95 = flagser_count(m2019_95, return_simplices=True)
X2021_95 = flagser_count(m2021_95, return_simplices=True)

#import pprint
#print(graph2000)
#pprint.pprint(X2000)

#print(intersection_of_size(X2000, X2019, 5))
#this returns the empty list, for 4 and 5
#same for 2019 and 2021
#but 2018 and 2019 have some 4 in common, and 2018 and 2021 have many in common at 4 an some at 5
#2017 and 2018 have LOTS in common




# X2000: {'euler': 8, 'cell_counts': [51, 295, 483, 261, 30] -- there is considerably less data from 2000
#X2016_95: {'euler': -14, 'cell_counts': [51, 262, 544, 548, 247, 46]
# X2017_95: {'euler': 11, 'cell_counts': [51, 278, 661, 781, 412, 54]
#  X2018_95: {'euler': 8, 'cell_counts': [51, 272, 611, 690, 374, 66]
#  X2019_95: {'euler': 3, 'cell_counts': [51, 269, 584, 591, 258, 30]
# X2021_95 : {'euler': 6, 'cell_counts': [51, 267, 572, 608, 302, 44]


# LOOKING AT 4-SIMPLICES
#intersection of X2016_95, X2017_95: 91
#intersection of X2016_95, X2018_95: 73
#intersection of X2016_95, X2019_95: 85
#intersection of X2016_95, X2021_95: 65
#intersection of X2017_95, X2018_95: 96
#intersection of X2017_95, X2019_95: 68
#intersection of X2017_95, X2021_95: 99
#intersection of X2018_95, X2019_95: 90
#intersection of X2018_95, X2021_95: 82
#intersection of X2019_95, X2021_95: 123

# LOOKING AT 5-SIMPLICES
#intersection of X2016_95, X2017_95: 0
#intersection of X2016_95, X2018_95: 0
#intersection of X2016_95, X2019_95: 19
#intersection of X2016_95, X2021_95: 19
#intersection of X2017_95, X2018_95: 4
#intersection of X2017_95, X2019_95: 0
#intersection of X2017_95, X2021_95: 0
#intersection of X2018_95, X2019_95: 0
#intersection of X2018_95, X2021_95: 0
#intersection of X2019_95, X2021_95: 30



#import pprint
#print(graph2000)
#pprint.pprint(X2000)

intersection_of_all =[]
for i in X2016_95['simplices'][4]:
    if i in X2017_95['simplices'][4] and i in X2018_95['simplices'][4] and i in X2019_95['simplices'][4] and i in X2021_95['simplices'][4]:
        intersection_of_all.append(i)


#Intersection of all
#[15, 13, 25, 9, 43]: Iowa, Illinois, Missouri, Florida, Texas
#[15, 13, 25, 43, 9]: Iowa, Illinois, Missouri, Texas, Florida
#[15, 25, 13, 9, 43]: Iowa, Missouri, Illinois, Florida, Texas
#[15, 25, 13, 43, 9]: Iowa, Missouri, Illinois, Texas, Florida
#[31, 5, 2, 4, 43]: New Mexico, Colorado, Arizona, California, Texas
#[31, 5, 2, 43, 4]: New Mexico, Colorado, Arizona, Texas, California
#[31, 5, 4, 2, 43]: New Mexico, Colorado, California, Colorado, Texas










######################### NOW FOR 0.9 THRESHOLD #################################################


m2000_9, ordering2000 = pipeline(2000, .9)
m2010_9, ordering2010 = pipeline(2010, .9)
m2011_9, ordering2011 = pipeline(2011, .9)
m2016_9, ordering2016 = pipeline(2016, .9)
m2017_9, ordering2017 = pipeline(2017, .9)
m2018_9, ordering2018 = pipeline(2018, .9)
m2019_9, ordering2019 = pipeline(2019, .9)
m2021_9, ordering2021 = pipeline(2021, .9)

if ordering2000 != ordering2019:
    print("uh oh")




X2000_9 = flagser_count(m2000_9, return_simplices=True)
X2010_9 = flagser_count(m2010_9, return_simplices=True)
X2011_9 = flagser_count(m2011_9, return_simplices=True)
X2016_9 = flagser_count(m2016_9, return_simplices=True)
X2017_9 = flagser_count(m2017_9, return_simplices=True)
X2018_9 = flagser_count(m2018_9, return_simplices=True)
X2019_9 = flagser_count(m2019_9, return_simplices=True)
X2021_9 = flagser_count(m2021_9, return_simplices=True)


# X2016_9: 'cell_counts': [51, 97, 36, 2],  3-dim simplices: [6, 21, 32, 9], [31, 2, 4, 43]

# X2017_9: 'cell_counts': [51, 88, 26]

# X2018_9: 'cell_counts': [51, 91, 38, 3], 3-dim simplices: [19, 21, 29, 9], [19, 29, 21, 9], [29, 19, 21, 9]

# X2019_9: 'cell_counts': [51, 88, 35, 5],  3-dim simplicies: [17, 14, 35, 9], [6, 21, 32, 9], [30, 38, 32, 9], [38, 30, 32, 9], [38, 32, 30, 9]

# X2021_9: 'cell_counts': [51, 92, 30, 3],   3-dim simplices: [0, 42, 10, 9], [19, 21, 32, 9], [6, 21, 32, 9]
 
# note that 9 (Florida), 21 (Massachusetts) are common in all


intersection_of_all =[]
for i in X2016_9['simplices'][2]:
    if i in X2017_9['simplices'][2] and i in X2018_9['simplices'][2] and i in X2019_9['simplices'][2] and i in X2021_9['simplices'][2]:
        intersection_of_all.append(i)


# intersection_of_all = 
# [0, 10, 9], Alabama, Georgia, Florida 
# [8, 20, 46], District of Columbia, Maryland, Virginia
# [32, 30, 9], New York, New Jersey, Florida
# [37, 47, 4], Oregon, Washington, California
# [6, 32, 9], Connecticut, New York, Florida
# [30, 32, 9], New Jersey, New York, Florida
# [30, 38, 9], New Jersey, Pennsylvania, Florida 