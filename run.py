from app import app, WSGI
import signal

# use gevent WSGI server instead of the Flask
http = WSGI

def stop_server(*args, **kwargs):
    print("Server stopped!")
    http.stop()

def run_server():
    print("Running server at: {}:{}".format(http.address[0], http.address[1]))
    http.serve_forever()
if __name__ == '__main__':
    
    signal.signal(signal.SIGINT, stop_server)
    run_server()
