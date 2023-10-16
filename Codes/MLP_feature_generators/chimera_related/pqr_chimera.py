#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#file_no=1000
from chimerax.core.commands import run



directory="C:/Users/johnkwon/Desktop/[Ultima]_Solubility/Data/Generative/PQR/"
for i in range(0,5):
    file_name=directory+str(i)+'.pqr'
    save_name=directory+str(i)+'.txt'
    run(session, "open "+file_name)
    run(session, "log clear")
    run(session, "select all")
    run(session, "select helix")
    run(session, "select strand")
    run(session, "select coil")
    run(session, "surface")
    run(session, "mlp")
    run(session, "coulombic") #will change to apbs later
    run(session, "measure area #1")
    run(session, "measure sasa")
    run(session, "measure volume #1")
    run(session, "hbonds")
    run(session, "contacts")
    run(session, "clash")
    run(session, "log save "+save_name)
    run(session, "select all")
    run(session, "delete sel")

