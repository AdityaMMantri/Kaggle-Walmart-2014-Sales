import pandas as pd

train_df = pd.read_csv(r"D:\walmart-recruiting-store-sales-forecasting\train.csv\train.csv")
store_df = pd.read_csv(r"D:\walmart-recruiting-store-sales-forecasting\stores.csv")
feature_df = pd.read_csv(r"D:\walmart-recruiting-store-sales-forecasting\features.csv\features.csv")

train_unique_dates = train_df["Date"].nunique()
features_unique_dates = feature_df["Date"].nunique()

print(f"the unique date values in train set : {train_unique_dates}\nthe unique date values in the features set : {features_unique_dates}")
print(train_df.info())
print(feature_df.info())

train_df["Date"]=pd.to_datetime(train_df["Date"])
feature_df["Date"]=pd.to_datetime(feature_df["Date"])

print(f"the data type of date columns now : {train_df['Date'].dtype} & {feature_df['Date'].dtype}")

train_merged=train_df.merge(feature_df,on=["Store","Date"],how="left",validate="many_to_one")
train_merged=train_merged.merge(store_df,on="Store",how="left",validate="many_to_many")

train_merged.to_csv("train_final.csv",index=False)