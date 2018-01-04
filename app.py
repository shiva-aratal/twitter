#tweeter

from flask import Flask, jsonify, request
from stweet import tweet, split_string

app = Flask(__name__)



@app.route('/search', methods=['GET', 'POST'])
def search_tweet():
	search_param = request.args.get('word')
	if not search_param:
		return jsonify({'Error': "Please enter a string or word to search"})
	return jsonify({'found_tweets': tweet(search_param)})


if __name__ == '__main__':
     app.run(debug=True)










