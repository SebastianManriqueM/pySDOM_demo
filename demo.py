import sdom

from sdom import run_solver, initialize_model, configure_logging, get_default_solver_config_dict
from sdom import load_data, export_results

import time
import logging
import highspy

# import xpress as xp
# xp.init('C:/xpressmp/xpauth.xpr')
# oemnum = 123456789
# if (xp.beginlicensing()):
#     string = ""
#     n,string = xp.license(0,string)
#     lic = oemnum - n*n//19
#     n,string = xp.license(lic,string)
#     xp.init()
#     xp.endlicensing()

def main( with_resilience_constraints = False, case='test_data' ):
    configure_logging(level=logging.DEBUG)
    n_steps = 24  # Number of steps in the simulation (IN HOURS - RECOMENDED = 8760)

    start_time = time.time()
    data = load_data( "C:\\Users\\smachado\\repositories\\pySDOM\\SDOM\\Data\\no_exchange_run_of_river" ) #INCLUDE THE FOLDER PATH WHERE YOU HAVE THE INPUT .CSV AND .TXT FILES
    elapsed_time = time.time() - start_time
    print(f"Data loading took {elapsed_time:.2f} seconds.")

    start_time = time.time()
    model = initialize_model( data, n_hours = n_steps, with_resilience_constraints = with_resilience_constraints )
    elapsed_time = time.time() - start_time
    print(f"Model initialization took {elapsed_time:.2f} seconds.")

    start_time = time.time()
    #solver_dict = get_default_solver_config_dict(solver_name="cbc", executable_path=".\\Solver\\bin\\cbc.exe")
    #solver_dict = get_default_solver_config_dict(solver_name="xpress", executable_path="C:\\xpressmp\\bin\\xprs.dll")
    solver_dict = get_default_solver_config_dict(solver_name="highs", executable_path="")
    
    best_result = run_solver(model, solver_dict)
    elapsed_time = time.time() - start_time
    print(f"Solver run for {n_steps} steps took {elapsed_time:.2f} seconds.")

    if best_result:
        export_results(model, case)
    else:
        print(f"Solver did not find an optimal solution for given data and with resilience constraints = {with_resilience_constraints}, skipping result export.")


# ---------------------------------------------------------------------------------
# Execute the main function
if __name__ == "__main__":
    main()