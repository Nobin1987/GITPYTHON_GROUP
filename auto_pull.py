import git

repo = git.Repo('GITPYTHON_GROUP')
# if my_repo.is_dirty(untracked_files=True):
#     print('Changes detected.')

print('Remotes:')
for remote in repo.remotes:
    print(f'- {remote.name} {remote.url}')


# Pull from remote repo
print(repo.remotes.origin.pull())
# Push changes
print(repo.remotes.origin.push())