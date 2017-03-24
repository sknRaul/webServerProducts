import web
import model

urls = (
    '/', 'Index',
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
		raise web.seeother('/')

class Add:
	def GET(self):
		return render.add()
	def POST(self):
		form = web.input()
		imagen = web.input(image_product={})
		filedir = 'static/images'#indica la ruta en la que se va a guardar
		#Las siguientes dos lineas se evitan si se crea un nombre para el archivo
		filepath = imagen.image_product.filename.replace('\\','/')#Elimina la ruta absoluta
		filename = filepath.split('/')[-1]
		#Copiar el archivo al servidor
		fileserver = open(filedir + '/' + filename, 'w')
		fileserver.write(imagen.image_product.file.read())
		fileserver.close()

		image_product = filename
		model.add_product(form['product'],
			form['description'],
			form['stock'],
			form['cost_price'],
			form['sale_price'],
			image_product
			)
		raise web.seeother('/')

class Delete:
	def GET(self, id_product):
		data = model.get_product(int(id_product))
		return render.delete(data)
	
	def POST(self, id_product):
		form = web.input()
		model.delete_product(form.id)
		raise web.seeother('/')


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()