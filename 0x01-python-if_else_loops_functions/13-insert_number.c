#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - Inserts a number into a sorted singly linked list
 *
 * @head: Address of the pointer to the start of the list
 * @number: The int data to be inserted
 *
 * Return: The address of the new node added
 * OR NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = NULL, *curr_node = NULL;

	if (head == NULL) /* address of head ptr is NULL */
		return (NULL);

	/* allocate memory for the new node */
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL) /* on alloc fail */
		return (NULL);

	/* assign int values to element of the new node */
	new_node->n = number;

	/* if the list is empty or the new node is the smallest */
	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	/* traverse the list to find the correct position to insert */
	curr_node = *head;
	while (curr_node->next != NULL && curr_node->next->n < number)
	{
		curr_node = curr_node->next;
	}

	new_node->next = curr_node->next;
	curr_node->next = new_node;

	return (new_node);
}
