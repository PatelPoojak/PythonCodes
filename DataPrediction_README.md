# PythonCodes
Code for Data Prediction.

Hello guys. Thank you for taking a moment to see my code. It is all writen in python, a coding language. 

What this code does is that it takes a file location from your computer, or a excel file in a csv format, which will be read through pandas with the code: 

dataset = pd.read_csv('C:/Users/patel/Downloads/StudentGrades.csv')

That is a sample file location for my excel csv, so you can download a data set which is in csv format and copy its file location. REMEBER TO HAVE FORWARD SLASHES!!!

Data set Source: Kaggle.com

Also, I am using a coding notebook called Jupyter Notebook through an app called Anaconda.

What this code else can do is that by reading the code, you can extract all necessary information with the other lines of codes below the read csv code.
I made the data set which I converted into a csv before setting the file location for the code to execute. 

My code is about students, their number, age, gender, and their grades. It is a sample data set which I made to work on this project. 
This code evaluates the data set and, with different lines of code, does different things.

If you get a data set and run the code of print(X), you will notice that the student number, the student's age, gender in digits 0 & 1, and History Grade shows up.
That showed three because of the first three lines with the code: X = dataset.iloc[:, [1, 2, 3]].values

With this code, you can find the average score, and much more. 
More importantly, as for the theme, this follows with Data Prediction in business with the last lines of code, where you can make your own prediction for the grades of a student.

You can play around with this code. If you have any questions, feel free to reach out !
