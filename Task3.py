#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

df = pd.DataFrame(dict(data=[2, 4, 1, 5, 9, 6, 0, 7]))
fig, ax = plt.subplots()

df['data'].plot(kind='bar', color='red')
df['data'].plot(kind='line', marker='*', color='black', ms=10)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Sample Plot")
plt.show()


# In[6]:


import numpy as np 
import matplotlib.pyplot as plt 

# set width of bar 
barWidth = 0.25
fig = plt.subplots(figsize =(12, 8)) 

# set height of bar 
B1 = [22, 10, 1, 9, 22] 
B2 = [18, 9, 12, 5, 19] 
B3 = [20, 13, 4, 15, 27] 

# Set position of bar on X axis 
br1 = np.arange(len(B1)) 
br2 = [x + barWidth for x in br1] 
br3 = [x + barWidth for x in br2] 

# Make the plot
plt.bar(br1, B1, color ='r', width = barWidth, 
        edgecolor ='grey', label ='B1') 
plt.bar(br2, B2, color ='g', width = barWidth, 
        edgecolor ='grey', label ='B2') 
plt.bar(br3, B3, color ='b', width = barWidth, 
        edgecolor ='grey', label ='B3') 

# Adding Xticks 
plt.xlabel('Branch', fontweight ='bold', fontsize = 15) 
plt.ylabel('Students passed', fontweight ='bold', fontsize = 15) 
plt.xticks([r + barWidth for r in range(len(B1))], 
        ['2020', '2021', '2022', '2023', '2024'])

plt.legend()
plt.show()


# In[ ]:




