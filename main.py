from PyQt5 import QtWidgets,QtGui,QtCore
import sys
import gpa_cal,grade_calculator

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("UTBOX")

        self.resize(800, 300)
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        self.open_main_page()
        self.menu_bar = self.menuBar()
        self.create_menus()

        

    def create_menus(self):
        gpa_calc_action = QtWidgets.QAction("GPA cal", self)
        gpa_calc_action.triggered.connect(self.open_gpa_calc)

        menu = self.menu_bar.addMenu("Applications")
        menu.addAction(gpa_calc_action)

    def open_gpa_calc(self):
        self.gpa_calc_window = gpa_cal.GPACalculator()
        self.gpa_calc_window.setupUi(main_window)

        self.time_layout = QtWidgets.QHBoxLayout()

        self.leave_button = QtWidgets.QPushButton('Leave')
        self.leave_button.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.time_layout.addWidget(self.leave_button)
        self.leave_button.clicked.connect(self.open_main_page)
        
        self.new_label = QtWidgets.QLabel("Welcome to GPA Calculator", self.centralWidget())
        self.font = QtGui.QFont()
        self.font.setPointSize(36)
        self.new_label.setFont(self.font)

        self.new_label.setAlignment(QtCore.Qt.AlignCenter)
        self.time_layout.addWidget(self.new_label)
        # 获取 central_widget 的布局
        central_layout = self.centralWidget().layout()
        

        # 将新创建的布局元素添加到 central_widget 的布局中
        central_layout.insertLayout(0, self.time_layout)

    def open_grad_calc(self):
        self.grad_calc_window = grade_calculator.GradeCalculator()
        self.grad_calc_window.setupUi(main_window)

        self.time_layout = QtWidgets.QHBoxLayout()

        self.leave_button = QtWidgets.QPushButton('Leave')
        self.leave_button.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.time_layout.addWidget(self.leave_button)
        self.leave_button.clicked.connect(self.open_main_page)
        
        self.new_label = QtWidgets.QLabel("Welcome to Grade Calculator", self.centralWidget())
        self.font = QtGui.QFont()
        self.font.setPointSize(36)
        self.new_label.setFont(self.font)

        self.new_label.setAlignment(QtCore.Qt.AlignCenter)
        self.time_layout.addWidget(self.new_label)
        # 获取 central_widget 的布局
        central_layout = self.centralWidget().layout()
        

        # 将新创建的布局元素添加到 central_widget 的布局中
        central_layout.insertLayout(0, self.time_layout)

    

    
    def open_main_page(self):
        self.setWindowTitle("UTBOX")

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        self.layout = QtWidgets.QVBoxLayout(central_widget)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.gpa_cal_button = QtWidgets.QPushButton('GPA cal')   
        self.horizontalLayout.addWidget(self.gpa_cal_button)
        self.corse_ave_button = QtWidgets.QPushButton('Corse ave')   
        self.horizontalLayout.addWidget(self.corse_ave_button)
        self.layout.addLayout(self.horizontalLayout)
        
        self.gpa_cal_button.clicked.connect(self.open_gpa_calc)
        self.corse_ave_button.clicked.connect(self.open_grad_calc)

app = QtWidgets.QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec_())