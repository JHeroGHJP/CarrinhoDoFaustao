from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import time
import RPi.GPIO as GPIO

GPIO.setmode (GPIO.BORAD)
GPIO.setwarnings (FALSE)
GPIO.setup (11, GPIO.OUT)
GPIO.setup (13, GPIO.OUT)
GPIO.setup (15, GPIO.OUT)
GPIO.setup (19, GPIO.OUT)

Builder.load_string('''
<vuild>:
    orientation: 'vertical'
    Button:
        text: 'LED 11_on'
        size_hint_y: None
        height: '48dp'
        on_press: print ("LED 11 ligado...")
        GPIO.output (11, GPIO.HIGH)
    Button:
        text: 'LED 13_on'
        size_hint_y: None
        height: '48dp'
        on_press: print ("LED 13 ligado...")
        GPIO.output (13, GPIO.HIGH)
    Button:
        text: 'LED 15_on'
        size_hint_y: None
        height: '48dp'
        on_press: print ("LED 15 ligado...")
        GPIO.output (15, GPIO.HIGH)
    Button:
        text: 'LED 19_on'
        size_hint_y: None
        height: '48dp'
        on_press: print ("LED 19 ligado...")
        GPIO.output (19, GPIO.HIGH)
    Button:
        text: 'LED 11_off'
        size_hint_y: None
        height: '48dp'
        on_press: print ("LED 11 desligado...")
        GPIO.output (11, GPIO.LOW)
    Button:
        text: 'LED 13_off'
        size_hint_y: None
        height: '48dp'
        on_press: print ("LED 13 desligado...")
        GPIO.output (13, GPIO.LOW)
    Button:
        text: 'LED 15_off'
        size_hint_y: None
        height: '48dp'
        on_press: print ("LED 15 desligado...")
        GPIO.output (15, GPIO.LOW)
    Button:
        text: 'LED 19_off'
        size_hint_y: None
        height: '48dp'
        on_press: print ("LED 19 desligado...")
        GPIO.output (19, GPIO.LOW)
''')


class vuild(BoxLayout):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        #camera = self.ids['camera']


class buildCamera(App):

    def build(self):
        return vuild()



buildCamera().run()
