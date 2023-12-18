from PyQt5 import QtCore, QtGui, QtWidgets


class GPACalculator(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("GPA Calculat")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setFocus()
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.grades = []
        self.credits = []    
        
        for i in range(5):
            course_layout = QtWidgets.QHBoxLayout()
            grade_label = QtWidgets.QLabel(f'Course {i+1} Percentage Grade:')
            course_layout.addWidget(grade_label)
            grade_input = QtWidgets.QLineEdit(self.centralwidget)
            grade_input.setText("85") # 默认分数
            course_layout.addWidget(grade_input)
            self.grades.append(grade_input)
            
            credit_label = QtWidgets.QLabel('Credit Hours:')
            course_layout.addWidget(credit_label)

            credit_input = QtWidgets.QLineEdit(self.centralwidget)
            credit_input.setText("0.5")  # 默认credit
            course_layout.addWidget(credit_input)
            self.credits.append(credit_input)

            self.verticalLayout.addLayout(course_layout)
        
        self.hvbox = QtWidgets.QHBoxLayout()
        self.del_course_button = QtWidgets.QPushButton('- Del Course')
        self.add_course_button = QtWidgets.QPushButton('+ Add Course')

        self.hvbox.addWidget(self.del_course_button)
        self.hvbox.addWidget(self.add_course_button)
        
        self.verticalLayout.addLayout(self.hvbox)

        self.calc_button = QtWidgets.QPushButton('Calculate GPA')
        self.verticalLayout.addWidget(self.calc_button)
        self.result_label = QtWidgets.QLabel('')
        self.verticalLayout.addWidget(self.result_label)
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.event()
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("GPA Calculat", "GPA Calculat"))
    
    def calculate_gpa(self):
        total_gpa = 0
        total_credits = 0
        try:
            for grade, credit in zip(self.grades, self.credits):
                if grade.text() and credit.text():
                    single_gpa = self.grade_to_gpa(float(grade.text()))
                    total_gpa += single_gpa * float(credit.text())
                    total_credits += float(credit.text())
            if not total_credits == 0:
                gpa = total_gpa / total_credits
                self.result_label.setText(f"Your GPA is: {gpa:.2f}")
            else:
                self.show_error_message("No credits entered", "Please enter the credit hours for the courses.")
        except ValueError:
            self.show_error_message("Invalid input", "Please enter valid numbers for grades and credits.")
    
    def event(self):
        self.calc_button.clicked.connect(self.calculate_gpa)
        self.add_course_button.clicked.connect(self.add_course)
        self.del_course_button.clicked.connect(self.del_course)
        
    def grade_to_gpa(self, grade):
        if 85 <= grade:
            return 4.0
        elif 80 <= grade <= 84:
            return 3.7
        elif 77 <= grade <= 79:
            return 3.3
        elif 73 <= grade <= 76:
            return 3.0
        elif 70 <= grade <= 72:
            return 2.7
        elif 67 <= grade <= 69:
            return 2.3
        elif 63 <= grade <= 66:
            return 2.0
        elif 60 <= grade <= 62:
            return 1.7
        elif 57 <= grade <= 59:
            return 1.3
        elif 53 <= grade <= 56:
            return 1.0
        elif 50 <= grade <= 52:
            return 0.7
        elif 0 <= grade <= 49:
            return 0.0
        else:
            return 0.0

    def del_course(self):
        if self.grades:
            # 获取最后一个课程的layout
            last_course_layout = self.verticalLayout.itemAt(self.verticalLayout.count() - 4)  
            
            # 删除这个layout里的所有内容
            while last_course_layout.count():
                item = last_course_layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()
            
            # 移除这个layout
            self.verticalLayout.removeItem(last_course_layout)

            # 删除lst中的内容
            del self.grades[-1]
            del self.credits[-1]


    def add_course(self):
        course_layout = QtWidgets.QHBoxLayout()
        grade_label = QtWidgets.QLabel(f'Course {len(self.grades)+1} Percentage Grade:')
        course_layout.addWidget(grade_label)

        grade_input = QtWidgets.QLineEdit(self.centralwidget)
        grade_input.setText("85")  # 默认分数
        course_layout.addWidget(grade_input)
        self.grades.append(grade_input)

        credit_label = QtWidgets.QLabel('Credit Hours:')
        course_layout.addWidget(credit_label)

        credit_input = QtWidgets.QLineEdit(self.centralwidget)
        credit_input.setText("0.5")  # 默认credit
        course_layout.addWidget(credit_input)
        self.credits.append(credit_input)

        self.verticalLayout.insertLayout(self.verticalLayout.count()-3, course_layout)

    # 错误提示框
    def show_error_message(self, title, message):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle(title)  # 标题
        msg.setText(message) #信息
        msg.setIcon(QtWidgets.QMessageBox.Critical) #类型 错误
        msg.addButton(QtWidgets.QMessageBox.Ok)

        msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.resize(800, 600)
    ui = GPACalculator()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    sys.exit(app.exec_())
