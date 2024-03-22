import anvil
from anvil.tables import app_tables
from kivy.animation import Animation
from kivy.uix.popup import Popup

from kivy.core.window import Window
from kivy.factory import Factory
from kivy.properties import ListProperty, Clock
from kivy.uix.label import Label
from kivy.uix.modalview import ModalView
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivymd.uix.button import MDRectangleFlatButton, MDRaisedButton
from kivymd.uix.slider import MDSlider
from kivymd.uix.label import MDLabel
import sqlite3
from math import pow
from kivymd.uix.dialog import MDDialog, dialog
import anvil.server
from kivy.uix.spinner import Spinner
from datetime import datetime

from kivymd.uix.spinner import MDSpinner

user_helpers2 = """

<WindowManager>:
    NewloanScreen:
    NewloanScreen1:
    NewloanScreen2:
<NewloanScreen>:
    name: 'NewloanScreen' 
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        MDTopAppBar:
            title: "New Loan Request"
            elevation: 2
            pos_hint: {'top': 1}
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['home', lambda x:root.go_to_lender_dashboard()]]
            title_align: 'center'
            md_bg_color: 0.043, 0.145, 0.278, 1

        ScrollView:  # Add ScrollView here
            do_scroll_x: False
            BoxLayout:
                orientation: "vertical"
                padding:dp(10)
                spacing:dp(30)
                size_hint_y: None
                height: self.minimum_height


                Image:
                    source:"LOGO.png"
                    size_hint:None,None
                    size:"100dp","100dp"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.89}
                MDLabel:
                    text: "  Experience Hassle-Free Borrowing  " 
                    font_size:dp(15)
                    halign:"center"
                    bold:True
                    height:dp(50)
                    underline:True
                    italic:True
                    pos_hint: {'center_x': 0.5, 'center_y': 0.4}
                MDLabel:
                    text:""
                MDGridLayout:
                    cols: 2
                    padding: dp(25)
                    spacing: dp(10)
                    MDLabel:
                        text: "Credit Limit" 
                        color:0.031, 0.463, 0.91, 1
                        bold:True
                        size_hint_y:None
                        height:dp(50)
                        halign: "center"
                        font_size:dp(23)
                    MDLabel:
                        id: credit_limit        
                        text: "" 
                        size_hint_y:None
                        height:dp(50)
                        halign: "center"
                        font_size:dp(20)
                MDLabel:
                    text:""
                MDLabel:
                    text:""

                MDGridLayout:
                    cols: 2

                    padding: dp(25)
                    spacing: dp(20)
                    MDLabel:
                        font_size: dp(16)
                        text: "Product Group"
                        bold: True
                        size_hint_y:None
                        height:dp(50)
                        halign: "center"

                    Spinner:
                        id: group_id1
                        text: "Select Group"
                        width: dp(200)
                        multiline: False
                        size_hint: None, None
                        pos_hint: {'center_x':0.5, 'center_y':0.5}
                        size: "180dp", "45dp"
                        height:dp(50)
                        halign: "center"
                        background_color: 1, 1, 1, 0
                        color: 0, 0, 0, 1
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1
                            Line:
                                width: 0.7
                                rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                        on_press: app.fetch_product_groups()
                        text_size: self.width - dp(20), None
                MDLabel:
                    text:""
                MDLabel:
                    text:""


                MDGridLayout:
                    cols: 2

                    padding: dp(25)
                    spacing: dp(20)
                    MDLabel:
                        font_size:dp(16)
                        text: "Product Categories"
                        bold: True
                        size_hint_y:None
                        height:dp(50)
                        halign: "center"

                    Spinner:
                        id: group_id2
                        text: "Select Categories"
                        width: dp(200)
                        multiline: False
                        size_hint: None, None
                        height:dp(50)
                        halign: "center"
                        pos_hint: {'center_x':0.5, 'center_y':0.5}
                        size: "180dp", "45dp"
                        background_color: 1, 1, 1, 0
                        color: 0, 0, 0, 1
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1
                            Line:
                                width: 0.7
                                rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                        on_press: app.fetch_product_categories()
                        text_size: self.width - dp(20), None
                        disabled: not group_id1.text or group_id1.text == 'Select Group'
                MDLabel:
                    text:""
                MDLabel:
                    text:""

                MDGridLayout:
                    cols: 2

                    padding: dp(25)
                    spacing: dp(20)
                    MDLabel:
                        font_size:dp(16)
                        text: "Product Name"
                        bold: True
                        size_hint_y:None
                        height:dp(50)
                        halign: "center"
                    Spinner:
                        id: group_id3
                        text: "Select product name"
                        width: dp(200)
                        multiline: False
                        size_hint: None, None
                        height:dp(50)
                        halign: "center"
                        pos_hint: {'center_x':0.5, 'center_y':0.5}
                        size: "180dp", "45dp"
                        background_color: 1, 1, 1, 0
                        color: 0, 0, 0, 1
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1
                            Line:
                                width: 0.7
                                rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                        on_press: app.fetch_product_name()
                        text_size: self.width - dp(20), None
                        disabled: not group_id2.text or group_id2.text == 'Select Categories'
                        on_text: app.fetch_product_description()
                MDLabel:
                    text: " "  
                MDLabel:
                    text:"" 
                MDLabel:
                    text:""


                MDGridLayout:
                    cols: 2

                    padding: dp(25)
                    spacing: dp(20)
                    MDLabel:
                        font_size: dp(16)
                        text: "Product Description"
                        bold: True
                    MDLabel:
                        id: product_description
                        text: " "
                        font_size: dp(11)
                        size_hint_y: None
                        halign: "center"

                        height: self.texture_size[1] + dp(20) if self.text else 0  # Adjust height to fit content
                        canvas.before:
                            Color:
                                rgba: 1, 1, 1, 1  # Background color
                            RoundedRectangle:
                                size: self.size
                                pos: self.pos
                                radius: [15, 15, 15, 15]  # Adjust radius for rounded corners
                            Color:
                                rgba: 0.043, 0.145, 0.278, 1
                            Line:
                                width: 1.5
                                rectangle: (self.x, self.y, self.width, self.height)
                MDLabel:
                    text: " "  
                MDLabel:
                    text: " "  
                MDLabel:
                    text: " "  
                MDLabel:
                    text: " "
                MDLabel:
                    text: " "  


                MDGridLayout:
                    cols: 1
                    spacing: dp(10)
                    padding: dp(10)
                    MDRaisedButton:
                        text: "Next"
                        md_bg_color: 0.043, 0.145, 0.278, 1
                        on_release: root.go_to_newloan_screen1()
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint:1, None  
                        font_name:"Roboto-Bold"

                MDLabel:
                    text: " "  
                MDLabel:
                    text: " "
<NewloanScreen1>:
    MDTopAppBar:
        title: "New Loan Request"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: root.go_back()]]
        right_action_items: [['home', lambda x:root.go_to_lender_dashboard()]]
        title_align: 'center'
        md_bg_color: 0.043, 0.145, 0.278, 1
    BoxLayout:
        pos_hint: {'center_x':0.5, 'center_y':0.4}
        elevation: 2
        padding: dp(20)
        spacing: dp(20)
        orientation: 'vertical'
        radius: [10,]

        BoxLayout:
            orientation: "vertical"
            padding:dp(10)
            spacing:dp(10)
            size_hint_y: None
            height: self.minimum_height


            Image:
                source:"LOGO.png"
                size_hint:None,None
                size:"100dp","100dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}




        MDGridLayout:
            cols: 2
            padding: dp(25)
            spacing: dp(10)
            MDLabel:
                text: "Loan Amount"
                bold:True
                font_size:dp(16)
            MDTextField:
                id: text_input1
                width: dp(250)
                multiline: False
                hint_text: "Enter amount"
                size_hint: None, None
                size: "180dp", "45dp"
                on_text: root.validate_amount(text_input1,self.text)
                background_color: 1, 1, 1, 0 
                color: 0, 0, 0, 1
                line_color_normal: 0, 0, 0, 1  # Set the line color to black
                color: 0, 0, 0, 1
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                helper_text: ""
        MDLabel:
            text:""
        MDLabel:
            text:""

        MDGridLayout:
            cols: 2
            padding: dp(25)
            spacing: dp(10)

            MDLabel:
                text: "Loan Period (Months)"
                font_size:dp(16)
                bold:True

            MDTextField:
                id: text_input2
                size_hint_x: 0.91
                multiline: False
                hint_text: "Enter loan period"
                on_text: root.validate_tenure(text_input2,self.text)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                helper_text: ""
                helper_text_mode: "on_error"
                size_hint: None, None
                size: "180dp", "45dp"
                background_color: 1, 1, 1, 0 
                color: 0, 0, 0, 1
                line_color_normal: 0, 0, 0, 1  # Set the line color to black
                color: 0, 0, 0, 1
        MDLabel:
            text:""
        MDLabel:
            text:""
        MDGridLayout:
            cols: 2
            padding: dp(25)
            spacing: dp(10)
            MDLabel:
                font_size: dp(16)
                text: "EMI Type"
                bold: True

            Spinner:
                id: group_id4
                text: "Select EMI type"
                width: dp(200)
                multiline: False
                size_hint: None, None
                pos_hint: {'center_x':0.5, 'center_y':0.5}
                size: "180dp", "45dp"
                background_color: 1, 1, 1, 0
                color: 0, 0, 0, 1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1
                    Line:
                        width: 0.7
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                on_press: app.fetch_emi_type()
                text_size: self.width - dp(20), None
                disabled: not group_id4.text or group_id4.text == 'Select Categories'


        MDLabel:
            id: max_tenure 
            color:1,1,1,1      
            text: "" 
            font_size:dp(1)
        MDLabel:
            id: min_tenure 
            color:1,1,1,1      
            text: "" 
            font_size:dp(1)

        MDLabel:
            id: max_amount
            color:1,1,1,1      
            text: "" 
            font_size:dp(1)
        MDLabel:
            id: min_amount
            color:1,1,1,1      
            text: "" 
            font_size:dp(1)
        MDLabel:
            id: product_id
            color:1,1,1,1      
            text: "" 
            font_size:dp(1)
        MDFloatLayout:
            MDRaisedButton:
                text: "Next"
                md_bg_color:0.043, 0.145, 0.278, 1
                on_release:  root.go_to_newloan_screen2()
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint:0.4, None  
                font_name:"Roboto-Bold"
                font_size:dp(15)
        MDLabel:
            text: " "
        MDLabel:
            text: " "

<NewloanScreen2>:
    MDTopAppBar:
        title: "View Deatils"
        elevation: 2
        pos_hint: {'top': 1}

        title_align: 'center'
        md_bg_color: 0.043, 0.145, 0.278, 1
    BoxLayout:
        pos_hint: {'center_x':0.5, 'center_y':0.4}
        padding: dp(20)
        spacing: dp(20)
        orientation: 'vertical'

        BoxLayout:
            orientation: "vertical"


            size_hint_y: None
            height: self.minimum_height


            Image:
                source:"LOGO.png"
                size_hint:None,None
                size:"50dp","50dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        MDGridLayout:
            cols: 1

            MDLabel:
                text: "Loan Summary"
                halign: "center"
                font_size:dp(20)
                bold: True
                underline:"True"

        MDGridLayout:
            cols: 2
            spacing:dp(30)
            padding:dp(50)

            MDLabel:
                text: "Loan Amount"
                bold:True

            MDLabel:
                id: loan_amount
                text: ""
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                halign:"left"

        MDGridLayout:
            cols: 2
            spacing:dp(30)
            padding:dp(50)

            MDLabel:
                text: "Total Interest Amount"
                bold:True

            MDLabel:
                id: roi
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                text: " "
                halign:"left"
        MDGridLayout:
            cols: 2
            spacing:dp(30)
            padding:dp(50)

            MDLabel:
                text: " Total Processing Amount "
                bold:True

            MDLabel:
                id: processing_fee
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                text: ""
                halign:"left"

        MDGridLayout:
            cols: 2
            spacing:dp(30)
            padding:dp(50)

            MDLabel:
                text: "EMI Payment"
                bold:True

            MDLabel:
                id: monthly_emi
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                text: ""
                halign:"left"
        MDGridLayout:
            cols: 2
            spacing:dp(30)
            padding:dp(50)

            MDLabel:
                text: "Tenure"
                bold:True

            MDLabel:
                id:tenure
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                text: ""
                halign:"left"

        MDGridLayout:
            cols: 2
            spacing:dp(30)
            padding:dp(50)

            MDLabel:
                text: "Total Repayment Amount"
                bold:True

            MDLabel:
                id: total
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                text: " "
                halign:"left"

        MDLabel:
            text: " "
        MDLabel:
            text: " "
        MDFloatLayout:
            GridLayout:
                cols: 2
                spacing:dp(20)
                padding:dp(20)
                pos_hint: {'center_x': 0.5, 'center_y': 1}
                size_hint: 1, None
                height: "50dp"
                MDRaisedButton:
                    text: "Back"
                    on_release: app.root.current = "NewloanScreen1"
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    theme_text_color: 'Custom'
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"
                MDRaisedButton:
                    text: "Send request"
                    on_release: root.send_request()
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"
        MDLabel:
            text: " "
"""

