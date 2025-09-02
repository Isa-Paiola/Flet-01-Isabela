import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora Simples"
    page.padding = 40
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = ft.Colors.BLUE_GREY_50

    # Campos e elementos
    numero1 = ft.TextField(
        label="Primeiro número", width=250, keyboard_type=ft.KeyboardType.NUMBER
    )
    numero2 = ft.TextField(
        label="Segundo número", width=250, keyboard_type=ft.KeyboardType.NUMBER
    )
    operacao = ft.Dropdown(
        label="Operação", width=250,
        options=[
            ft.dropdown.Option("Soma"),
            ft.dropdown.Option("Subtração"),
            ft.dropdown.Option("Multiplicação"),
            ft.dropdown.Option("Divisão")
        ]
    )
    resultado = ft.Text(
        "Resultado aparecerá aqui",
        size=18,
        text_align=ft.TextAlign.CENTER,
        color=ft.Colors.GREY_600,
        weight=ft.FontWeight.BOLD
    )
    
    # Funções
    def calcular(e):
        try:
            num1, num2, op = float(numero1.value), float(numero2.value), operacao.value

            if not op:
                resultado.value, resultado.color = "⚠️ Selecione uma operação", ft.Colors.ORANGE
            elif op == "Divisão" and num2 == 0:
                resultado.value, resultado.color = "❌ Erro: Divisão por zero", ft.Colors.RED
            else:
                simbolos = {
                    "Soma": ("+", num1 + num2),
                    "Subtração": ("-", num1 - num2),
                    "Multiplicação": ("x", num1 * num2),
                    "Divisão": ("÷", num1 / num2)
                }
                simbolo, res = simbolos[op]
                resultado.value, resultado.color = f"{num1} {simbolo} {num2} = {res:.2f}", ft.Colors.GREEN
        except ValueError:
            resultado.value, resultado.color = "❌ Digite números válidos!", ft.Colors.RED
        page.update()

    def limpar(e):
        numero1.value = numero2.value = operacao.value = ""
        resultado.value, resultado.color = "Campos limpos! ✨", ft.Colors.BLUE
        page.update()

    # Layout principal com card
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    ft.Text("🧮 Calculadora Simples", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE),
                    numero1, numero2, operacao,
                    ft.Row(
                        [
                            ft.ElevatedButton(
                                "🧮 Calcular",
                                on_click=calcular,
                                width=150,
                                style=ft.ButtonStyle(
                                    bgcolor=ft.Colors.GREEN,
                                    color=ft.Colors.WHITE,
                                    shape=ft.RoundedRectangleBorder(radius=12),
                                )
                            ),
                            ft.ElevatedButton(
                                "🧹 Limpar",
                                on_click=limpar,
                                width=150,
                                style=ft.ButtonStyle(
                                    bgcolor=ft.Colors.RED,
                                    color=ft.Colors.WHITE,
                                    shape=ft.RoundedRectangleBorder(radius=12),
                                )
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20,
                    ),
                    ft.Divider(),
                    resultado
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            ),
            padding=30,
            border_radius=20,
            bgcolor=ft.Colors.WHITE,
            shadow=ft.BoxShadow(blur_radius=15, color=ft.Colors.GREY_400, offset=ft.Offset(0, 4))
        )
    )

ft.app(target=main)
