
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

