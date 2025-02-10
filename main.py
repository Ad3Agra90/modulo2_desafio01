# Missão 1: Restaurando as Regras Escolares 📝
# O vírus apagou os critérios de aprovação dos alunos! Para ajudar o Professor Byte a organizar o sistema, sua tarefa é criar um programa que verifique se um aluno foi aprovado (nota maior ou igual à 6) ou reprovado (nota menor ou igual à 5).

import time
nota_aluno = float(input("Digite a nota do aluno de 0 a 10: "))
if nota_aluno >= 6:
    print("Parabéns! Você foi APROVADO com a nota: ", nota_aluno)
elif nota_aluno <= 5:
    print("Sinto muito, a sua nota ", nota_aluno,
          " foi a baixo da média. REPROVADO")
else:
    print("Nota inválida")

# Missão 2: O Sistema Eleitoral Secreto 📝
# O grêmio estudantil da escola realiza votações para decidir melhorias e inovações, mas o vírus desativou a verificação de elegibilidade para votar! Sua tarefa é criar um programa que pergunte a idade do usuário e informe se ele pode votar (mínimo: 16 anos).

idade_aluno = int(input("Quantos anos o aluno tem? "))
if idade_aluno >= 16:
    print("O aluno pode votar!")
else:
    print("Infelizmente o aluno em questão não pode votar!")

# Missão 3: Recuperando o Sistema de Notas 📊
# As classificações das provas desapareceram! Agora os alunos não sabem se tiraram um A, B, C, D ou F . Antes que o pânico se espalhe, sua tarefa é criar um programa que peça a nota do aluno e imprima sua classificação conforme a escala:

# - A (90-100) – "Parabéns, você tirou A!"
# - B (80-89) – "Muito bem, você tirou B."
# - C (70-79) – "Bom trabalho, você tirou C."
# - D (60-69) – "Fique atento, você tirou D."
# - F (menos de 60) – "Estude um pouco mais, você tirou F."

nota_aluno = int(input("Digite a nota do aluno: "))
if nota_aluno < 60:
    print("Estude um pouco mais, você tirou F.")
elif 60 <= nota_aluno <= 69:
    print("Fique atento, você tirou D.")
elif 70 <= nota_aluno <= 79:
    print("Bom trabalho, você tirou C.")
elif 80 <= nota_aluno <= 89:
    print("Muito bem, você tirou B.")
elif 90 <= nota_aluno <= 100:
    print("Parabéns, você tirou A!")
else:
    print("Nota indefinida!")

# Missão 4: Restaurando a Identificação de Números ⚖️
# Os robôs da escola precisam identificar padrões numéricos para resolver cálculos e otimizar os sistemas. No entanto, o vírus bagunçou os algoritmos e agora eles não conseguem mais somar corretamente!
# Crie um programa que peça dois números ao usuário e exiba a soma deles.
numero1 = input("Digite o primeiro número: ")
numero1 = float(numero1.replace(',', '.'))
numero2 = input("Digite o segundo número: ")
numero2 = float(numero2.replace(',', '.'))
resultado = str(numero1 + numero2).replace('.', ',')
print("A soma dos dois números digitados é ", resultado)

# Missão 5: Recuperando o Cofre de Segurança 🔒
# O cofre da biblioteca guarda códigos raros de programação, mas o vírus resetou a senha! Agora, apenas quem souber a combinação correta poderá acessá-lo.
# Crie um programa que solicite ao usuário uma senha e verifique se ela está correta. A senha correta é "Python123".

acesso_permitido = "Python123"
for tentativa in range(3):
    senha = input("Digite a senha: ")
    if senha == acesso_permitido:
        print("Senha Correta!")
        break
    else:
        tentativas_restantes = 2-tentativa
        if tentativas_restantes == 2:
            print("Senha incorreta! Você só tem mais ",
                  2-tentativa, " tentativas")
        elif tentativas_restantes == 1:
            print("Senha incorreta! Você só tem mais ",
                  2-tentativa, " tentativa")
        else:
            print("ACESSO BLOQUEADO!")

# Missão 6: Reforçando a Segurança e a Contagem do Sistema 💾
# O vírus está comprometendo o sistema de segurança e a contagem de registros! Para restaurar o funcionamento correto, você precisa reforçar as verificações e garantir que os dados sejam processados corretamente.
#   Exiba os números de 1 a 10 usando um loop while.
numero = 1
print("CONTAGEM: ")
while numero < 11:
    print(numero)
    numero += 1
    time.sleep(0.5)
print("KABOOOMMM!!!")

# Missão 7: Organizando a Lista📋
# Os números estão misturados e precisam ser organizados!
# Para resolver isso, você deve pegar os seguintes números: 8, 3, 10, 1 e 5, armazená-los em uma lista e depois exibi-los em ordem crescente. Isso ajudará a colocar tudo em ordem corretamente!

lista = [8, 3, 10, 1, 5]
lista.sort()
print("Segue a lista ordenada: ", lista)

# Missão 8: Acessando os Registros de Alunos 🏷️
# O sistema de alunos está desordenado! Para acessar as informações corretamente, você precisa organizar os dados.
# Crie uma tupla com os seguintes nomes: Ana, Bruno, Carla, Daniel, Eduardo e exiba o primeiro e o último nome.

registro_alunos = ("Ana", "Bruno", "Carla", "Daniel", "Eduardo")
primeiro_nome = str(registro_alunos[0])
ultimo_nome = str(registro_alunos[-1])
print("O primeiro nome é: ", primeiro_nome, " e o último é ", ultimo_nome)

# Missão 9: Calculando Dobro de um Número 🛠️
# Os alunos precisam de um programa que ajude em cálculos rápidos.
# Sua tarefa é criar uma função que receba um número e retorne o dobro do seu valor.
# ➡️ Exemplo: dobro(5)
# ➡️ Saída: "O dobro de 5 é 10"

numero = int(input("Digite um numero: "))


def dobro(numero):
    return numero*2


resultado = dobro(numero)
print("O dobro do número digitado é ", resultado)

# Missão 10: Contando Letras 🔄
# O sistema precisa contar quantas letras há em um nome.
# ➡️ Crie uma função que receba um nome e diga quantas letras esse nome tem.
# ➡️ Exemplo: contar_letras("Ana")
# ➡️ Saída:" O nome Ana tem 3 letras"

nome = input("Digite um nome: ")


def contador_nome(nome):
    return len(nome)


qntd_letras = contador_nome(nome)
print("O nome ", nome, " tem ", qntd_letras, " letras")
