import sys
import time
import traceback
from Phidget22.Devices.VoltageRatioInput import *
from PhidgetHelperFunctions import *
import calibration_helper as cali

# init variables
w1 = 0
w2 = 0
w3 = 0
w4 = 0

c1 = 0
c2 = 0
c3 = 0
c4 = 0

# ==== hosuekeeping functions ======================
def onAttachHandler(self):
    
    ph = self
    try:
        #If you are unsure how to use more than one Phidget channel with this event, we recommend going to
        #www.phidgets.com/docs/Using_Multiple_Phidgets for information

        """
        * Get device information and display it.
        """
        channelClassName = ph.getChannelClassName()
        serialNumber = ph.getDeviceSerialNumber()
        channel = ph.getChannel()
        if(ph.getDeviceClass() == DeviceClass.PHIDCLASS_VINT):
            hubPort = ph.getHubPort()
            a = 1
        else:
            a = 2

        ph.setDataInterval(50)

        ph.setVoltageRatioChangeTrigger(0.0)

        if(ph.getChannelSubclass() == ChannelSubclass.PHIDCHSUBCLASS_VOLTAGERATIOINPUT_SENSOR_PORT):
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

# ==== data sampling functions ======================
def onVoltageRatioChangeHandler(self, voltageRatio):
    global w1
    global c1

    w1 += voltageRatio
    c1 += 1
    print ". "

def onVoltageRatioChangeHandler2(self, voltageRatio):
    global w2
    global c2

    w2 += voltageRatio
    c2 += 1
    print ". "

def onVoltageRatioChangeHandler3(self, voltageRatio):
    global w3
    global c3

    w3 += voltageRatio
    c3 += 1
    print ". "

def onVoltageRatioChangeHandler4(self, voltageRatio):
    global w4
    global c4

    w4 += voltageRatio
    c4 += 1
    print ". "


def main():
    global w1
    global w2
    global w3
    global w4
    global c1
    global c2
    global c3
    global c4
    mvalue = []

    """
    * Define how long the program runs for
    """
    runtime = 1  # seconds

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

    print "motor 1 - w1"


    ch.openWaitForAttachment(5000)
    time.sleep(runtime)
    ch.setOnVoltageRatioChangeHandler(None)

    mvalue.append(w1/c1)
    w1 = 0
    c1 = 0

    x = raw_input("motor 1 - w2")
    ch.setOnVoltageRatioChangeHandler(onVoltageRatioChangeHandler)
    ch.openWaitForAttachment(5000)
    time.sleep(runtime)
    ch.setOnVoltageRatioChangeHandler(None)

    mvalue.append(w1/c1)
    w1 = 0
    c1 = 0

    x = raw_input("motor 2 - w1")
    ch2.openWaitForAttachment(5000)
    time.sleep(runtime)
    ch2.setOnVoltageRatioChangeHandler(None)

    mvalue.append(w2/c2)
    w2 = 0
    c2 = 0

    x = raw_input("motor 2 - w2")
    ch2.setOnVoltageRatioChangeHandler(onVoltageRatioChangeHandler2)
    ch2.openWaitForAttachment(5000)
    time.sleep(runtime)
    ch2.setOnVoltageRatioChangeHandler(None)

    mvalue.append(w2/c2)
    w2 = 0
    c2 = 0

    x = raw_input("motor 3 - w1")
    ch3.openWaitForAttachment(5000)
    time.sleep(runtime)
    ch3.setOnVoltageRatioChangeHandler(None)

    mvalue.append(w3/c3)
    w3 = 0
    c3 = 0

    x = raw_input("motor 3 - w2")
    ch3.setOnVoltageRatioChangeHandler(onVoltageRatioChangeHandler3)
    ch3.openWaitForAttachment(5000)
    time.sleep(runtime)
    ch3.setOnVoltageRatioChangeHandler(None)

    mvalue.append(w3/c3)
    w3 = 0
    c3 = 0

    x = raw_input("motor 4 - w1")
    ch4.openWaitForAttachment(5000)
    time.sleep(runtime)
    ch4.setOnVoltageRatioChangeHandler(None)

    mvalue.append(w4/c4)
    w4 = 0
    c4 = 0

    x = raw_input("motor 4 - w2")
    ch4.setOnVoltageRatioChangeHandler(onVoltageRatioChangeHandler4)
    ch4.openWaitForAttachment(5000)
    time.sleep(runtime)
    ch4.setOnVoltageRatioChangeHandler(None)

    mvalue.append(w4/c4)
    w4 = 0
    c4 = 0

    # calibration
    cali.run_calibration(mvalue)

    print("calibration file saved...")
    ch.close()
    ch2.close()
    ch3.close()
    ch4.close()


    print("\nExiting...")
    return 0

#============================================================================



main()

