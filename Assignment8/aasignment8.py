import doctest
import csv

# all 2 digit years assumed to be in the 2000s
START_YEAR = 2000

# represents a Gregorian date as (year, month, day)
#  where year>=START_YEAR,
#  month is a valid month, 1-12 to represent January-December
#  and day is a valid day of the given month and year
Date = tuple[int, int, int]
YEAR  = 0
MONTH = 1
DAY   = 2

# represents a Netflix show as (show type, title, directors, cast, date added)
#  where none of the strings are empty strings
NetflixShow = tuple[str, str, list[str], list[str], Date]
TYPE      = 0
TITLE     = 1
DIRECTORS = 2
CAST      = 3
DATE      = 4

# column numbers of data within input csv file
INPUT_TYPE      = 1
INPUT_TITLE     = 2
INPUT_DIRECTORS = 3
INPUT_CAST      = 4
INPUT_DATE      = 6

# the order that netflix shows are given in a file, months are the same as named above
INPUT_DAY = 0
INPUT_YEAR = 2

def create_date(date: str) -> Date :
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
    year = START_YEAR + int(date_list[INPUT_YEAR])
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
    if date_list[MONTH] == 'Dec' :
        month = 12
    day = int(date_list[INPUT_DAY])
    date_info = (year, month, day)
    return date_info

def read_file(filename: str) -> list[NetflixShow]:
    '''
    reads file into list of NetflixShow format.

    Precondition: filename is in csv format with data in expected columns
        and contains a header row with the column titles.
        NOTE: csv = comma separated values where commas delineate columns

    >>> read_file('0lines_data.csv')
    []
    
    >>> read_file('9lines_data.csv')
    [('Movie', 'SunGanges', ['Valli Bindana'], ['Naseeruddin Shah'], (2019, 11, 15)), \
('Movie', 'PK', ['Rajkumar Hirani'], ['Aamir Khan', 'Anuskha Sharma', 'Sanjay Dutt', 'Saurabh Shukla', 'Parikshat Sahni', 'Sushant Singh Rajput', 'Boman Irani', 'Rukhsar'], (2018, 9, 6)), \
('Movie', 'Phobia 2', ['Banjong Pisanthanakun', 'Paween Purikitpanya', 'Songyos Sugmakanan', 'Parkpoom Wongpoom', 'Visute Poolvoralaks'], ['Jirayu La-ongmanee', 'Charlie Trairat', 'Worrawech Danuwong', 'Marsha Wattanapanich', 'Nicole Theriault', 'Chumphorn Thepphithak', 'Gacha Plienwithi', 'Suteerush Channukool', 'Peeratchai Roompol', 'Nattapong Chartpong'], (2018, 9, 5)), \
('Movie', 'Super Monsters Save Halloween', [], ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman', 'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina', 'Ian James Corlett', 'Britt McKillip', 'Kathleen Barr'], (2018, 10, 5)), ('TV Show', 'First and Last', [], [], (2018, 9, 7)), \
('Movie', 'Out of Thin Air', ['Dylan Howitt'], [], (2017, 9, 29)), \
('Movie', 'Shutter', ['Banjong Pisanthanakun', 'Parkpoom Wongpoom'], ['Ananda Everingham', 'Natthaweeranuch Thongmee', 'Achita Sikamana', 'Unnop Chanpaibool', 'Titikarn Tongprasearth', 'Sivagorn Muttamara', 'Chachchaya Chalemphol', 'Kachormsak Naruepatr'], (2018, 9, 5)), \
('Movie', 'Long Shot', ['Jacob LaMendola'], [], (2017, 9, 29)), ('TV Show', 'FIGHTWORLD', ['Padraic McKinley'], ['Frank Grillo'], (2018, 10, 12))]
    '''
    # TODO: complete this method according to the documentation
    # Important: DO NOT delete the header row from the csv file,
    # your function should read the header line and ignore it (do nothing with it)
    # All files we test your function with will have this header row!
    file = open(filename, 'r')
    filereader = csv.reader(file)
    rows = []
    shows = []
    for row in filereader:
        rows.append(row)
    rows.pop(0)
    for row in rows:
        type_list = row[INPUT_TYPE]
        title_list = row[INPUT_TITLE]
        directors_list = row[INPUT_DIRECTORS]
        cast_list = row[INPUT_CAST]
        date_list = row[INPUT_DATE]
        if len(directors_list):
            directors_list = directors_list.split(':')
        else:
            directors_list = []
        if len(cast_list):
            cast_list = cast_list.split(':')
        else:
            cast_list = []
        date = create_date(date_list)
        show = [type_list, title_list, directors_list, cast_list, date]
        shows.append(tuple(show))
    file.close()
    
    return shows

