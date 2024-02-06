commandmap = {     "create a new github repo and push all this folder": r'''
gh repo create *{projectname}* --confirm *{--private or --public}*
git init
#touch readME.md   #this is to create an initial file to push
echo -e 'env\n__pycache__\n.env\nlib64/\nlib/\nshare' > .gitignore
git add .
git commit -m "first"
git remote add origin https://github.com/*{username}*/myproject.git
git branch -M main
git push -u origin main
'''}