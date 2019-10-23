from kivy.app import App
from kivy.lang import Builder

from kivymd.uix.navigationdrawer import NavigationDrawerIconButton
from kivymd.theming import ThemeManager
from kivymd.toast import toast
from menu import *  


class Example(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Teal'

    def build(self):
        self.main_widget = Builder.load_string(main_kv)
        return self.main_widget

    def callback(self, instance, value):
        toast("Pressed item menu %d" % value)

    def on_start(self):
        for i in range(15):
            self.main_widget.ids.nav_drawer.add_widget(
                NavigationDrawerIconButton(
                    icon='checkbox-blank-circle', text="Item menu %d" % i,
                    on_release=lambda x, y=i: self.callback(x, y)))


Example().run()