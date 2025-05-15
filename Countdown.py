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


ft.app(target=main)