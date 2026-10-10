import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
manual_rows = [
    ["USR101", 3, 15, 1, "Desktop", 3,"fashion",],  #
    ["USR102", 0, 1, 0, "Mobile", 0,"watches"],  
    ["USR103", 6, 110, 3, "Mobile", 4,"phone"],  
    ["USR104", 5, 120, 1, "Desktop", 2,"fashion"],  
    ["USR105", 2, 8, 0, "Desktop", 1,"phones"],  
    ["USR106", 5, 100, 0, "Mobile", 0,"fashion"],  
    ["USR107", 4, 30, 2, "Mobile", 3,"watches"],
    ["USR108",10,19,0,"Mobile",0,"watches"],
    ["USR109",12,20,0,"Desktop",0,"Fashion"],
    ["USR110", 0, 2, 0, "Mobile", 0, "fashion"],     
    ["USR111", 1, 5, 1, "Desktop", 0, "watches"],    
    ["USR112", 0, 14, 0, "Mobile", 0, "phones"],
    ]
categories = [
    "User_ID",
    "Items_Added",
    "Minutes_Spent",
    "Used_Discount",
    "Device_Type",
    "Made_Purchase",
    "Product_type",
]
df= pd.DataFrame(manual_rows,columns=categories)
df.to_csv("my_ecommerce_datasheet.csv",index=False)
my_system_df=pd.read_csv("my_ecommerce_datasheet.csv")
#print(my_system_df.head())
X=pd.DataFrame()
X['conversion_rate'] = df['Made_Purchase'].div(df['Items_Added']).fillna(0)
X['items_abandoned'] = df['Items_Added'] - df['Made_Purchase']
X['time_spent_mins'] = df['Minutes_Spent']
X['discount_applied'] = df['Used_Discount']

def determine_if_person_stays(row):
    if row['Made_Purchase'] > 0:
        return 1  # Person buys things -> Stays
    elif row['Minutes_Spent'] >= 15 and row['Items_Added'] > 0:
        return 1  # Person highly engaged -> Stays
    else:
        return 0
df['will_stay'] = df.apply(determine_if_person_stays, axis=1)
Y=df['will_stay']


X_train,X_test,Y_train,Y_test =train_test_split(
    X, Y, test_size=0.25, random_state=42,stratify=Y)
model = RandomForestClassifier(max_depth=None,class_weight="balanced", random_state=42)
model.fit(X_train, Y_train)
prediction=model.predict(X_test)

target_user = input("enter the user_id:")


user_index = df[df['User_ID'] == target_user].index

if len(user_index) > 0:
    
    specific_user_features = X.loc[user_index]
    user_prediction = model.predict(specific_user_features)
    print(user_prediction)
else:
    print(" target_user is not in database records")

#0 means customer will not stay.
#1 means customer will stay.






    





    

    


