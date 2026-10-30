# ==========================================
# DESAFIO NÍVEL 1 — PDV COM DESCONTOS
# ==========================================

compras = []

print("==========================================")
print("     SISTEMA PDV - DESCONTOS PROGRESSIVOS")
print("==========================================")

while True:
  # 1. Recebimento dos inputs
  valor_original = float(input("\nDigite o valor da compra (ou 0 para sair): R$ "))

  # 5. Condição de parada do loop
  if valor_original == 0:
    break

  idade = int(input("Digite a idade do cliente: "))

  # 7. Validação simples para valores negativos
  if valor_original < 0 or idade < 0:
    print(
        "⚠️ Aviso: O valor da compra e a idade não podem ser negativos. Tente"
        " novamente."
    )
    continue

  # 2. Regra 1 — Desconto por idade (>= 65 anos = 20%)
  if idade >= 65:
    desconto_idade = valor_original * 0.20
    valor_apos_idade = valor_original * 0.80
  else:
    desconto_idade = 0.0
    valor_apos_idade = valor_original

  # 3. Regra 2 — Desconto por valor (se > R$ 100,00 após idade = 10% extra)
  if valor_apos_idade > 100:
    desconto_valor_extra = valor_apos_idade * 0.10
    valor_final = valor_apos_idade * 0.90
  else:
    desconto_valor_extra = 0.0
    valor_final = valor_apos_idade

  # Total de descontos aplicados nesta compra específica
  desconto_total_compra = desconto_idade + desconto_valor_extra

  # 4. Exibir o valor final no console formatado em reais
  print(f"-> Valor final da compra: R$ {valor_final:.2f}")

  # 6. Guardar cada compra em uma lista
  compras.append({
      "bruto": valor_original,
      "desconto": desconto_total_compra,
      "final": valor_final,
  })

# ==========================================
# 6. RESUMO FINAL DO DIA
# ==========================================
print("\n" + "=" * 42)
print("           RESUMO DO DIA (PDV)           ")
print("=" * 42)

quantidade_compras = len(compras)
total_bruto = sum(item["bruto"] for item in compras)
total_descontos = sum(item["desconto"] for item in compras)
total_final = sum(item["final"] for item in compras)

print(f"Quantidade de compras registradas: {quantidade_compras}")
print(f"Total bruto acumulado:          R$ {total_bruto:.2f}")
print(f"Total de descontos concedidos:  R$ {total_descontos:.2f}")
print(f"Total final faturado:           R$ {total_final:.2f}")
print("=" * 42)
print("Fim do expediente. Sistema encerrado.")