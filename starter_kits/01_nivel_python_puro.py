# ==============================================================================
# 🧠 STARTER KIT: PYTHON PURO (Matemática do Zero)
# Missão: Implementar o algoritmo (ex: Naive Bayes ou Perceptron) sem usar 
# nenhuma biblioteca de Machine Learning.
# ==============================================================================

class ModeloPythonPuro:
    def __init__(self):
        # Aqui o modelo guarda o que aprendeu (ex: dicionário de contagens ou pesos)
        self.conhecimento = {} 

    def fit(self, X_treino, y_treino):
        """
        O Suor: Aprende os padrões matemáticos a partir dos dados.
        X_treino: Lista de entradas (ex: listas de palavras ou características).
        y_treino: Lista de respostas corretas (rótulos).
        """
        print("Treinando o modelo com matemática pura...")
        # TODO: Implemente o loop para contar frequências (Bayes) 
        # ou ajustar os pesos (Perceptron)
        
        pass

    def predict(self, X_novo):
        """
        O Lucro: Usa o 'conhecimento' para prever dados não vistos.
        """
        previsoes = []
        # TODO: Para cada item em X_novo, aplique a sua fórmula matemática
        # e adicione a resposta na lista 'previsoes'.
        
        return previsoes

# --- ÁREA DE TESTE ---
if __name__ == "__main__":
    X = [[1, 1], [0, 0]] # Exemplo de dados
    y = ["ClasseA", "ClasseB"]
    
    modelo = ModeloPythonPuro()
    modelo.fit(X, y)
    resultado = modelo.predict([[1, 0]])
    print(f"Previsão: {resultado}")