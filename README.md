# calculator-practice
Using PyQt5 to create a calculator.

# 计算器编程练习
参考资料：
<br/>1、实验楼的java开发简单的计算器教程 地址：https://www.shiyanlou.com/courses/185
<br/>2、PyQt5 中文教程 地址：https://legacy.gitbook.com/book/maicss/pyqt5/details

<br/><br/>

开发环境准备：
<br/>1、Python 3.6.2； 2、PyQt5 版本5.10； 3、sip 版本4.19.8； 4、PyInstaller 版本3.3.1。
<br/>注by20180708：当前PyQt5最新版本为5.11，但是需要更新的sip包支持（pypi上sip包没有最新版本，需要手动安装），否则打包EXE时会失败。

描述：
<br/>参照实验楼java的简单计算器开发教程，用python简单创建了gui界面，在计算控制上做了修改。
<br/>原java程序实现为每次按钮输入一个数，然后输入一个运算符，再输入一个数得到运算结果。此次python程序改善为可通过文本框和按钮两种途径输入，并可以输入多重四则运算通过一次计算得到结果。

<br/><br/>

模块：
<br/>calculator.exe： 此文件为pyinstaller打包的执行文件，可直接单独运行。
<br/>calculator.py: 此模块为gui界面初始化和布局设计，包括事件触发控制。
<br/>pushbutton.py: 按钮部件设计模块。此计算器以按钮部件为主。
<br/>operation.py： 计算处理模块。包括输入文本处理检验和四则运算的处理。
<br/>test：为上述模块的测试文件。

<br/><br/>

坑点：
<br/>1、pyinstaller打包依赖工具包版本，尽量避免用最新版本工具包。
<br/>2、打包前对代码进行整理，以免打包得到的文件过大。
<br/>3、PyQt5是C++编写的，参考文档看起来比较费劲，网上参考资料较少（雷同）。
<br/>4、按键时间中，Qt.Key_Enter没有触发，改成Qt.Key_Escape可以触发，原因未知。
<br/>5、按钮布局、大小调整受到gridlayout的限制，暂未调整。

<br/><br/>

后续：
<br/>可增加平方、开方、对数等运算，在operation处进行扩展。
<br/>gui界面可以进一步优化，包括字体，颜色，按钮大小。


