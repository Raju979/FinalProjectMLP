import nbformat as nbf

def py_to_notebook(py_filename, notebook_filename):
    # Create a new notebook object
    nb = nbf.v4.new_notebook()
    with open(py_filename, 'r') as f:
        code = f.read()
    
    # Create a code cell with the contents of the Python script
    code_cell = nbf.v4.new_code_cell(code)
    nb.cells.append(code_cell)
    
    # Write the notebook to a new file
    with open(notebook_filename, 'w') as f:
        nbf.write(nb, f)

# Usage example
py_to_notebook('NextDay-240,1-RF.py', 'test_notebook.ipynb')
