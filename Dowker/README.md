# SET-UP

The `dowker2` and `computePers2` functions are adapted from the functions `dowker` and `computePers` from [PersNet](https://github.com/fmemoli/PersNet).
These functions rely on Javaplex (installation instructions at [persnet-tutorial](https://github.com/fmemoli/PersNet/blob/master/persnet-tutorial.pdf)).
The `sinks` function does not rely on the Dowker construction, but is used to find complementary information. Specifically, it takes an adjacency matrix and will provide a dictionary where each key is a sink vertex and the values are the corresponding source vertices. 

**The input to `dowker2` should be an adjacency matrix**, similar to the format of the output of `make_matrix` from `flagser_file`.
*However*, zeros in this adjacency matrix are not read as absent edges by `dowker2`, instead they represent edges that are present at all levels of the filtration. 
Therefore, choose a number m that is greater than all of the edge weights in your matrix, and switch all entries in the adjacency matrix that would usually be zero to m.
This m is the 8th input of `dowker2`, and any edge with weight m will be treated as an absent edge by `dowker2`.


# USAGE 

Given this matrix M, run the following:
```sh
[x0,x1,x2,x3,x4,x5,x6,m] = dowker2(M)
computePers2(x0,x1,x2,x3,x4,x5,x6,diam)
```
where diam is the upper bound on filtration (you could set this to m).


# A note on efficiency 

The original funtions `dowker` and `computePers` only build simplicies and compute homology of at most dimension 3. Thus I extended the code for these functions to create `dowker2` and `computePers2` which build simplicies and compute homology up to dimension 6. However, this comes at the cost of efficiency. It takes a several minutes to run `dowker2`. One may choose to write analogous funcitons that build simplices of at most 4 or 5 dimensions to cut down on this time.

