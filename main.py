from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from ui.mainwindow import Ui_MainWindow
from PyQt5.QtCore import Qt
import sys


class CtfCodecMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(CtfCodecMainWindow, self).__init__()
        self.src = b''
        self.dst = b''
        self.setupUi(self)
        self.setWindowIcon(QIcon('favicon.ico'))
        self.setupToolboxLayout()
        self.setupActions()
        self.setupSignals()

    def setupToolboxLayout(self):
        '''设置toolbox的布局'''
        self.pageEncodeLayout = QtWidgets.QVBoxLayout(self.pageEncode)
        self.pageDecodeLayout = QtWidgets.QVBoxLayout(self.pageDecode)
        self.pageEncryptLayout = QtWidgets.QVBoxLayout(self.pageEncrypt)
        self.pageDecryptLayout = QtWidgets.QVBoxLayout(self.pageDecrypt)
        self.pageHexLayout = QtWidgets.QVBoxLayout(self.pageHex)

    def setPlainEditText(self, edit, text):
        '''仅设置PlainTextEdit的值'''
        if edit is self.srcTextEdit:
            self.srcTextEdit.blockSignals(True)
            self.srcTextEdit.setPlainText(text)
            self.srcTextEdit.blockSignals(False)
        elif edit is self.dstTextEdit:
            self.dstTextEdit.blockSignals(True)
            self.dstTextEdit.setPlainText(text)
            self.dstTextEdit.blockSignals(False)

    def setAndSyncPlainEditText(self, edit, origintext):
        '''设置PlainTextEdit的值，并同步self.src或self.dst'''
        try:
            if isinstance(origintext, bytes):
                btext = origintext
                stext = origintext.decode('utf-8')
            elif isinstance(origintext, str):
                btext = origintext.encode('utf-8')
                stext = origintext
            self.setPlainEditText(edit, stext)
        except:
            self.setPlainEditText(edit, f'无法显示结果，结果已存入内存，共{len(btext)}字节，请另存为文件查看')
        finally:
            if edit is self.srcTextEdit:
                self.src = btext
            elif edit is self.dstTextEdit:
                self.dst = btext

    def runCodec(self):
        try:
            result = self.sender().codec['func'](self.src,
                                                 self.srcLineEdit1.text(),
                                                 self.srcLineEdit2.text(),
                                                 self.dstLineEdit1.text(),
                                                 self.dstLineEdit2.text())
        except Exception as e:
            result = '转换失败:' + repr(e)
        self.setAndSyncPlainEditText(self.dstTextEdit, result)

    def setupActions(self):
        # 获取所有类
        from ctfcodecs.ctfcodecs import ctfcodecs
        for codec in ctfcodecs:
            act = QtWidgets.QAction(codec['text'], self)
            if 'tooltip' in codec:
                act.setToolTip(codec['tooltip'])
            act.codec = codec
            act.triggered.connect(self.runCodec)
            # 添加至menu
            if codec['category'] == 'encode':
                self.menuEncode.addAction(act)
            elif codec['category'] == 'decode':
                self.menuDecode.addAction(act)
            elif codec['category'] == 'encrypt':
                self.menuEncrypt.addAction(act)
            elif codec['category'] == 'decrypt':
                self.menuDecrypt.addAction(act)
            elif codec['category'] == 'Hex':
                self.menuHex.addAction(act)

            # 添加至toolbox
            toolButton = QtWidgets.QToolButton(self)
            toolButton.setDefaultAction(act)
            toolButton.setSizePolicy(
                QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed))
            if codec['category'] == 'encode':
                self.pageEncodeLayout.addWidget(toolButton, alignment=Qt.AlignTop)
            elif codec['category'] == 'decode':
                self.pageDecodeLayout.addWidget(toolButton, 0, Qt.AlignTop)
            elif codec['category'] == 'encrypt':
                self.pageEncryptLayout.addWidget(toolButton, 0, Qt.AlignTop)
            elif codec['category'] == 'decrypt':
                self.pageDecryptLayout.addWidget(toolButton, 0, Qt.AlignTop)
            elif codec['category'] == 'Hex':
                self.pageHexLayout.addWidget(toolButton, 0, Qt.AlignTop)
        self.pageEncodeLayout.addStretch(1)
        self.pageDecodeLayout.addStretch(1)
        self.pageEncryptLayout.addStretch(1)
        self.pageDecryptLayout.addStretch(1)
        self.pageHexLayout.addStretch(1)

    def openFile(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, '打开文件')
        if fname[0]:
            with open(fname[0], 'rb') as f:
                data = f.read()
                self.setAndSyncPlainEditText(self.srcTextEdit, data)

    def saveFile(self):
        fname = QtWidgets.QFileDialog.getSaveFileName(self, '保存文件')
        if fname[0]:
            with open(fname[0], 'wb') as f:
                f.write(self.dst)

    def swapText(self):
        srcText = self.srcTextEdit.toPlainText()
        dstText = self.dstTextEdit.toPlainText()
        self.setPlainEditText(self.srcTextEdit, dstText)
        self.setPlainEditText(self.dstTextEdit, srcText)
        self.src, self.dst = self.dst, self.src

    def setupSignals(self):
        def textEditTextChanged():
            if self.sender() is self.srcTextEdit:
                self.src = self.srcTextEdit.toPlainText().encode('utf-8')
            elif self.sender() is self.dstTextEdit:
                self.dst = self.dstTextEdit.toPlainText().encode('utf-8')

        self.srcTextEdit.textChanged.connect(textEditTextChanged)
        self.dstTextEdit.textChanged.connect(textEditTextChanged)

        self.srcOpenButton.clicked.connect(self.openFile)
        self.dstSaveButton.clicked.connect(self.saveFile)
        self.swapButton.clicked.connect(self.swapText)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = CtfCodecMainWindow()
    window.show()
    sys.exit(app.exec_())
