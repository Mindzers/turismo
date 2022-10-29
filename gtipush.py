import subprocess

#variable que guarda el archivo o directorio a agregar
arch_o_dir =""
#variable que guarda el mensaje de commit
commit = ""
#variable que guarda el token
git_token = "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"
#variable que guarda el user de github
git_user = "developer@mindzers.com"
#variable que guarda el comando status
git_push = subprocess.run(["git","status"])
#variable que guarda el comando git add
git_add = subprocess.run(["git","add","arch_o_dir"])
#variable que guarda el comando git commit 
git_commit = subprocess.run(["git", "commit", "-m", "commit"])
#variable que guarda el comando git push
git_commit = subprocess.run(["git", "push"])

