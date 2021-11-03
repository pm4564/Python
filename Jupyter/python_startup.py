import pymaid
import matplotlib.pyplot as plt
import numpy as np
import json
import seaborn as sns
from itertools import chain
import os
server = "https://neuropil.janelia.org/tracing/fafb/v14/"
http_user = "fly"
http_pw = "superfly"
token = "308e86c38e5de0d4cd3de4c4e5990e348c09d9f8"

# def connect_adult_em():
#     return pymaid.CatmaidInstance( server, http_user, http_pw, token)

def connect_adult_em():
    return pymaid.CatmaidInstance( server, token, http_user, http_pw)


connect_adult_em()
from py2cytoscape.data.cyrest_client import CyRestClient
from IPython.display import Image
import networkx as nx
import pandas as pd
import hemipy as hp
import dvidtools as dt
import neuprint as neu
import navis
import navis.interfaces.neuprint as nvneu

from neuprint import Client
c = Client('neuprint.janelia.org',
            dataset = 'hemibrain:v1.1',
   token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InBtNDU2NEBnbWFpbC5jb20iLCJsZXZlbCI6Im5vYXV0aCIsImltYWdlLXVybCI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hLS9BT2gxNEdobXdsUzdBcTlpOHZDSk9fakFUMzM4eHN2ekF6UHVYNkloUnl0cT9zej01MD9zej01MCIsImV4cCI6MTc2NzU0OTUzNX0.b9YJNbbUGOHZduU_k2JAQPzpp8bo4fJJ2OJ5cqD77E0")


c.fetch_version()


import bokeh
import hvplot.pandas
import holoviews as hv

import bokeh.palettes
from bokeh.plotting import figure, show, output_notebook
output_notebook()