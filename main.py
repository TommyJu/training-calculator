from user_input import get_user_input

def main():
    training_ride = get_user_input()
    training_ride.calculate_daily_nutrition_and_hydration()
    print("\n(ctrl + click) the link to see the guidelines used for these calculations.\n"
          "https://github.com/TommyJu/training-calculator/blob/main/readme.md")
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()