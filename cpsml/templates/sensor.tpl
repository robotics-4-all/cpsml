#!/usr/bin/env python

import sys
import time

from commlib.node import Node, TransportType

{% if transport_type == TransportType.REDIS %}
from commlib.transports.redis import ConnectionParameters
{% elif transport_type == TransportType.MQTT %}
from commlib.transports.mqtt import ConnectionParameters
{% elif transport_type == TransportType.AMQP %}
from commlib.transports.amqp import ConnectionParameters
{% endif %}

from .msg import {{ sensor_data_model }}


class {{ sensor_name }}(Node):

    def __init__(self, debug: bool = True):
        self.sensor_id = {{ sensor_id }}
        self.sensor_type = {{ sensor_type  }}
        self.transport_type = {{ transport_type }}
        self.pub_freq = {{ pub_freq }}
        self.topic = {{ sensor_data_topic }}
        self.node_name = f'sensor.{self.sensor_type}.{self.sensor_id}'

        conn_params = ConnectionParameters()
        super().__init__(node_name=self.node_name,
                         transport_type=self.transport_type,
                         transport_connection_params=conn_params,
                         # heartbeat_uri='nodes.add_two_ints.heartbeat',
                         debug=debug)
        self.pub = self.create_publisher(msg_type={{ sensor_data_model }},
                                         topic=self.topic)

    def run_forever(self):
        rate = Rate(self.pub_freq)
        while True:
            msg = {{ sensor_data_model }}()
            ## Here goes the implementation
            self.pub.publish(msg)
            rate.sleep()


if __name__ == '__main__':
    sonar_node = SonarNode()
    sonar_node.run_forever()
