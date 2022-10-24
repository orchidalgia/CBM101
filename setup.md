# Setting up your system

## Command prompt: 
If you are new to computer science, we *strongly* recommend you start by watching [this video](https://www.youtube.com/watch?v=4KpD-L8-uZQ) on how to navigate the command prompt (if you haven't already). Then you can proceed to following these instrcutions on how to set up the course environment.


## Anaconda:
We recommend installing Python via the [Anaconda Distribution](https://www.anaconda.com/download). Be sure to use the "Python 3.6.x" version or later. We will use the Conda Package Management System within the Anaconda Distribution. From the [documentation](https://conda.io/docs):
> Conda is an open source package management system and environment management system that runs on Windows, macOS and Linux. Conda quickly installs, runs and updates packages and their dependencies. Conda easily creates, saves, loads and switches between environments on your local computer.

After the installation run `python --version` in a **terminal window** (or in **Anaconda Prompt** if you are using Windows). If the output show "Python 3.6.x" or later (and "Anaconda") you are good to go.

## GitHub:
The course code is hosted on the code-sharing platform GitHub (where you now are reading this). If you do not have a GitHub account already you should make one now. We recommend that you are using the platform for you own projects during the course. https://github.com/join.

## Install and test the course environment:

After you have successfully installed Anaconda, go through the following steps (if you are using Windows, be at the "Anaconda Prompt").

### Install Git:
```bash
conda install git
```
### Download the repository (downloads inside the current directory):
```bash
git clone https://github.com/orchidalgia/CBM101
cd CBM101
```

### Install mamba
Mamba is a fast package-manager that we can use instead of conda. It works similarly so when using any conda commands (e.g. from <a href="https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf">conda-cheatsheet</a>), just replace 'conda' with 'mamba'.
```bash
conda install mamba -c conda-forge
```
> **NB!** If you can't get mamba to work (might not work on ARM-processors/MacOS), skip this and just use conda (replace any 'mamba' with conda)

### Configure the Python-environment:

```bash
mamba env update
```
This might take a few minutes. When it's ready, check the last outputs for errors. Warnings are fine, but if it throws an error the environment will not work
> **NB!** If this fails, there's a few things you could try:
> 1) If you're a Mac user you can remove the empty conda environment by running `conda env remove -n cbm101` and then try the folloing:
```
CONDA_SUBDIR=osx-64 conda create -n CBM101
conda activate CBM101
conda config --env --set subdir osx-64
mamba env update
```
> 2) You can try temporarily deactivating your antivirus (AV) software. Some software conflates python.exe with a virus (IDP.generic), and will corrupt your install. If your AV gives this warning, delete your environment (`conda remove --name cbm101 --all --yes`), deactivate the AV and run the command above again.
You should then reactivate the AV.


### Activate the environment:
Remember to do this every time you're gonna run anything. Everything is now installed inside this environment and can't be accessed from base environment.
```bash
conda activate cbm101
```
If you are using Linux or MacOS and the command above fails, type
```bash
source ~/.bash_profile
```
and try `conda activate cbm101` again. If this fails, activate the environment by typing `source activate cbm101` instead.

### Test your installation:
Open jupyter:
```bash
jupyter notebook
```
(Tip: you can auto complete the name of a file/directory by pressing Tab, so you won't have to write out the 
full name.) Jupyter notebook only supports Firefox, Safari and Chrome. Unless you have set one of these as your default browser, 
you should do so, or alternatively you can run `jupyter notebook --no-browser` and paste the link into a supported browser.
You can also use [JupyterLab](https://github.com/jupyterlab/jupyterlab): `jupyter lab`.

### Activate automatic table of contents:
1. Click Nbextensions at Jupyter menu (next to Files, Running, Cluster)
2. Find Table of contents(2) and Enable it.
3. Go back to Files and navigate to python_basics_notebooks (e.g. B_Python_and_friends/0_Python_basics_notebooks/0_Introduction.ipynb)
4. Now there should be a button for ToC in the menu bar next to icons (the rightmost icon). 
5. Now you can go through any notebooks in the folder you find helpful for you.


### That's it! Now you hopefully have a working environment for the course notebooks. 
This environment will be used in both PART1 an PART2 of this course. For PART3 you will need another environment that is installed in the next step. You can either do it now or later when you need it. In the end of this setup there is helpful commands for updating the course materials you have downloaded if (and when) they get updated here in github.

--- 

## Install environment for Pycaret:
Later in this course we will use Pycaret which is a machine learning library. Installing it in this same environment will cause package conflicts which is why we will make another environment for it. This time lets create an empty environment first instead of using ready-made environment file.
```bash
conda deactivate #exit current environment if it's activated
conda create --name cbmPycaret
conda activate cbmPycaret
pip install --pre pycaret
```

## Update your local repository:
The code and environment might get updated during the course. To update to most recent version run the following:
* Update code: 
```bash
git pull
```
* Update environment:
```bash
conda activate cbm101
mamba env update
```

## Overwriting local changes
Sometimes `git pull` will throw an error message as it would overwrite any local changes you have made. This 
problem can be solved by:
i) Make a copy of the notebook (.ipynb) files before working through them.
OR 
ii) 
```bash
git fetch --all
git reset --hard origin/master
```
**WARNING:** option ii) *will* permanently delete any personal changes you have made to any of the original files (ie. if the file name is same)
(but not the copied ones).
