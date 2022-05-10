# Missing Data Handling Module

def myPreprocessor(dataframe, handling_method, target_label_name):
    df = dataframe
    method = handling_method
    label = target_label_name
    
    #importing libraries 
    import numpy as np
    import pandas as pd
    from sklearn import preprocessing

    for i in range(df.shape[1]):
        n = df.iloc[:,i].isnull().sum()
        if n > 0:
            print("There is some missing values")
            print(df.iloc[:,i].name)
            if df.iloc[:,i].dtype == 'object':
                print('object')
                df.iloc[:,i]=df.iloc[:,i].fillna(df.iloc[:,i].mode()[0])
            else:
                print('numerical')
                
                if method == 'mean':
                    df.iloc[:,i]=df.iloc[:,i].fillna(df.iloc[:,i].mean())
                elif method == 'median':
                    df.iloc[:,i]=df.iloc[:,i].fillna(df.iloc[:,i].median())
                elif method == 'ffill':
                    df.iloc[:,i]=df.iloc[:,i].fillna(method = 'ffill')

# Label Encoder for converting categorical values to numerical values
    
    obj_features = []

    # Decide which categorical variables you want to use in model
    for col_name in df.columns:
        if df[col_name].dtypes == 'object':
            unique_cat = len(df[col_name].unique())
            print("Feature '{col_name}' has {unique_cat} unique categories".format(col_name=col_name, unique_cat=unique_cat))
            obj_features.append(col_name)
            
    label_encoder = preprocessing.LabelEncoder()

    k = df[obj_features].shape[1]

    for i in range(k):
        name=obj_features
        name[i]
        df[name[i]]= label_encoder.fit_transform(df[name[i]])
    

# Feature scaling - Normalization

    features_data=df.drop(label,axis=1)
    class_data=df[label]
    ###
    cols_name = features_data.columns
    
    minmax_scaler=preprocessing.MinMaxScaler()
    scaled =minmax_scaler.fit_transform(features_data)

    normalize_data = pd.DataFrame(scaled, columns = cols_name)

    return normalize_data, class_data

