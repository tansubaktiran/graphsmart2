import random
from bokeh.models.tools import Toolbar
import pandas
import numpy as np
import pandas as pd

import pandas
from bokeh.layouts import layout
from bokeh.models.glyphs import Circle
from bokeh.models.sources import ColumnDataSource
from bokeh.plotting import figure, output_file, save
from bokeh.io import curdoc, show
from numpy import source
import pandas

from bokeh.models import Range1d, PanTool, ResetTool, HoverTool, Band, Toggle
from bokeh.models.annotations import Label, LabelSet, Span
from bokeh.models.widgets import Slider
from bokeh.layouts import gridplot
from bokeh.io import curdoc
from bokeh.transform import dodge
from math import pi


data1 =pandas.DataFrame([[1,2,3,4,5], [6,7,8,9,10]])
print(data1)


f = figure()
f.square(x=data1.iloc[0,:] , y=data1.iloc[1,:], size=15, color="orangered")

myspan = Span(location=8, dimension='width',
line_color='blue',line_alpha = .5, line_width=1.5, level="underlay", visible=True)
f.add_layout(myspan)

def hide_span(arg):
    myspan.visible = not(myspan.visible)

toggle = Toggle(label="Show/Hide span", button_type="success", active=True)
toggle.on_click(hide_span)

lay_out2 = layout([[toggle]])
lay_out = gridplot([[f]],plot_width=600, plot_height=400)

curdoc().add_root(lay_out)
curdoc().add_root(lay_out2)


#show(f)