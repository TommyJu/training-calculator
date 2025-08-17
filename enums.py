from enum import Enum

# Describes the intensity of a training ride
class Intensity(Enum):
    LIGHT = "Light"
    MODERATE = "Moderate"
    HIGH = "High"

# Describes the weather conditions during a training ride
class Weather(Enum):
    COLD = "Cold"
    MODERATE = "Moderate"
    HOT = "Hot"