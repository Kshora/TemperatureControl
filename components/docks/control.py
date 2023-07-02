import pyqtgraph as pg
from PyQt5 import QtGui, QtCore, QtWidgets
from pyqtgraph.dockarea import Dock

# from components.scaleButtons import ScaleButtons
from ..buttons.toggles import MySwitch, OnOffSwitch, QmsSwitch
from ..widgets.analoggauge import AnalogGaugeWidget
from readsettings import select_settings
from QLed import QLed

config = select_settings(verbose=False)
print("GET CONFIG: control.py")
print(f'config["Max Temperature"] {config["Max Temperature"]}')
MAXTEMP = config["Max Temperature"]


class ControlDock(Dock):
    def __init__(self):
        super().__init__("Control")
        self.widget = pg.LayoutWidget()

        self.quitBtn = QtWidgets.QPushButton("quit")
        self.quitBtn.setStyleSheet(
            "QPushButton {color:#f9ffd9; background:#ed2a0c;}"
            "QPushButton:disabled {color:#8f8f8f; background:#bfbfbf;}"
        )
        self.quitBtn.setFont(QtGui.QFont("serif", 16))

        self.scaleBtn = QtWidgets.QComboBox()
        self.scaleBtn.setFont(QtGui.QFont("serif", 18))
        items = ["20 s", "60 sec", "5 min", "15 min", "30 min", "1 hr", "Full"]
        sizes = [20, 60, 5 * 60, 15 * 60, 30 * 60, 60 * 60, -1]
        [self.scaleBtn.addItem(i) for i in items]
        self.sampling_windows = {i: j for i, j in zip(items, sizes)}


        self.FullNormSW = MySwitch()
        self.OnOffSW = OnOffSwitch()
        self.OnOffSW.setFont(QtGui.QFont("serif", 16))

        self.explamp = QLed(self, onColour=QLed.Green, shape=QLed.Circle)
        self.explamp.setValue(False)



        # Analog Gauge to show Temperature
        self.gaugeT = AnalogGaugeWidget()
        self.gaugeT.set_MinValue(0)
        self.gaugeT.set_MaxValue(MAXTEMP)
        self.gaugeT.set_total_scale_angle_size(180)
        self.gaugeT.set_start_scale_angle(180)
        self.gaugeT.set_enable_value_text(False)

        self.__setLayout()

    def __setLayout(self):
        self.addWidget(self.widget)

        self.widget.addWidget(self.OnOffSW, 0, 0)
        self.widget.addWidget(self.explamp, 0, 1)
        self.widget.addWidget(self.quitBtn, 0, 2)

        self.widget.addWidget(self.FullNormSW, 1, 0)
        self.widget.addWidget(self.scaleBtn, 1, 1, 1,2)
        

        # Temperature analouge gauge
        self.widget.addWidget(self.gaugeT, 2, 0, 10, 2)


        self.verticalSpacer = QtWidgets.QSpacerItem(
            0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.widget.layout.setVerticalSpacing(3)
        self.widget.layout.addItem(self.verticalSpacer)


if __name__ == "__main__":
    pass
