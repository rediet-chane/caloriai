import os


def analyze_food_fake() -> dict:
    return {
        "items": [
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
        ],
        "total_calories": 508,
        "confidence": "high"
    }


def analyze_food(image_bytes: bytes) -> dict:
    mode = os.getenv("AI_MODE", "fake")

    if mode == "fake":
        return analyze_food_fake()

    elif mode == "openai":
        from openai_client import analyze_food_openai
        return analyze_food_openai(image_bytes)

    else:
        raise ValueError(f"Unknown AI_MODE: {mode}")