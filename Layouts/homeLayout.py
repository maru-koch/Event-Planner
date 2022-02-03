from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from datetime import date, timedelta
from kivy.clock import Clock
from kivy.utils import get_color_from_hex as c
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout


class HomeScreen(BoxLayout, Screen):
    started = False
    
    count = 0
    option = ObjectProperty

    image = StringProperty()
    title = StringProperty("Anulika's Wedding")
    address = StringProperty("Ikorodu")
    city = StringProperty("Ikeja")
    state = StringProperty("Lagos")

    year = NumericProperty()
    month = NumericProperty()
    day = NumericProperty()

    second = NumericProperty()
    hour = NumericProperty()
    minute = NumericProperty()

    hr = NumericProperty(2)
    minx = NumericProperty(45)
    sec = NumericProperty(60)


    days_remaining = NumericProperty(360)
    def on_start(self):
        self.event_date(2021, 12, 23)
        Clock.schedule_interval(self.count_down, 1)


    def update_time(self, nap):
        #self.root.ids.time.text = time.strftime("%H : %M : %S")
        pass
        

    def count_down(self, x):
        self.sec -= 1
        
        if self.sec == 0:
            self.minx = self.minx - 1
            self.sec = 60

        if self.minx == 0:
                self.hr = self.hr - 1
                self.minx = 60
        if self.hr == 0:
            #self.event_date.remaining_days -= 1
            print("event due")

        self.hour = str(self.hr)
        self.minute = str(self.minx)
        self.second = str(self.sec)
        

    def update_counter(self):
        self.started = not self.started
        self.root.ids.start_stop.text =("Stop" if self.started else "Start")
        self.root.ids.start_stop.background_color = (c("#567890") if self.started else c("#454545"))
        Clock.schedule_interval(self.counter, self.count)

    def add_option(self):
        option = self.root.ids.option
        self.root.add_widget(option)
    
    
    def event_date(self, year, month, day):
        remaining_days = ''
        #EVENT DATE ENTERED BY USER
        event_year = int(year)
        event_month = int(month)
        event_day = int(day)
        
        event_date = date(event_year, event_month, event_day)
        event_date_format = event_date.strftime("%a, %d %b %Y")

        #CURRENT DAY(tODAY'S DATE)
        current_day = str(date.today()).split('-')
        
        today_year = int(current_day[0])
        today_month = current_day[1].strip('0')
        today_day = current_day[2]

        #TOTAL NUMBER OF DAYS TO THE EVENT
        months = [31, 28, 31,30, 31, 30, 31, 31, 30, 31, 30, 31]
        current_days = sum(months[0:int(today_month)])
        event_days = sum(months[0: event_month + 1])


        #THE EVENT YEAR IS THE SAME AS THE CURRENT YEAR
        if event_date < date.today():
            print('Your event cant be in the past')
            
        elif event_year == today_year:
            
            remaining_days = abs(current_days - event_days)
            
            self.root.ids.days_remaining.text = str(remaining_days)
            
        else:
                remaining_months = len(months) - int(date.today().month)
                                                        
                remaining_days = sum(months[-remaining_months:]) + sum(months[0:event_month])

                self.root.ids.days_remaining.text = str(remaining_days)
                

        self.root.ids.event_date.text = event_date_format

        return remaining_days
        
    def option(self):
        con = FloatLayout(size = (200, 200), pos = (200, 0), size_hint = (None, None))
        event_option = AnchorLayout(anchor_x = 'left', anchor_y = 'bottom')
        Btn = Button(text = 'e', font_name = 'Icon')
        event_option.add_widget(Btn)
        con.add_widget(event_option)
        self.root.add_widget(con)
        
        
        
    
    def reset(self):
        if self.started:
            self.Seconds = 0
        else:
            self.Seconds = 0
            self.started = False
            self.root.ids.start_stop.text = "Start" 
            self.root.ids.counter.text = ("{}: {}: {}".format(00,00,00))