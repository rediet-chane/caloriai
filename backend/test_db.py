from db import save_meal, get_todays_meals

save_meal(
    total_calories=508,
    items=[
        {
            "name": "grilled chicken",
            "estimated_grams": 150,
            "calories": 248,
            "protein_g": 46,
            "carbs_g": 0,
            "fat_g": 5.4
        },
        {
            "name": "steamed rice",
            "estimated_grams": 200,
            "calories": 260,
            "protein_g": 4.8,
            "carbs_g": 56,
            "fat_g": 0.6
        }
    ]
)

print("Meal saved!")
print(get_todays_meals())