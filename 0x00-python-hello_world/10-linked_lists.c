#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

size_t print_listint(const listint_t *h)
{
    const listint_t *current;
    unsigned int n; /* number of nodes*/

    current = h;
    n = 0;
    while (current != NULL)
    {
        printf("%i", current->n);
        current = current->next;
        n++;
    }
    return (n);
}

