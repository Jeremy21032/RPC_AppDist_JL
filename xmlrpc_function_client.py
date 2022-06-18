import xmlrpc.client

proxy =xmlrpc.client.ServerProxy('http://localhost:9000')
directorio='C:/Users/jerem/Desktop/UNIVERSIDAD/QUINTO_SEMESTRE/APLICACIONES_DISTRIBUIDAS'
directorio1='/DirectorioPrueba'
directorio2='/DirectorioPrueba2'
print(proxy.list_contents(directorio))
print('---------------CREA LOS DIRECTORIOS ['+directorio1+','+directorio2+']-----------')
proxy.create_dir(directorio+directorio1)
proxy.create_dir(directorio+directorio2)
print(proxy.list_contents(directorio))
print('---------------ELIMINA LOS DIRECTORIOS ['+directorio1+','+directorio2+']-----------')
proxy.remove_dir(directorio+directorio1)
proxy.remove_dir(directorio+directorio2)
print(proxy.list_contents(directorio))


