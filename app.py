from chalice import Chalice
from recommend import get_repositories_for_user_by_content, get_network_recommendations_for_item, get_users_for_repository_by_content


app = Chalice(app_name='test')


@app.route('/contentrecommender/{item_type}/{id}', methods=['GET'])
def recommend(item_type, id):

    if item_type == "user":
        return get_repositories_for_user_by_content(id)
    elif item_type == "repository":
        return get_users_for_repository_by_content(id)
    else:
        return "Invalid item type"



