class Table():
	name_alias = ""
	name_db	= ""
	rows = {}
	type = ""

	def __init__(self, name_db, rows, name_alias="", type="TABLE"):
		if(name_alias == "")
			name_alias = name_db
		