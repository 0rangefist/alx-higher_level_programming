#include "lists.h"

/**
 * check_cycle - check if a cycle exists in a loop
 * @list: pointer to start of the linked list
 * Return: 1 if cycle is detected and 0 otherwise
 */
int check_cycle(listint_t *list)
{
	/* we use the tortoise & hare algorithm to detect a loop */
	listint_t *tortoise = list; /*tortoise points to list start */
	listint_t *hare	= list;/*hare points to list start */

	if (list == NULL) /* there is no list, so no loop*/
		return (0);

	/* traverse through the loop with both tortoise & hare */
	/* hare is the fastest so will reach end of list if no loop */
	/* thus we check for tortoise && tortoise->next being NULL */
	while (hare != NULL && hare->next != NULL)
	{
		tortoise = tortoise->next;
		hare	 = (hare->next)->next;
		if (tortoise == hare) /* if tortoise == hare, loop detected */
			return (1);
	}
	return (0); /* no loop found */
}
