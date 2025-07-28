# IMPORT SDOM - Notice the name SDOM python module might change to "pySDOM"
from SDOM import run_solver, initialize_model, configure_logging
from SDOM import load_data, export_results
import time

def main( with_resilience_constraints = False, case='test_data' ):
    configure_logging()
    n_steps = 48  # Number of steps in the simulation

    start_time = time.time()
    data = load_data( "C:\\Users\\smachado\\repositories\\pySDOM\\SDOM\\Data" ) 
    elapsed_time = time.time() - start_time
    print(f"Data loading took {elapsed_time:.2f} seconds.")

    start_time = time.time()
    model = initialize_model( data, n_hours = n_steps, with_resilience_constraints = with_resilience_constraints )
    elapsed_time = time.time() - start_time
    print(f"Model initialization took {elapsed_time:.2f} seconds.")

    start_time = time.time()
    best_result = run_solver(model, cbc_executable_path=".\\Solver\\bin\\cbc.exe")
    elapsed_time = time.time() - start_time
    print(f"Solver run for {n_steps} took {elapsed_time:.2f} seconds.")

    if best_result:
        export_results(model, case)
    else:
        print(f"Solver did not find an optimal solution for given data and with resilience constraints = {with_resilience_constraints}, skipping result export.")


# ---------------------------------------------------------------------------------
# Execute the main function
if __name__ == "__main__":
    main()