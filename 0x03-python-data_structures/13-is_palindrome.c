#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to a pointer to the first node in the list.
 *
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *last_node, *middle, *prev = NULL, *next = NULL;
	int		   result = 1;

	/*if head is NULL or empty or only one node in list*/
	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (result); /*we consider list a palindrome*/
	for (slow = *head, fast = *head; fast != NULL && fast->next != NULL;)
	{ /* find the middle and reverse the first half in one loop */
		fast	   = fast->next->next; /* fast moves by two steps */
		next	   = slow->next;	   /* save next node of slow */
		slow->next = prev;			   /* make slow point to previous node */
		prev	   = slow; /* make slow th prev node for next iteration */
		slow	   = next; /* slow moves by one step */
	}
	*head = prev; /* update head to point to last node of reversed first half */
	middle = slow;		   /* save the original middle node */
	if (fast != NULL)	   /* if list has odd num of nodes, skip slow by 1 */
		slow = slow->next; /* correct start for 2nd half of odd nodes list */
	for (; prev != NULL && slow != NULL; prev = prev->next, slow = slow->next)
	{							/* compare the two halves */
		if (prev->n != slow->n) /*if any pair doesnt match*/
		{
			result = 0; /* not a palindrome */
			break;
		}
	} /* reverse the first half back to its original state */
	prev = NULL, slow = *head;
	while (slow != NULL)
	{
		next	   = slow->next;
		slow->next = prev;
		prev	   = slow;
		slow	   = next;
	}
	*head	  = prev; /* head now points to the start of first half */
	last_node = *head;
	while (last_node->next != NULL) /* traverse to the end of the first half */
		last_node = last_node->next;
	last_node->next = middle; /*join end of 1st toF 2nd half from middle*/
	return (result); /*is palindrome->all value pairs from both halves matched*/
}
