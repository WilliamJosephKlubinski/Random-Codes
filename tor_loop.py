#!/usr/bin/env python
# coding: utf-8

# In[8]:


import time
import os
import webbrowser

while True:
    urL='https://sites.google.com/view/williamklubinski/home'
    firefox_path="C:\\Users\\T14s\\Desktop\\Tor Browser\\Browser\\firefox.exe"
    webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(firefox_path))
    webbrowser.get('firefox').open_new_tab(urL)
    
    time.sleep(38)
    
    os.system("taskkill /im firefox.exe /f")


# In[ ]:





# In[ ]:




