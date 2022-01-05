import numpy
import pyqtgraph as pg

from pyqtgraph.Qt import QtGui, QtCore


def gaussian(A, B, x):
  return A * numpy.exp(-(x/(2. * B))**2.)

def mouseMoved(evt):
  mousePoint = p.vb.mapSceneToView(evt[0])
  label.setText("<span style='font-size: 14pt; color: white'> x = %0.2f, <span style='color: white'> y = %0.2f</span>" % (int(mousePoint.x() + 0.5), mousePoint.y()))

# Initial data frame
# x = numpy.linspace(-5., 5., 10000)
# y = gaussian(5., 0.2, x)
y = [577,
            619,
            615,
            708,
            844,
            866,
            755,
            894,
            938,
            1080,
            1104,
            1178,
            875,
            1188
            ]

# xq = list(range(2001, 2016))
x = list(range(2008, 2022))


# Generate layout
win = pg.GraphicsWindow()
label = pg.LabelItem(justify = "right")
win.addItem(label)

p = win.addPlot(row = 1, col = 0)

plot = p.plot(x, y, pen = "y")

proxy = pg.SignalProxy(p.scene().sigMouseMoved, rateLimit=60, slot=mouseMoved)

# Update layout with new data
i = 0
for i in range(20):
    while i < 500:
      noise = numpy.random.normal(0, .2, len(y))

      y_new = y + noise

      plot.setData(x, y_new, pen = "y", clear = True)

      p.enableAutoRange("xy", False)

      pg.QtGui.QApplication.processEvents()

      i += 1
win.close()