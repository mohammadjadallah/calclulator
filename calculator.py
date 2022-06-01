from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton
from kivymd.uix.textfield import MDTextFieldRect, MDTextField
from kivy.lang.builder import Builder
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.floatlayout import FloatLayout
from pyperclip import copy


class CalculatorApp(MDApp):
    def build(self):
        # setup window
        Window.size = (400, 600)
        self.title = "Calculator"
        self.theme_cls.primary_palette = "Pink"

        screen = Screen()

        # GridLayout Widget
        flaotWidget = FloatLayout()
        self.output_of_calulation = MDTextField(
            multiline=False,
            line_color_focus= "#D100D1",
            size_hint=("100dp", '100dp'),
            pos_hint={"x": 0.0, "y": 0.86},
            font_size=30,
            font_name="Comic",

        )

        self.input_text = lambda texts: texts

        # GridLayout Widget
        self.floatButtons = FloatLayout()

        # Buttons 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, +, -, *, /, %, (, ), **, Mode(themes), CE, Clear, 16 BUTTONS SHOULD THERE
# The first row from bottom
        # Equal btn
        self.equal_btn = MDFlatButton(text="=", md_bg_color="#D100D1",
                                font_name="Comic", font_size=50,
                                size_hint=(1, 0.1), on_release=self.result_of_calculations)
# The second row from bottom
        # zero btn
        self.zero_btn = MDFlatButton(text="0", md_bg_color="#D100D1",
                                font_name="Comic", font_size=40,
                                size_hint=(0.25, 0.05), pos_hint={"x":0.0, "y":0.15},
                                on_release=self.insert_0)
        # one btn
        self.one_btn = MDFlatButton(text="1", md_bg_color="#D100D1",
                                font_name="Comic", font_size=40,
                                size_hint=(0.25, 0.05), pos_hint={"x": 0.27, "y": 0.15},
                               on_release=self.insert_1)
        # two btn
        self.two_btn = MDFlatButton(text="2", md_bg_color="#D100D1",
                               font_name="Comic", font_size=40,
                               size_hint=(0.25, 0.05), pos_hint={"x": 0.54, "y": 0.15},
                               on_release=self.insert_2)

        # plus btn
        self.plus_btn = MDFlatButton(text="+", md_bg_color="#D100D1",
                               font_name="Comic", font_size=40,
                               size_hint=(0.2, 0.05), pos_hint={"x": 0.81, "y": 0.534},
                                on_release=self.insert_plus)

        self.floatButtons.add_widget(self.equal_btn)
        self.floatButtons.add_widget(self.zero_btn)
        self.floatButtons.add_widget(self.one_btn)
        self.floatButtons.add_widget(self.two_btn)
        self.floatButtons.add_widget(self.plus_btn)

# The third row from bottom
        # 3 btn
        self.three_btn = MDFlatButton(text="3", md_bg_color="#D100D1",
                                font_name="Comic", font_size=40,
                                size_hint=(0.25, 0.05), pos_hint={"x":0.0, "y":0.277},
                                 on_release=self.insert_3)
        # 4 btn
        self.four_btn = MDFlatButton(text="4", md_bg_color="#D100D1",
                                font_name="Comic", font_size=40,
                                size_hint=(0.25, 0.05), pos_hint={"x": 0.27, "y": 0.277},
                                on_release=self.insert_4)
        # 5 btn
        self.five_btn = MDFlatButton(text="5", md_bg_color="#D100D1",
                               font_name="Comic", font_size=40,
                               size_hint=(0.25, 0.05), pos_hint={"x": 0.54, "y": 0.277},
                                on_release=self.insert_5)

        # - btn
        self.difference_btn = MDFlatButton(text="-", md_bg_color="#D100D1",
                               font_name="Comic", font_size=40,
                               size_hint=(0.2, 0.05), pos_hint={"x": 0.81, "y": 0.277},
                                      on_release=self.insert_diff)

        self.floatButtons.add_widget(self.three_btn)
        self.floatButtons.add_widget(self.four_btn)
        self.floatButtons.add_widget(self.five_btn)
        self.floatButtons.add_widget(self.difference_btn)

# The fourth row from bottom
        # 6 btn
        self.six_btn = MDFlatButton(text="6", md_bg_color="#D100D1",
                                 font_name="Comic", font_size=40,
                                 size_hint=(0.25, 0.05), pos_hint={"x": 0.0, "y": 0.405},
                               on_release=self.insert_6)
        # 7 btn
        self.seven_btn = MDFlatButton(text="7", md_bg_color="#D100D1",
                                font_name="Comic", font_size=40,
                                size_hint=(0.25, 0.05), pos_hint={"x": 0.27, "y": 0.405},
                                 on_release=self.insert_7)
        # 8 btn
        self.eight_btn = MDFlatButton(text="8", md_bg_color="#D100D1",
                                font_name="Comic", font_size=40,
                                size_hint=(0.25, 0.05), pos_hint={"x": 0.54, "y": 0.405},
                                 on_release=self.insert_8)

        # * btn
        self.multiply_btn = MDFlatButton(text="x", md_bg_color="#D100D1",
                                      font_name="Comic", font_size=40,
                                      size_hint=(0.2, 0.05), pos_hint={"x": 0.81, "y": 0.405},
                                    on_release=self.insert_multiply)

        self.floatButtons.add_widget(self.six_btn)
        self.floatButtons.add_widget(self.seven_btn)
        self.floatButtons.add_widget(self.eight_btn)
        self.floatButtons.add_widget(self.multiply_btn)

