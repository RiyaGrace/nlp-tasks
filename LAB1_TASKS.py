#!/usr/bin/env python
# coding: utf-8

# # LAB1

# In[3]:


#Import nltk package
import nltk
#Import book from nltk
from nltk.book import *


# In[4]:


#FROM CORPUS IMPORT BROWN CORPUS AND ACCESS
from nltk.corpus import brown
brown.categories()


# In[5]:


brown.words(categories='hobbies')[:100]


# In[6]:


#FROM CORPUS IMPORT INUGURAL CORPUS AND ACCESS
from nltk.corpus import inaugural
inaugural.fileids()
inaugural.words(fileids='2017-Trump.txt')


# In[7]:


from nltk.corpus import inaugural 
inaugural.fileids()


# In[8]:


# LIST OF 100 WORDS IN THE ONE OF THE INAUGURAL SPEECHES BY PRESIDENT LINCOLN
inaugural.words(fileids='1865-Lincoln.txt')[:100]


# In[9]:


#DISPLAY FIELDS OF INAUGURAL CORPUS AND GET WORDS FROM 1913-WILSON.TXT
from nltk.corpus import inaugural
inaugural.fileids()
inaugural.words(fileids='1913-Wilson.txt')


# In[10]:


#DISPLAY FIELDS OF INAUGURAL CORPUS AND GET WORDS FROM 1977-CARTER.txt
from nltk.corpus import inaugural
inaugural.fileids()
inaugural.words(fileids='1977-Carter.txt')


# In[11]:


#IMPORT WEBTEXT AND DISPLAY THE DATA
from nltk.corpus import webtext
webtext.fileids()
for fileid in webtext.fileids():
    print(fileid,webtext.raw(fileid)[:100])


# In[12]:


#FREQUENCY DISTRIBUTION
text1="Don't allow sites that set removed cookies to set future cookies"
fd=nltk.FreqDist(text1.split())


# In[13]:


fd


# In[14]:


#CONDITIONAL FREQUENCY DISTRIBUTION
from nltk.probability import ConditionalFreqDist
cfd=ConditionalFreqDist((len(word),word) for word in text1.split())
cfd[3]


# In[15]:


cfd[6]


# In[ ]:




