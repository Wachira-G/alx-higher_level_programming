#include "lists.h"

/**
 * insert_node - inserts a a number into a sorted singly linked list
 * @head: pointer to pointer to the first node of the linked list
 * @number: the number/node we want to add to the list
 * Return: the address of the new node, or NULL if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = NULL, *new_node = NULL, *prev = NULL;

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
	if (*head == NULL || (*head)->n >= number) /* empty list or beginning*/
	{
		new_node->next = *head;
		*head = new_node;
		return (*head);
	}

	temp = *head;
	/* middle of list or end of list*/
	while (temp->next != NULL && temp->n <= number)/* move till end */
	{
		prev = temp;
		temp = temp->next;
	}
	if (temp->next == NULL && temp->n < number)
	{
		temp->next = new_node;
		new_node->next = NULL;
		return (new_node);
	}
	/* add new node in middle of list */
	prev->next = new_node;
	new_node->next = temp;

	return (new_node);
}
