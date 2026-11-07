import csv
import sys
from datetime import date
from urllib.parse import urlparse

COLUNAS = [
    "empresa", "setor", "uf", "municipio", "valor_brl", "estagio",
    "fonte_url", "data_publicacao", "data_verificacao", "confianca",
]
SETORES = {"automotivo-ve", "mineracao", "agro", "energia", "logistica"}
ESTAGIOS = {"anunciado", "aprovado", "em_obras", "concluido"}
CONFIANCAS = {"alta", "media", "baixa"}
UFS = {
    "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS",
    "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC",
    "SP", "SE", "TO",
}


def ler_data(texto):
    try:
        return date.fromisoformat(texto)
    except ValueError:
        return None


def validar(caminho):
    erros = []
    total = 0
    hoje = date.today()
    with open(caminho, newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        cabecalho = next(leitor, None)
        if cabecalho != COLUNAS:
            return ["Cabeçalho diferente do esquema. Esperado: " + ",".join(COLUNAS)], 0
        vistos = set()
        for numero, linha in enumerate(leitor, start=2):
            if not any(celula.strip() for celula in linha):
                continue
            total += 1
            if len(linha) != len(COLUNAS):
                erros.append(f"Linha {numero}: esperava {len(COLUNAS)} colunas e encontrou {len(linha)}")
                continue
            r = dict(zip(COLUNAS, (celula.strip() for celula in linha)))

            for coluna, valor in r.items():
                if not valor:
                    erros.append(f"Linha {numero}: a coluna {coluna} está vazia")

            if r["setor"] and r["setor"] not in SETORES:
                erros.append(f"Linha {numero}: setor inválido ({r['setor']})")
            if r["uf"] and r["uf"] not in UFS:
                erros.append(f"Linha {numero}: UF inválida ({r['uf']})")
            if r["estagio"] and r["estagio"] not in ESTAGIOS:
                erros.append(f"Linha {numero}: estágio inválido ({r['estagio']})")
            if r["confianca"] and r["confianca"] not in CONFIANCAS:
                erros.append(f"Linha {numero}: confiança inválida ({r['confianca']})")
            if r["valor_brl"] and not (r["valor_brl"].isdigit() and int(r["valor_brl"]) > 0):
                erros.append(f"Linha {numero}: valor_brl deve ser um número inteiro positivo, sem pontuação")

            if r["fonte_url"]:
                url = urlparse(r["fonte_url"])
                if url.scheme not in ("http", "https") or not url.netloc:
                    erros.append(f"Linha {numero}: fonte_url não é um link válido")

            publicacao = ler_data(r["data_publicacao"]) if r["data_publicacao"] else None
            verificacao = ler_data(r["data_verificacao"]) if r["data_verificacao"] else None
            if r["data_publicacao"] and publicacao is None:
                erros.append(f"Linha {numero}: data_publicacao deve seguir o formato AAAA-MM-DD")
            if r["data_verificacao"] and verificacao is None:
                erros.append(f"Linha {numero}: data_verificacao deve seguir o formato AAAA-MM-DD")
            if publicacao and publicacao > hoje:
                erros.append(f"Linha {numero}: data_publicacao está no futuro")
            if verificacao and verificacao > hoje:
                erros.append(f"Linha {numero}: data_verificacao está no futuro")
            if publicacao and verificacao and verificacao < publicacao:
                erros.append(f"Linha {numero}: data_verificacao é anterior à data_publicacao")

            chave = (r["empresa"].lower(), r["uf"], r["municipio"].lower(), r["fonte_url"])
            if chave in vistos:
                erros.append(f"Linha {numero}: linha duplicada (mesma empresa, local e fonte)")
            vistos.add(chave)
    return erros, total


if __name__ == "__main__":
    caminho = sys.argv[1] if len(sys.argv) > 1 else "data/investimentos.csv"
    erros, total = validar(caminho)
    if erros:
        print(f"{len(erros)} problema(s) encontrado(s) em {caminho}")
        for erro in erros:
            print(" -", erro)
        sys.exit(1)
    print(f"OK, {total} linha(s) validada(s) em {caminho}")
