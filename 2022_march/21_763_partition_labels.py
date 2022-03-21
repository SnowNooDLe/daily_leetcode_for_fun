"""
763. Partition Labels

You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.


Example 1:
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

Example 2:
Input: s = "eccbbbbdec"
Output: [10]
"""
from typing import List


def partitionLabels(s: str) -> List[int]:
    """Runtime 64ms, Memory 14MB
    Used the following link to understand the question - https://youtu.be/B7m8UmZE-vw
    As I couldn't exactly figure out what the question was asking me for
    """
    # To get the last index of char seen in the given string s
    last_char_index = {}
    for idx, char in enumerate(s):
        last_char_index[char] = idx

    results = []
    count = 1
    end_cur_partition = 0
    """
    Idea is from the very first character, it is likely to be occurred multiple times but if so, they all have to be in
    the same partition, hence from the first char, we are going the loop over string by index and value,
    while iterating, checks the last seen index for the current index's value as they all need to be in the same partition
    and once the current index of S hits the last seen index from last_char_index, they are one partition with length of
    N, hence add this N to the results and move on to the new partition.
    Better explanation is in the video I watched.
    """
    for idx, char in enumerate(s):
        end_cur_partition = max(end_cur_partition, last_char_index[char])
        if idx < end_cur_partition:
            count += 1
        else:
            results.append(count)
            count = 1
            end_cur_partition = 0

    return results


print(partitionLabels("ababcbacadefegdehijhklij"))
print(partitionLabels("eccbbbbdec"))
