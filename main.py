from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.tabbedpanel import TabbedPanelItem
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from athenaseparator import AthenaSeparator
from athenaverticalbox import AthenaVerticalBox

from athenacommand import *
from athenaconfig import *

from json_converter import JsonConvert

import os
import os.path

'''
TabbedPanel - root
    TabbedPanelItem (TabbedPanel.tab_list)
        BoxLayout (TabbedPanelItem.content)
            BoxLayout ()  - group1
                Button
                CheckBox
                Separator
                Button
            BoxLayout ()  - group2
                Button
                ....
'''

class AthenaApp(App):

    buttonSize = (200, 30)
    groupLabelSize = (200, 30)

    def build(self):
        self.root = None
        aconfig = JsonConvert.FromFile('testconfig.json')
        if isinstance(aconfig, AthenaConfiguration):
            self.root = TabbedPanel(do_default_tab=False)
            for command in aconfig.commands:
                if isinstance(command, AthenaCommand):
                    layout = self.getGroupLayout(command)
                    cmdWidget = self.presentCommand(command)
                    layout.add_widget(cmdWidget)
                    separator = AthenaSeparator()
                    layout.add_widget(separator)
            
            # add an empty widget just to push everything to the top of the box layout...
            for child in self.root.tab_list:
                child.content.add_widget(Widget())
        return self.root

    def presentCommand(self, command):
        container = AthenaVerticalBox()
        cmdBtn = Button(text=command.caption, size_hint=(None, None))
        cmdBtn.bind(on_release=self.executeCmd)
        cmdBtn.size = self.buttonSize
        cmdBtn.command = command
        container.add_widget(cmdBtn)
        for paramname, parameter in command.parameters.iteritems():
            if isinstance(parameter, CommandParameter):
                paramWidget = self.presentParameter(paramname, parameter)
                if paramWidget is not None:
                    container.add_widget(paramWidget)
        return container

    def presentParameter(self, paramname, parameter):
        if parameter.type == ParameterType.OnOff:
            if len(parameter.collection) == 1:
                box = StackLayout(orientation='lr-tb', size_hint=(1,None), height=30)
                paramCheckbox = CheckBox(size_hint=(None,None), size=(30, 30), active=parameter.selectedIndex==0)
                paramCheckbox.bind(active=self.on_onoff_parameter_changed)
                paramCheckbox.parameter = parameter
                box.add_widget(paramCheckbox)
                box.add_widget(Label(text=parameter.collection[0].get('Caption', parameter.displayName)
                                    , size=(200, 30), size_hint=(None,None), halign='left', text_size=(200, None) ))
                return box
        return None

    def getTabLayout(self, command):
        tabItem = None
        for child in self.root.tab_list:
            if child.text == command.tabName:
                return child.content
        tabItem = TabbedPanelItem(text=command.tabName)
        self.root.add_widget(tabItem)
        tabItem.add_widget(BoxLayout(orientation='vertical', size_hint=(1,1)))
        return tabItem.content


    def getGroupLayout(self, command):
        tabLayout = self.getTabLayout(command)
        for child in tabLayout.children:
            if hasattr(child, 'groupName') and child.groupName == command.groupName:
                return child 
        groupLayout = AthenaVerticalBox()
        groupLayout.groupName = command.groupName
        tabLayout.add_widget(groupLayout)
        label = Label(text=command.groupName, size_hint=(None, None), size=self.groupLabelSize)
        groupLayout.add_widget(label)
        return groupLayout


    def on_onoff_parameter_changed(self, checkbox, newActive):
        if hasattr(checkbox, 'parameter'):
            parameter = checkbox.parameter
            if parameter is not None:
                if isinstance(parameter, CommandParameter):
                    parameter.selectedIndex = 0 if newActive else -1


    def executeCmd(self, button):
        exeFile = os.path.join(".", "Scripts", "Windows", button.command.commandStr)
        os.system("start cmd /c " + exeFile + " hahahaha")

if __name__ == '__main__':
    AthenaApp().run()
