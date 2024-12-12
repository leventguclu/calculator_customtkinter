
import customtkinter as ctk
import math

class Calculator(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configure window
        self.title("Neumorphic Calculator")
        self.geometry("400x600")
        
        # Configure grid
        self.grid_columnconfigure((0,1,2,3), weight=1)
        
        # Variables
        self.result_var = ctk.StringVar(value="0")
        self.expression = ""
        self.theme_mode = "light"
        
        # Create display
        self.display = ctk.CTkEntry(
            self,
            textvariable=self.result_var,
            font=("Arial", 40),
            height=100,
            justify="right",
            state="readonly"
        )
        self.display.grid(row=0, column=0, columnspan=4, padx=20, pady=20, sticky="nsew")
        
        # Button configurations
        self.buttons = {
            'C': (1, 0), '±': (1, 1), '%': (1, 2), '÷': (1, 3),
            '7': (2, 0), '8': (2, 1), '9': (2, 2), '×': (2, 3),
            '4': (3, 0), '5': (3, 1), '6': (3, 2), '-': (3, 3),
            '1': (4, 0), '2': (4, 1), '3': (4, 2), '+': (4, 3),
            '0': (5, 0, 2), '.': (5, 2), '=': (5, 3)
        }
        
        # Create buttons
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
                
        # Theme toggle button
        self.theme_button = ctk.CTkButton(
            self,
            text="🌙",
            width=40,
            height=40,
            corner_radius=20,
            command=self.toggle_theme
        )
        self.theme_button.grid(row=6, column=3, padx=5, pady=5, sticky="e")
        
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
                self.result_var.set("Error")
                self.expression = ""
        elif value == '±':
            try:
                current = float(self.expression)
                self.expression = str(-current)
                self.result_var.set(self.expression)
            except:
                pass
        elif value == '%':
            try:
                current = float(self.expression)
                self.expression = str(current/100)
                self.result_var.set(self.expression)
            except:
                pass
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
