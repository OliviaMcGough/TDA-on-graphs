# This file explains how to clone the tounser github repository 




############################# INSTALLATION #################################
# make directory on your computer where you want to install tounser 
mkdir tournser-compilation
# go into that directory 
cd !$
# clone the repository 
git clone --recursive https://github.com/JasonPSmith/tournser.git
# go into the file tournser from that repository 
cd tournser
# use g++ to run the C++ code needed to use code from this repository
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








