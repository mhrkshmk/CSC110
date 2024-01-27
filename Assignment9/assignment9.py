import doctest
import csv
from collections import defaultdict

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
NetflixShow = tuple[str, list[str], Date]
TITLE     = 0
CATEGORIES = 1
CAST      = 2
DATE      = 3

# column numbers of data within input csv file
INPUT_TITLE      = 2
INPUT_CAST       = 4
INPUT_DATE       = 6
INPUT_CATEGORIES = 10

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
    if date_list[MONTH] ==  'Dec' :
        month = 12
    day = int(date_list[INPUT_DAY])
    date_info = (year, month, day)
    return date_info


def read_show(filename: str) -> list[NetflixShow]:
    '''
    reads file into list of NetflixShow format.

    Precondition: filename is in csv format with data in expected columns
        and contains a header row with the column titles.
        NOTE: csv = comma separated values where commas delineate columns
    >>> read_show('11lines_data.csv')
    [('SunGanges', ['Documentaries', 'International Movies'], ['Naseeruddin Shah'], (2019, 11, 15)), ('PK', ['Comedies', 'Dramas', 'International Movies'], ['Aamir Khan', 'Anuskha Sharma', 'Sanjay Dutt', 'Saurabh Shukla', 'Parikshat Sahni', 'Sushant Singh Rajput', 'Boman Irani', 'Rukhsar'], (2018, 9, 6)), ('Phobia 2', ['Horror Movies', 'International Movies'], ['Jirayu La-ongmanee', 'Charlie Trairat', 'Worrawech Danuwong', 'Marsha Wattanapanich', 'Nicole Theriault', 'Chumphorn Thepphithak', 'Gacha Plienwithi', 'Suteerush Channukool', 'Peeratchai Roompol', 'Nattapong Chartpong'], (2018, 9, 5)), ('Super Monsters Save Halloween', ['Children & Family Movies'], ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman', 'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina', 'Ian James Corlett', 'Britt McKillip', 'Kathleen Barr'], (2018, 10, 5)), ('First and Last', ['Docuseries'], [], (2018, 9, 7)), ('Out of Thin Air', ['Documentaries', 'International Movies'], [], (2017, 9, 29)), ('Shutter', ['Horror Movies', 'International Movies'], ['Ananda Everingham', 'Natthaweeranuch Thongmee', 'Achita Sikamana', 'Unnop Chanpaibool', 'Titikarn Tongprasearth', 'Sivagorn Muttamara', 'Chachchaya Chalemphol', 'Kachormsak Naruepatr'], (2018, 9, 5)), ('Long Shot', ['Documentaries'], [], (2017, 9, 29)), ('FIGHTWORLD', ['Docuseries'], ['Frank Grillo'], (2018, 10, 12)), ("Monty Python's Almost the Truth", ['British TV Shows', 'Docuseries'], ['Graham Chapman', 'Eric Idle', 'John Cleese', 'Michael Palin', 'Terry Gilliam', 'Terry Jones'], (2018, 10, 2)), ('3 Idiots', ['Comedies', 'Dramas', 'International Movies'], ['Aamir Khan', 'Kareena Kapoor', 'Madhavan', 'Sharman Joshi', 'Omi Vaidya', 'Boman Irani', 'Mona Singh', 'Javed Jaffrey'], (2019, 8, 1))]
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
        category_list = row[INPUT_CATEGORIES]
        title_list = row[INPUT_TITLE]
        cast_list = row[INPUT_CAST]
        date_list = row[INPUT_DATE]
        if len(cast_list):
            cast_list = cast_list.split(':')
        else:
            cast_list = []
        if len(category_list):
            category_list = category_list.split(':')
        else:
            category_list = []
        date = create_date(date_list)
        show = [title_list, category_list, cast_list, date]
        shows.append(tuple(show))
    file.close()
    return shows

def read_file(filename: str) -> (dict[str, Date],
                                 dict[str, list[str]],
                                 dict[str, list[str]]):
    '''
    Populates and returns a tuple with the following 3 dictionaries
    with data from valid filename.
    
    3 dictionaries returned as a tuple:
    - dict[show title: date added to Netflix]
    - dict[show title: list of actor names]
    - dict[category: list of show titles]

    Keys without a corresponding value are not added to the dictionary.
    For example, the show 'First and Last' in the input file has no cast,
    therefore an entry for 'First and Last' is not added 
    to the dictionary dict[show title: list of actor names]
    
    Precondition: filename is csv with data in expected columns 
        and contains a header row with column titles.
        NOTE: csv = comma separated values where commas delineate columns
        Show titles are considered unique.
        
    >>> read_file('0lines_data.csv')
    ({}, {}, {})
    
    >>> read_file('11lines_data.csv')
    ({'SunGanges': (2019, 11, 15), \
'PK': (2018, 9, 6), \
'Phobia 2': (2018, 9, 5), \
'Super Monsters Save Halloween': (2018, 10, 5), \
'First and Last': (2018, 9, 7), \
'Out of Thin Air': (2017, 9, 29), \
'Shutter': (2018, 9, 5), \
'Long Shot': (2017, 9, 29), \
'FIGHTWORLD': (2018, 10, 12), \
"Monty Python's Almost the Truth": (2018, 10, 2), \
'3 Idiots': (2019, 8, 1)}, \
\
{'SunGanges': ['Naseeruddin Shah'], \
'PK': ['Aamir Khan', 'Anuskha Sharma', 'Sanjay Dutt', 'Saurabh Shukla', 'Parikshat Sahni', 'Sushant Singh Rajput', 'Boman Irani', 'Rukhsar'], \
'Phobia 2': ['Jirayu La-ongmanee', 'Charlie Trairat', 'Worrawech Danuwong', 'Marsha Wattanapanich', 'Nicole Theriault', 'Chumphorn Thepphithak', 'Gacha Plienwithi', 'Suteerush Channukool', 'Peeratchai Roompol', 'Nattapong Chartpong'], \
'Super Monsters Save Halloween': ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman', 'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina', 'Ian James Corlett', 'Britt McKillip', 'Kathleen Barr'], \
'Shutter': ['Ananda Everingham', 'Natthaweeranuch Thongmee', 'Achita Sikamana', 'Unnop Chanpaibool', 'Titikarn Tongprasearth', 'Sivagorn Muttamara', 'Chachchaya Chalemphol', 'Kachormsak Naruepatr'], \
'FIGHTWORLD': ['Frank Grillo'], "Monty Python's Almost the Truth": ['Graham Chapman', 'Eric Idle', 'John Cleese', 'Michael Palin', 'Terry Gilliam', 'Terry Jones'], \
'3 Idiots': ['Aamir Khan', 'Kareena Kapoor', 'Madhavan', 'Sharman Joshi', 'Omi Vaidya', 'Boman Irani', 'Mona Singh', 'Javed Jaffrey']}, \
\
{'Documentaries': ['SunGanges', 'Out of Thin Air', 'Long Shot'], \
'International Movies': ['SunGanges', 'PK', 'Phobia 2', 'Out of Thin Air', 'Shutter', '3 Idiots'], \
'Comedies': ['PK', '3 Idiots'], \
'Dramas': ['PK', '3 Idiots'], 'Horror Movies': ['Phobia 2', 'Shutter'], \
'Children & Family Movies': ['Super Monsters Save Halloween'], \
'Docuseries': ['First and Last', 'FIGHTWORLD', "Monty Python's Almost the Truth"], \
'British TV Shows': ["Monty Python's Almost the Truth"]})
    '''
    # TODO: complete this function according to the documentation
    # Important: DO NOT delete the header row from the csv file,
    # your function should read the header line and ignore it (do nothing with it)
    # All files we test your function with will have this header row!
    shows = read_show(filename)
    title_date = {}
    title_actor = {}
    category_title = {}
    for show in shows:
        title_date[show[TITLE]] = show[DATE]
        title_actor[show[TITLE]] = show[CAST]
        for category in show[CATEGORIES] :
            category_title.setdefault(category, []).append(show[TITLE])
    for cat_title in category_title:
            if category_title[cat_title] == None:
                category_title.pop(cat_title)
    return title_date, title_actor, category_title


def is_older(date1:Date, date2:Date) -> bool:
    """
    gets two date information, returns True if second one is older, False otherwise
    >>> is_older((2019, 5, 4), (2018, 2, 8))
    False
    >>> is_older((2018, 5, 4), (2019, 11, 3))
    True
    >>> is_older((2018, 5, 4), (2018, 5, 4))
    False
    """
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
                return False

def query(filename: str, category: str, date: Date, actors: list[str]
          ) -> list[str]:
    '''
    returns a list of sorted show titles of only shows that:
    - are of the given category
    - have at least one of the actor names in actors in the cast
    - were added to Netflix before the given date
    
    Precondition: category and actor names must match case exactly. 
    For example:
    'Comedies' doesn't match 'comedies', 'Aamir Khan' doesn't match 'aamir khan'
    
    You MUST call read_file and use look ups in the returned dictionaries 
    to help solve this problem in order to receive marks.
    You can and should design additional helper functions to solve this problem.
    
    >>> query('0lines_data.csv', 'Comedies', (2019, 9, 5), ['Aamir Khan'])
    []
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), [])
    []
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), ['Aamir Khan'])
    ['3 Idiots', 'PK']
    
    >>> query('11lines_data.csv', 'International Movies', (2019, 9, 5), \
    ['Aamir Khan', 'Mona Singh', 'Achita Sikamana'])
    ['3 Idiots', 'PK', 'Shutter']
    
    >>> query('11lines_data.csv', 'International Movies', (2019, 8, 1), \
    ['Aamir Khan', 'Mona Singh', 'Achita Sikamana'])
    ['PK', 'Shutter']
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), \
    ['not found', 'not found either'])
    []
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), \
    ['Aamir Khan', 'not found', 'not found either'])
    ['3 Idiots', 'PK']
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), \
    ['not found', 'Aamir Khan', 'not found either'])
    ['3 Idiots', 'PK']
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), \
    ['not found', 'not found either', 'Aamir Khan'])
    ['3 Idiots', 'PK']
    
    >>> query('large_data.csv', 'Comedies', (2019, 9, 5), \
    ['Aamir Khan', 'Mona Singh', 'Achita Sikamana'])
    ['3 Idiots', 'Andaz Apna Apna', 'PK']
    
    >>> query('large_data.csv', 'Comedies', (2020, 9, 5), \
    ['Aamir Khan', 'Mona Singh', 'Achita Sikamana'])
    ['3 Idiots', 'Andaz Apna Apna', 'Dil Chahta Hai', 'Dil Dhadakne Do', 'PK', 'Zed Plus']
    
    >>> query('large_data.csv', 'International Movies', (2020, 9, 5), \
    ['Aamir Khan', 'Mona Singh', 'Achita Sikamana'])
    ['3 Idiots', 'Andaz Apna Apna', 'Dangal', 'Dhobi Ghat (Mumbai Diaries)', \
'Dil Chahta Hai', 'Dil Dhadakne Do', 'Lagaan', 'Madness in the Desert', 'PK', \
'Raja Hindustani', 'Rang De Basanti', 'Secret Superstar', 'Shutter', \
'Taare Zameen Par', 'Talaash', 'Zed Plus']
    '''
    # TODO: complete this function according to the documentation

    title_date, title_actor, category_title = read_file(filename)
    title_list = []
    date_qualify = {}
    actor_qualify = {}
    category_qualify = {}
    for title in title_date:
       date_qualify[title] = False
       actor_qualify[title] = False
       category_qualify[title] = False
    if category in category_title:
        for title in category_title[category]:
            category_qualify[title] = True
    for actor in actors:
        for title in title_actor:
            if (actor in title_actor[title]) :
                actor_qualify[title] = True
    for title in title_date:
        if (is_older(date, title_date[title])):
            date_qualify[title] = True
    for title in title_date :
        #print(title, date_qualify[title], actor_qualify[title], category_qualify[title])
        if date_qualify[title] and actor_qualify[title] and category_qualify[title]:
            title_list.append(title)
    title_list.sort()
    return title_list
