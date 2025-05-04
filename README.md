# Sistema Especialista para Diagnóstico da Centralização do Bitcoin

Este projeto implementa um sistema especialista baseado em regras fuzzy para avaliar o nível de centralização da mineração de Bitcoin. Ele considera variáveis técnicas, econômicas e ambientais com o objetivo de sugerir um diagnóstico sobre a descentralização da rede.

## Objetivo

Desenvolver uma aplicação capaz de analisar variáveis relacionadas à mineração de Bitcoin (como custo da infraestrutura, ROI, temperatura, ruído, entre outros) e fornecer um diagnóstico automatizado sobre o risco de centralização do poder computacional da rede.

## Variáveis Consideradas

- **Crisp (nítidas):**
  - Porcentagem de centralização do hashrate nas 3 maiores pools
  - ROI (Retorno sobre investimento)
  - Ruído
  - Temperatura

- **Fuzzy:**
  - Acessibilidade ao conhecimento
  - Custo da aquisição de mineradoras
  - Custo do espaço
  - Refrigeração
  - Custo da usina de energia

- **Compostas:**
  - Custo da infraestrutura: composta por espaço, refrigeração e usina
  - Nível de ruído e temperatura: composta por ruído e temperatura

## Como executar

Certifique-se de ter Python 3 instalado.

1. Clone este repositório:
   ```bash
   git clone https://github.com/ticomelato/bitcoin
   cd bitcoin
   ```

2. Execute o sistema:
   ```bash
   python sistema_especialista.py
   ```

3. Insira os dados solicitados pelo terminal para obter o diagnóstico.

## Exemplo de Uso

```text
Porcentagem de centralização do hashrate (%): 65
Acessibilidade ao conhecimento (1-10): 3
ROI (em %): 12
Custo do espaço (1-10): 7
Refrigeração (1-10): 8
Custo da usina (1-10): 9
Custo de aquisição de mineradoras (1-10): 6
Ruído (dB): 85
Temperatura (°C): 40

Diagnóstico: Alta centralização detectada devido ao custo elevado e baixa acessibilidade.
```

## Autores

- Thiago Melato
- Bernardo Vannier

## Referências

- MELATO, Thiago; VANNIER, Bernardo. *bitcoin*. GitHub. Disponível em: https://github.com/ticomelato/bitcoin. Acesso em: 4 maio 2025.
- MININGPOOLSTATS. *Bitcoin Mining Pools*. Disponível em: https://miningpoolstats.stream/bitcoin. Acesso em: 4 maio 2025.
