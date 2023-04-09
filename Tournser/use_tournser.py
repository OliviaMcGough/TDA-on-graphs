# USING TOURNSER 
# go to directory where tournser is stored
# run the following code
# input.txt is formatted as described in tournser_documentation.pdf from https://github.com/JasonPSmith/tournser.git
# output.txt is the file you want to save the persistence intervals, cell counts, and betti numbers,
# extra.txt is the file you want to save the tournaple, formatted as  described in in tournser_documentation.pdf from https://github.com/JasonPSmith/tournser.git
./tournser input.txt output.txt --print extra.txt
# if you don't want the tournaplex printed, don't write '--print extra.txt'. 
# you can also specifiy filtrations, see tournser_documentation.pdf from https://github.com/JasonPSmith/tournser.git