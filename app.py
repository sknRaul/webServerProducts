import web
import model

urls = (
    '/index', 'Index',
    '/see/(\d+)', 'See',
    '/edit/(\d+)', 'Edit',
    '/add', 'Add',
    '/delete/(\d+)', 'Delete'
)

#web.config.debug = False

render = web.template.render('views',cache=None, base='base')

class Index:
    def GET(self):
    	products = model.get_products()
        return render.index(products)

class See:
	def GET(self, id_product):
		data = model.get_product(int(id_product))
		return render.see(data)

class Edit:
	def GET(self, id_product):
		data = model.get_product(int(id_product))
		return render.edit(data)
	
	def POST(self, id_product):
		form = web.input()
		model.update_product(form.id, form.product, form.description, form.stock, form.cost_price, form.sale_price)
		raise web.seeother('/index')

class Add:
	def GET(self):
		return render.add()
	def POST(self):
		form = web.input()
		model.add_product(form.product, form.description, form.stock, form.cost_price, form.sale_price)
		raise web.seeother('/index')

class Delete:
	def GET(self, id_product):
		data = model.get_product(int(id_product))
		return render.delete(data)
	
	def POST(self, id_product):
		form = web.input()
		model.delete_product(form.id)
		raise web.seeother('/index')


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()