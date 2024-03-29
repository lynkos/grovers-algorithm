<div align="center">
<h1>Grover's Algorithm</h1>
<img alt="Python" src="https://img.shields.io/static/v1?label=Language&style=flat&message=Python+3.10.13&logo=python&color=c7a228&labelColor=393939&logoColor=4f97d1">
<img alt="Jupyter" src="https://img.shields.io/static/v1?label=Packages&style=flat&message=Jupyter&logo=jupyter&color=f37626&labelColor=393939&logoColor=f37626">
<img alt="Qiskit" src="https://img.shields.io/static/v1?label=Packages&style=flat&message=Qiskit&logo=qiskit&color=6929c4&labelColor=393939&logoColor=af7afa">
<img alt="Shell" src="https://img.shields.io/static/v1?label=Shell&style=flat&message=Bash&logo=gnu+bash&color=4EAA25&labelColor=393939&logoColor=4EAA25">
<img alt="IDE" src="https://img.shields.io/static/v1?label=IDE&style=flat&message=Visual+Studio+Code&logo=visual+studio+code&color=007acc&labelColor=393939&logoColor=007acc">
</div>

<div align="center">
<img alt="License" src="https://img.shields.io/github/license/lynkos/grovers-algorithm?style=flat&label=License&labelColor=393939&color=788200&link=https%3A%2F%2Fgithub.com%2Flynkos%2Fgrovers-algorithm%2Fblob%2Fmaster%2FLICENSE.md">
<img alt="Last Commit" src="https://img.shields.io/github/last-commit/lynkos/grovers-algorithm?style=flat&label=Last+Commit&labelColor=393939&color=be0000">
<img alt="Commit Activity" src="https://img.shields.io/github/commit-activity/y/lynkos/grovers-algorithm?style=flat&label=Commit+Activity&labelColor=393939&color=b30086">
<img alt="Repo Size" src="https://img.shields.io/github/repo-size/lynkos/grovers-algorithm?style=flat&label=Repo+Size&labelColor=393939&color=ff62b1">
</div>

---

<p align="center">
 ⭐️⭐️⭐️ Please <a target="_blank" href="https://github.com/lynkos/grovers-algorithm">star</a> this repo if you find it helpful, interesting, or useful! ⭐️⭐️⭐️
</p>

---

## Requirements
- [x] [Anaconda](https://docs.continuum.io/free/anaconda/install) **OR** [Miniconda](https://docs.conda.io/projects/miniconda/en/latest)
> [!NOTE]
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
> <td>New to conda and/or Python</td>
> <td>Familiar with conda and/or Python</td>
> </tr>
> <tr>
> <td>Like the convenience of having Python and 1,500+ scientific packages automatically installed at once</td>
> <td>Want fast access to Python and the conda commands and plan to sort out the other programs later</td>
> </tr>
> <tr>
> <td>Have the time and space (a few minutes and 3 GB)</td>
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
4. Clone the repository (`grovers-algorithm`), then enter its directory
   ```
   git clone https://github.com/lynkos/grovers-algorithm.git && cd grovers-algorithm
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
     * If active, the virtual environment's name should be in parentheses () or brackets [] before your command prompt, e.g.
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
    * Mac
      ```
      ⌘ + Shift + P
      ```
    * Windows
      ```
      CTRL + Shift + P
      ```
2. Search and select `Python: Select Interpreter`
3. Select the virtual environment (`grovers_env`)
4. Open `Grovers-Algorithm.ipynb` and/or `Grovers-Algorithm.py`
5. Confirm `grovers_env` is the selected [kernel](https://docs.jupyter.org/en/latest/install/kernels.html)
6. Run program(s)
   * `Grovers-Algorithm.ipynb`: Click `Run All`
   * `Grovers-Algorithm.py`: Click `▷` (i.e. `Play` button) in the upper-right corner
7. Deactivate the virtual environment (`grovers_env`) when you're finished
   ```
   conda deactivate
   ```

### Command Line
#### Python
1. Run `Grovers-Algorithm.py`
   * UNIX
      ```
      $(which python) Grovers-Algorithm.py
      ```
   * Windows
      ```
      $(where python) Grovers-Algorithm.py
      ```
2. Deactivate the virtual environment (`grovers_env`) when you're finished
   ```
   conda deactivate
   ```

#### Jupyter Notebook
1. Install `ipykernel` in the virtual environment (`grovers_env`)
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

## License
Distributed under the [MIT License](LICENSE.md), Copyright © 2023 Kiran Brahmatewari
