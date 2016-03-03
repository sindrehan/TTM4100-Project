import json
class MessageParser():
    def __init__(self):

        self.possible_responses = {
            'error': self.parse_error,
            'info': self.parse_info,
            'message': self.parse_msg,
            'history': self.parse_history,
        }

    def parse(self, payload):
        payload = json.loads(payload)

        if payload['response'] in self.possible_responses:
            return self.possible_responses[payload['response']](payload)
        else:
            return "Received invalid response from server!"

    def parse_error(self, payload):
        return "<"+payload.get('timestamp')+"> Error: "+payload.get('content')
    def parse_info(self, payload):
        return "<"+payload.get('timestamp')+"> Info: "+payload.get('content')
    def parse_msg(self, payload):
        return "<"+payload.get('timestamp')+"> "+payload.get('sender')+": "+payload.get('content')
    def parse_history(self, payload):
        history_list = payload.get('content')
        history = ""
        for line in history_list:
            history += self.parse_msg(json.loads(line))
            history += "\n"
        return history
