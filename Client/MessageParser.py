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
        payload = json.loads(self)# decode the JSON object

        if payload['response'] in self.possible_responses:
            return self.possible_responses[payload['response']](payload)
        else:
            pass
            # Response not valid

    def parse_error(self, payload):
        return "Error:",
        pass
    def parse_info(self, payload):
        pass
    def parse_msg(self, payload):
        pass
    def parse_history(self, payload):
        pass
