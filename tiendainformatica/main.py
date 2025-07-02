
import flet as ft
from views.main_view import Main_Window
from views.panel_view_consultasgenerales import Panel_Window_ConsultasGenerales
from views.panel_view_pago import Panel_Window_Pago

def main(page:ft.Page):
    page.title = "Tienda Informática - Proyecto ABP"
    # index = Main_Window(page.width,page.height) # Pantalla principal
    index = Main_Window(page.width,page.height) # Pantalla principal
    page.views.append(index)
    page.update() # Siempre que quieras actualizar contenido hay que actulizar
    index.page.on_resized = index.ajustarPantalla
    index.ajustarPantalla()

if __name__ == "__main__":
    ft.app(target=main) 