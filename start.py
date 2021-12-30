from pwdcheck.server import app
import os
print(os.getcwd())
app.run('0.0.0.0', port=8090, debug=True)
