class Celsius:
    """
     Now when we call Celsius.temperature to get or set the value, the @property
    function is automatically called to retrieve the value and the @temperature.setter
    function is automatically called to set the value. This is used for instance to 
    constrain the values that temperature can take on, or to allow storage of multiple 
    values in _temperature, one of which is selected to return based on some other 
    criteria. Useful so that if code is changed to use getter and setter rather than
    direct class variable referencing, code doesn't need to be refactored (modified to
    accomodate this change.)
    """
    def __init__(self, temperature = 0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self._temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value
        

temp = Celsius(100)
temp.temperature # should print "Getting value"
temp.temperature = temp.temperature - 50 # should print "Getting value", then "Setting value"

try:
    temp.temperature = temp.temperature -500
except ValueError:
    print("Invalid temperature was correctly caught")