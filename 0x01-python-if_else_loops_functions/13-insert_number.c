#include "lists.h"
#include "stdlib.h"


/**
  *create_node - creates a new node
  *@number: the node value
  *Return: address of the created node
 */
listint_t *create_node(int number)
{
	listint_t *new_node = (listint_t *)malloc(sizeof(listint_t));

	if (new_node)
	{
		new_node->n = number;
		new_node->next = NULL;
	}
	return (new_node);
}

/**
  *insert_node - inserts node at a given index in a sorted singly linked list
  *@head: pointer to the first node in the list
  *@number: the number to add
  *Return: address of the newly added node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *prev = NULL;
	listint_t *new_node = create_node(number);

	if (!new_node)
	{
		return (NULL);
	}

	while (current && current->n < number)
	{
		prev = current;
		current = current->next;
	}

	if
	(!prev)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		prev->next = new_node;
		new_node->next = current;
	}

	return (new_node);
}
