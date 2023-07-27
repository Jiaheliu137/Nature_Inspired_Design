This repository is used to record the course Nature_Inspired_Design.

```
git clone https://github.com/Jiaheliu137/Nature_Inspired_Design
cd Nature_Inspired_Design
pip install -r requirements.txt
```

## Project1

Project 1 provides several multimodal functions and corresponding visualization tools

After understanding the multimodal functions, you can use the EP or FEP algorithm to find the optimal solution of the multimodal functions

### Function Visualization：

```
cd ./project1/draw_multimoldal_fun
python draw.py -h
python draw.py -g
```

![截屏2023-07-27 06.32.11](./README.assets/%E6%88%AA%E5%B1%8F2023-07-27%2006.32.11-0423494.png)



### Using Evolutionary Algorithm

```
cd ./project1/EP
python EP.py
```

Refer to the comments in EP.py to change any of the following parameters to observe the effect of the EP algorithm

```python
DNA_SIZE = 2             # DNA length
BOUND = [-10, 10]      # Upper and lower bounds for x and y
POP_SIZE = 1000           # Population size
N_GENERATIONS = 2000      # Number of generations

MUTATION_SIGMA = 0.1     # Standard deviation for mutation
MUTATION_P = 0.1            # Probability of mutation
EA_METHOD="FEP"             # Evolutionary algorithm choice: "EP" or "FEP"

func = rastrigin # rastrigin or peaks

"""
Name of the 23 function to plot (e.g., ackley, bukin,
cross_in_tray, drop_wave, easom, eggholder, first_penalized,
goldstein_price, holder_table, langermann, levy, levy13,
michalewicz, peaks, quartic, rastrigin, schaffer2, schaffer4,
second_penalized, shekels_foxholes, six_hump_camel,
styblinski_tang, three_hump_camel).
"""
```

![截屏2023-07-27 06.32.11](./README.assets/%E6%88%AA%E5%B1%8F2023-07-27%2006.32.11-0423494.png)

## Project2

Project 2 attempts to use the EP algorithm to solve the [Traveling Salesman Problem](https://en.wikipedia.org/wiki/Traveling_salesman_problem)

This project uses the EP algorithm to find the shortest path in two dimensions and three dimensions, and also implements a short animation, which can intuitively see the changes of the shortest path with the iteration of the population

```
cd ./project2
python TSP.py -h
```

To run

```
python TSP.py 
```

Or

```bash
python TSP.py -cn 30 -d 2 -in 200 -gn 1000 -mp 0.3 -f 20
```

<video controls>
  <source src="./project2/imgs/animation_2d.mp4" type="video/mp4">
</video>


<video controls>
  <source src="./project2/imgs/animation_3d.mp4" type="video/mp4">
</video>



![eg](./README.assets/%E6%88%AA%E5%B1%8F2023-07-27%2010.25.12-0423494.png)

[video](./project2/imgs)



[For more details,click me](./detail.md)



