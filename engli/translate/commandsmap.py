commandmap = { 
"Create new directory": r'''mkdir @?directory_name?@''',

      "Create scraping app": 
r'''cat > @?app_name?@.py <<'EOF'
from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route("/api/scrape", methods=["GET"])
def get_scraped_data():
    content = fetch_data("https://www.@?website?@", "@?specificword?@")  # replace with the site you want to scrape
    return jsonify(content), 200

def fetch_data(url, word):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text()  # get all the text

    # Find the word
    try:
        index = text.index(word)
        # Return all text after the word
        return text[index + len(word):]
    except ValueError: 
        return "The word does not appear in the text"

if __name__ == "__main__":
    app.run(debug=True)
EOF
''',

"Run the scraping app": r'''python3 @?app_name?@.py''',

"create scraping app to track data and store in a database": 
r'''cat > @?app_name?@.py <<'EOF'
from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
import requests
import sqlite3
import pandas as pd
from datetime import datetime

app = Flask(__name__)

@app.route('/api/scrape', methods=['GET'])
def get_scraped_data():
    word = request.args.get('word')  # Getting word from the request
    url = "https://www.@?website?@"  # Url to scrape
    content = fetch_data(url, word) 

    # Check if some content was found
    if content: 
        # Save scraped data to SQLite
        conn = sqlite3.connect('@?dbname?@.db')
        c = conn.cursor()
                # Create table if not exists
        c.execute('CREATE TABLE IF NOT EXISTS ScrapedData (content TEXT, timestamp DATETIME)')
        conn.commit()
        c.execute("INSERT INTO ScrapedData(content, timestamp) VALUES (?, ?)", (content, datetime.now()))

        # Save changes and close connection
        conn.commit()
        conn.close()
        
        # converting data into csv
        pd.DataFrame([content]).to_csv("@?csvname?@.csv", index=False)

        return jsonify({"message": "Data scraped and stored successfully", "content": content}), 200
    else:
        return jsonify({"message": "Data not found"}), 404

def fetch_data(url, word):

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()

    # Find the word
    try:
        index = text.index(word)

        # Return all text after the word
        return text[index + len(word):]
        
    except ValueError: 
        return None  
def create_database():
    # Connect to SQLite database
    conn = sqlite3.connect('scraped_data.db')
    c = conn.cursor()

    # Create table
    c.execute("CREATE TABLE IF NOT EXISTS ScrapedData (content TEXT, timestamp DATETIME)")

    # Save changes and close connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()  # create database and table before running the app
    app.run(debug=True)
EOF
''',

"Install necessary libraries for scraping app": r'''pip3 install flask beautifulsoup4 requests''',


"run python app": r"python3 @?appname?@.py",

"call scraping app to track word": r"curl http://127.0.0.1:5000/api/scrape?word=@?word?@",

"Git clone repository": r'''git clone @?repository_url?@''',

"Git check status": r'''git status''',

"Git add files to staging": r'''git add .''',

"Git commit changes": r'''git commit -m "@?commit_message?@"''',

"Git push changes to repository": r'''git push origin master''',

"Create a new directory in UNIX/Linux": r'''mkdir @?new_directory?@''',

"Change directory in UNIX/Linux": r'''cd @?directory_name?@''',

"List directory contents in UNIX/Linux": r'''ls''',

"Python run a script": r'''python @?script_name?@.py''',

"Node.js run a script": r'''node @?script_name?@.js''',

"Java compile a program": r'''javac @?program_name?@.java''',

"Java run a program": r'''java @?program_name?@''',

"C/C++ compile a program using gcc": r'''gcc -o @?program_name?@ @?program_name?@.c''',

"C/C++ run a compiled program": r'''./@?program_name?@''',

"Open a file with vim": r'''vim @?filename?@''',

"Exit vim": r''':q!''',

"Install package with npm": r'''npm install @?package_name?@''',

"Start a PostgreSQL server": r'''pg_ctl -D /usr/local/var/postgres start''',

"Connect to a PostgreSQL database": r'''psql -h localhost -U postgres -d @?database_name?@''',

"Docker build an image": r'''docker build -t @?image_name?@ .''',

"Docker run a container": r'''docker run -p 4000:80 @?image_name?@''',

"Docker list running containers": r'''docker ps''',

"Launch a python interactive shell with Django": r'''python manage.py shell''',

"Django create a new application": r'''python manage.py startapp @?app_name?@''',

"Django run a server": r'''python manage.py runserver''',

"Django migrate database": r'''python manage.py migrate''',

"Scrapy start a new project": r'''scrapy startproject @?project_name?@''',

"Scrapy crawl a spider": r'''scrapy crawl @?spider_name?@''',

"selenium navigate to a website": r'''driver.get("@?url?@")''',

"selenium find an element by id": r'''driver.find_element_by_id('@?id?@')''',

"selenium click on an element": r'''element.click()''',

"selenium submit a form": r'''element.submit()''',

"Start a Redis server": r'''redis-server''',

"Docker start a container": r'''docker start @?container_id?@''',

"Docker stop a container": r'''docker stop @?container_id?@''',

"Hadoop start all services": r'''start-all.sh''',

"Docker Compose build and run services": r'''docker-compose up --build -d''',

"Deploy with Kubernetes": r'''kubectl apply -f @?service_name?@.yaml''',

"Terraform initiate a working directory": r'''terraform init''',

"Terraform validate the configuration files": r'''terraform validate''',

"Terraform deploy the infrastructure": r'''terraform apply''',

"Update package list on Ubuntu": r'''sudo apt-get update''',

"Upgrade installed packages on Ubuntu": r'''sudo apt-get upgrade''',

"Install a package on Ubuntu": r'''sudo apt install @?package_name?@''',

"Check Ubuntu version": r'''lsb_release -a''',

"Check disk space on Unix/Linux": r'''df -h''',

"Check memory usage on Unix/Linux": r'''free -m''',

"Create a new user on Unix/Linux": r'''adduser @?username?@''',

"Give sudo privileges to a user on Ubuntu": r'''usermod -aG sudo @?username?@''',

"SSH into a remote server": r'''ssh @?username?@@@?ip_address?@''',

"Copy files to a remote server": r'''scp @?file_path?@ @?username?@@@?ip_address?@:@?destination_path?@''',

"Install Docker on Ubuntu": r'''curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh''',

"Add user to Docker group": r'''sudo usermod -aG docker @?username?@''',

"Install Docker Compose on Ubuntu": r'''sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose &&
sudo chmod +x /usr/local/bin/docker-compose''',

"Pull Docker image": r'''docker pull @?image_name?@''',

"Run Docker container": r'''docker run -d -p @?host_port?@:@?container_port?@ --name @?container_name?@ @?image_name?@''',

"Install Node.js and npm on Ubuntu": r'''sudo apt install -y nodejs npm''',

"Start MySQL server": r'''sudo systemctl start mysql''',

"Log in to MySQL server": r'''mysql -u @?username?@ -p''',

"Git clone repository": r'''git clone @?repository_url?@''',

"Git check status": r'''git status''',

"Git add files to staging": r'''git add .''',

"Git commit changes": r'''git commit -m "@?commit_message?@"''',

"Git push changes to repository": r'''git push origin master''',

"Create a new directory in UNIX/Linux": r'''mkdir @?new_directory?@''',

"Change directory in UNIX/Linux": r'''cd @?directory_name?@''',

"List directory contents in UNIX/Linux": r'''ls''',

"Python run a script": r'''python @?script_name?@.py''',

"Node.js run a script": r'''node @?script_name?@.js''',

"Java compile a program": r'''javac @?program_name?@.java''',

"Java run a program": r'''java @?program_name?@''',

"C/C++ compile a program using gcc": r'''gcc -o @?program_name?@ @?program_name?@.c''',

"C/C++ run a compiled program": r'''./@?program_name?@''',

"Open a file with vim": r'''vim @?filename?@''',

"Exit vim": r''':q!''',

"Install package with npm": r'''npm install @?package_name?@''',

"Start a PostgreSQL server": r'''pg_ctl -D /usr/local/var/postgres start''',

"Connect to a PostgreSQL database": r'''psql -h localhost -U postgres -d @?database_name?@''',

"Docker build an image": r'''docker build -t @?image_name?@ .''',

"Docker run a container": r'''docker run -p 4000:80 @?image_name?@''',

"Docker list running containers": r'''docker ps''',

"Launch a python interactive shell with Django": r'''python manage.py shell''',

"Django create a new application": r'''python manage.py startapp @?app_name?@''',

"Django run a server": r'''python manage.py runserver''',

"Django migrate database": r'''python manage.py migrate''',

"Scrapy start a new project": r'''scrapy startproject @?project_name?@''',

"Scrapy crawl a spider": r'''scrapy crawl @?spider_name?@''',

"selenium navigate to a website": r'''driver.get("@?url?@")''',

"selenium find an element by id": r'''driver.find_element_by_id('@?id?@')''',

"selenium click on an element": r'''element.click()''',

"selenium submit a form": r'''element.submit()''',

"Start a Redis server": r'''redis-server''',

"Docker start a container": r'''docker start @?container_id?@''',

"Docker stop a container": r'''docker stop @?container_id?@''',

"Hadoop start all services": r'''start-all.sh''',

"Docker Compose build and run services": r'''docker-compose up --build -d''',

"Deploy with Kubernetes": r'''kubectl apply -f @?service_name?@.yaml''',

"Terraform initiate a working directory": r'''terraform init''',

"Terraform validate the configuration files": r'''terraform validate''',

"Terraform deploy the infrastructure": r'''terraform apply''',

"Update package list on Ubuntu": r'''sudo apt-get update''',

"Upgrade installed packages on Ubuntu": r'''sudo apt-get upgrade''',

"Install a package on Ubuntu": r'''sudo apt install @?package_name?@''',

"Check Ubuntu version": r'''lsb_release -a''',

"Check disk space on Unix/Linux": r'''df -h''',

"Check memory usage on Unix/Linux": r'''free -m''',

"Create a new user on Unix/Linux": r'''adduser @?username?@''',

"Give sudo privileges to a user on Ubuntu": r'''usermod -aG sudo @?username?@''',

"SSH into a remote server": r'''ssh @?username?@@@?ip_address?@''',

"Copy files to a remote server": r'''scp @?file_path?@ @?username?@@@?ip_address?@:@?destination_path?@''',

"Install Docker on Ubuntu": r'''curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh''',

"Add user to Docker group": r'''sudo usermod -aG docker @?username?@''',

"Install Docker Compose on Ubuntu": r'''sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose &&
sudo chmod +x /usr/local/bin/docker-compose''',

"Pull Docker image": r'''docker pull @?image_name?@''',

"Run Docker container": r'''docker run -d -p @?host_port?@:@?container_port?@ --name @?container_name?@ @?image_name?@''',

"Install Node.js and npm on Ubuntu": r'''sudo apt install -y nodejs npm''',

"Start MySQL server": r'''sudo systemctl start mysql''',

"Log in to MySQL server": r'''mysql -u @?username?@ -p''',

"Install BeautifulSoup for parsing HTML": r'''pip install beautifulsoup4''',

"Install Requests for HTTP requests": r'''pip install requests''',

"Install Selenium for browser automation": r'''pip install selenium''',

"Install the WebDriver for your Browser (e.g., Chrome)": r'''# Must be done manually by downloading the correct driver''',

"Install Scrapy for robust web scraping": r'''pip install Scrapy''',

"Start a new Scrapy project": r'''scrapy startproject @?project_name?@''',

"Generate a Spider for Scrapy project": r'''cd @?project_name?@
scrapy genspider @?spider_name?@ @?website?@''',

"Run a Scrapy Spider": r'''scrapy crawl @?spider_name?@''',

"Export Scrapy Spider results to JSON": r'''scrapy crawl @?spider_name?@ -o @?results.json?@'''
,
              
              "create a new github repo and push all this folder": r'''
gh repo create @?projectname?@ --confirm @?--private or --public?@
git init
#touch readME.md   #this is to create an initial file to push
echo -e 'env\n__pycache__\n.env\nlib64/\nlib/\nshare' > .gitignore
git add .
git commit -m "first"
git remote add origin https://github.com/@?username?@/myproject.git
git branch -M main
git push -u origin main
''',
"delete .git" : r'''rm -fr .git''',
"push repo" : r'''git push @?source?@ @?destination?@''',
"push all repo" : r'''git add . 
git commit -m "autocommit"
git push @?source?@ @?destination?@''',
"install python" : r'''sudo apt-get install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.8''',
"delete .git" : r'''rm -fr .git''',
"delete .git" : r'''rm -fr .git''',
"delete .git" : r'''rm -fr .git''',

"Make directory" : r'''mkdir some_directory''',

"Change directory" : r'''cd some_directory''',

"Listing directory" : r'''ls''',

"Install pip (Python package manager)" : r'''sudo apt install python3-pip''',

"Install Python package with pip" : r'''pip3 install some_package''', 

"Run Python Script" : r'''python3 some_script.py''',

"Check Python Version" : r'''python3 --version''',

"Create an empty file" : r'''touch some_file''',

"Edit a file" : r'''nano some_file''',

"Check OS version" : r'''cat /etc/os-release''',

"Update all packages" : r'''sudo apt-get update && sudo apt-get upgrade''',

"Installing Git" : r'''sudo apt-get install git''',

"Cloning a Git Repository" : r'''git clone some_git_repo_URL''',

"Delete a directory" : r'''rm -R some_directory''',

"Installing Node.js and NPM": r'''sudo apt install nodejs npm''',

"Install a specific version of a package with pip" : r'''pip install some_package==some_version''',
    
"Make script executable" : r'''chmod +x some_script.sh''',

"Execute script" : r'''./some_script.sh''',

"Process monitoring" : r'''top''',

"Find process ID related to a running service" : r'''pgrep -f some_service''',

"Kill process by ID" : r'''kill -9 process_id''',

"Installing Docker" : r'''sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
sudo apt-get update
sudo apt-get install docker-ce''',

"Create Tarball (Compress directory)" : r'''tar -czvf archive_name.tar.gz directory_to_compress''',

"Extract Tarball (Uncompress directory)" : r'''tar -xzvf archive_name.tar.gz''',

"Create a Python virtual environment": r'''python3 -m venv myenv''',

"Activate Python environment": r'''source myenv/bin/activate''',

"Deactivate Python environment": r'''deactivate''',

"Install Jupyter Lab": r'''pip install jupyterlab''',

"Install complex package such as OpenCV": r'''pip install opencv-python-headless''' ,

"Run a Python script with arguments": r'''python3 some_script.py @?arg1?@ @?arg2?@''',

"Create a new branch in Git" : r'''git checkout -b @?branchname?@''',

"Switch to different Git branch" : r'''git checkout @?branchname?@''',

"Push git branch to remote" : r'''git push -u origin @?branchname?@''',

"Create a Python virtual environment with a specific name": r'''python3 -m venv @?envname?@''',

"Active Python environment with a specific name": r'''source @?envname?@/bin/activate''',

"Install specific python package in active environment": r'''pip install @?packagename?@''',

"Pull from a specific git branch": r'''git pull origin @?branchname?@''',

"Start a specific Docker container": r'''docker start @?containername?@''',

"Stop a specific Docker container": r'''docker stop @?containername?@''',

"Run a command in a specific Docker container": r'''docker exec -it @?containername?@ @?command?@''',

"Create a user in Linux": r'''sudo adduser @?username?@''',

"Add user to sudo group in Linux": r'''sudo usermod -aG sudo @?username?@''',

"Create a blank MySQL database and user": r'''CREATE DATABASE @?database?@; 
CREATE USER '@?user?@'@'localhost' IDENTIFIED BY '@?password?@';
GRANT ALL PRIVILEGES ON @?database?@.* TO '@?user?@'@'localhost'; 
FLUSH PRIVILEGES;''',

"Open an interactive Python shell in Docker Container": r'''docker run -it --rm @?imagename?@ python3''',

"Build a Docker image from Dockerfile": r'''docker build -t @?imagename?@:@?tag?@ .''',

"Run a Docker image with a specific port mapping": r'''docker run -d -p @?hostport?@:@?containerport?@ @?imagename?@''',

"Run a Docker container and mount a volume": r'''docker run -d -v @?hostdirectory?@:@?containerdirectory?@ @?imagename?@''',

"Check disk usage of directories": r'''du -sh @?directoryname?@''',

"Find files matching a pattern": r'''find . -name "@?pattern?@"''',

"Replace text in a file": r'''sed -i 's/@?oldtext?@/@?newtext?@/g' @?filename?@''',

"Zipping a directory": r'''zip -r @?archive.zip?@ @?directoryname?@''',

"Unzipping a directory": r'''unzip @?archive.zip?@''',

"Writing and reading to/from a file using script": r'''echo "@?text?@" > @?filename?@
cat @?filename?@''',

"SCP a file to remote server": r'''scp @?filename?@ @?user?@@@?host?@:@?directory?@''',

"Setup MySQL root user and password": r'''mysqladmin -u root password @?newpassword?@
mysqladmin -h localhost -u root -p @?newpassword?@''',

"Create a new RabbitMQ user": r'''rabbitmqctl add_user @?username?@ @?password?@
rabbitmqctl set_user_tags @?username?@ administrator
rabbitmqctl set_permissions -p / @?username?@ ".*" ".*" ".*"''',

"Create systemd service for script": r'''
echo -e '[Unit]
Description=@?desiredServiceDescription?@
After=network.target
[Service]
ExecStart=/usr/bin/python3 /path/to/@?yourscript.py?@
Restart=always
[Install]
WantedBy=multi-user.target' | sudo tee /etc/systemd/system/@?desiredServiceName?@.service
sudo systemctl daemon-reload
sudo systemctl start @?desiredServiceName?@
sudo systemctl enable @?desiredServiceName?@''',

"Create New PostgreSQL Database and User": r'''sudo -u postgres createuser @?username?@
sudo -u postgres createdb --owner=@?username?@ @?dbname?@''',

"Give Specific Privileges to User in PostgreSQL": r'''sudo -u postgres psql
GRANT ALL PRIVILEGES ON DATABASE @?dbname?@ to @?username?@;
\q''',

"Assign sudo Privileges to User in Linux": r'''usermod -aG sudo @?username?@''',

"Make a Curl Request": r'''curl -X GET http://@?url?@''',

"Create a hard link": r'''ln @?source_file?@ @?link?@''',

"Create a symbolic link": r'''ln -s @?source_file_replace?@ @?link_replace?@''',

"Download file with wget": r'''wget @?file_url?@''',

"Extract a .tar.gz file": r'''tar -xzf @?file?@.tar.gz''',

"Running a SQL file in a PostgreSQL database": r'''psql -U @?username?@ -d @?dbname?@ -a -f @?file.sql?@''',

"Change the ownership of a file or directory": r'''chown @?user?@: @?filename/directory?@''',

"Check listening ports and applications": r'''netstat -tuln''',

"Add user to a specific group": r'''sudo usermod -a -G @?group?@ @?username?@''',

"Change firewall rules (UFW)": r'''sudo ufw allow @?portnumber?@''',

"Encrypt a file with GPG": r'''gpg -c @?filename?@''',

"Decrypt a GPG file": r'''gpg @?filename.gpg?@''',

"Create a Docker Swarm": r'''docker swarm init --advertise-addr @?IP_address?@''',

"Deploy a service to Docker Swarm": r'''docker service create --replicas 1 --name @?service?@ @?docker_image?@''',

"Scale a service in Docker Swarm": r'''docker service scale @?service?@=@?num_replicas?@''',

"Create encrypted password with OpenSSL": r'''openssl passwd -1 @?password?@''',

"Running a Python HTTP server": r'''python3 -m http.server @?port?@''',

"Running a script on a Remote Machine": r'''ssh @?user?@@@?server?@ 'bash -s' < @?script.sh?@''',

"Setting Permissions on a Folder": r'''setfacl -m u:@?user?@:@?permissions?@ @?folder?@''',

"Transfer a file using SCP": r'''scp @?local_file?@ @?user?@@@?target?@:/@?target_directory?@/''',

"Networking | Interact with raw data from a website": r'''curl -s https://@?website_url?@ | grep @?some_text?@''',

"Run a process in the background": r'''nohup @?your_command?@ &''',

"Adding a cron job": r'''crontab -e
* * * * * /usr/bin/env @?some_script.sh?@''',

"Kill all processes for a given user": r'''pkill -U @?user?@''',

"Log in to Docker Hub": r'''docker login --username=@?username?@ --password=@?password?@''',

"Push an image to Docker Hub": r'''docker push @?username?@/'@?imagename?@''',

"Run job every amount of minute": r'''crontab -e
*/@?minute?@ * * * @?command?@''',

"Run job every minute": r'''crontab -e
* * * * * @?command?@''',

"Run job every 5 minutes": r'''crontab -e
*/5 * * * * @?command?@''',

"Run job every hour": r'''crontab -e
0 * * * * @?command?@''',

"Run job every day at midnight": r'''crontab -e
0 0 * * * @?command?@''',

"Run job on specific minute (5 past every hour)": r'''crontab -e
5 * * * * @?command?@''',

"Run job at a specific time (2:30 PM)": r'''crontab -e
30 14 * * * @?command?@''',

"Run job every day in a specific month (here every day at 2:30 PM in January)": r'''crontab -e
30 14 * JAN * @?command?@''',

"Run job every Monday at a specific time (here every Monday at 2:30 PM)": r'''crontab -e
30 14 * * MON @?command?@''',

"Run job every quarter (here every 1st of Jan, Apr, Jul, Oct at 2:30 PM)": r'''crontab -e
30 14 1 JAN,APR,JUL,OCT * @?command?@''',

"Delete (clear) all crontab jobs": r'''crontab -r''',

"Run job every @?n?@ minutes": r'''crontab -e
*/@?n?@ * * * * @?command?@''',

"Run job every @?n?@ hours": r'''crontab -e
0 */@?n?@ * * * @?command?@''',

"Run job at a specific time (@?h?@: @?m?@ AM/PM)": r'''crontab -e
*m* *h* * * * @?command?@''',

"Run job every day of a specific month at a specific time (@?h?@: @?m?@ AM/PM)": r'''crontab -e
*m* *h* * @?month?@ @?command?@''',

"Run job on a specific day of the week at a specific time (@?h?@: @?m?@ AM/PM)": r'''crontab -e
*m* *h* * * @?day?@ @?command?@''',

"Run job every quarter at a specific time (@?h?@: @?m?@ AM/PM)": r'''crontab -e
*m* *h* 1 @?month_set?@ @?command?@''',

"Install Flask via pip": r'''pip install flask''',

"Set environment variable for Flask app": r'''export FLASK_APP=@?your_flask_app?@.py*''',

"Run Flask Development Server": r'''flask run''',

"Run Flask Development Server with debug mode": r'''export FLASK_ENV=development
flask run''',

"Run Flask on Specific Port": r'''flask run --host=0.0.0.0 --port=@?port_number?@*''',

"Run Flask Application with gunicorn": r'''gunicorn -w 4 -b 0.0.0.0:@?port_number?@ @?module_name?@:app*''',

"Install Flask-SQLAlchemy (for database operations)": r'''pip install Flask-SQLAlchemy''',

"Install Flask-Migrate (for database migrations)": r'''pip install Flask-Migrate''',

"Initialize database": r'''flask db init''',

"Migrate database (generate migration scripts)": r'''flask db migrate -m "@?message?@''',

"Apply migration to database": r'''flask db upgrade''',

"Run flask shell for interactive shell context": r'''flask shell''',

"Changing file permissions": r'''chmod @?permission_numbers?@ @?file?@''',

"Changing directory permissions": r'''chmod @?permission_numbers?@ @?directory?@''',

"Changing ownership of a file": r'''chown @?username?@ @?file?@''',

"Changing ownership of a directory": r'''chown @?username?@ @?directory?@''',

"Running a script with specific interpreter": r'''@?interpreter?@ @?your_script?@''',

"Creating a directory": r'''mkdir @?directory_name?@''',

"Creating a file": r'''touch @?file_name?@''',

"Removing a file": r'''rm @?file_name?@''',

"Remove a directory and its contents": r'''rm -r @?directory_name?@''',

"Move or rename a file": r'''mv @?source?@ @?destination?@''',

"Copy a file": r'''cp @?source?@ @?destination?@''',

"Print the working directory": r'''pwd''',

"Moving into a directory": r'''cd @?directory?@''',

"Coming out of a directory": r'''cd ..''',

"Going to the home directory": r'''cd ~''',

"Writing to a file": r'''echo "@?text?@" > @?file?@''',

"Reading from a file": r'''cat @?file?@''',

"Running a Python script with arguments": r'''python3 @?script?@ @?arg1?@ @?arg2?@...''',

"Count words in a file": r'''wc -w @?file?@''',

"Monitor a file in real time": r'''tail -f @?file?@''',

"Find in files recursively": r'''grep -r @?search_string?@ @?directory?@''',

"Disk usage of directory": r'''du -sh @?directory?@''',

"Find files modified in the last @?n?@ days": r'''find @?directory?@ -mtime -@?n?@''',

"Find and replace text in all files recursively": r'''find @?directory?@ -type f -exec sed -i 's/@?search_string?@/@?replacement_string?@/g' @??@ \;''',

"Creating tarball of a directory": r'''tar -cvf @?archive_name?@.tar* @?directory?@''',

"Extracting a tarball": r'''tar -xvf @?archive_name?@.tar*''',

"Creating a gzipped tarball of a directory": r'''tar -cvzf @?archive_name?@.tar.gz* @?directory?@''',

"Extracting a gzipped tarball": r'''tar -xvzf @?archive_name?@.tar.gz*''',

"Check the syntax of a Python script": r'''python -m py_compile @?script?@.py*''',

"Run a Python script in the background": r'''nohup python @?script?@.py* &''',

"Check which Python packages are outdated": r'''pip list --outdated''',

"Update all Python packages": r'''pip freeze | cut -d = -f 1 | xargs -n1 pip install -U''',

"Compress a directory excluding some directories": r'''tar -cvzf @?archive_name?@.tar.gz* --exclude=@?directory_to_exclude?@ @?directory_to_compress?@''',

"List all services using systemctl": r'''systemctl list-units --type=service''',

"Check status of a service": r'''systemctl status @?service_name?@''',

"Start a service": r'''sudo systemctl start @?service_name?@''',

"Stop a service": r'''sudo systemctl stop @?service_name?@''',

"Check all running processes": r'''ps aux''',

"Check for running process": r'''ps aux | grep @?process_name?@''',

"Kill a process by its PID": r'''kill -9 @?PID?@''',

"Check the memory usage of the system": r'''free -m''',

"Check the disk usage of the system": r'''df -h''',

"SSH into a machine": r'''ssh @?username?@@@?hostname?@''',

"Run a command on a remote machine using ssh": r'''ssh @?username?@@@?hostname?@ @?command?@''',

"Copy file to a remote machine": r'''scp @?file?@ @?username?@@@?hostname?@:@?directory?@''',

"Check IP address of the machine": r'''ip addr show''',

"Check network statistics": r'''netstat -s''',

"Fetch the raw HTML content of a webpage": r'''curl @?url?@''',

"Save the HTML content of a webpage to a file": r'''curl @?url?@ -o @?filename?@''',

"Download a file from a given URL": r'''wget @?url?@''',

"Download and save with a specific filename": r'''wget -O @?filename?@ @?url?@''',

"Download files in the background": r'''wget -b @?url?@''',

"Download and retry for n times in case of failure": r'''wget --tries=@?n?@ @?url?@''',

"Download an entire website": r'''wget --mirror --convert-links --adjust-extension --page-requisites --no-parent @?website_url?@''',

"Download files from a list contained in a file": r'''wget -i @?file_containing_urls.txt?@''',

"Download only certain file types (e.g., .jpg)": r'''wget -r -A '*.jpg' @?website_url?@''',

"Crawl website and save for offline viewing": r'''wget --convert-links --mirror --trust-server-names --adjust-extension --span-hosts --backup-converted --page-requisites -P @?save_to?@ @?website_url?@''',

"Install BeautifulSoup for parsing HTML": r'''pip install beautifulsoup4''',

"Install Requests for HTTP requests": r'''pip install requests''',

"Install Selenium for browser automation": r'''pip install selenium''',

"Install the WebDriver for your Browser (e.g., Chrome)": r'''# Must be done manually by downloading the correct driver''',

"Install Scrapy for robust web scraping": r'''pip install Scrapy''',

"Start a new Scrapy project": r'''scrapy startproject @?project_name?@''',

"Generate a Spider for Scrapy project": r'''cd @?project_name?@
scrapy genspider @?spider_name?@ @?website?@''',

"Run a Scrapy Spider": r'''scrapy crawl @?spider_name?@''',

"Export Scrapy Spider results to JSON": r'''scrapy crawl @?spider_name?@ -o @?results.json?@'''
}


