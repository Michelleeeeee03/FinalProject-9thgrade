# Credits:
# https://flet.dev/docs/
# https://flet.dev/docs/controls/datepicker/
# https://flet.dev/docs/controls/timepicker/
# https://www.tickcounter.com/
# https://www.youtube.com/watch?v=vxXhJ1Qk8No&t=177s
# https://github.com/yafethtb/flet-countdown-timer/blob/main/timecounter.py
# https://docs.python.org/3/library/time.html
# https://docs.python.org/3/library/datetime.html
# https://docs.python.org/3/library/threading.html

import flet as ft
import time
import datetime
import threading

def main (page: ft.Page):
    page.title = "Countdown Event App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER 
    event_title_text_value = "My Awesome Event"
    page.theme_mode = "light" 
     
    selected_date = None
    selected_time = None 
    
    # EMELY
    def toggle_theme(e):
        if theme_switch.value:
            page.theme_mode = "dark"
            theme_switch.label = "Light Mode"  
        else:
            page.theme_mode = "light"
            theme_switch.label = "Dark Mode"
        page.update()

    theme_switch = ft.Switch(label="Dark Mode", value=False, on_change=toggle_theme)

    countdown_display_text = ft.Text(
        "Please select a date and time to start the countdown.", 
        size=30,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER)
    
    selected_date_display = ft.Text(
        "Selected date: Not set",
        size=20,
        weight=ft.FontWeight.NORMAL,
        text_align=ft.TextAlign.CENTER)

    selected_time_display = ft.Text(
        "Selected time: Not set",
        size=20,
        weight=ft.FontWeight.NORMAL,
        text_align=ft.TextAlign.CENTER)

    # MICHELLE
    def handle_change_d(e):
        nonlocal selected_date
        selected_date = e.control.value
        selected_date_display.value = f"Selected Date: {selected_date.strftime('%Y-%m-%d')}"
        page.update(selected_date_display) 
        update_countdown_display()
        
    def handle_dismissal_d(e):
        pass

    def handle_change_t(e):
        nonlocal selected_time
        selected_time = e.control.value
        selected_time_display.value = f"Selected time: {selected_time.strftime('%H:%M:%S')}"
        page.update(selected_time_display) 
        update_countdown_display()

    def handle_dismissal_t(e):
        pass

    def event_title_changed(e):
        nonlocal event_title_text_value 
        event_title_text_value = e.control.value
        event_title_field.value = event_title_text_value 
        page.update(event_title_field) 

        update_countdown_display()

    def update_countdown_display():
        current_event_title = event_title_text_value if event_title_text_value.strip() else "My Awesome Event"

        if selected_date and selected_time:
            combined_datetime = datetime.datetime.combine(selected_date, selected_time)
            time_difference = combined_datetime - datetime.datetime.now()

            if time_difference.total_seconds() <= 0:
                countdown_display_text.value = f"{current_event_title} has already passed!"
            else:
                days = time_difference.days
                remaining_seconds_in_day = time_difference.seconds 
                
                hours = remaining_seconds_in_day // 3600
                minutes = (remaining_seconds_in_day % 3600) // 60
                seconds = remaining_seconds_in_day % 60
                
                countdown_display_text.value = (
                    f"{current_event_title} in:\n"
                    f"{days}d : {hours:02}h : {minutes:02}m : {seconds:02}s")
        else:
            countdown_display_text.value = "Please select a date and time to start the countdown."
        
        page.update(countdown_display_text)

    def start_realtime_countdown():
        # Starts a background thread to update the countdown every second.
        while True:
            update_countdown_display()
            time.sleep(1)

    #--------------------------------------------------------------------------------------------------------
    # EMELY
    time_picker = ft.TimePicker(
    confirm_text="Confirm",
    error_invalid_text="Time out of range",
    help_text="Pick your time slot",
    on_change=handle_change_t,
    on_dismiss=handle_dismissal_t)

    date_picker = ft.DatePicker(
    first_date=datetime.datetime.now(),
    last_date=datetime.datetime(year=2050, month=1, day=1),
    on_change=handle_change_d,
    on_dismiss=handle_dismissal_d)

    # MICHELLE
    event_title_field = ft.TextField(
        label="Event Title",
        value=event_title_text_value, 
        width=500,
        text_align=ft.TextAlign.CENTER,
        on_change=event_title_changed)

    date_button = ft.ElevatedButton(
        "Pick date",
        icon=ft.Icons.CALENDAR_MONTH,
        on_click=lambda e: page.open(date_picker))

    time_button = ft.ElevatedButton(
        "Pick time",
        icon=ft.Icons.ACCESS_TIME,
        on_click=lambda _: page.open(time_picker))
    
    # ESMERALDA
    birthday_img = ft.Image(src=".", height=400, width=400)
    christmas_img = ft.Image(src=".", height=400, width=400)
    newyear_img = ft.Image(src=".", height=400, width=400)
    easter_img = ft.Image(src=".", height=400, width=400)
    summer_img = ft.Image(src=".", height=400, width=400)
    independenceday_img = ft.Image(src=".", height=400, width=400)
    halloween_img = ft.Image(src=".", height=400, width=400)
    thanksgiving_img = ft.Image(src=".", height=400, width=400)
    firstdayofschool_img = ft.Image(src=".", height=400, width=400)
    valentinesday_img = ft.Image(src=".", height=400, width=400)
    
    def process(e):
        if dropdown_btn.value == "Birthday":
            birthday_img.src = "birthdaycake.jpg"
        else:
            birthday_img.src = "."
    
        if dropdown_btn.value == "Christmas Day":
            christmas_img.src = "christmas.jpg"
        else:
            christmas_img.src = "."
    
        if dropdown_btn.value == "New Year's Day":
            newyear_img.src = "newyear.jpg"
        else:
            newyear_img.src = "."
    
        if dropdown_btn.value == "Easter":
            easter_img.src = "easter.jpg"
        else:
            easter_img.src = "."
    
        if dropdown_btn.value == "Summer Vacation":
            summer_img.src = "summer.jpg"
        else:
            summer_img.src = "."
    
        if dropdown_btn.value == "Independence Day":
            independenceday_img.src = "independenceday.jpg"
        else:
            independenceday_img.src = "."
    
        if dropdown_btn.value == "Halloween":
            halloween_img.src = "halloween.jpg"
        else:
            halloween_img.src = "."
    
        if dropdown_btn.value == "Thanks Giving":
            thanksgiving_img.src = "thanksgiving.jpg"
        else:
            thanksgiving_img.src = "."
    
        if dropdown_btn.value == "First Day of School":
            firstdayofschool_img.src = "firstdayofschool.jpg"
        else:
            firstdayofschool_img.src = "."
    
        if dropdown_btn.value == "Valentine's Day":
            birthday_img.src = "valentinesday.jpg"
        else:
            valentinesday_img.src = "."
        page.update()

    dropdown_btn = ft.Dropdown(
            label="Events",
            options=[
            ft.dropdown.Option("Birthday"),
            ft.dropdown.Option("Christmas Day"),
            ft.dropdown.Option("New Year's Day"),
            ft.dropdown.Option("Easter"),
            ft.dropdown.Option("Summer Vacation"),
            ft.dropdown.Option("Independence Day"),
            ft.dropdown.Option("Halloween"),
            ft.dropdown.Option("Thanks Giving"),
            ft.dropdown.Option("First Day of School"),
            ft.dropdown.Option("Valentine's Day")], on_change=process)
 
    page.add(
        event_title_field, 
        ft.Row([dropdown_btn]),
        ft.Row([theme_switch]),
        ft.Row([date_button, time_button]),
        selected_date_display,
        selected_time_display,
        ft.Divider(), 
        countdown_display_text,
        ft.Stack([birthday_img, christmas_img, newyear_img, easter_img, summer_img, 
        independenceday_img, halloween_img, thanksgiving_img, firstdayofschool_img, valentinesday_img]))
    
    threading.Thread(target=start_realtime_countdown, daemon=True).start()

ft.app(target=main, assets_dir="assets")