#!/usr/bin/env python3
# coding=utf-8

import sys
from random import randint

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)  # загрузка формы в py-скрипт

        self.setWindowTitle('Работа с визуальными табличными данными в Python')
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.btn_random_number.clicked.connect(self.fill_random_numbers)
        self.btn_solve.clicked.connect(self.solve)

    def fill_random_numbers(self):
        """
        Метод для кнопки "Заполнить случайными числами"
        Случайные числа от 1 до 100
        """
        row = 0
        col = 0
        while row < self.tableWidget.rowCount():
            while col < self.tableWidget.columnCount():
                random_num = randint(0, 101)
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(random_num)))
                col += 1
            row += 1
            col = 0

    def solve(self):
        """
        Метод для кнопки "Выполнить задание"
        """
        sum_row2 = self.find_sum_row2()
        self.label_info.setText(sum_row2.__str__())
        if sum_row2 > 200:
            self.find_mod_col3()

    def find_sum_row2(self):
        """
        Поиск суммы чисел во второй строке
        :return: сумма чисел во второй строке
        """
        sum_row2 = 0
        row = 1
        col = 0
        while col < self.tableWidget.columnCount():
            number = float(self.tableWidget.item(row, col).text())
            sum_row2 = sum_row2 + number
            col += 1
        return sum_row2

    def find_mod_col3(self):
        """
        Увеличение чисел второго столбца на два
        """
        row = 0
        col = 2
        while row < self.tableWidget.rowCount():
            number = float(self.tableWidget.item(row, col).text())
            number = number * 2
            self.tableWidget.setItem(row, col, QTableWidgetItem(str(number)))
            row += 1


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
