# Installation

To install, you need a C++ compiler. These examples use `g++`.

```sh
# make directory on your computer where you want to install tournser 
mkdir tournser-compilation
# go into that directory 
cd !$
# clone the repository 
git clone --recursive https://github.com/JasonPSmith/tournser.git
# go into the file tournser from that repository 
cd tournser
# build the tournser binary with your compiler of choice, e.g.
g++ --std=c++17 tournser.cpp -o ./tournser
# the rest of this installationtion code just organizes the code, but is not necessary for installation
# go back to tournser-compilation
cd ..
# move tournser file into tournser-compilation
mv tournser/ .
# go to directory tournser-compilation is inside of
cd ..
# move tournser to this directory 
mv tournser-compilation/tournser/ .
# remove tournser-compliation
rm -r tournser-compilation/
```

# Usage  
Go to directory where tournser is stored and run the following code. Run `make_tournaplex_input` from `use_tournser.py` to generate `input.txt` in correct format. Note that `output.txt` is the file you want to save the persistence intervals, cell counts, and Betti numbers, and `extra.txt` is the file you want to save the tournaplex, formatted as  described in [https://github.com/JasonPSmith/tournser/blob/master/tournser_documentation.pdf]. If you don't want the tournaplex printed, don't write `--print extra.txt`. You can also specifiy filtrations, see the documentation.

```sh
./tournser input.txt output.txt --print extra.txt
```

## input.txt

The `use_tournser.py` script expects a three-column dataframe whose rows are edges as follows:

- The first column, called "From", is the source nodes,
- the second column, called "To", is the sink nodes,
- the third column, called "Weight", is the edge weights.

From this dataframe, `make_tournaplex_input` can format the `input.txt` file correctly for tournser application.


## Parsing output
`parse_tournser.py` provides code to parse the tournser `extra.txt` file, and provides intersection function if one wants to find the intersection of two tournaplexes.