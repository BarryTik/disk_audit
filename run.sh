#!/bin/bash -l        
#SBATCH --time=4:00:00
#SBATCH --mem=10g
#SBATCH --tmp=10g
#SBATCH --mail-type=ALL  
#SBATCH --mail-user=tikal004@umn.edu
#SBATCH -J=miran-disk-audit
./disk_audit.py /home/miran045/ --days 700