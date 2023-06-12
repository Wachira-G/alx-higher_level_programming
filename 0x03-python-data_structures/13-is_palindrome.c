#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to the first node
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head, *temp2 = NULL, *next =  NULL, *previous = NULL;

	/* An empty list is considered a palindrome */
	if (head == NULL || *head == NULL)
		return (1);

	temp = *head;
	temp2 = *head;
	while (temp && temp->next != NULL) /* move to end and middle */
	{
		temp = temp->next->next;
		temp2 = temp2->next;
	}
	/* reverse the half list */
	while (temp2 != NULL)
	{
		next = temp2->next;
		temp2->next = previous;
		previous = temp2;
		temp2 = next;
	}
	temp = *head;
	while (previous != NULL) /* compare values */
	{
		if (temp->n != previous->n)
			return (0);
		temp = temp->next;
		previous = previous->next;
	}
	return (1);
}
