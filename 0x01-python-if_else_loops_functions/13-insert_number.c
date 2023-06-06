#include "lists.h"

/**
 * insert_node - inserts a a number into a sorted singly linked list
 * @head: pointer to pointer to the first node of the linked list
 * @number: the number/node we want to add to the list
 * Return: the address of the new node, or NULL if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = NULL, *new_node = NULL, *temp2 = NULL;

	/* check if list is NULL*/
	if (head == NULL)
	{
		return (NULL);
	}
	/* allocate memory for the new node*/
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL) /* check if allocation was successful*/
	{
		return (NULL);
	}
	new_node->n = number; /* populate the new node */
	/* traverse looking for a place to to insert it*/
	temp = *head;
	while (temp->next != NULL)
	{
		if (temp->n <= number)
		{
			temp2 = temp;
		}
		temp = temp->next;
	}
	temp = temp2->next;
	temp2->next = new_node;
	new_node->next = temp;
	return (new_node);
}
