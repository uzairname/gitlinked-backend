from chalice import Chalice

app = Chalice(app_name='test')


@app.route('/contentrecommender/{item_type}/{id}', methods=['GET'])
def recommend(item_type, id):
    return item_type + id




