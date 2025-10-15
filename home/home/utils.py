import datetime import datetime, time

def is_restaurant_open():
    """
    Checks if the restaurant is open basec on hardcoded opening hours.
    Returns True if open, False if closed.
    """



    #  Define opening hours (24-hour format)
    # Monday=0, Tuesday=1, ..., Sunday=6
    opening_hours = {
        0: (time(9,0), time(22,0)),  # Monday
        1: (time(9,0), time(22,0)), # Tuesday
        2: (time(9,0), time(22,0)), # Wednesday
        3: (time(9,0), time(22,0)), # Thursday
        4: (time(9,0), time(22,0)), # Friday
        5: (time(9,0), time(22,0)), # Saturday
        6: None                     # Sunday closed 
    }
 


    if open_time <= current_time <= close_time:
        return True

        
    else:
        return false
        