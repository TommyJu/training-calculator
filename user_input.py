from training_ride import TrainingRide
from training_parameters import Intensity, Weather

# Ask user for weight, intensity, and weather to create a TrainingRide instance
def get_user_input():
    while True:
        try:
            weight = float(input("Type your weight in kg and press Enter: ").strip())
            if weight <= 0 or weight > 300:
                print("Invalid weight. Please enter a weight between 0 and 300 kg.")
                continue
            else:
                break
        except ValueError:
            print("Invalid weight. Please enter a number.")

    # Get intensity
    while True:
        try:
            intensity_input = input("Type training intensity (Light, Moderate, High) and press Enter: ").strip().capitalize()
            intensity = Intensity(intensity_input)
            break
        except ValueError:
            print("Invalid intensity. Choose Light, Moderate, or High.")

    # Get weather
    while True:
        try:
            weather_input = input("Type weather (Cold, Moderate, Hot) and press Enter: ").strip().capitalize()
            weather = Weather(weather_input)
            break
        except ValueError:
            print("Invalid weather. Choose Cold, Moderate, or Hot.")

    return TrainingRide(weight, intensity, weather)