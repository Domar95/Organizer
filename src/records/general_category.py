class GeneralCategory:

    general_categories = [
        "Daily Goals",
        "Programming Projects",
        "Ideas To Implement",
        "Info",
        "Thoughts",
        "Others",
    ]

    def __init__(self, category_name: str, category_description=None):
        self.category_name = category_name
        self.category_description = category_description

    def count_categories(self):
        return len(self.general_categories)

    def __str__(self):
        """
        User-friendly representation of category
        """
        pass

    def __repr__(self):
        """
        Developer-friendly representation of category
        """
        pass


if __name__ == "__main__":
    category = GeneralCategory("Daily Goals")
    print(category.category_name)
    print(category.category_description)
    print(category.count_categories())
