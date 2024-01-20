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
    listint_t *temp;

	current = *head;
	if (*head == NULL)
		return (NULL);
	while (current->next != NULL)
    {
        if (current->n <= n)
            temp = current;
        current = current->next;
    }
    printf("This is the value of current n in the list %i", current->n);
	new = malloc(sizeof(listint_t));
    if (head == NULL)
       *head = new;
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = temp->next;
	temp->next = new;
	return (new);
}
