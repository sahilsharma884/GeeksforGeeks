# Description of filename
<hr>

```Array_01.py```: <strong>Subarray with given sum</strong> (Ref: https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0) <br>
<ul>
<li>Maintain start and last index to store and print these values </li>
<li>Iterate the complete array.</li>
<li>Add array elements to cuursum</li>
<li>If currsum becomes greater than S, then remove elements starting from start index, till it become less than or equal to S, and increement start.</li>
<li>if currsum becomes equals to S, then print the starting and last index</li>
<li>if the currsum never maches to S, then print -1</li>
</ul>

```Array_02.py```: <strong>Missing number in array</strong> (Ref: https://practice.geeksforgeeks.org/problems/missing-number-in-array/0) <br>
<ul>
<li>Sum of 'n' natural numbers from 1 to n.</li>
<li>Compute the sum of elements of array</li>
<li>Subtract the elements sum from natural numbers sum i.e. n*(n+1)/2 - (sum of array elements). Thus the resultant value will be our required missing number.</li>
</ul>

```String_01.py```: <strong>Reverse words in a given string</strong> (Ref: https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string/0) <br>
<ul>
<li>first create list of string separate by ' . ' <br>
  ["i", "like", "this", "program", "very", "much"] </li>
<li>Iterate over last to second list only followed by ' . ' <br>
  much.very.program.this.like </li>
<li>Append the first list of string without followed by ' . ' and display output<br>
  much.very.program.this.like.i </li>
