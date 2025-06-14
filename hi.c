#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Structure to represent a transition in the FA
typedef struct {
    int startState;
    char symbol;
    int endState;
} Transition;

// Function to display the regular grammar
void displayGrammar(Transition transitions[], int numTransitions, int numStates, int startState, int acceptState) {
    printf("Regular Grammar:\n");

    int i, j; // Declare loop variables outside the loop
    for (i = 0; i < numStates; i++) {
        printf("S%d -> ", i);
        int found = 0;

        for (j = 0; j < numTransitions; j++) {
            if (transitions[j].startState == i) {
                found = 1;
                printf("%cS%d | ", transitions[j].symbol, transitions[j].endState);
            }
        }

        // Add epsilon (e) transition for accept state
        if (i == acceptState) {
            printf("epsilon"); // Replace Unicode epsilon for compatibility
        }

        if (!found && i != acceptState) {
            printf("- (no transitions)");
        }

        printf("\n");
    }
}

int main() {
    int numStates, numTransitions, startState, acceptState, i;

    printf("Enter the number of states: ");
    scanf("%d", &numStates);

    printf("Enter the number of transitions: ");
    scanf("%d", &numTransitions);

    printf("Enter the start state: ");
    scanf("%d", &startState);

    printf("Enter the accept state: ");
    scanf("%d", &acceptState);

    Transition transitions[numTransitions];

    printf("Enter the transitions (startState symbol endState):\n");
    for (i = 0; i < numTransitions; i++) { // Use the declared loop variable
        scanf("%d %c %d", &transitions[i].startState, &transitions[i].symbol, &transitions[i].endState);
    }

    displayGrammar(transitions, numTransitions, numStates, startState, acceptState);

    return 0;
}
