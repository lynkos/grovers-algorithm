from qiskit import QuantumCircuit as qc
from qiskit import QuantumRegister as qr
from qiskit import transpile
from qiskit.providers import Backend
from qiskit.result import Counts
from qiskit_ibm_runtime import QiskitRuntimeService
from matplotlib.pyplot import show, subplots, xticks, yticks
from matplotlib.backend_bases import MouseEvent
from math import pi, sqrt
from heapq import nlargest

"""Feel free to modify the following constants."""
N: int = 5                                # Number of qubits
SEARCH_VALUES: set[int] = { 11, 9, 0, 3 } # Set of m nonnegative integers to search for using Grover's algorithm (i.e. TARGETS in base 10)
SHOTS: int = 10000                        # Amount of times the algorithm is simulated
FONTSIZE: int = 10                        # Histogram's font size

"""Unless you know what you are doing, please do not modify the following constants, otherwise you risk breaking the program."""
TARGETS: set[str] = { f"{s:0{N}b}" for s in SEARCH_VALUES }     # Set of m N-qubit binary strings representing target state(s) (i.e. SEARCH_VALUES in base 2)
QUBITS: qr = qr(N, "qubit")                                     # N-qubit quantum register
BACKEND_NAME: str = "ibmq_qasm_simulator"                       # Name of backend to run the algorithm on
BACKEND: Backend = QiskitRuntimeService().backend(BACKEND_NAME) # Backend to run the algorithm on

def print_circuit(circuit: qc, name: str = "") -> None:
    """Print quantum circuit.

    Args:
        circuit (qc): Quantum circuit to print.
        name (str, optional): Quantum circuit's name. Defaults to None.
    """
    print(f"\n{name}:" if name else "")
    print(f"{circuit}")

def oracle(targets: set[str] = TARGETS, name: str = "Oracle", display_oracle: bool = True) -> qc:
    """Mark target state(s) with negative phase.

    Args:
        targets (set[str]): N-qubit binary string(s) representing target state(s). Defaults to TARGETS.
        name (str, optional): Quantum circuit's name. Defaults to "Oracle".
        display_oracle (bool, optional): Whether or not to display oracle. Defaults to True.

    Returns:
        qc: Quantum circuit representation of oracle.
    """
    # Create N-qubit quantum circuit for oracle
    oracle = qc(QUBITS, name = name)

    for target in targets:
        # Reverse target state since Qiskit uses little-endian for qubit ordering
        target = target[::-1]
        
        # Flip zero qubits in target
        for i in range(N):
            if target[i] == "0":
                oracle.x(i)                   # Pauli-X gate

        # Simulate (N - 1)-control Z gate
        oracle.h(N - 1)                       # Hadamard gate
        oracle.mcx(list(range(N - 1)), N - 1) # (N - 1)-control Toffoli gate
        oracle.h(N - 1)                       # Hadamard gate

        # Flip back to original state
        for i in range(N):
            if target[i] == "0":
                oracle.x(i)                   # Pauli-X gate

    # Display oracle, if applicable
    if display_oracle: print_circuit(oracle, "ORACLE")

    return oracle

def diffuser(name: str = "Diffuser", display_diffuser: bool = True) -> qc:
    """Amplify target state(s) amplitude, which decreases the amplitudes of other states
    and increases the probability of getting the correct solution (i.e. target state(s)).

    Args:
        name (str, optional): Quantum circuit's name. Defaults to "Diffuser".
        display_diffuser (bool, optional): Whether or not to display diffuser. Defaults to True.

    Returns:
        qc: Quantum circuit representation of diffuser (i.e. Grover's diffusion operator).
    """
    # Create N-qubit quantum circuit for diffuser
    diffuser = qc(QUBITS, name = name)

    diffuser.h(QUBITS)                                  # Hadamard gate
    diffuser.append(oracle({"0" * N}), list(range(N)))  # Oracle with all zero target state
    diffuser.h(QUBITS)                                  # Hadamard gate
    
    # Display diffuser, if applicable
    if display_diffuser: print_circuit(diffuser, "DIFFUSER")
    
    return diffuser

def grover(oracle: qc = oracle(), diffuser: qc = diffuser(), name: str = "Grover Circuit", display_grover: bool = True) -> qc:
    """Create quantum circuit representation of Grover's algorithm,
    which consists of 4 parts: (1) state preparation/initialization,
    (2) oracle, (3) diffuser, and (4) measurement of resulting state.
    
    Steps 2-3 are repeated an optimal number of times (i.e. Grover's
    iterate) in order to maximize probability of success of Grover's algorithm.

    Args:
        oracle (qc, optional): Quantum circuit representation of oracle. Defaults to oracle().
        diffuser (qc, optional): Quantum circuit representation of diffuser. Defaults to diffuser().
        name (str, optional): Quantum circuit's name. Defaults to "Grover Circuit".
        display_grover (bool, optional): Whether or not to display grover circuit. Defaults to True.

    Returns:
        qc: Quantum circuit representation of Grover's algorithm.
    """
    # Create N-qubit quantum circuit for Grover's algorithm
    grover = qc(QUBITS, name = name)
    
    # Intialize qubits with Hadamard gate (i.e. uniform superposition)
    grover.h(QUBITS)
    
    # # Apply barrier to separate steps
    grover.barrier()

    # Apply oracle and diffuser (i.e. Grover operator) optimal number of times
    for _ in range(int((pi / 4) * sqrt((2 ** N) / len(TARGETS)))):
        grover.append(oracle, list(range(N)))
        grover.append(diffuser, list(range(N)))
     
    # Measure all qubits once finished
    grover.measure_all()

    # Display grover circuit, if applicable
    if display_grover: print_circuit(grover, "GROVER CIRCUIT")
    
    return grover

