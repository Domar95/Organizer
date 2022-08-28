from .models import *
from .db_manager import DBManager
from sqlalchemy.orm import sessionmaker


class DummyDataCreator():
    def __init__(self, engine):
        self.engine = engine

    def add_categories(self):
        Session = sessionmaker(self.engine)
        with Session() as session:
            my_category1 = GeneralCategory(
                category_name="Daily Goals",
                category_description="Things to do on a daily basis",
            )
            my_category2 = GeneralCategory(
                category_name="Programming Projects",
                category_description="Ideas for programming projects to build in near future",
            )
            my_category3 = GeneralCategory(
                category_name="Ideas To Implement",
                category_description="General improvement ideas to implement into real life",
            )
            my_category4 = GeneralCategory(
                category_name="Info",
                category_description="General information that may hold value",
            )
            my_category5 = GeneralCategory(
                category_name="Thoughts",
                category_description="Personal thoughts or reflections that may hold value",
            )
            my_category6 = GeneralCategory(
                category_name="Others",
                category_description="All other stuff that needs to be stored",
            )

            session.add_all(
                [
                    my_category1,
                    my_category2,
                    my_category3,
                    my_category4,
                    my_category5,
                    my_category6,
                ]
            )

            session.commit()

    def add_records(self, number):
        Session = sessionmaker(self.engine)
        with Session() as session:
            for i in range(1, number):
                my_goal = DailyGoal(
                    record_name=(f"My {i} daily goal"),
                    record_text="Daily goal description",
                    record_general_category_id=1,
                    record_importance=0,
                    record_date="01.01.2022",
                    record_duration=0,
                )

                my_idea = Idea(
                    record_name=(f"My {i} idea"),
                    record_text="Idea description",
                    record_general_category_id=3,
                    record_importance=0,
                    record_date="01.01.2022",
                    record_deadline="01.01.2023",
                    record_domain="Food",
                )

                my_info = Info(
                    record_name=(f"My {i} info"),
                    record_text="Info description",
                    record_general_category_id=4,
                    record_importance=0,
                    record_date="01.01.2022",
                    record_domain="Health",
                    record_link="link to website with more information or source",
                    record_image="related image if available",
                )

                my_other_record = OtherRecord(
                    record_name=(f"My {i} other record"),
                    record_text="Other record description",
                    record_general_category_id=6,
                    record_importance=0,
                    record_date="01.01.2022",
                    record_deadline="01.01.2022",
                    record_domain="Workout",
                    record_link="link to website with more information or source",
                    record_image="related image if available",
                )

                my_programming_project = ProgrammingProject(
                    record_name=(f"My {i} programming project"),
                    record_text="Programming project description",
                    record_general_category_id=2,
                    record_importance=0,
                    record_date="01.01.2022",
                    record_deadline="01.01.2022",
                    record_used_technologies="Python, Flask, MySQL",
                )

                my_reflection = Reflection(
                    record_name=(f"My {i} reflection"),
                    record_text="Reflection description",
                    record_general_category_id=5,
                    record_importance=0,
                    record_date="01.01.2022",
                    record_deadline="01.01.2022",
                    record_domain="Activities",
                    record_link="link to website with more information or source",
                )

                session.add_all(
                    [
                        my_goal,
                        my_idea,
                        my_info,
                        my_other_record,
                        my_programming_project,
                        my_reflection,
                    ]
                )

                session.commit()


if __name__ == "__main__":
    db_manager = DBManager()
    db_manager.start_engine()
    engine = db_manager.engine

    dummy_data_creator = DummyDataCreator(engine)
    dummy_data_creator.add_records(16)
