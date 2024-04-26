import http.server
import socketserver
import sys

# Define the port you want to use
PORT = 8000

# Create a handler to serve the files
Handler = http.server.SimpleHTTPRequestHandler

# Set up the server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    print("http://127.0.0.1:8000")
    try:
        # Serve continuously until interrupted
        httpd.serve_forever()
    except KeyboardInterrupt:
        # Handle keyboard interrupt (Ctrl + C)
        print("\nServer stopped.")
        sys.exit(0)