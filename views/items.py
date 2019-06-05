from flask import Flask, Blueprint,render_template, request
from models.item import Item
import json

item_blueprint = Blueprint('items', __name__)

@item_blueprint.route('/')
def index():
    items = Item.all()
    return render_template('items/index.html', items=items)

@item_blueprint.route('/', methods=['GET', 'POST'])
def new_item():
    if request.method == 'POST':
        url = request.form['url']
        tag_name = request.form['tag_name']
        query = json.loads(request.form['query'])

        Item(url, tag_name, query).save_to_mongo()

    return render_template('items/new_item.html')