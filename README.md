# Pivovarov_et_al_2026
This repository contains supplementary data for "The meta-analysis of the structures of type II and V CRISPR-Cas effectors obtained by Cryo-EM and X-Ray Crystallography"  

The best way to use the interactive HTML version of the table is by this URL: https://georgeegreat.github.io/Pivovarov_et_al_2026/


to reproduce the pictures and tables used in the study, .ipynb and .xlsx files from this repository are necessary.
also, environment shoud contain the following libraries:

pandas>=2.0,
numpy>=1.24,
scipy>=1.10,
matplotlib>=3.7,
gemmi>=0.6,
biopython>=1.81,
openpyxl>=3.1

US-align tool should also be installed. We used the this version of US-align

https://github.com/pylelab/USalign/releases/tag/20260527

which were compliled on a local machine (through make). We did not check whether the package version of US-align (i.e. installed through bioconda or homebrew) would also work with this notebook, but presumably it is also sufficient.

For USalign to work, you would need to add it to environment variable. If you run the notebook on HCP cluster, this can be done by pasting 

os.environ["USALIGN"] = "/path/to/USalign/executable"

in the Setup cell of the notebook

otherwise, add it through PATH
export PATH="/path/to/folder/USalign/USalign:$PATH"
