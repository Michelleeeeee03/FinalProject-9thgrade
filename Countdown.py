#Credits: 
# https://flet.dev/docs/controls/datepicker/
#https://flet.dev/docs/controls/timepicker/

import flet as ft
import flet_timer as ftt
import time
import datetime

def main (page: ft.Page):
    page.title = "Countdown App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def handle_change(e):
        page.add(ft.Text(f"Date changed: {e.control.value.strftime('%Y/%m/%d')}"))
        today = datetime.date.today()
        

    def handle_dismissal(e):
        page.add(ft.Text(f"DatePicker dismissed"))

    #------------------------------------------------------------------------

    def handle_change(e):
        page.add(ft.Text(f"TimePicker change: {time_picker.value}"))

    def handle_dismissal(e):
        page.add(ft.Text(f"TimePicker dismissed: {time_picker.value}"))

    def handle_entry_mode_change(e):
        page.add(ft.Text(f"TimePicker Entry mode changed to {e.entry_mode}"))

    time_picker = ft.TimePicker(
            confirm_text="Confirm",
            error_invalid_text="Time out of range",
            help_text="Pick your time slot",
            on_change=handle_change,
            on_dismiss=handle_dismissal,
            on_entry_mode_change=handle_entry_mode_change,
        )

    date_picker = ft.DatePicker(
        first_date=datetime.datetime.now(), 
        last_date=datetime.datetime(year=2050, month=1, day=1),
        on_change=handle_change,
        on_dismiss=handle_dismissal,
    )

    page.add(ft.ElevatedButton(
         "Pick date",
        icon=ft.Icons.CALENDAR_MONTH,
        on_click=lambda e: page.open(date_picker),
        ),
        ft.ElevatedButton(
        "Pick time",
        icon=ft.Icons.TIME_TO_LEAVE,
        on_click=lambda _: page.open(time_picker),
        ))
    
ft.app(target=main)