#!/usr/bin/env python
# coding: utf-8

# In[51]:


import json
from pyahp import parse

with open('ahpex.json') as json_model:
    # model can also be a python dictionary
    model = json.load(json_model)

ahp_model = parse(model)
priorities = ahp_model.get_priorities()


# In[52]:


priorities

