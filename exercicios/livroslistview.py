import flet as ft
from flet import AppBar, Text, View
from flet.core.colors import Colors
from flet.core.textfield import TextField

class User:
    def __init__(self, titulo, descricao,categoria, autor):
        self.titulo = titulo
        self.descricao = descricao
        self.categoria = categoria
        self.autor = autor


def main(page: ft.Page):
    # Configurações
    page.title = "Exemplo de Rotas"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Funções
    lista = []

    def salvar_titulo(e):
        if input_titulo.value == "" or input_descricao.value == "" or input_categoria.value == "" or input_autor.value == "":
            page.overlay.append(msg_error)
            msg_error.open = True
            page.update()

        else:
            obj_user = User(
                titulo=input_titulo.value,
                descricao=input_descricao.value,
                categoria=input_categoria.value,
                autor=input_autor.value,
            )
            lista.append(obj_user)
            input_descricao.value = ""
            input_titulo.value = ""
            input_categoria.value = ""
            input_autor.value = ""

            page.overlay.append(msg_sucesso)
            msg_sucesso.open = True
            page.update()

    # def salvar_titulo(e):
    #     if input_titulo.value == "":
    #         page.overlay.append(msg_error)
    #         msg_error.open = True
    #         page.update()
    #
    #     else:
    #         lista.append(obj_user)
    #         input_titulo.value = ""
    #         page.overlay.append(msg_sucesso)
    #         msg_sucesso.open = True
    #         page.update()

    def exibir_lista(e):
        lv_titulo.controls.clear()
        for user in lista:
            lv_titulo.controls.append(
                ft.Text(value=f"{user.titulo} - {user.descricao} - {user.categoria} - {user.autor}" ),
            )
        page.update()



    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Home"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_titulo,
                    input_descricao,
                    input_categoria,
                    input_autor,

                    ft.Button(
                        text="Salvar",
                        on_click=lambda _: salvar_titulo(e),

                    ),
                    ft.Button(
                        text="Exibir lista",
                        on_click=lambda _: page.go("/segunda")
                    )
                ],
            )
        )
        if page.route == "/segunda":
            exibir_lista(e)

            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Segunda tela"), bgcolor=Colors.SECONDARY_CONTAINER),
                        lv_titulo,
                        lv_descricao,
                        lv_categoria,
                        lv_autor,

                    ],
                )
            )
        page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    # Componentes
    msg_sucesso = ft.SnackBar(
        content=ft.Text("titulo salvo com sucesso!"),
        bgcolor=Colors.GREEN
    )

    msg_error = ft.SnackBar(
        content=ft.Text(("O titulo nao pode estar vazio!"),
                        bgcolor=Colors.RED)
    )

    input_titulo = ft.TextField(label="titulo")
    input_descricao = ft.TextField(label="descricao")
    input_categoria = ft.TextField(label="categoria")
    input_autor = ft.TextField(label="autor")

    lv_titulo = ft.ListView(
        height=500)

    lv_categoria = ft.ListView()

    lv_descricao = ft.ListView(
    )

    lv_autor = ft.ListView()

    # Eventos
    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar

    page.go(page.route)

    # Comando que executa o aplicativo
    # Deve estar sempre colado na linha
ft.app(main)






















