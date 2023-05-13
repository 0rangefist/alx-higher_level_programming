#include "lists.h"
#include <stdio.h>
/**
 * reverse_list - Reverses a listint_t linked list in place
 *
 * @head: Pointer to pointer to the first node of the list
 */
void reverse_list(listint_t **head)
{
	listint_t *current = *head, *prev = NULL, *next = NULL;

	while (current != NULL)
	{
		next		  = current->next;
		current->next = prev;
		prev		  = current;
		current		  = next;
	}

	*head = prev;
}

/**
 * do_lists_match - Compares the values of two listint_t linked lists to
 * check if the smaller list matches the bigger list or if the two lists
 * are the same.
 *
 * @list_one: Pointer to the head node of the first list.
 * @list_two: Pointer to the head node of the second list.
 *
 * Return: 1 if the smaller list matches the bigger list or if the two lists
 * are the same, 0 otherwise.
 */
int do_lists_match(listint_t *list_one, listint_t *list_two)
{
	/* compare the two lists */
	while (list_one != NULL && list_two != NULL)
	{
		if (list_one->n != list_two->n) /*if any pair doesnt match*/
		{
			return (0); /* the lists don't match */
		}
		list_one = list_one->next;
		list_two = list_two->next;
	}
	return (1); /* lists match */
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to a pointer to the first node in the list.
 *
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *first_half_end, *second_half_start;
	listint_t *slow, *fast, *prev = NULL;
	int		   palindrome_flag = 1;

	/*if head is NULL or empty or only one node in list*/
	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (palindrome_flag); /*we consider list a palindrome*/

	/* use slow to find middle node (odd list) or middle+1 (even list)*/
	for (slow = *head, fast = *head; fast != NULL && fast->next != NULL;)
	{
		fast = fast->next->next; /* fast moves by two steps */
		prev = slow;			 /* save previous slow node */
		slow = slow->next;		 /* slow moves by one step */
	}
	if (fast == NULL) /* if even num of nodes in list */
	{
		first_half_end	  = prev; /* save end node of 1st half */
		second_half_start = slow; /* save start node of 2nd half */
	}
	else /* if odd num of nodes in list */
	{
		first_half_end	  = slow;		/* save end node of 1st half */
		second_half_start = slow->next; /* save start node of 2nd half */
	}

	/* reverse the 2nd half in place */
	reverse_list(&second_half_start);
	/* check if the 2 list halves match */
	palindrome_flag = do_lists_match(*head, second_half_start);
	/* reverse the 2nd half back to its original state */
	reverse_list(&second_half_start);
	/* rejoin the 2 halves */
	first_half_end->next = second_half_start;

	return (palindrome_flag);
}
