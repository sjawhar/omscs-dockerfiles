from os import environ
import sys

if sys.version_info[0] > 2:
  import http.server as SimpleHTTPServer
  import socketserver as SocketServer
else:
  import SimpleHTTPServer
  import SocketServer

from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

if environ["POLLING"]:
  from watchdog.observers.polling import PollingObserver as Observer
else:
  from watchdog.observers import Observer

from watchdog.events import PatternMatchingEventHandler
from subprocess import check_output, CalledProcessError, STDOUT
from io import BytesIO

import time
import threading
import json
import timeit
import webbrowser

PORT = int(environ["PORT"]) if environ["PORT"] else 80
FILE = environ["FILE"] if environ["FILE"] else "src/RavensProject.py"
PYTHON_COMMAND = "python"

html_file = open("index.html", "r")
html = html_file.read()
html_file.close()

conns = []

class SimpleStdinPub(WebSocket):
  def handleConnected(self):
    conns.append(self)

  def handleClose(self):
    conns.remove(self)

class StringBodyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
  def send_head(self):
    if self.translate_path(self.path).endswith('/'):
      self.send_response(200)
      self.send_header("Content-type", "text/html; charset=utf-8")
      self.send_header("Content-Length", str(len(html)))
      self.end_headers()
      return BytesIO(html.encode())
    else:
      return SimpleHTTPServer.SimpleHTTPRequestHandler.send_head(self)

class AgentCodeChangeHandler(PatternMatchingEventHandler):
  def ensureUtf(self, s):
    try:
      return unicode(s)
    except: 
      return str(s)

  def sendWsJson(self, dict):
    for conn in conns:
      conn.sendMessage(self.ensureUtf(json.dumps(dict)))

  def on_any_event(self, event):
    print("Detected change in " + event.src_path)
    self.sendWsJson({ 'loading': True })

    start = timeit.default_timer()
    try:
      output = check_output([PYTHON_COMMAND, FILE], stderr = STDOUT)
      stop = timeit.default_timer()
      self.sendWsJson({ 'completed': True, 'output': output.decode('utf-8'), 'returncode': 0, 'time': stop - start })
    except CalledProcessError as e:
      stop = timeit.default_timer()
      self.sendWsJson({ 'completed': True, 'output': e.output.decode('utf-8'), 'returncode': e.returncode, 'time': stop - start })

if __name__ == "__main__":

  server = SimpleWebSocketServer('', PORT + 1, SimpleStdinPub)
  thread = threading.Thread(target=server.serveforever)
  thread.daemon = True
  thread.start()

  SocketServer.TCPServer.allow_reuse_address = True
  httpd = SocketServer.TCPServer(("", PORT), StringBodyHandler)

  observer = Observer()
  thread2 = threading.Thread(target=httpd.serve_forever)
  thread2.daemon = True
  thread2.start()

  url = "http://localhost:" + str(PORT)
  print("Serving at " + url)
  webbrowser.open(url)

  ignore_patterns = ['*/.git', '*/.git/*', '*/.hg', '*/.hg/*']
  event_handler = AgentCodeChangeHandler(patterns=["*.py", "*.txt"], ignore_patterns=ignore_patterns)
  observer.schedule(event_handler, '.', recursive=True)
  observer.start()

  try:
    while True:
      time.sleep(1)
  except KeyboardInterrupt:
    observer.stop()
  finally:
    httpd.server_close()
    observer.stop()
  observer.join()

