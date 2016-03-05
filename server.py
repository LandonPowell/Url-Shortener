import web  # For the web server.
import json # For the database.

database = json.loads(open('database.json').read())

urls = (
    '/([a-z\d]+)', 'redirect',
    '/.*',         'index'
)

class redirect:
    def GET(self, link):
        return web.redirect(database['links'][link])

class index:
    def GET(self):
        return open('index.html').read()

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()