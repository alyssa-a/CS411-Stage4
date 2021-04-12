from app import db

def fetch_shows() -> dict:
    conn = db.connect()
    query_results = conn.execute("SELECT * FROM Shows ORDER BY ShowID DESC LIMIT 10;").fetchall()
    conn.close()
    showList = []
    for result in query_results:
        show = {
            "ShowId": result[0],
            "ShowName": result[4],
            "AgeRating": result[7],
            "ReleaseYear": result[2],
            "Ratings": result[5]
        }
        showList.append(show)
    return showList

def update_show(showId: int, showName:str, ageRating: str, releaseYear: int, ratings: int) -> None:
    conn = db.connect()
    query = 'UPDATE Shows SET ShowName = "{}", AgeRating = "{}",  ReleaseYear = "{}", Ratings = "{}" WHERE ShowID = {};'.format(showName, ageRating, releaseYear, ratings, showId)
    conn.execute(query)
    conn.close()

def insert_new_show(showName: str, ageRating: str, releaseYear: int, ratings: int) -> int:
    conn = db.connect()
    query = 'INSERT INTO Shows (ShowName, AgeRating, ReleaseYear, Ratings) VALUES ("{}", "{}", "{}", "{}");'.format(showName, ageRating, releaseYear, ratings)
    conn.execute(query)
    query_results = conn.execute("SELECT LAST_INSERT_ID();")
    query_results = [x for x in query_results]
    ShowID = query_results[0][0]
    conn.close()

    return ShowID

def delete_show_by_id(showId: int) -> None:
    conn = db.connect()
    query = 'DELETE FROM Shows WHERE ShowID={};'.format(showId)
    conn.execute(query)
    conn.close()

def search_shows(keywords: str) -> dict:
    conn = db.connect()
    query = 'SELECT * FROM Shows WHERE ShowName LIKE \'%%{}%%\';'.format(keywords)
    query_results = conn.execute(query).fetchall()
    conn.close()
    showList = []
    for result in query_results:
        show = {
            "ShowId": result[0],
            "ShowName": result[4],
            "AgeRating": result[7],
            "ReleaseYear": result[2],
            "Ratings": result[5]
        }
        showList.append(show)
    return showList

def execute_advanced_query() -> dict:
    conn = db.connect()
    query = 'SELECT ShowName, ReleaseYear, AvgUserRating FROM Shows s NATURAL JOIN (SELECT ShowId, AVG(UserRating) AS AvgUserRating FROM UserReviews GROUP BY ShowId) AS temp WHERE s.ReleaseYear >= 1980 AND s.ReleaseYear <= 1989 ORDER BY AvgUserRating DESC;'
    query_results = conn.execute(query).fetchall()
    conn.close()
    showList = []
    for result in query_results:
        show = {
            "ShowName": result[0],
            "ReleaseYear": result[1],
            "AvgUserRating": result[2]
        }
        showList.append(show)
    return showList