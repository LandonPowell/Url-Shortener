import web  # For the web server.
import json # For the database.

# Converts ints into strings in base 36. Shorter URLs.
def to36(number):
    alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
    base36 = ''
    while number:
        number, i = divmod(number, 36)
        base36 = alphabet[i] + base36
    return base36

# Loads the database['counter'] and database['links'].
database = json.loads(open('database.json').read())

urls = (
    '/([a-z\d]+)', 'redirect',
    '/.*',         'index'
)

# Redirects the user to the correct link.
class redirect:
    def GET(self, link):
        if link in database['links']:
            return web.redirect(database['links'][link])
        else:
            return "You seem to have mistyped that URL."

# Landing page and short-link creation.
class index:
    def GET(self):
        return open('index.html').read()
    def POST(self):
        shortURL = to36(database['counter'])
        database['counter'] += 1

        database['links'][shortURL] = web.input()['longLink']

        print 'New link created at: ' + shortURL
        print 'For: ' + web.input()['longLink']

        return 'http://127.0.0.1:8080/' + shortURL


# This starts the webserver.
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()