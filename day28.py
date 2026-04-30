'''
DATA ANALYSIS:-
Why this is needed?
-->This is critical because it converts raw data into actionable insights,
enabling information to decision-making easy and improve operational efficiency..

1.Decision-making
2.Improved Operational Efficiency
3.Customer Understanding
4.Market Insight
5.Risk Management
6.Data-Driven Strategies

Line plot:-

import matplotlib.pyplot as pit
x = [1,2,3,4,5]
y = [10,20,15,25,50]
pit.plot(x,y)
pit.show()

Bar Graph:-

import matplotlib.pyplot as pip
pip.bar(["Etv","ABCtv","Tv9"],[20,15,18])
pip.show()

Pie Graph:-

import matplotlib.pyplot as pip
pip.pie([40,25,35,20], labels = ["janu","satya","jhanavi","honey"])
pip.show()

Histogram:-

import matplotlib.pyplot as pip
pip.hist([23,15,78,12])
pip.show()

NumPy:-
-->NumPy(Numerical Python) is the foundational open-source library for scientific computing in python,
providing high-performance,N-dimensional array objects (ndarray)
-->This enables effinient numerical computation linear algebra, and data manipulation,
serving as the basic for tools like Tensorflow and Scipy

import numpy as np
arr = np.array([1,2,3])
print(arr - 1)

Pandas:-

import pandas as pd
data = {"Name" : ["Janu","Satya"],"Marks" : [95,85]}
any = pd.DataFrame(data)
print(any)

import matplotlib.pyplot as pit
x = [1,2,3,4]
y = [0,0,15,16]
pit.plot(x,y)
pit.show()

import matplotlib.pyplot as pip
pip.bar(["Week1","Week2","Week3","Week4"],[10,12,16,18])
pip.show()

import matplotlib.pyplot as pip
pip.pie([10,12,16,18], labels = ["Week1","Week2","Week3","Week4"])
pip.show()

import matplotlib.pyplot as pip
pip.hist([23,15,78,12])
pip.show()


import matplotlib.pyplot as pip
pip.bar([2000,2001,2002,2003],[34,23,56,76],color = "pink" )
pip.title("Bike sales")
pip.xlabel("Years")
pip.ylabel("No.of.sales")
pip.show()

import matplotlib.pyplot as plp
plp.pie([40,15,35,20],labels=["Backend(Python)","Frontend(HTML,CSS)","Database(MySQL)","Testing"])
plp.title("ATM Application(Project)")
plp.legend(["Janu","Jhanavi","Satya","Honey"])
plp.show()

import matplotlib.pyplot as plp
plp.scatter([2023,2024,2025,2026],[67,89,50,66], color="Pink", s=500)
plp.title("Bike Sales")
plp.xlabel("Years")
plp.ylabel("Number of bikes sold")
plp.show()
