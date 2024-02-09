commandmap = { 
"Install BeautifulSoup for parsing HTML": r'''pip install beautifulsoup4''',

"Install Requests for HTTP requests": r'''pip install requests''',

"Install Selenium for browser automation": r'''pip install selenium''',

"Install the WebDriver for your Browser (e.g., Chrome)": r'''# Must be done manually by downloading the correct driver''',

"Install Scrapy for robust web scraping": r'''pip install Scrapy''',

"Start a new Scrapy project": r'''scrapy startproject *{project_name}*''',

"Generate a Spider for Scrapy project": r'''cd *{project_name}*
scrapy genspider *{spider_name}* *{website}*''',

"Run a Scrapy Spider": r'''scrapy crawl *{spider_name}*''',

"Export Scrapy Spider results to JSON": r'''scrapy crawl *{spider_name}* -o *{results.json}*'''
,
              
              "create a new github repo and push all this folder": r'''
gh repo create *{projectname}* --confirm *{--private or --public}*
git init
#touch readME.md   #this is to create an initial file to push
echo -e 'env\n__pycache__\n.env\nlib64/\nlib/\nshare' > .gitignore
git add .
git commit -m "first"
git remote add origin https://github.com/*{username}*/myproject.git
git branch -M main
git push -u origin main
''',
"delete .git" : r'''rm -fr .git''',
"push repo" : r'''git push *{source}* *{destination}*''',
"push all repo" : r'''git add . 
git commit -m "autocommit"
git push *{source}* *{destination}*''',
"install python" : r'''sudo apt-get install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.8''',
"delete .git" : r'''rm -fr .git''',
"delete .git" : r'''rm -fr .git''',
"delete .git" : r'''rm -fr .git''',
}