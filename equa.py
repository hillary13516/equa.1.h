import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


# ==============================
# CONFIGURAÇÃO DA PÁGINA
# ==============================

st.set_page_config(
    page_title="Equação do 1º Grau",
    page_icon="📈",
    layout="centered"
)


# ==============================
# CAMINHO DA IMAGEM
# ==============================

PASTA_APP = Path(__file__).parent
CAMINHO_LOGO = PASTA_APP / "mat.jpeg.jpeg"


# ==============================
# EXIBE A IMAGEM
# ==============================

if CAMINHO_LOGO.exists():

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.image(
            str(CAMINHO_LOGO),
            use_container_width=True
        )

else:

    st.warning(
        "A imagem 'mat.jpeg.jpeg' não foi encontrada. ⚠️"
    )


# ==============================
# TÍTULO
# ==============================

st.title("Equação do 1º Grau 📈")

st.write("Digite os valores da equação:")

st.latex(r"ax + b = 0")


# ==============================
# ENTRADA DOS VALORES
# ==============================

a = st.number_input(
    "Digite o valor de a",
    value=1.0,
    step=1.0
)

b = st.number_input(
    "Digite o valor de b",
    value=0.0,
    step=1.0
)


# ==============================
# BOTÃO CALCULAR
# ==============================

if st.button("Calcular", use_container_width=True):

    # --------------------------
    # CASO a = 0
    # --------------------------

    if a == 0:

        # 0x + 0 = 0
        if b == 0:

            st.warning(
                "A equação possui infinitas soluções."
            )

        # 0x + b = 0
        else:

            st.error(
                "A equação não possui solução."
            )


    # --------------------------
    # CASO a ≠ 0
    # --------------------------

    else:

        # Calcula a raiz
        x_raiz = -b / a


        # ======================
        # RESULTADO
        # ======================

        st.subheader("Resultado ✅")

        st.write("A raiz da equação é:")

        st.success(
            f"x = {x_raiz:.2f}"
        )


        # ======================
        # EQUAÇÃO
        # ======================

        st.subheader("Equação")

        if b >= 0:

            st.latex(
                rf"{a:g}x + {b:g} = 0"
            )

        else:

            st.latex(
                rf"{a:g}x - {abs(b):g} = 0"
            )


        # ======================
        # RESOLUÇÃO
        # ======================

        st.subheader("Resolução")

        # Primeira linha
        if b >= 0:

            st.latex(
                rf"{a:g}x + {b:g} = 0"
            )

        else:

            st.latex(
                rf"{a:g}x - {abs(b):g} = 0"
            )


        # Segunda linha
        st.latex(
            rf"{a:g}x = {-b:g}"
        )


        # Terceira linha
        st.latex(
            rf"x = \frac{{{-b:g}}}{{{a:g}}}"
        )


        # Resultado
        st.latex(
            rf"x = {x_raiz:.2f}"
        )


        # ======================
        # GRÁFICO
        # ======================

        st.subheader("Gráfico da função 📊")


        # Valores de x
        x = np.linspace(
            x_raiz - 10,
            x_raiz + 10,
            500
        )


        # Valores de y
        y = a * x + b


        # Cria o gráfico
        fig, ax = plt.subplots(
            figsize=(8, 5)
        )


        # Linha da função
        ax.plot(
            x,
            y,
            color="blue",
            linewidth=2,
            label=rf"$y = {a:g}x + {b:g}$"
        )


        # Eixo X
        ax.axhline(
            y=0,
            color="black",
            linewidth=1
        )


        # Eixo Y
        ax.axvline(
            x=0,
            color="black",
            linewidth=1
        )


        # Ponto da raiz
        ax.scatter(
            [x_raiz],
            [0],
            color="red",
            s=100,
            zorder=5,
            label=f"Raiz: x = {x_raiz:.2f}"
        )


        # Configurações
        ax.set_xlabel("x")
        ax.set_ylabel("y")

        ax.set_title(
            "Gráfico da Função do 1º Grau"
        )

        ax.grid(True)

        ax.legend()


        # Exibe o gráfico
        st.pyplot(fig)


        # Fecha a figura
        plt.close(fig)


# ==============================
# RODAPÉ
# ==============================

st.divider()

st.caption(
    "Calculadora de Equação do 1º Grau 📚"
)
