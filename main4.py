import flet as ft


def main(page: ft.Page):
    # Configuração da página
    page.title = "Minha Aplicação Flet"
    page.theme_mode = ft.ThemeMode.LIGHT  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Definição de funções
    def subtracao(e):
       subtracao=int(input_nm1.value) - int(input_nm2.value)
       txt_resultado.value = f'Resultado = {subtracao}'
       page.update()

    def soma(e):
       soma=int(input_nm1.value) + int(input_nm2.value)
       txt_resultado.value = f'Resultado = {soma}'
       page.update()

    def multiplicacao(e):
       multiplicacao=int(input_nm1.value) * int(input_nm2.value)
       txt_resultado.value = f'Resultado = {multiplicacao}'
       page.update()

    def divisao(e):
       divisao=int(input_nm1.value) / int(input_nm2.value)
       txt_resultado.value = f'Resultado = {divisao}'
       page.update()


    # Criação de componentes
    input_nm1 = ft.TextField(label="numero", hint_text="Digite o primeiro numero")
    input_nm2 = ft.TextField(label="numero", hint_text="Digite o segundo numero")

    btn_subtracao = ft.FilledButton(
        text="subtrair",
        width=page.window.width,
        on_click=subtracao

    )
    btn_multiplicacao = ft.FilledButton(
        text="multiplicar",
        width=page.window.width,
        on_click=multiplicacao

    )
    btn_divisao = ft.FilledButton(
        text="dividir",
        width=page.window.width,
        on_click=divisao

    )
    btn_soma = ft.FilledButton(
        text="somar",
        width=page.window.width,
        on_click=soma

    )

    txt_resultado = ft.Text(value="")

    # Construir o layout
    page.add(
        ft.Column(
            [
                input_nm1,
                input_nm2,
                btn_subtracao,
                btn_multiplicacao,
                btn_divisao,
                btn_soma,
                txt_resultado,
            ]
        )
    )

ft.app(main)



