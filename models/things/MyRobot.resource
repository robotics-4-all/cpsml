
    Resource<Sense> HCSR04
        uri: 'myrobot.sensors.rangefinder.hcsr04'
        interface: Publisher<RangeFinderData>
        namespace: ''
    end
    
    Resource<Sense> VL53L0X
        uri: 'myrobot.sensors.rangefinder.vl53l0x'
        interface: Publisher<RangeFinderData>
        namespace: ''
    end
    
    Resource<Act> DFRobotMotorCtrl
        uri: 'myrobot.actuators.motorcontroller.dfrobotmotorctrl'
        interface: Subscriber<MotorControllerCmdVel>
        namespace: ''
    end
    
    Resource<Act> GenericLedArray
        uri: 'myrobot.actuators.ledarray.genericledarray'
        interface: Subscriber<LedArrayData>
        namespace: ''
    end
    