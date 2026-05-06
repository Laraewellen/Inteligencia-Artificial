# pip install ydata_profiling

import pandas as pd
from ydata_profiling import ProfileReport
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# =====================
# EDA
# =====================

df = pd.read_csv(
    "olist_orders_dataset.csv",
    sep=",",
    on_bad_lines="skip"
)

df.describe()
df.info()

profile = ProfileReport(df, title="Profiling Report")
profile.to_notebook_iframe()

# =====================
# Pré-processamento
# =====================

cols_datas = [
    'order_purchase_timestamp',
    'order_approved_at',
    'order_delivered_customer_date',
    'order_estimated_delivery_date'
]

for col in cols_datas:
    df[col] = pd.to_datetime(df[col])

# Target
df['atraso'] = (
    df['order_delivered_customer_date'] > df['order_estimated_delivery_date']
).astype(int)

# Features auxiliares
df['tempo_entrega'] = (
    df['order_delivered_customer_date'] - df['order_purchase_timestamp']
).dt.days

df['tempo_estimado'] = (
    df['order_estimated_delivery_date'] - df['order_purchase_timestamp']
).dt.days

df['diff_estimado_real'] = df['tempo_entrega'] - df['tempo_estimado']

# Remover nulos
df = df.dropna(subset=[
    'tempo_entrega',
    'tempo_estimado',
    'diff_estimado_real',
    'atraso'
])

# =====================
# Features
# =====================

features = ['tempo_entrega', 'tempo_estimado', 'diff_estimado_real']

X = df[features]
y = df['atraso']

scaler = StandardScaler()
X = scaler.fit_transform(X)

# =====================
# Split
# =====================

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# =====================
# Modelo (ReLU)
# =====================

model = Sequential()
model.add(Dense(16, activation='relu', input_shape=(X.shape[1],)))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

history = model.fit(
    X_train, y_train,
    epochs=6,
    validation_data=(X_test, y_test)
)

# =====================
# Gráfico
# =====================

plt.figure()

plt.plot(history.history['loss'], label='Loss Treino')
plt.plot(history.history['val_loss'], label='Loss Validação')

plt.plot(history.history['accuracy'], '--', label='Accuracy Treino')
plt.plot(history.history['val_accuracy'], '--', label='Accuracy Validação')

plt.legend()
plt.grid()
plt.show()

# =====================
# Avaliação
# =====================

loss, acc = model.evaluate(X_test, y_test)
print("Acurácia:", acc)

# =====================
# Overfitting check
# =====================

train_loss = history.history['loss']
val_loss = history.history['val_loss']

diff = np.mean(np.array(val_loss) - np.array(train_loss))

print("Diferença média:", diff)

# =====================
# Modelo com Sigmoid
# =====================

model_sigmoid = Sequential()
model_sigmoid.add(Dense(16, activation='sigmoid', input_shape=(X.shape[1],)))
model_sigmoid.add(Dense(8, activation='sigmoid'))
model_sigmoid.add(Dense(1, activation='sigmoid'))

model_sigmoid.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

history_sigmoid = model_sigmoid.fit(
    X_train, y_train,
    epochs=7,
    validation_data=(X_test, y_test),
    verbose=0
)

# =====================
# Comparação
# =====================

print("ReLU val_loss:", history.history['val_loss'][-1])
print("Sigmoid val_loss:", history_sigmoid.history['val_loss'][-1])

# =====================
# Regressão Logística
# =====================

lr = LogisticRegression()
lr.fit(X_train, y_train)

y_pred = lr.predict(X_test)
acc_lr = accuracy_score(y_test, y_pred)

print("Acurácia Regressão Logística:", acc_lr)