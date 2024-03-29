# -*- coding: utf-8 -*-

@auth.requires_membership('Administrador')
def listar_depositos():
	projeto = db.projeto(request.args(0, cast=int))
	rows = db((db.deposito.projeto == request.args(0, cast=int))).select()
	return locals()

@auth.requires_membership('Administrador')
def inserir_deposito():
	projeto = db.projeto(request.args(0, cast=int))
	db.deposito.projeto.default = projeto.id
	db.deposito.projeto.readable = False
	db.deposito.projeto.writable = False
	merc = db(db.deposito.projeto==projeto.id).select()
	form = SQLFORM(db.deposito).process()
	if form.accepted:
		response.flash = 'Formulario aceito'
		redirect(URL('listar_depositos', args=projeto.id))
	elif form.errors:
		response.flash = 'Formulario não aceito'
	else:
		response.flash = 'Preencha o formulario'
	return locals()


@auth.requires_membership('Administrador')
def alterar_deposito():
	merc = db.deposito(request.args(0, cast=int))
	projeto = db.projeto(merc.projeto)
	db.deposito.id.readable = False
	db.deposito.id.writable = False
	db.deposito.projeto.readable = False
	db.deposito.projeto.writable = False
	form = SQLFORM(db.deposito, request.args(0, cast=int))
	if form.process().accepted:
		session.flash = 'Despesa atualizada'
		redirect(URL('listar_depositos', args=projeto.id))
	elif form.errors:
		response.flash = 'Erros no formulário!'
	else:
		if not response.flash:
			response.flash = 'Preencha o formulário!'
	return locals()
