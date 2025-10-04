from datetime import datetime, time


def is_restaurant_open():
    """
    Chech if  the restaurant is currently open based on hardcoded opening hours. 
    Retyrn True if open, False otherwise.
    """


    # Get current datetime info
    now = datetime.now()
    current_time = now.time()
    current_day = now.weekday()   # Monday = 0, Sunday = 6



    # Example opening hours
    # Weekend (Mon-Fri): 9AM to 10PM
    weekday_open = time(9,0)  # 09:00 AM
    weekday_close = time(23,0) # 11:00 PM


    # Check weekday vs weekend
    if current_day <5:  # Monday to Friday
       return weekday_open <= current_time <= weekday_close
    else:  # Saturday, Sunday
        return weekend_open <= current_time <= weekend_close