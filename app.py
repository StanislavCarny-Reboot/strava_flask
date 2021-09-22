from flask import Flask, request, render_template, make_response
from flask_restful import Api, Resource
import requests
import re

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        url = request.url
        code = re.search('code=+\w+',url).group()
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('home.html'),200,headers)
        #{"Hello":code}


api.add_resource(HelloWorld,'/exchange_token')



if __name__=='__main__':
    app.run(debug=True)
