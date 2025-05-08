import flet as ft

def main (page: ft.Page):
    page.title = "Countdown App"

    month_dropdown = ft.Dropdown(label="Hour", 
        options=[
            ft.dropdown.Option("12 AM"), 
            ft.dropdown.Option("01 AM"), 
            ft.dropdown.Option("02 AM"),
            ft.dropdown.Option("03 AM"),
            ft.dropdown.Option("04 AM"),
            ft.dropdown.Option("05 AM"),
            ft.dropdown.Option("06 AM"),
            ft.dropdown.Option("07 AM"),
            ft.dropdown.Option("08 AM"),
            ft.dropdown.Option("09 AM"),
            ft.dropdown.Option("10 AM"),
            ft.dropdown.Option("11 AM"),
            ft.dropdown.Option("12 PM"),
            ft.dropdown.Option("01 PM"),
            ft.dropdown.Option("02 PM"),
            ft.dropdown.Option("03 PM"),
            ft.dropdown.Option("04 PM"),
            ft.dropdown.Option("05 PM"),
            ft.dropdown.Option("06 PM"),
            ft.dropdown.Option("07 PM"),
            ft.dropdown.Option("08 PM"),
            ft.dropdown.Option("09 PM"),
            ft.dropdown.Option("10 PM"),
            ft.dropdown.Option("11 PM"),
            ])
    
    

ft.app(target=main)