
class TicketOffice(object):

    def reserve(self, train_id, seat_count):
        # TODO: write this code!
        pass

if __name__ == "__main__":
    """Deploy this class as a web service using CherryPy"""
    import cherrypy
    TicketOffice.reserve.exposed = True
    cherrypy.config.update({"server.socket_port" : 8083})
    cherrypy.quickstart(TicketOffice())
