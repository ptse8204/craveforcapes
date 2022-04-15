# CraveforCapes
## What is this project?
This is a project that would help better understand the data that was collected throughout [CAPE (Course and Professor Evaluations)](http://cape.ucsd.edu). 
There are a couple projects that had predated mine, such as [Seascape](https://github.com/dcao/seascape), and [SmarterCAPE](https://github.com/andportnoy/smartercapes.com). 

However, none of these project tries to pull the data inside CAPE(i.e.: the grade compositions and other questions that were asked in CAPE survey), the fact that
CAPE does not shows these info in a way that is easily accessible does not really help anyone. Therefore, this project aims to help solve the issue.

## What has been done so far?
I have made a couple jupyter notebooks that could scrape the entire site now, and I have tried to scrape some of the data from the site already. I just haven't really have the time to make another attempt for this. Now, 
if you know anything about Selenium, Jupyter Notebook, and Python, you could probably run this code. If you are having a hard time understanding it, you are welcome to
email me at ptse at ucsd.edu.

## Can I download the data that had been already scraped?
Yeah, sure! The data entire updated CAPE data is available [here](https://github.com/ptse8204/craveforcapes/blob/main/scrapedata/capes.csv), the data include the features listed below:

* Instructor Name
* Course ID and Name
* Term	
* Enrollment count
* Evaluations Made	
* Average Class Recommendation rate
* Average Instructor recommendation rate	
* Average study hours/week
* Average Grade Expected	
* Average Grade Received

However, the data does not include any data composition. The [finalscrapebook.ipynb](https://github.com/ptse8204/craveforcapes/blob/main/finalscrapebook.ipynb) has the code that has ability to pull this, but pulling the entire dataset takes time. The good news is some of the data is already available on the [repository](https://github.com/ptse8204/craveforcapes), I'll make gradual updates until all data were pull.

## What's next?
Depending on my work schedule, I would try my very best to update with all the available data and then start building an accessible website for everyone. 
If you wanted to help, you are free to send me an email.

## Acknowledgment 
Some of the original code were based on:
* [Seascape](https://github.com/dcao/seascape)
* [SmarterCAPE](https://github.com/andportnoy/smartercapes.com)

If not for them, this project would not even be possible for me :)

