#!/usr/bin/env python
# coding: utf-8

# In[2]:


import unittest

from test_manager import TestManager
from test_quizzing import TestQuizzing

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestManager))
    suite.addTest(unittest.makeSuite(TestQuizzing))
    return suite

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)


# In[ ]:




