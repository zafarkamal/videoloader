import datetime
import django
def day_to_goal_cal():
    user_input = "Learning Python:2024-08-31"
    user_input_list = user_input.split(":")
    current_date = datetime.datetime.today()
    goal_date = datetime.datetime.strptime(user_input_list[1],"%Y-%m-%d")
    days_to_goal = goal_date - current_date
    return days_to_goal


