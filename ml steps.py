#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


# In[2]:


url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=names)


# In[3]:


dataset.describe()


# In[4]:


dataset.groupby('class').size()


# In[5]:


url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"


# In[6]:


dataset.head()


# In[7]:


dataset.shape


# In[8]:


dataset.describe()


# In[9]:


dataset.info()


# In[10]:


dataset.groupby('class').size()


# In[12]:


dataset['class'].value_counts()


# In[15]:


dataset.plot(kind='box')  #, subplots=True, layout=(2,2), sharex=False, sharey=False
plt.show()


# In[ ]:




