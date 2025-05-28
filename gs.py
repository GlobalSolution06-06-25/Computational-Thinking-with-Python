def eh_decimal_simples(texto):
    """
    Verifica se texto é um número decimal positivo com no máximo um ponto,
    sem usar split nem count.
    Retorna True se for válido, False caso contrário.
    """
    ponto_encontrado = False  # Flag para controlar se já encontrou um ponto
    if len(texto) == 0:       # String vazia não é número válido
        return False
    for c in texto:
        if c == '.':
            if ponto_encontrado:
                # Se já encontrou um ponto antes, não pode ter outro
                return False
            ponto_encontrado = True
        elif not c.isnumeric():
            # Se encontrar caractere que não seja número nem ponto, inválido
            return False
    return True  # Passou por todas as verificações, é um número decimal válido

def validar_entrada(nome, minimo, maximo):
    """
    Solicita repetidamente um valor ao usuário até que seja um número decimal válido
    e esteja dentro do intervalo definido por minimo e maximo.
    Retorna o valor convertido para float.
    """
    while True:
        valor = input(f"{nome}: ")  # Solicita entrada do usuário

        if not eh_decimal_simples(valor):
            # Se a entrada não for número decimal válido, avisa e pede de novo
            print(f"[ERRO] {nome} deve ser um número positivo (ex: 23.5)")
            continue
        
        val = float(valor)  # Converte a string para float

        if val < minimo or val > maximo:
            # Se o valor estiver fora do intervalo permitido, avisa e pede de novo
            print(f"[ERRO] {nome} deve estar entre {minimo} e {maximo}")
            continue
        
        return val  # Valor válido e dentro do intervalo, retorna

def classificar_nivel(nivel_rio):
    """
    Classifica o nível do rio em três categorias:
    - Alerta máximo: nível >= 200 cm
    - Alerta: nível >= 100 cm e < 200 cm
    - Seguro: nível < 100 cm
    Retorna uma string com o status.
    """
    if nivel_rio >= 200:
        return "🔴 Alerta máximo"
    elif nivel_rio >= 100:
        return "🟡 Alerta"
    else:
        return "🟢 Seguro"

def processar_dados(nivel, umid):
    """
    Recebe o nível do rio e umidade, classifica o nível,
    e exibe uma análise formatada para o usuário.
    """
    status = classificar_nivel(nivel)  # Obtém status do nível
    print("\n📊 Análise de Risco:")
    print(f"Nível: {nivel:.1f} cm - {status}")  # Exibe nível com 1 casa decimal e status
    print(f"Umidade: {umid:.1f} %")             # Exibe umidade com 1 casa decimal

def receber_dados():
    """
    Função principal do programa.
    Solicita os dados ao usuário, valida as entradas,
    e chama a função para processar e mostrar o resultado.
    """
    print("Digite os dados coletados do sensor:")
    
    nivel_ok = validar_entrada("Nível do rio (cm)", 0, 300)  # Solicita e valida nível do rio
    umid_ok = validar_entrada("Umidade (%)", 0, 100)        # Solicita e valida umidade

    processar_dados(nivel_ok, umid_ok)  # Exibe análise com os dados válidos

# Início do programa: chama a função principal para rodar
receber_dados()
