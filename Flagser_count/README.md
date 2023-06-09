# INSTALLING 

## Normally

Install according to the instructions in the [pyflagser](https://github.com/giotto-ai/pyflagser) and [flagser-count](https://github.com/JasonPSmith/flagser-count) repositories.

## With Anaconda

If you have Anaconda on your machine, you may need to do extra work to set up `flagser-count`.

```sh
# go to directory you want to clone the repository in
# clone the repository 
git clone --recursive https://github.com/JasonPSmith/flagser-count.git
# manually change python path 
echo $PYTHONPATH
export PYTHONPATH=/usr/local/lib/python3.9/site-packages
# go into flagser-count file
cd flagser-count
# build the code into your computer
python3 setup.py build
```

If you installed this way, run as follows:

```sh
# in terminal, change python path
echo $PYTHONPATH
export PYTHONPATH=/usr/local/lib/python3.9/site-packages
# change directory to flagser-count, then go into build file, and then into lib file.  For example:
cd Documents/thesis/flagser-count/build/lib.macosx-10.9-x86_64-3.9/
# run file that has been saved in above directory
python3 <FILE>
```


# USAGE

The `flagser_file.py` script expects a three-column dataframe whose rows are edges as follows:

- The first column, called "From", is the source nodes,
- the second column, called "To", is the sink nodes,
- the third column, called "Weight", is the edge weights.

To apply the `flagser_count` function to an undirected graph, the adjacency matrix should be upper-triangular. The function `undirected` can turn the matrix of a directed graph into a matrix corresponding to the underlying undirected graph. You can specify *directed = False* in the `flagser_unweighted` and `flagser_weighted` functions in the case of an undirected graph.