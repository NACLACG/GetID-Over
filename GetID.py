import sys
import random
import re
import pyperclip
from PyQt6.QtWidgets import QApplication, QWidget
from OWO import Ui_GetID

IDfile = open('IDS.txt')
with open('IDS.txt', 'r') as f:
    ID = f.read()
print(ID)
# 初始化GetID字符串数组
GetID = []
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
IDfile.close()
IDfile = open('BAN.txt')
with open('BAN.txt', 'r') as f:
    ID = f.read()
print(ID)
# 初始化GetID字符串数组
BanID = []
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
                pyperclip.copy(random.choice(GetID))
            # 如果ID不包含Temp变量的字符串 将字符串写入IDS.txt文件 并添加到GetID数组中
            else:
                with open('IDS.txt', 'a') as f:
                    new_id = '点歌 ' + Temp
                    f.write(new_id + '\n')
                    GetID.append(new_id)
                pyperclip.copy(new_id)
        else:
            pyperclip.copy(random.choice(GetID))

if __name__ == '__main__':
    app = QApplication([])
    Theui =MyUI()
    Theui.show()
    sys.exit(app.exec())