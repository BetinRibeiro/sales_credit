# -*- coding: utf-8 -*-
# tente algo como

def listar_merc_envio():
    projeto = db.projeto(request.args(0, cast=int))
    rows = db(db.mercadoria.projeto == request.args(0, cast=int)).select()
    return locals()

def listar_merc_retorno():
    projeto = db.projeto(request.args(0, cast=int))
    rows = db(db.mercadoria.projeto == request.args(0, cast=int)).select()
    return locals()

def listar_merc_devolucao():
    projeto = db.projeto(request.args(0, cast=int))
    rows = db(db.mercadoria.projeto == request.args(0, cast=int)).select()
    return locals()
@auth.requires_membership('Administrador')
def inserir_merc_envio():
	proj = db.projeto(request.args(0, cast=int))
	db.mercadoria.projeto.default = proj.id
	db.mercadoria.projeto.writable = False
    
	db.mercadoria.quant_pcs_retorno.readable = False
	db.mercadoria.quant_pcs_retorno.writable = False
    
	db.mercadoria.quant_pcs_aprov_retorno.readable = False
	db.mercadoria.quant_pcs_aprov_retorno.writable = False
    
	db.mercadoria.quant_pcs_devolucao.readable = False
	db.mercadoria.quant_pcs_devolucao.writable = False
    
	db.mercadoria.quant_pcs_aprov_devolucao.readable = False
	db.mercadoria.quant_pcs_aprov_devolucao.writable = False
    
	merc = db(db.mercadoria.projeto==proj.id).select()
	form = SQLFORM(db.mercadoria).process()
	if form.accepted:
		response.flash = 'Formulario aceito'
		redirect(URL('listar_merc_envio', args=proj.id))
	elif form.errors:
		response.flash = 'Formulario não aceito'
	else:
		response.flash = 'Preencha o formulario'
	return locals()

@auth.requires_membership('Administrador')
def alterar_merc_enviada():
	merc = db.mercadoria(request.args(0, cast=int))
	proj = db.projeto(merc.projeto)
	db.mercadoria.id.readable = False
	db.mercadoria.id.writable = False
	db.mercadoria.projeto.readable = False
	db.mercadoria.projeto.writable = False
    
	db.mercadoria.quant_pcs_retorno.readable = False
	db.mercadoria.quant_pcs_retorno.writable = False
    
	db.mercadoria.quant_pcs_aprov_retorno.readable = False
	db.mercadoria.quant_pcs_aprov_retorno.writable = False
    
	db.mercadoria.quant_pcs_devolucao.readable = False
	db.mercadoria.quant_pcs_devolucao.writable = False
    
	db.mercadoria.quant_pcs_aprov_devolucao.readable = False
	db.mercadoria.quant_pcs_aprov_devolucao.writable = False
    
	form = SQLFORM(db.mercadoria, request.args(0, cast=int))
	if form.process().accepted:
		session.flash = 'atualizada'
		redirect(URL('listar_merc_envio', args=proj.id))
	elif form.errors:
		response.flash = 'Erros no formulário!'
	else:
		if not response.flash:
			response.flash = 'Preencha o formulário!'
	return locals()


@auth.requires_membership('Administrador')
def alterar_merc_retorno():
	merc = db.mercadoria(request.args(0, cast=int))
	proj = db.projeto(merc.projeto)
	db.mercadoria.id.readable = False
	db.mercadoria.id.writable = False
	db.mercadoria.projeto.readable = False
	db.mercadoria.projeto.writable = False
    
	db.mercadoria.quant_pcs_enviada.readable = True
	db.mercadoria.quant_pcs_enviada.writable = False 
    
	db.mercadoria.descricao.readable = True
	db.mercadoria.descricao.writable = False
    
	db.mercadoria.preco_unitario.readable = False
	db.mercadoria.preco_unitario.writable = False
    
	db.mercadoria.custo_unitario.readable = False
	db.mercadoria.custo_unitario.writable = False
    
	db.mercadoria.quant_pcs_devolucao.readable = False
	db.mercadoria.quant_pcs_devolucao.writable = False
    
	db.mercadoria.quant_pcs_aprov_devolucao.readable = False
	db.mercadoria.quant_pcs_aprov_devolucao.writable = False
    
	form = SQLFORM(db.mercadoria, request.args(0, cast=int))
	if form.process().accepted:
		session.flash = 'atualizada'
		redirect(URL('listar_merc_retorno', args=proj.id))
	elif form.errors:
		response.flash = 'Erros no formulário!'
	else:
		if not response.flash:
			response.flash = 'Preencha o formulário!'
	return locals()



@auth.requires_membership('Administrador')
def alterar_merc_devolucao():
	merc = db.mercadoria(request.args(0, cast=int))
	proj = db.projeto(merc.projeto)
	db.mercadoria.id.readable = False
	db.mercadoria.id.writable = False
	db.mercadoria.projeto.readable = False
	db.mercadoria.projeto.writable = False
    
	db.mercadoria.quant_pcs_enviada.readable = True
	db.mercadoria.quant_pcs_enviada.writable = False 
    
	db.mercadoria.descricao.readable = True
	db.mercadoria.descricao.writable = False
    
	db.mercadoria.preco_unitario.readable = False
	db.mercadoria.preco_unitario.writable = False
    
	db.mercadoria.custo_unitario.readable = False
	db.mercadoria.custo_unitario.writable = False
    
	db.mercadoria.quant_pcs_retorno.readable = False
	db.mercadoria.quant_pcs_retorno.writable = False
    
	db.mercadoria.quant_pcs_aprov_retorno.readable = False
	db.mercadoria.quant_pcs_aprov_retorno.writable = False
    
	form = SQLFORM(db.mercadoria, request.args(0, cast=int))
	if form.process().accepted:
		session.flash = 'atualizada'
		redirect(URL('listar_merc_devolucao', args=proj.id))
	elif form.errors:
		response.flash = 'Erros no formulário!'
	else:
		if not response.flash:
			response.flash = 'Preencha o formulário!'
	return locals()
