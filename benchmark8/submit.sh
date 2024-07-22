#!/bin/bash
#SBATCH --partition=rack1               # -p, first available from the list of partitions
#SBATCH --time=00-01:00:00                 # -t, time (hh:mm:ss or dd-hh:mm:ss)
#SBATCH --nodes=1                       # -N, total number of machines
#SBATCH --ntasks=1                      # -n, 64 MPI ranks per Opteron machine
#SBATCH --cpus-per-task=1               # threads per MPI rank
#SBATCH --job-name=benchmark8 # -J, for your records
#SBATCH --chdir=/working/aan2/surf-2024-austyn-nguyen/benchmark8   # -D, full path to an existing directory
#SBATCH --qos=test
#SBATCH --mem=0G
#SBATCH --output=slurm-%j.out

omp_threads=$SLURM_CPUS_PER_TASK
export OMP_NUM_THREADS=$omp_threads
export OPENBLAS_NUM_THREADS=$omp_threads
export MKL_NUM_THREADS=$omp_threads
export VECLIB_MAXIMUM_THREADS=$omp_threads
export NUMEXPR_NUM_THREADS=$omp_threads


micromamba activate  bm8-env
python benchmark8a.py params8a.yaml


