import sys
import random
import re
import pyperclip
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from OWO import Ui_GetID

IDfile = open('IDS.txt')
with open('IDS.txt', 'r') as f:
    ID = f.read()
# 初始化ID字符串数组
GetID = []
BanID = []
Temper = ""
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

class MyUI(QWidget, Ui_GetID):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bind()

    def bind(self):
        self.Get.clicked.connect(self.GetID)

    def GetID(self):
        OTemp = pyperclip.paste()
        # 从OTemp中提取数字字符串
        Temp = ''
        match = re.search(r'id=(\d+)', OTemp)
        if match:
            Temp = match.group(1)
            # 如果ID包含Temp变量的字符串 随机输出GetID数组中的一个元素到剪贴板
            if Temp in ID:
                Temper = random.choice(GetID)
                pyperclip.copy(Temper)
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
                IDfile.close()
                pyperclip.copy(new_id)
        else:
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
                    IDfile.close()
                    self.showget.setText(Temper.replace("\n",""))
                    break

if __name__ == '__main__':
    app = QApplication([])
    Theui =MyUI()
    Theui.show()
    sys.exit(app.exec())
