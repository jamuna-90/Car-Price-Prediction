# project
car dekho

The data geeting from https://www.cardekho.com/ 
I am retrieving data from Cardekho. I have car details for 6 cities:

Bangalore
Chennai
Delhi
Kolkata
Jaipur
Hyderabad
All of these datasets are in an unstructured format

Structured Format: All state datasets have been converted to structured format. First, the Bangalore dataset was converted to a structured format. I used the following method: First, I selected columns for new_car_details, applied a lambda function, converted the data to dictionary format, and appended it to a list. This method was applied to all columns. Finally, I concatenated all the columns. The above format was used for all states. All states have been converted to structured format, and the datasets were merged into one dataframe.

Preprocessing:

Check the data types (dtype) and correct the dtype of particular columns (e.g., int, float, object).
Fill the NaN values.
Remove duplicates.
Remove unwanted characters like ",", "$", "Km", "@", "sets" by extracting and removing any added alphabetic characters (e.g., for "3000 km," remove "km").

IQR Calculation:

The IQR is calculated by finding the 25th percentile (Q1) and 75th percentile (Q3) of the data.
The difference between Q3 and Q1 is the IQR, which helps identify the spread of the middle 50% of the data.
Outlier Limits:

Outliers are defined as values below Q1 - 1.5 * IQR (lower limit) or above Q3 + 1.5 * IQR (upper limit).
This formula identifies extreme values beyond a reasonable range.
Removing Outliers:

The dataset is filtered to retain only the values within the upper and lower limits, effectively removing outliers.
Boxplot Visualization:

A boxplot is created after outliers are removed to show the clean distribution of the data.
This method ensures that outliers are properly identified, removed, and the data distribution is visualized clearly. Let me know if you'd like further details
Correlation Matrix:
Correlation:
The corr() function computes the pairwise correlation between numerical features, creating a correlation matrix. This matrix shows how strongly each pair of features is linearly related (with values ranging from -1 to 1).
Seaborn Heatmap:

The sns.heatmap() function from Seaborn is used to visualize the correlation matrix.
annot=True adds the actual correlation values on the heatmap.
cmap='coolwarm' defines the color scheme, where warmer colors (closer to 1) represent stronger positive correlations, and cooler colors (closer to -1) represent negative correlations.
Visualization:

The heatmap visually shows how different features in the dataset correlate with one another. Strong positive or negative correlations could indicate relationships that may influence further data analysis

Algorithms: I am using three algorithms: Linear Regression, Decision Tree, and Random Forest. The best accuracy was achieved with the Random Forest model.
