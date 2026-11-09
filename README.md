
# Portulano · dados

Base aberta e colaborativa de dados econômicos e industriais do Brasil. O primeiro conjunto reúne investimentos industriais anunciados no país e a situação de cada um, sempre com a fonte que sustenta a informação.

## O que há neste repositório

```
data/
  investimentos.csv     investimentos industriais, um por linha
LICENSE                 licença dos dados (CC BY 4.0)
LICENSE-CODE            licença dos scripts (MIT)
```

## Esquema do arquivo investimentos.csv

| Coluna | Descrição |
|---|---|
| empresa | Nome da empresa responsável pelo investimento |
| setor | automotivo-ve, mineracao, agro, energia ou logistica |
| uf | Sigla do estado |
| municipio | Município onde o investimento ocorre |
| valor_brl | Valor em reais, sem pontuação (ex. 5000000000) |
| estagio | anunciado, aprovado, em_obras ou concluido |
| fonte_url | Link do documento que sustenta a informação |
| data_publicacao | Data da fonte, no formato AAAA-MM-DD |
| data_verificacao | Data em que alguém conferiu a fonte, no mesmo formato |
| confianca | alta, media ou baixa |

Os quatro estágios existem para separar promessa de realização. Um investimento fica como **anunciado** quando só há uma declaração pública, como uma notícia ou um comunicado. Passa a **aprovado** quando existe uma decisão formal, como licença, contrato ou aprovação de financiamento. Vira **em_obras** quando há evidência de construção ou instalação em andamento, e **concluido** quando a unidade já opera.

## Origem dos dados

Os dados vêm de fontes públicas, como o Comex Stat (MDIC), o IBGE, a ANTAQ, comunicados de empresas e portais de governos estaduais. Cada linha indica a sua fonte no campo `fonte_url`. Os termos de uso de cada base original continuam valendo, e a licença deste repositório cobre o trabalho que o projeto acrescenta, como a curadoria, a classificação e a organização.

## Como contribuir

1. Escolha uma tarefa no canal #tarefas-abertas do Discord [link] ou em uma issue deste repositório.
2. Faça um fork e edite o arquivo CSV, respeitando o esquema acima.
3. Abra um pull request e preencha o modelo, listando as fontes consultadas.
4. Uma verificação automática confere o esquema, e uma segunda pessoa revisa a fonte antes da aprovação.

## Regras dos dados

- Toda linha precisa de uma fonte com link e data, e o que chegar sem fonte será recusado.
- O projeto trabalha com empresas, setores, locais e indicadores públicos, então dados de pessoas físicas ficam de fora.
- O estágio deve seguir o que o documento da fonte comprova. Na dúvida entre dois estágios, use o mais baixo.
- Quando duas fontes divergirem, registre a mais confiável e explique a divergência na descrição do pull request.

## Licenças

Os dados são licenciados sob a Creative Commons Atribuição 4.0 Internacional (arquivo `LICENSE`). Os scripts são licenciados sob MIT (arquivo `LICENSE-CODE`).

Ao usar os dados, cite como "Dados: Portulano, licenciados sob CC BY 4.0" e inclua o link para este repositório.

## Aviso

Os dados podem conter erros e ficar desatualizados. Eles são fornecidos sem garantia, e quem for tomar uma decisão com base neles deve conferir a fonte original.

## Comunidade

Dúvidas e ideias são bem-vindas no [Discord](https://discord.gg/6gF3ytc5mV) ou nas issues deste repositório.
