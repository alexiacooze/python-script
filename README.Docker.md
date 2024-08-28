### Building and running your application

docker build -t python-script-takehome .
docker run -p 8080:8080 python-script-takehome


http://localhost:8080/execute

# Run Unit Tests in Terminal
docker run --rm python-script-takehome pytest


## Testing the Endpoint on Postman/Curl
Using curl to Test the Endpoint
Here is how you can use curl to test the /execute endpoint:

curl -X POST "http://localhost:8080/execute" -H "Content-Type: application/json" -d '{"script": "def main(): return {\"message\": \"Hello, World!\"}"}'

Set the Content-Type Header:

Add a new header with Key as Content-Type and Value as application/json.

Add the JSON Payload in the Body Section: Select raw and JSON 

