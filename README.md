# Grover's Algorithm
![](https://img.shields.io/static/v1?label=Language&style=flat&message=Python+3.10.9&logo=python&color=c7a228&labelColor=393939&logoColor=4f97d1)
![](https://img.shields.io/static/v1?label=Packages&style=flat&message=Jupyter+Notebook&logo=jupyter&color=f37626&labelColor=393939&logoColor=f37626)
![](https://img.shields.io/static/v1?label=Packages&style=flat&message=Qiskit&logo=qiskit&color=6929c4&labelColor=393939&logoColor=af7afa)
![](https://img.shields.io/static/v1?label=Kernel&style=flat&message=Anaconda+3&logo=anaconda&color=44a833&labelColor=393939&logoColor=44a833)
![](https://img.shields.io/static/v1?label=IDE&style=flat&message=Visual+Studio+Code&logo=visual+studio+code&color=007acc&labelColor=393939&logoColor=007acc)

## Requirements
- [x] [Python](https://www.python.org/downloads)
- [x] [Anaconda](https://docs.continuum.io/free/anaconda/install) **OR** [Miniconda](https://docs.conda.io/projects/miniconda/en/latest)
> [!IMPORTANT]
> If you have trouble deciding between Anaconda and Miniconda, please refer to the table below
> <table>
> <thead>
> <tr>
> <th><center>Anaconda</center></th>
> <th><center>Miniconda</center></th>
> </tr>
> </thead>
> <tbody>
> <tr>
> <td>Are new to conda and/or Python</td>
> <td>Are familiar with conda and/or Python</td>
> </tr>
> <tr>
> <td>Like the convenience of having Python and 1,500+ scientific packages automatically installed at once</td>
> <td>Want fast access to Python and the conda commands and plan to sort out the other programs later</td>
> </tr>
> <tr>
> <td>Have the time and space — a few minutes and 3 GB</td>
> <td>Don't have the time or space to install 1,500+ packages</td>
> </tr>
> <tr>
> <td>Don't want to individually install each package</td>
> <td>Don't mind individually installing each package</td>
> </tr>
> </tbody>
> </table>

## Installation
1. Verify that conda is installed
     ```
     conda --version
     ```
2. Ensure conda is up to date
     ```
     conda update conda
     ```
3. Enter the directory where you want the repository (`grovers-algorithm`) to be cloned
     * Unix
          ```
          cd ~/path/to/directory
          ```
     * Windows
          ```
          cd C:\Users\user\path\to\directory
          ```
4. Clone the repository (`grovers-algorithm`)
     * HTTPS (Recommended)
          ```
          git clone https://github.com/lynkos/grovers-algorithm.git
          ```
     * SSH
          ```
          git clone git@github.com:lynkos/grovers-algorithm.git
          ```
     * GitHub CLI
          ```
          gh repo clone lynkos/grovers-algorithm
          ```
5. Create a conda virtual environment from `environment.yml`
     ```
     conda env create -f environment.yml
     ```
6. Activate the virtual environment (`grovers_env`)
     ```
     conda activate grovers_env
     ```
7. Confirm that the virtual environment (`grovers_env`) is active
     * If active, the virtual environment's name (`grovers_env`) should be in parentheses () or brackets [] before your command prompt, e.g.
          ```
          (grovers_env) $
          ```
     * If necessary, see which environments are available and/or currently active (active environment denoted with asterisk (*))
          ```
          conda info --envs
          ```
          **OR**
          ```
          conda env list
          ```

## Usage
### [Visual Studio Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) (Recommended)
1. Open the Command Palette in [Visual Studio Code](https://code.visualstudio.com/download) with the relevant keyboard shortcut
    * `⌘ + Shift + P` for Mac
    * `CTRL + Shift + P` for Windows
2. Search and select `Python: Select Interpreter`
3. Select the virtual environment (`grovers_env`)
4. Open `Grovers-Algorithm.ipynb`
5. Confirm `grovers_env` is the selected [kernel](https://docs.jupyter.org/en/latest/install/kernels.html)
6. Click `Run All` to run all cells
7. Deactivate the virtual environment (`grovers_env`) when you're finished
     ```
     conda deactivate
     ```

### Jupyter Notebook
1. After creating and activating the virtual environment (`grovers_env`) as detailed in [Installation](#installation), install `ipykernel` in the virtual environment (`grovers_env`)
     ```
     conda install -n grovers_env ipykernel
     ```
2. Add the virtual environment (`grovers_env`) as a Jupyter kernel
     ```
     python -m ipykernel install --user --name=grovers_env
     ```
3. Open `Grovers-Algorithm.ipynb` in the currently running notebook server, starting one if necessary
     ```
     jupyter notebook Grovers-Algorithm.ipynb
     ```
4. Select the virtual environment (`grovers_env`) as the kernel before running `Grovers-Algorithm.ipynb`
5. Deactivate the virtual environment (`grovers_env`) when you're finished
     ```
     conda deactivate
     ```

## Resources
* [Anaconda Documentation](https://docs.anaconda.com)
* [Conda Documentation](https://docs.conda.io/en/latest)
* [Getting Started with Conda](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html)
* [Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/en/latest)
* [Jupyter Project Documentation](https://docs.jupyter.org/en/latest/index.html) [[PDF](https://buildmedia.readthedocs.org/media/pdf/jupyter/latest/jupyter.pdf)]
* [Technical Support - Jupyter Google Group](https://discourse.jupyter.org)
* [Qiskit Documentation](https://qiskit.org/documentation/index.html)
* [Documentation for Visual Studio Code](https://code.visualstudio.com/docs)

## Contact
For all questions, bugs, suggestions, etc. relating to this project, please create an [issue](https://github.com/lynkos/grovers-algorithm/issues/new) with a relevant label/tag. For all other queries, feel free to reach out via:<br>

<a href="https://twitter.com/0xLynkos" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/6/6f/Logo_of_Twitter.svg" width="31px" height="27px" alt="Twitter" /></a>&nbsp; <a href="mailto:kiwi2mii@gmail.com" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/7/7e/Gmail_icon_%282020%29.svg" width="28px" height="28px" alt="Gmail" /></a> &nbsp; <a href="https://www.linkedin.com/in/kiran-brahmatewari" target="_blank"><img src="https://cdn.worldvectorlogo.com/logos/linkedin-icon-2.svg" width="28px" height="28px" alt="LinkedIn" /></a>

<sup>Note: Timely response is not guaranteed!</sup>

## Show Support
Please :star: [star](https://github.com/lynkos/grovers-algorithm) :star: this repo if you find it helpful or useful!

## License
Distributed under the [MIT License](https://github.com/lynkos/grovers-algorithm/blob/main/LICENSE.md), Copyright © 2023 Kiran Brahmatewari