# The fourth row from bottom
        # 9 btn
        self.nine_btn = MDFlatButton(text="9", md_bg_color="#D100D1",
                               font_name="Comic", font_size=40,
                               size_hint=(0.25, 0.05), pos_hint={"x": 0.0, "y": 0.534},
                                on_release=self.insert_9)
        # / btn
        self.division_btn = MDFlatButton(text="÷", md_bg_color="#D100D1",
                                 font_name="Comic", font_size=40,
                                 size_hint=(0.25, 0.05), pos_hint={"x": 0.27, "y": 0.534},
                                    on_release=self.insert_div)
        # % btn
        self.mod_btn = MDFlatButton(text="%", md_bg_color="#D100D1",
                                 font_name="Comic", font_size=40,
                                 size_hint=(0.25, 0.05), pos_hint={"x": 0.54, "y": 0.534},
                               on_release=self.insert_mod)

        # remove btn
        self.remove_btn = MDFlatButton(text="CE", md_bg_color="#D100D1",
                                    font_name="Comic", font_size=36,
                                    size_hint=(0.2, 0.05), pos_hint={"x": 0.81, "y": 0.664},
                                  on_release=self.remove_char_one_by_one)

        self.floatButtons.add_widget(self.nine_btn)
        self.floatButtons.add_widget(self.division_btn)
        self.floatButtons.add_widget(self.mod_btn)
        self.floatButtons.add_widget(self.remove_btn)

