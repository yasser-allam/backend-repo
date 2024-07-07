class Server:
    def __init__(self, server_ip):
        self.server_ip = server_ip
    
    def start_server(self):
        print(f"Starting server at {self.server_ip}")
