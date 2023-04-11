import pandas as pd

# simplifying the data because tournser requires that the vertices be labeled 1 through n and the edges be in lexicographic order
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


# the threshold input value can be used to set an upper threshold on weights
def make_tournaplex_input(df, year, threshold):
    df = simplify(df)
    df = df[df.Weight <= threshold]
    
    ret = "dim 0:\n"
    ret += " ".join("1" for _ in range(number_vertices(df)))
    ret += "\n"
    ret += "dim 1:"
    ret += "\n"
    
    for source, sink, weight in zip(df["From"], df["To"], df["Weight"]):
        ret += str(source) + " " + str(sink) + " " + str(weight) + "\n"
    return 