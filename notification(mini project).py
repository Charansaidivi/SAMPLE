from plyer import notification
import time
def get_time():
    hour=int(input("enter number of hours:"))
    m=int(input("enter number of minutes:"))
    return hour*3600+m*60
if __name__ == '__main__':
    t=get_time()
    b=20#15*60
    while True:
        time.sleep(t)
        notification.notify(
            title="***Take Rest***",
            message="After hours of focused studying, it's essential to recharge and rejuvenate by taking a well-deserved break to refresh the mind and enhance overall productivity.",
            app_icon="C:\\Users\\CHARANSAI &YASWITHA\\Downloads\\break.ico",  # Corrected path with double backslashes
            timeout=10
        )
        time.sleep(b)
        notification.notify(
            title="***Start work***",
            message="It's time to get back to work! Start your focused work session now.",
            app_icon="C:\\Users\\CHARANSAI &YASWITHA\\Downloads\\work.ico",  
            timeout=10
        )
        
        
        
        

        
