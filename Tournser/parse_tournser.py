import pandas as pd

def parse(tournser: str):
    ret = []
    dim = -1
    simplices_of_dim = []
    for line in tournser.splitlines():
        if "Dim" in line:
            # assume it never skips a dimension
            dim += 1
            if dim:
                ret.append(simplices_of_dim)
            simplices_of_dim = []
            continue
        vrts = None
        orts = None
        for segment in line.split("|"):
            if "Vrts" in segment:
                vrts = [*map(int, segment[7:].strip().split(" "))]
                if len(vrts) != dim + 1:
                    print(f"something went wrong: dim is {dim} but vrts are {vrts}")
            if dim > 0 and "ort" in segment:
                parsed = segment[7:].replace(" :", "").strip()
                orts = [*map(int, parsed.split(" "))]
                if len(orts) != dim * (dim + 1) / 2:
                    print(f"something went wrong: dim is {dim} but orts are {orts}")
            
        if vrts is None:
            print("Why are there no vrts?")
            
        simplices_of_dim.append((vrts, orts))
    
    ret.append(simplices_of_dim)
    return ret


def intersection_of_size(x1, x2, n):
    x1_n = x1[n - 1]
    x2_n = x2[n - 1]
    return [v for v in x1_n if v in x2_n]

if __name__ == "__main__":
    with open("extra2021all95source.txt") as f:
        contents = f.read()
        data_a = parse(contents)

    with open("extra2021all95sink.txt") as f:
        contents = f.read()
        data_b = parse(contents)

    print(intersection_of_size(data_a, data_b, 2))












