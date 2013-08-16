import os
import sys
import json
from wsgiref.simple_server import make_server

# Every WSGI application must have an application object - a callable
# object that accepts two arguments. For that purpose, we're going to
# use a function (note that you're not limited to a function, you can
# use a class for example). The first argument passed to the function
# is a dictionary containing CGI-style envrironment variables and the
# second variable is the callable object (see PEP 333).
def bukkit_app(environ, start_response):
    status = '200 OK' # HTTP Status
    headers = [('Content-type', 'text/plain')] # HTTP Headers
    start_response(status, headers)

    # retrieve the STACKATO_SERVICES environment variable as a JSON object
    stackato_services = json.loads(os.environ['STACKATO_SERVICES'])
    
    # retrieve the external port number from STACKATO SERVICES
    external_port = str(stackato_services['server']['port'])
    
    # retrieve the hostname from STACKATO_SERVICES
    hostname = str(stackato_services['server']['hostname'])

    # Print the connection details (hostname:port)
    return ['Connect to the Minecraft server at ' + hostname + ':' + external_port + '. Happy crafting!']


application = bukkit_app


if __name__ == '__main__':
    port = int(os.getenv('PORT', '3000'))
    srv = make_server('0.0.0.0', port, application)
    srv.serve_forever()
