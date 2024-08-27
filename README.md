# python-script

# correct curl command
curl -X POST http://localhost:8080/execute \
    -H "Content-Type: application/json" \
    -d '{"script": "def main():\n    return {\"message\": \"Hello, world!\"}\n"}'

Should return:

{
    "output": "{\"message\": \"Hello, world!\"}\n"
}


# Test Case: Script Without a main() Function
curl -X POST http://localhost:8080/execute \
    -H "Content-Type: application/json" \
    -d '{"script": "def hello():\n    return {\"message\": \"Hello, world!\"}\n"}'

Should return:

{
    "error": "The script must define a callable 'main' function."
}


# Test Case: Script Where main() Does Not Return JSON
curl -X POST http://localhost:8080/execute \
    -H "Content-Type: application/json" \
    -d '{"script": "def main():\n    return \"Hello, world!\"\n"}'

Should return:

{
    "error": "The 'main' function must return a JSON object."
}
