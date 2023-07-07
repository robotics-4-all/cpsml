TopicMsg  RangeFinderMsg
    a: int
end

    Resource<Sense> HCSR04
        uri: 'myrobot.sensors.rangefinder.hcsr04'
        interface: AsyncProducer<RangeFinderMsg>
        namespace: ''
        tags:
            - Physical
    end

    Resource<Sense> VL53L0X
        uri: 'myrobot.sensors.rangefinder.vl53l0x'
        interface: AsyncProducer<RangeFinderMsg>
        namespace: ''
        tags:
            - Physical
    end

    Resource<Act> DFRobotMotorCtrl
        uri: 'myrobot.actuators.motorcontroller.dfrobotmotorctrl'
        interface: AsyncConsumer<MotorControllerCmdVel>
        namespace: ''
        tags:
            - Physical
    end

    Resource<Act> GenericLedArray
        uri: 'myrobot.actuators.ledarray.genericledarray'
        interface: AsyncConsumer<LedArrayData>
        namespace: ''
        tags:
            - Physical
    end
