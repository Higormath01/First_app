import flet as ft


def main(page: ft.Page):
    # Configuração da página
    page.title = "Minha Aplicação Flet"
    page.theme_mode = ft.ThemeMode.LIGHT  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Definição de funções
    def mostrar_par_ou_impar(e):
        try:
            num = int(input_nm1.value)
            par_impar = num % 2
            if par_impar == 0:
                txt_resultado.value = "Par"
            else:
                txt_resultado.value = "Impar"
            page.update()
        except ValueError:
            txt_resultado.value = "Digite um numero inteiro"
            page.update()

    # Criação de componentes
    input_nm1 = ft.TextField(label="Par ou Impar", hint_text="Digite o primeiro numero")

    btn_enviar = ft.FilledButton(
        text="Enviar",
        width=page.window.width,
        on_click=mostrar_par_ou_impar, )
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



