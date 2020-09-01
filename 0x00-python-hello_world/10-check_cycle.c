#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - checks if there's a cycle in linked list
 * @list: the list to check
 * Return: 1 if cycle = true/ 0 if cycle = false
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	while (fast && slow && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
		if (fast == slow)
			return (1);
	}
	return (0);
}
