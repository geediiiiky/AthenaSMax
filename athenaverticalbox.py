from kivy.uix.boxlayout import BoxLayout

class AthenaVerticalBox(BoxLayout):

    def __init__(self, **kwargs):
        super(AthenaVerticalBox, self).__init__(**kwargs)
        self.height = 0
        self.size_hint = (1, None)
        self.orientation='vertical'

    def add_widget(self, widget, index=0, canvas=None):
        self.height = self.height + widget.height
        return super(AthenaVerticalBox, self).add_widget(widget, index, canvas)