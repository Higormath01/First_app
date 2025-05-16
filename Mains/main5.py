
from datetime import datetime
import flet as ft


def main(page: ft.Page):
    # Configuração da página
    page.title = "Minha Aplicação Flet"
    page.theme_mode = ft.ThemeMode.LIGHT  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667


    def mostrar_idade(e):

        data_nascimento = datetime.strptime(input_nm1.value, "%d/%m/%Y")
        data_atual = datetime.now()
        idade = data_atual.year - data_nascimento.year

        if data_atual.month > data_nascimento.month:
            idade = idade - 1

        if int(idade) >= 18:
            txt_resultado.value = f'voce tem {idade} ja é maior de idade'
            print(f'voce tem {idade} ja é maior de idade')
            page.update()
        else:
            txt_resultado.value = f'voce tem {idade} ano e ainda menor de idade'

            page.update()

    # Criação de componentes
    input_nm1 = ft.TextField(label="digite a data", hint_text="Digite")

    btn_enviar = ft.FilledButton(
        text="Enviar",
        width=page.window.width,
        on_click=mostrar_idade,
    )
    txt_resultado = ft.Text(value="")

    # Construir o layout
    page.add(
        ft.Column(
            [
                input_nm1,
                btn_enviar,
                txt_resultado,
            ]
        )
    )

ft.app(main)

