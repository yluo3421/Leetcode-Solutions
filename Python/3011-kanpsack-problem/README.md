<p>
  You're given an array of arrays where each subarray holds two integer values
  and represents an item; the first integer is the item's value, and the second
  integer is the item's weight. You're also given an integer representing the
  maximum capacity of a knapsack that you have.
</p>
<p>
  Your goal is to fit items in your knapsack without having the sum of their
  weights exceed the knapsack's capacity, all the while maximizing their
  combined value. Note that you only have one of each item at your disposal.
</p>
<p>
  Write a function that returns the maximized combined value of the items that
  you should pick as well as an array of the indices of each item picked.
</p>
<p>
  If there are multiple combinations of items that maximize the total value in
  the knapsack, your function can return any of them.
</p>
<h3>Sample Input</h3>
<pre>
    <span class="CodeEditor-promptParameter">items</span> = [[1, 2], [4, 3], [5, 6], [6, 7]]
    <span class="CodeEditor-promptParameter">capacity</span> = 10
</pre>
    <pre>[10, [1, 3]] <span class="CodeEditor-promptComment"></span>// items [4, 3] and [6, 7]
</pre>