import sys
import datetime
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer, Qt

class TimePercentageWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
        self.calculate_percentage()

    def init_ui(self):
        self.layout = QVBoxLayout()

        self.year_label = QLabel(self)
        self.year_label.setFont(QFont("Arial", 12))
        self.year_label.setAlignment(Qt.AlignCenter)

        self.month_label = QLabel(self)
        self.month_label.setFont(QFont("Arial", 12))
        self.month_label.setAlignment(Qt.AlignCenter)

        self.day_label = QLabel(self)
        self.day_label.setFont(QFont("Arial", 12))
        self.day_label.setAlignment(Qt.AlignCenter)

        self.layout.addWidget(self.year_label)
        self.layout.addWidget(self.month_label)
        self.layout.addWidget(self.day_label)
        self.setLayout(self.layout)

        self.setWindowTitle('Y.O.L.O.')
        self.setGeometry(300, 300, 350, 200)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)  # 窗口保持在所有程序上方

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.calculate_percentage)
        self.timer.start(100)  # 每秒刷新一次

    def calculate_percentage(self):
        now = datetime.datetime.now()

        # 年度时间百分比
        start_of_year = datetime.datetime(now.year, 1, 1)
        end_of_year = datetime.datetime(now.year + 1, 1, 1)
        passed_time_year = now - start_of_year
        total_time_year = end_of_year - start_of_year
        percentage_year = (passed_time_year.total_seconds() / total_time_year.total_seconds()) * 100
        self.year_label.setText(f"年: {percentage_year:.4f}%")

        # 每月时间百分比
        start_of_month = datetime.datetime(now.year, now.month, 1)
        if now.month == 12:
            end_of_month = datetime.datetime(now.year + 1, 1, 1)
        else:
            end_of_month = datetime.datetime(now.year, now.month + 1, 1)
        passed_time_month = now - start_of_month
        total_time_month = end_of_month - start_of_month
        percentage_month = (passed_time_month.total_seconds() / total_time_month.total_seconds()) * 100
        self.month_label.setText(f"月: {percentage_month:.4f}%")

        # 每日时间百分比
        start_of_day = datetime.datetime(now.year, now.month, now.day)
        end_of_day = start_of_day + datetime.timedelta(days=1)
        passed_time_day = now - start_of_day
        total_time_day = end_of_day - start_of_day
        percentage_day = (passed_time_day.total_seconds() / total_time_day.total_seconds()) * 100
        self.day_label.setText(f"日: {percentage_day:.4f}%")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TimePercentageWidget()
    window.show()
    sys.exit(app.exec_())
