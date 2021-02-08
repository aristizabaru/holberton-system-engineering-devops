#include <unistd.h>
#include <stdio.h>

/**
 * infinite_while - creates an infinite loop
 * Return: 0 on success
 */
int infinite_while(void)
{
	while (1)
		sleep(1);
	return (0);
}

/**
 * main - create 5 zombie processes
 * Return: 0 on succes
 */
int main(void)
{
	int i = 0;
	int pid = -1;

	/* create zombie process */
	for (; i < 5; i++)
		if (fork() == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			return (0);
		}
	/* print PID in child process */
	if (pid != 0)
		infinite_while();
	return (0);
}
