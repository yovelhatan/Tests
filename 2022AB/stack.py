#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

// Define the structure for a node in the linked list
 typedef struct Node{
    int data;
    struct Node *next;
} node;

// Define the structure for the stack
typedef struct {
    int n_elements;
    node *top;
} stack;

// Function declarations
stack init(int arr[], int size);
void print(stack s);
int pop(stack * ptr);

int main(void) {
    int a[3] = {1,2,3};
    stack s;
    int value;
    s = init(a, 3);
    // Print the elements of the stack
    print(s);
    value = pop(&s);
    printf("%d\n", value);
    print(s);

    return 0;
}

// Function definitions

// Initialize the stack with elements from an array
stack init(int arr[], int size) {
    int i;
    stack s;
    node *head, *tail;
    if (size == 0){
        s.n_elements = 0;
        s.top = NULL;
    }

    // Allocate memory for the head node
    head = (node *)malloc(sizeof(node));
    assert(head != NULL);

    // Initialize the first node with the first element of the array
    head->data = arr[0];
    head->next = NULL; // Initialize next pointer

    // Initialize the stack with the head node
    s.n_elements = size;
    

    tail = head;

    // Iterate through the array to create the linked list
    for (i = 1; i < size; i++) {
        // Allocate memory for the next node
        tail->next = (node *)malloc(sizeof(node));
        assert(tail->next != NULL);
        tail = tail->next;
        // Initialize the node with the corresponding element of the array
        tail->data = arr[i];
        tail->next = NULL; // Initialize next pointer
    }
    s.top = head;
    return s;
}

// Print the elements of the stack
void print(stack s) {
    node *current = s.top;

    printf("Stack elements: ");
    while (current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n");
}

int pop(stack * ptr){
    node * curr_top;
    int value;

    assert(ptr != NULL);
    assert(ptr->top != NULL);

    value = ptr->top->data;
    /*removing top from elements list*/
    curr_top = ptr->top;
    ptr->top = ptr->top->next;

    (ptr->n_elements)--;
    free(curr_top);

    return value;
}