Builder.load_string(user_helpers2)


class NewloanScreen(Screen):
    # Add this line to check if the build method is called

    def on_pre_enter(self, *args):
        Window.bind(on_keyboard=self.on_back_button)
        try:
            # Get the first row from the 'fin_borrower' table
            row = app_tables.fin_borrower.search()[0]  # Fetch the first row

            # Fetch the credit limit from the row
            credit_limit = row['credit_limit']

            # Update the credit_limit MDLabel with the fetched data
            self.ids.credit_limit.text = str(credit_limit)
        except Exception as e:
            print(f"Error: {e}")

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'DashboardScreen'

    def go_to_lender_dashboard(self):
        self.manager.add_widget(Factory.DashboardScreen(name='DashboardScreen'))
        self.manager.current = 'DashboardScreen'

    def current(self):
        self.manager.current = 'DashboardScreen'

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def go_to_newloan_screen1(self):
        # Check if all required fields are selected
        if (self.ids.group_id1.text == 'Select Group' or
                self.ids.group_id2.text == 'Select Categories' or
                self.ids.group_id3.text == 'Select product name'):
            # If any field is not selected, display a popup
            self.show_popup("Please select all fields.")
        else:
            # Show modal view with loading label
            modal_view = ModalView(size_hint=(None, None), size=(300, 100),
                                   background_color=(0, 0, 0, 0))  # Set background color to transparent

            # Create a loading label
            loading_label = Label(text="Loading...", font_size=25)
            modal_view.add_widget(loading_label)
            modal_view.open()

            # Animate the loading label
            Clock.schedule_once(lambda dt: self.animate_loading_text(loading_label, modal_view.height), 0.1)

            # Perform the actual action (e.g., fetching loan requests)
            # You can replace the sleep with your actual logic
            Clock.schedule_once(lambda dt: self.performance_go_to_newloan_screen1(modal_view), 2)

    def performance_go_to_newloan_screen1(self, modal_view):

        # selected_group = self.ids.group_id1.text
        # selected_category = self.ids.group_id2.text
        # self.selected_category = selected_category
        # self.selected_group = selected_group
        # Get the existing ScreenManager
        # product_name = self.ids.product_id1.text

        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        # Close the modal view after performing the action
        modal_view.dismiss()
        self.manager.add_widget(Factory.NewloanScreen1(name='NewloanScreen1'))
        self.manager.current = 'NewloanScreen1'
        # print(self.selected_category)
        # print(product_name)

    def show_popup(self, text):
        content = MDLabel(text=text)
        popup = Popup(title="Warning", content=content, size_hint=(None, None), size=(400, 200))
        popup.open()


