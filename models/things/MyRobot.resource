
TopicMsg RangeFinderDataMsg
    range: float
    hfov: float
    vfov: float
    range_min: float
    range_max: float
    sensor_id: str
end

TopicMsg JointStateMsg
    name: str[]
    position: float[]
    velocity: float[]
    effort: float[]
end

TopicMsg TransformStampedMsg
    timestamp: int
    frame_id: str
    child_frame_id: str
    transform: Transform
end

TopicMsg MotorControllerCmdVelMsg
    velocities: float
end

TopicMsg LedArrayDataMsg
    size: int
    colors: float
end


// Sense Resources ---------------------------------------------------------
Resource<Sense> HCSR04
    uri: 'myrobot.sensors.hcsr04'
    interface: AsyncProducer<RangeFinderDataMsg>
end
Resource<Sense> VL53L0X
    uri: 'myrobot.sensors.vl53l0x'
    interface: AsyncProducer<RangeFinderDataMsg>
end
// -----------------------------------------------------------------------

// Act Resources ---------------------------------------------------------
Resource<Act> DFRobotMotorCtrl
    uri: 'myrobot.actuators.dfrobotmotorctrl'
    interface: AsyncConsumer<MotorControllerCmdVelMsg>
end
Resource<Act> GenericLedArray
    uri: 'myrobot.actuators.genericledarray'
    interface: AsyncConsumer<LedArrayDataMsg>
end
// -----------------------------------------------------------------------

// Robotic Resources ----------------------------------------------------
Resource<Sense> Tf
    uri: 'myrobot.sensors.tf'
    interface: AsyncProducer<TransformStampedMsg>
end

Resource<Sense> JointStates
    uri: 'myrobot.sensors.joint_states'
    interface: AsyncProducer<JointStateMsg>
end
// -----------------------------------------------------------------------