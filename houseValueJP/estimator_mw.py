import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge

# Define the factors and their assumed weights (These weights should be adjusted based on actual market data)
manual_weights = {
    "location": -0.25,  # Proximity to subway
    "land_area": 0.15,  # Size of land
    "terrain": 0.05,  # Terrain type
    "construction_type": 0.10,  # Wooden or Steel
    "building_age": -0.10,  # Older buildings depreciate
    "building_area": 0.15,  # Size of the building
    "building_grade": 0.05,  # Quality of the building
    "building_direction": 0.15,  # Direction of the building
    "enclosed_garage": 0.02,  # Whether it's an enclosed garage
    "parking_capacity": 0.03,  # How many cars it can hold
    "shopping_mall": -0.05,  # Proximity to shopping malls
    "educational_facilities": -0.05,  # Proximity to schools
    "security": 0.05  # Crime rate or security level
}

# Sample dataset
# Each row represents a house with different attributes
houses_data = pd.DataFrame({
    "location": [11, 12, 11, 9, 16, 15, 11, 16, 14, 10],  # Walking time to subway in minutes
    "land_area": [179.42, 59.41, 44.04, 73.02, 165, 299.28, 179.42, 244.27, 299.28, 101.68], # Size of land[m2]
    "terrain": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # Flat = 1, Slope = 2, Mountain = 3
    "construction_type": [1, 1, 1, 1, 1.5, 1, 1, 1, 1, 1],  # Wooden = 1, Steel = 2
    "building_age": [4, 3, 3, 6, 13, 3, 4, 5, 2.5, 2], 
    "building_area": [74.11, 95.64, 87.14, 104.33, 144.05, 128.76, 74.11, 144, 128.76, 90.25], # Size of the building [m2]
    "building_grade": [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],  # Rating 1-5
    "building_direction": [0, 0, 0, 0, 1, 0, 1, 1, 1, 0], # Direction of the building [south 1, other 0]
    "enclosed_garage": [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # Whether it's an enclosed garage
    "parking_capacity": [2, 1, 1, 3, 2, 2, 2, 3, 2, 2], # How many cars it can hold
    "shopping_mall": [0.8, 1.2, 1.01, 0.68, 0.89, 1.4, 0.802, 1.5, 1.63, 0.625], # distance to supermarket [km]
    "educational_facilities": [0.414, 1.04, 0.342, 0.85, 0.76, 1.12, 0.414, 1.5, 1.12, 1.054], # distance to school [km]
    "security": [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],  # Security rating 1-5
    "price": [5980, 4680, 4150, 4780, 7880, 11000, 5980, 9200, 11000, 6198]  # Price in 10k yen
})

# 手动计算一个“基准价格”
def manual_price_estimate(row):
    return sum(row[col] * weight for col, weight in manual_weights.items())
houses_data["manual_price"] = houses_data.apply(manual_price_estimate, axis=1)
print(houses_data.head())

# 让回归模型在“基准价格”上做调整
X = houses_data.drop(columns=["price", "manual_price"])
y = houses_data["price"] - houses_data["manual_price"]

# 使用 Ridge 回归，防止权重被数据完全改写
model = Ridge(alpha=1.0) 
model.fit(X, y)

# Function to estimate house price
def estimate_price(features):
    manual_base_price = manual_price_estimate(pd.Series(features, index=X.columns))
    adjustment = model.predict([features])[0]
    return manual_base_price + adjustment

example_house = [15, 125.61, 1, 1, 4, 117.16, 3, 1, 0, 2, 0.349, 0.523, 3]
predicted_price = estimate_price(example_house)
print(f"Estimated Price: {predicted_price} 10k yen")
