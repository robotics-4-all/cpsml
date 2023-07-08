TopicMsg RangeFinderDataMsg
    range: float
    hfov: float
    vfov: float
    range_min: float
    range_max: float
    sensor_id: str
end

TopicMsg MotorControllerCmdVelMsg
    velocities: float
end

TopicMsg LedArrayDataMsg
    size: int
    colors: float
end

Resource<Sense> HCSR04
   uri: 'myrobot.sensors.rangefinder.hcsr04'
   interface: AsyncProducer<RangeFinderDataMsg>
   namespace: ''
end

Resource<Sense> VL53L0X
   uri: 'myrobot.sensors.rangefinder.vl53l0x'
   interface: AsyncProducer<RangeFinderDataMsg>
   namespace: ''
end

Resource<Act> DFRobotMotorCtrl
   uri: 'myrobot.actuators.motorcontroller.dfrobotmotorctrl'
   interface: AsyncConsumer<MotorControllerCmdVelMsg>
   namespace: ''
end

Resource<Act> GenericLedArray
   uri: 'myrobot.actuators.ledarray.genericledarray'
   interface: AsyncConsumer<LedArrayDataMsg>
   namespace: ''
end

