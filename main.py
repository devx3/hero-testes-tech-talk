def return_age_between_two_years(birth_year: int, year_to_compare: int) -> int:
    """
    Return a age.

    Args:
        birth_year (int): The birth year of user
        year_to_compare (int): The year to compare and discover the age

    Returns:
        age (int): The age of user.
    """
    age = year_to_compare - birth_year
    return age
