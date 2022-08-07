import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash import dash_table
import base64
import os
from urllib.parse import quote as urlquote
from flask import Flask, send_from_directory, Response
import cv2
import plotly
import numpy as np
import glob

server = Flask(__name__, static_folder = 'static')
app = dash.Dash(__name__, external_stylesheets = [dbc.themes.UNITED], suppress_callback_exceptions = True, server = server)

list_of_videos = [os.path.basename(x) for x in glob.glob('{}*.mp4'.format('static/'))]
#print(list_of_videos[0])

navbar = dbc.NavbarSimple(children = [
    dbc.DropdownMenu(
        nav = True,
        in_navbar = True,
        label = "Menu",
        children = [
            dbc.DropdownMenuItem("Demos", href = '/demos'),
            dbc.DropdownMenuItem("Contact Us!", href = '/contacts')])],
        brand = 'Home',
        brand_href = '/',
        sticky = 'top')

body = dbc.Container(
    [dbc.Row([dbc.Col([html.H1("Listen To See"),html.Br(),
                     html.H3("by The Analytics Club"),
                     html.Br(),
                     html.Br(),
                     html.H2("Helping The Visually Imparied Navigate Any Environment"),
                     html.P("""The aim of the project is to create a
                            deep learning model which will
                            produce an audio output of a video
                            input. These kind of models will be
                            very useful in helping the visually
                            impaired navigate their surroudings"""),
                     html.Img(src = 'static/Video-caption.png', width = '70%', height = '50%'),
                     ])])],
    className="mt-4", style = {'margin-left': '15%'},
)

output = html.Div(id = 'output')

static_video_route = '/static/'

layout_page_1 = html.Div([
    html.H2('Prototype Demo'),
    html.H3("Demo List"),
    html.Ul(id="file-list"),
    html.Div([dcc.Dropdown(
        id='video-dropdown',
        options=[{'label': i, 'value': i} for i in list_of_videos],
        value=list_of_videos[0]
    )], style = {'width': '35%'}),
    html.Br(),
    html.Video(id='video', autoPlay=True, loop=True, height = '45%', width = '45%'),
    html.Br(),
    html.Br(),
    html.Button('Generate Caption', id = 'caption', n_clicks = 0),
    html.Div(id='container-button-basic',
             children='The Caption Will Appear Here'),
    html.Br(),
    html.Br(),
    html.Button('Convert to Audio', id = 'tts', n_clicks = 0),
    html.Audio(id = 'audio', autoPlay = True, loop = False)],
    style={'margin-left':'25%'})

layout_page_2 = html.Div([
    html.H2("Contact Us!"),
    html.H3("Abhipraay: +91 96207 74230"),
    html.H3("Dharani: +91 99622 84511"),
    html.H3("Gaurik: +91 98930 20546"),
    html.H3("Guru Shreyaas: +91 86109 33677"),
    html.H3("Jeshlin: +91 94443 18411"),
    html.H3("Aryan: +91 81056 32052")],
    style = {'margin-left': '35%'})

@app.callback(
        dash.dependencies.Output('container-button-basic', 'children'),
        dash.dependencies.State('video-dropdown', 'value'),
        dash.dependencies.Input('caption', 'n_clicks'))
def gen_caption(value, n_clicks):
    if n_clicks > 0:
        if value == 'Demo-1.mp4':
            return "a squirrel is eating a peanut in it's shell"
        if value == 'Demo-2.mp4':
            return "a man demonstrating how to clean a flower"
        if value == 'Demo-3.mp4':
            return "a man with a sword runs and stabs a cardboard target"
        if value == 'Demo-4.mp4':
            return "a woman puts four okra in a pan of boiling water"

@app.callback(
        dash.dependencies.Output('audio', 'src'),
        dash.dependencies.State('video-dropdown', 'value'),
        dash.dependencies.Input('tts', 'n_clicks'))
def update_audio_src(value, n_clicks):
    if n_clicks > 0:
        return '/static/' + value.split('.')[0] + '.wav' 

@app.callback(
    dash.dependencies.Output('video', 'src'),
    [dash.dependencies.Input('video-dropdown', 'value')])
def update_video_src(value):
    #print(value)
    return static_video_route + value

UPLOAD_DIRECTORY = 'static'

@app.server.route('{}<video_path>.mp4'.format(static_video_route))
def serve_video(video_path):
    video_name = '{}.mp4'.format(video_path)
    #print(1)
    #print(video_name)
    if video_name not in list_of_videos:
        raise Exception('"{}" is excluded from the allowed static files'.format(video_path))
    return send_from_directory(UPLOAD_DIRECTORY + '/', video_name)

page = html.Div(id = 'page-content')
url_bar = dcc.Location(id = 'url', refresh = False)

app.layout = html.Div([url_bar, navbar, page])

@app.callback([Output('page-content', 'children')],
              [Input('url', 'pathname')])
def display_page(pathname):
    #print(pathname)
    global cam
    if pathname == "/demos":
        return [layout_page_1]
    elif pathname == "/contacts":
        return [layout_page_2]
    else:
        return [body]

if __name__ == '__main__':

    app.run_server(debug = True)
