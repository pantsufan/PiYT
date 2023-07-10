import http.server
import socketserver

# Define the directory to serve files from
directory = "Output"

# Define the port for the HTTP server
port = 80

# Change the current directory to the specified directory
if directory:
    import os
    os.chdir(directory)

# Start the HTTP server
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", port), Handler) as httpd:
    print(f"Server started on port {port}")
    httpd.serve_forever()
