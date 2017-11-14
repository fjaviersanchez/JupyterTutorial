# Jupyter Tutorial

*Javier Sanchez, David Kirkby, Phil Marshall, July 2016*

Basic tutorial on how to use Jupyter notebooks for Astrophysics/Cosmology.

## Get Started

Chose one of the following methods to access the tutorial:

* [View the tutorial notebook on GitHub.](https://github.com/fjaviersanchez/JupyterTutorial/blob/master/TutorialJupyter.ipynb) This only requires a browser but does not allow you to edit and run code.

* Download the necessary files from [https://goo.gl/3GYFTQ](https://goo.gl/3GYFTQ) then expand the archive (zip or tar file):
  * `tar -zxf v0.1.tar.gz` or `unzip v0.1.zip`
  * `cd JupyterTutorial ; jupyter notebook &`
  * The notebook should open in a nearby browser window: click on `TutorialJupyter.ipynb` to launch the notebook.

* Clone the repository from github (requires that you have `git` installed):
  * `git clone https://github.com/fjaviersanchez/JupyterTutorial.git`
  * `cd JupyterTutorial ; jupyter notebook &`
  * The notebook should open in a nearby browser window: click on `TutorialJupyter.ipynb` to launch the notebook.

* Step through the tutorial notebook at [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/fjaviersanchez/jupytertutorial/master)
 
## Requirements

You'll need to install all the packages listed in `[requirements.txt](https://github.com/fjaviersanchez/JupyterTutorial/blob/master/requirements.txt)`:
```bash
pip install -r requirements.txt
```
These are:
```
seaborn
randomfield
bokeh
speclite
sklearn
```
All of which are very useful! -- The tutorial also depends on astropy but this is included in anaconda. Also, it is optional but encouraged to install ```healpy```
