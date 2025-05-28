def eh_decimal_simples(texto):
    """
    Verifica se texto é um número decimal positivo com no máximo um ponto.
    Retorna True se for válido, False se não.
    """
    ponto_encontrado = False
    if len(texto) == 0:
        return False
    for c in texto:
        if c == '.':
            if ponto_encontrado:
                return False
            ponto_encontrado = True
        elif not c.isnumeric():
            return False
    return True

def validar_entrada(nome, minimo, maximo):
    """
    Solicita repetidamente um valor ao usuário até que seja um número decimal válido
    e esteja dentro do intervalo definido.
    """
    while True:
        valor = input(f"{nome}: ")

        if not eh_decimal_simples(valor):
            print(f"[ERRO] {nome} deve ser um número positivo (ex: 23.5)")
            continue
        
        val = float(valor)

        if val < minimo or val > maximo:
            print(f"[ERRO] {nome} deve estar entre {minimo} e {maximo}")
            continue
        
        return val

def classificar_nivel(nivel_rio):
    """
    Classifica o nível do rio em:
    - Alerta máximo: nível >= 200 cm
    - Alerta: nível >= 100 cm e < 200 cm
    - Seguro: nível < 100 cm
    """
    if nivel_rio >= 200:
        return "🔴 Alerta máximo"
    elif nivel_rio >= 100:
        return "🟡 Alerta"
    else:
        return "🟢 Seguro"

def processar_dados(nivel, umid, temp):
    """
    Recebe o nível do rio, umidade e temperatura,
    classifica o nível e exibe análise formatada.
    """
    status = classificar_nivel(nivel)
    print("\n📊 Análise de Risco:")
    print(f"Nível: {nivel:.1f} cm - {status}")
    print(f"Umidade: {umid:.1f} %")
    print(f"Temperatura: {temp:.1f} °C")

def receber_dados():
    """
    Função principal.
    Solicita nível, umidade e temperatura,
    e mostra o resultado final.
    """
    print("Digite os dados coletados do sensor:")
    
    nivel_ok = validar_entrada("Nível do rio (cm)", 0, 300)
    umid_ok = validar_entrada("Umidade (%)", 0, 100)
    temp_ok = validar_entrada("Temperatura (°C)", -20, 60)  # Limites típicos do DHT22

    processar_dados(nivel_ok, umid_ok, temp_ok)

# Início do programa
receber_dados()
