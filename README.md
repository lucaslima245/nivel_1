# nivel_1

# PDV com Descontos Progressivos

## O que o código faz
Este script simula um Ponto de Venda (PDV) automatizado que calcula o valor de compras aplicando regras de descontos progressivos baseados na idade do cliente e no valor total da transação. O sistema opera em um loop contínuo até que o operador decida encerrar, gerando ao final um relatório consolidado com o resumo financeiro do dia.

## Como ele faz
1. **Entrada de Dados:** O programa solicita o valor bruto da compra e a idade do cliente.
2. **Validação:** Verifica se os números digitados são negativos; caso sejam, emite um alerta e solicita os dados novamente.
3. **Desconto por Idade:** Caso o cliente tenha 65 anos ou mais, aplica-se automaticamente um desconto de 20% sobre o valor original.
4. **Desconto por Valor:** Avalia o valor resultante após o desconto de idade. Se esse valor ultrapassar R$ 100,00, aplica-se um desconto adicional de 10% sobre ele.
5. **Armazenamento:** Cada transação validada tem seus valores (bruto, desconto e final) salvos em uma lista estruturada.
6. **Encerramento e Resumo:** Quando o valor `0` é digitado, o loop é finalizado e o sistema exibe o total de compras, a somatória bruta, o total de descontos concedidos e o faturamento líquido final.

## Como rodar
Certifique-se de ter o Python instalado em sua máquina. Abra o terminal na pasta do projeto e execute o seguinte comando:

```bash
python pdv.py