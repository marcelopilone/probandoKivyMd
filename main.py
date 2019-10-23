from kivy.app import App
from kivy.lang import Builder

from kivymd.uix.navigationdrawer import NavigationDrawerIconButton
from kivymd.theming import ThemeManager
from kivymd.toast import toast


class Example(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Teal'
    title = "Menu"

    

    def build(self):
        return ContentNavigationDrawerMDNavigationDrawer()


    def callback(self, instance, value):
        toast("Pressed item menu %d" % value)

    def on_start(self):
        for i in range(15):
            self.main_widget.ids.nav_drawer.add_widget(
                NavigationDrawerIconButton(
                    icon='checkbox-blank-circle', text="El link %d" % i,
                    on_release=lambda x, y=i: self.callback(x, y)))

class ContentNavigationDrawerMDNavigationDrawer():
    	pass


Example().run()