# Date: 2021.10.30 
# Author: evan

# class ListNode:
# 	def __init__(self, x):
# 		self.val = x
# 		self.next = None
		
class Solution:

	def reverseList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		cur, prev = head, None
		while cur:
			cur.next, prev, cur = prev, cur, cur.next
		return prev
