# CraveforCapes
## Update 22 May, 2022
I have finished scrapping the data from FA12 to WI22. I have done some EDA myself on the data right now, but I am kinda lazy to keep updating the EDA stuff. The next big plan for me to use the data is that I would try to predict student's performance in a class based on their previous grades in the previous quarters.

The general prediction function goes like this: First, the predict function would read in your class and your GPA, and find which distribution that your grades are in those classes (e.g.: top 30, bottom 20). Next, you would give a bunch of class for the function to predict, the function would output your predicted grades based on your previous location of those grades.

The hypothesis that why does this function is valid goes like this: Because your level of ability in class A, could be translate to your level of ability to class B.

## What is this project?
This is a project that would help better understand the data that was collected throughout [CAPE (Course and Professor Evaluations)](http://cape.ucsd.edu). 
There are a couple projects that had predated mine, such as [Seascape](https://github.com/dcao/seascape), and [SmarterCAPE](https://github.com/andportnoy/smartercapes.com). 

However, none of these project tries to pull the data inside CAPE(i.e.: the grade compositions and other questions that were asked in CAPE survey), the fact that
CAPE does not shows these info in a way that is easily accessible does not really help anyone. Therefore, this project aims to help solve the issue.

## What has been done so far?
I have made a couple jupyter notebooks that could scrape the entire site, and I finished scrapping the data from FA12 to WI22 from the site already. 
Now, 
if you know anything about Selenium, Jupyter Notebook, and Python, you could probably run the code in Github and did the same thing as I did. If you are having a hard time understanding it, you are welcome to
email me at ptse at ucsd.edu.

## What's next?
Depending on my work schedule, I would start building an accessible website for everyone and a prediction model for grades as well. 
If you wanted to help me, you are free to send me an email.

## Acknowledgment 
Some of the original code were based on:
* [Seascape](https://github.com/dcao/seascape)
* [SmarterCAPE](https://github.com/andportnoy/smartercapes.com)

If not for them, this project would not even be possible for me :)
