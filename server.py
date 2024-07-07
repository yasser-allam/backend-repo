import yaml

class Server:
    def __init__(self):
        with open("../config.yaml", "r") as config_file:
            config = yaml.safe_load(config_file)
            self.server_ip = config["ServerIPAddress"]
    
    def start_server(self):
        print(f"Starting server at {self.server_ip}")
