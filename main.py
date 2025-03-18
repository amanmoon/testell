import eel

# Initialize Eel with the folder containing your web files
eel.init('easy_tune/public')  # Assuming your index.html is in a folder named "web"

# Expose a Python function to JavaScript
@eel.expose
def my_python_function(name):
    return f"Hello, {name}! This message is from Python."

# Start the Eel app, which opens index.html in a local window
eel.start('index.html', size=(800, 600))