class NewloanScreen1(Screen):
    selected_category = ""
    product_id = ""

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)
        self.root_screen = self.manager.get_screen('NewloanScreen')
        selected_category = self.root_screen.ids.group_id2.text
        selected_product_name = self.root_screen.ids.group_id3.text
        try:
            # Call the Anvil server function to get the latest credit limit for the specified customer_id
            tenure = app_tables.fin_product_details.search(product_name=selected_product_name)
            max_tenure = tenure[0]['max_tenure']
            min_tenure = tenure[0]['min_tenure']
            max_amount = tenure[0]['max_amount']
            min_amount = tenure[0]['min_amount']
            # Update the credit_limit MDLabel with the fetched data
            self.ids.max_tenure.text = str(max_tenure)
            self.ids.min_tenure.text = str(min_tenure)
            self.ids.max_amount.text = str(max_amount)
            self.ids.min_amount.text = str(min_amount)
        except anvil._server.AnvilWrappedError as e:
            print(f"Anvil error: {e}")

    def validate_amount(self, text_input, text):
        try:
            if not text:
                text_input.helper_text = ""
                text_input.error = False
                return

            amount = float(text)
            text_input.helper_text = ""
            if amount < float(self.ids.min_amount.text):
                text_input.helper_text = f"enter amount more than {self.ids.min_amount.text} "
                text_input.error = True
            elif amount > float(self.ids.max_amount.text):
                text_input.helper_text = f"enter amount less than {self.ids.max_amount.text}"
                text_input.error = True

            else:
                text_input.error = False

        except ValueError:
            text_input.helper_text = " Please enter a valid number "
            text_input.error = True

        def reset_helper_text(instance_textfield, value):
            instance_textfield.helper_text = ""
            instance_textfield.error = False

        text_input.bind(on_focus=reset_helper_text)

    def go_to_lender_dashboard(self):
        self.manager.add_widget(Factory.DashboardScreen(name='DashboardScreen'))
        self.manager.current = 'DashboardScreen'
    def reset_fields(self):
        self.ids.text_input1.text = ""
        self.ids.text_input2.text = ""
        self.ids.group_id3.text = "Select EMI Type"

    def validate_tenure(self, text_input, text):
        try:
            if not text:
                text_input.helper_text = ""
                text_input.error = False
                return

            tenure = float(text)
            text_input.helper_text = ""

            if tenure < float(self.ids.min_tenure.text):
                text_input.helper_text = f"enter tenure more than {self.ids.min_tenure.text} "
                text_input.error = True
            elif tenure > float(self.ids.max_tenure.text):
                text_input.helper_text = f"enter tenure less than {self.ids.max_tenure.text}"
                text_input.error = True
            else:
                text_input.error = False

        except ValueError:
            text_input.helper_text = " Please enter a valid number "
            text_input.error = True

        def reset_helper_text(instance_textfield, value):
            instance_textfield.helper_text = ""
            instance_textfield.error = False

        text_input.bind(on_focus=reset_helper_text)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'NewloanScreen'

    def current(self):
        self.manager.current = 'NewloanScreen'

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def go_to_newloan_screen2(self):
        # Show modal view with loading label
        modal_view = ModalView(size_hint=(None, None), size=(300, 100),
                               background_color=(0, 0, 0, 0))  # Set background color to transparent

        # Create a loading label
        loading_label = Label(text="Loading...", font_size=25)
        modal_view.add_widget(loading_label)
        modal_view.open()

        # Animate the loading label
        Clock.schedule_once(lambda dt: self.animate_loading_text(loading_label, modal_view.height), 0.1)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.performance_go_to_newloan_screen2(modal_view), 2)

    def performance_go_to_newloan_screen2(self, modal_view):

        loan_amount = self.ids.text_input1.text
        loan_tenure = self.ids.text_input2.text
        # Get the existing ScreenManager

        self.selected_category = self.root_screen.ids.group_id2.text
        # Create a new instance of the LoginScreen
        self.manager.add_widget(Factory.NewloanScreen2(name='NewloanScreen2'))
        self.manager.current = 'NewloanScreen2'

        modal_view.dismiss()


