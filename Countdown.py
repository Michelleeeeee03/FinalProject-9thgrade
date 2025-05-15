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

    def main (page: ft.Page):
        page.title = "Countdown App"
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def handle_change(e):
        page.add(ft.Text(f"Date changed: {e.control.value.strftime('%m/%d/%Y')}"))

    def handle_dismissal(e):
        page.add(ft.Text(f"DatePicker dismissed"))

    #------------------------------------------------------------------------

    def handle_change(e):
        page.add(ft.Text(f"TimePicker change: {time_picker.value}"))

    def handle_dismissal(e):
        page.add(ft.Text(f"TimePicker dismissed: {time_picker.value}"))

    def handle_entry_mode_change(e):
        page.add(ft.Text(f"TimePicker Entry mode changed to {e.entry_mode}"))

ft.app(target=main)