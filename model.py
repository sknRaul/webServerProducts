import web

db_host = 'y0nkiij6humroewt.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'#host
db_user = 'whhb7hzets64lglk'#usuario
db_passworld = 'u9to7skhda094huz'#contrasena
db_name = 'gpw5td5hlz65mrqa'#nombre de la base de datos

#db_host = 'localhost'#host
#db_name = 'products'#nombre de la base de datos
#db_user = 'root'#usuario
#db_passworld = '1234'#contrasena


db = web.database(#Metodo de conexion
		dbn = 'mysql',#Tipo de servidor
		host = db_host,
		db = db_name,
		user = db_user,
		pw = db_passworld
	)

def get_products():
	try:
		return db.select('products')#Consulta
	except Exception, e:
		return e

def get_product(id):
	try:
		return db.select('products', where='id_product=$id', vars=locals())[0]
	except Exception, e:
		return e

def update_product(id, product, description, stok, cost_price, sale_price):
	    db.update('products',
	    	where="id_product=$id", 
	    	vars=locals(), 
	    	product=product, 
	    	description=description, 
	    	stok=stok, 
	    	cost_price=cost_price, 
	    	sale_price=sale_price)

def add_product(product, description, stock, cost_price, sale_price, image):
    db.insert('products',
    	product=product, 
    	description=description, 
    	stok=stock,
    	cost_price=cost_price,
    	sale_price=sale_price,
    	image_product=image)

def delete_product(id):
	db.delete('products', where='id_product=$id', vars=locals())