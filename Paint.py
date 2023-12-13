import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from untitled import Ui_MainWindow
from resize import Ui_MainWindow as resizer
from queue import Queue


# Диалоговое окно для выбора размера
class DialogButton(QMainWindow, QDialog, resizer):
    def __init__(self, weight_for_dialog, height_for_dialog):
        super().__init__()
        self.setupUi(self)
        self.wfd = weight_for_dialog
        self.hfd = height_for_dialog
        self.d = self.wfd / self.hfd
        self.setWindowTitle("Изменить размер")
        self.buttonBox.accepted.connect(self.closed)
        self.buttonBox.rejected.connect(self.close)
        self.radioButton_2.clicked.connect(self.pixels)
        self.radioButton.clicked.connect(self.procents)
        self.checkBox.clicked.connect(self.all)
        self.lineEdit.textEdited.connect(self.prop)
        self.lineEdit_2.textEdited.connect(self.prop2)
        self.is_closed = True

    def closed(self):
        self.is_closed = False
        self.w = int(self.lineEdit.text())
        self.h = int(self.lineEdit_2.text())
        self.is_rb = self.radioButton.isChecked()
        self.close()

    def pixels(self):
        self.lineEdit.setText(str(self.wfd))
        self.lineEdit_2.setText(str(self.hfd))

    def procents(self):
        self.lineEdit.setText('100')
        self.lineEdit_2.setText('100')

    def all(self):
        self.prop()

    def prop(self):
        if self.checkBox.isChecked() and self.radioButton_2.isChecked():
            self.lineEdit_2.setText(str(
                int(int(self.lineEdit.text()) / self.d)))
        elif self.checkBox.isChecked():
            self.lineEdit_2.setText(self.lineEdit.text())

    def prop2(self):
        if self.checkBox.isChecked() and self.radioButton_2.isChecked():
            self.lineEdit.setText(str(
                int(int(self.lineEdit_2.text()) / self.d)))
        elif self.checkBox.isChecked():
            self.lineEdit.setText(self.lineEdit_2.text())


