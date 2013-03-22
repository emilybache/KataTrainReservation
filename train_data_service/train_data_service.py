
import json
import cherrypy

class TrainDataService(object):
    
    def __init__(self, json_data):
        self.trains = json.loads(json_data)
    
    def data_for_train_as_dict(self, train_id):
        return self.trains.get(train_id)
        
    def data_for_train(self, train_id):
        return json.dumps(self.data_for_train_as_dict(train_id))
    
    data_for_train.exposed = True

def main(args):
    if args:
        trains_data_file = args[0]
    else:
        trains_data_file = "trains.json"
    with open(trains_data_file) as f:
        trains_data = f.read()
    
    cherrypy.config.update({"server.socket_port" : 8081})
    cherrypy.quickstart(TrainDataService(trains_data))

if __name__ == "__main__":
    help_text = """ 
Use this program to start a train data service:

    python train_data_service.py

It will start a service on:

    http://localhost:8081/data_for_train

You can pass on the command line the name of the json file to use as a data source. 
It defaults to looking for "trains.json" in the current working directory.
    
    python train_data_service.py trains.json
    """
    import sys
    if "-help" in sys.argv or "--help" in sys.argv or "-h" in sys.argv:
        print help_text
    else:
        main(sys.argv[1:])