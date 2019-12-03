from app import app
import logging

logg = logging
logg.basicConfig(level=logging.INFO)
app.add_api('openapi.yaml')

if __name__ == '__main__':
    app.run(port=5000, use_reloader=False, threaded=False, debug=True)
