#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 *check_cycle - function that cycles through linked list
 *
 *
 */
int check_cycle(listint_t *list)
{
	listint_t *skips;
	listint_t *node;


	if (list == NULL)
		return (0);
	if (list->next == NULL)
		return (0);
	
	skips = list;
	node = list;

	while (skips && skips->next && node && node->next)
	{	
		if (skips == node)
			return (1);
		skips = skips->next->next;
		node = node->next;
	
	}
	return (0);
}
