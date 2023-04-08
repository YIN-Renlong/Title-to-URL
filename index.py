import re
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

def normalize_url(title, year, month, day):
    # Remove any non-alphanumeric characters from the title
    title = re.sub(r'\W+', ' ', title)
    # Replace any remaining spaces with hyphens
    title = re.sub(r'\s+', '-', title)
    # Convert the title to lowercase
    title = title.lower()
    # Construct the URL using the provided year, month, and day
    url = f'https://www.website.com/{year}/{month:02}/{day:02}/{title}/'
    return url

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Serve the form HTML when a GET request is received
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'''
        <html>
        <head>
            <title>Title to URL</title>
        </head>
        <body>
            <form action="/" method="post">
                <label for="link">Link address:</label>
                <input type="text" id="link" name="link"><br>

                <label for="title">Article title:</label>
                <input type="text" id="title" name="title"><br>

                <label for="month">Month:</label>
                <input type="text" id="month" name="month"><br>

                <label for="day">Day:</label>
                <input type="text" id="day" name="day"><br>

                <label for="year">Year:</label>
                <input type="text" id="year" name="year"><br>

                <input type="submit" value="Generate URL">
            </form>
        </body>
        </html>
        ''')

    def do_POST(self):
        # Process the form data and return the generated URL when a POST request is received
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        post_params = parse_qs(post_data.decode('utf-8'))
        link = post_params['link'][0]
        title = post_params['title'][0]
        month = post_params['month'][0]
        day = post_params['day'][0]
        year = post_params['year'][0]
        url = normalize_url(title, year, month, day)
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(url.encode())

if __name__ == '__main__':
    # Start the HTTP server and listen for requests
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    httpd.serve_forever()
