import flet as ft

def main(page: ft.Page):
    page.padding = 0
    page.bgcolor = 'white'
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'

    def button_clicked(e):
        texto.value = f"Os valores são:  '{email.value}', '{senha.value}'."
        page.update()

    texto = ft.Text(color="black")
    title = ft.Text(value="Cadastro", size=50, color="black")
    email = ft.TextField(label="Digite o seu email", color="black", focused_border_color="black", label_style=ft.TextStyle(color="black"), width=500)
    senha = ft.TextField(label="Digite a sua senha", password=True, can_reveal_password=True, color="black", focused_border_color="black", label_style=ft.TextStyle(color="black"), hint_style=ft.TextStyle(color="black"), width=500)
    button = ft.ElevatedButton(text="Enviar", on_click=button_clicked, color="white", width=200, height=40, bgcolor="black")
    googleButton = ft.ElevatedButton(text="Cadastrar", icon=ft.Image(src="assets/google.svg", width=24, height=24), color="white", bgcolor="black")
    githubButton = ft.ElevatedButton(text="Cadastrar", icon=ft.Image(src="assets/github.svg", width=24, height=24), color="white", bgcolor="black")

    # Criando um container para agrupar os elementos
    form = ft.Container(
        content = ft.Column(
            controls = [email, senha, button, texto],
            alignment = ft.MainAxisAlignment.CENTER,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER
        ),
        # bgcolor="blue",
        padding = ft.Padding(50, 35, 50, 0),
        border_radius = 10,  
        border = ft.BorderSide(color="black", width=3)
    )

    socialButtons = ft.Container(
        content = ft.Row(
            controls = [googleButton, githubButton],
            alignment = ft.MainAxisAlignment.CENTER,
            vertical_alignment = ft.CrossAxisAlignment.CENTER
        ),
        # bgcolor="blue",
        border_radius = 10,  
        border = ft.BorderSide(color="black", width=3)
    )

    page.add(title, form, socialButtons)

ft.app(main)
