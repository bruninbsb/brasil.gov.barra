# -*- coding: utf-8 -*-
""" Modulo que implementa uma browser view de suporte a Barra de Identidade"""
from Acquisition import aq_inner
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

from zope.interface import implements

from brasil.gov.barra.interfaces import IBarraHelper


class BarraHelper(BrowserView):
    ''' Browser view que retorna as configuracoes da Barra de Identidade
    '''
    implements(IBarraHelper)

    def __init__(self, context, request, *args, **kwargs):
        ''' Inicializacao da browser view

            :param context: [requerido] Contexto que esta view e utilizada.
            :type context: objeto context
            :param request: [requerido] Request para o qual obteremos a view
            :type request: objeto request.
            :returns: Nothing
            :rtype: None
        '''
        super(BarraHelper, self).__init__(context, request, *args, **kwargs)
        context = aq_inner(context)
        self.context = context
        # Obtem a tool portal_properties
        pp = getToolByName(context, 'portal_properties')
        # Armazena a property sheet brasil_gov no atributo sheet desta classe
        # Caso a sheet nao exista, retornamos None
        self.sheet = getattr(pp, 'brasil_gov', None)

    def cor(self):
        ''' Retorna a configuracao de cor da barra de identidade

            :returns: Cor da barra de identidade
            :rtype: string
        '''
        # Retorna a cor da barra, como armazenada na property sheet
        # ou o valor padrao verde
        cor = 'verde'
        if self.sheet:
            cor = self.sheet.getProperty('cor', cor)
        return cor

    def local(self):
        ''' Retorna a configuracao de cor da view

            :returns: Cor da barra de identidade
            :rtype: string
        '''
        # Retorna se a barra sera montada localmente,
        # como armazenada na property sheet ou o valor padrao True
        local = True
        if self.sheet:
            local = self.sheet.getProperty('local', local)
        return local
