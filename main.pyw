#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

__author__ = "Ilia B. Anosov"
__copyright__ = "Copyright 2017, Debian SSH Backup"
__credits__ = ["Zukhra Miftakhova", "Olesia Lobankova", "Tatiana Anosova"]
__license__ = "gpl-3.0"
__version__ = "1.0.0"
__maintainer__ = "Ilia Anosov"
__email__ = "anosovilya465@yandex.ru"
__status__ = "Development"


class ADSDictator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    # noinspection PyPep8Naming
    def initUI(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ADSDictator()
    ex.show()
    sys.exit(app.exec())
