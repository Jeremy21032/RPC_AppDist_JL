from xmlrpc.server import SimpleXMLRPCServer

import logging
import os
logging.basicConfig(level=logging.INFO)

server = SimpleXMLRPCServer(('localhost', 9000), allow_none=True)

def list_contents(dir_name):
    logging.info('list_contents(%s)', dir_name)
    return os.listdir(dir_name)

def create_dir(direct):
    logging.info('create_dir(%s)',direct)
    logging.info("------------------CREANDO EL DIRECTORIO-----:"+direct)
    return os.mkdir(direct)


def remove_dir(direct_name):
    logging.info('remove_dir(%s)', remove_dir)
    logging.info("------------------ELIMINA EL DIRECTORIO-----:"+direct_name)
    return os.rmdir(direct_name)


server.register_function(list_contents)
server.register_function(create_dir)
server.register_function(remove_dir)

try:
    print('presione Ctrl + C para salir')
    server.serve_forever()
except KeyboardInterrupt:
    print('Saliendo')
