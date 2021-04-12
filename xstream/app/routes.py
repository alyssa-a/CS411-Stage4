from flask import render_template, request, jsonify
from app import app
from app import database as db_helper

@app.route("/delete/<int:showId>", methods=["POST"])
def delete(showId):
    try:
        db_helper.delete_show_by_id(showId)
        result = {'success': True, 'response': 'Show deleted'}
    except:
        result = {'success': False, 'response': 'Show could not be deleted'}
    return jsonify(result)

@app.route("/edit/<int:showId>", methods=["POST"])
def edit(showId):
    data = request.get_json()
    try:
        db_helper.update_show(data['showId'], data['showName'], data['ageRating'], data['releaseYear'], data['ratings'])
        result = {'success': True, 'response': 'Show updated'}
    except:
        result = {'success': False, 'response': 'Show could not be edited'}
    return jsonify(result)

@app.route("/create", methods=["POST"])
def create():
    data = request.get_json()
    db_helper.insert_new_show(data['showName'], data['ageRating'], data['releaseYear'], data['ratings'])
    result = {'success': True, 'response': 'Show added successfully'}
    return jsonify(result)

@app.route("/advanced-query")
def advanced_query():
    shows = db_helper.execute_advanced_query()
    return render_template("advanced.html", shows=shows)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        keywords = request.values.get('keywords')
        shows = db_helper.search_shows(keywords)
    else:
        shows = db_helper.fetch_shows()
    return render_template("index.html", shows=shows)