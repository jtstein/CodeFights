/*
Jordan Stein
7/15/2017

Given a singly linked list of integers l and an integer k, remove all elements from list l that have a value equal to k.

Example

For l = [3, 1, 2, 3, 4, 5] and k = 3, the output should be
removeKFromList(l, k) = [1, 2, 4, 5];
For l = [1, 2, 3, 4, 5, 6, 7] and k = 10, the output should be
removeKFromList(l, k) = [1, 2, 3, 4, 5, 6, 7].
Input/Output

[time limit] 500ms (cpp)
[input] linkedlist.integer l

A singly linked list of integers.

Guaranteed constraints:
0 ≤ list size ≤ 105,
-1000 ≤ element value ≤ 1000.

[input] integer k

An integer.

Guaranteed constraints:
-1000 ≤ k ≤ 1000.

[output] linkedlist.integer

Return l with all the values equal to k removed.
*/

ListNode<int> * removeKFromList(ListNode<int> * l, int k) {
    
    ListNode<int> * head = l;
    ListNode<int> * prev;
 
    while(l && l->value == k){
        head = l->next;
        l = head;
    }
    
    if(!head){
        return head;
    }

    while (l->next){
        if (l->value == k){
            if (l->next->next){
                l->value = l->next->value;
                l->next = l->next->next; 
            }
        }
        prev = l;
        if (l->value == k){
            if (l->next->next){
                l->value = l->next->value;
                l->next = l->next->next; 
            }
        }
        l = l->next;
    }
    
    if (prev->next->value == k){
        prev->next = NULL;
    }
    
    return head;
}