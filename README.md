# ECE2112 Experiment 3
Experiment 3 contains two problems for the student to identify the codes and functions in the Pandas library and apply and use them in creating a Python program using the said library.

## Problem 1
The problem asks to load a cars.csv file, assign it to the variable _cars_, and load the first 5 rows and the last 5 rows of the resulting cars.

It is done by accessing the file with **pd.read_csv('cars.csv')**, then getting the first five rows using **cars.head()**, which will display the first five rows by default, and the last five rows using **cars.tail()**, which will display the last five rows by default.
![image](https://github.com/user-attachments/assets/cead2113-743f-4cfc-951d-35860d710077)


## Problem 2
The problem asks to use the loaded .csv file to extract the following:
  1. The first five rows with _odd-numbered columns_ of cars,
  2. The row that contains _Mazda RX4_ in the column _Model_,
  3. The _number of cylinders_ that the car model _Camaro Z28_ have, and
  4. The _number of cylinders_ and the _gear type_ that the car models _Mazda RX4 Wag_, _Ford Pantera L_, and _Honda Civic_ have.

To extract the first five rows with odd-numbered columns of cars, **cars.iloc[0:5,1::2]** is used, where _0:5_ refers that the slice starts at row 0 and row 5 onwards will not display and _1::2_ refers that the slice starts at column 1 with a step size of 2 to display the odd-numbered columns.

To extract the row that contains _Mazda RX4_ in the column _Model_, **cars.loc[cars['Model']=='Mazda RX4']** is used, where the condition that the row must contain the string _'Mazda RX4'_ in the column _'Model'_ must be satisfied only to show the row containing Mozda RX4 in the column Model.

To extract the number of cylinders that the Camaro Z28 has, **cars.loc[cars['Model']=='Camaro Z28',['cyl']]** is used, where the conditions that the row must contain the string _'Camaro Z28'_ in the column _'Model'_ and to only show the column _cyl_ must be satisfied to show the number of cylinders that the Camaro Z28 have.

To extract the number of cylinders and the gear type that the Mazda RX4 Wag, Ford Pantera L, and Honda Civic have, **cars.loc[cars['Model'].isin(["Mazda RX4 Wag", "Ford Pantera L", "Honda Civic"]), ['cyl', 'gear']]** is used, where the first condition that only shows the rows that contain _Mazda RX4 Wag_, _Ford Pantera L_, and _Honda Civic_ in the column _Model_ is set with the use of function **.isin** that is included in the Pandas Library, where the parameters set are the mentioned car models. The second condition of only showing the columns _cyl_ and _gear_ is also set.

![image](https://github.com/user-attachments/assets/aec4702a-f2da-4e9a-86be-91061cae2657)
