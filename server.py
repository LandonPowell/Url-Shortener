import web

urls = (
    '/([a-z\d]+)', 'redirect',
    '/.*', 'static'
)

class redirect:
    def GET(self, link):
        return web.redirect(database[link])

class static:
    def GET(self):
        return 'meme'

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()