# Email-markdown-sections
_Program that Emails random sections of a markdown document_

#### Installation instructions

1. Download this repo as a zip file
2. Unzip the file 
3. Provide markdown file location
4. Provide sender and receiver email address
5. Input your email address password

### What gets emailed

The way this program works is it gathers the location of all h2 tags or all lines that start with "## ".

Then it randomly selects one of these locations and it emails all the content from this h2 to the next. 

### Scheduling daily emails

The program is best used with windows task [scheduler](https://www.windowscentral.com/how-create-automated-task-using-task-scheduler-windows-10) and to specifically schedule python files see [here](https://stackoverflow.com/questions/44727232/scheduling-a-py-file-on-task-scheduler-in-windows-10)
