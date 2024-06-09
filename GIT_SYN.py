import git
  2 import datetime
  3 import shutil
  4 import subprocess
  5 src="/var/www/html/index.html"
  6 md = datetime.datetime.now()
  7 bkptime = md.strftime("%Y-%m-%d-%H-%M-%S")
  8 git_ind="/home/ubuntu//Project1/GITPYTHON_GROUP/index.html"
  9 dst="/var/www/html/bkp_html/index.html"
 10 backuppath=dst+bkptime
 11 print(backuppath)
 12 #repo = git.Repo('C:\devops\Assign-3\GITPYTHON_GROUP')
 13 repo = git.Repo('/home/ubuntu/Project1/GITPYTHON_GROUP')
 14 print(repo.branches)
 15 repo.git.checkout("GIT_SYN")
 16 print("PULL STARTED ")
 17 #repo.remotes.origin.pull('https://github.com/Nobin1987/GITPYTHON_GROUP.git','main')
 18 git.cmd.Git().pull('https://github.com/Nobin1987/GITPYTHON_GROUP.git','main' ,'--allow-unrelated-histories' )
 19 diff = repo.git.diff('main','GIT_SYN','--name-only')
 20 print( diff)
 21 if ( diff == "index.html" ) :
 22      print("=== New commit found. Deployment to start ===")
 23      repo.git.checkout("main")
 24      repo.git.merge('GIT_SYN')
 25      repo.git.diff('main','GIT_SYN','--name-only')
 26      shutil.copy2(src, backuppath)
 27      shutil.copy2(git_ind,src)
 28      process = subprocess.Popen(["sudo" ,"service", "nginx" ,"restart"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
 29      std_out, std_err = process.communicate()
 30      print(f"Standard Output: {std_out.decode()}")
 31      print(f"Standard Error: {std_err.decode()}")
 32      shutil.copy2(src, backuppath)
 33      shutil.copy2(git_ind,src)
 34 else :
 35      repo.git.checkout("main")
 36      print("no diff")
