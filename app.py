# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from textblob import TextBlob

# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)

# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.


class Hello(Resource):

    # corresponds to the GET request.
    # this function is called whenever there
    # is a GET request for this resource
    def get(self):

        return jsonify({'message': 'Welcome to Sentiment Analyser API'})

# another resource to analyse the sentiment of comment
class Analyse(Resource):

    def get(self, comment):
        try:
            obj = TextBlob(comment)
            sen = obj.sentiment.polarity
            return jsonify(
                {'status': 'success', 'sentiment': sen}
            )
        except Exception:
            return jsonify(
                {'status': 'Some Error Occured'}
            )


# adding the defined resources along with their corresponding urls
api.add_resource(Hello, '/')
api.add_resource(Analyse, '/analyse/<string:comment>')


# driver function
if __name__ == '__main__':

    app.run(debug=True)
