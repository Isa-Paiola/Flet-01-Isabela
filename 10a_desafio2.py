    # Campo de texto para buscar produtos por nome
    campo_busca = ft.TextField(
        label="Buscas prodduto",
        width=200,
        prefix_icon=ft.Icons.SEARCH # Ícone de lupa
    )

    def remover_do_carrinho(index):
        """Remove um produto específico do carrinho usando seu índice"""
        nonlocal total_carrinho # Permite modificar a variável global total_carrinho
        # Verifica se o índice é válido (existe na lista)
        if 0 <= index < len(carrinho):
            #Remove o produto da lista e armazena os dados dele
            produto = carrinho.pop(index)
            #Subtrai o preço do produto do total
            total_carrinho -= produto["preço"]
            #Atualiza a interface do carrinho
            atualizar_carrinho()
            #mostrar_notificacao de remoção
            mostrar_notificacao(f"❌ {produto['nome']} removido!")

    def atualizar_carrinho():
        """Atualiza a exibição do carrinho na interface"""
        # Atualiza o contador de itens no carrinho
        contador_carrinho.value = f"Carrinho ({len(carrinho)})"
        # Atualiza o  valor total formatado em reais
        total_texto.value = f"Total: R$ {total_carrinho:.2f}"

        # Limpa a lista visual do carrinho
        lista_carrinho.controls.clear()

        # Adiciona cada item do carrinho na lista visual
        for i, item in enumerate(carrinho):
            # Cria uma linha para cada produto no carrinho
            linha_produto = ft.row([
                # Nome do produto (expande para ocupar espaço desponível)
                ft.Text(f"{item['nome']}", expand=True),
                # Preço do produto
                ft.Text(f"R$ {item['preco']:.2f}", color=ft.Colors.GREEN_600),
                # Botão para remover o produto (usando o índice atual)
                ft.IconButton(
                    ft.Icons.DELETE,
                    icon_color=ft.Colors.RED,
                    on_click=lambda e, idx=i: remover_do_carrinho(idx)
                )
            ], spacing=10)

            # Adiciona a linha à lista visual
            lista_carrinho.controls.append(linha_produto)

        # Atualiza a página para refletir as mudanças
        page.update()

    def carregar_produtos(e=None):
        """Carrega e exibe produtos aplicando os filtros selecionados"""
        # Limpa a área de produtos antesde recarregar
        area_produtos.controls.clear()

        # Obtém os valores dos filtros
        categoria = filtro_categoria.value
        preco_faixa = filtro_preco.value
        busca= (campo_busca.value or "").lower() # Converte para minúscula para busca

        # Percorre todos os produtos disponíveis
        for produto in produtos:
            # Aplica filtro de categoria
            if categoria !="Todas" and produto["categoria"] !=categoria:
                continue # Pula este produto se não bater a categoria

            # Aplica filtro de busca por nome 
            if busca and busca not it produto["nome"].lower():
                continue # Pula se o termo buscado não estiver no nome

            # Se chegou até aqui, o produto passou por todos os filtros
            # Cria o card do produto
            card = criar_card_produto(
                produto["nome"],
                produto["preco"],
                produto["categoria"],
                produto[emoji],
                produto[cor]
            )
            # Adiciona o card à área de produtos
            area_produtos.controls.append(card)

        # Atualiza a página para mostrar os produtos filtrados
        page.update()

    def finalizar_comprar(e):
    """Finaliza a compra - limpa o carrinho e zera o total"""
    nonlocal total_carrinho # Perite modificar a variável global
    if len(carrinho) > 0:
        # Limpa cmpletamente a lista do carrinho
        carrinho.clear()
        # Zero o total (importante: usar nonlocal para modificar a variável global)
        total_carrinho = 0.0
        # Atualiza a interface do carrinho
        atualizar_carrinho()
        # Mostra mensagem de sucesso
        mostrar_notificacao(f"🎉 Compra finalizada! Obrigado!")
    else:
        # Mostra aviso se carrinho estiver vazio
        mostrar_notificacao("⚠️ Carrinho vazio!")

def limpar_filtros(e):
    """Limpa todos os filtros e redefine para valores padrão"""
    # Redefine todos os filtros para seus valores iniciais
    filtro_categoria.value = "Todas"
    filtro_preco.value = "Todos"
    campo_busca.value = ""

    # Recarrega os produtos sem filtros
    carregar_produtos()

    # Mostra notificacao de que os filtros foram limpos
    mostrar_notificacao(mensagem):
    """Exibe uma mensagem de notificação para o usuário"""
    notificacao.value = mensagem
    page.update()

    # Conecta os eventos de mudança dos filtros à função de carregar produtos
    # Sempre que o usuário mudar algum filtro, os produtos serão recarregados
    for controle in [filtro_categoria, filtro_preco, campo_busca]:
        controle.om_change = carregar_produtos

        