#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - Checks if a singly linked list has a cycle
 * @list: Pointer to the head of the singly linked list
 *
 * Return: 1 if a cycle is found, 0 otherwise
 */
int check_cycle(listint_t *list)
{
    listint_t *slow, *fast;

    if (!list)
        return (0);

    slow = list;
    fast = list;

    while (fast != NULL && fast->next != NULL)
    {
        slow = slow->next;         // Move slow pointer by 1
        fast = fast->next->next;   // Move fast pointer by 2

        if (slow == fast)
            return (1);            // Cycle detected
    }

    return (0);                    // No cycle
}
