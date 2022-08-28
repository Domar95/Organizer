from ..db.models import GeneralCategory, DailyGoal, Idea, Info, OtherRecord, ProgrammingProject, Reflection


class RecordFactory():

    def get_record_object(self, record):
        records = dict(daily_goal=DailyGoal(
            record_name="Dummy daily goal",
            record_text="Dummy description",
            record_general_category_id=1,
            record_importance=0,
            record_date="01.01.2022",
            record_duration=0,
        ), programming_project=ProgrammingProject(
            record_name="Dummy programming project",
            record_text="Dummy description",
            record_general_category_id=2,
            record_importance=0,
            record_date="01.01.2022",
            record_deadline="01.01.2022",
            record_used_technologies="Python, Flask, MySQL",
        ), idea=Idea(
            record_name="Dummy idea",
            record_text="Dummy description",
            record_general_category_id=3,
            record_importance=0,
            record_date="01.01.2022",
            record_deadline="01.01.2023",
            record_domain="Food",
        ), info=Info(
            record_name="Dummy info",
            record_text="Dummy description",
            record_general_category_id=4,
            record_importance=0,
            record_date="01.01.2022",
            record_domain="Health",
            record_link="link to website with more information or source",
            record_image="related image if available",
        ), reflection=Reflection(
            record_name="Dummy reflection",
            record_text="Dummy description",
            record_general_category_id=5,
            record_importance=0,
            record_date="01.01.2022",
            record_deadline="01.01.2022",
            record_domain="Activities",
            record_link="link to website with more information or source",
        ), other_record=OtherRecord(
            record_name="Dummy other record",
            record_text="Dummy description",
            record_general_category_id=6,
            record_importance=0,
            record_date="01.01.2022",
            record_deadline="01.01.2022",
            record_domain="Workout",
            record_link="link to website with more information or source",
            record_image="related image if available",
        ))
        return records[record]

    def get_record_class(self, record):
        records = dict(daily_goal=DailyGoal, programming_project=ProgrammingProject,
                       idea=Idea, info=Info, reflection=Reflection, other_record=OtherRecord)
        return records[record]


if __name__ == "__main__":
    record = RecordFactory()
    print(record.get_record_object('daily_goal'))
    print(record.get_record_class('daily_goal'))
