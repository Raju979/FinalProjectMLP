import nbformat as nbf

def py_to_notebook(py_filename, notebook_filename):
    # Create a new notebook object
    nb = nbf.v4.new_notebook()
    with open(py_filename, 'r') as f:
        code = f.read()
    
    code_cell = nbf.v4.new_code_cell(code)
    nb.cells.append(code_cell)
    
    with open(notebook_filename, 'w') as f:
        nbf.write(nb, f)

py_to_notebook('NextDay-240,1-RF.py', 'Modified_NextDay-240,1-RF.ipynb')
py_to_notebook('NextDay-240,1-RF.py', 'Modified_NextDay-240,1-LSTM.ipynb')
