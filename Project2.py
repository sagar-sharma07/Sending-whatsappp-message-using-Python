import pywhatkit

phone_numer = ''
group_id = ''
message = ''
time_hour = 19
time_minute = 57
waiting_time_to_send = 15
close_tab = True
waiting_time_to_close = 2

mode = "contact"

if mode == "contact":
    pywhatkit.sendwhatmsg(phone_numer, message, time_hour, time_minute, waiting_time_to_send, close_tab, waiting_time_to_close)
elif mode == "group":
    pywhatkit.sendwhatmsg_to_group(group_id, message, time_hour, time_minute, waiting_time_to_send, close_tab, waiting_time_to_close)
else:
    print("Error code: 97654")
    print("Error Message: Please select a mode to send your message.")
