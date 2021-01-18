import os

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


class MyHandler(FTPHandler):

    def on_connect(self):
        print("New Connection: " + str(self.remote_ip))

    def on_disconnect(self):
        # do something when client disconnects
        pass

    def on_login(self, username):
        # do something when user login
        print("username has logged in")
        pass

    def on_logout(self, username):
        # do something when user logs out
        pass

    def on_file_sent(self, file):
        # do something when a file has been sent
        pass

    def on_file_received(self, file):
        # do something when a file has been received
        print("file has been received")
        print(file)
        pass

    def on_incomplete_file_sent(self, file):
        # do something when a file is partially sent
        pass

    def on_incomplete_file_received(self, file):
        # remove partially uploaded files
        import os
        os.remove(file)

def main():
	# Instantiate a dummy authorizer for managing 'virtual' users
	authorizer = DummyAuthorizer()

	# Define a new user having full r/w permissions and a read-only
	# anonymous user
	authorizer.add_user('intesla', 'cata2016', '/home/ftp/', perm='elradfmwMT')
	#authorizer.add_anonymous(os.getcwd())

	# Instantiate FTP handler class
	handler = MyHandler
	hangler.certfile = 'keycert.pem'
	handler.authorizer = authorizer

	# Define a customized banner (string returned when client connects)
	handler.banner = "Castle Server\nDeveloped by Theorical.net and Intesla.cl"

	# Specify a masquerade address and the range of ports to use for
	# passive connections.  Decomment in case you're behind a NAT.
	#handler.masquerade_address = '151.25.42.11'
	#handler.passive_ports = range(60000, 65535)

	# Instantiate FTP server class and listen on 0.0.0.0:2121
	address = ('', 2121)
	server = FTPServer(address, handler)

	# set a limit for connections
	server.max_cons = 256
	server.max_cons_per_ip = 5

	# start ftp server
	server.serve_forever()

if __name__ == '__main__':
	main()