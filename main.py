from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.tabbedpanel import TabbedPanelItem
from separator import Separator

from athena_command import *
from athena_config import *

from json_converter import JsonConvert

import os
import os.path

class AthenaApp(App):

    def build(self):
        self.root = None
        aconfig = JsonConvert.FromFile('testconfig.json')
        if isinstance(aconfig, AthenaConfiguration):
            self.root = TabbedPanel(do_default_tab=False)
            for command in aconfig.commands:
                if isinstance(command, AthenaCommand):
                    layout = self.getHoldingLayout(command)
                    cmdWidget = self.presentCommand(command)
                    separator = Separator()
                    layout.add_widget(cmdWidget)
                    layout.add_widget(separator)
        return self.root

    def presentCommand(self, command):
        cmdBtn = Button(text=command.caption, size_hint=(None, None))
        cmdBtn.bind(on_release=self.executeCmd)
        cmdBtn.size = (200, 50)
        cmdBtn.command = command
        return cmdBtn

    def getHoldingLayout(self, command):
        tabItem = None
        for child in self.root.tab_list:
            if child.text == command.tabName:
                return child.content
        tabItem = TabbedPanelItem(text=command.tabName)
        tabItem.content = StackLayout(orientation='tb-lr')
        self.root.add_widget(tabItem)
        return tabItem.content

    def executeCmd(self, button):
        exeFile = os.path.join(".", "Scripts", "Windows", button.command.commandStr)
        os.system("start cmd /c " + exeFile + " hahahaha")

if __name__ == '__main__':
    AthenaApp().run()
