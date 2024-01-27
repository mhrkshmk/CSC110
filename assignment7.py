import doctest
from typing import Tuple, List

DAY = 0
MONTH = 1
YEAR = 2
#represents a date(year, month, day)
# 1 <= month and 12 >= month, day is between 1 and the number of days in the given month
DateInformation = tuple[0, 0, 0]

#represent a netflix show(the type of show, the title of the show, a list of show director names, a list of show actor names, the date the show was added)
# the date is as described in DateInformation
ShowInformation = tuple[str, str, list[str], list[str], DateInformation]

def multiply_by(numbers: list[int], multipliers: list[int]) -> None :
    """
    This function gets 2 list of integers, one of numbers, and one of multipliers, it will then multiply each element in the first list by the element which is in the same position in the second list.
    This function will result in the first list being changed, and it will not return a value.
    >>> multiply_by([1, 2, 3], [2, 4, 0])
    >>> multiply_by([1, 2, 3], [2, 4])
    >>> multiply_by([1, 2, 3], [2, 4, 0, 2])
    """
    while (len(multipliers) < len(numbers)) :
        multipliers.append(1)
    length = len(numbers)
    for i in range(length) :
        numbers[i] *= multipliers[i]

def create_date(date: str) -> DateInformation :
    """
    This function gets a date as string and it will return a DateInformation tuple consisting of year, month, and day
    The given string will be non empty and will contain a valid date
    >>> create_date('10-Jan-18')
    (2018, 1, 10)
    >>> create_date('22-Feb-00')
    (2000, 2, 22)
    >>> create_date('22-Mar-00')
    (2000, 3, 22)
    >>> create_date('19-Apr-01')
    (2001, 4, 19)
    >>> create_date('22-May-04')
    (2004, 5, 22)
    >>> create_date('04-Jun-17')
    (2017, 6, 4)
    >>> create_date('01-Jul-19')
    (2019, 7, 1)
    >>> create_date('15-Aug-21')
    (2021, 8, 15)
    >>> create_date('02-Sep-02')
    (2002, 9, 2)
    >>> create_date('30-Oct-21')
    (2021, 10, 30)
    >>> create_date('04-Nov-21')
    (2021, 11, 4)
    >>> create_date('16-Dec-03')
    (2003, 12, 16)
    """
    date_list = date.split('-')
    year = 2000 + int(date_list[YEAR])
    if date_list[MONTH] == 'Jan' :
        month = 1
    if date_list[MONTH] == 'Feb' :
        month = 2
    if date_list[MONTH] == 'Mar' :
        month = 3
    if date_list[MONTH] == 'Apr' :
        month = 4
    if date_list[MONTH] == 'May' :
        month = 5
    if date_list[MONTH] == 'Jun' :
        month = 6
    if date_list[MONTH] == 'Jul' :
        month = 7
    if date_list[MONTH] == 'Aug' :
        month = 8
    if date_list[MONTH] == 'Sep' :
        month = 9
    if date_list[MONTH] == 'Oct' :
        month = 10
    if date_list[MONTH] == 'Nov' :
        month = 11
    if date_list[MONTH] ==  'Dec' :
        month = 12
    day = int(date_list[DAY])
    date_info = (year, month, day)
    return date_info

def create_show(show_type: str, show_title: str, directors: str, actors: str, date: str) -> ShowInformation :
    """
    This function gets a string as show_type, another string as show title, a list of string as names of directors, a list of string as names of actors, and a date.
    It will the return a tuple with ShowInformation type, as described in lines 11 to 13
    >>> create_show('Movie', 'The Invention of Lying', 'Ricky Gervais:Matthew Robinson', 'Ricky Gervais:Jennifer Garner:Jonah Hill:Rob Lowe:Tina Fey', '02-Jan-18')
    ('Movie', 'The Invention of Lying', ['Ricky Gervais', 'Matthew Robinson'], ['Ricky Gervais', 'Jennifer Garner', 'Jonah Hill', 'Rob Lowe', 'Tina Fey'], (2018, 1, 2))
    >>> create_show('TV Show', 'The Mind Explained', '', 'Emma Stone', '12-Sep-09')
    ('TV Show', 'The Mind Explained', [], ['Emma Stone'], (2009, 9, 12))
    >>> create_show('Movie', 'The Bad Kids', 'Keith Fulton:Louis Pepe', '', '01-Apr-17')
    ('Movie', 'The Bad Kids', ['Keith Fulton', 'Louis Pepe'], [], (2017, 4, 1))
    >>> create_show('Movie', 'The Bad Kids', '', '', '01-Apr-17')
    ('Movie', 'The Bad Kids', [], [], (2017, 4, 1))
    """
    directors_list = []
    actors_list = []
    if directors != '' :
        directors_list = directors.split(':')
    if actors != '' :
        actors_list = actors.split(':')
    corrected_date = create_date(date)
    show_info = (show_type, show_title, directors_list, actors_list, corrected_date)
    return show_info

