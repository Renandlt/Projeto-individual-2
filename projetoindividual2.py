def avaliar_candidatos(candidatos, nota_e, nota_t, nota_p, nota_s):
    candidatos_atendem_critérios = []

    for i, candidato in enumerate(candidatos):
        notas = candidato.split("_")
        nota_e_candidato = int(notas[0][1:])
        nota_t_candidato = int(notas[1][1:])
        nota_p_candidato = int(notas[2][1:])
        nota_s_candidato = int(notas[3][1:])

        if (
            nota_e_candidato >= nota_e
            and nota_t_candidato >= nota_t
            and nota_p_candidato >= nota_p
            and nota_s_candidato >= nota_s
        ):
            candidatos_atendem_critérios.append(i + 1)  # Adiciona o candidato à lista (1-based index)

    return candidatos_atendem_critérios

# Lista de candidatos com resultados no formato "eX_tX_pX_sX"
candidatos = [
    "e4_t4_p8_s8",
    "e3_t5_p7_s7",
    "e5_t3_p6_s8",
    "e4_t4_p8_s7",
    "e4_t4_p8_s9",
]

# Solicita ao usuário as notas mínimas
nota_e = int(input("Digite a nota mínima em entrevista (e): "))
nota_t = int(input("Digite a nota mínima em teste teórico (t): "))
nota_p = int(input("Digite a nota mínima em teste prático (p): "))
nota_s = int(input("Digite a nota mínima em soft skills (s): "))

# Chama a função para avaliar candidatos
candidatos_encontrados = avaliar_candidatos(candidatos, nota_e, nota_t, nota_p, nota_s)

if candidatos_encontrados:
    print("Candidatos que atendem aos critérios:")
    for candidato_num in candidatos_encontrados:
        print(f"Candidato {candidato_num}")
else:
    print("Nenhum candidato atende aos critérios especificados.")
