# using flagser_count 
# assuming we have data in a dataframe (df) with three columns, From, To, and Weight to describe a weighted, directed graph


from pyflagsercount import flagser_count
import numpy as np
import pandas as pd
import networkx as nx
from pyflagser import flagser_unweighted
from pyflagser import flagser_weighted
import scipy



# DEFINE FUNCTIONS

# this function will make sure the labels of your vertices are consistent with those used in tournser
def simplify(df):
    ordering = {}
    for (i, j) in enumerate(set(df["To"]).union(set(df["From"]))):
        ordering[j] = i
    new_from = df["From"].apply(lambda r: ordering[r])
    new_to = df["To"].apply(lambda r: ordering[r])
    new_df = pd.DataFrame({"From": new_from, "To": new_to, "Weight": df["Weight"]})
    return new_df.sort_values(["From", "To"]), ordering


def number_vertices(df):
    return len(set(df["To"]).union(set(df["From"])))

# set threshold as highested weight you want
def make_matrix(df, threshold):
    n = number_vertices(df)
    # create nodelist otherwise adjecency_matrix will reorder your vertices
    nodeList = []
    for i in range(n):
        nodeList.append(i)

    # filter too-high weights
    for row in range(len(df)):
        if df.iloc[row,2] > threshold:
            df.iloc[row,2] = 0 
    graph = nx.from_pandas_edgelist(df, 'From', 'To', create_using=nx.DiGraph())

    # make adjacency matrix
    attr = {}
    for i in range(len(df)):#
        node1 = df.iloc[i,0]
        node2 = df.iloc[i,1]
        attr[(node1,node2)]={'weight': df.iloc[i,2]}
    nx.set_edge_attributes(graph, attr)
    mat = nx.adjacency_matrix(graph, nodelist=nodeList).todense()
    return scipy.sparse.csr_matrix(mat)

# look at intersection of two flagser_count outputs, where n is the number of vertices in the simplices you want to find the intersection of
def intersection_of_size(x1, x2, n):
    x1_n = x1["simplices"][n - 1]
    x2_n = x2["simplices"][n - 1]
    return [v for v in x1_n if v in x2_n]










# EXAMPLE: suppose you have two graphs (represented as dataframes df1, df2) 
m1 = make_matrix(simplify(df1))
m2 = make_matrix(simplify(df2))

# if you only want betti numbers and cell counts, indicate return_simplices=False
x1 = flagser_count(m1, return_simplices=True)
x2 = flagser_count(m1, return_simplices=True)

print(intersection_of_size(x1,x2,3))
