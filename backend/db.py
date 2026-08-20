import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


def save_meal(total_calories: int, items: list):
    response = supabase.table("meals").insert({
        "total_calories": total_calories,
        "items_json": items
    }).execute()

    return response.data


def get_todays_meals():
    response = (
        supabase
        .table("meals")
        .select("*")
        .execute()
    )

    return response.data