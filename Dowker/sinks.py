# takes adjacency matrix as input and outputs dictionary with every sink vertex and their corresponding source vertices]
def sinks(mat):
    ret = {}
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat.item(i, j) > 0:
                if j in ret:
                    ret[j].append(i)
                else:
                    ret[j] = [i]
    return ret