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
import flet_timer as ftt
import time
import datetime
import threading

def main (page: ft.Page):
    page.title = "Countdown App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    selected_date = None
    selected_time = None 
    event_title = "My Awesome Event"

    # Text to display the countdown
    countdown_display_text = ft.Text(
        "Please select a date and time to start the countdown.", 
        size=24,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER)
    
    # Text to display the selected date
    selected_date_display = ft.Text(
        "Selected date: Not set",
        size=16,
        weight=ft.FontWeight.NORMAL,
        text_align=ft.TextAlign.CENTER)

    # Text to display the selected time
    selected_time_display = ft.Text(
        "Selected time: Not set",
        size=16,
        weight=ft.FontWeight.NORMAL,
        text_align=ft.TextAlign.CENTER)

    def handle_change_d(e):
        nonlocal selected_date
        selected_date = e.control.value
        selected_date_display.value = f"Selected Date: {selected_date.strftime('%Y-%m-%d')}" # Update display
        page.update(selected_date_display) 
        update_countdown_display()
        
    def handle_dismissal_d(e):
        pass

    def handle_change_t(e):
        nonlocal selected_time
        selected_time = e.control.value
        selected_time_display.value = f"Selected time: {selected_time.strftime('%H:%M:%S')}" # Update display
        page.update(selected_time_display) 
        update_countdown_display()

    def handle_dismissal_t(e):
        pass

    def event_title_changed(e):
        nonlocal event_title
        event_title = e.control.value
        update_countdown_display()
        page.update(event_title) # Update the text field if its value changed internally

    def update_countdown_display():
        # Updates the countdown text based on selected date/time and event title.
        # Only proceed if both date and time are selected
        if selected_date and selected_time:
            combined_datetime = datetime.datetime.combine(selected_date, selected_time)
            time_difference = combined_datetime - datetime.datetime.now()

            if time_difference.total_seconds() <= 0:
                countdown_display_text.value = f"{event_title} has already passed!"
            else:
                days = time_difference.days
                remaining_seconds_in_day = time_difference.seconds 
                
                hours = remaining_seconds_in_day // 3600
                minutes = (remaining_seconds_in_day % 3600) // 60
                seconds = remaining_seconds_in_day % 60
                
                countdown_display_text.value = (
                    f"{event_title} in:\n"
                    f"{days}d : {hours:02}h : {minutes:02}m : {seconds:02}s")
        else:
            # If date or time is missing, display the initial instruction
            countdown_display_text.value = "Please select a date and time to start the countdown."
        
        page.update(countdown_display_text) # Only update the countdown text for efficiency

    def start_realtime_countdown():
        """Starts a background thread to update the countdown every second."""
        while True:
            update_countdown_display()
            time.sleep(1)

    #--------------------------------------------------------------------------------------------------------

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

    event_title = ft.TextField(
        label="Event Title",
        value=event_title, 
        width=300,
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

    page.add(
        event_title,
        ft.Row([date_button, time_button],
        alignment=ft.MainAxisAlignment.CENTER),
        selected_date_display,
        selected_time_display,
        ft.Divider(), 
        countdown_display_text)
    
    # Start the real-time countdown in a separate thread
    threading.Thread(target=start_realtime_countdown, daemon=True).start()

ft.app(target=main)