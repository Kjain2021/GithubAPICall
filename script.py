from github import Github 
from pprint import pprint
import pandas as pd
import json


g = Github("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")
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
            "Date created": repo.created_at,
            "Language": repo.language,
            "Topics": repo.get_topics(),
            }

# creating a list of all the repos collected
repos =[]

# getting top 100 repos only
top_repo = []
for i, repo in enumerate(all_repo):
    top_repo.append(repo)
    if i == 99:
        break
pprint(top_repo)



