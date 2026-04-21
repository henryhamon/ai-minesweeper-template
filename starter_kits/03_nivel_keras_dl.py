# ==============================================================================
# 🤖 STARTER KIT: KERAS / TENSORFLOW (Deep Learning)
# Missão: Construir e treinar uma Rede Neural Profunda.
# ==============================================================================
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
# Importe outras camadas conforme a necessidade

def construir_rede_neural(input_shape, num_classes):
    """
    Define a arquitetura (as camadas) do cérebro.
    """
    modelo = Sequential()
    
    # TODO: Adicione as camadas ocultas (Hidden Layers)
    # Exemplo: modelo.add(Dense(64, activation='relu', input_shape=input_shape))
    
    # TODO: Adicione a camada de saída (Output Layer)
    # Dica: Se for classificação, a ativação costuma ser 'softmax' ou 'sigmoid'.
    # modelo.add(Dense(num_classes, activation='...'))
    
    # TODO: Compile o modelo com o Otimizador e a Função de Perda (Loss) correta
    # modelo.compile(optimizer='adam', loss='...', metrics=['accuracy'])
    
    return modelo

def treinar_e_avaliar(X_train, y_train, X_test, y_test):
    # 1. Definir os formatos (Shapes)
    input_shape = (X_train.shape[1],)
    num_classes = len(np.unique(y_train))
    
    # 2. Construir
    modelo = construir_rede_neural(input_shape, num_classes)
    
    # 3. Treinar (O .fit em Deep Learning requer 'epochs' e 'batch_size')
    print("Iniciando o treinamento (Epochs)...")
    # historico = modelo.fit(X_train, y_train, epochs=20, batch_size=32, validation_split=0.2)
    
    # 4. Avaliar
    # loss, acuracia = modelo.evaluate(X_test, y_test)
    # print(f"Acurácia Final no Teste: {acuracia * 100:.2f}%")
    
    return modelo

# --- ÁREA DE TESTE ---
if __name__ == "__main__":
    # X_train, y_train, X_test, y_test = ... (Carregue e converta seus dados para NumPy Arrays)
    # meu_modelo_dl = treinar_e_avaliar(X_train, y_train, X_test, y_test)
    print("Boilerplate Deep Learning (Keras) pronto!")