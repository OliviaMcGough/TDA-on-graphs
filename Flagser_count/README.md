# INSTALLING flagset-count

## Normally

Install according to the instructions in the [flagser-count](https://github.com/JasonPSmith/flagser-count) repository.

## With Anaconda

If you have Anaconda on your machine, you may need to do extra work to set it up.

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