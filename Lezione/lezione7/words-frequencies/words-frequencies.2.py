import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download delle stop words
import nltk
nltk.download('stopwords')
nltk.download('punkt')

# Funzione per ottenere le prime N parole con maggiore frequenza da un testo


def get_top_words(text, n):
    # Tokenizzazione delle parole
    words = word_tokenize(text)

    # Rimozione di stop words e simboli di interpunzione
    stop_words = set(stopwords.words('italian'))
    words = [word.lower() for word in words if word.isalpha()
             and word.lower() not in stop_words]

    # Calcolo della frequenza delle parole
    words_freq = pd.Series(words).value_counts()

    # Ordinamento in base alla frequenza in senso decrescente
    words_freq = words_freq.sort_values(ascending=False)
    print(words_freq.index, words_freq.values)
    print(type(words_freq))

    return words_freq.head(n)

# Funzione principale per Streamlit


def main():
    st.title("Analisi di Frequenza delle Parole")

    # Caricamento del file di testo
    uploaded_file = st.file_uploader(
        "Carica un file di testo con codifica ISO", type=["txt"])

    if uploaded_file is not None:
        st.text("Contenuto del file:")
        # text = uploaded_file.read().decode("ISO-8859-1")
        text = uploaded_file.read().decode("utf-8")
        st.text_area("Testo", text, height=300)

        # Slider per selezionare il numero di parole da visualizzare
        num_words = st.slider(
            "Seleziona il numero di parole da visualizzare", 1, 40, 20)

        # Calcolo delle prime N parole con maggiore frequenza
        top_words = get_top_words(text, num_words)

        df_top_words = pd.DataFrame(
            {"Parola": top_words.index, "Frequenza": top_words.values})
        print(df_top_words)

        # Creare un diagramma a barre
        st.pyplot(draw_bar_chart(df_top_words))


def draw_bar_chart(df):
    fig, ax = plt.subplots()
    ax.bar(df["Parola"], df["Frequenza"])
    ax.set_xlabel("Parola")
    ax.set_ylabel("Frequenza")
    ax.set_title("Diagramma a Barre delle Parole più Frequenti")
    plt.xticks(rotation=90, ha="right")
    return fig


if __name__ == "__main__":
    main()
