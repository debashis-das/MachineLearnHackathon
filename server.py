from flask import render_template
import connexion

def set_cors_headers_on_response(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'X-Requested-With'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS'
    return response

# Create the application instance
application = connexion.FlaskApp(__name__, specification_dir='./')
application.add_api('swagger.yml')
application.app.after_request(set_cors_headers_on_response)
# Create a URL route in our application for "/"
@application.route('/')
def home():
    return render_template('home.html')

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    application.run()
    
