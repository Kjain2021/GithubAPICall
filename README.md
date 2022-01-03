# GithubAPICall
Hi!
A very basic API call is being made using Python currently, just to get top 100 repositories with the topic, "Interview-practice", the data being collected is stored in a json file and Pandas Dataframe. 

<img width="1314" alt="Screen Shot 2022-01-03 at 5 31 33 PM" src="https://user-images.githubusercontent.com/91281025/147928281-57546605-a0e2-4178-96d5-707fa6a06e00.png">

Essential requirements for this project to run:
1. Python Version 3.0
2. Install pip
3. pip install pygithub 
4. pip install pandas 
5. pip install pyvis


After installing pip, you can run the install.sh runscript using ./install.sh to install pygithub, pandas and pyvis. Then generate your token and run the ./run.sh. Also open localhost:8000 to view the visualisation. 

*Please generate your own Github token to run this project*
The topic can be changed in the program. 
I chose to collect data on interview practice repositories and color code them, because I personally when preparing for interviews find it really hard to look at the repositories and then figure out in which language the source code is. Color coding based on languages allows one to quicly figure out which repo to look at and one doesn't has to bother scrolling through the several repos in the profile. 


Use of pyis has allowed for an easy creation of html page. All the libraries and modules used have a special purpose to make the task easy and really efficient. 
I hope to work on it in the near future to add more functionalities specially user interaction. But I couldn't at the moment due to pressing personal unforseen circumstances. 

*No personal user infomation has been extracted, excpet of public user repository names*
