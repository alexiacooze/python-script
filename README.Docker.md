### Building and running your application

docker build -t python-script-takehome .


docker run -p 8080:8080 python-script-takehome


http://localhost:8080/execute

## Testing the Endpoint
Using curl to Test the Endpoint
Here is how you can use curl to test the /execute endpoint:

curl -X POST "http://localhost:8080/execute" -H "Content-Type: application/json" -d '{"script": "def main(): return {\"message\": \"Hello, World!\"}"}'

Using Postman to Test the Endpoint
Set the Request Method to POST:

Open Postman.
Select POST from the dropdown menu next to the URL input field.
Set the URL:

Enter http://localhost:8080/execute in the URL input field.
Set the Content-Type Header:

Go to the Headers tab.
Add a new header with Key as Content-Type and Value as application/json.
Add the JSON Payload in the Body Section:

Go to the Body tab.
Select raw and choose JSON from the dropdown menu.

### Deploying your application to the cloud 

First, build your image, e.g.: `docker build -t myapp .`.
If your cloud uses a different CPU architecture than your development
machine (e.g., you are on a Mac M1 and your cloud provider is amd64),
you'll want to build the image for that platform, e.g.:
`docker build --platform=linux/amd64 -t myapp .`.

Then, push it to your registry, e.g. `docker push myregistry.com/myapp`.

Consult Docker's [getting started](https://docs.docker.com/go/get-started-sharing/)
docs for more detail on building and pushing.

### References
* [Docker's Python guide](https://docs.docker.com/language/python/)