def get_titles(shows: list[ShowInformation]) -> list[str] :
    """
    This function gets a list of Show Information and will return a list of their titles.
    >>> get_titles([('Movie', 'The Invention of Lying', ['Ricky Gervais', 'Matthew Robinson'], ['Ricky Gervais', 'Jennifer Garner', 'Jonah Hill', 'Rob Lowe', 'Tina Fey'], (2018, 1, 2)), ('TV Show', 'The Mind Explained', [], ['Emma Stone'], (2009, 9, 12))])
    ['The Invention of Lying', 'The Mind Explained']
    >>> get_titles([])
    []
    """
    titles = []
    for show in shows :
        titles.append(show[1])
    return titles

def is_actor_in_show(show: ShowInformation, actor: str) -> bool :
    """
    This function gets a tuple of Show Information and an actors name, and will return True if that actor has had a role in the show, and False otherwise.
    >>> is_actor_in_show(('Movie', 'The Invention of Lying', ['Ricky Gervais', 'Matthew Robinson'], ['Ricky Gervais', 'Jennifer Garner', 'Jonah Hill', 'Rob Lowe', 'Tina Fey'], (2018, 1, 2)), 'Rob Lowe')
    True
    >>> is_actor_in_show(('Movie', 'The Invention of Lying', ['Ricky Gervais', 'Matthew Robinson'], ['Ricky Gervais', 'Jennifer Garner', 'Jonah Hill', 'Rob Lowe', 'Tina Fey'], (2018, 1, 2)), 'roB lowE')
    True
    >>> is_actor_in_show(('Movie', 'The Invention of Lying', ['Ricky Gervais', 'Matthew Robinson'], ['Ricky Gervais', 'Jennifer Garner', 'Jonah Hill', 'Rob Lowe', 'Tina Fey'], (2018, 1, 2)), 'Emma Stone')
    False
    """
    actors_list = show[3]
    for index in range(len(actors_list)) :
        actors_list[index] = actors_list[index].lower()
    actor = actor.lower()
    for actors in actors_list :
        if actors == actor :
            return True
    return False

def count_shows_before_date(shows: list[ShowInformation], date:  DateInformation) -> int :
    """
    This function gets a list of netflix show information as described in lines 11-13 and a date as Date Information described in lines 7-9, it will then count and return how many shows were added before the given date.
    >>> count_shows_before_date([('TV Show', 'x', ['a', 'b'], ['a', 'c'], (2019, 9, 1)), ('TV Show', 'y', [], [], (2017, 4, 1))], (2018, 12, 12))
    1
    >>> count_shows_before_date([('TV Show', 'x', ['a', 'b'], ['a', 'c'], (2018, 12, 12)), ('TV Show', 'y', [], [], (2018, 4, 1))], (2018, 12, 12))
    1
    >>> count_shows_before_date([('TV Show', 'x', ['a', 'b'], ['a', 'c'], (2018, 12, 13)), ('TV Show', 'y', [], [], (2018, 12, 1))], (2018, 12, 12))
    1
    """
    number_of_shows = 0
    for show in shows :
        show_date = show[4]
        if show_date[0] < date[0] :
            number_of_shows += 1
        if show_date[0] == date[0] and show_date[MONTH] < date[MONTH] :
            number_of_shows += 1
        if show_date[0] == date[0] and show_date[MONTH] == date[MONTH] and show_date[2] < date[2] :
            number_of_shows += 1
    return number_of_shows

def get_shows_with_actor(shows: list[ShowInformation], actor: str) -> list[ShowInformation] :
    """
    This function gets a list of show information and an actors name as string, and then will return all the shows that the given actor has appeared in.
    >>> get_shows_with_actor([('TV Show', 'a', [], ['Emma Stone'], (2019, 9, 12)), ('TV Show', 'b', [], ['Emma stone'], (2019, 9, 12)), ('TV Show', 'c', [], ['Tom Hardy'], (2019, 9, 12))], 'emma sTone')
    [('TV Show', 'a', [], ['Emma Stone'], (2019, 9, 12)), ('TV Show', 'b', [], ['Emma stone'], (2019, 9, 12))]
    >>> get_shows_with_actor([('TV Show', 'a', [], ['Emma Stone'], (2019, 9, 12)), ('TV Show', 'b', [], ['Emma stone'], (2019, 9, 12)), ('TV Show', 'c', [], ['Tom Hardy'], (2019, 9, 12))], 'Martin Freeman')
    []
    >>> get_shows_with_actor([], 'Martin Freeman')
    []
    """
    actor = actor.lower()
    actors_shows = []
    for show in shows :
        actor_list = []
        for actors in show[3] :
            name = actors
            actor_list.append(name.lower())
        for actors in actor_list :
            if actors == actor :
                actors_shows.append(show)
    return actors_shows