## Linear Least Squares (LLS)
### Tehran House Price
There is a dataset which collect by mohamadreza kariminezhad and you can access it from below link:

https://www.kaggle.com/mokar2001/house-price-tehran-iran

getting the price of 5 most expensive house in tehran. then I alculate the correlation matric for features and I use the features that have most correlation with price. And then I fit these features and the price columns to LLs algorithm as train and test respectivily.
### Show the address of the 5 most expensive houses

| row          | address     | Price     | 
| :---         | :----  | :---- | 
| 1  | Zaferanieh  | 	9.240000e+10  | 
| 2  | Abazar  | 	9.100000e+10  | 
| 3  | Lavasan  | 	8.500000e+10  | 
| 4  | Ekhtiarieh  | 	8.160000e+10  | 
| 5  | Niavaran  | 		8.050000e+10  | 
### Compare your result with Scikit-Learn's results

Tehran House Price
| Models          | MAE    | MSE     | RMAE     |
| :---            | :----  | :---- | :---- |
| my LLS results  | 3145859531.486994  | 3.944041367901528e+19 | 6280160322.715917  |
| sklearn results | 2924869589.0485244  |4.074285732083931e+19  | 6383013185.074844  |
| RidgeCV results | 2921432814.4555564  | 4.076564555644759e+19  | 6384798004.357506  |

### Dollar prices
There is a dataset which collect by Taghizadeh from tgju.org site and you can access it from below link:

https://github.com/M-Taghizadeh/Dollar_Rial_Price_Dataset
preprocessing this dataset to delete duplicate rows, dividing data to 3 part that each part relate to one of presidency period.
### Evaluate each model on test dataset using MAE loss function in Scikit-Learn

| Presidency          | Ahmadinejad    | Rouhani     | Ebram     |
| :---            | :----  | :---- | :---- |
| MAE  |  2633  | 33504.9  | 34441.8  |
