from app import create_app
from app.config import socketio

app = create_app()

if __name__ == '__main__':
    socketio.run(app, debug=True, use_reloader=False)
