select PESSOA.n_identidade,PESSOA.nome,PESSOA.fone,VIAGEM.data_viagem,PESSOA_VIAGEM.hora,PESSOA_VIAGEM.turno,PESSOA_VIAGEM.parada,PESSOA_VIAGEM.destino 
from PESSOA,VIAGEM,PESSOA_VIAGEM
where PESSOA.n_identidade = PESSOA_VIAGEM.n_identidade
and VIAGEM.cod_viagem = PESSOA_VIAGEM.cod_viagem
and VIAGEM.data_viagem = '2022-11-11' and pessoa_viagem.turno = 'Manhã'
