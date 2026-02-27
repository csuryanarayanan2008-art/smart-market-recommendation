from fastapi import FastAPI
from pydantic import BaseModel
from backend.data_loader import load_data
from backend.predictor import predict_price
from backend.profit import calculate_profit
from backend.recommender import recommend_best

app = FastAPI()

class RequestModel(BaseModel):
    crop: str
    quantity: int

@app.post("/recommend")
def recommend_market(request: RequestModel):

    data = load_data()
    crop_data = data[data["Crop"] == request.crop]

    results = []

    for _, row in crop_data.iterrows():
        predicted_price = predict_price(row["Modal_Price"])
        transport_cost, net_profit_per_kg, total_profit = calculate_profit(
            predicted_price,
            row["Distance_km"],
            request.quantity
        )

        results.append({
            "Market": row["Market"],
            "Predicted_Price": predicted_price,
            "Transport_Cost": transport_cost,
            "Net_Profit_per_kg": net_profit_per_kg,
            "Total_Profit": total_profit
        })

    best_market = recommend_best(results)

    return {
        "recommended_market": best_market["Market"],
        "expected_profit": best_market["Total_Profit"],
        "details": results
    }