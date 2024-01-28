## Search algorithms comparison

**Search algorithms selected for comparison:**

 - Boyer-Moore search
 - Knuth-Morris-Pratt search
 - Rabin-Karp search

**Test strategy:** 
Measuring the time needed to find given substring in the text. Two substring are used: one is existing wich means that search will be interrupted somewhere in the middle, another substring is fake which means that whole article need to be scanned.

**Test results:** 
| Algorithm| Substring | Execution time, sec |
| ------ | ---------- | ---------- |
|**Boyer-Moore search**|Existing substring | 0.00180
|**Knuth-Morris-Pratt search**|Existing substring |0.00587
|**Rabin-Karp search**|Existing substring |0.01138
|**Boyer-Moore search**|Fake substring | 0.00581
|**Knuth-Morris-Pratt search**|Fake substring |0.01638
|**Rabin-Karp search**|Fake substring |0.03957

**Conclusions:**
As can be seen from the provided testing results, we have undeniable leader. **Boyer-Moore search algorithm** is the fastest serch algorithm from the list of propsed, it shows the best results in all tests. The algorithm couple times faster (5 times faster in test case with existing substring and 3 times faster with fake substring test) than it closest opponent.