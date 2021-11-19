#!/usr/bin/env python
# coding: utf-8

# In[3]:


user=input('enter your name')
s=input('guess a word')
l=['kamalsir','is','good','teacher']
if s in l:
    print('your guess is right',s,'word is found')
else:
    print('your guess is wrong try next ')

