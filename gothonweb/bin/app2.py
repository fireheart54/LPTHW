import web

urls = (
  '/hello', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('/home/bob/Projects/gothonweb/templates', base = "layout")

class Index(object):
    def GET(self):
            return render.template_hello_form()


    def POST(self):
        form = web.input(name='Nobody', greet='Hello')
        greeting = "%s, %s" %(form.greet, form.name)
        return render.template_index(greeting = greeting)



if __name__ == "__main__":
    app.run()