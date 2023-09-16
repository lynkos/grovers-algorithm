# Grover's Algorithm
![](https://img.shields.io/static/v1?label=Language&style=flat&message=Python+3.10.9&logo=python&color=c7a228&labelColor=393939&logoColor=4f97d1)
![](https://img.shields.io/static/v1?label=Packages&style=flat&message=Jupyter+Notebook&logo=jupyter&color=f37626&labelColor=393939&logoColor=f37626)
![](https://img.shields.io/static/v1?label=Packages&style=flat&message=Qiskit&logo=qiskit&color=6929c4&labelColor=393939&logoColor=af7afa)
![](https://img.shields.io/static/v1?label=Kernel&style=flat&message=Anaconda+3&logo=anaconda&color=44a833&labelColor=393939&logoColor=44a833)
![](https://img.shields.io/static/v1?label=IDE&style=flat&message=Visual+Studio+Code&logo=visual+studio+code&color=007acc&labelColor=393939&logoColor=007acc)

## Requirements
- [x] [Python 3.7+](https://www.python.org/downloads) (preferably latest version)
- [x] [Pip](https://pip.pypa.io/en/stable/installation)
- [x] [Jupyter](https://docs.jupyter.org/en/latest/install/notebook-classic.html)
- [x] [Qiskit](https://qiskit.org/documentation/getting_started.html)

## Setting Up (Optional)
> **Warning**
> It's highly recommended that you set up a [virtual environment](https://docs.python.org/3.10/tutorial/venv.html) before using pip
1. Create your virtual environment
      * UNIX
      ```
      python -m venv /path/to/virtual/environment
      ```
      * Windows
      ```
      python -m venv c:\path\to\virtual\environment
      ```
     > **Note**
     > If `python` doesn't work, try using `python3`<br><br>
     > If you haven't configured `PATH` and `PATHEXT` in Windows, replace `python` with `c:\Python35\python`

1. Activate your virtual environment
     <table>
     <thead>
     <tr><th>Platform</th>
     <th>Shell</th>
     <th>Command</th>
     </tr>
     </thead>
     <tbody>
     <tr><td rowspan="4">POSIX</td>
     <td>bash/zsh</td>
     <td><p style="margin-bottom: 0px">

     ```
     source /path/to/virtual/environment/bin/activate
     ```
     </p></td>
     </tr>
     <tr><td>fish</td>
     <td><p style="margin-bottom: 0px">

     ```
     source /path/to/virtual/environment/bin/activate.fish
     ```
     </p></td>
     </tr>
     <tr><td>csh/tcsh</td>
     <td><p style="margin-bottom: 0px">

     ```
     source /path/to/virtual/environment/bin/activate.csh
     ```
     </p></td>
     </tr>
     <tr><td>PowerShell</td>
     <td><p style="margin-bottom: 0px">

     ```
     source /path/to/virtual/environment/bin/Activate.ps1
     ```
     </p></td>
     </tr>
     <tr><td rowspan="2">Windows</td>
     <td>cmd.exe</td>
     <td><p style="margin-bottom: 0px">

     ```
     c:\path\to\virtual\environment\Scripts\activate.bat
     ```
     </p></td>
     </tr>
     <tr><td>PowerShell</td>
     <td><p style="margin-bottom: 0px">

     ```
     c:\path\to\virtual\environment\Scripts\Activate.ps1
     ```
     </p></td>
     </tr>
     </tbody>
     </table>

## Installation
> **Warning**
> Jupyter and Qiskit installation requires Python 3.7+
1. Pip
     * If you haven't already, install pip via Python's [`ensurepip`](https://docs.python.org/3/library/ensurepip.html) module
     ```
     python -m ensurepip --upgrade
     ```
     * If you already have pip, ensure you have the latest version
     ```
     pip install --upgrade pip
     ```
2. Install/update Jupyter and Qiskit
     ```
     pip install --upgrade jupyter qiskit qiskit[visualization] qiskit[quantum_info]
     ```
     > **Note**
     > If you're using zsh, you'll need to put `qiskit[visualization]` and `qiskit[quantum_info]` in quotes
3. If the packages were installed/updated correctly, the latest version of Jupyter and Qiskit should show up in your virtual environment's active packages list
     ```
     pip list
     ```
     > **Note**
     > If `pip` doesn't work, try using `pip3` and/or adding `python -m` or `python3 -m` before `pip`
4. Download `Grovers-Algorithm.ipynb`

## Usage
### [Visual Studio Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) (Recommended)
1. Open Visual Studio Code
    * If you downloaded [Anaconda](https://www.anaconda.com/download), open `Anaconda Navigator`, scroll down to `VS Code`, then click `Launch`
    * If not, open [Visual Studio Code](https://code.visualstudio.com/download) as you normally do
2. Set up a [virtual environment](https://py-vscode.readthedocs.io/en/latest/files/venv.html), if you haven't already
3. Open the Command Palette with the relevant keyboard shortcut
    * `⌘ + Shift + P` for Mac
    * `CTRL + Shift + P` for Windows
4. Search and select `Python: Select Interpreter`
5. Select your virtual environment
6. Open `Grovers-Algorithm.ipynb`
7. Click `Select Kernel` and choose a [kernel](https://docs.jupyter.org/en/latest/install/kernels.html)
8. Click `Run All` to run all cells
9. Deactivate your virtual environment when you're finished
     ```
     deactivate
     ```

### Jupyter Notebook
1. Open `Grovers-Algorithm.ipynb` in the currently running notebook server, starting one if necessary
     ```
     jupyter notebook Grovers-Algorithm.ipynb
     ```
2. Run `Grovers-Algorithm.ipynb`
     ```
     jupyter run Grovers-Algorithm.ipynb
     ```

## Resources
* [Anaconda Documentation](https://docs.anaconda.com)
* [Anaconda Distribution Documentation](https://docs.continuum.io/free/anaconda)
* [Conda Documentation](https://docs.conda.io/en/latest)
* [Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/en/latest)
* [Jupyter Project Documentation](https://docs.jupyter.org/en/latest/index.html) [[PDF](https://buildmedia.readthedocs.org/media/pdf/jupyter/latest/jupyter.pdf)]
* [Technical Support - Jupyter Google Group](https://discourse.jupyter.org)
* [Qiskit Documentation](https://qiskit.org/documentation/index.html)
* [Documentation for Visual Studio Code](https://code.visualstudio.com/docs)
