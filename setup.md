# Setting up your system

## Video walkthrough: 
We provide a [step-by-step instruction video](https://www.youtube.com/watch?v=BF9OTam4nwk) which covers everything you need to do get started with CBM101. Also, if you are new to computer science, we *strongly* recommend you start by watching [this video](https://www.youtube.com/watch?v=4KpD-L8-uZQ) on how to navigate the command terminal.


## Anaconda:
We recommend installing Python via the [Anaconda Distribution](https://www.anaconda.com/download). Be sure to use the "Python 3.6.x" version or later. We will use the Conda Package Management System within the Anaconda Distribution. From the [documentation](https://conda.io/docs):
> Conda is an open source package management system and environment management system that runs on Windows, macOS and Linux. Conda quickly installs, runs and updates packages and their dependencies. Conda easily creates, saves, loads and switches between environments on your local computer.

After the installation run `python --version` in a terminal window (in "Anaconda Prompt" if you are using Windows). If the output show "Python 3.6.x" or later (and "Anaconda") you are good to go.

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
Mamba is a fast package-manager that we can use instead of conda. It works similarly so when using any conda commands, just replace 'conda' with 'mamba'.
```bash
conda install mamba
```
**NB** If you can't install mamba (might not work on ARM-processors/MacOS), skip this and just use conda (replace any 'mamba' with conda)

### Configure the Python-environment:
```bash
mamba env update
```
**NB!** If this fails, we recommend you temporarily deactivate your antivirus (AV) software. Some software conflates python.exe with a virus (IDP.generic), and will corrupt your install. If your AV gives this warning, delete your environment (`conda remove --name cbm101 --all --yes`), deactivate the AV and run the commands below.
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
3. Go back to Files and open any notebook (e.g B_Python_and_friends/1_pandas_basics.ipynb)
4. Now there should be a button for ToC next to icons (the rightmost icon). 

## Install the other environment:
Later in this course we use Pycaret and we need to install it in another environment
So in the base environment (use conda deactivate to exit cbm101):
```bash
conda create --name cbmPycaret
conda activate cbmPycaret
pip install --pre pycaret
```

## Update your local repository:
The code and environment will be updated during the course. Run the following commands regularly:
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
