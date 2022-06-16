from openerp import fields,models

class Mahasiswa(models.Model):
	_name = "ridhabouazizi.ridhabouazizi"

	name = fields.Char(size=32,string="name")
	lastname = fields.Char(size=32,string="lastname")
	address = fields.Char(size=32,string="address")