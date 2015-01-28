#!/usr/bin/python

import web
import requests

n = 0

urls = ("/.*", "river")

app = web.application(urls,globals())

class river:
    def GET(self):
        #r =requests.get("http://waterservices.usgs.gov/nwis/iv?sites=12155500&period=P1D&modifiedSince=PT30M&format=rdb")
        r =requests.get("http://waterservices.usgs.gov/nwis/iv?sites=12155500&period=P1D&format=rdb")
        print r.status_code
        return r.text

        

if __name__ == "__main__":
    app.run()
