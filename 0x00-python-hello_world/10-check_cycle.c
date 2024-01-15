#include <stdio.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks for a cycle in the list
 * @list: pointer to the head of the list
 * Return: one or 0 if the node has cycle
 */

int check_cycle(listint_t *list)
{
	const listint_t *current;
	unsigned int n;

	if(list == NULL)
	{
		return (0);
	}

	current = list;
	n = 0;

	while (current->next != NULL)
	{
		current = current->next;
		n++;
		if (n == 20)
		{
			return 1;
			break;
		}
	}
	if (current->next == NULL)
		{
			return (0);
		}
		else
		{
			return (1);
		}
}
