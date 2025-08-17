from constants import *
from training_ride import TrainingRide
from enums import Intensity, Weather

# Ask user for weight, intensity, and weather to create a TrainingRide instance
def get_user_input():
    weight = float(input("Type your weight in kg and press enter: "))
    intensity_input = input("Type your training intensity (Light, Moderate, High) and press enter: ")
    weather_input = input("Type the weather (Cold, Moderate, Hot) and press enter: ")

    # Convert inputs to enums
    intensity = Intensity(intensity_input.capitalize())
    weather = Weather(weather_input.capitalize())

    return TrainingRide(weight, intensity, weather)

def main():
    training_ride = get_user_input()
    training_ride.calculate_daily_nutrition_and_hydration()
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()