import customtkinter as ctk
from tkinter import filedialog, messagebox
from config import HOSPITAL_CONFIG, EPS_CONFIG
from main import rename_pdfs_with_prefix, split_pdfs, process_pdfs, combine_and_rename_pdfs


class PDFProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Procesador de PDFs")
        self.root.geometry("520x600")
        self.root.minsize(520, 600)  # Tamaño mínimo
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("blue")

        # Variables para las acciones seleccionadas
        self.rename_var = ctk.BooleanVar(value=False)
        self.split_var = ctk.BooleanVar(value=False)
        self.ocr_var = ctk.BooleanVar(value=False)
        self.combine_var = ctk.BooleanVar(value=False)

        # Configuración de EPS y Hospital
        self.eps_name_var = ctk.StringVar()
        self.hospital_name_var = ctk.StringVar()

        # Ruta de entrada
        self.input_path = ctk.StringVar(value="")

        # Interfaz gráfica
        self.create_widgets()
        self.configure_grid()

    def create_widgets(self):
        """Crear los widgets de la interfaz gráfica."""

        # Sección para la ruta de entrada
        ctk.CTkLabel(self.root, text="Seleccionar carpeta o ingresar ruta manualmente:").grid(
            row=0, column=0, columnspan=2, sticky="w", padx=10, pady=5
        )

        self.path_entry = ctk.CTkEntry(self.root, textvariable=self.input_path, width=300)
        self.path_entry.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        ctk.CTkButton(self.root, text="Buscar carpeta", command=self.select_input_path).grid(
            row=1, column=1, padx=10, pady=5
        )

        # Separador visual
        ctk.CTkLabel(self.root, text="").grid(row=2, column=0, columnspan=2, pady=5)

        # Selección de EPS
        ctk.CTkLabel(self.root, text="Seleccionar EPS:").grid(row=3, column=0, sticky="w", padx=10, pady=5)
        eps_options = [""] + list(EPS_CONFIG.keys())  # Agregar una opción vacía
        self.eps_dropdown = ctk.CTkOptionMenu(self.root, values=eps_options, variable=self.eps_name_var)
        self.eps_dropdown.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

        # Selección de Hospital
        ctk.CTkLabel(self.root, text="Seleccionar Hospital:").grid(row=4, column=0, sticky="w", padx=10, pady=5)
        hospital_options = [""] + list(HOSPITAL_CONFIG.keys())  # Agregar una opción vacía
        self.hospital_dropdown = ctk.CTkOptionMenu(self.root, values=hospital_options, variable=self.hospital_name_var)
        self.hospital_dropdown.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

        # Separador visual
        ctk.CTkLabel(self.root, text="").grid(row=5, column=0, columnspan=2, pady=5)

        # Acciones (Checkbuttons)
        ctk.CTkLabel(self.root, text="Seleccionar acciones:").grid(row=6, column=0, columnspan=2, sticky="w", padx=10, pady=5)

        ctk.CTkCheckBox(self.root, text="Renombrar PDFs con prefijo", variable=self.rename_var).grid(
            row=7, column=0, columnspan=2, sticky="w", padx=20
        )
        ctk.CTkCheckBox(self.root, text="Dividir PDFs por páginas", variable=self.split_var).grid(
            row=8, column=0, columnspan=2, sticky="w", padx=20
        )
        ctk.CTkCheckBox(self.root, text="Extraer texto o aplicar OCR", variable=self.ocr_var).grid(
            row=9, column=0, columnspan=2, sticky="w", padx=20
        )
        ctk.CTkCheckBox(self.root, text="Combinar y renombrar PDFs", variable=self.combine_var).grid(
            row=10, column=0, columnspan=2, sticky="w", padx=20
        )

        # Botón para ejecutar las acciones seleccionadas
        ctk.CTkButton(self.root, text="Ejecutar acciones seleccionadas", command=self.run_selected_actions).grid(
            row=11, column=0, columnspan=2, pady=10
        )

        # Salida de logs
        self.log_text = ctk.CTkTextbox(self.root, height=10, width=500)
        self.log_text.grid(row=12, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        self.log_text.configure(state="disabled")

    def configure_grid(self):
        """Configura la cuadrícula para que sea responsiva."""
        for i in range(2):
            self.root.columnconfigure(i, weight=1)
        for i in range(13):
            self.root.rowconfigure(i, weight=0)
        self.root.rowconfigure(12, weight=1)  # Expande el área de logs

    def select_input_path(self):
        """Permite al usuario seleccionar una carpeta."""
        selected_path = filedialog.askdirectory()  # Puedes usar askopenfilename para archivos
        if selected_path:
            self.input_path.set(selected_path)

    def log_message(self, message):
        """Muestra mensajes en el área de logs."""
        self.log_text.configure(state="normal")
        self.log_text.insert("end", f"{message}\n")
        self.log_text.configure(state="disabled")
        self.log_text.see("end")

    def run_selected_actions(self):
        """Ejecuta las acciones seleccionadas por el usuario."""
        input_path = self.input_path.get()
        eps_name = self.eps_name_var.get()
        hospital_name = self.hospital_name_var.get()

        # Validar elementos obligatorios
        if not input_path:
            messagebox.showerror("Error", "Por favor, selecciona o ingresa una carpeta válida.")
            return
        if not eps_name:
            messagebox.showerror("Error", "Por favor, selecciona una EPS.")
            return
        if not hospital_name:
            messagebox.showerror("Error", "Por favor, selecciona un hospital.")
            return

        try:
            # Ejecutar las acciones en orden
            if self.rename_var.get():
                self.log_message("Renombrando PDFs con prefijo...")
                rename_pdfs_with_prefix(input_path)

            if self.split_var.get():
                self.log_message("Dividiendo PDFs por páginas...")
                split_pdfs(input_path)

            if self.ocr_var.get():
                self.log_message("Extrayendo texto o aplicando OCR...")
                process_pdfs(input_path)

            if self.combine_var.get():
                self.log_message("Combinar y renombrar PDFs...")
                combine_and_rename_pdfs(input_path, EPS_CONFIG[eps_name], HOSPITAL_CONFIG[hospital_name])

            self.log_message("Todas las acciones seleccionadas se completaron exitosamente.")

        except Exception as e:
            self.log_message(f"Error: {e}")
            messagebox.showerror("Error", f"Ha ocurrido un error: {e}")


if __name__ == "__main__":
    root = ctk.CTk()
    app = PDFProcessorApp(root)
    root.mainloop()
