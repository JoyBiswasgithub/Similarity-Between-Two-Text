import streamlit as st
import difflib
from difflib import SequenceMatcher

def calculate_similarity(text1, text2):
    # Calculate the similarity ratio between the two texts
    similarity_ratio = SequenceMatcher(None, text1, text2).ratio()
    similarity_percentage = round(similarity_ratio * 100, 2)
    return similarity_percentage

def highlight_differences(text1, text2):
    d = difflib.Differ()
    diff = list(d.compare(text1.split(), text2.split()))
    
    # Highlight differences
    highlighted_text1 = []
    highlighted_text2 = []
    
    for word in diff:
        if word.startswith('- '):
            highlighted_text1.append(f'<span style="background-color: #ffcccc">{word[2:]}</span>')
        elif word.startswith('+ '):
            highlighted_text2.append(f'<span style="background-color: #ccffcc">{word[2:]}</span>')
        elif word.startswith('  '):
            highlighted_text1.append(word[2:])
            highlighted_text2.append(word[2:])
    
    return ' '.join(highlighted_text1), ' '.join(highlighted_text2)

st.title("Text Similarity Checker")

text1 = st.text_area("Enter Text 1", height=150)
text2 = st.text_area("Enter Text 2", height=150)

if st.button("Compare"):
    if text1 and text2:
        similarity = calculate_similarity(text1, text2)
        st.write(f"**Similarity:** {similarity}%")
        
        highlighted_text1, highlighted_text2 = highlight_differences(text1, text2)
        
        st.markdown("### Text 1 with Differences Highlighted")
        st.markdown(f'<p style="font-family: monospace;">{highlighted_text1}</p>', unsafe_allow_html=True)
        
        st.markdown("### Text 2 with Differences Highlighted")
        st.markdown(f'<p style="font-family: monospace;">{highlighted_text2}</p>', unsafe_allow_html=True)
    else:
        st.write("Please enter both texts to compare.")

if st.button("Refresh"):
    st.experimental_rerun()
