import streamlit as st
from streamlit_chat import message
from bardapi import Bard
token='token_value'
#fun to create respond
def generate_response(prompt):
    bard = Bard(token=token)
    response = bard.get_answer(prompt)['content']
    return response
#fun ti receive input
def get_text():
    input_text=st.text_input('CBot:','Hey!',key='input')
    return input_text
st.title('Chat Master')

#to change the background u need the url of image and the placeholder
changes = '''
<style>
[data-testid = "stAppViewContainer"]
    {
    background-image:url('https://c1.wallpaperflare.com/preview/569/469/165/whatsapp-emoji-smiley-zo-tangible-al.jpg');
    background-size:cover;
    }
</style>
'''
#to commit the changes
st.markdown(changes,unsafe_allow_html=True)

if 'generated' not in st.session_state:
    st.session_state['generated']=[]
if 'past' not in st.session_state:
    st.session_state['past']=[]


user_input=get_text()
if user_input:
    print(user_input)
    output=generate_response(user_input)
    print(output)
    st.session_state['past'].append(user_input)
    st.session_state['generated'].append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1,-1,-1):
        message(st.session_state['generated'][i],key=str(i))
        message(st.session_state['past'][i],key="user_"+str(i),is_user=True)



