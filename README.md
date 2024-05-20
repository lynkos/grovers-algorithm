<div align="center">
<h1>Grover's Algorithm</h1>
<img alt="Python" src="https://img.shields.io/static/v1?label=Language&style=flat&message=Python+3.10.13&logo=python&color=c7a228&labelColor=393939&logoColor=4f97d1">
<img alt="Jupyter" src="https://img.shields.io/static/v1?label=Packages&style=flat&message=Jupyter&logo=jupyter&color=f37626&labelColor=393939&logoColor=f37626">
<img alt="Qiskit" src="https://img.shields.io/static/v1?label=Packages&style=flat&message=Qiskit&logo=qiskit&color=6929c4&labelColor=393939&logoColor=af7afa">
<img alt="Shell" src="https://img.shields.io/static/v1?label=Shell&style=flat&message=Bash&logo=gnu+bash&color=4EAA25&labelColor=393939&logoColor=4EAA25">
<img alt="Code+Editor" src="https://img.shields.io/static/v1?label=IDE&style=flat&message=Visual+Studio+Code&logo=visual+studio+code&color=007acc&labelColor=393939&logoColor=007acc">
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

> [!TIP]
> If you have trouble deciding between Anaconda and Miniconda, please refer to the table below
> <table>
>  <thead>
>   <tr>
>    <th><center>Anaconda</center></th>
>    <th><center>Miniconda</center></th>
>   </tr>
>  </thead>
>  <tbody>
>   <tr>
>    <td>New to conda and/or Python</td>
>    <td>Familiar with conda and/or Python</td>
>   </tr>
>   <tr>
>    <td>Not familiar with using terminal and prefer GUI</td>
>    <td>Comfortable using terminal</td>
>   </tr>
>   <tr>
>    <td>Like the convenience of having Python and 1,500+ scientific packages automatically installed at once</td>
>    <td>Want fast access to Python and the conda commands and plan to sort out the other programs later</td>
>   </tr>
>   <tr>
>    <td>Have the time and space (a few minutes and 3 GB)</td>
>    <td>Don't have the time or space to install 1,500+ packages</td>
>   </tr>
>   <tr>
>    <td>Don't want to individually install each package</td>
>    <td>Don't mind individually installing each package</td>
>   </tr>
>  </tbody>
> </table>
>
> Typing out entire Conda commands can sometimes be tedious, so I wrote a shell script ([`conda_shortcuts.sh` on GitHub Gist](https://gist.github.com/lynkos/7a4ce7f9e38bb56174360648461a3dc8)) to define shortcuts for commonly used Conda commands.
> <details>
>   <summary>Example: Delete/remove a conda environment named <code>test_env</code></summary>
>
> * Shortcut command
>     ```
>     rmenv test_env
>     ```
> * Manually typing out the entire command
>     ```sh
>     conda env remove -n test_env && rm -rf $(conda info --base)/envs/test_env
>     ```
>
> The shortcut has 80.8% fewer characters!
> </details>

## Installation
1. Verify that conda is installed
   ```
   conda --version
   ```
2. Ensure conda is up to date
   ```
   conda update conda
   ```
3. Enter the directory where you want the repository ([`grovers-algorithm`](https://github.com/lynkos/grovers-algorithm)) to be cloned
     * POSIX
       ```sh
       cd ~/path/to/directory
       ```
     * Windows
       ```sh
       cd C:\Users\user\path\to\directory
       ```
4. Clone the repository ([`grovers-algorithm`](https://github.com/lynkos/grovers-algorithm)), then enter its directory
   ```
   git clone https://github.com/lynkos/grovers-algorithm.git && cd grovers-algorithm
   ```
5. Create a conda virtual environment from [`environment.yml`](environment.yml)
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
### [`grovers_algorithm.py`](grovers_algorithm.py)
#### Command Line (Recommended)
1. Run [`grovers_algorithm.py`](grovers_algorithm.py)
   * POSIX
      ```sh
      python grovers_algorithm.py
      ```
   * Windows
      ```sh
      python grovers_algorithm.py
      ```

   <details open>
      <summary>Command Line Arguments</summary>
      <table align="center" style="width: 100%; text-align: center; display: block; max-width: -moz-fit-content; max-width: fit-content; overflow-x: auto;">
          <thead>
          <tr>
              <th><center>Option</center></th>
              <th><center>Type</center></th>
              <th><center>Description</center></th>
              <th><center>Default</center></th>
          </tr>
          </thead>
          <tbody>
          <tr>
              <td align="center" style="white-space: nowrap;"><code>-H, --help</code></td>
              <td align="center"></td>
              <td align="center">Show help message and exit</td>
              <td align="center"></td>
          </tr>
          <tr>
              <td align="center" style="white-space: nowrap;"><code>-T, --title &lt;title&gt;</code></td>
              <td align="center"><code>str</code></td>
              <td align="center">Window title</td>
              <td align="center">"Grover's Algorithm"</td>
          </tr>
          <tr>
              <td id="modpath" align="center" style="white-space: nowrap;"><code>-n, --n-qubits &lt;n_qubits&gt;</code></td>
              <td align="center"><code>int</code></td>
              <td align="center">Number of qubits</td>
              <td align="center"><code>5</code></td>
          </tr>
          <tr>
              <td align="center" style="white-space: nowrap;"><code>-s, --search &lt;search&gt;</code></td>
              <td align="center"><code>int</code></td>
              <td align="center">Nonnegative integers to search for</td>
              <td align="center"><code>11 9 0 3</code><br>(i.e., { 11, 9, 0, 3 })</td>
          </tr>
          <tr>
              <td align="center" style="white-space: nowrap;"><code>-S, --shots &lt;shots&gt;</code></td>
              <td align="center"><code>int</code></td>
              <td align="center">Number of simulations</td>
              <td align="center"><code>1000</code></td>
          </tr>
          <tr>
              <td align="center" style="white-space: nowrap;"><code>-f, --font-size &lt;font_size&gt;</code></td>
              <td align="center"><code>int</code></td>
              <td align="center">Histogram's font size</td>
              <td align="center"><code>10</code></td>
          </tr>
          <tr>
              <td align="center" style="white-space: nowrap;"><code>-p, --print</code></td>
              <td align="center"><code>bool</code></td>
              <td align="center">Whether or not to print quantum circuit(s)</td>
              <td align="center"><code>False</code></td>
          </tr>
          <tr>
              <td align="center" style="white-space: nowrap;"><code>-c, --combine</code></td>
              <td align="center"><code>bool</code></td>
              <td align="center">Whether to combine all non-winning states into 1 bar labeled "Others" or not</td>
              <td align="center"><code>False</code></td>
          </tr>
          </tbody>
      </table>
   </details>

2. Deactivate the virtual environment (`grovers_env`) when you're finished
   ```
   conda deactivate
   ```

#### Visual Studio Code
1. Open [`grovers_algorithm.py`](grovers_algorithm.py)
2. Run [`grovers_algorithm.py`](grovers_algorithm.py): Click `▷` (i.e. `Play` button) in the upper-right corner
3. Deactivate the virtual environment (`grovers_env`) when you're finished
   ```
   conda deactivate
   ```

### [`grovers_algorithm.ipynb`](grovers_algorithm.ipynb)
#### Visual Studio Code (Recommended)
1. Open the Command Palette with the relevant keyboard shortcut
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
4. Open [`grovers_algorithm.ipynb`](grovers_algorithm.ipynb)
5. Confirm `grovers_env` is the selected [kernel](https://docs.jupyter.org/en/latest/install/kernels.html)
6. Run [`grovers_algorithm.ipynb`](grovers_algorithm.ipynb) by clicking `Run All`
7. Deactivate the virtual environment (`grovers_env`) when you're finished
   ```
   conda deactivate
   ```

#### Command Line
1. Install `ipykernel` in the virtual environment (`grovers_env`)
   ```
   conda install -n grovers_env ipykernel
   ```
2. Add the virtual environment (`grovers_env`) as a Jupyter kernel
   ```
   python -m ipykernel install --user --name=grovers_env
   ```
3. Open [`grovers_algorithm.ipynb`](grovers_algorithm.ipynb) in the currently running notebook server, starting one if necessary
   ```
   jupyter notebook grovers_algorithm.ipynb
   ```
4. Select the virtual environment (`grovers_env`) as the kernel before running [`grovers_algorithm.ipynb`](grovers_algorithm.ipynb)
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
* [Using Jupyter Notebooks in Visual Studio Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)

## License
Distributed under the [MIT License](LICENSE.md), Copyright © 2024 Kiran Brahmatewari
