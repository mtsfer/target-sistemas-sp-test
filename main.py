# 2) Sequência de Fibonacci:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
import json

print('2) ', end='')
number = int(input('Digite um número: '))

firstFibonacciNumber = 0
secondFibonacciNumber = 1
nextFibonacciNumber = 1

isNumberFoundOnSequence = True if number in (0, 1) else False
while nextFibonacciNumber < number and not isNumberFoundOnSequence:
    firstFibonacciNumber = secondFibonacciNumber
    secondFibonacciNumber = nextFibonacciNumber
    nextFibonacciNumber = firstFibonacciNumber + secondFibonacciNumber
    if nextFibonacciNumber == number:
        isNumberFoundOnSequence = True

if isNumberFoundOnSequence:
    print(f'O número {number} faz parte da Sequência de Fibonacci!\n')
else:
    print(f'O número {number} NÃO faz parte da Sequência de Fibonacci!\n')


"""3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que 
desejar, que calcule e retorne: • O menor valor de faturamento ocorrido em um dia do mês; • O maior valor de 
faturamento ocorrido em um dia do mês; • Número de dias no mês em que o valor de faturamento diário foi superior à 
média mensal.

IMPORTANTE: a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal; b) Podem existir dias sem 
faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;"""
print('3) Faturamento de uma distribuidora:')

with open('dados.json') as data:
    incomes: list = json.load(data)

monthIncomeAverage = round(sum(income['valor'] for income in incomes) / len(incomes), 4)

lowerIncome = min(income['valor'] for income in incomes)
higherIncome = max(income['valor'] for income in incomes)

daysWithLowerIncome = \
    list(str(income['dia']) for income in list(filter(lambda income: income['valor'] == lowerIncome, incomes)))

daysWithHigherIncome = \
    list(str(income['dia']) for income in list(filter(lambda income: income['valor'] == higherIncome, incomes)))

numberOfDaysWithIncomeAboveAverage = len(list(filter(lambda income: income['valor'] > monthIncomeAverage, incomes)))

print(f'a) O maior faturamento foi de R${higherIncome}, ocorrido no(s) dia(s) {", ".join(daysWithHigherIncome)} do mês.')
print(f'b) O menor faturamento foi de R${lowerIncome}, ocorrido no(s) dia(s) {", ".join(daysWithLowerIncome)} do mês.')
print(f'c) O faturamento ultrapassou a média mensal de R${monthIncomeAverage} em {numberOfDaysWithIncomeAboveAverage} '
      f'dias deste mês.\n')


"""4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53
Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro 
do valor total mensal da distribuidora."""

print('4) Porcentagem de representação no faturamento mensal por estado:')
incomesByState = [
    {
        'uf': 'SP',
        'faturamento': 67836.43
    },
    {
        'uf': 'RJ',
        'faturamento': 36678.66
    },
    {
        'uf': 'MG',
        'faturamento': 29229.88
    },
    {
        'uf': 'ES',
        'faturamento': 27165.48
    },
    {
        'uf': 'Outros',
        'faturamento': 19849.53
    },
]

totalIncome = sum(stateIncome['faturamento'] for stateIncome in incomesByState)
for income in incomesByState:
    print(f'{income["uf"]}: R${income["faturamento"]} ({round(income["faturamento"] * 100 / totalIncome, 2)}%)')
print(f'Total: R${totalIncome} (100%)\n')


# 5) Escreva um programa que inverta os caracteres de um string.
print('5) ', end='')
text = input('Digite uma frase: ')
reversedText = ''
for index in range(len(text) - 1, -1, -1):
    reversedText += text[index]
print(f'O texto invertido é: {reversedText}')