def outcome(winners: list[str], counts: Counts) -> None:
    """Print top measurement(s) (state(s) with highest frequency)
    and target state(s) in binary and decimal form, determine
    if top measurement(s) equals target state(s), then print result.

    Args:
        winners (list[str]): State(s) (N-qubit binary string(s))
        with highest probability of being measured.
        counts (Counts): Each state and its respective frequency.
    """
    print("WINNER(S):")
    print(f"Binary = {winners}\nDecimal = {[ int(key, 2) for key in winners ]}\n")
        
    print("TARGET(S):")
    print(f"Binary = {TARGETS}\nDecimal = {SEARCH_VALUES}\n")

    if not all(key in TARGETS for key in winners): print("Target(s) not found...")

    else:
        winners_frequency, total = 0, 0

        for value, frequency in counts.items():
            if value in winners:
                winners_frequency += frequency
            total += frequency
        
        print(f"Target(s) found with {winners_frequency / total:.2%} accuracy!")

def display_results(results: Counts, combine_other_states: bool = True) -> None:
    """Print outcome and display histogram of simulation results.

    Args:
        results (Counts): Each state and its respective frequency.
        combine_other_states (bool, optional): Whether to combine all non-winning states into 1 bar
        labeled "Others" or not. Defaults to True.
    """
    # State(s) with highest count and their frequencies
    winners = { winner : results.get(winner) for winner in nlargest(len(TARGETS), results, key = results.get) }

    # Print outcome
    outcome(list(winners.keys()), results)

    # X-axis and y-axis value(s) for winners, respectively
    winners_x_axis = [ str(winner) for winner in [*winners] ]
    winners_y_axis = [ *winners.values() ]

    # All other states (i.e. non-winners) and their frequencies
    others = {state : frequency for state, frequency in results.items() if state not in winners}

    # X-axis and y-axis value(s) for all other states, respectively
    other_states_x_axis = "Others" if combine_other_states else [*others]
    other_states_y_axis = [ sum([*others.values()]) ] if combine_other_states else [ *others.values() ]

    # Create histogram for simulation results
    figure, axes = subplots(num = "Grover's Algorithm — Results", layout = "constrained")
    axes.bar(winners_x_axis, winners_y_axis, color = "green", label = "Target")
    axes.bar(other_states_x_axis, other_states_y_axis, color = "red", label = "Non-target")
    axes.legend(fontsize = FONTSIZE)
    axes.grid(axis = "y", ls = "dashed")
    axes.set_axisbelow(True)

    # Set histogram title, x-axis title, and y-axis title respectively
    axes.set_title(f"Outcome of {SHOTS} Simulations", fontsize = int(FONTSIZE * 1.45))
    axes.set_xlabel("States (Qubits)", fontsize = int(FONTSIZE * 1.3))
    axes.set_ylabel("Frequency", fontsize = int(FONTSIZE * 1.3))

    # Set font properties for x-axis and y-axis labels respectively
    xticks(fontsize = FONTSIZE, family = "monospace", rotation = 0 if combine_other_states else 70)
    yticks(fontsize = FONTSIZE, family = "monospace")
    
    # Set properties for annotations displaying frequency above each bar
    annotation = axes.annotate("",
                               xy = (0, 0),
                               xytext = (5, 5),
                               xycoords = "data",
                               textcoords = "offset pixels",
                               ha = "center",
                               va = "bottom",
                               family = "monospace",
                               weight = "bold",
                               fontsize = FONTSIZE,
                               bbox = dict(facecolor = "white", alpha = 0.4, edgecolor = "None", pad = 0)
                               )
    
    def hover(event: MouseEvent) -> None:
        """Display frequency above each bar upon hovering over it.

        Args:
            event (MouseEvent): Matplotlib mouse event.
        """
        visibility = annotation.get_visible()
        if event.inaxes == axes:
            for bars in axes.containers:
                for bar in bars:
                    cont, _ = bar.contains(event)
                    if cont:
                        x, y = bar.get_x() + bar.get_width() / 2, bar.get_y() + bar.get_height()
                        annotation.xy = (x, y)
                        annotation.set_text(y)
                        annotation.set_visible(True)
                        figure.canvas.draw_idle()
                        return
        if visibility:
            annotation.set_visible(False)
            figure.canvas.draw_idle()
        
    # Display histogram
    id = figure.canvas.mpl_connect("motion_notify_event", hover)
    show()
    figure.canvas.mpl_disconnect(id)

if __name__ == "__main__":
    # Generate quantum circuit for Grover's algorithm 
    grover_circuit = grover()

    # Simulate Grover's algorithm with a Qiskit backend and get results
    with BACKEND.open_session() as session:
        results = BACKEND.run(transpile(grover_circuit, BACKEND, optimization_level = 2), shots = SHOTS).result()

    # Get each state's frequency and display simulation results
    display_results(results.get_counts(), False)