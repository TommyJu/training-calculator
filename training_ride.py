from training_parameters import Intensity, Weather
from nutrition_constants import *

class TrainingRide:
    def __init__(self, weight: float, intensity: Intensity, weather: Weather):
        self.weight = weight
        self.intensity = intensity
        self.weather = weather
    
    # Calculates and prints daily nutrition based on weight, intensity, and weather
    def calculate_daily_nutrition_and_hydration(self):
        print("\n📄 Your Training Ride Details:")
        print(f"Rider Weight: {self.weight} kg")
        print(f"Training Intensity: {self.intensity.value}")
        print(f"Weather: {self.weather.value}")
        
        print(f"\n🥗 Daily Intake Recommendations:")
        print(f"Carbohydrates: {self.weight * CARBOHYDRATE_BASELINE[self.intensity.value]} g")
        print(f"Proteins: {self.weight * PROTEIN_BASELINE[self.intensity.value]} g")
        print(f"Fats: {self.weight * FAT_BASELINE[self.intensity.value]} g")
        print(f"Sodium: {self.weight * SODIUM_BASELINE[self.intensity.value]} mg")
        print(f"Potassium: {self.weight * POTASSIUM_BASELINE[self.intensity.value]} mg")
        print(f"Magnesium: {self.weight * MAGNESIUM_BASELINE[self.intensity.value]} mg")
        print(f"Calcium: {self.weight * CALCIUM_BASELINE[self.intensity.value]} mg")
        print(f"Fluids: {self.weight * HYDRATION_BASELINE[self.intensity.value]} ml")

        print(f"\n🚴 During Training Targets:")
        print(f"Carbohydrates: {CARBOHYDRATE_DURING_RIDE[self.intensity.value]} g/hour")
        print(f"Fluids: {FLUID_INTAKE_DURING_RIDE[self.weather.value]} ml/hour")
        print(f"Sodium: {SODIUM_INTAKE_DURING_RIDE[self.weather.value]} mg/hour")