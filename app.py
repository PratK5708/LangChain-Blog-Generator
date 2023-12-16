import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

#Function to get response
def getCreativeResponse(input_text, no_words, blog_style):
    llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type='llama',
                        config={'max_new_tokens': 256,
                                'temperature': 0.01})

    template = """
        Imagine you are writing a captivating blog post for {blog_style} professionals about {input_text}.
        The goal is to engage your readers with a story or anecdote. Your post should be around {no_words} words.
        """

    prompt = PromptTemplate(input_variables=["blog_style", "input_text", 'no_words'],
                            template=template)

    response = llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
    return response

#set page config
st.set_page_config(
    page_title="Creative Blog Generator",
    page_icon='✨',
    layout='wide',
    initial_sidebar_state='collapsed'
)

st.title("Creative Blog Generator ✨")
st.subheader("Generate unique and captivating blog content with AI")


input_text = st.text_input("Enter the Blog Topic")

#creating two more columns for additional two fields
col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input('No of Words')
with col2:
    blog_style = st.selectbox('Writing the blog for',
                              ('Researchers', 'Data Scientist', 'Common People'), index=0)

#spinner
submit = st.button("Generate")

if submit:
    with st.spinner("Generating..."):
        result = getCreativeResponse(input_text, no_words, blog_style)
    
    st.success("Blog generated successfully!")
    st.write(result)
