#!/usr/bin/env python
# coding: utf-8

# In[47]:


#import the dataset from pycaret repository
import pandas as pd
data = pd.read_csv('/Users/pratikk/desktop/jupiter/nric_stock.csv')
#import anomaly detection module
#intialize the setup
exp_ano = setup(data)


# In[42]:


anomaly


# In[59]:


## creating a model
cluster=create_model('iforest')
## plotting a model
plot_model(cluster)


# In[ ]:




