# Grover's Algorithm
![](https://img.shields.io/static/v1?label=Language&message=Python+3.10.9&logo=python&color=yellow&labelColor=393939&logoColor=white)
![](https://img.shields.io/static/v1?label=Kernel&message=Anaconda3&logo=anaconda&color=39ae39&labelColor=393939&logoColor=white)
![](https://img.shields.io/static/v1?label=IDE&message=Visual+Studio+Code&logo=visual+studio+code&color=blue&labelColor=393939&logoColor=white)

Python implementation of Grover's Algorithm aka Quantum Search Algorithm.

## Requirements
- [ ] [Python 3.7+](https://www.python.org/downloads) (preferably Python's latest version)
- [ ] [Jupyter](https://docs.jupyter.org/en/latest/install/notebook-classic.html)
- [ ] [Qiskit](https://qiskit.org/documentation/getting_started.html)

## Installation
### Set Up Virtual Environment (Optional)
> **Warning**
> It's highly recommended that you setup a [virtual environment](https://docs.python.org/3.10/tutorial/venv.html) before installing packages with [`pip`](https://pip.pypa.io/en/stable/installation)
1. Decide which directory you want to place it in and run `venv`
      * UNIX
      ```
      python -m venv /path/to/virtual/environment
      ```
      * Windows, if you've configured `PATH` and `PATHEXT` variables for your Python installation
      ```
      python -m venv c:\path\to\virtual\environment
      ```
      * Windows, if you haven't configured `PATH` and `PATHEXT`
      ```
      c:\Python35\python -m venv c:\path\to\virtual\environment
      ```
> **Note**
> If `python` doesn't work, try using `python3`

2. Activate your virtual environment
<table>
<thead>
<tr><th>Platform</th>
<th>Shell</th>
<th>Command to activate virtual environment</th>
</tr>
</thead>
<tbody>
<tr><td rowspan="4">POSIX</td>
<td>bash/zsh</td>
<td>

```
source /path/to/virtual/environment/bin/activate
```
</td>
</tr>
<tr><td>fish</td>
<td>

```
source /path/to/virtual/environment/bin/activate.fish
```
</td>
</tr>
<tr><td>csh/tcsh</td>
<td>

```
source /path/to/virtual/environment/bin/activate.csh
```
</td>
</tr>
<tr><td>PowerShell</td>
<td>

```
source /path/to/virtual/environment/bin/Activate.ps1
```
</td>
</tr>
<tr><td rowspan="2">Windows</td>
<td>cmd.exe</td>
<td>

```
c:\path\to\virtual\environment\Scripts\activate.bat
```
</td>
</tr>
<tr><td>PowerShell</td>
<td>

```
c:\path\to\virtual\environment\Scripts\Activate.ps1
```
</td>
</tr>
</tbody>
</table>
3. Deactivate your virtual environment whenever you're ready

```
deactivate
```

### Install Jupyter and Qiskit
> **Warning**
> Jupyter installation requires Python 3.3 or greater, or Python 2.7
1. Make sure you have the latest version of `pip`
```
pip install --upgrade pip
```
2. Install Jupyter
```
pip install jupyter
```
3. Install Qiskit
```
pip install qiskit
```
4. If the packages were installed correctly, Qiskit and Jupyter should show up in your virtual environment's active packages list
```
pip list
```

> **Note**
> If `pip` doesn't work, try using `pip3`

## Usage
1. Download `Grovers-Algorithm.ipynb` and `requirements.txt` to your computer
2. Install necessary packages
```
pip install -r requirements.txt
```
> **Note**
> If `requirements.txt` is in different directory than the one you're currently in, specify its path like `/path/to/requirements.txt`
3. Decide how you want to run `Grovers-Algorithm.ipynb` and follow the appropriate steps

### [Visual Studio Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)
1. Open Visual Studio Code
    * If you downloaded Anaconda, open `Anaconda Navigator`, scroll down to `VS Code`, then click `Launch`
    * If not, open Visual Studio Code as you normally do
2. [Set up and activate your environment](https://py-vscode.readthedocs.io/en/latest/files/venv.html) (Anaconda or another Python environment in which you've installed Jupyter)
3. Select environment (using the `Python: Select Interpreter` command from the Command Palette)
4. Open `Grovers-Algorithm.ipynb`
5. Click on `Select Kernel` to choose a kernel (preferably Anaconda3)
6. Click on `Run All` to run all cells

### Jupyter Notebook
```
jupyter notebook Grovers-Algorithm.ipynb
```

## Resources
* [Anaconda Documentation](https://docs.anaconda.com)
* [Anaconda Distribution Documentation](https://docs.continuum.io/free/anaconda)
* [Conda Documentation](https://docs.conda.io/en/latest)
* [Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/en/latest)
* [Jupyter Project Documentation](https://docs.jupyter.org/en/latest/index.html) [[PDF](https://buildmedia.readthedocs.org/media/pdf/jupyter/latest/jupyter.pdf)]
* [Technical Support - Jupyter Google Group](https://discourse.jupyter.org)
* [Qiskit Documentation](https://qiskit.org/documentation/index.html)
* [Requirements Files](https://pip.pypa.io/en/latest/user_guide/#requirements-files)
