from github import Github 




#g = Github("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")
g = Github("<Please add your token>")
# please generate your personal access token 
print("testing github call")

#prints repos of the user
for repo in g.get_user().get_repos():
   print(repo.name)

# Topic we are looking to use retrieve repos on 
TOPIC = "interview-practice"

# searches repos by topic
all_repo = g.search_repositories(f'topic:{TOPIC}')
print(all_repo.totalCount) # returns number of repositories collected with topic interview-practice  
