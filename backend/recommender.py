def recommend_best(results):
    return max(results, key=lambda x: x["Total_Profit"])