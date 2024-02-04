#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - adds a new node in the sorted one
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */

listint_t *insert_node(listint_t **head, const int n)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *current;
	listint_t *temp;

	current = *head;
	if (*head == NULL)
	{
		new->n = n;
		new->next = 0;
		*head = new;
		return *head;
	}
	while (current != NULL)
	{
		if (current->n <= n)
			temp = current;
		current = current->next;
	}
	if (new == NULL)
		return (NULL);

	if (n < 0)
	{
		new->n = n;
		new->next = *head;
		*head = new;
	}
	else
	{
		new->n = n;
		new->next = temp->next;
		temp->next = new;
	}
	return (new);
}
