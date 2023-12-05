from qiskit import QuantumCircuit as qc
from qiskit import QuantumRegister as qr
from qiskit import execute
from matplotlib.pyplot import show, text, subplots
from qiskit_aer import Aer
from math import pi, sqrt
from heapq import nlargest

"""Feel free to modify the following constants"""
N = 5                          # Number of qubits
SEARCH_VALUES = {9, 0, 3, 19}  # Set of m nonnegative integers to search for using Grover's algorithm (i.e. TARGETS in base 10)
SHOTS = 10000                  # Amount of times the algorithm is simulated

"""Please do not modify the following constants, otherwise you risk breaking the program"""
TARGETS = {f"{s:0{N}b}" for s in SEARCH_VALUES}  # Set of m N-qubit binary strings representing target state(s) (i.e. SEARCH_VALUES in base 2)
QUBITS = qr(N, "q")                              # N-qubit quantum register

def print_circuit(circuit: qc, title: str = "") -> None:
    print(f"\n{title}:\n")
    print(circuit)

def oracle(targets: set[str], name: str = "Oracle", display_oracle: bool = True) -> qc:
    """Mark target state(s) with negative phase.

    Args:
        targets (set[str]): N-qubit binary string(s) representing target state(s).
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
                oracle.x(i)                    # Pauli-X gate

        # Simulate (N - 1)-control Z gate
        oracle.h(N - 1)                        # Hadamard gate
        oracle.mcx(list(range(N - 1)), N - 1)  # (N - 1)-control Toffoli gate
        oracle.h(N - 1)                        # Hadamard gate

        # Flip back to original state
        for i in range(N):
            if target[i] == "0":
                oracle.x(i)                    # Pauli-X gate

    # Display oracle, if applicable
    if display_oracle:
        print_circuit(oracle, "ORACLE")

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
    
    diffuser.h(QUBITS)                          # Hadamard gate
    diffuser.append(oracle(["0" * N]), QUBITS)  # Oracle with all zero target state
    diffuser.h(QUBITS)                          # Hadamard gate

    # Display diffuser, if applicable
    if display_diffuser:
        print_circuit(diffuser, "DIFFUSER")
    
    return diffuser

def grover(oracle: qc = oracle(TARGETS), diffuser: qc = diffuser(), name: str = "Grover Circuit", display_grover: bool = True) -> qc:
    """Create quantum circuit representation of Grover's algorithm,
    which consists of 4 parts: (1) state preparation/initialization,
    (2) oracle, (3) diffuser, and (4) measurement of resulting state.
    
    Steps 2-3 are repeated an optimal number of times (i.e. Grover's
    iterate) in order to maximize probability of success of Grover's algorithm.

    Args:
        oracle (qc, optional): Quantum circuit representation of oracle. Defaults to oracle(TARGETS).
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
    
    # Apply barrier to separate steps
    grover.barrier()
    
    # Apply oracle and diffuser (i.e. Grover operator) optimal number of times
    for _ in range(int((pi / 4) * sqrt((2 ** N) / len(TARGETS)))):
        grover.append(oracle, QUBITS)
        grover.append(diffuser, QUBITS)
     
    # Measure all qubits once finished
    grover.measure_all()

    # Display grover circuit, if applicable
    if display_grover:
        print_circuit(grover, "GROVER CIRCUIT")
    
    return grover

def outcome(winners_dict: dict[str, int]) -> None:
    """Print top measurement(s) (state(s) with highest frequency)
    and target state(s) in binary and decimal form, determine
    if top measurement(s) equals target state(s), then print result.

    Args:
        winners_dict (dict[str, int]): State(s) (N-qubit binary string(s)) with
        highest probability of being measured, and its respective frequency.
    """
    print("WINNER(S):")
    print(f"Binary = {[*winners_dict]}\nDecimal = {[int(winner, 2) for winner in [*winners_dict]]}\n")
        
    print("TARGET(S):")
    print(f"Binary = {TARGETS}\nDecimal = {SEARCH_VALUES}\n")
    
    print(f"Target(s) found with {sum(winners_dict.values()) / SHOTS:.2%} accuracy!\n"
          if all(winner in TARGETS for winner in [*winners_dict])
          else "Target(s) not found...\n")

def bar_graph(results: dict[str, int]) -> None:
    """
    Generate and display histogram of simulation results.

    Args:
        results (dict[str, int]): All state(s) (N-qubit binary string(s)) and its respective frequency.
    """
    # Histogram x-axis
    x_axis = [str(winner) for winner in [*results]]

    # Histogram y-axis
    y_axis = [*results.values()]

    # Create histogram for simulation results
    _, ax = subplots(num = "Simulation Results")
    ax.bar(x_axis, y_axis, color = ["green" if key in TARGETS else "red" for key in x_axis])

    # Set histogram title, x-axis label, and y-axis label respectively
    ax.set_title("Simulation Results")
    ax.set_xlabel("States (Qubits)")
    ax.set_ylabel("Frequency")
    
    # Display frequency above each bar
    for index, frequency in enumerate(y_axis):
        text(index, frequency, str(frequency), weight = "bold", ha = "center", va = "bottom")
    
    # Display histogram
    show()

if __name__ == "__main__":
    # Generate quantum circuit for Grover's algorithm 
    grover_circuit = grover()

    # Simulate Grover's algorithm with grover_circuit SHOTS times and get results
    results = execute(grover_circuit, backend = Aer.get_backend("qasm_simulator"), shots = SHOTS).result()

    # Get each state's frequency
    counts = results.get_counts()

    # Create dictionary to store winners (i.e. state(s) with highest count) and their frequencies
    winners_dict = { }

    # Populate winners_dict
    for winner in nlargest(len(TARGETS), counts, key = counts.get):
        winners_dict[winner] = counts.get(winner)

    # Print outcome
    outcome(winners_dict)

    # Add frequency of all other states to winners_dict
    winners_dict["All Other States"] = sum([counts.get(other_states) for other_states in set(counts) - set([*winners_dict])])

    # Display simulation results as histogram
    bar_graph(winners_dict)