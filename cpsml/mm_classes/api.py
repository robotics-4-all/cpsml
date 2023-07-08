class API:
    def __init__(self, parent, name, broker, endpoints, msgs):
        self.parent = parent
        self.name = name
        self.broker = broker
        self.endpoints = endpoints
        self.msgs = msgs


class Endpoint:
    def __init__(self, parent):
        self.parent = parent


class Publisher:
    def __init__(self, parent, uri, msg, namespace):
        super().__init__(parent)
        self.uri = uri
        self.msg = msg
        self.namespace = namespace


class Subscriber:
    def __init__(self, parent, uri, msg, namespace):
        super().__init__(parent)
        self.uri = uri
        self.msg = msg
        self.namespace = namespace


class BrokerInfo:
    def __init__(self, parent, btype, host, port, username, password):
        self.btype = btype
        self.host = host
        self.port = port
        self.username = username
        self.password = password
