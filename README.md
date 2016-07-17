# Jupyter Tutorial

*Javier Sanchez, David Kirkby, Phil Marshall, July 2016*

Basic tutorial on how to use Jupyter notebooks for Astrophysics/Cosmology.

## Get Started

* [Read the tutorial notebook on GitHub](https://github.com/fjaviersanchez/JupyterTutorial/blob/master/TutorialJupyter.ipynb)

* Step through the tutorial notebook at [mybinder.org](http://mybinder.org/status/fjaviersanchez/jupytertutorial): [![Binder](http://mybinder.org/badge.svg)](http://mybinder.org:/repo/fjaviersanchez/jupytertutorial)
  * Note that anyone can rebuild the `binder` instance of the notebook - just go to [http://mybinder.org/status/fjaviersanchez/jupytertutorial](http://mybinder.org/status/fjaviersanchez/jupytertutorial) and hit relaunch, or go to [http://mybinder.org](http://mybinder.org) and re-enter the repo URL.

* Clone the repo and try it at home:
  * From the command line: `git clone https://github.com/fjaviersanchez/JupyterTutorial.git`
  * Then: `cd JupyterTutorial ; jupyter notebook &`
  * The notebook should open in a nearby browser window: click on `TutorialJupyter.ipynb` to launch the notebook.


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
