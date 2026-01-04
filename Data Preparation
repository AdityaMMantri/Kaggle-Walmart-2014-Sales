import pandas as pd

test_df = pd.read_csv(r"D:\walmart-recruiting-store-sales-forecasting\test.csv\test.csv")
store_df = pd.read_csv(r"D:\walmart-recruiting-store-sales-forecasting\stores.csv")
feature_df = pd.read_csv(r"D:\walmart-recruiting-store-sales-forecasting\features.csv\features.csv")

test_unique_dates = test_df["Date"].nunique()
features_unique_dates = feature_df["Date"].nunique()

print(f"the unique date values in test set : {test_unique_dates}\nthe unique date values in the features set : {features_unique_dates}")
print(test_df.info())
print(feature_df.info())

test_df["Date"]=pd.to_datetime(test_df["Date"])
feature_df["Date"]=pd.to_datetime(feature_df["Date"])

print(f"the data type of date columns now : {test_df['Date'].dtype} & {feature_df['Date'].dtype}")

test_merged=test_df.merge(feature_df,on=["Store","Date"],how="left",validate="many_to_one")
test_merged=test_merged.merge(store_df,on="Store",how="left",validate="many_to_many")

test_merged.to_csv("test_final.csv",index=False)