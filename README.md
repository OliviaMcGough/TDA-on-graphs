This repository contains an agglomeration of code for the purpose of applying Topological Data Analysis (TDA) to graph data. Specifically, given a (directed) graph, this code allows one to calculate the (persistent) homology of the corresponding flag complex, directed flag complex, flag tournaplex, and Dowker sink complex. Additionally, options are provided to print all of the simplices present in these complexes.

The code corresponding to the flag complex and directed flag complex can be found in the folder `Flagser_count`. This folder relies on the [pyflagser](https://github.com/giotto-ai/pyflagser) and [flagser-count](https://github.com/JasonPSmith/flagser-count) repositories.

The code corresponding to the flag tournaplex can be found in the folder `Tournser`.  This folder relies on the [tournser](https://github.com/JasonPSmith/tournser.git) repository.

Finally, the code corresponding to the Dowker sink complex can be found in the folder `Dowker`. This folder contains adaptations of the code from [PersNet](https://github.com/fmemoli/PersNet) repository. Note that the Dowker calcuations rely on Javaplex, so this code is written in matlab.