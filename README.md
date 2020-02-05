# optimizationResearch
This repo contains public data only.  
Please, place your scripts under directories with good desriptive naming.  

## To Automatically install all dependencies into your Anaconda environment:

conda create -n myenv python=3.6.9

activate myenv

while read requirement; do conda install --yes $requirement; done < requirements.txt

