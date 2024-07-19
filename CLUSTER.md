# Running on the Cluster

Generate an environment with Poetry

    $ micromamba create -n cluster python=3 poetry
	$ eval "$(micromamba shell hook --shell bash)"
	$ micromamba activate cluster
	
Install the environment in the base of the repe (where the toml file is).

    $ poetry install
	
	
To view the machines that are free

   $ sinfo

This is helpful, set this in ~/.bashrc
   
   $ alias jobs='squeue -o "%14i %10j %4t %8q %8a %8g %10P %10Q %8D %11l %11L %R" -u ${USER}'
   
