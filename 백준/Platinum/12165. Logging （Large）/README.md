# [Platinum II] Logging (Large) - 12165 

[문제 링크](https://www.acmicpc.net/problem/12165) 

### 성능 요약

메모리: 2576 KB, 시간: 3976 ms

### 분류

정렬, 기하학, 두 포인터, 각도 정렬

### 제출 일자

2025년 12월 17일 16:50:19

### 문제 설명

<p>A certain forest consists of <strong>N</strong> trees, each of which is inhabited by a squirrel.</p>

<p>The <strong>boundary</strong> of the forest is the convex polygon of smallest area which contains every tree, as if a giant rubber band had been stretched around the outside of the forest.</p>

<p>Formally, every tree is a single point in two-dimensional space with unique coordinates (<strong>X<sub>i</sub></strong>, <strong>Y<sub>i</sub></strong>), and the boundary is the convex hull of those points.</p>

<p>Some trees are <strong>on the boundary</strong> of the forest, which means they are on an edge or a corner of the polygon. The squirrels wonder how close their trees are to being on the boundary of the forest.</p>

<p>One at a time, each squirrel climbs down from its tree, examines the forest, and determines the minimum number of trees that would need to be cut down for its own tree to be on the boundary. It then writes that number down on a log.</p>

<p>Determine the list of numbers written on the log.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow; each consists of a single line with an integer <strong>N</strong>, the number of trees, followed by <strong>N</strong> lines with two space-separated integers <strong>X<sub>i</sub></strong> and <strong>Y<sub>i</sub></strong>, the coordinates of each tree. No two trees will have the same coordinates.</p>

<h3>Limits</h3>

<ul>
	<li>-10<sup>6</sup> ≤ <strong>X<sub>i</sub></strong>, <strong>Y<sub>i</sub></strong> ≤ 10<sup>6</sup>.</li>
	<li>1 ≤ <strong>T</strong> ≤ 14.</li>
	<li>1 ≤ <strong>N</strong> ≤ 3000.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x:", followed by <strong>N</strong> lines with one integer each, where line <strong>i</strong> contains the number of trees that the squirrel living in tree <strong>i</strong>would need to cut down.</p>

