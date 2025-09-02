import flet as ft

def main(page: ft.Page):
    page.title = "Campo de Texto"
    page.padding = 30
    page.bgcolor = ft.Colors.BLUE_50
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    # Título principal
    titulo = ft.Text(
        "Vamos nos conhecer! ☺️",
        size=26,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE_900,
        text_align=ft.TextAlign.CENTER,
    )

    # Campo de entrada
    campo_nome = ft.TextField(
        label="Digite seu nome aqui",
        width=320,
        border_color=ft.Colors.BLUE_400,
        focused_border_color=ft.Colors.BLUE_600,
        cursor_color=ft.Colors.BLUE_700,
        prefix_icon=ft.Icons.PERSON, # ícone dentro do campo
    )

    # Texto de resposta
    resposta = ft.Text(
        value="",
        size=18,
        text_align=ft.TextAlign.CENTER,
        weight=ft.FontWeight.W_500,
    )

    # Função do botão
    def processar_nome(evento):
        nome_digitado = campo_nome.value

        if not nome_digitado:
            resposta.value = "⚠️ Por favor, digite seu nome!"
            resposta.color = ft.Colors.RED
        elif len(nome_digitado) < 2:
            resposta.value = "⚠️ Nome muito curto!"
            resposta.color = ft.Colors.ORANGE
        else:
            resposta.value = f"✅ Olá, {nome_digitado}! Prazer em conhecê-lo(a)!"
            resposta.color = ft.Colors.GREEN_700
        page.update()

    # Botão estilizado
    botao_ok = ft.ElevatedButton(
        text="Confirmar",
        on_click=processar_nome,
        width=180,
        height=50,
        bgcolor=ft.Colors.BLUE_600,
        color=ft.Colors.WHITE,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            elevation=5,
        ),
        icon=ft.Icons.CHECK_CIRCLE_OUTLINE, # ícone no botão
    )

    # Layout organizado
    conteudo = ft.Column(
        [
            titulo,
            campo_nome,
            botao_ok,
            resposta,
        ],
        alignment="center",
        horizontal_alignment="center",
        spacing=20,
    )

    page.add(conteudo)


ft.app(target=main)
