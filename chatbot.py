# Simple enterprise AI assistant placeholder

def chatbot(query):
    if "expenses" in query.lower():
        return "Power department has highest spend."

    if "predict" in query.lower():
        return "Predicted next month cost: 165000"

    return "Query processed by AI assistant"

print(chatbot("predict expenses"))
