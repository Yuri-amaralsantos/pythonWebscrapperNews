import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

class ThemeNavigator:
    def __init__(self, df):
        self.df = df
        self.temas = df["tema"].unique()
        self.index = 0

    
        self.fig, self.ax = plt.subplots(figsize=(10,6))
        plt.subplots_adjust(bottom=0.2) 

       
        ax_prev = plt.axes([0.7, 0.05, 0.1, 0.075])
        ax_next = plt.axes([0.81, 0.05, 0.1, 0.075])

      
        self.b_prev = Button(ax_prev, 'Anterior')
        self.b_next = Button(ax_next, 'Próximo')

        self.b_prev.on_clicked(self.go_back)
        self.b_next.on_clicked(self.go_forward)

     
        self.plot_current_theme()

    
        self.update_button_states()

        plt.show()

    def plot_theme(self, tema):
        self.ax.clear()
        subset = self.df[self.df["tema"] == tema]

       
        subset = subset.sort_values(by="frequencia", ascending=False).head(10)

        self.ax.bar(subset["palavra"], subset["frequencia"], color='skyblue')
        self.ax.set_title(f"Palavras mais frequentes em {tema.capitalize()}", fontsize=16)
        self.ax.set_ylabel("Frequência", fontsize=12)

        # Ajusta rótulos do eixo X
        self.ax.set_xticks(range(len(subset["palavra"])))
        self.ax.set_xticklabels(subset["palavra"], rotation=45, ha='right')

        # Apenas redesenha o canvas, sem tight_layout
        self.fig.canvas.draw_idle()

    def plot_current_theme(self):
        tema_atual = self.temas[self.index]
        self.plot_theme(tema_atual)
        self.update_button_states()

    def update_button_states(self):
      
        self.b_prev.set_active(self.index > 0)
        self.b_next.set_active(self.index < len(self.temas) - 1)
        self.fig.canvas.draw_idle()

    def go_back(self, event):
        if self.index > 0:
            self.index -= 1
            self.plot_current_theme()

    def go_forward(self, event):
        if self.index < len(self.temas) - 1:
            self.index += 1
            self.plot_current_theme()

def main(filepath="data/processed/frequency_by_theme.csv"):
    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        print(f"Aviso: Arquivo {filepath} não encontrado. Usando dados de exemplo.")
        data = {
            'tema': ['tema_a'] * 5 + ['tema_b'] * 5 + ['tema_c'] * 5,
            'palavra': ['p1', 'p2', 'p3', 'p4', 'p5'] * 3,
            'frequencia': [100, 90, 80, 70, 60, 110, 85, 75, 65, 55, 120, 95, 85, 75, 65]
        }
        df = pd.DataFrame(data)

    ThemeNavigator(df)

if __name__ == "__main__":
    main()