def is_older(date1:Date, date2:Date) -> bool:
    if date1[YEAR] > date2[YEAR]:
        return True
    elif date1[YEAR] < date2[YEAR]:
        return False
    elif date1[YEAR] == date2[YEAR]:
        if date1[MONTH] > date2[MONTH]:
            return True
        elif date1[MONTH] < date2[MONTH]:
            return False
        elif date1[MONTH] == date2[MONTH]:
            if date1[DAY] > date2[DAY]:
                return True
            elif date1[DAY] < date2[DAY]:
                return False
            elif date1[DAY] == date2[DAY]:
                return True



def get_oldest_titles(show_data: list[NetflixShow]) -> list[str]:
    '''
    returns a list of the titles of NetflixShows in show_data
    with the oldest added date

    >>> shows_unique_dates = [\
    ('Movie', 'Super Monsters Save Halloween', [],\
    ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman',\
    'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina', 'Ian James Corlett',\
    'Britt McKillip', 'Kathleen Barr'], (2018, 10, 5)),\
    ('TV Show', 'First and Last', [], [], (2018, 9, 7)),\
    ('Movie', 'Out of Thin Air', ['Dylan Howitt'], [], (2017, 9, 29))]

    >>> shows_duplicate_oldest_date = [\
    ('Movie', 'Super Monsters Save Halloween', [],\
    ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman',\
    'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina',\
    'Ian James Corlett', 'Britt McKillip', 'Kathleen Barr'], (2017, 9, 29)),\
    ('TV Show', 'First and Last', [], [], (2018, 9, 7)),\
    ('Movie', 'Out of Thin Air', ['Dylan Howitt'], [], (2017, 9, 29))]

    >>> get_oldest_titles([])
    []
    >>> get_oldest_titles(shows_unique_dates)
    ['Out of Thin Air']
    >>> get_oldest_titles(shows_duplicate_oldest_date)
    ['Super Monsters Save Halloween', 'Out of Thin Air']
    '''
    # TODO: complete this function according to the documentation
    oldest_date = tuple([2099, 12, 31])
    for show in show_data:
        if is_older(oldest_date, show[DATE]):
            oldest_date = show[DATE]
    shows = []
    for show in show_data:
        if oldest_date == show[DATE]:
            shows.append(show[TITLE])
    return shows


def get_actors_in_most_shows(shows: list[NetflixShow]) -> list[str]:
    '''
    returns a list of actor names that are found in the casts of the most shows

    >>> l_unique_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Michael Cera'], (2019, 9, 1)), \
    ('TV Show', 'Maniac', [], ['Emma Stone'], (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal'], (2019, 12, 31))]

    >>> one_actor_in_multiple_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal'], \
    (2019, 12, 31))]

    >>> actors_in_multiple_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal', 'Om Puri'], \
    (2019, 12, 31))]

    >>> get_actors_in_most_shows([])
    []

    >>> get_actors_in_most_shows(l_unique_casts)
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers', 'Michael Cera', 'Emma Stone', 'Paresh Rawal']

    >>> get_actors_in_most_shows(one_actor_in_multiple_casts)
    ['Jonah Hill']

    >>> get_actors_in_most_shows(actors_in_multiple_casts)
    ['Om Puri', 'Jonah Hill']
    '''
    # TODO: complete this function according to the documentation
    number_of_shows = {}
    for show in shows :
        cast_list = show[CAST]
        for cast in cast_list:
            number_of_shows[cast] = 0
    for show in shows:
        cast_list = show[CAST]
        for cast in cast_list:
            number_of_shows[cast] += 1
    mx = 0
    for cast in number_of_shows:
        if mx < number_of_shows[cast]:
            mx = number_of_shows[cast]
    most_credit = []
    for cast in number_of_shows:
        if mx == number_of_shows[cast]:
            most_credit.append(cast)
    return most_credit

