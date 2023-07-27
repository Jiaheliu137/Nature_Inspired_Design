This repository is used to record Course Nature_Inspired_Design.

```
git clone https://github.com/Jiaheliu137/Nature_Inspired_Design
cd Nature_Inspired_Design
pip install -r requirements.txt
```

## Project1

项目1提供了若干多模态函数以及对应的可视化工具

在了解了多模态函数的基础上可以使用EP或者FEP算法来寻找多模态函数的最优解

### 函数可视化：

```
cd ./project1/draw_multimoldal_fun
python draw.py -h
python draw.py -g
```

![截屏2023-07-27 06.26.34](./README.assets/%E6%88%AA%E5%B1%8F2023-07-27%2006.26.34.png)

### 使用进化算法

```
cd ./project1/EP
python EP.py
```

在EP.py中参考注释任意更改以下参数观察算法的效果

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

![截屏2023-07-27 06.32.11](./README.assets/%E6%88%AA%E5%B1%8F2023-07-27%2006.32.11.png)

## Project2

项目二尝试用EP算法解决[旅行商问题](https://en.wikipedia.org/wiki/Traveling_purchaser_problem)

该项目用EP算法实现了二维和三维最短路径的寻找，同时实现了简短的动画，可以直观的看到随着种群的迭代，每一代中最短路径的变化情况

```
cd ./project2
python TSP.py -h
```

运行

```
python TSP.py 
```

或者

```
python TSP.py -cn 30 d 2 in 200 -gn 1000 -mp 0.3 -f 20
```



<video controls>
  <source src="./project2/imgs/animation_2d.mp4" type="video/mp4">
</video>

<video  controls>
  <source src="./project2/imgs/animation_3d.mp4" type="video/mp4">
</video>
[更详细的内容,点击我](./detail_CN.md)