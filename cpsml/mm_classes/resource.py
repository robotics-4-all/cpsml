class Resource:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name


class SenseResource(Resource):
    def __init__(self, parent, name, uri, interface,
                 namespace, tags, ctags, description):
        """
        Creates and returns an Resource object
        :param name: Resource name. e.g: 'temperature_sensor'
        :param uri: uri on which resource communicates using the Broker. e.g: 'sensors.temp_sensor' corresponds to
                        uri sensors/temp_sensor
        :param parent: Parameter required for Custom Class compatibility in textX
        :param attributes: List of Attribute objects belonging to the Resource
        """
        super().__init__(parent, name)
        # MQTT uri for Resource
        self.uri = uri
        self.interface = interface
        self.tags = tags
        self.ctags = ctags
        self.description = description


class ActResource(Resource):
    def __init__(self, parent, name, uri, interface,
                 namespace, tags, ctags, description):
        super().__init__(parent, name)
        self.uri = uri
        self.interface = interface
        self.tags = tags
        self.ctags = ctags
        self.description = description


class ComputeResource(Resource):
    def __init__(self, parent, name, uri, interface,
                 namespace, tags, ctags, description):
        super().__init__(parent, name)
        self.uri = uri
        self.interface = interface
        self.tags = tags
        self.ctags = ctags
        self.description = description