def get_shows_with_search_terms(show_data: list[NetflixShow], terms: list[str]
                                 ) -> list[NetflixShow]:
    '''
    returns a list of only those NetflixShow elements in show_data
    that contain any of the given terms in the title.
    Matching of terms ignores case ('roAD' is found in 'Road to Sangam') and
    matches on substrings ('Sang' is found in 'Road to Sangam')

    Precondition: the strings in terms are not empty strings

    >>> movies = [\
    ('Movie', 'Rang De Basanti', ['Rakeysh Omprakash Mehra'], ['Aamir Khan', 'Siddharth', 'Atul Kulkarni', 'Sharman Joshi', 'Kunal Kapoor', 'Alice Patten', 'Soha Ali Khan', 'Waheeda Rehman', 'Kiron Kher', 'Om Puri', 'Anupam Kher', 'Madhavan'], (2018, 8, 2)),\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'], ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', 'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', 'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', 'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], (2019, 12, 31))]

    >>> terms1 = ['House']
    >>> terms1_wrong_case = ['hoUSe']

    >>> terms_subword = ['Sang']

    >>> terms2 = ['House', 'Road', 'Basanti']
    >>> terms2_wrong_case = ['house', 'ROAD', 'bAsanti']

    >>> get_shows_with_search_terms([], [])
    []

    >>> get_shows_with_search_terms(movies, [])
    []

    >>> get_shows_with_search_terms([], terms1)
    []

    >>> get_shows_with_search_terms(movies, terms1)
    [('Movie', "Viceroy's House", ['Gurinder Chadha'], ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', 'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', 'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], (2017, 12, 12))]

    >>> get_shows_with_search_terms(movies, terms1_wrong_case)
    [('Movie', "Viceroy's House", ['Gurinder Chadha'], ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', 'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', 'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], (2017, 12, 12))]

    >>> get_shows_with_search_terms(movies, terms_subword)
    [('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', 'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], (2019, 12, 31))]

    >>> get_shows_with_search_terms(movies, terms2)
    [('Movie', 'Rang De Basanti', ['Rakeysh Omprakash Mehra'], ['Aamir Khan', 'Siddharth', 'Atul Kulkarni', 'Sharman Joshi', 'Kunal Kapoor', 'Alice Patten', 'Soha Ali Khan', 'Waheeda Rehman', 'Kiron Kher', 'Om Puri', 'Anupam Kher', 'Madhavan'], (2018, 8, 2)), ('Movie', "Viceroy's House", ['Gurinder Chadha'], ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', 'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', 'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], (2017, 12, 12)), ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', 'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], (2019, 12, 31))]

    >>> get_shows_with_search_terms(movies, terms2_wrong_case)
    [('Movie', 'Rang De Basanti', ['Rakeysh Omprakash Mehra'], ['Aamir Khan', 'Siddharth', 'Atul Kulkarni', 'Sharman Joshi', 'Kunal Kapoor', 'Alice Patten', 'Soha Ali Khan', 'Waheeda Rehman', 'Kiron Kher', 'Om Puri', 'Anupam Kher', 'Madhavan'], (2018, 8, 2)), ('Movie', "Viceroy's House", ['Gurinder Chadha'], ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', 'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', 'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], (2017, 12, 12)), ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', 'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], (2019, 12, 31))]
    '''
    # TODO: complete this function according to the documentation
    for index in range(len(terms)):
        terms[index] = terms[index].lower()
    shows = []
    for show in show_data:
        title = show[TITLE]
        title = title.lower()
        for term in terms:
            if term in title:
                shows.append(show)
    return shows


def query(show_data: list[NetflixShow]) -> list[str]:
    '''
    Returns a list of only the show titles from show_data
    that are acted in by the 'most popular' actors
    where the 'most popular' is defined as the actors in the most shows.
    The returned list is in sorted order and does not contain duplicate entries.

    >>> l_unique_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Michael Cera'], (2019, 9, 1)), \
    ('TV Show', 'Maniac', [], ['Emma Stone'], (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal'], (2019, 12, 31))]
    
    >>> one_actor_in_multiple_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal'], \
    (2019, 12, 31))]
    
    >>> actors_in_multiple_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal', 'Om Puri'], \
    (2019, 12, 31))]
    
    >>> query([])
    []
    
    >>> query(l_unique_casts)
    ['Maniac', 'Road to Sangam', 'Superbad', "Viceroy's House"]
    
    >>> query(one_actor_in_multiple_casts)
    ['Maniac', 'Superbad']

    >>> query(actors_in_multiple_casts)
    ['Maniac', 'Road to Sangam', 'Superbad', "Viceroy's House"]
    '''
    # TODO: complete this function according to the documentation
    casts = get_actors_in_most_shows(show_data)
    shows = []
    for show in show_data:
        for cast in casts:
            if cast in show[CAST]:
                shows.append(show[TITLE])
    unique_shows = []
    for show in shows:
        if not(show in unique_shows):
            unique_shows.append(show)
    unique_shows.sort()
    return unique_shows
