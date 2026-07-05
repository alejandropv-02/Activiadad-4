import reflex as rx
import re

# 1. Definimos el Estado de la aplicación (Equivalente al useState de React)
class FormState(rx.State):
    # Datos del formulario
    username: str = ""
    email: str = ""
    password: str = ""

    # Mensajes de error para validación inmediata
    username_error: str = ""
    email_error: str = ""
    password_error: str = ""

    # Controlar si el campo ha sido modificado/tocado
    username_touched: bool = False
    email_touched: bool = False
    password_touched: bool = False

    # 2. Manejadores de eventos y validación en tiempo real (onChange / onBlur)
    def validate_username(self, value: str):
        self.username = value
        self.username_touched = True
        
        if not value.strip():
            self.username_error = "El nombre de usuario es obligatorio."
        elif len(value) < 3:
            self.username_error = "Debe tener al menos 3 caracteres."
        else:
            self.username_error = ""

    def validate_email(self, value: str):
        self.email = value
        self.email_touched = True
        email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        
        if not value.strip():
            self.email_error = "El correo electrónico es obligatorio."
        elif not re.match(email_regex, value):
            self.email_error = "El formato de correo no es válido."
        else:
            self.email_error = ""

    def validate_password(self, value: str):
        self.password = value
        self.password_touched = True
        
        if not value:
            self.password_error = "La contraseña es obligatoria."
        elif len(value) < 6:
            self.password_error = "Debe tener al menos 6 caracteres."
        else:
            self.password_error = ""

    # 3. Manejador del envío del formulario (onSubmit)
    def handle_submit(self, form_data: dict):
        # Forzar validación de todos por si se envían vacíos
        self.validate_username(self.username)
        self.validate_email(self.email)
        self.validate_password(self.password)

        # Comprobar si hay errores activos o campos vacíos
        has_errors = any([self.username_error, self.email_error, self.password_error])
        has_empty = not all([self.username, self.email, self.password])

        if has_errors or has_empty:
            return rx.window_alert("Por favor, corrige los errores antes de enviar.")
        
        return rx.window_alert(f"¡Formulario enviado con éxito! Usuario: {self.username}")


# 4. Interfaz de Usuario (Componentes enlazados al Estado)
def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Registro", size="7", margin_bottom="15px"),
            
            rx.form(
                rx.vstack(
                    # Campo: Username
                    rx.text("Nombre de Usuario:"),
                    rx.input(
                        value=FormState.username,
                        on_change=FormState.validate_username, # Validación inmediata al escribir
                        placeholder="Ej. alejandro123",
                        border_color=rx.cond(FormState.username_error & FormState.username_touched, "red", "silver")
                    ),
                    rx.cond(
                        FormState.username_touched & FormState.username_error,
                        rx.text(FormState.username_error, color="red", font_size="12px"),
                    ),

                    # Campo: Email
                    rx.text("Correo Electrónico:", margin_top="10px"),
                    rx.input(
                        value=FormState.email,
                        on_change=FormState.validate_email,
                        placeholder="correo@ejemplo.com",
                        border_color=rx.cond(FormState.email_error & FormState.email_touched, "red", "silver")
                    ),
                    rx.cond(
                        FormState.email_touched & FormState.email_error,
                        rx.text(FormState.email_error, color="red", font_size="12px"),
                    ),

                    # Campo: Password
                    rx.text("Contraseña:", margin_top="10px"),
                    rx.input(
                        value=FormState.password,
                        on_change=FormState.validate_password,
                        type="password",
                        placeholder="Mínimo 6 caracteres",
                        border_color=rx.cond(FormState.password_error & FormState.password_touched, "red", "silver")
                    ),
                    rx.cond(
                        FormState.password_touched & FormState.password_error,
                        rx.text(FormState.password_error, color="red", font_size="12px"),
                    ),

                    # Botón de envío
                    rx.button("Registrarse", type="submit", margin_top="20px", width="100%", color_scheme="blue"),
                    align_items="start",
                    width="100%"
                ),
                on_submit=FormState.handle_submit,
                width="100%"
            ),
            padding="30px",
            border="1px solid #e2e8f0",
            border_radius="8px",
            box_shadow="lg",
            width="400px",
        ),
        height="100vh",
    )

# Configuración de la app de Reflex
app = rx.App()
app.add_page(index)