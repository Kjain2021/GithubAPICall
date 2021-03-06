from github import Github 
from pprint import pprint
import pandas as pd
import json
import os
from dotenv import load_dotenv

# loading the .env file  or use $TOKEN to set var on your own 
load_dotenv('set.env')

# setting the token  
tk = os.getenv('TOKEN')
g = Github(tk)

#g = Github("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")
#g = Github("<Please add your token>")
# please generate your personal access token 
print("testing github call")

#prints repos of the user, was just testing for access 
#for repo in g.get_user().get_repos():
     # print(repo.name)

# Topic we are looking to use retrieve repos on 
TOPIC = "interview-practice"

# searches repos by topic
all_repo = g.search_repositories(f'topic:{TOPIC}')
print(all_repo.totalCount) # returns number of repositories collected with topic interview-practice  

# to get details for repos 
def get_repo_d(repo):
    return {
            "Full name": repo.full_name,
            "Description": repo.description,
            "Language": repo.language,
            "Topics": repo.get_topics(),
            "Number of stars": repo.stargazers_count,
            }

# creating a list of all the repos collected
repos =[]

# getting top 100 repos only
top_repo = []
for i, repo in enumerate(all_repo):
    top_repo.append(repo)
    if i == 99:
        break
#pprint(top_repo)

# add more fields of the hundred repos
repo_list = []
for repo in top_repo:
    repo_list.append(get_repo_d(repo))



# to create a JSON file to test the repo list info as its extensive to print 
with open(f'{TOPIC}.json', 'w', encoding='utf-8') as f:
    json.dump(repo_list, f, ensure_ascii=False, indent=4)

#transforming and storing data in Pandas Dataframe
repos_df = pd.DataFrame(repo_list)
repos_df.to_csv(TOPIC+'.csv')

#printing it to test it  
#pprint(repos_df)

#checking retrieval of data from dataframe 
topics = repos_df.Topics
print(topics)



