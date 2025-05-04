# Fuzzificação das variáveis fuzzy

def fuzzificar_acessibilidade(conhecimento):
    if conhecimento < 3:
        return "baixa"
    elif 3 <= conhecimento <= 7:
        return "média"
    else:
        return "alta"

def fuzzificar_custo_equipamento(custo):
    if custo < 5000:
        return "baixo"
    elif 5000 <= custo <= 15000:
        return "moderado"
    else:
        return "alto"

def fuzzificar_custo_espaco(valor_m2):
    if valor_m2 < 20:
        return "baixo"
    elif 20 <= valor_m2 <= 50:
        return "moderado"
    else:
        return "alto"

def fuzzificar_refrigeracao(demanda):
    if demanda < 2:
        return "simples"
    elif 2 <= demanda <= 4:
        return "moderada"
    else:
        return "exigente"

def fuzzificar_custo_usina(custo_kw):
    if custo_kw < 0.4:
        return "baixo"
    elif 0.4 <= custo_kw <= 0.8:
        return "moderado"
    else:
        return "alto"

# Variável composta: Custo da infraestrutura
def avaliar_infraestrutura(custo_espaco, refrigeracao, custo_usina):
    valores = [custo_espaco, refrigeracao, custo_usina]
    if valores.count("alto") >= 2:
        return "alto"
    elif "alto" in valores or "moderado" in valores:
        return "moderado"
    else:
        return "baixo"

# Variável composta: Ruído e Temperatura
def avaliar_ruido_temperatura(ruido, temperatura):
    if ruido > 55 or temperatura > 80:
        return "inviável"
    else:
        return "aceitável"

# Diagnóstico final com base na árvore de decisão
def diagnosticar(hashrate_pct, roi, conhecimento, custo_equip, custo_espaco,
                 refrigeracao, custo_usina, ruido, temperatura):

    acessibilidade = fuzzificar_acessibilidade(conhecimento)
    custo_mineradora = fuzzificar_custo_equipamento(custo_equip)
    espaco = fuzzificar_custo_espaco(custo_espaco)
    refrig = fuzzificar_refrigeracao(refrigeracao)
    usina = fuzzificar_custo_usina(custo_usina)

    infra = avaliar_infraestrutura(espaco, refrig, usina)
    ambiente = avaliar_ruido_temperatura(ruido, temperatura)

    # Lógica da árvore de decisão
    if hashrate_pct > 60:
        if roi > 2:
            return "Alto grau de centralização"
        elif acessibilidade == "baixa" or custo_mineradora == "alto":
            return "Tendência à centralização"
        else:
            return "Cenário parcialmente centralizado"
    else:
        if infra == "alto" or ambiente == "inviável":
            return "Tendência à centralização"
        elif acessibilidade == "alta" and custo_mineradora == "baixo":
            return "Cenário descentralizado"
        else:
            return "Diagnóstico inconclusivo"

# Exemplo de uso
if __name__ == "__main__":
    hashrate_pct = float(input("Porcentagem nas 3 maiores pools (%): "))
    roi = float(input("ROI mensal (%): "))
    conhecimento = float(input("Acessibilidade ao conhecimento (0-10): "))
    custo_equip = float(input("Custo médio do equipamento das mineradoras (R$): "))
    custo_espaco = float(input("Custo por m² do espaço (R$): "))
    refrigeracao = float(input("Demanda de refrigeração (1-5): "))
    custo_usina = float(input("Custo por kWh da usina (R$): "))
    ruido = float(input("Nível de ruído (dB): "))
    temperatura = float(input("Temperatura de operação (°C): "))

    resultado = diagnosticar(hashrate_pct, roi, conhecimento, custo_equip,
                             custo_espaco, refrigeracao, custo_usina, ruido, temperatura)

    print("\nDiagnóstico do sistema:", resultado)
