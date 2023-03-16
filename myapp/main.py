from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
import kivy
import mysql


class MyRoot(BoxLayout):

    def __init__(self):
        super(MyRoot, self).__init__()

    def calc_symbol(self, symbol):
        self.calc_field.text += symbol

    def clear(self):
        self.calc_field.text = ""

    def get_result(self):
        self.calc_field.text = str(eval(self.calc_field.text))


class Calc(App):

    def __init__(self):
        super().__init__()
        self.db = None

    def build(self):
        return MyRoot()

    def make_table(self):
        self.db = mysql.create_database()
        conn = mysql.connect()
        mysql.create_table(conn)

    @staticmethod
    def add_entry(date, time, category, note, amount):
        conn = mysql.connect()
        mysql.add_entry(conn, date, time, category, note, amount)
        conn.commit()
        conn.close()


calc = Calc()
calc.run()