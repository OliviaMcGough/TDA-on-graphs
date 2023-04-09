# Install flagser-count and RUN flagser-count file


# INSTALLING flagser-count

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


# NOTE: if you do not have anaconda downloaded, you may be able to clone the repository as usual. Python on my computer automatically runs through anaconda which was for some reason not compatible with flagser-count. This is why I have to manually change my python path each time.








# RUN file that relies on flagser-count

# in terminal, change python path
echo $PYTHONPATH
export PYTHONPATH=/usr/local/lib/python3.9/site-packages
# change directory to flagser-count, then go into build file, and then into lib file.  For example:
cd Documents/thesis/flagser-count/build/lib.macosx-10.9-x86_64-3.9/
# run file that has been saved in above directory
python3 <insert what file to run here. ex: mytest.py, net_migration1.py>