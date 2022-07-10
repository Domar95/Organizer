from .general_category import GeneralCategory
from .record import Record


class Reflection(Record, GeneralCategory):
    def __init__(
        self,
        record_name,
        record_text,
        record_general_category,
        record_importance,
        record_date,
        deadline=None,
        domain=None,
        link=None,
    ):
        super().__init__(
            record_name,
            record_text,
            record_general_category,
            record_importance,
            record_date,
        )
        self.deadline = deadline
        self.domain = domain
        self.link = link


if __name__ == "__main__":
    general_category = GeneralCategory("Daily Goals", "To do daily")
    daily_goal = Reflection(1, "10 mins of meditation", general_category, 3, 10)
    print(daily_goal.count_categories())
    print(daily_goal.record_general_category.category_description)
