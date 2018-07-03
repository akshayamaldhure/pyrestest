headers = {'Content-Type': 'application/json'}


class Header:
    def __init__(self):
        self.headers = headers

    def get_base_headers(self):
        return self.headers
