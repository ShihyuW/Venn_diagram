#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 17:47:11 2020

@author: shihyu
"""

import pandas as pd
from venn import venn
import matplotlib.pyplot as plt

gene_file=pd.read_excel(r'Input/Genelist.xlsx')
SetA=set(gene_file.iloc[:,0].dropna())
SetB=set(gene_file.iloc[:,1].dropna())
SetC=set(gene_file.iloc[:,2].dropna())


genelist={"A":SetA, "B":SetB, "C":SetC}
venn(genelist)
plt.show()
intersec=cgmh.intersection(SetA).intersection(SetB).intersection(SetC)