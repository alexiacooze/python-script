# python-script

# Deployed curl url with Google Cloud API
curl -X POST https://python-script-takehome-urxqnrtkla-uc.a.run.app/execute \
    -H "Content-Type: application/json" \
    -d '{"script": "def main():\n    return {\"message\": \"Hello, world!\"}\n"}'

Should return:

{
    "output": "{\"message\": \"Hello, world!\"}\n"
}



# Test Case: Script Without a main() Function
curl -X POST https://python-script-takehome-urxqnrtkla-uc.a.run.app/execute \
    -H "Content-Type: application/json" \
    -d '{"script": "def hello():\n    return {\"message\": \"Hello, world!\"}\n"}'

Should return:

{
    "error": "The script must define a callable 'main' function."
}



# Test Case: Script Where main() Does Not Return JSON
curl -X POST https://python-script-takehome-urxqnrtkla-uc.a.run.app/execute \
    -H "Content-Type: application/json" \
    -d '{"script": "def main():\n    return \"Hello, world!\"\n"}'

Should return:

{
    "error": "The 'main' function must return a JSON serializable dictionary."
}



# Testing for Malicious Input
 curl -X POST https://python-script-takehome-urxqnrtkla-uc.a.run.app/execute \
    -H "Content-Type: application/json" \
    -d '{"script": "def main():\n    import os\n    os.system(\"rm -rf /\")"}'

Should return:

{
    "error":"Script contains disallowed keywords"
}



# Testing for Numpy and Pandas
 curl -X POST https://python-script-takehome-urxqnrtkla-uc.a.run.app/execute \
    -H "Content-Type: application/json" \
    -d '{"script": "import numpy as np\nimport pandas as pd\ndef main():\n    arr = np.array([1, 2, 3])\n    df = pd.DataFrame({\"A\": arr, \"B\": arr * 2})\n    return df.to_dict()"}'

Should return:

{"A":{"0":1,"1":2,"2":3},"B":{"0":2,"1":4,"2":6}}
