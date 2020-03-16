# Description of filename
<hr>

```Array_01.py```: Subarray with given sum (Ref: https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0) <br>
<ul>
<li>Maintain start and last index to store and print these values </li>
<li>Iterate the complete array.</li>
<li>Add array elements to cuursum</li>
<li>If currsum becomes greater than S, then remove elements starting from start index, till it become less than or equal to S, and increement start.</li>
<li>if currsum becomes equals to S, then print the starting and last index</li>
<li>if the currsum never maches to S, then print -1</li>
</ul>
