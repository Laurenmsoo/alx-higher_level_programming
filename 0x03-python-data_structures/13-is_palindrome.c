#include "lists.h"

/**
 * is_palindrome - function to call check_pal to see if list is palindrome
 * @head: pointer to the beginning of the list
 * Return: 0 if not palindrome or 1 otherwise
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (check_pal(head, *head));
}

/**
 * check_pal - function to check if the list is palindrome
 * @head: pointer to the beginning of the list
 * @last: pointer to the end of the list
 * Return: 0 if not palindrom or 1  otherwise
 */
int check_pal(listint_t **head, listint_t *last)
{
	if (last == NULL)
		return (1);
	if (check_pal(head, last->next) && (*head)->n == last->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
