import requests
def url_parsing(URL):
    try:
        response = requests.get(URL)
        if response.status_code !=200:
            print (f"Error code is {response.status_code}")
        else:
            completedata = response.json()
            for data in completedata:
                print(data)
                #print(f"Project Name is {data['name']}, User Name is {data['full_name']}, Login Name is {data['owner']['login']}, URL is {data['url']} {response.status_code}")
                #return (data['name'],data['full_name'],data['owner']['login'],data['url'],response.status_code)
    except:
        print("something is wrong with input")

url_parsing("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
url_parsing("https://pro-api.coingecko.com/api/v3/ping")
#print (html_returned)
#print (returned_data[0],returned_data[1],returned_data[2],returned_data[3],returned_data[4])

