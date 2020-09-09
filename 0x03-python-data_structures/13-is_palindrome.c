#include "lists.h"
/**
 * len - palindrome lenght
 * @head: pointer to head
 * Return: size
 */
int len(listint_t *head)
{
	int counter;

	if (!head)
		return (EXIT_FAILURE);
	for (counter = 0; head; counter++)
		head = head->next;

	return (counter);
}
/**
 * is_palindrome - check if linked list is palindrome
 * @head: pointer to linked list's head
 * Return: 0 if is not, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *aux = *head;
	int size = len(aux);

	int *array, index;
	int i = 0;

	array = malloc(sizeof(int) * size);
	if (!array)
		return (EXIT_FAILURE);
	
	for (index = 0; aux; index++)
	{
		array[index] = aux->n;
		aux = aux->next;
	}

	while (i < size / 2)
	{
		if (array[i] == array[index - 1])
		{
			i++;
			index--;
			continue;
		}
		break;
	}
	if (i == size / 2)
	{
		free (array);
		return (1);
	}
	free (array);
	return(0);
}
