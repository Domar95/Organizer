from ..general_category import GeneralCategory
from ..record import Record


class DailyGoal(Record):
    def __init__(
        self,
        record_name,
        record_text,
        record_general_category,
        record_importance,
        record_date,
        duration=None,
    ):
        super().__init__(
            record_name,
            record_text,
            record_general_category,
            record_importance,
            record_date,
        )
        self.duration = duration


if __name__ == "__main__":
    general_category = GeneralCategory("Daily Goals", "To do daily")
    daily_goal = DailyGoal(1, "10 mins of meditation", general_category, 3, 10)
    print(daily_goal.record_general_category.count_categories())
    print(daily_goal.record_general_category.category_description)
    print(dir(daily_goal))
    print(daily_goal.get_instance_attributes())
    print(daily_goal.get_available_attributes())
