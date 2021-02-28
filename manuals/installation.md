
### Biotiger configuration

The project was based on python 2. Here are the steps that you can make to configure the project:

1. Clone or download the forked repository:\
`git clone git@github.com:alexander-pv/biotiger.git`
   

2. Configure your python 2 environment via conda:
   
    `conda env create -f environment.yml` for Linux OS;\
    `conda env create -f environment_win.yml` for Windows OS;
   
   However, if it doesn't work, you can create your own environment from scratch:\
   `conda create --name py2 python=2.7.*`\
   `conda activate py2`\
   `pip install pytest tqdm`

    Feel free to contact to fix the latest version of the repo.

3. To make sure that everything is OK, run tests:\
   `pytest ./tests`
   