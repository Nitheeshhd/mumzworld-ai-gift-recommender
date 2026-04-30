import json
from utils.ai_handler import call_ai


def load_products():
    with open("products.json", "r") as f:
        return json.load(f)


def extract_json(text):
    """
    Safely extract JSON from AI response
    Handles cases where model adds extra text
    """
    try:
        return json.loads(text)
    except:
        start = text.find("{")
        end = text.rfind("}") + 1
        if start != -1 and end != -1:
            try:
                return json.loads(text[start:end])
            except:
                return None
        return None


def main():
    print("🎁 Mumzworld AI Gift Recommender (AI Powered)")
    user_input = input("Enter your request: ")

    products = load_products()

    # 🔹 Call AI
    response = call_ai(user_input, products)

    # 🔍 Clean Debug Info (Professional Output)
    print("\n🔍 AI Debug Info:")
    try:
        print("Model:", response.get("model"))
        print("Tokens used:", response.get("usage", {}).get("total_tokens"))
    except:
        print("Debug info not available")

    # 🔹 Extract AI content safely
    try:
        ai_text = response["choices"][0]["message"]["content"]
    except:
        print("❌ Invalid AI response structure")
        return

    # 🔹 Parse JSON safely
    result = extract_json(ai_text)

    if not result:
        print("❌ Failed to parse AI output")
        print("AI said:", ai_text)
        return

    # 🔹 Handle error case
    if "error" in result:
        print("❌", result["error"])
        print("👉 This request is outside Mumzworld domain")
        return

    # 🔹 Validate output structure
    if "recommendations" not in result or not result["recommendations"]:
        print("❌ No suitable products found (Out of scope)")
        return

    # 🔹 Print English output
    print("\n✅ Recommendations (EN):")
    for item in result["recommendations"]:
        name = item.get("name", "Unknown")
        price = item.get("price", "N/A")
        reason = item.get("reason", "No reason provided")

        print(f"- {name} ({price} AED): {reason}")

    # 🔹 Print Arabic output
    print("\n🌍 Recommendations (AR):")
    for item in result["recommendations"]:
        arabic_name = item.get("arabic_name", "غير متوفر")
        print(f"- {arabic_name}")


if __name__ == "__main__":
    main()