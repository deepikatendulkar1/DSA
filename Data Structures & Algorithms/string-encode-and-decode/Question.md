# Encode and Decode Strings

## Problem

Design an algorithm to encode a list of strings into a single string and then decode it back to the original list.

The encoded string is sent over a network and should be decoded correctly on the receiver side.

---

## Examples

**Example 1**

**Input**

["Hello","World"]


**Output**

["Hello","World"]


**Explanation**

**Machine 1 (Sender):**

Codec encoder = new Codec();
String msg = encoder.encode(strs);


Machine 1 sends:

--- msg --->


**Machine 2 (Receiver):**

Codec decoder = new Codec();
String[] strs = decoder.decode(msg);


The decoded output matches the original input.

**Example 2**

Input: [""]
Output: [""]


---

## Constraints

- 0 <= strs.length < 100  
- 0 <= strs[i].length < 200  
- Strings can contain any of the 256 ASCII characters  



---
