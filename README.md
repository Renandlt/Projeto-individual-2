# Projeto-individual-2
Projeto individual do segundo módulo do curso formação de análise de dados
# Avaliação de Candidatos

Este é um script Python simples para avaliar candidatos com base em critérios específicos. O script recebe uma lista de candidatos e notas mínimas para as etapas de avaliação, e então identifica os candidatos que atendem aos critérios especificados.

## Como Funciona

O script utiliza uma função chamada `avaliar_candidatos` que aceita a lista de candidatos e as notas mínimas para as etapas de avaliação (entrevista, teste teórico, teste prático e avaliação de soft skills) como argumentos.

A função percorre a lista de candidatos e verifica se cada candidato atende aos critérios definidos pelo usuário. Ela compara as notas de cada candidato com as notas mínimas especificadas. Se um candidato atender a todos os critérios, ele é adicionado a uma lista de candidatos que atendem aos critérios.

## Uso

Para utilizar o script, siga estas etapas:

1. Execute o script Python em um ambiente compatível (por exemplo, um IDE Python ou um terminal).

2. O script solicitará as notas mínimas em entrevista (e), teste teórico (t), teste prático (p) e soft skills (s).

3. Após inserir as notas mínimas, o script avaliará os candidatos com base nos critérios especificados.

4. Os candidatos que atendem aos critérios serão listados no console, indicando seus números de candidato.

## Exemplo

Suponha que a lista de candidatos seja a seguinte:

```
candidatos = [
    "e4_t4_p8_s8",
    "e3_t5_p7_s7",
    "e5_t3_p6_s8",
    "e4_t4_p8_s7",
    "e4_t4_p8_s9",
]
```

Se você definir as notas mínimas como e=4, t=4, p=8 e s=8, o script identificará os candidatos que atendem a esses critérios e os listará.

## Observações

Este script foi projetado para ser simples e fácil de entender. Você pode personalizá-lo para atender às suas necessidades específicas, como fornecer uma lista diferente de candidatos ou adicionar mais critérios de avaliação. Ele serve como uma base para a automação da avaliação de candidatos com base em critérios específicos.
