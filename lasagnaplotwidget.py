"""
A simple subclass of PlotWidget to add a lasagna viewbox in Qt Designer
"""

from pyqtgraph import PlotWidget
from lasagna_viewBox import lasagna_viewBox

class LasagnaPlotWidget(PlotWidget):

    def __init__(self, *args, **kwargs):
        if not 'viewBox' in list(kwargs.keys()):
            kwargs['viewBox']=lasagna_viewBox()
        super(LasagnaPlotWidget,self).__init__(*args, **kwargs)
