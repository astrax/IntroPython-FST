from PyQt4 import QtCore,  QtGui
from PyQt4.QtGui import QSizePolicy
from PyQt4.QtCore import QSize
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as Canvas
from matplotlib.backends.backend_qt4 import NavigationToolbar2QT as NavigationToolbar
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.figure import Figure
from matplotlib import rcParams
rcParams['font.size'] = 9


class QtMplCanvas(Canvas):
    def __init__(self, parent=None, width = 6.5, height = 5.5, dpi = 100, sharex = None, sharey = None, fig = None):
        if fig == None:
            self.fig = Figure(figsize = (width, height), dpi=dpi, facecolor = '#FFFFFF')
            self.ax = self.fig.add_subplot(111, projection='3d')
            self.fig.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9)
            self.ax.hold(True)
        else:
            self.fig = fig

        Canvas.__init__(self, self.fig)
        Canvas.setSizePolicy(self,
            QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Expanding)
        Canvas.updateGeometry(self)

    def sizeHint(self):
        w, h = self.get_width_height()
        return QtCore.QSize(w, h)

    def minimumSizeHint(self):
        return QtCore.QSize(10, 10)

#    def sizeHint(self):
#        w, h = self.get_width_height()
#        return QtCore.QSize(w, h)
#
#    def minimumSizeHint(self):
#        return QtCore.QSize(10, 10)


class MyNavigationToolbar(NavigationToolbar) :
    def __init__(self, parent, canvas, direction = 'h' ) :

        self.canvas = canvas
        QWidget.__init__( self, parent )

        if direction=='h' :
            self.layout = QHBoxLayout( self )
        else :
            self.layout = QVBoxLayout( self )

        self.layout.setMargin( 2 )
        self.layout.setSpacing( 0 )

        NavigationToolbar2.__init__( self, canvas )


    def set_message( self, s ):
        pass


class MPL_WIDGET_3D(QtGui.QWidget):
    def __init__(self, parent = None, enableAutoScale = False, enableCSV = False, enableEdit = False, fig = None):
        QtGui.QWidget.__init__(self, parent)
        self.canvas = QtMplCanvas(fig)
        self.canvas.ax.mouse_init()
        self.toolbar = NavigationToolbar(self.canvas, self.canvas)
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.canvas)
        self.vbox.addWidget(self.toolbar)
        self.setLayout(self.vbox)

class MatplotlibWidget(Canvas):
    """
    MatplotlibWidget inherits PyQt4.QtGui.QWidget
    and matplotlib.backend_bases.FigureCanvasBase
    
    """
    def __init__(self, parent=None, title='',suptitle='', xlabel='', ylabel='',
                 xlim=None, ylim=None, xscale='linear', yscale='linear',
                 width=6.5, height= 5.5, dpi=100, hold=False):
        self.figure = Figure(figsize=(width, height), dpi=dpi)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_title(title)
        self.figure.suptitle(suptitle)
        self.ax.set_xlabel(xlabel)
        self.ax.set_ylabel(ylabel)
       

        if xscale is not None:
            self.ax.set_xscale(xscale)
        if yscale is not None:
            self.ax.set_yscale(yscale)
        if xlim is not None:
            self.ax.set_xlim(*xlim)
        if ylim is not None:
            self.ax.set_ylim(*ylim)
        self.ax.hold(hold)

        Canvas.__init__(self, self.figure)
        self.setParent(parent)
        Canvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        Canvas.updateGeometry(self)

    def sizeHint(self):
        w, h = self.get_width_height()
        return QSize(w, h)

    def minimumSizeHint(self):
        return QSize(10, 10)
        
class MPL_WIDGET_2D(QtGui.QWidget):
    def __init__(self, parent = None, enableAutoScale = False, enableCSV = False, enableEdit = False, fig = None):
        QtGui.QWidget.__init__(self, parent)
        self.canvas = MatplotlibWidget(fig)
        self.toolbar = NavigationToolbar(self.canvas, self.canvas)
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.canvas)
        self.vbox.addWidget(self.toolbar)
        self.setLayout(self.vbox)

