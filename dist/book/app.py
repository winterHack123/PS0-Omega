
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
         <button onclick="runScript()">BOOK 1 - Object Oriented Programming</button>
        <button onclick="runScript2()">BOOK 2 - Java Script</button>

        <div class="container">
        <input type="file" id="pdfUploader" accept=".pdf">
        <button onclick="runScript3()">Run</button>
    </div>
    <div id="output"></div>


    <style>

  body {
    font-family: Arial, sans-serif;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    margin: 0;
}

.container {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
}

input[type="file"] {
    margin-right: 10px;
}

button {
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}

#output {
    margin-top: 20px;
    font-weight: bold;
}


.button-container {
    display: flex;
    justify-content: space-around;
    align-items: center;
    width: 300px; /* Set your desired width */
    height: 50px; /* Set your desired height */
    border: 1px solid #000; /* Optional: Add border for visual separation */
}

button {
    width: 100%; /* Make buttons take equal width inside the container */
}





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
        <script>
            function runScript3() {
                fetch('/run-script3')
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


@app.route('/run-script3')
def run_script3():
    result = subprocess.run(['python', 'dsa.py'], capture_output=True, text=True)
    return result.stdout







if __name__ == '__main__':
    app.run(debug=True)

