main_kv = """
<ContentNavigationDrawer@MDNavigationDrawer>:
    drawer_logo: 'drawer_logo.png'

    NavigationDrawerSubheader:
        text: "Menu:"


NavigationLayout:
    id: nav_layout

    ContentNavigationDrawer:
        id: nav_drawer

    BoxLayout:
        orientation: 'vertical'

        MDToolbar:
            id: toolbar
            title: 'KivyMD Kitchen Sink'
            md_bg_color: app.theme_cls.primary_color
            background_palette: 'Primary'
            background_hue: '500'
            elevation: 10
            left_action_items:
                [['dots-vertical', lambda x: app.root.toggle_nav_drawer()]]

        Widget:
"""