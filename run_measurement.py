import sys
import time
import traceback
from Phidget22.Devices.VoltageRatioInput import *
from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Net import *
from PhidgetHelperFunctions import *

millis = lambda: int(round(time.time() * 1000))
t1 = 0
t2 = 0
t3 = 0
t4 = 0

f1 = open("motor1.txt", "a+")
f2 = open("motor2.txt", "a+")
f3 = open("motor3.txt", "a+")
f4 = open("motor4.txt", "a+")


def onAttachHandler(self):
    
    ph = self
    try:
        #If you are unsure how to use more than one Phidget channel with this event, we recommend going to
        #www.phidgets.com/docs/Using_Multiple_Phidgets for information
        
        print("\nAttach Event:")
        
        """
        * Get device information and display it.
        """
        channelClassName = ph.getChannelClassName()
        serialNumber = ph.getDeviceSerialNumber()
        channel = ph.getChannel()
        if(ph.getDeviceClass() == DeviceClass.PHIDCLASS_VINT):
            hubPort = ph.getHubPort()
            print("\n\t-> Channel Class: " + channelClassName + "\n\t-> Serial Number: " + str(serialNumber) +
                "\n\t-> Hub Port: " + str(hubPort) + "\n\t-> Channel:  " + str(channel) + "\n")
        else:
            print("\n\t-> Channel Class: " + channelClassName + "\n\t-> Serial Number: " + str(serialNumber) +
                    "\n\t-> Channel:  " + str(channel) + "\n")
    
        """
        * Set the DataInterval inside of the attach handler to initialize the device with this value.
        * DataInterval defines the minimum time between VoltageRatioChange events.
        * DataInterval can be set to any value from MinDataInterval to MaxDataInterval.
        """
        print("\n\tSetting DataInterval to 50ms")
        ph.setDataInterval(50)

        """
        * Set the VoltageRatioChangeTrigger inside of the attach handler to initialize the device with this value.
        * VoltageRatioChangeTrigger will affect the frequency of VoltageRatioChange events, by limiting them to only occur when
        * the voltage ratio changes by at least the value set.
        """
        print("\tSetting Voltage Ratio ChangeTrigger to 0.0")
        ph.setVoltageRatioChangeTrigger(0.0)
        
        """
        * Set the SensorType inside of the attach handler to initialize the device with this value.
        * You can find the appropriate SensorType for your sensor in its User Guide and the VoltageRatioInput API
        * SensorType will apply the appropriate calculations to the voltage ratio reported by the device
        * to convert it to the sensor's units.
        * SensorType can only be set for Sensor Port voltage ratio inputs (VINT Ports and Analog Input Ports)
        """
        if(ph.getChannelSubclass() == ChannelSubclass.PHIDCHSUBCLASS_VOLTAGERATIOINPUT_SENSOR_PORT):
            print("\tSetting VoltageRatio SensorType")
            ph.setSensorType(VoltageRatioSensorType.SENSOR_TYPE_VOLTAGERATIO)
            
        
    except PhidgetException as e:
        print("\nError in Attach Event:")
        DisplayError(e)
        traceback.print_exc()
        return

def onDetachHandler(self):

    ph = self

    try:
        #If you are unsure how to use more than one Phidget channel with this event, we recommend going to
        #www.phidgets.com/docs/Using_Multiple_Phidgets for information
        
        print("\nDetach Event:")
        
        """
        * Get device information and display it.
        """
        channelClassName = ph.getChannelClassName()
        serialNumber = ph.getDeviceSerialNumber()
        channel = ph.getChannel()
        if(ph.getDeviceClass() == DeviceClass.PHIDCLASS_VINT):
            hubPort = ph.getHubPort()
            print("\n\t-> Channel Class: " + channelClassName + "\n\t-> Serial Number: " + str(serialNumber) +
                "\n\t-> Hub Port: " + str(hubPort) + "\n\t-> Channel:  " + str(channel) + "\n")
        else:
            print("\n\t-> Channel Class: " + channelClassName + "\n\t-> Serial Number: " + str(serialNumber) +
                    "\n\t-> Channel:  " + str(channel) + "\n")
        
    except PhidgetException as e:
        print("\nError in Detach Event:")
        DisplayError(e)
        traceback.print_exc()
        return

def onErrorHandler(self, errorCode, errorString):

    sys.stderr.write("[Phidget Error Event] -> " + errorString + " (" + str(errorCode) + ")\n")


def onVoltageRatioChangeHandler(self, voltageRatio):
    onVoltageRatioChangeHandler.time = getattr(onVoltageRatioChangeHandler, 'time', millis())

    global t1
    global f1

    dt = millis() - onVoltageRatioChangeHandler.time

    t1 += dt

    onVoltageRatioChangeHandler.time = millis()

    w1 = voltageRatio*559110 - 14.343

    print "v1: %0.2f" % w1,

    f1.write(str(w1) + ' ' + str(t1) + '\n')

