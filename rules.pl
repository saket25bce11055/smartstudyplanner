% Priority
high_priority(Days, Difficulty) :-
    Days =< 2;
    Difficulty >= 4.

medium_priority(Days, Difficulty) :-
    Days > 2,
    Days =< 5,
    Difficulty >= 3.

low_priority(Days, Difficulty) :-
    Days > 5,
    Difficulty < 3.

% Break Suggestion
take_break(Duration) :-
    Duration >= 2.

% Overload 
overloaded(Hours) :-
    Hours > 6.