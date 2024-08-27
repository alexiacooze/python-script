from flask import Flask, request, jsonify
import json
import logging
import numpy as np
import pandas as pd

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/execute', methods=['POST'])
def execute_script():
    app.logger.debug("Received request: %s", request.data)
    
    # Check if JSON payload is provided
    if not request.is_json:
        return jsonify({"error": "Request must be in JSON format"}), 400
    
    data = request.get_json()
    script = data.get('script', '')

    # Basic input validation
    if not script:
        return jsonify({"error": "No script provided"}), 400
    
    if not isinstance(script, str):
        return jsonify({"error": "Script must be a string"}), 400

    if len(script) > 1000:  # Arbitrary size limit for security
        return jsonify({"error": "Script is too long"}), 400

    # Basic keyword filtering with numpy and pandas allowed
    disallowed_keywords = [
        'sys', 'shutil', 'open', 'builtins', 'input', 'compile',
        'pickle', 'cPickle', 'execfile', 'getattr', 'setattr', 'delattr',
        'os.system', 'subprocess.Popen'
    ]
    
    if any(keyword in script for keyword in disallowed_keywords):
        return jsonify({"error": "Script contains disallowed keywords"}), 400
    local_vars = {}
    
    try:
        # Provide 'numpy' and 'pandas' as 'np' and 'pd' to the exec environment
        exec(script, {'np': np, 'pd': pd}, local_vars)
        
        # Check if 'main' function is defined
        if 'main' not in local_vars or not callable(local_vars['main']):
            return jsonify({"error": "The script must define a callable 'main' function."}), 400
        
        # Call the 'main' function and get the result
        result = local_vars['main']()
        
        # Ensure the result is JSON serializable
        if not isinstance(result, dict):
            return jsonify({"error": "The 'main' function must return a JSON serializable dictionary."}), 400
        
        return jsonify(result)
    except Exception as e:
        app.logger.error("Error executing script: %s", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
