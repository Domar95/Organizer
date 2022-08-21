from .models import *


class DailyGoalForm():

    def __init__(self):
        my_goal = DailyGoal(
            record_name="My first daily goal",
            record_text="Daily goal description",
            record_general_category_id=1,
            record_importance=6,
            record_date="20.08.2022",
            record_duration=10,
        )


if __name__ == "__main__":
    form_provider = FormProvider(daily_goal=DailyGoal)
    print(form_provider.daily_goal)
