SMART STUDY PLANNER
-----------------------------------------------------------------------------------------------------------------
A simple but smart study planner that helps you decide what to study and when, based on deadlines and difficulty. This project combines Python for scheduling and Prolog for logical reasoning

-----------------------------------------------------------------------------------------------------------------
 What This Project Does:
 -----------------------------------------------------------------------------------------------------------------
Takes multiple study tasks as input
Assigns priority using Prolog rules
Creates a daily study schedule
Adjusts tasks based on available time
Even splits tasks if time is not enough

-----------------------------------------------------------------------------------------------------------------
 How It Works:
 -----------------------------------------------------------------------------------------------------------------
You enter your tasks:
Name
Subject
Deadline
Difficulty (1–5)
Duration (hours)
Python sends data to Prolog:
Prolog decides priority (high / medium / low)

-----------------------------------------------------------------------------------------------------------------
Tasks are:
-----------------------------------------------------------------------------------------------------------------
Sorted by priority
Fitted into your available study hours
Final output:
A clean time-based schedule starting from 4:00 PM


-----------------------------------------------------------------------------------------------------------------
 Technology Used:
 -----------------------------------------------------------------------------------------------------------------
Python
Prolog
pyswip (to connect Python and Prolog)



-----------------------------------------------------------------------------------------------------------------
 Project Structure:
-----------------------------------------------------------------------------------------------------------------


project/
│── main.py        # Main Python code
│── rules.pl       # Prolog rules for priority
│── README.md      # This file


-----------------------------------------------------------------------------------------------------------------
 Setup Instructions
 -----------------------------------------------------------------------------------------------------------------
 
1. Install Python

Make sure Python is installed (3.x recommended)

2. Install Prolog

Download and install SWI-Prolog

3. Install pyswip

Run this in terminal / PowerShell:

pip install pyswip

If import errors happen, try reinstalling Prolog and pyswip.



-----------------------------------------------------------------------------------------------------------------
 How to Run
 -----------------------------------------------------------------------------------------------------------------
 
python main.py
Then follow the prompts:
Enter number of tasks
Fill task details
Enter available study hours

Rules.pl (!!!IF USING VS CODE MAKE SURE TO NOT MISTAKE .PL WITH other extension)




-----------------------------------------------------------------------------------------------------------------
 Example Output:
 -----------------------------------------------------------------------------------------------------------------


--------------------------Today's Study Plan--------------------------

16:00 - 18:00 → Math (Assignment)
18:00 - 19:30 → Physics (Revision)
19:30 - 20:00 → Chemistry (Part)


-----------------------------------------------------------------------------------------------------------------
Limitations
-----------------------------------------------------------------------------------------------------------------
-Fixed start time (4 PM)
-No GUI
-Only daily scheduling
-Needs Prolog installed


-----------------------------------------------------------------------------------------------------------------
 Future Improvements
-Add GUI (Tkinter / Web app)
-Weekly planner support
-Break scheduling (Pomodoro)
-Smarter AI-based prioritization
-Calendar integration

-----------------------------------------------------------------------------------------------------------------
 Credits
 -----------------------------------------------------------------------------------------------------------------
Python Docs
SWI-Prolog
pyswip
Some debugging help from online resources
Prevoiusly learned algorithms from learncpp.com
SWI-Prolog
pyswip
Some debugging help from online resources
Prevoiusly learned algorithms from learncpp.com
