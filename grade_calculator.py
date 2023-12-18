from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget


class GradeCalculator(object):
    def setupUi(self, MainWindow):
        
        self.main_widget = QtWidgets.QWidget(MainWindow)
        self.main_widget.setFocus()
        MainWindow.setCentralWidget(self.main_widget)
        MainWindow.setWindowTitle("Grade Calculator")
        

        self.vbox = QtWidgets.QVBoxLayout(self.main_widget)

        self.grades = []
        self.weights = []

        
        self.hvbox = QtWidgets.QHBoxLayout()
        self.del_grade_button = QtWidgets.QPushButton('- Del Course')
        self.add_grade_button = QtWidgets.QPushButton('+ Add Grade')
        self.hvbox.addWidget(self.del_grade_button)
        self.hvbox.addWidget(self.add_grade_button)

        self.vbox.addLayout(self.hvbox)

        rbox_layout = QtWidgets.QHBoxLayout()
        self.rbox_cal_final_mark = QtWidgets.QRadioButton("calculate final mark")
        self.rbox_cal_final_mark.setChecked(True)
        self.rbox_cal_exam_mark = QtWidgets.QRadioButton("calculate exam mark")
        rbox_layout.addWidget(self.rbox_cal_final_mark)
        rbox_layout.addWidget(self.rbox_cal_exam_mark)
        self.vbox.addLayout(rbox_layout)

        self.optionChoose = "cfm"

        final_grade_layout = QtWidgets.QHBoxLayout()
        self.final_input = QtWidgets.QLineEdit()
        self.final_input.setPlaceholderText("Enter you exam mark (%)")
        self.final_grade_weight_input = QtWidgets.QLineEdit()
        self.final_grade_weight_input.setPlaceholderText("Enter the exam weight (%)")
        final_grade_layout.addWidget(self.final_input)
        final_grade_layout.addWidget(self.final_grade_weight_input)
        self.vbox.addLayout(final_grade_layout)

        self.cal_buttom = QtWidgets.QPushButton("Calculate your final grade")
        self.vbox.addWidget(self.cal_buttom)

        self.result_label = QtWidgets.QLabel()
        self.vbox.addWidget(self.result_label)

        self.events()

        for i in range(5):
            self.createOneAssignment()

    def events(self):
        self.rbox_cal_final_mark.toggled.connect(lambda: self.rboxClick("cfm"))
        self.rbox_cal_exam_mark.toggled.connect(lambda: self.rboxClick("cem"))
        self.cal_buttom.clicked.connect(self.calFinalMark)
        self.add_grade_button.clicked.connect(self.createOneAssignment)
        self.del_grade_button.clicked.connect(self.delateOneAssignment)

        
    def rboxClick(self, key):
        if key == "cem":
            self.final_input.setPlaceholderText("Enter expected final grade (%)")
            self.cal_buttom.setText("Calculate the final exam mark you need to get")
            self.optionChoose = "cem"
        elif key == "cfm":
            self.final_input.setPlaceholderText("Enter you exam grade (%)")
            self.cal_buttom.setText("Calculate your final grade")
            self.optionChoose = "cfm"

    def calFinalMark(self):
        try:
            mark_before_exam = 0
            for g, w in zip(self.grades, self.weights):
                mark_before_exam += float(g.text()) * float(w.text()) / 100

            if self.optionChoose == "cem":
                if float(self.final_grade_weight_input.text()) != 0:
                    result = (
                        (float(self.final_input.text()) - mark_before_exam)
                        / float(self.final_grade_weight_input.text())
                        / 100
                    )
                result = float(self.final_input.text()) - mark_before_exam
                self.result_label.setText(
                    f"You need to get at least {result:.2f}% on you exam inorder to achieve your expectation."
                )
            elif self.optionChoose == "cfm":
                result = (
                    mark_before_exam
                    + float(self.final_input.text())
                    * float(self.final_grade_weight_input.text())
                    / 100
                )
                self.result_label.setText(f"You final grade is {result:.2f}%")

        except ValueError:
            self.show_error_message(
                "Invalid input", "Please re-check the grades and weight you entered!"
            )

    def createOneAssignment(self):
        layout = QtWidgets.QHBoxLayout()

        assignment_input = QtWidgets.QLineEdit()
        grade_input = QtWidgets.QLineEdit()
        weight_input = QtWidgets.QLineEdit()

        idx = self.vbox.count() - 5

        assignment_input.setPlaceholderText(f"assignment {idx+1}")
        grade_input.setPlaceholderText(f"Grade for assignment {idx+1} (%)")
        weight_input.setPlaceholderText(f"Weight for assignment {idx+1} (%)")

        self.grades.append(grade_input)
        self.weights.append(weight_input)

        layout.addWidget(assignment_input)
        layout.addWidget(grade_input)
        layout.addWidget(weight_input)

        self.vbox.insertLayout(idx,layout)

        return layout

    def delateOneAssignment(self):
        if self.grades:
            # 获取最后一个课程的layout
            last_course_layout = self.vbox.itemAt(self.vbox.count() - 6)  
            
            # 删除这个layout里的所有内容
            while last_course_layout.count():
                item = last_course_layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()
            
            # 移除这个layout
            self.vbox.removeItem(last_course_layout)

            # 删除lst中的内容
            del self.grades[-1]
            del self.weights[-1]

    # 错误提示框
    def show_error_message(self, title, message):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle(title)  # 标题
        msg.setText(message)  # 信息
        msg.setIcon(QtWidgets.QMessageBox.Critical)  # 类型 错误
        msg.addButton(QtWidgets.QMessageBox.Ok)

        msg.exec_()


if __name__ == "__main__":
    import sys
    
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.resize(800, 300)
    qr = win.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    win.move(qr.topLeft())
    
    ui = GradeCalculator()
    ui.setupUi(win)
    
    win.show()
    sys.exit(app.exec_())