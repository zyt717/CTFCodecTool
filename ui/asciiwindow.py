# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'asciiwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_asciiForm(object):
    def setupUi(self, asciiForm):
        asciiForm.setObjectName("asciiForm")
        asciiForm.resize(838, 519)
        self.gridLayout = QtWidgets.QGridLayout(asciiForm)
        self.gridLayout.setObjectName("gridLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(asciiForm)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 0, 0, 1, 1)

        self.retranslateUi(asciiForm)
        QtCore.QMetaObject.connectSlotsByName(asciiForm)

    def retranslateUi(self, asciiForm):
        _translate = QtCore.QCoreApplication.translate
        asciiForm.setWindowTitle(_translate("asciiForm", "ASCII"))
        self.plainTextEdit.setPlainText(_translate("asciiForm", "十六进制    十进制    字符       |十六进制    十进制    字符       |十六进制    十进制    字符       |十六进制    十进制    字符       \n"
"0x00        0         \\0 (终止符)|0x20        32        space(空格)|0x41        65        A          |0x61        97        a          \n"
"0x01        1         \\x1        |0x21        33        !          |0x42        66        B          |0x62        98        b          \n"
"0x02        2         \\x2        |0x22        34        \"          |0x43        67        C          |0x63        99        c          \n"
"0x03        3         \\x3        |0x23        35        #          |0x44        68        D          |0x64        100       d          \n"
"0x04        4         \\x4        |0x24        36        $          |0x45        69        E          |0x65        101       e          \n"
"0x05        5         \\x5        |0x25        37        %          |0x46        70        F          |0x66        102       f          \n"
"0x06        6         \\x6        |0x26        38        &          |0x47        71        G          |0x67        103       g          \n"
"0x07        7         \\x7        |0x27        39        \'          |0x48        72        H          |0x68        104       h          \n"
"0x08        8         \\b (退格符)|0x28        40        (          |0x49        73        I          |0x69        105       i          \n"
"0x09        9         \\t (制表符)|0x29        41        )          |0x4a        74        J          |0x6a        106       j          \n"
"0x0a        10        \\n (换行符)|0x2a        42        *          |0x4b        75        K          |0x6b        107       k          \n"
"0x0b        11        \\xb        |0x2b        43        +          |0x4c        76        L          |0x6c        108       l          \n"
"0x0c        12        \\xc        |0x2c        44        ,          |0x4d        77        M          |0x6d        109       m          \n"
"0x0d        13        \\r (回车符)|0x2d        45        -          |0x4e        78        N          |0x6e        110       n          \n"
"0x0e        14        \\xe        |0x2e        46        .          |0x4f        79        O          |0x6f        111       o          \n"
"0x0f        15        \\xf        |0x2f        47        /          |0x50        80        P          |0x70        112       p          \n"
"0x10        16        \\x10       |0x30        48        0          |0x51        81        Q          |0x71        113       q          \n"
"0x11        17        \\x11       |0x31        49        1          |0x52        82        R          |0x72        114       r          \n"
"0x12        18        \\x12       |0x32        50        2          |0x53        83        S          |0x73        115       s          \n"
"0x13        19        \\x13       |0x33        51        3          |0x54        84        T          |0x74        116       t          \n"
"0x14        20        \\x14       |0x34        52        4          |0x55        85        U          |0x75        117       u          \n"
"0x15        21        \\x15       |0x35        53        5          |0x56        86        V          |0x76        118       v          \n"
"0x16        22        \\x16       |0x36        54        6          |0x57        87        W          |0x77        119       w          \n"
"0x17        23        \\x17       |0x37        55        7          |0x58        88        X          |0x78        120       x          \n"
"0x18        24        \\x18       |0x38        56        8          |0x59        89        Y          |0x79        121       y          \n"
"0x19        25        \\x19       |0x39        57        9          |0x5a        90        Z          |0x7a        122       z          \n"
"0x1a        26        \\x1a       |0x3a        58        :          |0x5b        91        [          |0x7b        123       {          \n"
"0x1b        27        \\x1b       |0x3b        59        ;          |0x5c        92        \\          |0x7c        124       |          \n"
"0x1c        28        \\x1c       |0x3c        60        <          |0x5d        93        ]          |0x7d        125       }          \n"
"0x1d        29        \\x1d       |0x3d        61        =          |0x5e        94        ^          |0x7e        126       ~          \n"
"0x1e        30        \\x1e       |0x3e        62        >          |0x5f        95        _          |0x7f        127                  \n"
"0x1f        31        \\x1f       |0x3f        63        ?          |0x60        96        `          |\n"
"                                 |0x40        64        @          "))
