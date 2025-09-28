from folha_pagamento import FolhaPagamento
from contrato_clt import ContratoCLT
from estagio import Estagio
from contrato_pj import ContratoPJ

folha = FolhaPagamento()

clt = ContratoCLT("Nome 1",5000)
estagiario = Estagio("Nome 2",2000)
pj = ContratoPJ("Nome 3",7000)

print("CLT:", folha.calcular_salario(clt))
print("Estágio:", folha.calcular_salario(estagiario))
print("PJ:", folha.calcular_salario(pj))