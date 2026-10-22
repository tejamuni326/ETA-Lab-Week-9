import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

st.set_page_config(page_title="Iris Prediction")
st.title("Lab 8: Iris Flower Prediction")
st.write("Adjust the measurements to predict the Iris species.")

iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
accuracy = accuracy_score(y_test, model.predict(X_test))

st.sidebar.header("Flower Measurements")
sepal_length = st.sidebar.slider("Sepal length (cm)", 4.0, 8.0, 5.1, 0.1)
sepal_width = st.sidebar.slider("Sepal width (cm)", 2.0, 4.5, 3.5, 0.1)
petal_length = st.sidebar.slider("Petal length (cm)", 1.0, 7.0, 1.4, 0.1)
petal_width = st.sidebar.slider("Petal width (cm)", 0.1, 2.5, 0.2, 0.1)

sample = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]], columns=iris.feature_names)
prediction = int(model.predict(sample)[0])
st.subheader("Prediction")
st.success(f"Predicted species: {iris.target_names[prediction].title()}")
st.write(f"Test accuracy on this split: {accuracy:.2%}")
st.write("Input measurements")
st.dataframe(sample, use_container_width=True)
