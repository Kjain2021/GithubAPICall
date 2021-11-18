from github import Github 

g = Github("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")
print("testing github call")
#Trivial details for testing.
user=g.get_user()
print("user"+ user.login)
