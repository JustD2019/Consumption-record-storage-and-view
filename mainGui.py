import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pandas as pd
import operator  # 比较模块
import mainWindow, childWin

# 本程序采用pyqt5设计，包含Qcombobox，Qpushbutton，QFileDialog，QdateEdit，QtextBrowser,QlineEdit.QtableWidget,Qmessagebox,Qmenu

#实例化主窗口
class parentWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = mainWindow.Ui_MainWindow()
        self.ui.setupUi(self)

        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        # 创建QMenu信号事件
        self.customContextMenuRequested.connect(self.showMenu)

    def showMenu(self, pos):
        menu = QMenu()
        menu1 = menu.addAction('打开文件')
        menu2 = menu.addAction('创建文件')
        menu1.triggered.connect(Open_File)
        menu2.triggered.connect(Create_File)
        #在鼠标点击位置显示右键菜单
        menu.exec_(QCursor.pos())


# 实例化第二个窗口
class childWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child_ui = childWin.Ui_Dialog()
        self.child_ui.setupUi(self)

class F_P:
    File_Path = ''

    
def Open_File():
    main_ui.ui.type_cb.clear()  # 初始化下拉选项
    file_path = QFileDialog.getOpenFileName(None, 'Open file', '', 'Excel files (*.csv)')  # 打开文件
    F_P.File_Path = file_path[0]
    main_ui.ui.textBrowser.setText(F_P.File_Path)  # 为文本浏览框显示当前选择的文件路径

    if len(F_P.File_Path) > 0:
        try:
            cb_data = pd.read_csv(F_P.File_Path, encoding='gbk')
            # 删除首列作为行索引的【消费日期】，把余下可存储类型显示到ComboBox上
            new_cb = cb_data.columns.values.tolist()
            new_cb.remove(cb_data.columns.values.tolist()[0])
            main_ui.ui.type_cb.addItems(new_cb)  # 添加下拉选项内容

        except Exception:
            F_P.File_Path = ''
            QMessageBox.warning(None, '错误', '文件错误!', QMessageBox.Close)
    else:
        pass


