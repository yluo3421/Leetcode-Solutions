<h1>116 · Jump Game</h1>
<div data-h5="false" class="problem-description-content-niBfd problem-detail-bottom-LKDTq"><div data-h5="false" class="content-wrapper-bgslg"><div class="sub-title-D4Ea3 with-action-U2Xi7">Description</div><div class="react-markdown react-markdown-xncmA"><p>Given an array of non-negative integers, you are initially positioned at the first index of the array.</p>
<p>Each element in the array represents your maximum jump length at that position.</p>
<p>Determine if you are able to reach the last index.</p></div><div data-show="true" class="ant-alert ant-alert-info ant-alert-with-description ant-alert-no-icon connection-pXLnw" role="alert" style="margin-bottom: 16px;"><div class="ant-alert-content"><div class="ant-alert-description"><div class="react-markdown react-markdown-xncmA"><p>Wechat reply  【Google】 get the latest requent Interview questions. (wechat id : <strong>jiuzhang1104</strong>)</p></div></div></div><button type="button" class="ant-alert-close-icon" tabindex="0"><span role="img" aria-label="close" class="anticon anticon-close"><svg viewBox="64 64 896 896" focusable="false" data-icon="close" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M563.8 512l262.5-312.9c4.4-5.2.7-13.1-6.1-13.1h-79.8c-4.7 0-9.2 2.1-12.3 5.7L511.6 449.8 295.1 191.7c-3-3.6-7.5-5.7-12.3-5.7H203c-6.8 0-10.5 7.9-6.1 13.1L459.4 512 196.9 824.9A7.95 7.95 0 00203 838h79.8c4.7 0 9.2-2.1 12.3-5.7l216.5-258.1 216.5 258.1c3 3.6 7.5 5.7 12.3 5.7h79.8c6.8 0 10.5-7.9 6.1-13.1L563.8 512z"></path></svg></span></button></div><div data-show="true" class="ant-alert ant-alert-info ant-alert-with-description notice-tn1L9" role="alert"><span role="img" aria-label="info-circle" class="anticon anticon-info-circle ant-alert-icon"><svg viewBox="64 64 896 896" focusable="false" data-icon="info-circle" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M512 64C264.6 64 64 264.6 64 512s200.6 448 448 448 448-200.6 448-448S759.4 64 512 64zm0 820c-205.4 0-372-166.6-372-372s166.6-372 372-372 372 166.6 372 372-166.6 372-372 372z"></path><path d="M464 336a48 48 0 1096 0 48 48 0 10-96 0zm72 112h-48c-4.4 0-8 3.6-8 8v272c0 4.4 3.6 8 8 8h48c4.4 0 8-3.6 8-8V456c0-4.4-3.6-8-8-8z"></path></svg></span><div class="ant-alert-content"><div class="ant-alert-description"><div class="react-markdown react-markdown-xncmA"><p>The array <code>A</code> contains 𝑛 integers 𝑎1, 𝑎2, …, 𝑎𝑛 (1≤𝑎𝑖≤5000) (1≤n≤5000 )</p></div></div></div></div></div><div data-h5="false" class="content-wrapper-bgslg"><div class="sub-title-D4Ea3">Example</div><div class="react-markdown react-markdown-xncmA"><p><strong>Example 1:</strong></p>
<p>Input:</p>
<pre><div class="markdown-thumbnail-wrapper" style="height: auto; max-height: unset;"><div class="lc-code-wrapper"><pre style="display: block; overflow-x: auto; background: rgb(43, 43, 43); color: rgb(248, 248, 242); padding: 0.5em;"><code style="white-space: pre;"><span>A = [</span><span style="color: rgb(245, 171, 53);">2</span><span>,</span><span style="color: rgb(245, 171, 53);">3</span><span>,</span><span style="color: rgb(245, 171, 53);">1</span><span>,</span><span style="color: rgb(245, 171, 53);">1</span><span>,</span><span style="color: rgb(245, 171, 53);">4</span><span>]</span></code></pre><div class="code-block-buttons"><span title="Copy Code" class="code-block-copy-button"><span role="img" aria-label="copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" data-icon="copy" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></span></span></div></div></div></pre>
<p>Output:</p>
<pre><div class="markdown-thumbnail-wrapper" style="height: auto; max-height: unset;"><div class="lc-code-wrapper"><pre style="display: block; overflow-x: auto; background: rgb(43, 43, 43); color: rgb(248, 248, 242); padding: 0.5em;"><code style="white-space: pre;"><span style="color: rgb(245, 171, 53);">true</span></code></pre><div class="code-block-buttons"><span title="Copy Code" class="code-block-copy-button"><span role="img" aria-label="copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" data-icon="copy" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></span></span></div></div></div></pre>
<p>Explanation:</p>
<p>0 -&gt; 1 -&gt; 4 (the number here is subscript) is a reasonable scheme.</p>
<p><strong>Example 2:</strong></p>
<p>Input:</p>
<pre><div class="markdown-thumbnail-wrapper" style="height: auto; max-height: unset;"><div class="lc-code-wrapper"><pre style="display: block; overflow-x: auto; background: rgb(43, 43, 43); color: rgb(248, 248, 242); padding: 0.5em;"><code style="white-space: pre;"><span>A = [</span><span style="color: rgb(245, 171, 53);">3</span><span>,</span><span style="color: rgb(245, 171, 53);">2</span><span>,</span><span style="color: rgb(245, 171, 53);">1</span><span>,</span><span style="color: rgb(245, 171, 53);">0</span><span>,</span><span style="color: rgb(245, 171, 53);">4</span><span>]</span></code></pre><div class="code-block-buttons"><span title="Copy Code" class="code-block-copy-button"><span role="img" aria-label="copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" data-icon="copy" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></span></span></div></div></div></pre>
<p>Output:</p>
<pre><div class="markdown-thumbnail-wrapper" style="height: auto; max-height: unset;"><div class="lc-code-wrapper"><pre style="display: block; overflow-x: auto; background: rgb(43, 43, 43); color: rgb(248, 248, 242); padding: 0.5em;"><code style="white-space: pre;"><span style="color: rgb(245, 171, 53);">false</span></code></pre><div class="code-block-buttons"><span title="Copy Code" class="code-block-copy-button"><span role="img" aria-label="copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" data-icon="copy" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></span></span></div></div></div></pre>
<p>Explanation:</p>
<p>There is no solution that can reach the end.</p></div></div><div data-h5="false" class="content-wrapper-bgslg"><div class="sub-title-D4Ea3">Challenge</div><div class="react-markdown react-markdown-xncmA"><p>This problem have two method which is <code>Greedy</code> and <code>Dynamic Programming</code>.</p>
<p>The time complexity of <code>Greedy</code> method is <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>O</mi><mo stretchy="false">(</mo><mi>n</mi><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">O(n)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="mord mathnormal" style="margin-right: 0.02778em;">O</span><span class="mopen">(</span><span class="mord mathnormal">n</span><span class="mclose">)</span></span></span></span></span>.</p>
<p>The time complexity of <code>Dynamic</code> Programming method is <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>O</mi><mo stretchy="false">(</mo><msup><mi>n</mi><mn>2</mn></msup><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">O(n^2)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1.0641em; vertical-align: -0.25em;"></span><span class="mord mathnormal" style="margin-right: 0.02778em;">O</span><span class="mopen">(</span><span class="mord"><span class="mord mathnormal">n</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height: 0.8141em;"><span style="top: -3.063em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span><span class="mclose">)</span></span></span></span></span>.</p>
<p>We manually set the small data set to allow you pass the test in both ways. This is just to let you learn how to use this problem in dynamic programming ways. If you finish it in dynamic programming ways, you can try greedy method to make it accept again.</p></div></div></div>