def onVoltageRatioChangeHandler2(self, voltageRatio):
    onVoltageRatioChangeHandler2.time = getattr(onVoltageRatioChangeHandler2, 'time', millis())

    global t2
    global f2

    dt = millis() - onVoltageRatioChangeHandler2.time

    t2 += dt

    onVoltageRatioChangeHandler2.time = millis()

    w2 = voltageRatio * 559110 - 13.343

    print "v2: %0.2f" % w2,

    f2.write(str(w2) + ' ' + str(t2) + '\n')

def onVoltageRatioChangeHandler3(self, voltageRatio):
    onVoltageRatioChangeHandler3.time = getattr(onVoltageRatioChangeHandler3, 'time', millis())

    global t3
    global f3

    dt = millis() - onVoltageRatioChangeHandler3.time

    t3 += dt

    onVoltageRatioChangeHandler3.time = millis()

    w3 = voltageRatio * 559110 - 14.343

    print "v3: %0.2f" % w3,

    f3.write(str(w3) + ' ' + str(t3) + '\n')


def onVoltageRatioChangeHandler4(self, voltageRatio):
    onVoltageRatioChangeHandler4.time = getattr(onVoltageRatioChangeHandler4, 'time', millis())

    global t4
    global f4

    dt = millis() - onVoltageRatioChangeHandler4.time

    t4 += dt

    onVoltageRatioChangeHandler4.time = millis()

    w4 = voltageRatio * 559110 - 14.343

    print "v4: %0.2f ts: %d" % (w4, t4)

    f4.write(str(w4) + ' ' + str(t4) + '\n')




def main():
    """
    * Define how long the program runs for
    """
    runtime = int(input("Measure for long long: "))  # seconds

    """
    * Allocate a new Phidget Channel object
    """

    ch = VoltageRatioInput()
    ch2 = VoltageRatioInput()
    ch3 = VoltageRatioInput()
    ch4 = VoltageRatioInput()


    """
    * Set matching parameters to specify which channel to open
    """
    ch.setDeviceSerialNumber(533379)
    ch.setIsHubPortDevice(False)
    ch.setChannel(0)

    ch2.setDeviceSerialNumber(533379)
    ch2.setIsHubPortDevice(False)
    ch2.setChannel(1)

    ch3.setDeviceSerialNumber(533379)
    ch3.setIsHubPortDevice(False)
    ch3.setChannel(2)

    ch4.setDeviceSerialNumber(533379)
    ch4.setIsHubPortDevice(False)
    ch4.setChannel(3)

    """
    * Add event handlers before calling open so that no events are missed.
    """
    print("\n--------------------------------------")
    ch.setOnAttachHandler(onAttachHandler)
    ch2.setOnAttachHandler(onAttachHandler)
    ch3.setOnAttachHandler(onAttachHandler)
    ch4.setOnAttachHandler(onAttachHandler)

    ch.setOnDetachHandler(onDetachHandler)
    ch2.setOnDetachHandler(onDetachHandler)
    ch3.setOnDetachHandler(onDetachHandler)
    ch4.setOnDetachHandler(onDetachHandler)

    ch.setOnErrorHandler(onErrorHandler)
    ch2.setOnErrorHandler(onErrorHandler)
    ch3.setOnErrorHandler(onErrorHandler)
    ch4.setOnErrorHandler(onErrorHandler)

    ch.setOnVoltageRatioChangeHandler(onVoltageRatioChangeHandler)
    ch2.setOnVoltageRatioChangeHandler(onVoltageRatioChangeHandler2)
    ch3.setOnVoltageRatioChangeHandler(onVoltageRatioChangeHandler3)
    ch4.setOnVoltageRatioChangeHandler(onVoltageRatioChangeHandler4)


    """
    * Open the channel with a timeout
    """

    print("\nOpening and Waiting for Attachment...")


    ch.openWaitForAttachment(5000)
    ch2.openWaitForAttachment(5000)
    ch3.openWaitForAttachment(5000)
    ch4.openWaitForAttachment(5000)



    time.sleep(runtime)

    """
    * Perform clean up and exit
    """

    #clear the VoltageRatioChange event handler
    ch.setOnVoltageRatioChangeHandler(None)
    ch2.setOnVoltageRatioChangeHandler(None)
    ch3.setOnVoltageRatioChangeHandler(None)
    ch4.setOnVoltageRatioChangeHandler(None)

    print("Cleaning up...")
    ch.close()
    ch2.close()
    ch3.close()
    ch4.close()

    f1.close()
    f2.close()
    f3.close()
    f4.close()

    print("\nExiting...")
    return 0



main()

