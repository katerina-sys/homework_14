import sqlite3


def get_value_from_db(sql):
    # Шаг 0
    with sqlite3.connect("netflix.db") as connection:
        result = connection.execute(sql).fetchall()
        return result


def search_of_title(title):
    # Шаг 1
    with sqlite3.connect("netflix.db") as connection:
        sqlite_query = f"""
                        SELECT title, country, release_year, listed_in, description
                        FROM netflix
                        WHERE title LIKE '%{title}%'
                        ORDER BY release_year DESC 
                        LIMIT 1"""

    result = connection.execute(sqlite_query).fetchone()
    return {
        "title": result[0],
        "country": result[1],
        "release_year": result[2],
        "listed_in": result[3],
        "description": result[4]
    }


def search_by_release_year(year1, year2):
    # Шаг 2
    sqlite_query = f"""
                        SELECT title, release_year
                        FROM netflix
                        WHERE release_year BETWEEN '{year1}' AND '{year2}' 
                        LIMIT 100
        """

    result = get_value_from_db(sqlite_query)
    response = []
    for item in result:
        response.append(item)

    return response


def search_by_rating(rating):
    # Шаг 3
    with sqlite3.connect("netflix.db") as connection:
        dict_rating = {
            "children": ("G", "G"),
            "family": ("G", "PG", "PG-13"),
            "adult": ("R", "NC-17")
        }
        sqlite_query = f"""
                SELECT title, rating, description
                FROM netflix
                WHERE rating in {dict_rating.get(rating)}
        """

    result = connection.execute(sqlite_query)
    response = []
    for item in result:
        response.append(item)
    return response


def search_by_listed_in(genre):
    # Шаг 4
    with sqlite3.connect("netflix.db") as connection:
        sqlite_query = f"""
                SELECT *
                FROM netflix
                WHERE listed_in like '%{genre}%'
                order by release_year desc 
                limit 10
    """
    result = connection.execute(sqlite_query)
    response = []
    for item in result:
        response.append(item)
    return response


def only_double_cast(name1, name2):
    # Шаг 5
    with sqlite3.connect("netflix.db") as connection:
        sqlite_query = f"""
                        SELECT netflix.cast
                        FROM netflix
                        WHERE netflix.cast LIKE '%{name1}%'
                        AND netflix.cast LIKE '%{name2}%'
        """

        result = connection.execute(sqlite_query)
        response = []
        names_dict = {}
        for item in result:
            names = set(dict(item).get('netflix.cast').split(",")) - set([name1, name2])

            for name in names:
                names_dict[str(name).strip()] = names_dict.get(str(name).strip(), 0) + 1

        for key, value in names_dict.items():
            if value >= 2:
                response.append(key)

        return response

def page_title_and_description(typ, year, genre):
        sqlite_query = f"""
                        SELECT title, description
                        FROM netflix
                        WHERE type = '{typ}'
                        AND release_year = '{year}'
                        AND listed_in like '%{genre}%'
        """
        result = get_value_from_db(sqlite_query)
        list_of_films = []
        for item in result:
            list_of_films.append(item)
        return list_of_films


print(page_title_and_description('Movie', 2021, 'Documentaries'))