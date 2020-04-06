# Bus route optimization project
This repo contains an entire pipeline used for data gathering, analysis and final problem optimization using a number of different solvers. In addition to that, the repo has a mathematical QUBO formulation of the problem along several tests. The QUBO problem is solved using D-Waves offline CPU based simulated annealing solver. The optimality of the solution is checked using GEKKO APOPT and IPOPT continuous solvers. There is also a code for calling D-Waves QPU, however it requires a D-Waves account.

### The structure of the repository is as follows:
* [Optimization pipeline with final results ](https://github.com/lostdevfound/optimizationResearch/blob/master/optimization/optimization.ipynb)

* [TOPSIS bus stop scoring](https://github.com/lostdevfound/optimizationResearch/tree/master/topsis)

* [Getting bus stop data from Translink API](https://github.com/lostdevfound/optimizationResearch/tree/master/get_stops_data)

### Dependencies:
The project uses conda and pip installed packages. To install necessary libs use both *requirements-pip.txt* and *requirements-conda.txt* files.
