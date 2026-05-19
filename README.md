# Projeto: Calculadora Inteligente em Python

## Objetivo

Desenvolver uma calculadora capaz de interpretar e resolver contas matemáticas digitadas diretamente pelo usuário, de forma simples, rápida e intuitiva.

A calculadora permite desde operações básicas até expressões mais completas, como:

```python
4 + 5 - 78 * 89
10 - 5
20 + 7
9 * 6
100 / 30
10% de 200
```

Além disso, o sistema oferece uma experiência mais inteligente, com recursos como histórico, edição da conta e tratamento de erros.

# Funcionalidades

## 1. Entrada de dados: O usuário digita a conta completa de uma única vez, sem precisar inserir número por número.

## 2. Execução contínua: A calculadora permanece ativa, permitindo vários cálculos seguidos sem reiniciar o programa.

## 3. Tratamento de erros: Caso o usuário digite algo inválido, como letras ou contas incorretas, o sistema retorna:

```python
[erro]
```
Sem travar ou encerrar o programa.


## 4. Limpar conta (comando L)
O usuário pode digitar:
```python
L
```
Para limpar a conta atual e começar uma nova.
O histórico não é apagado.


## 5. Deletar último caractere (comando D)
O usuário pode digitar:
```python
D
```
Para apagar apenas o último caractere digitado.
Exemplo:
```python
6 + 9 + 9
```
Após usar D:
```python
6 + 9 +
```

## 6. Histórico de cálculos (comando H)
O usuário pode visualizar todos os cálculos realizados.
O histórico mostra:
- Contas corretas
- Contas com erro

## 7. Execução automática
Assim que a conta é digitada, o resultado aparece automaticamente.
Não é necessário pressionar "=".

## 8. Exibição do resultado
O resultado aparece em uma cor mais suave no terminal para facilitar a visualização.

# Regras de cálculo
A calculadora entende:
- Soma
- Subtração
- Multiplicação
- Divisão
- Parênteses

## Tratamento de porcentagem
A porcentagem é interpretada de forma natural.
Exemplos:
```python
10% de 200
```
Resultado:
```python
20
```
```python
50 + 10%
```
Resultado:
```python
55
```
```python
50 - 10%
```
Resultado:
```python
45
```

# Estrutura interna
## Histórico
Lista com todos os cálculos realizados, incluindo erros.

## Conta atual
Valor que está sendo digitado ou editado no momento.

# Fluxo de uso
1. O usuário digita uma conta ou comando
2. O sistema identifica se é cálculo ou comando
3. Se for cálculo:
   - Interpreta a conta
   - Calcula o resultado
   - Mostra o resultado
   - Salva no histórico
4. Se for comando:
   - Executa a ação correspondente
5. O sistema continua rodando

# Como executar o projeto
## Abrir o arquivo Python
```bash
python3 calculadora.py
```

## Executar pelo arquivo .sh
Primeiro dar permissão:
```bash
chmod +x calculadora2.sh
```
Depois executar:
```bash
./calculadora2.sh
```

# Possíveis melhorias futuras
- Aceitar números com vírgula
- Criar interface visual
- Adicionar funções avançadas
- Salvar histórico permanentemente
