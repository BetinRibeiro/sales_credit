# -*- coding: utf-8 -*-
# tente algo como
def prestacao_venda():
    projeto = db.projeto(request.args(0, cast=int))
    return locals()
def prestacao_cobr():
    projeto = db.projeto(request.args(0, cast=int))
    return locals()

@auth.requires_membership('Administrador')
def lucros_prej():
    projeto = db.projeto(request.args(0, cast=int))
    return locals()

@auth.requires_membership('Administrador')
def investimento():
    projeto = db.projeto(request.args(0, cast=int))
    return locals()
@cache.action()
def acesso_geral_projeto():
    projeto = db.projeto(request.args(0, cast=int))
    return locals()

@auth.requires_membership('Administrador')
def alterar_projeto():
    projeto = db.projeto(request.args(0, cast=int))

    db.projeto.id.readable = False
    db.projeto.id.writable = False


    db.projeto.adiantamento_dinh_cobranca.readable = False
    db.projeto.adiantamento_dinh_cobranca.writable = False

    db.projeto.comissao_cobrador.readable = False
    db.projeto.comissao_cobrador.writable = False

    db.projeto.data_chegada_cobrador.readable = False
    db.projeto.data_chegada_cobrador.writable = False

    db.projeto.data_chegada_venda.readable = False
    db.projeto.data_chegada_venda.writable = False

    db.projeto.data_saida_cobrador.readable = False
    db.projeto.data_saida_cobrador.writable = False

    db.projeto.devolucao_dinh_cobranca.readable = False
    db.projeto.devolucao_dinh_cobranca.writable = False

    db.projeto.devolucao_dinh_venda.readable = False
    db.projeto.devolucao_dinh_venda.writable = False

    db.projeto.nome_cobrador.readable = False
    db.projeto.nome_cobrador.writable = False

    db.projeto.ultima_cidade.readable = False
    db.projeto.ultima_cidade.writable = False

    db.projeto.ultima_data_cobranca.readable = False
    db.projeto.ultima_data_cobranca.writable = False

    db.projeto.vale_cobrador.readable = False
    db.projeto.vale_cobrador.writable = False


    form = SQLFORM(db.projeto, request.args(0, cast=int))
    if form.process().accepted:
        session.flash = 'Filme atualizado'
        redirect(URL('listar_projetos'))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário!'
    return locals()

@auth.requires_login()
def listar_projetos():
    a = auth.user
    rows = db(db.projeto.created_by == auth.user).select()
    return locals()

@auth.requires_membership('Administrador')
def criar_projeto():
    conteudo = db.projeto(request.args(0, auth.user))

    db.projeto.adiantamento_dinh_cobranca.readable = False
    db.projeto.adiantamento_dinh_cobranca.writable = False

    db.projeto.comissao_cobrador.readable = False
    db.projeto.comissao_cobrador.writable = False

    db.projeto.data_chegada_cobrador.readable = False
    db.projeto.data_chegada_cobrador.writable = False

    db.projeto.data_chegada_venda.readable = False
    db.projeto.data_chegada_venda.writable = False

    db.projeto.data_saida_cobrador.readable = False
    db.projeto.data_saida_cobrador.writable = False

    db.projeto.devolucao_dinh_cobranca.readable = False
    db.projeto.devolucao_dinh_cobranca.writable = False

    db.projeto.devolucao_dinh_venda.readable = False
    db.projeto.devolucao_dinh_venda.writable = False

    db.projeto.nome_cobrador.readable = False
    db.projeto.nome_cobrador.writable = False

    db.projeto.ultima_cidade.readable = False
    db.projeto.ultima_cidade.writable = False

    db.projeto.ultima_data_cobranca.readable = False
    db.projeto.ultima_data_cobranca.writable = False

    db.projeto.vale_cobrador.readable = False
    db.projeto.vale_cobrador.writable = False
    form = SQLFORM(db.projeto).process()
    if form.accepted:
        response.flash = 'Formulario aceito'
        redirect(URL('listar_projetos'))
    elif form.errors:
        response.flash = 'Formulario não aceito'
    else:
        response.flash = 'Preencha o formulario'
    return locals()

@auth.requires_membership('Administrador')
def alterar_dados_chegada_venda():
    projeto = db.projeto(request.args(0, cast=int))

    db.projeto.id.readable = False
    db.projeto.id.writable = False


    db.projeto.adiantamento_dinh_cobranca.readable = False
    db.projeto.adiantamento_dinh_cobranca.writable = False

    db.projeto.comissao_cobrador.readable = False
    db.projeto.comissao_cobrador.writable = False

    db.projeto.data_chegada_cobrador.readable = False
    db.projeto.data_chegada_cobrador.writable = False

    db.projeto.data_saida_cobrador.readable = False
    db.projeto.data_saida_cobrador.writable = False

    db.projeto.devolucao_dinh_cobranca.readable = False
    db.projeto.devolucao_dinh_cobranca.writable = False

    db.projeto.nome_cobrador.readable = False
    db.projeto.nome_cobrador.writable = False

    db.projeto.vale_cobrador.readable = False
    db.projeto.vale_cobrador.writable = False

    db.projeto.recebido_chegada_venda.readable = True
    db.projeto.recebido_chegada_venda.writable = True

    form = SQLFORM(db.projeto, request.args(0, cast=int))
    if form.process().accepted:
        session.flash = 'Filme atualizado'
        redirect(URL('prestacao_venda', args=projeto.id))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário!'
    return locals()


@auth.requires_membership('Administrador')
def alterar_dados_cobranca():
    projeto = db.projeto(request.args(0, cast=int))

    db.projeto.id.readable = False
    db.projeto.id.writable = False


    db.projeto.nome.readable = False
    db.projeto.nome.writable = False

    db.projeto.nome_chefe.readable = False
    db.projeto.nome_chefe.writable = False

    db.projeto.primeira_cidade.readable = False
    db.projeto.primeira_cidade.writable = False

    db.projeto.vale_saida_chefe.readable = False
    db.projeto.vale_saida_chefe.writable = False

    db.projeto.adiantamento_dinh_venda.readable = False
    db.projeto.adiantamento_dinh_venda.writable = False

    db.projeto.comissao_chefe_venda.readable = False
    db.projeto.comissao_chefe_venda.writable = False

    db.projeto.data_saida_venda.readable = False
    db.projeto.data_saida_venda.writable = False
    
    db.projeto.devolucao_dinh_venda.readable = False
    db.projeto.devolucao_dinh_venda.writable = False

    db.projeto.data_chegada_venda.readable = False
    db.projeto.data_chegada_venda.writable = False

    db.projeto.recebido_chegada_venda.readable = False
    db.projeto.recebido_chegada_venda.writable = False

    db.projeto.comissao_chefe_cobranca.readable = False
    db.projeto.comissao_chefe_cobranca.writable = False

    db.projeto.adiantamento_dinh_venda.readable = False
    db.projeto.adiantamento_dinh_venda.writable = False

    db.projeto.comissao_chefe_venda.readable = False
    db.projeto.comissao_chefe_venda.writable = False

    db.projeto.data_saida_venda.readable = False
    db.projeto.data_saida_venda.writable = False

    db.projeto.comissao_chefe_cobranca.readable = False
    db.projeto.comissao_chefe_cobranca.writable = False
    
    db.projeto.recebido_chegada_cobrac.readable = True
    db.projeto.recebido_chegada_cobrac.writable = True


    form = SQLFORM(db.projeto, request.args(0, cast=int))
    if form.process().accepted:
        session.flash = 'Filme atualizado'
        redirect(URL('prestacao_cobr', args=projeto.id))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário!'
    return locals()
