from abc import ABC, abstractmethod

from .general_category import GeneralCategory


class Record(ABC):
    @abstractmethod
    def __init__(
        self,
        record_name: str,
        record_text: str,
        record_general_category: GeneralCategory,
        record_importance=None,
        record_date=None,
    ):
        self.record_name = record_name
        self.record_text = record_text
        self.record_general_category = record_general_category
        self.record_importance = record_importance
        self.record_date = record_date

    def __str__(self):
        """
        User-friendly representation of record
        """
        pass

    def __repr__(self):
        """
        Developer-friendly representation of record
        """
        pass

    def get_available_attributes(self):
        return [
            "record_name",
            "record_text",
            "record_general_category",
            "record_importance",
            "record_date",
            "duration",
            "deadline",
            "domain",
            "link",
            "image",
            "used_technologies",
        ]

    def get_instance_attributes(self):

        attributes = []

        for attribute in dir(self):
            if not attribute.startswith("_"):
                attributes.append(attribute)

        return attributes


if __name__ == "__main__":
    general_category = GeneralCategory("Daily Goals", "To do daily")
    record = Record("Meditation", "10 mins of meditation", general_category)
    print(record.record_general_category.category_name)
