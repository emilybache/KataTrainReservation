"""
This module exposes a TrainDataService on http using Cherrypy
"""
import json
import cherrypy


def start(trains_data):
    from train_data_service import TrainDataService
    TrainDataService.data_for_train.exposed = True
    TrainDataService.reserve.exposed = True
    TrainDataService.reset.exposed = True
    cherrypy.config.update({"server.socket_port" : 8081})
    cherrypy.quickstart(TrainDataService(trains_data))
    