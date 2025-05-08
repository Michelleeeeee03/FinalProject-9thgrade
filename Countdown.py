import flet as ft

def main (page: ft.Page):
    page.title = "Countdown App"

    month_dropdown = ft.Dropdown(label="12 AM", 
        options=[
            ft.dropdown.Option("12 AM"), 
            ft.dropdown.Option("01 AM"), 
            ft.dropdown.Option("02 AM"),
            ])
    

ft.app(target=main)