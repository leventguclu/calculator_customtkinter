import customtkinter as ctk
import math

class Calculator(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Scientific Calculator")
        self.geometry("500x700")
        
        self.grid_columnconfigure((0,1,2,3), weight=1)
        
        self.result_var = ctk.StringVar(value="0")
        self.expression = ""
        self.theme_mode = "light"
        
        self.credit_label = ctk.CTkLabel(
            self,
            text="made by levo_gcl",
            text_color="red",
            font=("Arial", 16)
        )
        self.credit_label.grid(row=0, column=0, columnspan=4, padx=5, pady=(10, 0), sticky="nsew")
        
        self.display = ctk.CTkEntry(
            self,
            textvariable=self.result_var,
            font=("Arial", 40),
            height=100,
            justify="right",
            state="readonly"
        )
        self.display.grid(row=1, column=0, columnspan=4, padx=20, pady=20, sticky="nsew")
        
        self.buttons = {
            'sin': (2, 0), 'cos': (2, 1), 'tan': (2, 2), 'C': (2, 3),
            'log': (3, 0), '√': (3, 1), '^': (3, 2), '÷': (3, 3),
            '7': (4, 0), '8': (4, 1), '9': (4, 2), '×': (4, 3),
            '4': (5, 0), '5': (5, 1), '6': (5, 2), '-': (5, 3),
            '1': (6, 0), '2': (6, 1), '3': (6, 2), '+': (6, 3),
            '0': (7, 0, 2), '.': (7, 2), '=': (7, 3)
        }
        
        for text, pos in self.buttons.items():
            width = 160 if len(pos) > 2 else 80
            button = ctk.CTkButton(
                self,
                text=text,
                width=width,
                height=80,
                corner_radius=20,
                font=("Arial", 24),
                fg_color="#e0e5ec",
                text_color="#2d2d2d",
                hover_color="#d0d5dc",
                command=lambda t=text: self.button_click(t)
            )
            if len(pos) > 2:
                button.grid(row=pos[0], column=pos[1], columnspan=pos[2], padx=5, pady=5, sticky="nsew")
            else:
                button.grid(row=pos[0], column=pos[1], padx=5, pady=5, sticky="nsew")
                
        self.theme_button = ctk.CTkButton(
            self,
            text="🌙",
            width=40,
            height=40,
            corner_radius=20,
            command=self.toggle_theme
        )
        self.theme_button.grid(row=7, column=3, columnspan=1, padx=5, pady=5, sticky="se")
        
    def button_click(self, value):
        if value == 'C':
            self.expression = ""
            self.result_var.set("0")
        elif value == '=':
            try:
                expression = self.expression.replace('×', '*').replace('÷', '/')
                result = eval(expression)
                self.result_var.set(result)
                self.expression = str(result)
            except Exception as e:
                self.result_var.set("Hata")
                self.expression = ""
        elif value in ['sin', 'cos', 'tan']:
            try:
                current = float(self.expression)
                if value == 'sin':
                    result = math.sin(math.radians(current))
                elif value == 'cos':
                    result = math.cos(math.radians(current))
                else:
                    result = math.tan(math.radians(current))
                self.expression = str(result)
                self.result_var.set(self.expression)
            except:
                self.result_var.set("Hata")
                self.expression = ""
        elif value == 'log':
            try:
                current = float(self.expression)
                result = math.log10(current)
                self.expression = str(result)
                self.result_var.set(self.expression)
            except:
                self.result_var.set("Hata")
                self.expression = ""
        elif value == '√':
            try:
                current = float(self.expression)
                result = math.sqrt(current)
                self.expression = str(result)
                self.result_var.set(self.expression)
            except:
                self.result_var.set("Hata")
                self.expression = ""
        elif value == '^':
            self.expression += '**'
            self.result_var.set(self.expression)
        else:
            self.expression += value
            self.result_var.set(self.expression)
            
    def toggle_theme(self):
        if self.theme_mode == "light":
            self.theme_mode = "dark"
            self._set_appearance_mode("dark")
            self.theme_button.configure(text="☀️")
        else:
            self.theme_mode = "light"
            self._set_appearance_mode("light")
            self.theme_button.configure(text="🌙")

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
