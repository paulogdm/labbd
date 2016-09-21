import cx_Oracle

SERVER_URL = "grad.icmc.usp.br"
SERVER_PORT = "15215"
SERVER_SID = "orcl"

class DBApi(object):
	"""docstring for DBApi"""
	
	def __init__(self, username, password):
		self.connect(username, password)

	def connect(self, username, password):

			try:
				dsnStr = cx_Oracle.makedsn(SERVER_URL, SERVER_PORT, SERVER_SID)
				self.db = cx_Oracle.connect(username, password, dsnStr)	

			except cx_Oracle.DatabaseError as e:
				error, = e.args
				
				if error.code == 1017:
					print('[ERROR] Please check your credentials.')
				
				else:
					print('[ERROR] Database connection error: %s' % e)

				raise

			self.cursor = self.db.cursor()

	def disconnect(self):
			
		try:
			self.cursor.close()
			self.db.close()
			
		except cx_Oracle.DatabaseError:
			pass
	
	# http://stackoverflow.com/questions/7465889/cx-oracle-and-exception-handling-good-practices
	def execute(self, sql, bindvars=None, commit=False):
		try:
			self.cursor.execute(sql, bindvars)

		except cx_Oracle.DatabaseError as e:
			error, = e.args
			
			if error.code == 955:
				print('Table already exists')

			elif error.code == 1031:
				print("Insufficient privileges")

			print(error.code)
			print(error.message)
			print(error.context)

			# Raise the exception.
			raise

		# Only commit if it-s necessary.
		if commit:
			self.db.commit()
