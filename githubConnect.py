'''
docker run -v /Users/zafarkamal/Downloads/logs:/app/logs --rm zafarkamal84/githubconnect.py:3.1

# This command runs the Docker container using the image 'zafarkamal84/githubconnect.py:3.1'.
# The '-v' option mounts the local directory '/Users/zafarkamal/Downloads/logs' on the host
# to the '/app/logs' directory inside the container. This means that any logs generated
# by the script inside the container at '/app/logs' will be directly saved to the
# '/Users/zafarkamal/Downloads/logs' directory on your local machine.
# The '--rm' flag ensures that the container is automatically removed after it stops.

to  run  on the local host

uncomment this log_dir = f"{user_home_dir}/Downloads/logs/"
comment this  #log_dir = '/app/logs/'  # This directory should be mounted to the host's directory
'''


import requests
import time
import logging
import os
from datetime import datetime

#: This is a special built-in variable that stores the path of the script being executed.
script_path = __file__
# Extract the script name (file name) from the full path
script_name = os.path.basename(script_path)
user_home_dir = os.path.expanduser("~")
print (f"User home directory {user_home_dir}")
print(f"The script name is: {script_name}")
# Create a unique log file name based on the current timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#log_dir = f"{user_home_dir}/Downloads/logs/"
log_dir = '/app/logs/'  # This directory should be mounted to the host's directory
filename = f"{log_dir}app_{script_name}_{timestamp}.log"  # Log file name
print (f"log file name is {filename}")
# Define the directory inside the container where logs will be written

 # File handler for logging to file
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler(filename)
logging.basicConfig(
    #filename = f"{log_dir}app_{script_name}_{timestamp}.log",  # Log file name
    level=logging.INFO,  # Log level: INFO captures everything except debug messages
    format='%(asctime)s - %(levelname)s - %(message)s',# Log format
    handlers=[console_handler,file_handler]
)

def url_parsing(URL):
    try:
        logging.info(f"Attempting to connect to {URL} and fetch data")
        response = requests.get(URL)
        if response.status_code !=200:
            logging.error("Failed to fetch data. Error code: {response.status_code}")
            print (f"Error code is {response.status_code}")
        else:
            logging.info(f"Data fetched successfully {URL}")
            completedata = response.json()
            for data in completedata:
                #print(f"Project Name is {data['name']}, User Name is {data['full_name']}, Login Name is {data['owner']['login']}, URL is {data['url']} {response.status_code}")
                logging.info(f"{data['name']},{data['full_name']},{data['owner']['login']},{data['url']},{response.status_code}")
                return ({data['name']},{data['full_name']},{data['owner']['login']},{data['url']},{response.status_code})
    except:
        logging.exception(f"An error occurred during parsing {URL}")
        print("something is wrong with input")

def generate_html_email(data):
    # Creating the HTML content
    html_content = f"""
    <html>
    <head></head>
    <body>
        <h2>GitHub Repository Information</h2>
        <table border="1" cellpadding="5" cellspacing="0">
            <tr>
                <th>Project Name</th>
                <th>Full Name</th>
                <th>Login Name</th>
                <th>Repository URL</th>
                <th>Status Code</th>
            </tr>
            <tr>
                <td>{data[0]}</td>
                <td>{data[1]}</td>
                <td>{data[2]}</td>
                <td><a href="{data[3]}">{data[3]}</a></td>
                <td>{data[4]}</td>
            </tr>
        </table>
    </body>
    </html>
    """
    return html_content

for remaining in range(10,0,-5):
    logging.info(f"Waiting for {remaining} seconds")
    print (f"Please wait for {remaining} seconds\n")
    time.sleep(5)
returned_data = url_parsing("https://api.github.com/users/zafarkamal/repos")
logging.info(f"GitHUb project name is {returned_data[0]},{returned_data[1]},UserName is :{returned_data[2]},WEB_URL: {returned_data[3]},Status Code:{returned_data[4]}")
print (returned_data[0],returned_data[1],returned_data[2],returned_data[3],returned_data[4])

for handler in logging.getLogger().handlers:
    handler.flush()
    handler.close()