class NewloanScreen2(Screen):
    loan_amount = ""
    loan_tenure = ""
    product_name = ""

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)
        self.root_screen = self.manager.get_screen('NewloanScreen1')

        if self.root_screen and self.root_screen.ids:
            loan_amount = float(self.root_screen.ids.text_input1.text)
            self.loan_tenure = float(self.root_screen.ids.text_input2.text)  # Define loan_tenure here
            self.ids.loan_amount.text = str(loan_amount)
            selected_category = self.root_screen.selected_category
            self.ids.tenure.text = str(self.loan_tenure)
            # selected_product_name = self.root_screen.selected_product_name
            try:
                data = app_tables.fin_product_details.search(product_categories=selected_category)
                processing_fee = data[0]['processing_fee']
                roi = data[0]['roi']
                self.ids.roi.text = str(roi)
                self.ids.processing_fee.text = str(processing_fee)
                monthly_interest_rate = (roi / 100) / 12
                # Number of Monthly Installments
                num_installments = self.loan_tenure

                # Calculate EMI using the formula
                emi = (loan_amount * monthly_interest_rate * pow(1 + monthly_interest_rate, num_installments)) / \
                      (pow(1 + monthly_interest_rate, num_installments) - 1)
                total_repayment = emi * num_installments
                self.ids.monthly_emi.text = f"{float(emi):.2f}"
                self.ids.total.text = f"{total_repayment:.2f}"

            except anvil._server.AnvilWrappedError as e:
                print(f"Anvil error: {e}")

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'NewloanScreen1'

    def current(self):
        self.manager.current = 'NewloanScreen1'

    def generate_loan_id(self):
        loan_id = anvil.server.call('generate_loan_id')
        return loan_id

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def send_request(self):
        # Show modal view with loading label
        modal_view = ModalView(size_hint=(None, None), size=(300, 150),
                               background_color=(0, 0, 0, 0))  # Set background color to transparent

        # Create a loading label
        loading_label = Label(text="Loading...", font_size=25)
        modal_view.add_widget(loading_label)
        modal_view.open()

        # Animate the loading label
        Clock.schedule_once(lambda dt: self.animate_loading_text(loading_label, modal_view.height), 0.1)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.performance_send_request(modal_view), 2)

    def performance_send_request(self, modal_view):
        if self.ids.loan_amount and self.ids.roi and self.ids.total:
            loan_amount = float(self.ids.loan_amount.text)
            loan_tenure = float(self.root_screen.ids.text_input2.text)
            selected_category = self.root_screen.selected_category
            roi = float(self.ids.roi.text)
            total_repayment = float(self.ids.total.text)
            date_of_apply = datetime.now().date()

            try:
                loan_id = anvil.server.call(
                    'add_loan_data',
                    loan_amount,
                    loan_tenure,
                    roi,
                    total_repayment,
                    date_of_apply
                )
                modal_view.dismiss()
                self.show_success_dialog(f"Loan details added successfully! Loan ID: {loan_id}")
            except anvil._server.AnvilWrappedError as e:
                modal_view.dismiss()
                print(f"Anvil error: {e}")

    def show_success_dialog(self, text):
        dialog = MDDialog(
            text=text,
            size_hint=(0.8, 0.3),
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=lambda *args: self.open_dashboard_screen(dialog),
                    theme_text_color="Custom",
                    text_color=(0.043, 0.145, 0.278, 1),
                )
            ]
        )
        dialog.open()

    def open_dashboard_screen(self, dialog):

        dialog.dismiss()
        self.manager.current = 'DashboardScreen'


class MyScreenManager(ScreenManager):
    pass
