# SLOW AND FAST POINTER ALGORITHM
from typing import List, Optional

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

def hasCycle(head: Optional[ListNode]) -> bool:
