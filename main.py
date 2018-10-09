from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button

import os
import os.path

class MedusaApp(App):

    def build(self):
        parent = Widget()
        cmdBtn = Button(text='Execute Command')
        cmdBtn.bind(on_release=self.executeCmd)
        cmdBtn.pos = (100, 150)
        cmdBtn.size = (200, 50)
        parent.add_widget(cmdBtn)
        return parent

    def executeCmd(self, obj):
        exeFile = os.path.join(".", "Scripts", "Windows", "Test.bat")
        os.system("start cmd /c " + exeFile + " hahahaha")

if __name__ == '__main__':
    MedusaApp().run()
