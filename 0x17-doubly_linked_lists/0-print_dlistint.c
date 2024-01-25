#include <stdio.h>
#include <stdlib.h>
#include "lists.h"


/**
 * print_dlistint - prints all elements of a dlisint
 * @h: pointer to head of list
 * Return: number of nodes
 */

size_t print_dlistint(const dlistint_t *h)
{
	const struct dlistint_s *temp;
	unsigned int i;

	i = 0;
	temp = h;

	while (temp != 0)
	{
		i ++;
		printf("%d\n", temp->n);
		temp = temp->next;
	}

	return i;
}
