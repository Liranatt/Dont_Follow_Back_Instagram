# Dont_Follow_Back_Instagram
A Python script that parses your downloaded Instagram data to quickly find out which accounts you follow do not follow you back.

How It Works
The script ingests two HTML files you must download from your Instagram account:

followers_1.html: A list of your followers.

following.html: A list of accounts you follow.

It then uses BeautifulSoup to parse both files, extracts the usernames, and compares the two lists. Finally, it uses pandas to print a clean, numbered list of all the accounts that do not follow you back.

Requirements
Python 3

BeautifulSoup4

Pandas

You can install the required libraries using pip:

Bash

pip install beautifulsoup4 pandas
Usage Instructions
Download Your Instagram Data:

Go to your Instagram profile > Settings and privacy > Accounts Center.

Select Your information and permissions.

Click Download your information.

Request a download.

Important: On the "Select information" page, ensure you select HTML as the format, not JSON.

Make sure "Followers and following" is included in the download.

Instagram will email you a link to a .zip file. Download and unzip it.

Locate Your Files:

Inside the unzipped folder, navigate to connections/followers_and_following/.

Copy the followers_1.html and following.html files.

Paste these two files into the same directory as the doesnt_follow_me_back.py script.

Run the Script:

Open a terminal or command prompt in the project directory.

Execute the script:

Bash

python doesnt_follow_me_back.py
Output
The script will first print the total count of your followers and the accounts you are following. It will then display a numbered list (a pandas DataFrame) of all the usernames that do not follow you back.
