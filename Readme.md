# Sentiment Analyser REST API

## Overiew

A simple and minimalistic API that can be used to perform Sentiment Analysis on text.

This API uses [TextBlob](https://textblob.readthedocs.io/en/dev/) to perform Sentiment Analysis.

## Getting started
For getting started with this project just clone the repo
```sh
$ git clone https://github.com/kundroomajid/sentiment-analyser-api.git
```

After Repo is cloned cd into the repo directory
```sh
$ cd sentiment-analyser-api
```

And install the necessary requirements via pip
```sh
$ pip install -r requirements.txt
```
## Starting the API server

The Flask API server can be started by running:

```sh
$ python app.py 
 * Running on http://127.0.0.1:5000
```

You can now access the REST API via `http://127.0.0.1:5000`

## Usage

```sh
Method                      Route                           Response
GET                           /                         Welcome message
GET                         /analyse/{text}             Returns JSON response containing sentiment of the text
```

### Live Demo

I have deployed the API on Heroku which can be accessed at:
https://sent-analyser.herokuapp.com/