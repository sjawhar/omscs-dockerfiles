## Setting up an OpenMPI Cluster
Just copy `docker-compose.cluster.yml` and `mpi-hosts` to the directory with your HPC assignments and run `docker-compose up`:

```bash
cp docker-compose.cluster.yml $HPC_ASSIGNMENT_DIRECTORY/
cp mpi-hosts $HPC_ASSIGNMENT_DIRECTORY/
cd $HPC_ASSIGNMENT_DIRECTORY
docker-compose -f docker-compose.cluster.yml --project-name hpc up --scale slave=4
```

Now `docker exec -it hpc_master_1 bash` and run
`ssh-keygen -t rsa -N "" -f /root/.ssh/id_rsa`.

OK, you're all set up. Just add `--hostfile /omscs/mpi-hosts` to your `mpirun` commands and they will run on the slaves.

If you're on a Windows machine and you get a hostfile formatting error when running `mpirun`, you need to make sure to remove carriage returns from `mpi-hosts`.
