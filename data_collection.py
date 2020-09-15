# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 09:01:09 2020

@author: Zheng Xie
"""

import glassdoor_scraper as gs

path = "D:/Learn/Python/geckodriver"
df = gs.get_jobs("data_scientist", 100, False, path, 15)

df.to_csv("glassdoor_jobs.csv", index = False)