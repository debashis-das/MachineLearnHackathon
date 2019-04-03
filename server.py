from flask import render_template
import connexion

# Create the application instance
application = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure the endpoints
application.add_api('swagger.yml')

# Create a URL route in our application for "/"
@app.route('/')
def home():
    return render_template('home.html')

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    application.run(host='0.0.0.0')