def Read_File():
    if len(F_P.File_Path) > 0:
        output_data = pd.read_csv(F_P.File_Path, encoding='gbk')
        # 通过shape获取文件拥有的行数和列数,shape输出为（行，列）
        output_data_rows = output_data.shape[0]
        output_data_columns = output_data.shape[1]

        # 通过columns.values.tolist()获取表格头
        output_data_header = output_data.columns.values.tolist()

        # 设置tableWidget的行列及列名称
        main_ui.ui.tableWidget.setColumnCount(output_data_columns)
        main_ui.ui.tableWidget.setRowCount(output_data_rows)
        main_ui.ui.tableWidget.setHorizontalHeaderLabels(output_data_header)
        # 通过遍历把数据输出到tableWidget上
        for i in range(output_data_rows):
            output_data_rows_values = output_data.iloc[i]  # 获取每行数据

            for j in range(output_data_columns):
                out_items_list = output_data_rows_values[j]  # 获取对应行相应列的数据

                # 将遍历的数据放tablewidget显示
                out_items_lists = str(out_items_list)
                newItem = QTableWidgetItem(out_items_lists)
                main_ui.ui.tableWidget.setItem(i, j, newItem)
        main_ui.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)    #设置表格不能修改
    else:
        reply = QMessageBox.information(None, '错误', '您没有选择文件!是否选择文件？', QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            Open_File()
            Read_File()
        else:
            pass


def save_data():
    save_Date = main_ui.ui.dateEdit.date().toString(Qt.ISODate)  # 获取dataEdit的当前日期
    save_money = main_ui.ui.money_le.text()  # 获取lineEdit中输入的数据
    save_type = main_ui.ui.type_cb.currentText()  # 获取ComboBox中选择的数据
    if len(F_P.File_Path) > 0:
        df = pd.read_csv(F_P.File_Path, encoding='gbk', index_col='消费日期').sort_index()
        try:
            float(save_money)
            if save_type == '消费总额':
                df.loc[save_Date, ['消费总额']] = save_money
                df = df.fillna(0)  # 把缺失值定为0

                df = df.sort_index()  # 按照索引进行排序

                df.to_csv(F_P.File_Path, encoding='gbk')
                main_ui.ui.money_le.setText('')
                Read_File()
            else:
                df.loc[save_Date, [save_type]] = save_money
                df = df.fillna(0)
                # 选择存储消费项目列
                new = df.columns.values.tolist()
                new.remove(df.columns.values.tolist()[0])
                # 计算当日消费总金额
                money = df.loc[save_Date, new]
                sum_money = 0
                for i in range(len(money)):
                    sum_money += float(money[i])
                df.loc[save_Date, ['消费总额']] = sum_money
                df = df.sort_index()
                df.to_csv(F_P.File_Path, encoding='gbk')
                main_ui.ui.money_le.setText('')
                Read_File()
        except ValueError:
            QMessageBox.warning(None, '错误提示', '您输入的存储金额为非数字类型,请重新输入!', QMessageBox.Ok)
            main_ui.ui.money_le.setText('')
    else:
        QMessageBox.warning(None, '错误提示', '您还没有选择文件，无法进行存储操作', QMessageBox.Ok)


def Create_File():
    main_ui.ui.type_cb.clear()
    F_P.File_Path = ''
    save_path = QFileDialog.getSaveFileName(None, 'Create file', 'D:\\', 'Excel files (*.csv)')  # 创建保存文件
    F_P.File_Path = save_path[0]
    main_ui.ui.textBrowser.setText(F_P.File_Path)  # 为文本浏览框显示当前选择的文件路径
    # 通过判断文件是否有路径来推出是否创建了文件
    if len(F_P.File_Path) > 0:
        # 自定义消息提示框
        messageBox = QMessageBox()
        messageBox.setWindowTitle('文件提示')
        messageBox.setText('我们已经为您准备好了存储列【消费日期,消费总额,吃喝消费,购物消费,其他消费】，是否启用？')
        messageBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Close)
        buttonY = messageBox.button(QMessageBox.Yes)
        buttonY.setText('启用')
        buttonN = messageBox.button(QMessageBox.No)
        buttonN.setText('自定义')
        buttonC = messageBox.button(QMessageBox.Close)
        buttonC.setText('下次一定')
        messageBox.exec_()

        if messageBox.clickedButton() == buttonY:
            column_name = pd.DataFrame(['消费日期', '消费总额', '吃喝消费', '购物消费', '其他消费']).T
            column_name.to_csv(save_path[0], header=None, index=False, encoding='gbk')

            cb_data = pd.read_csv(F_P.File_Path, encoding='gbk')
            # 删除首列作为行索引的【消费日期】，把余下可存储类型显示到ComboBox上
            new_cb = cb_data.columns.values.tolist()
            new_cb.remove(cb_data.columns.values.tolist()[0])
            main_ui.ui.type_cb.addItems(new_cb)  # 添加下拉选项内容

        # 显示第二个存储自定义列名的新窗口
        elif messageBox.clickedButton() == buttonN:
            child = childWindow()
            child.show()

            # 把定义的列存储进新文件
            def new_type():
                save_columns = []
                save_columns.append(child.child_ui.type_input1.text())
                save_columns.append(child.child_ui.type_input2.text())
                new_columns = child.child_ui.type_input3.text().split(' ')

                for i in range(len(new_columns)):
                    save_columns.append(new_columns[i])

                set_columns = set(save_columns)
                # 判断是否自定义了重复的列名
                if len(set_columns) != len(save_columns):
                    QMessageBox.warning(None, '错误提示', '请不要输入重复的列名!', QMessageBox.Ok)
                    clear_columns()
                else:
                    # 写入自定义列名
                    column_name = pd.DataFrame(save_columns).T
                    column_name.to_csv(save_path[0], header=None, index=False, encoding='gbk')

                    # 在ComboBox显示列名
                    cb_data = pd.read_csv(F_P.File_Path, encoding='gbk')
                    # 删除首列作为行索引的【消费日期】，把余下可存储类型显示到ComboBox上
                    new_cb = cb_data.columns.values.tolist()

                    if operator.eq(save_columns, new_cb):  # 通过operator.eq判断里面两个元素是否相等
                        QMessageBox.information(None, '存储结果', '存储成功!', QMessageBox.Ok)
                        new_cb.remove(cb_data.columns.values.tolist()[0])
                        main_ui.ui.type_cb.addItems(new_cb)  # 添加下拉选项内容
                        child.close()  # 关闭Dialog窗体
                    else:
                        QMessageBox.warning(None, '存储结果', '存储失败!', QMessageBox.Ok)
                        child.close()

            def clear_columns():
                child.child_ui.type_input3.setText('')

            child.child_ui.save_type_btn.clicked.connect(new_type)
            child.child_ui.clear_btn.clicked.connect(clear_columns)
        else:
            pass
    else:
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_ui = parentWindow()

    main_ui.ui.read_btn.clicked.connect(Read_File)
    main_ui.ui.open_btn.clicked.connect(Open_File)
    main_ui.ui.save_btn.clicked.connect(save_data)
    main_ui.ui.dateEdit.setDate(QDate.currentDate())  # 设置默认显示当前日期
    main_ui.ui.actionOpen_File.triggered.connect(Open_File)  # 菜单栏触发方法
    main_ui.ui.actionCreate_File.triggered.connect(Create_File)

    main_ui.show()
    sys.exit(app.exec_())
