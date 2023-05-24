import sys
import os
import random
import re
import pyperclip
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import QProcess, Qt, QFile, QIODevice
from PyQt6.QtGui import QGuiApplication, QPixmap, QFontDatabase, QFont
from OWO import Ui_GetID
import GetIDFile


IDfile = open('IDS.txt')
with open('IDS.txt', 'r') as f:
    ID = f.read()
# 初始化ID字符串数组
GetID = []
BanID = []
NullList = []
Temper = ""
StillCopy = ""
IDlong = 0
Ltmp = ""
# 处理IDS.txt文件 将每一行的点歌号存入GetID数组
while IDlong >= 0:
    Ltmp = IDfile.readline()
    if Ltmp == "":
        break
    else:
        GetID.append(Ltmp)
        IDlong += 1
IDfile = open('BAN.txt')
with open('BAN.txt', 'r') as f:
    Ban = f.read()
# 初始BanID字符串数组
IDlong = 0
Ltmp = ""
# 处理IDS.txt文件 将每一行的点歌号存入GetID数组
while IDlong >= 0:
    Ltmp = IDfile.readline()
    if Ltmp == "":
        break
    else:
        BanID.append(Ltmp)
        IDlong += 1
IDfile.close()

os.chdir(os.path.dirname(os.path.abspath(__file__)))
class MyUI(QWidget, Ui_GetID):
    def __init__(self):
        super().__init__()
        self.setGeometry(1510, 40, 200, 200)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
        TheFont = QFontDatabase.addApplicationFont(':/EllenMiraMathers/EllenMiraMathers/华康方圆体W7.ttf')
        if TheFont != -1:
            font_family = QFontDatabase.applicationFontFamilies(TheFont)[0]
            font = QFont(font_family)
        self.setupUi(self)
        self.StartALL()
        self.bind()

    def StartALL(self):
        IDfile = open('BAN.txt')
        with open('BAN.txt', 'r') as f:
            Ban = f.read()
        # 初始BanID字符串数组
        IDlong = 0
        Ltmp = ""
        # 处理IDS.txt文件 将每一行的点歌号存入BanID数组
        while IDlong >= 0:
            Ltmp = IDfile.readline()
            if Ltmp == "":
                break
            else:
                BanID.append(Ltmp)
                self.overcopy.addItem(" "+Ltmp.replace("\n", ""))
                IDlong += 1
        IDfile.close()
        print(len(BanID))
        self.lcdNumber.setProperty("value",self.overcopy.count())
        if len(BanID) == len(GetID):
                    self.lcdNumber.setStyleSheet("background-image: url(:/EllenMiraMathers/EllenMiraMathers/Nll.png);\n"
"color: rgb(183, 21, 48);")

    def bind(self):
        self.Get.clicked.connect(self.GetID)
        self.ReSet.clicked.connect(self.ReSetBAN)
        self.getready.clicked.connect(self.StillcopyR)

    def GetID(self):
        OTemp = pyperclip.paste()
        # 从OTemp中提取数字字符串
        Temp = ''
        match = re.search(r'id=(\d+)', OTemp)
        if match:
            Temp = match.group(1)
            # 如果ID包含Temp变量的字符串 随机输出GetID数组中的一个元素到剪贴板
            if len(BanID) < len(GetID):
                self.overcopy.setStyleSheet("color: rgb(174, 174, 176);\n"
"background-image: url(:/EllenMiraMathers/EllenMiraMathers/Nll.png);")
                if Temp in ID:
                    self.showready.setText(Temp.replace("\n", ""))
                    while True:
                        Temper = random.choice(GetID)
                        self.showget.setText(Temper.replace("\n",""))
                        if Temper in Ban:
                            self.showready.setText(Temper.replace("\n",""))
                            continue
                        else:
                            pyperclip.copy(Temper)
                            with open('BAN.txt', 'a') as f:
                                f.write(Temper)
                                BanID.append(Temper)
                                self.overcopy.addItem(" "+Temper.replace("\n",""))
                                self.lcdNumber.setProperty("value",self.overcopy.count())
                                if len(BanID) ==len(GetID):
                                    self.lcdNumber.setStyleSheet("background-image: url(:/EllenMiraMathers/EllenMiraMathers/Nll.png);\n"
    "color: rgb(183, 21, 48);")
                            IDfile.close()
                            self.showget.setText(Temper.replace("\n",""))
                            break
                # 如果ID不包含Temp变量的字符串 将字符串写入IDS.txt文件 并添加到GetID数组中
                else:
                    with open('IDS.txt', 'a') as f:
                        new_id = '点歌 ' + Temp
                        f.write(new_id + '\n')
                        GetID.append(new_id)
                    with open('BAN.txt', 'a') as f:
                        new_id = '点歌 ' + Temp
                        f.write(new_id + '\n')
                        BanID.append(new_id)
                        self.overcopy.addItem(" "+new_id.replace("\n",""))
                        self.lcdNumber.setProperty("value",self.overcopy.count())
                        if len(BanID) ==len(GetID):
                            self.lcdNumber.setStyleSheet("background-image: url(:/EllenMiraMathers/EllenMiraMathers/Nll.png);\n"
    "color: rgb(183, 21, 48);")
                    IDfile.close()
                    pyperclip.copy(new_id)
                    self.showget.setText(new_id.replace("\n",""))
        else:
            if len(BanID) < len(GetID):
                self.overcopy.setStyleSheet("color: rgb(174, 174, 176);\n"
                                            "background-image: url(:/EllenMiraMathers/EllenMiraMathers/Nll.png);")
                while True:
                    Temper = random.choice(GetID)
                    self.showget.setText(Temper.replace("\n",""))
                    if Temper in Ban:
                        self.showready.setText(Temper.replace("\n",""))
                        print(Temper)
                        continue
                    else:
                        pyperclip.copy(Temper)
                        with open('BAN.txt', 'a') as f:
                            f.write(Temper)
                            BanID.append(Temper)
                            self.overcopy.addItem(" "+Temper.replace("\n",""))
                            self.lcdNumber.setProperty("value",self.overcopy.count())
                            if len(BanID) ==len(GetID):
                                self.lcdNumber.setStyleSheet("background-image: url(:/EllenMiraMathers/EllenMiraMathers/Nll.png);\n"
    "color: rgb(183, 21, 48);")
                        IDfile.close()
                        self.showget.setText(Temper.replace("\n",""))
                        break
            else:
                self.lcdNumber.setStyleSheet("background-image: url(:/EllenMiraMathers/EllenMiraMathers/Nll.png);\n"
        "color: rgb(183, 21, 48);")

    def ReSetBAN(self):
        with open('BAN.txt', 'w') as f:
            f.truncate(0)
        IDfile.close()
        os.execl(sys.executable, sys.executable, *sys.argv)

    def StillcopyR(self):
        pyperclip.copy(self.showready.text())

if __name__ == '__main__':
    app = QApplication([])
    Theui = MyUI()
    Theui.show()
    app.exec()
