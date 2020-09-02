#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - insert node sorted
 * @head: reference to linked list
 * @number: number to add in linked list
 * Return: The new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = *head;
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if (*head == NULL || (*head)->n >= new_node->n)
	{
		*head = new_node;
		new_node->next = tmp;
	}
	else
	{
		while (tmp->next)
		{
			if (tmp->next->n >= new_node->n)
				break;
			else
				tmp = tmp->next;
		}
		new_node->next = tmp->next;
		tmp->next = new_node;
	}
	return (new_node);
}
