#!/usr/bin/env python
# encoding: utf-8
from flask import Flask
from flask.ext.restful import Api
from resource.files import FileResource
from resource.music import MusicResource, MusicListResource
from resource.channel import ChannelResource, ChannelListResource
from resource.playlist import PlaylistListResource, PlaylistResource
from resource.user import UserResource, UserListResource, UserCurrentResource, UserCurrentHistoryResource, UserCurrentFavorResource
from config import SECRET_KEY

app = Flask(__name__)
api = Api(app)

app.jinja_env.variable_start_string = '[['
app.jinja_env.variable_end_string = ']]'

api.add_resource(FileResource, '/api/fs/<string:key>/')

api.add_resource(MusicListResource, '/api/music/')
api.add_resource(MusicResource, '/api/music/<string:key>/')
api.add_resource(ChannelListResource, '/api/channel/')
api.add_resource(ChannelResource, '/api/channel/<string:key>/')
api.add_resource(PlaylistListResource, '/api/playlist/')
api.add_resource(PlaylistResource, '/api/playlist/<string:key>/')
api.add_resource(UserListResource, '/api/user/')
api.add_resource(UserCurrentResource, '/api/user/current/')
api.add_resource(UserResource, '/api/user/<string:key>/')
api.add_resource(UserCurrentHistoryResource, '/api/user/current/history/')
api.add_resource(UserCurrentFavorResource, '/api/user/current/favor/')

app.secret_key = SECRET_KEY

# templates
from flask import render_template


@app.route('/')
def index():
    return render_template("index.html")
