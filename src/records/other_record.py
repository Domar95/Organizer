from .general_category import GeneralCategory
from .record import Record


class OtherRecord(Record, GeneralCategory):
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
        image=None,
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
        self.image = image


if __name__ == "__main__":
    general_category = GeneralCategory("Daily Goals", "To do daily")
    daily_goal = OtherRecord(1, "10 mins of meditation", general_category, 3, 10)
    print(daily_goal.count_categories())
    print(daily_goal.record_general_category.category_description)
