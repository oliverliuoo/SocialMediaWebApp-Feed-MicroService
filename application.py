from flask import Flask, request
from flask_cors import CORS

import config
from resource import User, Post

application = Flask(__name__)
CORS(application)


@application.route('/', methods=['GET'])
def host():
    return 'Social Media Feed MicroService.'


@application.route('/health', methods=['GET'])
def check_health():
    return 'Instance is healthy!'


@application.route('/feed/<user_id>', methods=['GET'])
def get_user_feed(user_id: str):
    following_list = User.get_user_followings(user_id)
    user_list = [user_id] + following_list
    feeds = Post.get_posts_by_user_ids_within_window(user_list,
                                                     window=request.args.get('window', default=72))
    # limit maximum return amount
    return {'data': feeds[:config.max_feed]}


if __name__ == '__main__':
    application.run()
