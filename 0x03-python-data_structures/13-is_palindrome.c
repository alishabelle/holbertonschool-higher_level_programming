#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int length_function(listint_t *h);

/**
 *is_palindrome - function to check if linked list is palindrome
 *@head: parameter
 * Return: returns 0 if its not a palindrome returns 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t **gold = head;
	listint_t *move;
	int buffer[3000], i = 0, idk, beg = 0, end;

	move = *head;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	while (move != NULL)
	{
		buffer[i] = move->n;
		move = move->next;
		i++;
	}
	buffer[i++] = '\0';
	i = 0;
	idk = length_function(*gold);
	if (idk == 1)
		return (1);
	for (end = idk - 1; beg < idk && end >= 0; beg++, end--)
	{
		if (beg > end)
		{
			return (1);
		}
		if (buffer[beg] != buffer[end])
		{
			return (0);
		}
	}
	return (0);
}

/**
 *length_function - function that returns the length of an array
 *@h: parameter
 * Return: returns an int
 */
int length_function(listint_t *h)
{
	listint_t *num = h;
	int i = 0;

	while (num != NULL)
	{
		num = num->next;
		i++;
	}
	return (i);
}
