import time
import calendar

Calendar = calendar.month(2025,1)
Calendar = calendar.calendar(2025,w=2,l=1,c=6)
tick = time.asctime( time.localtime(time.time()) )
print(Calendar)
print(tick)