class Paint(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.settings()

    # Настройка всех параметров виджетов
    def settings(self):
        self.is_filled = False
        self.is_saved = True
        self.size_of_fill = 10
        self.path_to_file = ''
        self.pushButton_6.clicked.connect(self.size_of_image)
        self.pm = QPoint(0, self.menubar.height())
        self.action_2.triggered.connect(self.create_new_image)
        self.action_3.triggered.connect(self.open_image)
        self.action_4.triggered.connect(self.save_image)
        self.action_5.triggered.connect(self.save_new_image)
        self.btn_from_palette = 70
        self.ch = 0
        self.drawing = False
        self.lastPoint = QPoint()
        self.type = 10
        self.image = QPixmap("start_image.png").scaled(self.label.size())
        self.name = "Безымянный"
        self.setWindowTitle('Paint: ' + self.name)
        self.label.setPixmap(self.image)
        self.verticalSlider.setValue(9)
        self.is_slider = False
        self.is_btn46 = True
        self.label_3.setVisible(False)
        self.label_3.setStyleSheet("background-color: lightgrey; "
                                   "border-color: grey; "
                                   "border-style: outset;"
                                   "border-width: 2px;")
        self.verticalSlider.setVisible(False)
        self.is_rotate = False
        self.pushButton_2.setVisible(False)
        self.pushButton_3.setVisible(False)
        self.pushButton_4.setVisible(False)
        self.pushButton_5.setVisible(False)
        self.pushButton_7.setVisible(False)
        self.pushButton_2.clicked.connect(self.r90r)
        self.pushButton_3.clicked.connect(self.r90l)
        self.pushButton_4.clicked.connect(self.r180)
        self.pushButton_7.clicked.connect(self.over)
        self.pushButton_5.clicked.connect(self.ohor)
        self.label_6.setVisible(False)
        self.label_6.setStyleSheet("background-color: lightgrey; "
                                   "border-color: grey; "
                                   "border-style: outset;"
                                   "border-width: 2px;")
        self.pushButton_43.clicked.connect(self.thickness)
        self.pushButton.clicked.connect(self.rotate)
        self.pushButton_46.setEnabled(False)
        self.pushButton_46.clicked.connect(self.color1)
        self.pushButton_48.clicked.connect(self.color2)
        self.pushButton_81.setText("Изменение\nцветов")
        self.pushButton_46.setText("\n\nЦвет 1")
        self.pushButton_48.setText("\n\nЦвет 2")
        self.label_4.setStyleSheet("background-color: rgb(0, 0, 0); "
                                   "border-color: black; "
                                   "border-style: outset;"
                                   "border-width: 1px;")
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255); "
                                   "border-color: black; "
                                   "border-style: outset;"
                                   "border-width: 1px;")
        self.set_colors(self.pushButton_50, (0, 0, 0))
        self.set_colors(self.pushButton_51, (128, 128, 128))
        self.set_colors(self.pushButton_52, (128, 0, 0))
        self.set_colors(self.pushButton_53, (255, 0, 0))
        self.set_colors(self.pushButton_54, (255, 128, 0))
        self.set_colors(self.pushButton_55, (255, 255, 0))
        self.set_colors(self.pushButton_56, (0, 128, 0))
        self.set_colors(self.pushButton_57, (0, 128, 128))
        self.set_colors(self.pushButton_58, (0, 0, 255))
        self.set_colors(self.pushButton_59, (128, 0, 128))
        self.set_colors(self.pushButton_60, (255, 255, 255))
        self.set_colors(self.pushButton_61, (192, 192, 192))
        self.set_colors(self.pushButton_62, (185, 122, 87))
        self.set_colors(self.pushButton_63, (255, 128, 128))
        self.set_colors(self.pushButton_64, (255, 201, 14))
        self.set_colors(self.pushButton_65, (239, 228, 176))
        self.set_colors(self.pushButton_66, (181, 230, 29))
        self.set_colors(self.pushButton_67, (153, 217, 234))
        self.set_colors(self.pushButton_68, (112, 146, 190))
        self.set_colors(self.pushButton_69, (200, 191, 231))
        self.pushButton_81.clicked.connect(self.set_palette)
        for i in range(50, 80):
            eval(f'self.pushButton_{i}.clicked'
                 f'.connect(self.set_color_for_pen)')
        for i in range(10):
            eval(f"self.pushButton_{70 + i}.setEnabled(False)")
        self.pushButton_10.setEnabled(False)
        self.current_btn = self.pushButton_10
        for i in range(10, 14):
            eval(f'self.pushButton_{i}.clicked'
                 f'.connect(self.type_of_paint)')

    # Вызов выбора размера
    def size_of_image(self):
        self.dialog = DialogButton(self.label.width(), self.label.height())
        self.dialog.show()
        self.dialog.closeEvent = self.clevent

    # само изменение размера
    def clevent(self, event):
        if not self.dialog.is_closed:
            if self.dialog.is_rb:
                w = int(self.dialog.w * self.label.width() / 100)
                h = int(self.dialog.h * self.label.height() / 100)
            else:
                w = int(self.dialog.w)
                h = int(self.dialog.h)
            self.label.resize(w, h)
            self.image = self.image.scaled(w, h)
            self.label.setPixmap(self.image)

    # выбор типа рисования
    def type_of_paint(self):
        btn = self.sender()
        btn.setEnabled(False)
        self.type = int(btn.objectName()[-2:])
        self.current_btn.setEnabled(True)
        self.current_btn = btn

    # создание нового изображения
    def create_new_image(self):
        if not self.is_saved:
            msgBox = QMessageBox()
            msgBox.setWindowTitle('Paint')
            savebutton = msgBox.addButton('Сохранить', QMessageBox.AcceptRole)
            unsavebutton = msgBox.addButton('Не сохранять',
                                            QMessageBox.DestructiveRole)
            msgBox.addButton("Отмена", QMessageBox.RejectRole)
            msgBox.setText(f"Вы хотите сохранить "
                           f"изменения в файле\n{self.name}")
            font = QFont("Calibri", 13)
            msgBox.setFont(font)
            msgBox.exec_()
            if msgBox.clickedButton() == savebutton:
                fname = QFileDialog.getSaveFileName(
                    self, 'Сохранить изображение', '',
                    'Картинка (*.jpg);;Картинка (*.png);;Все файлы (*)')[0]
                self.image.save(fname)
                self.image = QPixmap("start_image.png")\
                    .scaled(self.label.size())
                self.name = "Безымянный"
                self.setWindowTitle('Paint: ' + self.name)
                self.label.setPixmap(self.image)
            elif msgBox.clickedButton() == unsavebutton:
                self.image = QPixmap("start_image.png")\
                    .scaled(self.label.size())
                self.label.setPixmap(self.image)
                self.name = "Безымянный"
                self.setWindowTitle('Paint: ' + self.name)
        else:
            self.image = QPixmap("start_image.png")\
                .scaled(self.label.size())
            self.label.setPixmap(self.image)
            self.name = "Безымянный"
            self.setWindowTitle('Paint: ' + self.name)

    # открытие изображения
    def open_image(self):
        if not self.is_saved:
            msgBox = QMessageBox()
            msgBox.setWindowTitle('Paint')
            savebutton = msgBox.addButton('Сохранить', QMessageBox.AcceptRole)
            unsavebutton = msgBox.addButton('Не сохранять',
                                            QMessageBox.DestructiveRole)
            msgBox.addButton("Отмена", QMessageBox.RejectRole)
            msgBox.setText(f"Вы хотите сохранить "
                           f"изменения в файле\n{self.name}")
            font = QFont("Calibri", 13)
            msgBox.setFont(font)
            msgBox.exec_()
            if msgBox.clickedButton() == savebutton:
                fname = QFileDialog.getSaveFileName(
                    self, 'Сохранить изображение', '',
                    'Картинка (*.jpg);;Картинка (*.png);;Все файлы (*)')[0]
                self.image.save(fname)
            if msgBox.clickedButton() == savebutton\
                    or msgBox.clickedButton() == unsavebutton:
                self.path_to_file = QFileDialog.getOpenFileName(
                    self, 'Открыть изображение', '',
                    'Картинка (*.jpg);;Картинка (*.png);;Все файлы (*)')[0]
                self.image = QPixmap(self.path_to_file)\
                    .scaled(self.label.size())
                self.name = self.path_to_file.split('/')[-1].split('.')[0]
                self.setWindowTitle('Paint: ' + self.name)
                self.label.setPixmap(self.image)
        else:
            self.path_to_file = QFileDialog.getOpenFileName(
                self, 'Открыть изображение', '',
                'Картинка (*.jpg);;Картинка (*.png);;Все файлы (*)')[0]
            self.image = QPixmap(self.path_to_file)\
                .scaled(self.label.size())
            self.name = self.path_to_file.split('/')[-1].split('.')[0]
            self.setWindowTitle('Paint: ' + self.name)
            self.label.setPixmap(self.image)

    # сохранение изображения
    def save_image(self):
        if bool(self.path_to_file):
            self.image.save(self.path_to_file)
        else:
            fname = QFileDialog.getSaveFileName(
                self, 'Сохранить изображение', '',
                'Картинка (*.jpg);;Картинка (*.png);;Все файлы (*)')[0]
            self.name = fname.split('/')[-1].split('.')[0]
            self.setWindowTitle('Paint: ' + self.name)
            self.image.save(fname)

    # сохранение изображения как...
    def save_new_image(self):
        fname = QFileDialog.getSaveFileName(
            self, 'Сохранить изображение', '',
            'Картинка (*.jpg);;Картинка (*.png);;Все файлы (*)')[0]
        self.name = fname.split('/')[-1].split('.')[0]
        self.setWindowTitle('Paint: ' + self.name)
        self.image.save(fname)

    # выбор собственного цвета кисти
    def set_palette(self):
        color = QColorDialog.getColor()
        for i in range(70, 79):
            eval(f'self.pushButton_{i}.setStyleSheet'
                 f'(self.pushButton_{i + 1}.styleSheet())')
        rgb_color = \
            f'rgb({color.red()}, {color.green()}, {color.blue()})'
        self.set_colors(self.pushButton_79,
                        (color.red(), color.green(), color.blue()))
        eval(f'self.label_{5 - int(self.is_btn46)}.setStyleSheet' +
             f'(\'background-color: \' + rgb_color + \';\' + \';\''
             f'.join(self.label_{5 - int(self.is_btn46)}'
             f'.styleSheet().split(\';\')[1:]))')

    # изменение цвета кисти
    def set_color_for_pen(self):
        btn = self.sender()
        style = btn.styleSheet()
        color = style[(style.index(':') + 2):style.index(';')]
        eval(f'self.label_{5 - int(self.is_btn46)}.setStyleSheet' +
             f'(\'background-color: \' + color + \';\' + \';\''
             f'.join(self.label_{5 - int(self.is_btn46)}'
             f'.styleSheet().split(\';\')[1:]))')

    # функция для оптимизации настройки палитры
    def set_colors(self, btn, color):
        btn.setStyleSheet(f"background-color: rgb"
                          f"({color[0]}, {color[1]}, {color[2]});"
                          f"border-style: outset;"
                          f"border-width: 1px;"
                          f"border-color: white;")
        btn.setEnabled(True)

    # рисование цветом 1
    def color1(self):
        self.pushButton_46.setEnabled(False)
        self.pushButton_48.setEnabled(True)
        self.is_btn46 = True

    # рисование цветом 2
    def color2(self):
        self.pushButton_48.setEnabled(False)
        self.pushButton_46.setEnabled(True)
        self.is_btn46 = False

    # открытие/закрытие изменения толщины
    def thickness(self):
        if not self.is_slider:
            self.label_3.setVisible(True)
            self.verticalSlider.setVisible(True)
            self.is_slider = True
        else:
            self.is_slider = False
            self.label_3.setVisible(False)
            self.verticalSlider.setVisible(False)

    # открытие/закрытие поворота изображения
    def rotate(self):
        if not self.is_rotate:
            self.label_6.setVisible(True)
            self.pushButton_2.setVisible(True)
            self.pushButton_3.setVisible(True)
            self.pushButton_4.setVisible(True)
            self.pushButton_5.setVisible(True)
            self.pushButton_7.setVisible(True)
            self.is_rotate = True
        else:
            self.is_rotate = False
            self.label_6.setVisible(False)
            self.pushButton_2.setVisible(False)
            self.pushButton_3.setVisible(False)
            self.pushButton_4.setVisible(False)
            self.pushButton_5.setVisible(False)
            self.pushButton_7.setVisible(False)

    # поворот изображения вправо на 90 градусов
    def r90r(self):
        self.image = self.image.transformed(
            QTransform().rotate(90), Qt.SmoothTransformation)
        self.label.resize(self.image.width(), self.image.height())
        self.label.setPixmap(self.image)

    # поворот на 90 градусов влево
    def r90l(self):
        self.image = self.image.transformed(
            QTransform().rotate(270), Qt.SmoothTransformation)
        self.label.resize(self.image.width(), self.image.height())
        self.label.setPixmap(self.image)

    # поворот на 180 градусов
    def r180(self):
        self.image = self.image.transformed(
            QTransform().rotate(180), Qt.SmoothTransformation)
        self.label.setPixmap(self.image)

    # отражение по вертикали
    def over(self):
        img = self.image.toImage()
        self.image = QPixmap().fromImage(
            img.mirrored(horizontal=False, vertical=True))
        self.label.setPixmap(self.image)

    # отражение по горизонтали
    def ohor(self):
        img = self.image.toImage()
        self.image = QPixmap().fromImage(
            img.mirrored(horizontal=True, vertical=False))
        self.label.setPixmap(self.image)

    # проверка для заливки
    def check(self, x, y, color):
        is_rect = 2
        if [x, y] in self.rects:
            is_rect = 1
        else:
            for i in range(x, x + self.size_of_fill):
                for j in range(y, y + self.size_of_fill):
                    if self.pixel_hunt.pixelColor(i, j) != color:
                        is_rect = 0
                        break
                if is_rect == 0:
                    break
        return is_rect

    def mousePressEvent(self, event):
        # исчезновение "виджета" изменения толщины и поворота
        if self.is_slider:
            self.label_3.setVisible(False)
            self.verticalSlider.setVisible(False)
            self.is_slider = False
            self.lastPoint = event.pos() - self.label.pos() - self.pm
        elif self.is_rotate:
            self.is_rotate = False
            self.label_6.setVisible(False)
            self.pushButton_2.setVisible(False)
            self.pushButton_3.setVisible(False)
            self.pushButton_4.setVisible(False)
            self.pushButton_5.setVisible(False)
            self.pushButton_7.setVisible(False)
            self.lastPoint = event.pos() - self.label.pos() - self.pm
        else:
            # карандаш
            if self.type == 10:
                self.lastPoint = event.pos() - self.label.pos() - self.pm
                painter = QPainter(self.image)
                if event.buttons() == Qt.LeftButton:
                    style = self.label_4.styleSheet()
                elif event.buttons() == Qt.RightButton:
                    style = self.label_5.styleSheet()
                else:
                    self.lastPoint = QPoint()
                    return
                self.color = eval(
                    'QColor' + style[(style.index(':') + 5):style.index(';')])
                painter.setPen(QPen(self.color, (
                        self.verticalSlider.value() + 2) // 2, Qt.SolidLine))
                painter.drawPoint(event.pos() - self.label.pos() - self.pm)
                self.lastPoint = event.pos() - self.label.pos() - self.pm
                self.label.setPixmap(self.image)
                self.is_saved = False
            # стерка
            elif self.type == 11:
                painter = QPainter(self.image)
                painter.setPen(Qt.white)
                painter.setBrush(Qt.white)
                rect = QRect(event.x() - self.label.x() -
                             (self.verticalSlider.value() + 2) // 4,
                             event.y() - self.label.y() - self.menubar.height() -
                             (self.verticalSlider.value() + 2) // 4,
                             (self.verticalSlider.value() + 2) // 2,
                             (self.verticalSlider.value() + 2) // 2)
                painter.drawRect(rect)
                self.label.setPixmap(self.image)
                self.is_saved = False
            # долгая заливка
            elif self.type == 13:
                x = event.x() - self.label.x()
                y = event.y() - self.label.y() - self.menubar.height()
                points = []
                self.rects = []
                self.pixel_hunt = self.image.toImage()
                color = self.pixel_hunt.pixelColor(x, y)
                if event.buttons() == Qt.LeftButton:
                    style = self.label_4.styleSheet()
                elif event.buttons() == Qt.RightButton:
                    style = self.label_5.styleSheet()
                else:
                    self.lastPoint = QPoint()
                    return
                if color == eval('QColor' + style[(
                        style.index(':') + 5):style.index(';')]):
                    return
                # очереедь для прямоугольников
                q = Queue()
                # очередь для точек
                q2 = Queue()
                is_check = self.check(x, y, color)
                if is_check == 2:
                    self.rects.append([x, y])
                    q.put([x + self.size_of_fill, y])
                    q.put([x - self.size_of_fill, y])
                    q.put([x, y + self.size_of_fill])
                    q.put([x, y - self.size_of_fill])
                else:
                    for i in range(x, x + self.size_of_fill):
                        for j in range(y, y + self.size_of_fill):
                            if self.pixel_hunt.pixelColor(i, y) == color:
                                q2.put([i, j])
                                points.append([i, j])
                # здесь я обходом в ширину проверяю,
                # можно ли поставить квадрат указанных
                # размеров. Если да, то после цикла я
                # его рисую. Иначе я добавляю в другую
                # очередб точки.
                while not q.empty():
                    x, y = q.get()
                    y += self.size_of_fill
                    check_rect = self.check(x, y, color)
                    if check_rect == 2:
                        q.put([x, y])
                        self.rects.append([x, y])
                    elif check_rect == 0:
                        for i in range(x, x + self.size_of_fill):
                            if self.pixel_hunt.pixelColor(i, y) == color:
                                q2.put([i, y])
                                points.append([i, y])
                    y -= self.size_of_fill * 2
                    check_rect = self.check(x, y, color)
                    if check_rect == 2:
                        q.put([x, y])
                        self.rects.append([x, y])
                    elif check_rect == 0:
                        y += (self.size_of_fill - 1)
                        for i in range(x, x + self.size_of_fill):
                            if self.pixel_hunt.pixelColor(i, y) == color:
                                q2.put([i, y])
                                points.append([i, y])
                        y -= (self.size_of_fill - 1)
                    y += self.size_of_fill
                    x += self.size_of_fill
                    check_rect = self.check(x, y, color)
                    if check_rect == 2:
                        q.put([x, y])
                        self.rects.append([x, y])
                    elif check_rect == 0:
                        for i in range(y, y + self.size_of_fill):
                            if self.pixel_hunt.pixelColor(x, i) == color:
                                q2.put([x, i])
                                points.append([x, i])
                    x -= self.size_of_fill * 2
                    check_rect = self.check(x, y, color)
                    if check_rect == 2:
                        q.put([x, y])
                        self.rects.append([x, y])
                    elif check_rect == 0:
                        x += self.size_of_fill - 1
                        for i in range(y, y + self.size_of_fill):
                            if self.pixel_hunt.pixelColor(x, i) == color:
                                q2.put([x, i])
                                points.append([x, i])
                painter = QPainter(self.image)
                if event.buttons() == Qt.LeftButton:
                    style = self.label_4.styleSheet()
                elif event.buttons() == Qt.RightButton:
                    style = self.label_5.styleSheet()
                else:
                    self.lastPoint = QPoint()
                    return
                color2 = eval(
                    'QColor' + style[(style.index(':') + 5):style.index(';')])
                painter.setBrush(color2)
                painter.setPen(QPen(color2))
                # само рисование квадратов
                for i in self.rects:
                    rect_fill = QRect(
                        i[0], i[1], self.size_of_fill, self.size_of_fill)
                    painter.drawRect(rect_fill)
                self.pixel_hunt = self.image.toImage()
                sof = self.size_of_fill
                self.size_of_fill = 1
                # обзод в ширину точек
                while not q2.empty():
                    x, y = q2.get()
                    y += self.size_of_fill
                    if [x, y] not in points and \
                            self.pixel_hunt.pixelColor(x, y) == color:
                        points.append([x, y])
                        q2.put([x, y])
                    y -= self.size_of_fill * 2
                    if [x, y] not in points and \
                            self.pixel_hunt.pixelColor(x, y) == color:
                        points.append([x, y])
                        q2.put([x, y])
                    y += self.size_of_fill
                    x += self.size_of_fill
                    if [x, y] not in points and \
                            self.pixel_hunt.pixelColor(x, y) == color:
                        points.append([x, y])
                        q2.put([x, y])
                    x -= self.size_of_fill * 2
                    if [x, y] not in points and \
                            self.pixel_hunt.pixelColor(x, y) == color:
                        points.append([x, y])
                        q2.put([x, y])
                self.size_of_fill = sof
                # само рисование точек
                for i in points:
                    point = QPoint(i[0], i[1])
                    painter.drawPoint(point)
                self.label.setPixmap(self.image)
                self.is_saved = False

    def mouseMoveEvent(self, event):
        # здесь все то же, что и в MousePressEvent
        if not self.is_slider and not self.is_rotate:
            if not bool(self.lastPoint):
                self.lastPoint = event.pos() - self.label.pos() - self.pm
            else:
                if self.type == 10:
                    painter = QPainter(self.image)
                    if event.buttons() == Qt.LeftButton:
                        style = self.label_4.styleSheet()
                    elif event.buttons() == Qt.RightButton:
                        style = self.label_5.styleSheet()
                    else:
                        self.lastPoint = QPoint()
                        return
                    color = eval(
                        'QColor' +
                        style[(style.index(':') + 5):style.index(';')])
                    painter.setPen(QPen(color, (
                            self.verticalSlider.value() + 2) / 2,
                                        Qt.SolidLine))
                    line = QLine(self.lastPoint,
                                 event.pos() - self.label.pos() - self.pm)
                    painter.drawLine(line)
                    self.lastPoint = event.pos() - self.label.pos()
                    self.lastPoint -= self.pm
                    self.label.setPixmap(self.image)
                    self.is_saved = False
                elif self.type == 11:
                    painter = QPainter(self.image)
                    painter.setPen(QPen(Qt.white, (
                            self.verticalSlider.value() + 2) // 2,
                                        Qt.SolidLine))
                    line = QLineF(self.lastPoint,
                                  event.pos() - self.label.pos() - self.pm)
                    painter.drawLine(line)
                    self.lastPoint = event.pos() - self.label.pos() - self.pm
                    self.label.setPixmap(self.image)
                    self.is_saved = False
                elif self.type == 13 and not self.is_filled:
                    self.is_filled = True
                    x = event.x() - self.label.x()
                    y = event.y() - self.label.y() - self.menubar.height()
                    points = []
                    self.rects = []
                    self.pixel_hunt = self.image.toImage()
                    color = self.pixel_hunt.pixelColor(x, y)
                    if event.buttons() == Qt.LeftButton:
                        style = self.label_4.styleSheet()
                    elif event.buttons() == Qt.RightButton:
                        style = self.label_5.styleSheet()
                    else:
                        self.lastPoint = QPoint()
                        return
                    if color == eval('QColor' + style[(
                            style.index(':') + 5):style.index(';')]):
                        return
                    q = Queue()
                    q2 = Queue()
                    is_check = self.check(x, y, color)
                    if is_check == 2:
                        self.rects.append([x, y])
                        q.put([x + self.size_of_fill, y])
                        q.put([x - self.size_of_fill, y])
                        q.put([x, y + self.size_of_fill])
                        q.put([x, y - self.size_of_fill])
                    else:
                        for i in range(x, x + self.size_of_fill):
                            for j in range(y, y + self.size_of_fill):
                                if self.pixel_hunt.pixelColor(i, y) == color:
                                    q2.put([i, j])
                                    points.append([i, j])
                    while not q.empty():
                        x, y = q.get()
                        y += self.size_of_fill
                        check_rect = self.check(x, y, color)
                        if check_rect == 2:
                            q.put([x, y])
                            self.rects.append([x, y])
                        elif check_rect == 0:
                            for i in range(x, x + self.size_of_fill):
                                if self.pixel_hunt.pixelColor(i, y) == color:
                                    q2.put([i, y])
                                    points.append([i, y])
                        y -= self.size_of_fill * 2
                        check_rect = self.check(x, y, color)
                        if check_rect == 2:
                            q.put([x, y])
                            self.rects.append([x, y])
                        elif check_rect == 0:
                            y += (self.size_of_fill - 1)
                            for i in range(x, x + self.size_of_fill):
                                if self.pixel_hunt.pixelColor(i, y) == color:
                                    q2.put([i, y])
                                    points.append([i, y])
                            y -= (self.size_of_fill - 1)
                        y += self.size_of_fill
                        x += self.size_of_fill
                        check_rect = self.check(x, y, color)
                        if check_rect == 2:
                            q.put([x, y])
                            self.rects.append([x, y])
                        elif check_rect == 0:
                            for i in range(y, y + self.size_of_fill):
                                if self.pixel_hunt.pixelColor(x, i) == color:
                                    q2.put([x, i])
                                    points.append([x, i])
                        x -= self.size_of_fill * 2
                        check_rect = self.check(x, y, color)
                        if check_rect == 2:
                            q.put([x, y])
                            self.rects.append([x, y])
                        elif check_rect == 0:
                            x += self.size_of_fill - 1
                            for i in range(y, y + self.size_of_fill):
                                if self.pixel_hunt.pixelColor(x, i) == color:
                                    q2.put([x, i])
                                    points.append([x, i])
                    painter = QPainter(self.image)
                    if event.buttons() == Qt.LeftButton:
                        style = self.label_4.styleSheet()
                    elif event.buttons() == Qt.RightButton:
                        style = self.label_5.styleSheet()
                    else:
                        self.lastPoint = QPoint()
                        return
                    color2 = eval(
                        'QColor' +
                        style[(style.index(':') + 5):style.index(';')])
                    painter.setBrush(color2)
                    painter.setPen(QPen(color2))
                    for i in self.rects:
                        rect_fill = QRect(i[0], i[1],
                                          self.size_of_fill, self.size_of_fill)
                        painter.drawRect(rect_fill)
                    self.pixel_hunt = self.image.toImage()
                    sof = self.size_of_fill
                    self.size_of_fill = 1
                    while not q2.empty():
                        x, y = q2.get()
                        y += self.size_of_fill
                        if [x, y] not in points and \
                                self.pixel_hunt.pixelColor(x, y) == color:
                            points.append([x, y])
                            q2.put([x, y])
                        y -= self.size_of_fill * 2
                        if [x, y] not in points and \
                                self.pixel_hunt.pixelColor(x, y) == color:
                            points.append([x, y])
                            q2.put([x, y])
                        y += self.size_of_fill
                        x += self.size_of_fill
                        if [x, y] not in points and \
                                self.pixel_hunt.pixelColor(x, y) == color:
                            points.append([x, y])
                            q2.put([x, y])
                        x -= self.size_of_fill * 2
                        if [x, y] not in points and \
                                self.pixel_hunt.pixelColor(x, y) == color:
                            points.append([x, y])
                            q2.put([x, y])
                    self.size_of_fill = sof
                    for i in points:
                        point = QPoint(i[0], i[1])
                        painter.drawPoint(point)
                    self.label.setPixmap(self.image)
                    self.is_saved = False

    def mouseReleaseEvent(self, event):
        self.lastPoint = QPoint()
        # пипетка
        if self.type == 12:
            img = self.image.toImage()
            x = event.x() - self.label.x()
            y = event.y() - self.label.y() - self.menubar.height()
            r = img.pixelColor(x, y).red()
            g = img.pixelColor(x, y).green()
            b = img.pixelColor(x, y).blue()
            img.pixelColor(x, y).blue()
            color = f'rgb({r}, {g}, {b})'
            eval(f'self.label_4.setStyleSheet' +
                 f'(\'background-color: \' + color + \';\' + \';\'.join' +
                 f'(self.label_4.styleSheet().split(\';\')[1:]))')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainMenu = Paint()
    mainMenu.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
