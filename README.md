# Url-Shortener
Simple URL-Shortening website written in Python2!

It's completely finished and working code as of March 6, 2016. 
Licensed under CC0, which means it's just as much yours as 
it is mine. Do what thou wilt!

I'd like it if you gave me a shout out if you use it, but that's
your choice. 

### To Run Server - 
Move into your Url-Shortener directory, and modify server.py's 
46th line, which looks something like - 
```
        # Gives the user their link.
        return 'http://127.0.0.1:8080/' + shortURL
```
Change the localhost IP and port to either your server's IP or your domain,
so that it looks like - 
```
        # Gives the user their link.
        return 'http://mini.me/' + shortURL
```
You might also find it useful to change index.html's <h1> so that it says 
your website's catchy name. 

Next, simply run the server.py through python2 from the command line. 
```
python2 server.py
```
To run on port 80, you might need to use sudo: `sudo python2 server.py 80`

Now you're running a URL-Shortener!
