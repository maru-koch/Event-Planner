from kivy.app import App 


"""
    - importing screen from layouts
"""
from Layouts.homeLayout import HomeScreen


"""
    - initializing screens
"""
HomeScreen()


class EventApp(App):
    pass


if __name__=="__main__":
    from kivy.core.text import LabelBase
    LabelBase.register(name = 'Icon', fn_regular='Resources/font/heydings_icons.ttf')
    LabelBase.register(name = 'Icon', fn_regular='Resources/font/modernpics.ttf')
    LabelBase.register(name = 'RobotoMedium', fn_regular='Resources/font/RobotoMedium500.ttf')
    LabelBase.register(name = 'RobotoLight', fn_regular='Resources/font/Roboto400.ttf')
    EventApp().run()
