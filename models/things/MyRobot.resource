
    Resource<Sense> HCSR04
        uri: 'myrobot.sensors.hcsr04'
        interface: Publisher<RangeFinderData>
        namespace: ''
    end
    
    Resource<Sense> VL53L0X
        uri: 'myrobot.sensors.vl53l0x'
        interface: Publisher<RangeFinderData>
        namespace: ''
    end
    
    Resource<Act> DFRobotMotorCtrl
        uri: 'myrobot.actuators.dfrobotmotorctrl'
        interface: Subscriber<MotorControllerCmdVel>
        namespace: ''
    end
    
    Resource<Act> GenericLedArray
        uri: 'myrobot.actuators.genericledarray'
        interface: Subscriber<LedArrayData>
        namespace: ''
    end
    