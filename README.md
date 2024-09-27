# Text Similarity Checker

This is a Streamlit application that compares two texts, calculates the similarity percentage, and highlights the dissimilar words. It is a powerful tool for tasks that require text comparison, such as plagiarism detection, content revision, and more.

## 🚀 Deployment

You can try out the application live at the following link:

[**Text Similarity Checker - Live Demo**](https://text2textsimilarity.streamlit.app/)

## Working Principle

### 1. **Text Similarity Calculation:**
The application leverages Python's `difflib` library to calculate the similarity between two texts. Specifically, it uses the `SequenceMatcher` class, which computes a ratio indicating how closely two sequences (in this case, texts) resemble each other..

- **SequenceMatcher:** This algorithm works by finding the longest contiguous matching subsequence between the two texts, ignoring small differences like word order. The result is a similarity ratio between `0` and `1`, which is then converted into a percentage.

### 2. **Highlighting Differences:**
To identify and highlight the differences between the two texts, the application uses `difflib.Differ`. This tool generates a list of changes required to transform one text into the other. It categorizes changes as additions, deletions, or unchanged parts:

- **Deletions:** Words present in the first text but not in the second are highlighted in red.
- **Additions:** Words present in the second text but not in the first are highlighted in green.
- **Unchanged Words:** Words that are identical in both texts remain unhighlighted.

### 3. **Streamlit Interface:**
The user interface is built with Streamlit, a popular Python library for creating web applications. Streamlit allows users to interact with the application in real-time, input their texts, and instantly view the similarity results along with the highlighted differences.

## Use Cases

### 1. **Plagiarism Detection:**
Educators, researchers, and content creators can use this tool to detect plagiarism by comparing two documents. The similarity percentage provides a quick overview, while the highlighted differences make it easy to spot copied or paraphrased content.

### 2. **Content Revision and Editing:**
Writers and editors can compare different versions of a document to identify changes made during the revision process. The tool highlights exactly what has been added, removed, or modified, simplifying the editing workflow.

### 3. **Code Review and Comparison:**
In software development, this tool can be adapted to compare source code files, helping developers quickly identify differences between code versions or branches.

### 4. **Document Comparison:**
Legal professionals, contract managers, and other business users can compare contracts, agreements, or any other legal documents to ensure consistency and identify any alterations made between drafts.

### 5. **Language Translation Validation:**
When working with translations, this tool can compare the original text with its translation to ensure that the translated text closely matches the original. While the comparison won't check the accuracy of the translation, it can highlight structural differences.

