<h2><a href="">3001. Degree of Friendship</a></h2><h3>Medium</h3><hr><div>
<p>
<em>We're building a new social network where users are friends with one another. In order to make better friend recommendations, we want to develop a "friend distance" algorithm.</em>

Write a function <code>friend_distance(friends, userA, userB)</code> that returns the minimum distance between two users (similar to the "degree" of connection on LinkedIn).

The input to your function will be a 2D array <code>friends</code>, where each entry (A, B) contains the friendship status between user A and user B.
</p>
<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> friends = [[0 1 0],
                  [1 0 1],
                  [0 1 0]]
<strong>Output:</strong> friend_distance(friends, 0, 1) # => 1
</pre>



<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 10</code></li>
	<li><code>-100 &lt;= matrix[i][j] &lt;= 100</code></li>
</ul>
</div>