import webapp2
from alg import Algorithm

class MainPage(webapp2.RequestHandler):

    def get(self):

        input = [9,8,7,6,5,4,3,2,1]               

        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('<center><h1>Welcome to Webapp2!</h1></center>')
        self.response.write("<h3>Input: </h3>")
        self.response.write(input)
        output = Algorithm(input)
        self.response.write("<h3>Output: </h3>")
        self.response.write(output.get())

app = webapp2.WSGIApplication([

    ('/', MainPage),

], debug=True)


