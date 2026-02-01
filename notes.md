#basic notes

#venv
/bin -> contains the Python interpreter and the activate scripts.
/lib -> Where all the packages  pip install are stored.
include/ -> Compiled C headers for certain Python packages.
pyvenv.cfg -> A small config file that tells the environment where the "real" Python lives.

good programming practice to not add venv to the git folder
    its  very heavy
    not portable
    system dependicies

project structure 
    my_gdp_project/
        ├── .git/                 # Hidden Git metadata
        ├── .gitignore            # Tells Git to ignore venv/
        ├── config.json           # Your configuration file
        ├── dashboard.py          # Entry point
        ├── data_loader.py        # Module 1
        ├── data_processor.py     # Module 2
        ├── visualizer.py         # Module 3
        ├── requirements.txt      # THE LIST OF LIBRARIES
        ├── gdp_data.csv          # Your dataset
        └── venv/                 # THE ACTUAL LIBRARIES (Ignored by Git)
            ├── bin/
            ├── lib/
            └── ...

When your partner pulls your latest commit from GitHub, their venv won't automatically have the new library. They need to run:
    pip install -r requirements.txt