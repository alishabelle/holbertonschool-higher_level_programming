#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 *insert_node - function to insert a node into linked list
 *@head: parameter points to beg of list
 *@number: parameter
 * Return: return is astructure of listint_t type
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp, *store;

	temp = *head;
	store = NULL;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	while (temp  && temp->n < number)
	{
		store = temp;
		temp = temp->next;
	}

       	new->next = temp;
	if (store)
		store->next = new;
	else
		*head = new;
	return (new);
}
