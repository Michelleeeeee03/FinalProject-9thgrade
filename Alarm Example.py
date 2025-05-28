from flet import *
from time import localtime, sleep, strftime

def main(page:Page):
    
    #GET REALTIME NOW
    now = lambda : strftime("%H:%M:%S", localtime())
    mytime = Text(value=now(), size=60, weight= "bold")

    #NOW SET ALARM IF TIME IS YOUR VALUE INPUT 
    #SHOW MODAL
    #SHOW DIALOG TEXT
    setalarm = TextField(label="Insert your time")

    def showalarm():
        if mytime.value == setalarm.value:
            #AND SHOW DIALOG ALERT
            dialogtime = AlertDialog(
                title = Text(f"your time is {mytime.value}",
                            size=50, color="red"))
            
            page.dialog = dialogtime
            dialogtime.open = True
            page.update()

    page.add(
        Column([
            Text("Alarm App", size=30, weight= "bold"),
            Row([mytime], alignment="center"),
            setalarm, 
            ElevatedButton("set Now", bgcolor="blue", 
                color="white", on_click=showalarm
                                     )])
    )

    def realtimeTime():
        #CHECK TIME AND UPDATE TEXT EVERY 1 SECONDS
        while True:
            mytime.value = now()
            mytime.update()
            #IF NOT VALUE INPUT, NOT TIME NOW
            #NOT SHOW ALERT
            showalarm()
            sleep(1)

    realtimeTime()

app(target=main)