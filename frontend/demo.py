import os

import requests
import streamlit as st

REST_API_HOST = os.environ.get("REST_API_HOST", None)
REST_API_PORT = os.environ.get("REST_API_PORT", None)

if REST_API_HOST is None or REST_API_PORT is None:
    raise RuntimeError("These env variables should be present")


def _generate_text(prompt: str, temp: float, max_token_len: int) -> str:
    # TODO: EOS token inclusion
    url: str = f"http://{REST_API_HOST}:{REST_API_PORT}/generate/?prompt={prompt}&temperature={temp}&max_token_length={max_token_len}"
    res = requests.get(url).json()
    return res["generated_text"]


def app():
    st.set_page_config(layout="wide")
    st.title("GPT-J Demo")

    st.sidebar.title("Config")
    temperatre_input = st.sidebar.number_input(label="Temperature", min_value=0.0, max_value=1.0, value=0.7, step=0.01)
    max_token_len_input = st.sidebar.number_input(label="Max number of tokens",
                                                  min_value=1,
                                                  max_value=2000,
                                                  value=100,
                                                  step=1)
    nb_generated_texts = st.sidebar.number_input(label="Variations", min_value=1, max_value=10, value=1, step=1)
    st.sidebar.markdown(f"Created by *[Gabor Vecsei](https://gaborvecsei.com)*")

    # TODO: we'll need some optionslie temperatre


    st.header("The prompt")
    # User prompt textbox
    prompt_text_area = st.text_area("")

    # This is what triggers the generation
    send_button = st.button("Send")

    st.header("Generated result")

    if send_button:
        for _ in range(int(nb_generated_texts)):
            with st.spinner("loading..."):
                gen_text = _generate_text(prompt_text_area, float(temperatre_input), int(max_token_len_input))
                prompt_len = len(prompt_text_area)
                text_to_display = f"**[{gen_text[:prompt_len]}]**{gen_text[prompt_len:]}"
            st.markdown(text_to_display)
            st.markdown("-------------")


if __name__ == "__main__":
    app()
