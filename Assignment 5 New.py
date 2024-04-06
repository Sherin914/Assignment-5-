#!/usr/bin/env python
# coding: utf-8

# In[14]:


#Importing libraries.
import pandas as pd

#Importing the excel file.
data = pd.read_excel("C:\\Users\\sheri\\OneDrive\\Desktop\\Assignment 5 New .xlsx")


# Calculate average height
average_height = data['Height'].mean()

# Calculate average weight
average_weight = data['Weight'].mean()

# Calculate average IQ
average_iq = data['PIQ'].mean()

# Print results
print("Average Height:", average_height)
print("Average Weight:", average_weight)
print("Average IQ:", average_iq)


# In[15]:


std = data['Height'].std()
print("Standard Deviation of Height:", std)


# In[16]:


std1 = data['Weight'].std()
print("Standard Deviation of Weight:", std1)


# In[17]:


std2 = data['BMI'].std()
print("Standard Deviation of BMI:", std2)


# In[ ]:




