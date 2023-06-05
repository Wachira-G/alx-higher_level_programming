#include "lists.h"

/**
 * check_cycle - checks a linked list for a cycle
 * @list: pointer to the head of the list to check for cycle
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *head;
	listint_t *current;

	head = list;
	current = list;
	while (head != NULL && head->next->next != NULL)
	{
		current = current->next;
		head = head->next->next;
		if (head == current)
			return (1);
	}
	return (0);
}
