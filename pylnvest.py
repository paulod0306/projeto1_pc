import math 
import random 
import datetime 
import statistics 
import locale 

locale.setlocale(locale.LC_ALL, 'PT_BR.UFT-8')
#ENTRADAS
capital = float(input('capital inicial: '))
aporte = float(input('aporte mensal: '))
meses  = float(input('prazo (meses):'))
cdi_anual = float(input('CDI anual %: '))/100
perc_cdb = float (input('percentualdo CDI - CDB (%): '))/100
perc_lci = float(input('percentual do CDI - LCI (%): '))/100
taxa_fii = float(input('rentabilidade do fii (%): '))/100 
meta     = float(input('meta financeira (r$): '))

#conversao CDI
cdi_mensal = math.pow((1+cdi_anual), 1/12) -1 
#total investido 
total_investido = capital + (aporte * meses) 

#CDB
taxa_cdb= cdi_mensal * perc_cdb 
montante_cdb = (capital * math.pow((1+taxa_cdb),meses))+(aporte a8 meses)
lucro_cdb = montante_cdb - total_investido 
montante_cdb_liquido = total_investido + (lucro_cdb * 0.85)

#LCI/LCI
taxa_lci = cdi_mensal * perc_lci
montante_lci = (capital * math.pow((1+taxa_lci),meses))+(aporte * meses)

#poupança 
taxa__poupanca = 0.005
montagem_poupanca = (capital * math.pow((1+taxa_poupanca),meses))+(aporte*meses)


