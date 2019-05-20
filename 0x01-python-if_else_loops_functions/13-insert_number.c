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
	listint_t *new;
	listint_t *temp;

	temp = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
		return (new);
	}
	while (temp && temp->n < number)
	{
		if (temp->next == NULL || temp->next->n > number)
			break;
		else
			temp = temp->next;
	}

       	new->next = temp->next;
       	temp->next = new;
	return (new);
}
