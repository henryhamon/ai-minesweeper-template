# ==============================================================================
# 🚀 STARTER KIT: SCIKIT-LEARN (Machine Learning Clássico)
# Missão: Utilizar modelos tradicionais (Árvores, Regressão, Random Forest)
# ==============================================================================
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# TODO: Importe o seu modelo (ex: from sklearn.ensemble import RandomForestClassifier)

def pipeline_scikit_learn(caminho_dados):
    # 1. ETL (Extração e Limpeza)
    print("1. Carregando dados...")
    # df = pd.read_csv(caminho_dados)
    
    # TODO: Separe as Features (X) do Target (y)
    X = [] 
    y = []
    
    # 2. Divisão de Treino e Teste (Obrigatório em ML)
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 3. Instanciação e Treinamento
    print("2. Treinando o modelo...")
    # modelo = RandomForestClassifier()
    # modelo.fit(X_train, y_train)
    
    # 4. Avaliação (O Teste Cego)
    print("3. Avaliando o modelo...")
    # previsoes = modelo.predict(X_test)
    # acuracia = accuracy_score(y_test, previsoes)
    # print(f"Acurácia no Teste: {acuracia * 100:.2f}%")
    
    # return modelo

# --- ÁREA DE TESTE ---
if __name__ == "__main__":
    # modelo_pronto = pipeline_scikit_learn("dados.csv")
    print("Boilerplate Scikit-Learn pronto!")