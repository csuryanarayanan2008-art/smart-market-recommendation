def calculate_profit(predicted_price, distance_km, quantity):
    transport_rate = 0.05
    transport_cost = distance_km * transport_rate
    net_profit_per_kg = predicted_price - transport_cost
    total_profit = net_profit_per_kg * quantity

    return round(transport_cost, 2), round(net_profit_per_kg, 2), round(total_profit, 2)