# The fifth row from the bottom
        # remove all "clear"
        self.clear_btn = MDFlatButton(text="clear", md_bg_color="#D100D1",
                                  font_name="Comic", font_size=36,
                                  size_hint=(0.25, 0.05), pos_hint={"x":0.0, "y": 0.664}, on_release=self.clear_all)

        self.floatButtons.add_widget(self.clear_btn)

        # copy
        self.copy_btn = MDFlatButton(text="copy", md_bg_color="#D100D1",
                                 font_name="Comic", font_size=36,
                                 size_hint=(0.25, 0.05), pos_hint={'x':0.27, "y": 0.664},
                                on_release=self.copy_text_input)

        self.floatButtons.add_widget(self.copy_btn)

        # exponentiation
        self.ex_btn = MDFlatButton(text="x^y", md_bg_color="#D100D1",
                                font_name="Comic", font_size=36,
                                size_hint=(0.25, 0.05), pos_hint={'x': 0.54, "y": 0.664},
                              on_release = self.insert_ex)

        self.floatButtons.add_widget(self.ex_btn)

        # par open
        self.par_open_btn = MDFlatButton(text="( ", md_bg_color="#D100D1",
                              font_name="Comic", font_size=30,
                              size_hint=(0.25, 0.02), pos_hint={'x': 0.0, "y": 0.784},
                              on_release=self.insert_par_open)

        self.floatButtons.add_widget(self.par_open_btn)

        # par open
        self.par_close_btn = MDFlatButton(text=")", md_bg_color="#D100D1",
                                    font_name="Comic", font_size=30,
                                    size_hint=(0.25, 0.02), pos_hint={'x': 0.27, "y": 0.784},
                                    on_release=self.insert_par_close)

        self.floatButtons.add_widget(self.par_close_btn)

        # point
        self.point_btn = MDFlatButton(text=".", md_bg_color="#D100D1",
                                     font_name="Comic", font_size=38,
                                     size_hint=(0.2, 0.05), pos_hint={"x": 0.81, "y": 0.15},
                                     on_release=self.insert_point)

        self.floatButtons.add_widget(self.point_btn)

        # mode theme backgrount color option
        self.mode_color_option_btn = MDFlatButton(
            text="Theme Color ",
            md_bg_color="#D100D1",
            font_name="Comic", font_size=28,
            size_hint=(0.5, 0.09), pos_hint={"x": 0.54, "y": 0.784},
            on_release=self.mode_color_option

        )

        self.floatButtons.add_widget(self.mode_color_option_btn)

        flaotWidget.add_widget(self.output_of_calulation)
        # add flaotlayout to the screen
        screen.add_widget(flaotWidget)
        # add floatButtons to the screen
        screen.add_widget(self.floatButtons)


        return screen

    # insert 0 when press
    def insert_0(self, instance):
        self.output_of_calulation.text += '0'

    # insert 1 when press
    def insert_1(self, instance):
        self.output_of_calulation.text += '1'

    # insert 2 when press
    def insert_2(self, instance):
        self.output_of_calulation.text += '2'

    # insert 3 when press
    def insert_3(self, instance):
        self.output_of_calulation.text += '3'

    # insert 4 when press
    def insert_4(self, instance):
        self.output_of_calulation.text += '4'

    # insert 5 when press
    def insert_5(self, instance):
        self.output_of_calulation.text += '5'

    # insert 6 when press
    def insert_6(self, instance):
        self.output_of_calulation.text += '6'

    # insert 7 when press
    def insert_7(self, instance):
        self.output_of_calulation.text += '7'

    # insert 8 when press
    def insert_8(self, instance):
        self.output_of_calulation.text += '8'

    # insert 9 when press
    def insert_9(self, instance):
        self.output_of_calulation.text += '9'

    # insert + when press
    def insert_plus(self, instance):
        self.output_of_calulation.text += '+'

    # insert - when press
    def insert_diff(self, instance):
        self.output_of_calulation.text += '-'

    # insert * when press
    def insert_multiply(self, instance):
        self.output_of_calulation.text += '*'

    # insert / when press
    def insert_div(self, instance):
        self.output_of_calulation.text += '/'

    # insert % when press
    def insert_mod(self, instance):
        self.output_of_calulation.text += '%'

    # insert ** when press
    def insert_ex(self, instance):
        self.output_of_calulation.text += '**'

    # insert 2 when press
    def insert_2(self, instance):
        self.output_of_calulation.text += '2'

    # insert ( when press
    def insert_par_open(self, instance):
        self.output_of_calulation.text += '('

    # insert ) when press
    def insert_par_close(self, instance):
        self.output_of_calulation.text += ')'

    # insert point when press
    def insert_point(self, instance):
        self.output_of_calulation.text += '.'

    # clear all text
    def clear_all(self, instance):
        self.output_of_calulation.text = ""

    # remove char one by one
    def remove_char_one_by_one(self, instance):
        try:
            # length text
            length_of_text_input = len(self.output_of_calulation.text)

            # remove the last litter using the length - 1 as index
            remove_last_char = self.output_of_calulation.text[:length_of_text_input - 1]

            # text for conditions
            text_for_conditions = self.output_of_calulation.text

            if text_for_conditions[-1] + text_for_conditions[-2] == "**":
                self.output_of_calulation.text = text_for_conditions[:length_of_text_input - 2]
            else:
                self.output_of_calulation.text = remove_last_char

        except IndexError:
            self.output_of_calulation.text = ""

    # copy text from the text field
    def copy_text_input(self, instance):
         copy(self.output_of_calulation.text)

    # calculate input of user
    def result_of_calculations(self, instance):
        try:
            result = eval(self.output_of_calulation.text)
            self.output_of_calulation.text = str(result)
            return self.output_of_calulation.text
        except ZeroDivisionError:
            self.output_of_calulation.text = "Zero Division Error"
            return self.output_of_calulation.text
        except SyntaxError:
            if len(self.output_of_calulation.text) == 0:
                return
            self.output_of_calulation.text = "Syntax Error"
            return self.output_of_calulation.text
        except NameError:
            self.output_of_calulation.text = "Sorry That Was Wrong"
            return self.output_of_calulation.text

    def mode_color_option(self, instance):
        if self.theme_cls.theme_style == "Dark":
            self.output_of_calulation.line_color_focus = '#D100D1'
            self.theme_cls.theme_style = "Light"
            for button in (self.mode_color_option_btn, self.ex_btn, self.one_btn, self.mod_btn,
                           self.par_open_btn, self.plus_btn, self.four_btn, self.six_btn, self.two_btn,
                           self.equal_btn, self.clear_btn, self.multiply_btn, self.three_btn, self.difference_btn,
                           self.division_btn, self.nine_btn, self.remove_btn, self.copy_btn, self.par_close_btn, self.seven_btn,
                           self.eight_btn, self.five_btn, self.zero_btn, self.point_btn):

                button.md_bg_color = "#D100D1"
                self.theme_cls.primary_palette = "Red"

        else:
            self.output_of_calulation.line_color_focus = 'orange'
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = "Blue"
            for button in (self.mode_color_option_btn, self.ex_btn, self.one_btn, self.mod_btn,
                           self.par_open_btn, self.plus_btn, self.four_btn, self.six_btn, self.two_btn,
                           self.equal_btn, self.clear_btn, self.multiply_btn, self.three_btn, self.difference_btn,
                           self.division_btn, self.nine_btn, self.remove_btn, self.copy_btn, self.par_close_btn, self.seven_btn,
                           self.eight_btn, self.five_btn, self.zero_btn, self.point_btn):

                button.md_bg_color = "orange"


if __name__ == "__main__":
    CalculatorApp().run()


