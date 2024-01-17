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
	listint_t *new;
	listint_t *current;

	current = *head;
	if (*head == NULL)
		return (NULL);
	while (current->n < n)
		current = current->next;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = current->next;
	current->next = new;
	return (new);
}
