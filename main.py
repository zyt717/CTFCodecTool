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
        self.pageModernEncryptLayout = QtWidgets.QVBoxLayout(self.pageModernEncrypt)
        self.pageModernDecryptLayout = QtWidgets.QVBoxLayout(self.pageModernDecrypt)
        self.pageHexLayout = QtWidgets.QVBoxLayout(self.pageHex)
        self.pageHashLayout = QtWidgets.QVBoxLayout(self.pageHash)

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

    def setAndSyncPlainEditText(self, edit, text):
        '''设置PlainTextEdit的值，并同步self.src或self.dst'''
        try:
            if isinstance(text, bytes):
                btext = text
                stext = text.decode('utf-8')
            elif isinstance(text, str):
                btext = text.encode('utf-8')
                stext = text
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
            elif codec['category'] == 'modernencrypt':
                self.menuModernEncrypt.addAction(act)
            elif codec['category'] == 'moderndecrypt':
                self.menuModernDecrypt.addAction(act)
            elif codec['category'] == 'hex':
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
            elif codec['category'] == 'modernencrypt':
                self.pageModernEncryptLayout.addWidget(toolButton, 0, Qt.AlignTop)
            elif codec['category'] == 'moderndecrypt':
                self.pageModernDecryptLayout.addWidget(toolButton, 0, Qt.AlignTop)
            elif codec['category'] == 'hex':
                self.pageHexLayout.addWidget(toolButton, 0, Qt.AlignTop)
            elif codec['category'] == 'hash':
                self.pageHashLayout.addWidget(toolButton, 0, Qt.AlignTop)
        self.pageEncodeLayout.addStretch(1)
        self.pageDecodeLayout.addStretch(1)
        self.pageEncryptLayout.addStretch(1)
        self.pageDecryptLayout.addStretch(1)
        self.pageModernEncryptLayout.addStretch(1)
        self.pageModernDecryptLayout.addStretch(1)
        self.pageHexLayout.addStretch(1)
        self.pageHashLayout.addStretch(1)

    def setupSignals(self):
        def textEditTextChanged():
            if self.sender() is self.srcTextEdit:
                self.src = self.srcTextEdit.toPlainText().encode('utf-8')
            elif self.sender() is self.dstTextEdit:
                self.dst = self.dstTextEdit.toPlainText().encode('utf-8')

        def openFile():
            fname = QtWidgets.QFileDialog.getOpenFileName(self, '打开文件')
            if fname[0]:
                with open(fname[0], 'rb') as f:
                    data = f.read()
                    self.setAndSyncPlainEditText(self.srcTextEdit, data)

        def saveFile():
            fname = QtWidgets.QFileDialog.getSaveFileName(self, '保存文件')
            if fname[0]:
                with open(fname[0], 'wb') as f:
                    f.write(self.dst)

        def swapText():
            srcText = self.srcTextEdit.toPlainText()
            dstText = self.dstTextEdit.toPlainText()
            self.setPlainEditText(self.srcTextEdit, dstText)
            self.setPlainEditText(self.dstTextEdit, srcText)
            self.src, self.dst = self.dst, self.src

        def copyText():
            if self.sender() is self.srcCopyButton:
                self.srcTextEdit.selectAll()
                self.srcTextEdit.copy()
            elif self.sender() is self.dstCopyButton:
                self.dstTextEdit.selectAll()
                self.dstTextEdit.copy()

        def replaceText():
            if self.sender() is self.srcReplaceButton:
                oldText = self.srcLineEdit1.text()
                newText = self.srcLineEdit2.text()
                self.setAndSyncPlainEditText(self.srcTextEdit, self.srcTextEdit.toPlainText().replace(oldText, newText))
            elif self.sender() is self.dstReplaceButton:
                oldText = self.dstLineEdit1.text()
                newText = self.dstLineEdit2.text()
                self.setAndSyncPlainEditText(self.dstTextEdit, self.dstTextEdit.toPlainText().replace(oldText, newText))

        self.srcTextEdit.textChanged.connect(textEditTextChanged)
        self.dstTextEdit.textChanged.connect(textEditTextChanged)

        self.srcOpenButton.clicked.connect(openFile)
        self.dstSaveButton.clicked.connect(saveFile)
        self.swapButton.clicked.connect(swapText)
        self.srcCopyButton.clicked.connect(copyText)
        self.dstCopyButton.clicked.connect(copyText)
        self.srcReplaceButton.clicked.connect(replaceText)
        self.dstReplaceButton.clicked.connect(replaceText)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = CtfCodecMainWindow()
    window.show()
    sys.exit(app.exec_())
