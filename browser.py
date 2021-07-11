import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


#window browser uchun
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://google.com"))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #navbar =button uchun
        navbar = QToolBar()
        self.addToolBar(navbar)

        pre_btn = QAction('<=',self)
        pre_btn.triggered.connect(self.browser.back)
        navbar.addAction(pre_btn)

        next_button = QAction('=>',self)
        next_button.triggered.connect(self.browser.forward)
        navbar.addAction(next_button)

        reload_button = QAction('reload', self)
        reload_button.triggered.connect(self.browser.reload)
        navbar.addAction(reload_button)

        home_button = QAction('home', self)
        home_button.triggered.connect(self.navigate_home)
        navbar.addAction(home_button)

        # search box
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate2)
        navbar.addWidget(self.url_bar)

        #set.browser.urlChanged.connect(self.update_url)

    #home button uchun
    def navigate_home(self):
        self.browser.setUrl(QUrl("http://gmail.com"))
    def navigate2(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))
    #def update_url(self,q):
    #    self.url_bar.setText(q.toString())
app = QApplication(sys.argv)
QApplication.setApplicationName("my browser")

window=MainWindow()
app.exec_()