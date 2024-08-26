from flask import Flask, request, jsonify
import json
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/execute', methods=['POST'])
def execute_script():
    app.logger.debug("Received request: %s", request.data)
    data = request.get_json()
    script = data.get('script', '')
    local_vars = {}

    try:
        # Execute the script in a controlled environment
        exec(script, {}, local_vars)
        
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