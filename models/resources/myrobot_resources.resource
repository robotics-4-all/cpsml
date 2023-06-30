Resource<Sense> MySonar1
    uri: 'sensors.range.mysonar1'
    interface: Publisher<RangeFinderData>
end

Resource<Act> MyMotorController
    uri: 'actuators.motion.motor.mycontroller'
    interface: Subscriber<MotorControllerCmdVel>
end
