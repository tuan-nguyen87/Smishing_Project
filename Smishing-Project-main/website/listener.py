#from flask import Flask, request
#from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.chrome.options import Options
#from webdriver_manager.chrome import ChromeDriverManager

#app = Flask(__name__)

#@app.route('/login', methods=['POST'])
#def login():
    # Read the username and password from the POST request
    #username = request.form['username']
    #password = request.form['password']

    # TODO: Add your login script here to login with the provided credentials
    # Initialize the driver object
    #print(username)
    #print(password)
    #return "Login successful!"  # Return a response to the client

#if __name__ == '__main__':
    #app.run(debug=True)  # Run the server in debug mode


from flask import Flask, request

app = Flask(__name__)

@app.route('/Users/karypaquot/documents/github/smishing-project/website/listener.py', methods=['POST'])
def process_data():
    ##username = request.form['username']
    #password = request.form['password']
    # Do something with the username
    #print(username)
    #print(password)

    # Get the input values from the request body
    username = request.json['username']
    password = request.json['password']

    # Run your Python script here
    print("Received input values: username={}, password={}".format(username, password))
    return "Script executed successfully"

if __name__ == '__main__':
    app.run()