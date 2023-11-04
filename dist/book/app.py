
from flask import Flask
import subprocess
import psutil

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <html>
    <body>
        <h1>Click the button to listen the audio book:</h1>



        
        <button onclick="runScript()">Object Oriented Programming</button>
        <button onclick="runScript2()">Java Script</button>


               <style>
          h1 {
    font-family: Arial, sans-serif;
    text-align: center;
    color: #4CAF50;
}

button {
    font-family: 'Arial', sans-serif;
    font-size: 16px;
    background-color: #008CBA;
    color: white;
    border: none;
    padding: 10px 20px;
    margin: 10px;
    cursor: pointer;
    border-radius: 5px;
    transition: background-color 0.3s ease;
}

button:hover {
    background-color: #005A6E;
}

button:focus {
    outline: none;
    box-shadow: 0 0 5px 0px #4CAF50;
}
</style>

        <script>
            function runScript() {
                fetch('/run-script')
                    .then(response => response.text())
                    .then(data => alert(data));
            }
        </script>

        <script>
            function runScript2() {
                fetch('/run-script2')
                    .then(response => response.text())
                    .then(data => alert(data));
            }
        </script>



    </body>
    </html>
    '''

@app.route('/run-script')
def run_script():
    result = subprocess.run(['python', 'opp.py'], capture_output=True, text=True)
    return result.stdout


@app.route('/run-script2')
def run_script2():
    result = subprocess.run(['python', 'js.py'], capture_output=True, text=True)
    return result.stdout







if __name__ == '__main__':
    app.run(debug=True)

