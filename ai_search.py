def ai_search(query):
    """Mock search for demo — no API needed"""
    if not query:
        return {"response": "Try searching for food, beauty, or tech!"}
    
    # Sample responses based on search
    mock_data = {
        "food": "🍔 Try Campus Chili Kitchen or Fit Eats!",
        "beauty": "💅 Check out Cecilia's Glow Skincare or HairCraft!",
        "tech": "💻 TechFix Solutions offers phone repairs and laptop help!"
    }
    
    query_lower = query.lower()
    for key in mock_data:
        if key in query_lower:
            return {"response": mock_data[key]}
    
    return {"response": f"Check out businesses related to: {query} in our directory!"}

if __name__ == "__main__":
    print(ai_search("food"))
